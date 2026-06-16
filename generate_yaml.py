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
    node_identity_key,
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



def _free_tcp_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def _expected_statuses(raw: str | None = None) -> set[int]:
    if raw is None:
        raw = os.getenv("URL_TEST_EXPECTED_STATUS", os.getenv("REAL_CHECK_EXPECTED_STATUS", "204,200,301,302"))
    raw = str(raw or "204,200,301,302").strip()
    statuses: set[int] = set()
    for item in raw.replace("/", ",").replace(";", ",").split(","):
        item = item.strip()
        if not item:
            continue
        try:
            statuses.add(int(item))
        except ValueError:
            pass
    return statuses or {204, 200, 301, 302}


def _wait_controller(controller_url: str, timeout_s: float = 10.0) -> bool:
    deadline = time.time() + max(1.0, timeout_s)
    while time.time() < deadline:
        try:
            response = requests.get(controller_url + "/proxies", timeout=0.6)
            if response.status_code < 500:
                return True
        except Exception:
            time.sleep(0.2)
    return False


def _node_name(node: Any) -> str:
    return str(node.clash.get("name") or node.name or "")


def _mihomo_url_test_nodes(
    nodes: list[Any],
    *,
    target_count: int,
    test_url: str,
    timeout_ms: int,
    expected_statuses: set[int] | None = None,
) -> tuple[list[Any], int, str, list[dict[str, Any]]]:
    """Filter automatic nodes with a real Mihomo URL test.

    This test is intentionally applied only to automatic subscription nodes.
    Manual nodes are handled outside this function and are not filtered.
    """
    target_count = max(1, int(target_count))
    rows: list[dict[str, Any]] = []
    if not nodes:
        return [], 0, "no automatic nodes to URL test", rows

    if not _env_bool("REQUIRE_URL_TEST", True):
        final_nodes = nodes[:target_count]
        for node in final_nodes:
            node.url_test_status = "skipped-disabled"
            node.url_test_success = True
        return final_nodes, len(final_nodes), "URL test disabled", rows

    core_path = os.getenv("MIHOMO_PATH", "./mihomo").strip() or "./mihomo"
    if not Path(core_path).exists():
        raise SystemExit(f"Mihomo binary tidak ditemukan di {core_path}; URL test wajib aktif.")

    expected = expected_statuses or _expected_statuses()
    proxy_port = _free_tcp_port()
    controller_port = _free_tcp_port()
    names = [_node_name(node) for node in nodes if _node_name(node)]
    if not names:
        return [], 0, "no usable proxy names for URL test", rows

    tmpdir_obj = tempfile.TemporaryDirectory(prefix="mihomo-urltest-")
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
        "profile": {"store-selected": False, "store-fake-ip": False},
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
        "proxy-groups": [{"name": "GLOBAL", "type": "select", "proxies": names}],
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
            raise SystemExit("Mihomo controller tidak start, URL test tidak bisa dilakukan.")

        proxy_url = f"http://127.0.0.1:{proxy_port}"
        request_timeout = max(1.0, float(timeout_ms) / 1000.0)
        settle_s = float(os.getenv("URL_TEST_SETTLE_SECONDS", "0.12"))
        user_agent = os.getenv("URL_TEST_USER_AGENT", "Mozilla/5.0 SumberYAML-URLTest/1.0")

        for node in nodes:
            if len(passed) >= target_count:
                break
            name = _node_name(node)
            checked += 1
            start = time.perf_counter()
            status_text = ""
            success = False
            try:
                switch = requests.put(controller_url + "/proxies/GLOBAL", json={"name": name}, timeout=1.5)
                if switch.status_code >= 400:
                    status_text = f"switch HTTP {switch.status_code}"
                else:
                    time.sleep(settle_s)
                    response = requests.get(
                        test_url,
                        proxies={"http": proxy_url, "https": proxy_url},
                        timeout=request_timeout,
                        allow_redirects=False,
                        headers={"User-Agent": user_agent},
                    )
                    status_text = f"HTTP {response.status_code}"
                    success = response.status_code in expected
            except Exception as exc:
                status_text = type(exc).__name__ + ": " + str(exc)[:120]

            elapsed = int((time.perf_counter() - start) * 1000)
            node.url_test_ms = elapsed
            node.url_test_status = status_text
            node.url_test_success = success
            row = {
                "name": name,
                "type": getattr(node, "type", ""),
                "network": node_network(node),
                "original_server": getattr(node, "original_server", ""),
                "bug_sni": getattr(node, "bug_sni", ""),
                "handshake_ms": getattr(node, "best_delay_ms", ""),
                "ws_upgrade_ms": getattr(node, "ws_best_delay_ms", ""),
                "url_test_ms": elapsed,
                "url_test_status": status_text,
                "url_test_success": "yes" if success else "no",
            }
            rows.append(row)

            if success:
                node.status = "alive"
                node.reason = (getattr(node, "reason", "") + "; URL test ok").strip("; ")
                passed.append(node)
            else:
                node.status = "dead"
                node.reason = (getattr(node, "reason", "") + "; URL test failed: " + status_text).strip("; ")

        reason = f"URL test passed {len(passed)}/{checked} tested"
        return passed, checked, reason, rows
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


def _build_urltest_report_csv(rows: list[dict[str, Any]]) -> str:
    import csv
    import io
    fields = [
        "name", "type", "network", "original_server", "bug_sni",
        "handshake_ms", "ws_upgrade_ms", "url_test_ms", "url_test_status", "url_test_success",
    ]
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=fields)
    writer.writeheader()
    for row in rows:
        writer.writerow({field: row.get(field, "") for field in fields})
    return buffer.getvalue()


def _as_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except Exception:
        return default


def _ws_opts(node: Any) -> tuple[str, str]:
    clash = getattr(node, "clash", {}) or {}
    ws_opts = clash.get("ws-opts") if isinstance(clash.get("ws-opts"), dict) else {}
    path = str(ws_opts.get("path") or "/") or "/"
    headers = ws_opts.get("headers") if isinstance(ws_opts.get("headers"), dict) else {}
    host = str(headers.get("Host") or getattr(node, "bug_sni", "") or clash.get("servername") or clash.get("sni") or "").strip()
    return path, host


def _singbox_tls(clash: dict[str, Any], node: Any) -> dict[str, Any] | None:
    enabled = bool(clash.get("tls", True)) or str(clash.get("type", "")).lower() in {"vless", "trojan", "vmess"}
    if not enabled:
        return None
    server_name = str(clash.get("servername") or clash.get("sni") or getattr(node, "bug_sni", "") or "").strip()
    if not server_name:
        return None
    fingerprint = str(clash.get("client-fingerprint") or "chrome").strip().lower()
    allowed = {"chrome", "firefox", "safari", "ios", "android", "edge", "360", "qq", "random"}
    if fingerprint in {"randomized", "randomizedalpn"}:
        fingerprint = "random"
    if fingerprint not in allowed:
        fingerprint = "chrome"
    tls = {
        "enabled": True,
        "server_name": server_name,
        "insecure": bool(clash.get("skip-cert-verify", True)),
        "utls": {"enabled": True, "fingerprint": fingerprint},
    }
    alpn = clash.get("alpn")
    if isinstance(alpn, list) and alpn:
        # WebSocket is safest with HTTP/1.1. This avoids h2-first cases that can break WS.
        tls["alpn"] = ["http/1.1"] if node_network(node) == "ws" else [str(x) for x in alpn if str(x).strip()]
    elif node_network(node) == "ws":
        tls["alpn"] = ["http/1.1"]
    return tls


def _singbox_transport(node: Any) -> dict[str, Any] | None:
    network = node_network(node)
    if network != "ws":
        return None
    path, host = _ws_opts(node)
    transport: dict[str, Any] = {"type": "ws", "path": path or "/"}
    if host:
        transport["headers"] = {"Host": host}
    return transport


def _singbox_outbound_from_node(node: Any) -> dict[str, Any] | None:
    clash = getattr(node, "clash", {}) or {}
    proto = str(clash.get("type") or getattr(node, "type", "")).lower()
    server = str(clash.get("server") or TARGET_SERVER).strip()
    port = _as_int(clash.get("port"), ONLY_PORT) or ONLY_PORT
    base: dict[str, Any] = {"type": proto, "tag": "proxy", "server": server, "server_port": port}

    transport = _singbox_transport(node)
    tls = _singbox_tls(clash, node)

    if proto == "vless":
        uuid = str(clash.get("uuid") or "").strip()
        if not uuid:
            return None
        base["uuid"] = uuid
        if clash.get("flow"):
            base["flow"] = str(clash.get("flow"))
    elif proto == "trojan":
        password = str(clash.get("password") or "").strip()
        if not password:
            return None
        base["password"] = password
    elif proto == "vmess":
        uuid = str(clash.get("uuid") or "").strip()
        if not uuid:
            return None
        base["uuid"] = uuid
        # sing-box accepts common VMess security values. Keep it conservative.
        security = str(clash.get("cipher") or "auto").strip().lower() or "auto"
        if security not in {"auto", "none", "zero", "aes-128-gcm", "chacha20-poly1305"}:
            security = "auto"
        base["security"] = security
        if "alterId" in clash:
            base["alter_id"] = _as_int(clash.get("alterId"), 0)
    elif proto == "ss":
        method = str(clash.get("cipher") or "").strip()
        password = str(clash.get("password") or "").strip()
        if not method or not password:
            return None
        base["type"] = "shadowsocks"
        base["method"] = method
        base["password"] = password
    else:
        return None

    if tls and proto in {"vless", "trojan", "vmess"}:
        base["tls"] = tls
    if transport and proto in {"vless", "trojan", "vmess"}:
        base["transport"] = transport
    return base


def _wait_local_port(port: int, timeout_s: float = 8.0) -> bool:
    deadline = time.time() + max(1.0, timeout_s)
    while time.time() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", int(port)), timeout=0.3):
                return True
        except Exception:
            time.sleep(0.15)
    return False


def _singbox_url_test_nodes(
    nodes: list[Any],
    *,
    target_count: int,
    test_url: str,
    timeout_ms: int,
    expected_statuses: set[int] | None = None,
) -> tuple[list[Any], int, str, list[dict[str, Any]]]:
    """Filter automatic nodes with sing-box, as a NekoBox compatibility check.

    NekoBox for Android uses a sing-box based core, so this test is closer to
    NekoBox behavior than only relying on Mihomo/OpenClash. Manual nodes are not
    passed here and remain unfiltered by design.
    """
    target_count = max(1, int(target_count))
    rows: list[dict[str, Any]] = []
    if not nodes:
        return [], 0, "no automatic nodes to NekoBox/sing-box test", rows

    if not _env_bool("REQUIRE_NEKOBOX_TEST", True):
        final_nodes = nodes[:target_count]
        for node in final_nodes:
            node.nekobox_status = "skipped-disabled"
            node.nekobox_ready = True
        return final_nodes, len(final_nodes), "NekoBox/sing-box test disabled", rows

    core_path = os.getenv("SINGBOX_PATH", "./sing-box").strip() or "./sing-box"
    if not Path(core_path).exists():
        raise SystemExit(f"sing-box binary tidak ditemukan di {core_path}; NekoBox test wajib aktif.")

    expected = expected_statuses or _expected_statuses()
    passed: list[Any] = []
    checked = 0
    request_timeout = max(1.0, float(timeout_ms) / 1000.0)
    start_timeout = float(os.getenv("SINGBOX_START_TIMEOUT", "8"))
    user_agent = os.getenv("NEKOBOX_TEST_USER_AGENT", "Mozilla/5.0 SumberYAML-NekoBoxTest/1.0")

    for node in nodes:
        if len(passed) >= target_count:
            break
        name = _node_name(node)
        checked += 1
        status_text = ""
        success = False
        elapsed = 0
        outbound = _singbox_outbound_from_node(node)
        if outbound is None:
            status_text = "unsupported for sing-box conversion"
            rows.append({
                "name": name,
                "type": getattr(node, "type", ""),
                "network": node_network(node),
                "original_server": getattr(node, "original_server", ""),
                "bug_sni": getattr(node, "bug_sni", ""),
                "mihomo_status": getattr(node, "url_test_status", ""),
                "nekobox_test_ms": "",
                "nekobox_status": status_text,
                "nekobox_ready": "no",
            })
            continue

        proxy_port = _free_tcp_port()
        tmpdir_obj = tempfile.TemporaryDirectory(prefix="singbox-nekobox-test-")
        tmpdir = Path(tmpdir_obj.name)
        config_path = tmpdir / "config.json"
        config = {
            "log": {"level": os.getenv("SINGBOX_LOG_LEVEL", "error")},
            "inbounds": [
                {
                    "type": "mixed",
                    "tag": "mixed-in",
                    "listen": "127.0.0.1",
                    "listen_port": proxy_port,
                    "sniff": False,
                }
            ],
            "outbounds": [outbound],
        }
        config_path.write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8")
        proc: subprocess.Popen[str] | None = None
        start = time.perf_counter()
        try:
            proc = subprocess.Popen(
                [core_path, "run", "-c", str(config_path)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                text=True,
            )
            if not _wait_local_port(proxy_port, timeout_s=start_timeout):
                status_text = "sing-box inbound did not start"
            else:
                proxy_url = f"http://127.0.0.1:{proxy_port}"
                response = requests.get(
                    test_url,
                    proxies={"http": proxy_url, "https": proxy_url},
                    timeout=request_timeout,
                    allow_redirects=False,
                    headers={"User-Agent": user_agent},
                )
                status_text = f"HTTP {response.status_code}"
                success = response.status_code in expected
        except Exception as exc:
            status_text = type(exc).__name__ + ": " + str(exc)[:140]
        finally:
            elapsed = int((time.perf_counter() - start) * 1000)
            if proc is not None:
                with suppress(Exception):
                    proc.terminate()
                with suppress(Exception):
                    proc.wait(timeout=2)
                if proc.poll() is None:
                    with suppress(Exception):
                        proc.kill()
            tmpdir_obj.cleanup()

        node.nekobox_test_ms = elapsed
        node.nekobox_status = status_text
        node.nekobox_ready = success
        row = {
            "name": name,
            "type": getattr(node, "type", ""),
            "network": node_network(node),
            "original_server": getattr(node, "original_server", ""),
            "bug_sni": getattr(node, "bug_sni", ""),
            "mihomo_status": getattr(node, "url_test_status", ""),
            "url_test_ms": getattr(node, "url_test_ms", ""),
            "nekobox_test_ms": elapsed,
            "nekobox_status": status_text,
            "nekobox_ready": "yes" if success else "no",
        }
        rows.append(row)
        if success:
            node.status = "alive"
            node.reason = (getattr(node, "reason", "") + "; NekoBox/sing-box ok").strip("; ")
            passed.append(node)
        else:
            node.status = "dead"
            node.reason = (getattr(node, "reason", "") + "; NekoBox/sing-box failed: " + status_text).strip("; ")

    reason = f"NekoBox/sing-box passed {len(passed)}/{checked} tested"
    return passed, checked, reason, rows


def _build_nekobox_report_csv(rows: list[dict[str, Any]]) -> str:
    import csv
    import io
    fields = [
        "name", "type", "network", "original_server", "bug_sni",
        "mihomo_status", "url_test_ms", "nekobox_test_ms", "nekobox_status", "nekobox_ready",
    ]
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=fields)
    writer.writeheader()
    for row in rows:
        writer.writerow({field: row.get(field, "") for field in fields})
    return buffer.getvalue()


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


def _extend_links_from_text(links: list[str], text: str) -> None:
    for line in (text or "").splitlines():
        line = line.strip().strip(",'\"")
        if line and not line.startswith("#"):
            links.append(line)


def build_streaming_links_text() -> str:
    """Build a separate subscription list for STREAMING-FAST.

    Streaming uses its own pool so it can discover accounts outside the standard
    MAX_NODES result. Add streaming-only sources in streaming_subscription_links.txt
    or EXTRA_STREAMING_SUBSCRIPTION_LINKS. By default it also scans the public
    defaults and subscription_links.txt, but selected standard accounts are
    excluded later before STREAMING-FAST is built.
    """
    links: list[str] = []
    if _env_bool("STREAMING_USE_DEFAULT_LINKS", True):
        links.extend(DEFAULT_LINKS)

    if _env_bool("STREAMING_INCLUDE_STANDARD_LINKS", True):
        _extend_links_from_text(links, _read_text_file(os.getenv("SUBSCRIPTION_LINKS_FILE", "subscription_links.txt")))
        _extend_links_from_text(links, os.getenv("EXTRA_SUBSCRIPTION_LINKS", ""))

    streaming_file = os.getenv("STREAMING_SUBSCRIPTION_LINKS_FILE", "streaming_subscription_links.txt")
    _extend_links_from_text(links, _read_text_file(streaming_file))
    _extend_links_from_text(links, os.getenv("EXTRA_STREAMING_SUBSCRIPTION_LINKS", ""))

    unique: list[str] = []
    seen: set[str] = set()
    for link in links:
        if link not in seen:
            seen.add(link)
            unique.append(link)
    return "\n".join(unique)


def _exclude_existing_identities(nodes: list[Any], existing_nodes: list[Any]) -> list[Any]:
    existing_keys = {node_identity_key(node) for node in existing_nodes}
    out: list[Any] = []
    seen: set[Any] = set()
    for node in nodes:
        key = node_identity_key(node)
        if key in existing_keys or key in seen:
            node.status = "skipped"
            node.reason = (getattr(node, "reason", "") + "; skipped for streaming: duplicate of standard pool").strip("; ")
            continue
        seen.add(key)
        out.append(node)
    return out


def _unique_streaming_names(nodes: list[Any], existing_names: set[str]) -> None:
    seen = set(existing_names)
    for i, node in enumerate(nodes, start=1):
        node.original_name = node.original_name or normalize_name(node.name, f"STREAMING-ORIGINAL-{i:03d}")
        proto = safe_proxy_name(str(getattr(node, "type", "NODE")).upper(), "NODE")
        net = safe_proxy_name(node_network(node).upper(), "NET")
        delay_value = getattr(node, "nekobox_test_ms", None) or getattr(node, "url_test_ms", None) or getattr(node, "best_delay_ms", None)
        try:
            delay = f"{int(delay_value)}MS" if delay_value is not None else "NA"
        except Exception:
            delay = "NA"
        provider = provider_label_from_original_server(node)
        base = safe_proxy_name(f"STREAM-{i:03d}-{provider}-{proto}-{net}-{delay}", f"STREAM-{i:03d}")
        name = base
        counter = 2
        while name in seen:
            suffix = f"-{counter}"
            name = (base[: 64 - len(suffix)] + suffix).strip("-._") or f"STREAM-{i:03d}-{counter}"
            counter += 1
        seen.add(name)
        node.name = name
        node.clash["name"] = name
        node.tier = node.tier or "STREAMING"
        node.reason = (getattr(node, "reason", "") + "; selected for STREAMING-FAST dedicated pool").strip("; ")


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
    output_urltest_report = os.getenv("OUTPUT_URLTEST_REPORT", "urltest_report.csv")
    output_nekobox_report = os.getenv("OUTPUT_NEKOBOX_REPORT", "nekobox_test_report.csv")
    output_streaming_urltest_report = os.getenv("OUTPUT_STREAMING_URLTEST_REPORT", "streaming_urltest_report.csv")
    output_streaming_nekobox_report = os.getenv("OUTPUT_STREAMING_NEKOBOX_REPORT", "streaming_nekobox_report.csv")
    output_streaming_akun = os.getenv("OUTPUT_STREAMING_AKUN", "akun_streaming.txt")
    output_android_yaml = os.getenv("OUTPUT_ANDROID_YAML", "openclash_android.yaml")
    output_stamp = os.getenv("OUTPUT_STAMP", "last_update.txt")
    manual_file = os.getenv("MANUAL_NODES_FILE", "manual_nodes.txt")

    max_nodes = _env_int("MAX_NODES", 10)
    min_output_nodes = _env_int("MIN_OUTPUT_NODES", 10)
    fetch_timeout = _env_int("FETCH_TIMEOUT", 12)
    tcp_timeout = _env_float("TCP_TIMEOUT", 2.0)
    max_workers = _env_int("MAX_WORKERS", 64)
    attempts = _env_int("ATTEMPTS", 2)
    require_successes = min(_env_int("REQUIRE_SUCCESSES", 1), attempts)

    links_text = build_links_text()
    streaming_links_text = build_streaming_links_text()
    manual_text = _read_text_file(manual_file)
    manual_text, manual_server_changes = normalize_manual_nodes_text(manual_text)
    if manual_text:
        # GitHub Actions will commit this normalized manual_nodes.txt, so future
        # runs no longer contain original servers.
        Path(manual_file).write_text(manual_text, encoding="utf-8")
    manual_nodes, manual_skipped = parse_manual_nodes_unscreened(manual_text)

    print("[INFO] Generate YAML OpenClash otomatis")
    print(f"[INFO] Target output otomatis: {max_nodes} node, minimal: {min_output_nodes} node")
    print(f"[INFO] Links subscription standar: {len([x for x in links_text.splitlines() if x.strip()])}")
    print(f"[INFO] Links subscription streaming khusus: {len([x for x in streaming_links_text.splitlines() if x.strip()])}")
    print(f"[INFO] Manual nodes parsed: {len(manual_nodes)}; skipped: {len(manual_skipped)}")
    print(f"[INFO] Manual node server normalized to {TARGET_SERVER}:{ONLY_PORT}: {manual_server_changes} link")

    # Important: manual_text is intentionally NOT passed into process_sources.
    # Manual nodes must not be strict-filtered and must not reduce the automatic quota.
    # We first collect a small strict WS pool, then run a real URL test through Mihomo
    # and stop as soon as MAX_NODES alive nodes are found.
    urltest_pool_nodes = max(max_nodes, _env_int("URLTEST_POOL_NODES", max(30, max_nodes * 3)))
    print(f"[INFO] Pool kandidat sebelum URL test: {urltest_pool_nodes} node")
    auto_pool_nodes, all_nodes, fetch_logs, skipped = process_sources(
        links_text=links_text,
        manual_text="",
        fetch_timeout=fetch_timeout,
        tcp_timeout=tcp_timeout,
        max_workers=max_workers,
        max_nodes=urltest_pool_nodes,
        fast_target_ms=_env_int("FAST_TARGET_MS", 123),
        fill_delay_ms=_env_int("FILL_DELAY_MS", 1200),
        min_output_nodes=min_output_nodes,
        attempts=attempts,
        require_successes=require_successes,
        require_original=_env_bool("REQUIRE_ORIGINAL", False),
        candidate_multiplier=_env_int("CANDIDATE_MULTIPLIER", 35),
        candidate_min=_env_int("CANDIDATE_MIN", 350),
        max_jitter_ms=_env_int("MAX_JITTER_MS", 0),
        prefer_ws=_env_bool("PREFER_WS", True),
        require_ws_upgrade=_env_bool("REQUIRE_WS_UPGRADE", True),
        force_ws_only=_env_bool("FORCE_WS_ONLY", True),
        reserve_pool_nodes=_env_int("RESERVE_POOL_NODES", urltest_pool_nodes),
        early_stop_good_nodes=_env_bool("EARLY_STOP_GOOD_NODES", True),
        test_batch_size=_env_int("TEST_BATCH_SIZE", 80),
    )

    nekobox_pool_nodes = max(max_nodes, _env_int("NEKOBOX_POOL_NODES", max(20, max_nodes * 3)))
    mihomo_pass_nodes, urltest_checked_count, urltest_reason, urltest_rows = _mihomo_url_test_nodes(
        auto_pool_nodes,
        target_count=nekobox_pool_nodes,
        test_url=os.getenv("URL_TEST_URL", os.getenv("TEST_URL", ALT_TEST_URL)),
        timeout_ms=_env_int("URL_TEST_TIMEOUT_MS", _env_int("HEALTH_TIMEOUT_MS", 6000)),
    )
    print(f"[INFO] URL test Mihomo otomatis: {urltest_reason}")

    alive_nodes, nekobox_checked_count, nekobox_reason, nekobox_rows = _singbox_url_test_nodes(
        mihomo_pass_nodes,
        target_count=max_nodes,
        test_url=os.getenv("NEKOBOX_TEST_URL", os.getenv("URL_TEST_URL", os.getenv("TEST_URL", ALT_TEST_URL))),
        timeout_ms=_env_int("NEKOBOX_TEST_TIMEOUT_MS", _env_int("URL_TEST_TIMEOUT_MS", _env_int("HEALTH_TIMEOUT_MS", 6000))),
    )
    unique_names(alive_nodes)
    print(f"[INFO] NekoBox/sing-box test otomatis standar: {nekobox_reason}")

    streaming_enabled = _env_bool("ENABLE_STREAMING_DEDICATED_POOL", True)
    streaming_all_nodes: list[Any] = []
    streaming_pool_nodes_list: list[Any] = []
    streaming_mihomo_pass_nodes: list[Any] = []
    streaming_alive_nodes: list[Any] = []
    streaming_fetch_logs: list[tuple[str, str]] = []
    streaming_skipped: list[str] = []
    streaming_urltest_rows: list[dict[str, Any]] = []
    streaming_nekobox_rows: list[dict[str, Any]] = []
    streaming_urltest_checked_count = 0
    streaming_nekobox_checked_count = 0
    streaming_urltest_reason = "streaming dedicated pool disabled"
    streaming_nekobox_reason = "streaming dedicated pool disabled"

    if streaming_enabled and streaming_links_text.strip():
        streaming_max_nodes = _env_int("STREAMING_MAX_NODES", 20)
        streaming_min_nodes = _env_int("STREAMING_MIN_OUTPUT_NODES", min(10, streaming_max_nodes))
        streaming_urltest_pool_nodes = max(
            streaming_max_nodes,
            _env_int("STREAMING_URLTEST_POOL_NODES", max(80, streaming_max_nodes * 4)),
        )
        streaming_nekobox_pool_nodes = max(
            streaming_max_nodes,
            _env_int("STREAMING_NEKOBOX_POOL_NODES", max(40, streaming_max_nodes * 2)),
        )
        print(f"[INFO] Pool kandidat khusus streaming sebelum URL test: {streaming_urltest_pool_nodes} node")
        streaming_pool_nodes_list, streaming_all_nodes, streaming_fetch_logs, streaming_skipped = process_sources(
            links_text=streaming_links_text,
            manual_text="",
            fetch_timeout=_env_int("STREAMING_FETCH_TIMEOUT", fetch_timeout),
            tcp_timeout=_env_float("STREAMING_TCP_TIMEOUT", tcp_timeout),
            max_workers=_env_int("STREAMING_MAX_WORKERS", max_workers),
            max_nodes=streaming_urltest_pool_nodes,
            fast_target_ms=_env_int("STREAMING_FAST_TARGET_MS", _env_int("FAST_TARGET_MS", 123)),
            fill_delay_ms=_env_int("STREAMING_FILL_DELAY_MS", _env_int("FILL_DELAY_MS", 1200)),
            min_output_nodes=streaming_min_nodes,
            attempts=_env_int("STREAMING_ATTEMPTS", attempts),
            require_successes=min(_env_int("STREAMING_REQUIRE_SUCCESSES", require_successes), _env_int("STREAMING_ATTEMPTS", attempts)),
            require_original=_env_bool("STREAMING_REQUIRE_ORIGINAL", _env_bool("REQUIRE_ORIGINAL", False)),
            candidate_multiplier=_env_int("STREAMING_CANDIDATE_MULTIPLIER", _env_int("CANDIDATE_MULTIPLIER", 35)),
            candidate_min=_env_int("STREAMING_CANDIDATE_MIN", _env_int("CANDIDATE_MIN", 350)),
            max_jitter_ms=_env_int("STREAMING_MAX_JITTER_MS", _env_int("MAX_JITTER_MS", 0)),
            prefer_ws=_env_bool("STREAMING_PREFER_WS", _env_bool("PREFER_WS", True)),
            require_ws_upgrade=_env_bool("STREAMING_REQUIRE_WS_UPGRADE", _env_bool("REQUIRE_WS_UPGRADE", True)),
            force_ws_only=_env_bool("STREAMING_FORCE_WS_ONLY", _env_bool("FORCE_WS_ONLY", True)),
            reserve_pool_nodes=_env_int("STREAMING_RESERVE_POOL_NODES", streaming_urltest_pool_nodes),
            early_stop_good_nodes=_env_bool("STREAMING_EARLY_STOP_GOOD_NODES", True),
            test_batch_size=_env_int("STREAMING_TEST_BATCH_SIZE", _env_int("TEST_BATCH_SIZE", 80)),
        )
        streaming_pool_nodes_list = _exclude_existing_identities(streaming_pool_nodes_list, alive_nodes)
        print(f"[INFO] Pool khusus streaming setelah buang duplikat standar: {len(streaming_pool_nodes_list)} node")

        streaming_expected_statuses = _expected_statuses(
            os.getenv("STREAMING_URL_TEST_EXPECTED_STATUS", os.getenv("STREAMING_EXPECTED_STATUS", "200,204,301,302,403"))
        )
        streaming_mihomo_pass_nodes, streaming_urltest_checked_count, streaming_urltest_reason, streaming_urltest_rows = _mihomo_url_test_nodes(
            streaming_pool_nodes_list,
            target_count=streaming_nekobox_pool_nodes,
            test_url=os.getenv("STREAMING_REAL_CHECK_TEST_URL", os.getenv("STREAMING_TEST_URL", os.getenv("URL_TEST_URL", os.getenv("TEST_URL", ALT_TEST_URL)))),
            timeout_ms=_env_int("STREAMING_URL_TEST_TIMEOUT_MS", _env_int("URL_TEST_TIMEOUT_MS", _env_int("HEALTH_TIMEOUT_MS", 6000))),
            expected_statuses=streaming_expected_statuses,
        )
        streaming_mihomo_pass_nodes = _exclude_existing_identities(streaming_mihomo_pass_nodes, alive_nodes)
        print(f"[INFO] URL test Mihomo khusus streaming: {streaming_urltest_reason}")

        streaming_alive_nodes, streaming_nekobox_checked_count, streaming_nekobox_reason, streaming_nekobox_rows = _singbox_url_test_nodes(
            streaming_mihomo_pass_nodes,
            target_count=streaming_max_nodes,
            test_url=os.getenv("STREAMING_NEKOBOX_TEST_URL", os.getenv("STREAMING_TEST_URL", os.getenv("NEKOBOX_TEST_URL", os.getenv("URL_TEST_URL", os.getenv("TEST_URL", ALT_TEST_URL))))),
            timeout_ms=_env_int("STREAMING_NEKOBOX_TEST_TIMEOUT_MS", _env_int("NEKOBOX_TEST_TIMEOUT_MS", _env_int("URL_TEST_TIMEOUT_MS", _env_int("HEALTH_TIMEOUT_MS", 6000)))),
            expected_statuses=streaming_expected_statuses,
        )
        streaming_alive_nodes = _exclude_existing_identities(streaming_alive_nodes, alive_nodes)[:streaming_max_nodes]
        _unique_streaming_names(streaming_alive_nodes, {node.clash.get("name") for node in alive_nodes if node.clash.get("name")})
        print(f"[INFO] NekoBox/sing-box test khusus streaming: {streaming_nekobox_reason}")
        if len(streaming_alive_nodes) < streaming_min_nodes:
            print(f"[WARN] Node khusus streaming hanya {len(streaming_alive_nodes)}/{streaming_min_nodes}. STREAMING-FAST tetap dibuat dari node streaming yang tersedia.")
    else:
        print("[INFO] Pool khusus streaming dimatikan atau tidak ada link streaming.")

    yaml_text = build_openclash_yaml(
        alive_nodes,
        interval=_env_int("URLTEST_INTERVAL", 60),
        tolerance=_env_int("TOLERANCE", 40),
        test_url=os.getenv("TEST_URL", ALT_TEST_URL),
        health_timeout=_env_int("HEALTH_TIMEOUT_MS", 6000),
        rule_mode=os.getenv("RULE_MODE", "Lite"),
        streaming_nodes=streaming_alive_nodes,
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

    csv_text = build_csv(all_nodes + streaming_all_nodes + manual_nodes)
    akun_text = build_akun_txt(alive_nodes)
    streaming_akun_text = build_akun_txt(streaming_alive_nodes)
    manual_akun_text = build_akun_txt(manual_nodes)
    manual_skipped_text = "\n".join(manual_skipped) + ("\n" if manual_skipped else "")

    Path(output_yaml).write_text(yaml_text, encoding="utf-8")
    Path(output_android_yaml).write_text(android_yaml_text, encoding="utf-8")
    Path(output_csv).write_text(csv_text, encoding="utf-8")
    Path(output_akun).write_text(akun_text, encoding="utf-8")
    Path(output_streaming_akun).write_text(streaming_akun_text, encoding="utf-8")
    Path(output_manual_akun).write_text(manual_akun_text, encoding="utf-8")
    Path(output_manual_skipped).write_text(manual_skipped_text, encoding="utf-8")
    Path(output_urltest_report).write_text(_build_urltest_report_csv(urltest_rows), encoding="utf-8")
    Path(output_nekobox_report).write_text(_build_nekobox_report_csv(nekobox_rows), encoding="utf-8")
    Path(output_streaming_urltest_report).write_text(_build_urltest_report_csv(streaming_urltest_rows), encoding="utf-8")
    Path(output_streaming_nekobox_report).write_text(_build_nekobox_report_csv(streaming_nekobox_rows), encoding="utf-8")

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    summary = (
        f"Last update: {now}\n"
        f"Mode: FAST10 + Mihomo URL test + NekoBox/sing-box test early-stop\n"
        f"OpenClash YAML: {output_yaml}\n"
        f"Android YAML: {output_android_yaml}\n"
        f"Automatic YAML nodes after NekoBox test: {len(alive_nodes)}\n"
        f"Dedicated streaming YAML nodes after NekoBox test: {len(streaming_alive_nodes)}\n"
        f"Total YAML proxy nodes without manual: {len(alive_nodes) + len(streaming_alive_nodes)}\n"
        f"Automatic strict pool before URL test: {len(auto_pool_nodes)}\n"
        f"Automatic Mihomo URL-test checked: {urltest_checked_count}\n"
        f"Automatic Mihomo URL-test result: {urltest_reason}\n"
        f"Automatic NekoBox/sing-box checked: {nekobox_checked_count}\n"
        f"Automatic NekoBox/sing-box result: {nekobox_reason}\n"
        f"Streaming strict pool before URL test: {len(streaming_pool_nodes_list)}\n"
        f"Streaming Mihomo URL-test checked: {streaming_urltest_checked_count}\n"
        f"Streaming Mihomo URL-test result: {streaming_urltest_reason}\n"
        f"Streaming NekoBox/sing-box checked: {streaming_nekobox_checked_count}\n"
        f"Streaming NekoBox/sing-box result: {streaming_nekobox_reason}\n"
        f"Manual group nodes: {len(manual_nodes)}\n"
        f"Akun txt automatic: {len([x for x in akun_text.splitlines() if x.strip()])}\n"
        f"Akun txt streaming: {len([x for x in streaming_akun_text.splitlines() if x.strip()])}\n"
        f"Akun txt manual: {len([x for x in manual_akun_text.splitlines() if x.strip()])}\n"
        f"Parsed subscription nodes standard: {len(all_nodes)}\n"
        f"Parsed subscription nodes streaming: {len(streaming_all_nodes)}\n"
        f"Fetched links standard: {len(fetch_logs)}\n"
        f"Fetched links streaming: {len(streaming_fetch_logs)}\n"
        f"Skipped raw URI standard: {len(skipped)}\n"
        f"Skipped raw URI streaming: {len(streaming_skipped)}\n"
        f"Skipped manual URI: {len(manual_skipped)}\n"
        f"Manual server normalized: {manual_server_changes} link\n"
        f"Manual nodes source file: {manual_file}\n"
        f"Bug server for akun txt/manual_nodes: {TARGET_SERVER}:443\n"
    )
    Path(output_stamp).write_text(summary, encoding="utf-8")

    print(summary)
    if len(alive_nodes) < min_output_nodes:
        print(f"[WARN] Node otomatis yang lolos NekoBox/sing-box test hanya {len(alive_nodes)}/{min_output_nodes}. YAML tetap dibuat dengan node yang tersedia.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
