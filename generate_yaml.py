from __future__ import annotations

import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlparse, urlunparse

import base64
import json
import yaml

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
    """Give manual nodes safe names with MANUAL prefix.

    Manual nodes are intentionally not strict-filtered or tested. The name uses
    original-server provider when it can be detected, but falls back safely when
    detection fails. The MANUAL prefix prevents collision with the 20 automatic
    nodes that use AKUN-001, AKUN-002, and so on.
    """
    seen: set[str] = set()
    for i, node in enumerate(nodes, start=1):
        node.original_name = node.original_name or normalize_name(node.name, f"MANUAL-ORIGINAL-{i:03d}")
        try:
            provider = provider_label_from_original_server(node)
        except Exception:
            provider = "UNKNOWN"
        provider = safe_proxy_name(str(provider or "UNKNOWN").upper(), "UNKNOWN")
        proto = safe_proxy_name(str(node.type or "NODE").upper(), "NODE")
        net = safe_proxy_name(node_network(node).upper(), "NET")
        base = safe_proxy_name(f"MANUAL-{i:03d}-{provider}-{proto}-{net}", f"MANUAL-{i:03d}")
        name = base
        counter = 2
        while name in seen:
            suffix = f"-{counter}"
            name = (base[: 64 - len(suffix)] + suffix).strip("-._")
            counter += 1
        seen.add(name)
        node.name = name
        node.clash["name"] = name
        node.status = "manual-unfiltered"
        node.tier = "MANUAL"
        node.reason = "manual_nodes.txt: added without strict filtering/testing"


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

    # Keep manual group outside AUTO-FAST/FALLBACK/LOAD-BALANCE. It is selectable
    # from GLOBAL/PROXY only and does not reduce the 20 auto nodes.
    for group in groups:
        if not isinstance(group, dict):
            continue
        name = str(group.get("name") or "")
        proxies_list = group.get("proxies")
        if not isinstance(proxies_list, list):
            continue
        if name == "GLOBAL":
            # Put MANUAL after DIRECT if present; otherwise after FALLBACK.
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
    manual_file = os.getenv("MANUAL_NODES_FILE", "manual_nodes.txt")

    max_nodes = _env_int("MAX_NODES", 20)
    min_output_nodes = _env_int("MIN_OUTPUT_NODES", 20)
    fetch_timeout = _env_int("FETCH_TIMEOUT", 15)
    tcp_timeout = _env_float("TCP_TIMEOUT", 3.0)
    max_workers = _env_int("MAX_WORKERS", 80)
    attempts = _env_int("ATTEMPTS", 2)
    require_successes = min(_env_int("REQUIRE_SUCCESSES", 1), attempts)

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

    # Important: manual_text is intentionally NOT passed into process_sources.
    # Manual nodes must not be strict-filtered and must not reduce the 20 automatic nodes.
    alive_nodes, all_nodes, fetch_logs, skipped = process_sources(
        links_text=links_text,
        manual_text="",
        fetch_timeout=fetch_timeout,
        tcp_timeout=tcp_timeout,
        max_workers=max_workers,
        max_nodes=max_nodes,
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
    )

    yaml_text = build_openclash_yaml(
        alive_nodes,
        interval=_env_int("URLTEST_INTERVAL", 60),
        tolerance=_env_int("TOLERANCE", 40),
        test_url=os.getenv("TEST_URL", ALT_TEST_URL),
        health_timeout=_env_int("HEALTH_TIMEOUT_MS", 6000),
        rule_mode=os.getenv("RULE_MODE", "Lite"),
    )
    yaml_text = add_manual_group_to_yaml_text(yaml_text, manual_nodes, android=False)

    android_yaml_text = build_openclash_android_yaml(
        alive_nodes,
        interval=_env_int("ANDROID_URLTEST_INTERVAL", _env_int("URLTEST_INTERVAL", 60)),
        tolerance=_env_int("ANDROID_TOLERANCE", _env_int("TOLERANCE", 40)),
        test_url=os.getenv("ANDROID_TEST_URL", os.getenv("TEST_URL", ALT_TEST_URL)),
        health_timeout=_env_int("ANDROID_HEALTH_TIMEOUT_MS", _env_int("HEALTH_TIMEOUT_MS", 6000)),
    )
    android_yaml_text = add_manual_group_to_yaml_text(android_yaml_text, manual_nodes, android=True)

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

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    summary = (
        f"Last update: {now}\n"
        f"OpenClash YAML: {output_yaml}\n"
        f"Android YAML: {output_android_yaml}\n"
        f"Automatic YAML nodes: {len(alive_nodes)}\n"
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
