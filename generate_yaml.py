from __future__ import annotations

import base64
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, urlencode

from sumberyaml_core import (
    ALT_TEST_URL,
    DEFAULT_LINKS,
    build_csv,
    build_openclash_yaml,
    process_sources,
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
    # Deduplicate while preserving order.
    unique: list[str] = []
    seen: set[str] = set()
    for link in links:
        if link not in seen:
            seen.add(link)
            unique.append(link)
    return "\n".join(unique)



def _get_ws_host(clash: dict) -> str:
    ws_opts = clash.get("ws-opts") if isinstance(clash.get("ws-opts"), dict) else {}
    headers = ws_opts.get("headers") if isinstance(ws_opts.get("headers"), dict) else {}
    host = headers.get("Host") or headers.get("host") or ""
    return str(host).strip()


def _get_ws_path(clash: dict) -> str:
    ws_opts = clash.get("ws-opts") if isinstance(clash.get("ws-opts"), dict) else {}
    path = str(ws_opts.get("path") or "/").strip() or "/"
    return path


def _get_alpn(clash: dict) -> str:
    alpn = clash.get("alpn")
    if isinstance(alpn, list):
        return ",".join(str(x).strip() for x in alpn if str(x).strip())
    if isinstance(alpn, str):
        return alpn.strip()
    return ""


def _node_to_account_link(node) -> str:
    """Convert the selected Clash node back to a share URI.

    akun.txt must follow the final YAML output, so the link uses the generated
    bug server, SNI, Host, path, and safe account name instead of blindly copying
    the raw public subscription URI.
    """
    clash = node.clash
    proto = str(clash.get("type") or node.type or "").lower()
    if proto not in {"vless", "vmess", "trojan"}:
        return ""

    name = str(clash.get("name") or node.name or "AKUN").strip() or "AKUN"
    server = str(clash.get("server") or "").strip()
    port = str(clash.get("port") or "443").strip()
    network = str(clash.get("network") or "tcp").strip().lower() or "tcp"
    sni = str(clash.get("servername") or clash.get("sni") or "").strip()
    fp = str(clash.get("client-fingerprint") or "").strip()
    alpn = _get_alpn(clash)
    host = _get_ws_host(clash)
    path = _get_ws_path(clash)

    if not server or not port:
        return ""

    if proto == "vless":
        uuid = str(clash.get("uuid") or "").strip()
        if not uuid:
            return ""
        params = {
            "encryption": "none",
            "security": "tls" if bool(clash.get("tls")) else "none",
            "type": network,
        }
        if sni:
            params["sni"] = sni
        if fp:
            params["fp"] = fp
        if alpn:
            params["alpn"] = alpn
        if network == "ws":
            params["path"] = path
            if host:
                params["host"] = host
        elif network == "grpc":
            grpc_opts = clash.get("grpc-opts") if isinstance(clash.get("grpc-opts"), dict) else {}
            service = str(grpc_opts.get("grpc-service-name") or "grpc").strip() or "grpc"
            params["serviceName"] = service
        flow = str(clash.get("flow") or "").strip()
        if flow:
            params["flow"] = flow
        return f"vless://{quote(uuid, safe='')}@{server}:{port}?{urlencode(params, safe='')}#{quote(name, safe='')}"

    if proto == "trojan":
        password = str(clash.get("password") or "").strip()
        if not password:
            return ""
        params = {
            "security": "tls",
            "type": network,
        }
        if sni:
            params["sni"] = sni
        if fp:
            params["fp"] = fp
        if alpn:
            params["alpn"] = alpn
        if network == "ws":
            params["path"] = path
            if host:
                params["host"] = host
        elif network == "grpc":
            grpc_opts = clash.get("grpc-opts") if isinstance(clash.get("grpc-opts"), dict) else {}
            service = str(grpc_opts.get("grpc-service-name") or "grpc").strip() or "grpc"
            params["serviceName"] = service
        return f"trojan://{quote(password, safe='')}@{server}:{port}?{urlencode(params, safe='')}#{quote(name, safe='')}"

    if proto == "vmess":
        uuid = str(clash.get("uuid") or "").strip()
        if not uuid:
            return ""
        vmess_data = {
            "v": "2",
            "ps": name,
            "add": server,
            "port": port,
            "id": uuid,
            "aid": str(clash.get("alterId") if clash.get("alterId") is not None else 0),
            "scy": str(clash.get("cipher") or "auto"),
            "net": network,
            "type": "none",
            "host": host if network == "ws" else "",
            "path": path if network == "ws" else "",
            "tls": "tls" if bool(clash.get("tls")) else "",
            "sni": sni,
        }
        if fp:
            vmess_data["fp"] = fp
        if alpn:
            vmess_data["alpn"] = alpn
        encoded = base64.b64encode(json.dumps(vmess_data, ensure_ascii=False, separators=(",", ":")).encode("utf-8")).decode("ascii")
        return f"vmess://{encoded}"

    return ""


def build_akun_txt(nodes) -> str:
    links: list[str] = []
    seen: set[str] = set()
    for node in nodes:
        link = _node_to_account_link(node).strip()
        if link and link not in seen:
            seen.add(link)
            links.append(link)
    return "\n".join(links) + ("\n" if links else "")

def main() -> int:
    output_yaml = os.getenv("OUTPUT_YAML", "openclash_auto.yaml")
    output_csv = os.getenv("OUTPUT_CSV", "openclash_auto_report.csv")
    output_stamp = os.getenv("OUTPUT_STAMP", "last_update.txt")
    output_akun = os.getenv("OUTPUT_AKUN", "akun.txt")
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

    print("[INFO] Generate YAML OpenClash otomatis")
    print(f"[INFO] Target output: {max_nodes} node, minimal: {min_output_nodes} node")
    print(f"[INFO] Links subscription: {len([x for x in links_text.splitlines() if x.strip()])}")

    alive_nodes, all_nodes, fetch_logs, skipped = process_sources(
        links_text=links_text,
        manual_text=manual_text,
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
    csv_text = build_csv(all_nodes)
    akun_text = build_akun_txt(alive_nodes)

    Path(output_yaml).write_text(yaml_text, encoding="utf-8")
    Path(output_csv).write_text(csv_text, encoding="utf-8")
    Path(output_akun).write_text(akun_text, encoding="utf-8")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    summary = (
        f"Last update: {now}\n"
        f"YAML nodes: {len(alive_nodes)}\n"
        f"Akun links: {len([line for line in akun_text.splitlines() if line.strip()])}\n"
        f"Parsed nodes: {len(all_nodes)}\n"
        f"Fetched links: {len(fetch_logs)}\n"
        f"Skipped raw URI: {len(skipped)}\n"
    )
    Path(output_stamp).write_text(summary, encoding="utf-8")

    print(summary)
    if len(alive_nodes) < min_output_nodes:
        print(f"[WARN] Node strict yang lolos hanya {len(alive_nodes)}/{min_output_nodes}. YAML tetap dibuat dengan node yang tersedia.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
