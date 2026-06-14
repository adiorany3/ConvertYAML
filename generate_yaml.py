from __future__ import annotations

import os
import socket
import subprocess
import tempfile
import time
from contextlib import suppress
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlparse, urlunparse

import base64
import json
import yaml
import requests

from sumberyaml_core import (
    ALT_TEST_URL,
    DEFAULT_LINKS,
    TARGET_SERVER,
    ONLY_PORT,
    b64decode_text,
    build_akun_txt,
    build_csv,
    build_openclash_android_yaml,
    build_openclash_yaml,
    extract_uris,
    node_network,
    normalize_name,
    parse_uri,
    process_sources,
    provider_label_from_original_server,
    safe_proxy_name,
    unique_names,
)


def _read_text_file(path: str) -> str:
    file_path = Path(path)
    if not file_path.exists():
        return ""
    return file_path.read_text(encoding="utf-8", errors="ignore")


def _env_int(name: str, default: int) -> int:
    value = os.getenv(name, "").strip()
    if not value:
        return default
    try:
        return int(value)
    except ValueError:
        print(f"[WARN] {name}={value!r} tidak valid, pakai default {default}.")
        return default


def _env_float(name: str, default: float) -> float:
    value = os.getenv(name, "").strip()
    if not value:
        return default
    try:
        return float(value)
    except ValueError:
        print(f"[WARN] {name}={value!r} tidak valid, pakai default {default}.")
        return default


def _env_bool(name: str, default: bool) -> bool:
    value = os.getenv(name, "").strip().lower()
    if not value:
        return default
    return value in {"1", "true", "yes", "y", "on", "aktif"}


def build_links_text() -> str:
    links = list(DEFAULT_LINKS)
    extra_file = os.getenv("SUBSCRIPTION_LINKS_FILE", "subscription_links.txt")
    extra_text = _read_text_file(extra_file)
    extra_env = os.getenv("EXTRA_SUBSCRIPTION_LINKS", "")
    for source in (extra_text, extra_env):
        for line in source.splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                links.append(line)
    unique: list[str] = []
    seen: set[str] = set()
    for link in links:
        if link not in seen:
            seen.add(link)
            unique.append(link)
    return "\n".join(unique)



def normalize_manual_uri_server(raw: str, target_server: str = TARGET_SERVER) -> str:
    """Return manual URI with its outbound server changed to the bug server.

    This is intentionally done before manual nodes are parsed, so manual_nodes.txt
    itself can be normalized and committed by GitHub Actions. SNI/Host/path and
    credentials are preserved; only the connect server and port are changed to
    104.17.3.81:443.
    """
    raw = str(raw or "").strip()
    if not raw or "://" not in raw:
        return raw
    scheme = raw.split("://", 1)[0].lower()
    try:
        if scheme == "vmess":
            payload = raw.split("://", 1)[1].split("#", 1)[0]
            decoded = b64decode_text(payload)
            if not decoded:
                return raw
            data = json.loads(decoded)
            data["add"] = str(target_server)
            if "server" in data:
                data["server"] = str(target_server)
            data["port"] = str(ONLY_PORT)
            encoded = base64.b64encode(
                json.dumps(data, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
            ).decode("ascii")
            return "vmess://" + encoded

        body, hash_sep, fragment = raw.partition("#")
        parsed = urlparse(body)
        if not parsed.netloc:
            return raw
        if "@" in parsed.netloc:
            userinfo, _serverpart = parsed.netloc.rsplit("@", 1)
            netloc = f"{userinfo}@{target_server}:{ONLY_PORT}"
        else:
            # Do not rewrite fully base64 ss:// payloads because changing the
            # server safely requires decoding all cipher/password forms.
            if scheme == "ss":
                return raw
            netloc = f"{target_server}:{ONLY_PORT}"
        new_body = urlunparse((parsed.scheme, netloc, parsed.path, parsed.params, parsed.query, ""))
        return new_body + (("#" + fragment) if hash_sep else "")
    except Exception:
        return raw


def normalize_manual_nodes_text(manual_text: str) -> tuple[str, int]:
    """Normalize every supported URI in manual_nodes.txt to TARGET_SERVER:443.

    Comments and blank lines are preserved when a line only contains comments or
    text. URI lines are rewritten as one URI per line to avoid leaving stale
    original servers in the repository.
    """
    out: list[str] = []
    changed = 0
    for line in (manual_text or "").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            out.append(line)
            continue
        uris = extract_uris(line)
        if not uris:
            out.append(line)
            continue
        for uri in uris:
            fixed = normalize_manual_uri_server(uri)
            if fixed != uri:
                changed += 1
            out.append(fixed)
    return "\n".join(out) + ("\n" if out else ""), changed


def _unique_manual_names(nodes: list[Any]) -> None:
    """Keep manual node names from source and only add MANUAL prefix.

    Example:
      source fragment: Singapore-VIP
      YAML name      : MANUAL-Singapore-VIP

    Manual nodes are intentionally not strict-filtered or tested. This function
    only ensures the final YAML proxy names stay unique, because OpenClash/Mihomo
    requires every proxy name to be unique and proxy-groups must reference the
    exact same names.
    """
    seen: set[str] = set()
    for i, node in enumerate(nodes, start=1):
        source_name = normalize_name(node.name, f"NODE-{i:03d}")
        node.original_name = node.original_name or source_name

        # Keep the user's/source fragment as much as possible. Only add MANUAL-
        # in front. Do not convert to provider/ASN naming for manual nodes.
        base_raw = f"MANUAL-{source_name}"
        base = normalize_name(base_raw, f"MANUAL-NODE-{i:03d}")
        base = base[:96].strip(" -_|/") or f"MANUAL-NODE-{i:03d}"

        name = base
        counter = 2
        while name in seen:
            suffix = f"-{counter}"
            name = (base[: 96 - len(suffix)] + suffix).strip(" -_|/")
            counter += 1

        seen.add(name)
        node.name = name
        node.clash["name"] = name
        node.status = "manual-unfiltered"
        node.tier = "MANUAL"
        node.reason = "manual_nodes.txt: added without strict filtering/testing; name kept from source with MANUAL prefix"

def parse_manual_nodes_unscreened(manual_text: str) -> tuple[list[Any], list[str]]:
    """Parse manual_nodes.txt and do not run strict SNI/WS filtering on it.

    This still requires the URI to be syntactically supported by the parser
    (vless/vmess/trojan/ss and the app's bug-server format), but it does not run
    the automatic subscription filters, WS strict test, timeout test, SNI strict
    selection, jitter filter, or quota limit.
    """
    nodes: list[Any] = []
    skipped: list[str] = []
    seen_keys: set[str] = set()
    for uri in extract_uris(manual_text or ""):
        node = parse_uri(uri, "manual_nodes.txt")
        if not node:
            skipped.append(uri[:180])
            continue
        # Do not filter strict. Only dedupe exact same parsed account so repeated
        # copy-paste lines do not break YAML with duplicates.
        key = node.key or uri
        if key in seen_keys:
            continue
        seen_keys.add(key)
        nodes.append(node)
    _unique_manual_names(nodes)
    return nodes, skipped


def _insert_once(values: list[str], item: str, index: int | None = None) -> None:
    if item in values:
        return
    if index is None or index < 0 or index > len(values):
        values.append(item)
    else:
        values.insert(index, item)


def add_manual_group_to_config(config: dict[str, Any], manual_nodes: list[Any], *, android: bool = False) -> dict[str, Any]:
    if not manual_nodes:
        return config

    manual_names = [str(node.clash.get("name") or node.name) for node in manual_nodes if node.clash.get("name")]
    if not manual_names:
        return config

    proxies = config.setdefault("proxies", [])
    existing_proxy_names = {str(p.get("name")) for p in proxies if isinstance(p, dict)}
    for node in manual_nodes:
        clash = node.clash
        name = str(clash.get("name") or "")
        if name and name not in existing_proxy_names:
            proxies.append(clash)
            existing_proxy_names.add(name)

    groups = config.setdefault("proxy-groups", [])
    # Remove previous MANUAL group when regenerating from an existing config.
    groups[:] = [g for g in groups if not (isinstance(g, dict) and g.get("name") == "MANUAL")]

    manual_group = {
        "name": "MANUAL",
        "type": "select",
        "proxies": manual_names + ["DIRECT"],
    }

    # Manual nodes remain outside the automatic 20-node quota. However, the
    # FALLBACK group intentionally starts with MANUAL so manually curated nodes
    # are tried first, then the strict automatic nodes continue after it.
    for group in groups:
        if not isinstance(group, dict):
            continue
        name = str(group.get("name") or "")
        proxies_list = group.get("proxies")
        if not isinstance(proxies_list, list):
            continue
        if name == "FALLBACK":
            # Required layout: FALLBACK -> MANUAL -> auto account nodes.
            # Do not append individual manual nodes here; the MANUAL select group
            # keeps manual accounts separated and does not reduce the 20 auto nodes.
            _insert_once(proxies_list, "MANUAL", 0)
        elif name == "GLOBAL":
            # Keep MANUAL visible in the main selector too.
            if "DIRECT" in proxies_list:
                _insert_once(proxies_list, "MANUAL", proxies_list.index("DIRECT") + 1)
            elif "FALLBACK" in proxies_list:
                _insert_once(proxies_list, "MANUAL", proxies_list.index("FALLBACK") + 1)
            else:
                _insert_once(proxies_list, "MANUAL", 0)
        elif (not android) and name == "PROXY":
            if "DIRECT" in proxies_list:
                _insert_once(proxies_list, "MANUAL", proxies_list.index("DIRECT") + 1)
            else:
                _insert_once(proxies_list, "MANUAL", 1)

    groups.append(manual_group)
    return config



def _free_tcp_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def _expected_statuses() -> set[int]:
    raw = os.getenv("REAL_CHECK_EXPECTED_STATUS", "204,200,301,302").strip()
    statuses: set[int] = set()
    for part in raw.split(","):
        part = part.strip()
        if not part:
            continue
        try:
            statuses.add(int(part))
        except ValueError:
            pass
    return statuses or {204, 200, 301, 302}


def _wait_controller(controller_url: str, timeout_s: float = 8.0) -> bool:
    deadline = time.time() + max(1.0, timeout_s)
    while time.time() < deadline:
        try:
            response = requests.get(controller_url + "/proxies", timeout=0.5)
            if response.status_code < 500:
                return True
        except Exception:
            time.sleep(0.2)
    return False


def _mihomo_real_check_nodes(nodes: list[Any], *, limit: int, test_url: str, timeout_ms: int) -> tuple[list[Any], int, str]:
    """Run a real proxy health check through Mihomo for automatic nodes only.

    WS Upgrade 101 proves the Cloudflare WS endpoint exists, but it still does
    not prove VLESS/VMess/Trojan can forward traffic. This check starts Mihomo,
    selects every automatic node one by one, then requests generate_204 through
    the local mixed-port. Manual nodes are intentionally not passed here.
    """
    if not nodes:
        return [], 0, "no auto nodes to test"

    if not _env_bool("REAL_CHECK", True):
        final_nodes = nodes[:limit]
        for node in final_nodes:
            node.real_check_status = "skipped-disabled"
            node.real_check_success = True
        return final_nodes, len(final_nodes), "real check disabled"

    core_path = os.getenv("MIHOMO_PATH", "./mihomo").strip() or "./mihomo"
    if not Path(core_path).exists():
        final_nodes = nodes[:limit]
        for node in final_nodes:
            node.real_check_status = "skipped-mihomo-not-found"
            node.real_check_success = True
        return final_nodes, len(final_nodes), f"mihomo not found at {core_path}; fallback to strict WS list"

    expected = _expected_statuses()
    proxy_port = _free_tcp_port()
    controller_port = _free_tcp_port()
    names = [str(node.clash.get("name") or node.name) for node in nodes if node.clash.get("name")]
    if not names:
        return [], 0, "no usable proxy names"

    tmpdir_obj = tempfile.TemporaryDirectory(prefix="mihomo-realcheck-")
    tmpdir = Path(tmpdir_obj.name)
    config_path = tmpdir / "config.yaml"
    config = {
        "mixed-port": proxy_port,
        "allow-lan": False,
        "bind-address": "127.0.0.1",
        "mode": "global",
        "log-level": os.getenv("MIHOMO_LOG_LEVEL", "error"),
        "ipv6": False,
        "unified-delay": True,
        "tcp-concurrent": True,
        "global-client-fingerprint": "chrome",
        "external-controller": f"127.0.0.1:{controller_port}",
        "dns": {
            "enable": True,
            "ipv6": False,
            "listen": "127.0.0.1:0",
            "enhanced-mode": "fake-ip",
            "fake-ip-range": "198.18.0.1/16",
            "default-nameserver": ["1.1.1.1", "8.8.8.8"],
            "nameserver": ["https://1.1.1.1/dns-query", "https://dns.google/dns-query"],
        },
        "proxies": [node.clash for node in nodes],
        "proxy-groups": [
            {"name": "GLOBAL", "type": "select", "proxies": names},
        ],
        "rules": ["MATCH,GLOBAL"],
    }
    config_path.write_text(yaml.safe_dump(config, allow_unicode=True, sort_keys=False, width=140), encoding="utf-8")

    proc: subprocess.Popen[str] | None = None
    passed: list[Any] = []
    checked = 0
    reason = "ok"
    try:
        proc = subprocess.Popen(
            [core_path, "-d", str(tmpdir), "-f", str(config_path)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            text=True,
        )
        controller_url = f"http://127.0.0.1:{controller_port}"
        if not _wait_controller(controller_url, timeout_s=float(os.getenv("MIHOMO_START_TIMEOUT", "10"))):
            reason = "mihomo controller did not start"
            for node in nodes:
                node.real_check_status = "mihomo-start-failed"
            return nodes[:limit], 0, reason

        proxy_url = f"http://127.0.0.1:{proxy_port}"
        request_timeout = max(1.0, float(timeout_ms) / 1000.0)
        settle_s = float(os.getenv("REAL_CHECK_SETTLE_SECONDS", "0.15"))
        for node in nodes:
            if len(passed) >= limit:
                break
            name = str(node.clash.get("name") or node.name)
            checked += 1
            start = time.perf_counter()
            try:
                switch = requests.put(controller_url + "/proxies/GLOBAL", json={"name": name}, timeout=1.5)
                if switch.status_code >= 400:
                    node.real_check_status = f"switch-{switch.status_code}"
                    node.real_check_success = False
                    node.status = "dead"
                    node.reason = (node.reason + "; real check switch failed").strip("; ")
                    continue
                time.sleep(settle_s)
                # Jangan percaya satu kali sukses saja. Banyak akun publik bisa
                # lolos sesaat, tetapi gagal handshake saat dites di OpenClash.
                real_attempts = max(1, int(os.getenv("REAL_CHECK_ATTEMPTS", "3")))
                real_required = max(1, min(real_attempts, int(os.getenv("REAL_CHECK_REQUIRE_SUCCESSES", "2"))))
                real_gap_s = max(0.0, float(os.getenv("REAL_CHECK_GAP_SECONDS", "0.25")))
                ok_count = 0
                last_status = ""
                best_real_ms: int | None = None
                for real_i in range(real_attempts):
                    req_start = time.perf_counter()
                    try:
                        response = requests.get(
                            test_url,
                            proxies={"http": proxy_url, "https": proxy_url},
                            timeout=request_timeout,
                            allow_redirects=False,
                            headers={"User-Agent": "Mozilla/5.0 SumberYAML-RealCheck/1.0"},
                        )
                        req_elapsed = int((time.perf_counter() - req_start) * 1000)
                        best_real_ms = req_elapsed if best_real_ms is None else min(best_real_ms, req_elapsed)
                        last_status = f"HTTP {response.status_code}"
                        if response.status_code in expected:
                            ok_count += 1
                    except Exception as exc:
                        last_status = type(exc).__name__
                    if real_i + 1 < real_attempts and real_gap_s:
                        time.sleep(real_gap_s)

                elapsed = int((time.perf_counter() - start) * 1000)
                node.real_check_ms = best_real_ms if best_real_ms is not None else elapsed
                node.real_check_status = f"{last_status}; success {ok_count}/{real_attempts}"
                if ok_count >= real_required:
                    node.real_check_success = True
                    node.status = "alive"
                    node.reason = (node.reason + f"; real proxy check ok {ok_count}/{real_attempts}").strip("; ")
                    passed.append(node)
                else:
                    node.real_check_success = False
                    node.status = "dead"
                    node.reason = (node.reason + f"; real proxy check gagal {ok_count}/{real_attempts}").strip("; ")
            except Exception as exc:
                node.real_check_success = False
                node.real_check_status = type(exc).__name__
                node.status = "dead"
                node.reason = (node.reason + "; real proxy check failed: " + str(exc)[:100]).strip("; ")

        reason = f"real check passed {len(passed)}/{checked} tested"
        return passed, checked, reason
    finally:
        if proc is not None:
            with suppress(Exception):
                proc.terminate()
            with suppress(Exception):
                proc.wait(timeout=3)
            if proc.poll() is None:
                with suppress(Exception):
                    proc.kill()
        tmpdir_obj.cleanup()



class _NoAliasSafeDumper(yaml.SafeDumper):
    """PyYAML dumper that avoids anchors (&id001 / *id001).

    Some OpenClash/Android importers can parse YAML anchors, but removing anchors
    makes the generated files more portable and easier to read.
    """

    def ignore_aliases(self, data: Any) -> bool:  # type: ignore[override]
        return True


def dump_yaml_no_alias(config: dict[str, Any]) -> str:
    # JSON round-trip removes shared list references that PyYAML would otherwise
    # serialize as anchors. The OpenClash config only contains JSON-compatible types.
    clean = json.loads(json.dumps(config, ensure_ascii=False))
    return yaml.dump(clean, Dumper=_NoAliasSafeDumper, allow_unicode=True, sort_keys=False, width=140)


def finalize_yaml_for_openclash(yaml_text: str) -> str:
    config = yaml.safe_load(yaml_text) or {}
    if not isinstance(config, dict):
        raise ValueError("YAML root must be a mapping/dictionary")
    return dump_yaml_no_alias(config)


def _as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _rule_target(rule: str) -> str:
    parts = [p.strip() for p in str(rule).split(",")]
    if not parts:
        return ""
    if parts[-1].lower() == "no-resolve" and len(parts) >= 2:
        return parts[-2]
    return parts[-1]


def validate_openclash_compatibility(yaml_text: str, label: str, *, android: bool = False) -> tuple[list[str], list[str]]:
    """Validate generated YAML before commit.

    This is a structural compatibility check for OpenClash/Mihomo import:
    - YAML can be parsed.
    - proxy names are unique.
    - proxy-groups only reference existing proxies/groups or built-in policies.
    - RULE-SET rules reference existing rule-providers.
    - Android output stays lightweight and rule-free.
    - WS proxy fields are syntactically complete enough for Mihomo/OpenClash.
    """
    errors: list[str] = []
    warnings: list[str] = []
    try:
        config = yaml.safe_load(yaml_text) or {}
    except Exception as exc:
        return [f"{label}: YAML parse failed: {exc}"], []

    if not isinstance(config, dict):
        return [f"{label}: YAML root is not a mapping"], []

    if "&id" in yaml_text or "*id" in yaml_text:
        errors.append(f"{label}: YAML still contains anchors/aliases (&id/*id); regenerate with no-alias dumper")

    proxies = config.get("proxies")
    if not isinstance(proxies, list):
        errors.append(f"{label}: missing or invalid proxies list")
        proxies = []
    groups = config.get("proxy-groups")
    if not isinstance(groups, list):
        errors.append(f"{label}: missing or invalid proxy-groups list")
        groups = []

    proxy_names: list[str] = []
    seen_proxy: set[str] = set()
    allowed_types = {"vless", "vmess", "trojan", "ss", "http", "socks5", "socks", "hysteria2", "tuic"}
    for idx, proxy in enumerate(proxies):
        if not isinstance(proxy, dict):
            errors.append(f"{label}: proxy #{idx + 1} is not a mapping")
            continue
        name = str(proxy.get("name") or "").strip()
        ptype = str(proxy.get("type") or "").strip().lower()
        if not name:
            errors.append(f"{label}: proxy #{idx + 1} has empty name")
            continue
        if name in seen_proxy:
            errors.append(f"{label}: duplicate proxy name: {name}")
        seen_proxy.add(name)
        proxy_names.append(name)
        if ptype not in allowed_types:
            errors.append(f"{label}: proxy {name} has unsupported/empty type: {ptype!r}")
        if not proxy.get("server"):
            errors.append(f"{label}: proxy {name} missing server")
        try:
            port = int(proxy.get("port"))
            if port <= 0 or port > 65535:
                errors.append(f"{label}: proxy {name} invalid port: {proxy.get('port')!r}")
        except Exception:
            errors.append(f"{label}: proxy {name} invalid/missing port: {proxy.get('port')!r}")

        network = str(proxy.get("network") or "tcp").lower()
        if network == "ws" and ptype in {"vless", "vmess", "trojan"}:
            ws_opts = proxy.get("ws-opts")
            if not isinstance(ws_opts, dict):
                errors.append(f"{label}: WS proxy {name} missing ws-opts")
            else:
                if not str(ws_opts.get("path") or "").strip():
                    errors.append(f"{label}: WS proxy {name} missing ws-opts.path")
                headers = ws_opts.get("headers")
                host = ""
                if isinstance(headers, dict):
                    host = str(headers.get("Host") or headers.get("host") or "").strip()
                if not host:
                    warnings.append(f"{label}: WS proxy {name} has no ws-opts.headers.Host")
            sni = str(proxy.get("servername") or proxy.get("sni") or "").strip()
            # Manual nodes are allowed unfiltered, so missing SNI is a warning, not a hard error.
            if not sni:
                warnings.append(f"{label}: WS proxy {name} has no servername/sni; may import but can timeout")
            alpn = [str(x).lower() for x in _as_list(proxy.get("alpn"))]
            if alpn and "http/1.1" not in alpn:
                warnings.append(f"{label}: WS proxy {name} alpn does not include http/1.1")

    group_names: list[str] = []
    seen_group: set[str] = set()
    for idx, group in enumerate(groups):
        if not isinstance(group, dict):
            errors.append(f"{label}: proxy-group #{idx + 1} is not a mapping")
            continue
        name = str(group.get("name") or "").strip()
        if not name:
            errors.append(f"{label}: proxy-group #{idx + 1} has empty name")
            continue
        if name in seen_group:
            errors.append(f"{label}: duplicate proxy-group name: {name}")
        seen_group.add(name)
        group_names.append(name)
        refs = group.get("proxies")
        if refs is not None and not isinstance(refs, list):
            errors.append(f"{label}: group {name} proxies must be a list")

    valid_refs = set(proxy_names) | set(group_names) | {"DIRECT", "REJECT", "REJECT-DROP", "PASS", "COMPATIBLE"}
    for group in groups:
        if not isinstance(group, dict):
            continue
        name = str(group.get("name") or "")
        refs = group.get("proxies")
        if not isinstance(refs, list):
            continue
        if not refs:
            errors.append(f"{label}: group {name} has empty proxies list")
        for ref in refs:
            ref_text = str(ref)
            if ref_text not in valid_refs:
                errors.append(f"{label}: group {name} references missing proxy/group: {ref_text}")

    if android:
        for forbidden in ("rule-providers", "redir-port", "tproxy-port"):
            if forbidden in config:
                errors.append(f"{label}: Android config must not contain {forbidden}")
        if config.get("mode") != "global":
            warnings.append(f"{label}: Android config mode is {config.get('mode')!r}, expected 'global'")
    else:
        rules = config.get("rules")
        if not isinstance(rules, list) or not rules:
            errors.append(f"{label}: missing rules list")
        else:
            if not any(str(rule).startswith("MATCH,") for rule in rules):
                errors.append(f"{label}: rules missing final MATCH rule")
            providers = config.get("rule-providers") or {}
            provider_names = set(providers.keys()) if isinstance(providers, dict) else set()
            for rule in rules:
                text = str(rule)
                parts = [p.strip() for p in text.split(",")]
                if len(parts) >= 2 and parts[0] == "RULE-SET":
                    if parts[1] not in provider_names:
                        errors.append(f"{label}: RULE-SET references missing provider: {parts[1]}")
                target = _rule_target(text)
                if target and target not in valid_refs:
                    errors.append(f"{label}: rule references missing policy/group: {text}")

    if "FALLBACK" in group_names and "MANUAL" in group_names:
        fallback = next((g for g in groups if isinstance(g, dict) and g.get("name") == "FALLBACK"), None)
        fallback_refs = fallback.get("proxies") if isinstance(fallback, dict) else []
        if isinstance(fallback_refs, list) and fallback_refs and fallback_refs[0] != "MANUAL":
            errors.append(f"{label}: FALLBACK must start with MANUAL when MANUAL group exists")

    return errors, warnings


def build_compatibility_report(items: list[tuple[str, str, bool]]) -> tuple[str, bool]:
    lines: list[str] = []
    ok = True
    for label, text, android in items:
        errors, warnings = validate_openclash_compatibility(text, label, android=android)
        lines.append(f"[{label}]")
        if not errors and not warnings:
            lines.append("OK: compatible structure check passed")
        for error in errors:
            ok = False
            lines.append("ERROR: " + error)
        for warning in warnings:
            lines.append("WARN: " + warning)
        lines.append("")
    return "\n".join(lines), ok


def add_manual_group_to_yaml_text(yaml_text: str, manual_nodes: list[Any], *, android: bool = False) -> str:
    if not manual_nodes:
        return yaml_text
    config = yaml.safe_load(yaml_text) or {}
    if not isinstance(config, dict):
        return yaml_text
    config = add_manual_group_to_config(config, manual_nodes, android=android)
    return yaml.safe_dump(config, allow_unicode=True, sort_keys=False, width=140)


def main() -> int:
    output_yaml = os.getenv("OUTPUT_YAML", "openclash_auto.yaml")
    output_csv = os.getenv("OUTPUT_CSV", "openclash_auto_report.csv")
    output_akun = os.getenv("OUTPUT_AKUN", "akun.txt")
    output_manual_akun = os.getenv("OUTPUT_MANUAL_AKUN", "akun_manual.txt")
    output_manual_skipped = os.getenv("OUTPUT_MANUAL_SKIPPED", "manual_nodes_skipped.txt")
    output_android_yaml = os.getenv("OUTPUT_ANDROID_YAML", "openclash_android.yaml")
    output_stamp = os.getenv("OUTPUT_STAMP", "last_update.txt")
    output_compat = os.getenv("OUTPUT_COMPAT_REPORT", "compatibility_report.txt")
    manual_file = os.getenv("MANUAL_NODES_FILE", "manual_nodes.txt")

    max_nodes = _env_int("MAX_NODES", 20)
    min_output_nodes = _env_int("MIN_OUTPUT_NODES", 20)
    fetch_timeout = _env_int("FETCH_TIMEOUT", 15)
    tcp_timeout = _env_float("TCP_TIMEOUT", 3.0)
    max_workers = _env_int("MAX_WORKERS", 80)
    attempts = _env_int("ATTEMPTS", 5)
    require_successes = min(_env_int("REQUIRE_SUCCESSES", 4), attempts)
    max_handshake_ms = _env_int("MAX_HANDSHAKE_MS", 250)
    max_avg_handshake_ms = _env_int("MAX_AVG_HANDSHAKE_MS", 350)

    links_text = build_links_text()
    manual_text = _read_text_file(manual_file)
    manual_text, manual_server_changes = normalize_manual_nodes_text(manual_text)
    if manual_text:
        # GitHub Actions will commit this normalized manual_nodes.txt, so future
        # runs no longer contain original servers.
        Path(manual_file).write_text(manual_text, encoding="utf-8")
    manual_nodes, manual_skipped = parse_manual_nodes_unscreened(manual_text)

    print("[INFO] Generate YAML OpenClash otomatis")
    print(f"[INFO] Target output otomatis: {max_nodes} node, minimal: {min_output_nodes} node")
    print(f"[INFO] Links subscription: {len([x for x in links_text.splitlines() if x.strip()])}")
    print(f"[INFO] Manual nodes parsed: {len(manual_nodes)}; skipped: {len(manual_skipped)}")
    print(f"[INFO] Manual node server normalized to {TARGET_SERVER}:{ONLY_PORT}: {manual_server_changes} link")
    print(f"[INFO] Filter low handshake otomatis: max best={max_handshake_ms}ms; max avg={max_avg_handshake_ms if max_avg_handshake_ms > 0 else 'off'}")

    validation_pool_nodes = max(max_nodes, _env_int("VALIDATION_POOL_NODES", max(80, max_nodes * 4)))
    print(f"[INFO] Pool validasi otomatis sebelum real-check: {validation_pool_nodes} node")

    # Important: manual_text is intentionally NOT passed into process_sources.
    # Manual nodes must not be strict-filtered and must not reduce the 20 automatic nodes.
    alive_nodes, all_nodes, fetch_logs, skipped = process_sources(
        links_text=links_text,
        manual_text="",
        fetch_timeout=fetch_timeout,
        tcp_timeout=tcp_timeout,
        max_workers=max_workers,
        max_nodes=validation_pool_nodes,
        fast_target_ms=_env_int("FAST_TARGET_MS", 123),
        fill_delay_ms=_env_int("FILL_DELAY_MS", 1200),
        min_output_nodes=min_output_nodes,
        attempts=attempts,
        require_successes=require_successes,
        require_original=_env_bool("REQUIRE_ORIGINAL", False),
        candidate_multiplier=_env_int("CANDIDATE_MULTIPLIER", 100),
        candidate_min=_env_int("CANDIDATE_MIN", 2500),
        max_jitter_ms=_env_int("MAX_JITTER_MS", 0),
        prefer_ws=_env_bool("PREFER_WS", True),
        require_ws_upgrade=_env_bool("REQUIRE_WS_UPGRADE", True),
        force_ws_only=_env_bool("FORCE_WS_ONLY", True),
        reserve_pool_nodes=_env_int("RESERVE_POOL_NODES", 120),
        max_handshake_ms=max_handshake_ms,
        max_avg_handshake_ms=max_avg_handshake_ms,
    )

    auto_pool_nodes = alive_nodes
    alive_nodes, real_checked_count, real_check_reason = _mihomo_real_check_nodes(
        auto_pool_nodes,
        limit=max_nodes,
        test_url=os.getenv("REAL_CHECK_TEST_URL", os.getenv("TEST_URL", ALT_TEST_URL)),
        timeout_ms=_env_int("REAL_CHECK_TIMEOUT_MS", _env_int("HEALTH_TIMEOUT_MS", 6000)),
    )
    unique_names(alive_nodes)
    print(f"[INFO] Real proxy check otomatis: {real_check_reason}")

    yaml_text = build_openclash_yaml(
        alive_nodes,
        interval=_env_int("URLTEST_INTERVAL", 60),
        tolerance=_env_int("TOLERANCE", 40),
        test_url=os.getenv("TEST_URL", ALT_TEST_URL),
        health_timeout=_env_int("HEALTH_TIMEOUT_MS", 6000),
        rule_mode=os.getenv("RULE_MODE", "Lite"),
    )
    yaml_text = add_manual_group_to_yaml_text(yaml_text, manual_nodes, android=False)
    yaml_text = finalize_yaml_for_openclash(yaml_text)

    android_yaml_text = build_openclash_android_yaml(
        alive_nodes,
        interval=_env_int("ANDROID_URLTEST_INTERVAL", _env_int("URLTEST_INTERVAL", 60)),
        tolerance=_env_int("ANDROID_TOLERANCE", _env_int("TOLERANCE", 40)),
        test_url=os.getenv("ANDROID_TEST_URL", os.getenv("TEST_URL", ALT_TEST_URL)),
        health_timeout=_env_int("ANDROID_HEALTH_TIMEOUT_MS", _env_int("HEALTH_TIMEOUT_MS", 6000)),
    )
    android_yaml_text = add_manual_group_to_yaml_text(android_yaml_text, manual_nodes, android=True)
    android_yaml_text = finalize_yaml_for_openclash(android_yaml_text)

    compatibility_report, compatibility_ok = build_compatibility_report([
        (output_yaml, yaml_text, False),
        (output_android_yaml, android_yaml_text, True),
    ])
    print(compatibility_report)

    csv_text = build_csv(all_nodes + manual_nodes)
    akun_text = build_akun_txt(alive_nodes)
    manual_akun_text = build_akun_txt(manual_nodes)
    manual_skipped_text = "\n".join(manual_skipped) + ("\n" if manual_skipped else "")

    Path(output_yaml).write_text(yaml_text, encoding="utf-8")
    Path(output_android_yaml).write_text(android_yaml_text, encoding="utf-8")
    Path(output_csv).write_text(csv_text, encoding="utf-8")
    Path(output_akun).write_text(akun_text, encoding="utf-8")
    Path(output_manual_akun).write_text(manual_akun_text, encoding="utf-8")
    Path(output_manual_skipped).write_text(manual_skipped_text, encoding="utf-8")
    Path(output_compat).write_text(compatibility_report, encoding="utf-8")

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    summary = (
        f"Last update: {now}\n"
        f"OpenClash YAML: {output_yaml}\n"
        f"Android YAML: {output_android_yaml}\n"
        f"Automatic YAML nodes: {len(alive_nodes)}\n"
        f"Automatic strict pool before real check: {len(auto_pool_nodes)}\n"
        f"Automatic real-check tested: {real_checked_count}\n"
        f"Automatic real-check result: {real_check_reason}\n"
        f"Low handshake filter max best: {max_handshake_ms}ms\n"
        f"Low handshake filter max avg: {max_avg_handshake_ms if max_avg_handshake_ms > 0 else 'off'}\n"
        f"Manual group nodes: {len(manual_nodes)}\n"
        f"Akun txt automatic: {len([x for x in akun_text.splitlines() if x.strip()])}\n"
        f"Akun txt manual: {len([x for x in manual_akun_text.splitlines() if x.strip()])}\n"
        f"Parsed subscription nodes: {len(all_nodes)}\n"
        f"Fetched links: {len(fetch_logs)}\n"
        f"Skipped raw URI: {len(skipped)}\n"
        f"Skipped manual URI: {len(manual_skipped)}\n"
        f"Manual server normalized: {manual_server_changes} link\n"
        f"Manual nodes source file: {manual_file}\n"
        f"Bug server for akun txt/manual_nodes: {TARGET_SERVER}:443\n"
    )
    Path(output_stamp).write_text(summary, encoding="utf-8")

    print(summary)
    if len(alive_nodes) < min_output_nodes:
        print(f"[WARN] Node strict otomatis yang lolos hanya {len(alive_nodes)}/{min_output_nodes}. YAML tetap dibuat dengan node yang tersedia.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
