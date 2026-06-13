from __future__ import annotations

import base64
import concurrent.futures
import csv
import html
import io
import json
import os
import re
import socket
import ssl
import statistics
import time
from dataclasses import dataclass, field
from typing import Any
from urllib.parse import parse_qs, quote, unquote, urlparse

import requests
import yaml

DEFAULT_LINKS = [
    "https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/xray/normal/mix",
    "https://raw.githubusercontent.com/arshiacomplus/v2rayExtractor/refs/heads/main/mix/sub.html",
    "https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt",
    "https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity.txt",
    "https://raw.githubusercontent.com/Everyday-VPN/Everyday-VPN/main/subscription/main.txt",
    "https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt",
    "https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/All_Configs_Sub.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/trojan.txt",
    "https://raw.githubusercontent.com/ebrasha/free-v2ray-public-list/main/vmess_configs.txt",
    "https://raw.githubusercontent.com/Argh94/Proxy-List/refs/heads/main/Trojan.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/26.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/25.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/24.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/23.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/22.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/21.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/20.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/19.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/18.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/17.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/16.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/15.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/14.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/13.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/12.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/11.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/10.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/9.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/8.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/7.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/6.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/5.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/4.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/3.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/2.txt",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/1.txt",
    "https://raw.githubusercontent.com/sakha1370/OpenRay/refs/heads/main/output/kind/vmess.txt",
    "https://raw.githubusercontent.com/sakha1370/OpenRay/refs/heads/main/output/kind/vless.txt",
    "https://raw.githubusercontent.com/sakha1370/OpenRay/refs/heads/main/output/kind/trojan.txt",
]

TARGET_SERVER = "104.17.3.81"
ONLY_PORT = 443
USER_AGENT = "Mozilla/5.0 SumberYAML-OpenClash-BugCompat/3.0"
URI_RE = re.compile(r"(?:vless|vmess|trojan|ss)://[^\s<'\"`]+", re.IGNORECASE)
FAST_TEST_URL = "http://cp.cloudflare.com/generate_204"
ALT_TEST_URL = "http://www.gstatic.com/generate_204"
THIRD_TEST_URL = "https://www.google.com/generate_204"
FAST_TARGET_DELAY_MS = 123
DEFAULT_FILL_DELAY_MS = 400
HARD_MAX_DELAY_MS = 1500
MIN_OUTPUT_NODES = 20
DEFAULT_URLTEST_INTERVAL = 60
DEFAULT_TOLERANCE_MS = 40
DEFAULT_TCP_TIMEOUT = 1.5
DEFAULT_FETCH_TIMEOUT = 15
DEFAULT_HEALTH_TIMEOUT_MS = 5000
DEFAULT_RESERVE_POOL_NODES = 100
DEFAULT_FORCE_WS_ONLY = True

OPTIMIZATION_PRESETS: dict[str, dict[str, Any]] = {
    "Cepat": {
        "max_nodes": 20,
        "min_output_nodes": 15,
        "fill_delay_ms": 400,
        "attempts": 2,
        "require_successes": 1,
        "tcp_timeout": 1.5,
        "max_workers": 64,
        "fetch_timeout": 10,
        "urltest_interval": 60,
        "tolerance": 50,
        "require_original": False,
        "candidate_multiplier": 40,
        "candidate_min": 1000,
        "reserve_pool_nodes": 60,
        "max_jitter_ms": 200,
        "rule_mode": "Lite",
        "force_ws_only": True,
        "health_timeout_ms": 5000,
    },
    "Seimbang": {
        "max_nodes": 20,
        "min_output_nodes": 20,
        "fill_delay_ms": 800,
        "attempts": 3,
        "require_successes": 2,
        "tcp_timeout": 2.0,
        "max_workers": 64,
        "fetch_timeout": 15,
        "urltest_interval": 60,
        "tolerance": 50,
        "require_original": False,
        "candidate_multiplier": 80,
        "candidate_min": 2000,
        "reserve_pool_nodes": 100,
        "max_jitter_ms": 300,
        "rule_mode": "Lite",
        "force_ws_only": True,
        "health_timeout_ms": 5000,
    },
    "Kejar 20 Hidup": {
        "max_nodes": 20,
        "min_output_nodes": 20,
        "fill_delay_ms": 1200,
        "attempts": 4,
        "require_successes": 3,
        "tcp_timeout": 3.0,
        "max_workers": 80,
        "fetch_timeout": 20,
        "urltest_interval": 60,
        "tolerance": 80,
        "require_original": False,
        "candidate_multiplier": 120,
        "candidate_min": 3000,
        "reserve_pool_nodes": 160,
        "max_jitter_ms": 500,
        "rule_mode": "Lite",
        "force_ws_only": True,
        "health_timeout_ms": 6000,
    },
    "Ketat": {
        "max_nodes": 20,
        "min_output_nodes": 20,
        "fill_delay_ms": 1500,
        "attempts": 5,
        "require_successes": 4,
        "tcp_timeout": 3.0,
        "max_workers": 60,
        "fetch_timeout": 25,
        "urltest_interval": 90,
        "tolerance": 60,
        "require_original": True,
        "candidate_multiplier": 120,
        "candidate_min": 3000,
        "reserve_pool_nodes": 160,
        "max_jitter_ms": 500,
        "rule_mode": "Lengkap",
        "force_ws_only": True,
        "health_timeout_ms": 6000,
    },
}


@dataclass
class ProxyNode:
    name: str
    type: str
    original_server: str
    port: int
    raw: str
    clash: dict[str, Any]
    source: str = "manual"
    status: str = "pending"
    best_delay_ms: int | None = None
    avg_delay_ms: int | None = None
    jitter_ms: int | None = None
    success_count: int = 0
    attempts: int = 0
    score: int = 999999
    reason: str = ""
    original_best_delay_ms: int | None = None
    bug_best_delay_ms: int | None = None
    bug_avg_delay_ms: int | None = None
    bug_jitter_ms: int | None = None
    bug_success_count: int = 0
    original_success_count: int = 0
    bug_sni: str = ""
    ws_upgrade_ms: int | None = None
    ws_success_count: int = 0
    ws_status: str = ""
    tier: str = ""
    original_name: str = ""
    key: str = field(default="")


def b64decode_text(value: str) -> str | None:
    if not value:
        return None
    cleaned = re.sub(r"\s+", "", value.strip())
    if not cleaned:
        return None
    padding = "=" * (-len(cleaned) % 4)
    candidates = [cleaned + padding, cleaned.replace("-", "+").replace("_", "/") + padding]
    for candidate in candidates:
        try:
            data = base64.b64decode(candidate, validate=False)
            text = data.decode("utf-8", errors="ignore")
            if text and len(text.strip()) >= 4:
                return text
        except Exception:
            continue
    return None


def normalize_name(name: str | None, fallback: str) -> str:
    text = html.unescape(unquote(name or "")).strip()
    text = re.sub(r"[\x00-\x1f\x7f\r\n\t]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = text[:70].strip(" -_|/")
    return text or fallback


def safe_proxy_name(value: str | None, fallback: str) -> str:
    """Return an OpenClash-safe proxy name.

    Public subscription names often contain emoji, quotes, slashes, hidden newline,
    YAML-reserved characters, or duplicate text. Some OpenClash builds reject those
    names. This function converts every proxy name to a short ASCII-only alias.
    """
    text = html.unescape(unquote(value or "")).strip()
    text = re.sub(r"[\x00-\x1f\x7f]+", "", text)
    text = re.sub(r"[^A-Za-z0-9_.-]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-._")
    if not text:
        text = fallback
    text = text[:64].strip("-._") or fallback
    if not re.fullmatch(r"[A-Za-z0-9_.-]{1,64}", text):
        text = fallback
    return text


def unique_names(nodes: list[ProxyNode]) -> None:
    """Replace all proxy names with safe unique aliases.

    The generated names intentionally do not reuse the public subscription name,
    because those names are the common source of OpenClash import errors.
    Original names are kept only in the CSV report.
    """
    seen: set[str] = set()
    for i, node in enumerate(nodes, start=1):
        node.original_name = node.original_name or normalize_name(node.name, f"ORIGINAL-{i:03d}")
        delay = f"{int(node.best_delay_ms)}MS" if node.best_delay_ms is not None else "NA"
        proto = safe_proxy_name(node.type.upper(), "NODE")
        base = safe_proxy_name(f"AKUN-{i:03d}-{proto}-{delay}", f"AKUN-{i:03d}")
        name = base
        counter = 2
        while name in seen:
            suffix = f"-{counter}"
            name = (base[: 64 - len(suffix)] + suffix).strip("-._")
            counter += 1
        seen.add(name)
        node.name = name
        node.clash["name"] = name


def first_query(params: dict[str, list[str]], *names: str, default: str = "") -> str:
    for name in names:
        if name in params and params[name]:
            return params[name][0]
    return default


def is_supported_network(network: str) -> bool:
    return (network or "tcp").lower() in {"tcp", "ws", "grpc", "h2", "http"}


def parse_vless(uri: str, source: str) -> ProxyNode | None:
    parsed = urlparse(uri)
    uuid = parsed.username or ""
    server = parsed.hostname or ""
    port = parsed.port or 0
    if not uuid or not server or port != ONLY_PORT:
        return None

    params = parse_qs(parsed.query)
    network = (first_query(params, "type", default="tcp") or "tcp").lower()
    if not is_supported_network(network):
        return None
    security = (first_query(params, "security", default="tls") or "tls").lower()
    sni = first_query(params, "sni", "servername", "peer", default="") or server
    host = first_query(params, "host", default="") or sni or server
    path = first_query(params, "path", default="/") or "/"
    flow = first_query(params, "flow", default="")
    fp = first_query(params, "fp", default="chrome") or "chrome"
    alpn = first_query(params, "alpn", default="")

    name = normalize_name(parsed.fragment, f"VLESS-{server}")
    clash: dict[str, Any] = {
        "name": name,
        "type": "vless",
        "server": TARGET_SERVER,
        "port": ONLY_PORT,
        "uuid": uuid,
        "udp": True,
        "tls": security in {"tls", "reality"} or port == 443,
        "servername": sni,
        "network": "http" if network == "h2" else network,
        "client-fingerprint": fp,
        "skip-cert-verify": True,
    }
    if flow:
        clash["flow"] = flow
    if alpn:
        clash["alpn"] = [x.strip() for x in alpn.split(",") if x.strip()]
    if network == "ws":
        clash["ws-opts"] = {"path": path, "headers": {"Host": host}}
    elif network == "grpc":
        service_name = first_query(params, "serviceName", "service-name", default="")
        clash["grpc-opts"] = {"grpc-service-name": service_name or "grpc"}
    elif network in {"h2", "http"}:
        clash["http-opts"] = {"method": "GET", "path": [path], "headers": {"Host": [host]}}
    if security == "reality":
        pbk = first_query(params, "pbk", "public-key", default="")
        sid = first_query(params, "sid", "short-id", default="")
        clash["reality-opts"] = {}
        if pbk:
            clash["reality-opts"]["public-key"] = pbk
        if sid:
            clash["reality-opts"]["short-id"] = sid

    key = f"vless|{uuid}|{server}|{port}|{network}|{path}|{host}"
    return ProxyNode(name, "vless", server, port, uri, clash, source=source, key=key)


def parse_trojan(uri: str, source: str) -> ProxyNode | None:
    parsed = urlparse(uri)
    password = parsed.username or ""
    server = parsed.hostname or ""
    port = parsed.port or 0
    if not password or not server or port != ONLY_PORT:
        return None

    params = parse_qs(parsed.query)
    network = (first_query(params, "type", default="tcp") or "tcp").lower()
    if not is_supported_network(network):
        return None
    sni = first_query(params, "sni", "peer", "servername", default="") or server
    host = first_query(params, "host", default="") or sni or server
    path = first_query(params, "path", default="/") or "/"
    alpn = first_query(params, "alpn", default="")

    name = normalize_name(parsed.fragment, f"TROJAN-{server}")
    clash: dict[str, Any] = {
        "name": name,
        "type": "trojan",
        "server": TARGET_SERVER,
        "port": ONLY_PORT,
        "password": unquote(password),
        "udp": True,
        "sni": sni,
        "skip-cert-verify": True,
        "network": "http" if network == "h2" else network,
    }
    if alpn:
        clash["alpn"] = [x.strip() for x in alpn.split(",") if x.strip()]
    if network == "ws":
        clash["ws-opts"] = {"path": path, "headers": {"Host": host}}
    elif network == "grpc":
        service_name = first_query(params, "serviceName", "service-name", default="")
        clash["grpc-opts"] = {"grpc-service-name": service_name or "grpc"}
    elif network in {"h2", "http"}:
        clash["http-opts"] = {"method": "GET", "path": [path], "headers": {"Host": [host]}}

    key = f"trojan|{password}|{server}|{port}|{network}|{path}|{host}"
    return ProxyNode(name, "trojan", server, port, uri, clash, source=source, key=key)


def parse_vmess(uri: str, source: str) -> ProxyNode | None:
    payload = uri.split("://", 1)[1].split("#", 1)[0]
    decoded = b64decode_text(payload)
    if not decoded:
        return None
    try:
        data = json.loads(decoded)
    except Exception:
        return None

    server = str(data.get("add") or data.get("server") or "").strip()
    try:
        port = int(data.get("port") or 0)
    except Exception:
        port = 0
    uuid = str(data.get("id") or "").strip()
    if not server or not uuid or port != ONLY_PORT:
        return None

    network = str(data.get("net") or "tcp").strip().lower() or "tcp"
    if not is_supported_network(network):
        return None
    tls_value = str(data.get("tls") or "tls").strip().lower()
    sni = str(data.get("sni") or data.get("host") or server).strip()
    host = str(data.get("host") or sni or server).strip()
    path = str(data.get("path") or "/").strip() or "/"
    cipher = str(data.get("scy") or data.get("cipher") or "auto").strip() or "auto"
    fp = str(data.get("fp") or "chrome").strip() or "chrome"

    name = normalize_name(str(data.get("ps") or ""), f"VMESS-{server}")
    clash: dict[str, Any] = {
        "name": name,
        "type": "vmess",
        "server": TARGET_SERVER,
        "port": ONLY_PORT,
        "uuid": uuid,
        "alterId": int(data.get("aid") or 0),
        "cipher": cipher,
        "udp": True,
        "tls": tls_value in {"tls", "true", "1"} or port == 443,
        "servername": sni,
        "network": "http" if network == "h2" else network,
        "client-fingerprint": fp,
        "skip-cert-verify": True,
    }
    if network == "ws":
        clash["ws-opts"] = {"path": path, "headers": {"Host": host}}
    elif network == "grpc":
        clash["grpc-opts"] = {"grpc-service-name": path.strip("/") or "grpc"}
    elif network in {"h2", "http"}:
        clash["http-opts"] = {"method": "GET", "path": [path], "headers": {"Host": [host]}}

    key = f"vmess|{uuid}|{server}|{port}|{network}|{path}|{host}"
    return ProxyNode(name, "vmess", server, port, uri, clash, source=source, key=key)


def decode_ss_userinfo(userinfo: str) -> tuple[str, str] | None:
    userinfo = unquote(userinfo or "")
    decoded = b64decode_text(userinfo) or userinfo
    if ":" not in decoded:
        return None
    method, password = decoded.split(":", 1)
    method = method.strip()
    password = password.strip()
    if not method or not password:
        return None
    return method, password


def parse_ss(uri: str, source: str) -> ProxyNode | None:
    raw_without_scheme = uri.split("://", 1)[1]
    name = ""
    if "#" in raw_without_scheme:
        raw_without_scheme, name = raw_without_scheme.split("#", 1)
        name = unquote(name)
    raw_without_scheme = raw_without_scheme.split("?", 1)[0]

    method = password = server = ""
    port = 0

    if "@" in raw_without_scheme:
        userinfo, serverpart = raw_without_scheme.rsplit("@", 1)
        credentials = decode_ss_userinfo(userinfo)
        if not credentials:
            return None
        method, password = credentials
        parsed_server = urlparse("ss://" + serverpart)
        server = parsed_server.hostname or ""
        port = parsed_server.port or 0
    else:
        decoded = b64decode_text(raw_without_scheme)
        if not decoded or "@" not in decoded:
            return None
        userinfo, serverpart = decoded.rsplit("@", 1)
        credentials = decode_ss_userinfo(userinfo)
        if not credentials:
            return None
        method, password = credentials
        parsed_server = urlparse("ss://" + serverpart)
        server = parsed_server.hostname or ""
        port = parsed_server.port or 0

    if not server or port != ONLY_PORT:
        return None

    final_name = normalize_name(name, f"SS-{server}")
    clash: dict[str, Any] = {
        "name": final_name,
        "type": "ss",
        "server": TARGET_SERVER,
        "port": ONLY_PORT,
        "cipher": method,
        "password": password,
        "udp": True,
    }
    key = f"ss|{method}|{password}|{server}|{port}"
    return ProxyNode(final_name, "ss", server, port, uri, clash, source=source, key=key)


def parse_uri(uri: str, source: str) -> ProxyNode | None:
    uri = html.unescape(uri.strip()).strip("'\",[]()")
    if not uri or "://" not in uri:
        return None
    scheme = uri.split("://", 1)[0].lower()
    try:
        if scheme == "vless":
            return parse_vless(uri, source)
        if scheme == "trojan":
            return parse_trojan(uri, source)
        if scheme == "vmess":
            return parse_vmess(uri, source)
        if scheme == "ss":
            return parse_ss(uri, source)
    except Exception:
        return None
    return None


def extract_uris(text: str) -> list[str]:
    if not text:
        return []
    chunks: list[str] = []
    text = html.unescape(text)
    text = text.replace("<br>", "\n").replace("<br/>", "\n").replace("<br />", "\n")
    chunks.append(text)
    decoded = b64decode_text(text)
    if decoded and decoded != text:
        chunks.append(html.unescape(decoded))
    found: list[str] = []
    for chunk in chunks:
        for match in URI_RE.findall(chunk):
            uri = match.strip().rstrip(",;)]}'\"")
            found.append(uri)
    unique: list[str] = []
    seen = set()
    for uri in found:
        if uri not in seen:
            seen.add(uri)
            unique.append(uri)
    return unique


def fetch_url(url: str, timeout: int) -> tuple[str, str, str]:
    try:
        response = requests.get(url, timeout=timeout, headers={"User-Agent": USER_AGENT})
        response.raise_for_status()
        text = response.text or ""
        if not text.strip():
            return url, "", f"dead: HTTP {response.status_code}, kosong"
        return url, text, f"alive: HTTP {response.status_code}"
    except Exception as exc:
        return url, "", f"dead: {exc}"


def fetch_url_cached(url: str, timeout: int) -> tuple[str, str, str]:
    """Fetch subscription URL. The Streamlit app version may cache this; CLI mode keeps it direct."""
    return fetch_url(url, timeout)


def one_tcp_delay(host: str, port: int, timeout: float) -> int | None:
    start = time.perf_counter()
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return int((time.perf_counter() - start) * 1000)
    except Exception:
        return None


def stability_check(host: str, port: int, timeout: float, attempts: int) -> tuple[bool, dict[str, Any]]:
    delays: list[int] = []
    last_error = ""
    for _ in range(max(1, attempts)):
        start = time.perf_counter()
        try:
            with socket.create_connection((host, port), timeout=timeout):
                delays.append(int((time.perf_counter() - start) * 1000))
        except Exception as exc:
            last_error = str(exc)
        # small gap so a node with one lucky accept is less likely to pass every attempt instantly
        time.sleep(0.03)

    if not delays:
        return False, {
            "best_delay_ms": None,
            "avg_delay_ms": None,
            "jitter_ms": None,
            "success_count": 0,
            "attempts": attempts,
            "score": 999999,
            "reason": last_error or "timeout",
        }

    best = min(delays)
    avg = int(statistics.mean(delays))
    jitter = int(max(delays) - min(delays)) if len(delays) > 1 else 0
    # Score favors low latency, stable repeated success, and low jitter.
    score = best + int(jitter * 0.7) + int((attempts - len(delays)) * 120)
    return True, {
        "best_delay_ms": best,
        "avg_delay_ms": avg,
        "jitter_ms": jitter,
        "success_count": len(delays),
        "attempts": attempts,
        "score": score,
        "reason": "alive",
    }


def looks_like_ip(host: str) -> bool:
    try:
        socket.inet_aton(host)
        return True
    except Exception:
        return False


def node_sni_host(node: ProxyNode) -> str:
    clash = node.clash
    # VLESS/VMess commonly use servername; Trojan commonly uses sni.
    candidates: list[str] = []
    for key in ("servername", "sni"):
        value = str(clash.get(key) or "").strip()
        if value:
            candidates.append(value)
    ws_host = clash.get("ws-opts", {}).get("headers", {}).get("Host", "") if isinstance(clash.get("ws-opts"), dict) else ""
    if isinstance(ws_host, str) and ws_host.strip():
        candidates.append(ws_host.strip())
    http_host = clash.get("http-opts", {}).get("headers", {}).get("Host", []) if isinstance(clash.get("http-opts"), dict) else []
    if isinstance(http_host, list) and http_host:
        candidates.append(str(http_host[0]).strip())
    candidates.append(node.original_server)
    for candidate in candidates:
        candidate = candidate.strip().strip("[]")
        if candidate and not looks_like_ip(candidate):
            return candidate
    return node.original_server


def node_network(node: ProxyNode) -> str:
    """Return the normalized transport network used by the proxy node."""
    if str(node.type or "").lower() == "ss":
        return "ss"
    network = str(node.clash.get("network") or "tcp").strip().lower()
    if network in {"h2", "http"}:
        return "http"
    return network or "tcp"


def protocol_priority_rank(node: ProxyNode) -> int:
    """Prefer protocols that usually work better with bug server + SNI/Host."""
    return {"vless": 0, "trojan": 1, "vmess": 2, "ss": 3}.get(str(node.type or "").lower(), 9)


def network_priority_rank(node: ProxyNode, prefer_ws: bool = True) -> int:
    """When prefer_ws is enabled, WebSocket nodes are tested and selected first."""
    if not prefer_ws:
        return 0
    return {"ws": 0, "grpc": 1, "http": 2, "tcp": 3, "ss": 4}.get(node_network(node), 9)


def node_sort_key(node: ProxyNode, prefer_ws: bool = True) -> tuple[int, int, int, int, int]:
    return (
        network_priority_rank(node, prefer_ws),
        protocol_priority_rank(node),
        int(node.score or 999999),
        int(node.best_delay_ms or 999999),
        int(node.jitter_ms or 999999),
    )


def domain_root(host: str) -> str:
    """Return a simple root domain used only for soft diversity scoring."""
    text = str(host or "").strip().lower().strip(".")
    if not text or looks_like_ip(text):
        return text
    parts = [p for p in text.split(".") if p]
    if len(parts) <= 2:
        return text
    # Keep common 2-level public suffixes together enough for our duplicate filter.
    if parts[-2] in {"co", "com", "net", "org", "ac", "sch", "web", "or"} and len(parts[-1]) == 2 and len(parts) >= 3:
        return ".".join(parts[-3:])
    return ".".join(parts[-2:])


def node_identity_key(node: ProxyNode) -> tuple[str, str, str, str, str]:
    """Hard duplicate key: same protocol/account/host/path should appear only once."""
    clash = node.clash or {}
    credential = str(clash.get("uuid") or clash.get("password") or "").strip().lower()
    return (
        str(node.type or "").lower(),
        credential,
        node_network(node),
        ws_host_header(node).lower() if node_network(node) == "ws" else node_sni_host(node).lower(),
        ws_path(node) if node_network(node) == "ws" else str(node.original_server).lower(),
    )


def select_diverse_nodes(nodes: list[ProxyNode], limit: int, prefer_ws: bool = True) -> list[ProxyNode]:
    """Pick stable nodes while avoiding many copies of the same host/root domain.

    This is intentionally soft: it first takes one per exact identity, then limits
    root-domain concentration. If that makes the result too small, it fills from
    the remaining alive nodes so the app can still pursue the requested 20 output.
    """
    sorted_nodes = sorted(nodes, key=lambda n: node_sort_key(n, prefer_ws))
    selected: list[ProxyNode] = []
    seen_identity: set[tuple[str, str, str, str, str]] = set()
    root_counts: dict[str, int] = {}

    for node in sorted_nodes:
        ident = node_identity_key(node)
        if ident in seen_identity:
            continue
        root = domain_root(ws_host_header(node) if node_network(node) == "ws" else node_sni_host(node))
        # Keep some diversity, but allow up to 4 nodes per root because public CF
        # pools can legitimately host several working accounts on one root domain.
        if root and root_counts.get(root, 0) >= 4:
            continue
        selected.append(node)
        seen_identity.add(ident)
        if root:
            root_counts[root] = root_counts.get(root, 0) + 1
        if len(selected) >= limit:
            return selected

    # Fill if strict diversity was too limiting.
    selected_ids = {id(n) for n in selected}
    for node in sorted_nodes:
        if id(node) in selected_ids:
            continue
        ident = node_identity_key(node)
        if ident in seen_identity:
            continue
        selected.append(node)
        seen_identity.add(ident)
        if len(selected) >= limit:
            break
    return selected


def ws_path(node: ProxyNode) -> str:
    ws_opts = node.clash.get("ws-opts") if isinstance(node.clash, dict) else None
    path = ws_opts.get("path") if isinstance(ws_opts, dict) else "/"
    path = str(path or "/").strip() or "/"
    if not path.startswith("/"):
        path = "/" + path
    # Request-line must be ASCII. Keep existing percent escapes and common URL chars.
    return quote(path, safe="/%?&=:+,;@._~!$'()*-[]")


def ws_host_header(node: ProxyNode) -> str:
    ws_opts = node.clash.get("ws-opts") if isinstance(node.clash, dict) else None
    if isinstance(ws_opts, dict):
        headers = ws_opts.get("headers")
        if isinstance(headers, dict):
            host = headers.get("Host") or headers.get("host")
            if isinstance(host, str) and host.strip():
                return host.strip()
    return node_sni_host(node)


def is_placeholder_uuid(value: str | None) -> bool:
    uuid = str(value or "").strip().lower()
    compact = uuid.replace("-", "")
    placeholder_set = {
        "00000000-0000-0000-0000-000000000000",
        "ffffffff-ffff-ffff-ffff-ffffffffffff",
        "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
        "aaaaaabb-4ddd-4eee-9fff-ffffffffffff",
    }
    if uuid in placeholder_set:
        return True
    if re.fullmatch(r"[0-9a-f]{32}", compact):
        # Reject obvious public-list dummy UUIDs made mostly from a/f/0/1.
        dominant = max(compact.count(ch) for ch in set(compact)) if compact else 0
        if dominant >= 20 and len(set(compact)) <= 5:
            return True
    return False


def harden_ws_node(node: ProxyNode) -> None:
    """Make WS output closer to what OpenClash/Mihomo expects."""
    if node_network(node) != "ws":
        return
    node.clash["alpn"] = ["http/1.1"]
    ws_opts = node.clash.setdefault("ws-opts", {})
    if not isinstance(ws_opts, dict):
        ws_opts = {}
        node.clash["ws-opts"] = ws_opts
    ws_opts["path"] = ws_path(node)
    headers = ws_opts.setdefault("headers", {})
    if not isinstance(headers, dict):
        headers = {}
        ws_opts["headers"] = headers
    headers["Host"] = str(headers.get("Host") or headers.get("host") or node_sni_host(node)).strip()


PLACEHOLDER_VALUES = {"", "-", "none", "null", "undefined", "nil", "nan"}


def complete_value(value: Any) -> bool:
    """True if a config value is meaningful enough to be written to YAML."""
    if value is None:
        return False
    if isinstance(value, str):
        text = html.unescape(unquote(value)).strip()
        return text.lower() not in PLACEHOLDER_VALUES
    if isinstance(value, (list, tuple, set)):
        return any(complete_value(item) for item in value)
    if isinstance(value, dict):
        return bool(value)
    return True


def get_nested(data: dict[str, Any], *keys: str) -> Any:
    current: Any = data
    for key in keys:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current


def has_host_value(value: Any) -> bool:
    if isinstance(value, list):
        return any(complete_value(item) for item in value)
    return complete_value(value)


def validate_network_options(clash: dict[str, Any], missing: list[str]) -> None:
    network = str(clash.get("network") or "tcp").lower()
    if network == "ws":
        ws_opts = clash.get("ws-opts")
        if not isinstance(ws_opts, dict):
            missing.append("ws-opts")
            return
        if not complete_value(ws_opts.get("path")):
            missing.append("ws-opts.path")
        if not has_host_value(get_nested(ws_opts, "headers", "Host")):
            missing.append("ws-opts.headers.Host")
    elif network == "grpc":
        grpc_opts = clash.get("grpc-opts")
        if not isinstance(grpc_opts, dict):
            missing.append("grpc-opts")
            return
        if not complete_value(grpc_opts.get("grpc-service-name")):
            missing.append("grpc-opts.grpc-service-name")
    elif network == "http":
        http_opts = clash.get("http-opts")
        if not isinstance(http_opts, dict):
            missing.append("http-opts")
            return
        if not complete_value(http_opts.get("path")):
            missing.append("http-opts.path")
        if not has_host_value(get_nested(http_opts, "headers", "Host")):
            missing.append("http-opts.headers.Host")


def validate_complete_node(node: ProxyNode) -> tuple[bool, str]:
    """Reject incomplete public accounts before they are tested or written.

    Because the output server is forced to the Cloudflare bug IP, a usable account
    must have enough protocol information for OpenClash/Mihomo to build the real
    connection: credentials, TLS SNI/Host where applicable, network-specific
    options, and port 443.
    """
    clash = node.clash
    missing: list[str] = []

    if node.port != ONLY_PORT:
        missing.append("port 443")
    if not complete_value(node.original_server):
        missing.append("original_server")
    if not complete_value(clash.get("type")):
        missing.append("type")
    if not complete_value(clash.get("server")):
        missing.append("server")
    if not complete_value(clash.get("port")):
        missing.append("port")

    proto = str(clash.get("type") or node.type or "").lower()
    network = str(clash.get("network") or "tcp").lower()

    if proto in {"vless", "vmess", "trojan"}:
        sni = node_sni_host(node)
        node.bug_sni = sni
        if not complete_value(sni) or looks_like_ip(str(sni)):
            missing.append("SNI/Host domain")
        if network not in {"tcp", "ws", "grpc", "http"}:
            missing.append("network")
        validate_network_options(clash, missing)

    if proto == "vless":
        if not complete_value(clash.get("uuid")):
            missing.append("uuid")
        elif is_placeholder_uuid(str(clash.get("uuid"))):
            missing.append("uuid placeholder")
        if not complete_value(clash.get("servername")):
            missing.append("servername")
        if str(clash.get("tls", "")).lower() in {"false", "0", "none"}:
            missing.append("tls")
        if isinstance(clash.get("reality-opts"), dict):
            reality_opts = clash.get("reality-opts") or {}
            if not complete_value(reality_opts.get("public-key")):
                missing.append("reality-opts.public-key")
    elif proto == "vmess":
        if not complete_value(clash.get("uuid")):
            missing.append("uuid")
        elif is_placeholder_uuid(str(clash.get("uuid"))):
            missing.append("uuid placeholder")
        if not complete_value(clash.get("cipher")):
            missing.append("cipher")
        if not complete_value(clash.get("servername")):
            missing.append("servername")
        if str(clash.get("tls", "")).lower() in {"false", "0", "none"}:
            missing.append("tls")
        try:
            int(clash.get("alterId"))
        except Exception:
            missing.append("alterId")
    elif proto == "trojan":
        if not complete_value(clash.get("password")):
            missing.append("password")
        if not complete_value(clash.get("sni")):
            missing.append("sni")
    elif proto == "ss":
        if not complete_value(clash.get("cipher")):
            missing.append("cipher")
        if not complete_value(clash.get("password")):
            missing.append("password")
        # Plain Shadowsocks cannot carry SNI/Host when the server is replaced by
        # the bug IP. Keeping it would often create YAML that imports but cannot
        # connect through 104.17.3.81.
        if str(node.original_server).strip() != TARGET_SERVER:
            missing.append("ss tidak kompatibel dengan bug server tanpa SNI/Host")
    else:
        missing.append("protocol unsupported")

    if missing:
        unique_missing = []
        seen = set()
        for item in missing:
            if item not in seen:
                seen.add(item)
                unique_missing.append(item)
        return False, "incomplete: " + ", ".join(unique_missing[:10])
    return True, "complete"


def tls_bug_delay(node: ProxyNode, timeout: float, attempts: int) -> tuple[bool, dict[str, Any]]:
    """Measure whether TARGET_SERVER:443 can complete TLS with the node SNI/Host.

    This is the important check when the YAML output forces server to 104.17.3.81.
    It does not replace OpenClash url-test, but it prevents many accounts whose SNI/Host
    cannot work through the selected bug IP from entering the generated YAML.
    """
    sni = node_sni_host(node)
    node.bug_sni = sni
    delays: list[int] = []
    last_error = ""
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    for _ in range(max(1, attempts)):
        start = time.perf_counter()
        try:
            raw = socket.create_connection((TARGET_SERVER, ONLY_PORT), timeout=timeout)
            raw.settimeout(timeout)
            with raw:
                with context.wrap_socket(raw, server_hostname=sni):
                    delays.append(int((time.perf_counter() - start) * 1000))
        except Exception as exc:
            last_error = str(exc)
        time.sleep(0.03)

    if not delays:
        return False, {
            "best_delay_ms": None,
            "avg_delay_ms": None,
            "jitter_ms": None,
            "success_count": 0,
            "attempts": attempts,
            "score": 999999,
            "reason": last_error or "bug tls timeout",
        }
    best = min(delays)
    avg = int(statistics.mean(delays))
    jitter = int(max(delays) - min(delays)) if len(delays) > 1 else 0
    score = best + int(jitter * 0.8) + int((attempts - len(delays)) * 160)
    return True, {
        "best_delay_ms": best,
        "avg_delay_ms": avg,
        "jitter_ms": jitter,
        "success_count": len(delays),
        "attempts": attempts,
        "score": score,
        "reason": "bug-tls-alive",
    }


def ws_upgrade_delay(node: ProxyNode, timeout: float, attempts: int) -> tuple[bool, dict[str, Any]]:
    """Check TLS + WebSocket Upgrade through the selected bug IP.

    A node can complete TLS with Cloudflare but still fail OpenClash health check
    if the WS path/Host is wrong. This check only accepts HTTP 101 Switching Protocols.
    """
    sni = node_sni_host(node)
    host = ws_host_header(node)
    path = ws_path(node)
    node.bug_sni = sni
    delays: list[int] = []
    status_codes: list[int] = []
    last_error = ""
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    for _ in range(max(1, attempts)):
        start = time.perf_counter()
        try:
            raw = socket.create_connection((TARGET_SERVER, ONLY_PORT), timeout=timeout)
            raw.settimeout(timeout)
            with raw:
                with context.wrap_socket(raw, server_hostname=sni) as sock:
                    key = base64.b64encode(os.urandom(16)).decode("ascii")
                    request = (
                        f"GET {path} HTTP/1.1\r\n"
                        f"Host: {host}\r\n"
                        f"User-Agent: {USER_AGENT}\r\n"
                        "Connection: Upgrade\r\n"
                        "Upgrade: websocket\r\n"
                        "Sec-WebSocket-Version: 13\r\n"
                        f"Sec-WebSocket-Key: {key}\r\n"
                        "Pragma: no-cache\r\n"
                        "Cache-Control: no-cache\r\n"
                        "\r\n"
                    )
                    sock.sendall(request.encode("ascii", errors="ignore"))
                    response = sock.recv(512)
                    first_line = response.split(b"\r\n", 1)[0].decode("iso-8859-1", errors="ignore")
                    match = re.search(r"\s(\d{3})\s", first_line)
                    status = int(match.group(1)) if match else 0
                    status_codes.append(status)
                    if status == 101:
                        delays.append(int((time.perf_counter() - start) * 1000))
                    else:
                        last_error = first_line or f"HTTP {status}"
        except Exception as exc:
            last_error = str(exc)
        time.sleep(0.03)

    node.ws_success_count = len(delays)
    node.ws_upgrade_ms = min(delays) if delays else None
    node.ws_status = "101" if delays else (str(status_codes[-1]) if status_codes else str(last_error)[:80])

    if not delays:
        return False, {
            "best_delay_ms": None,
            "avg_delay_ms": None,
            "jitter_ms": None,
            "success_count": 0,
            "attempts": attempts,
            "score": 999999,
            "reason": f"ws upgrade gagal: {node.ws_status}",
        }

    best = min(delays)
    avg = int(statistics.mean(delays))
    jitter = int(max(delays) - min(delays)) if len(delays) > 1 else 0
    score = best + int(jitter * 0.9) + int((attempts - len(delays)) * 220)
    return True, {
        "best_delay_ms": best,
        "avg_delay_ms": avg,
        "jitter_ms": jitter,
        "success_count": len(delays),
        "attempts": attempts,
        "score": score,
        "reason": "bug-ws-101-alive",
    }


def check_node_bug_compat(node: ProxyNode, timeout: float, attempts: int, require_original: bool, require_ws_upgrade: bool = True) -> ProxyNode:
    harden_ws_node(node)
    if require_ws_upgrade and node_network(node) == "ws":
        bug_ok, bug_info = ws_upgrade_delay(node, timeout, attempts)
    else:
        bug_ok, bug_info = tls_bug_delay(node, timeout, attempts)

    # Optimasi penting: kalau original server tidak diwajibkan, jangan dites.
    # Seleksi YAML memang memakai delay ke bug server, jadi cek original hanya menambah waktu proses.
    if require_original:
        orig_ok, orig_info = stability_check(node.original_server, node.port, timeout, attempts)
    else:
        orig_ok = False
        orig_info = {
            "best_delay_ms": None,
            "success_count": 0,
            "reason": "original check skipped",
        }

    node.bug_best_delay_ms = bug_info["best_delay_ms"]
    node.bug_avg_delay_ms = bug_info["avg_delay_ms"]
    node.bug_jitter_ms = bug_info["jitter_ms"]
    node.bug_success_count = bug_info["success_count"]
    node.original_best_delay_ms = orig_info["best_delay_ms"]
    node.original_success_count = orig_info["success_count"]

    # Selection uses bug delay because output server is the bug IP.
    node.best_delay_ms = node.bug_best_delay_ms
    node.avg_delay_ms = node.bug_avg_delay_ms
    node.jitter_ms = node.bug_jitter_ms
    node.success_count = node.bug_success_count
    node.attempts = attempts
    node.score = bug_info["score"] + int((attempts - node.bug_success_count) * 200)

    if not bug_ok:
        node.status = "dead"
        node.reason = "bug server gagal: " + str(bug_info["reason"])[:120]
    elif require_original and not orig_ok:
        node.status = "dead"
        node.reason = "original server gagal: " + str(orig_info["reason"])[:120]
    else:
        node.status = "alive"
        node.reason = "bug server alive" + (" + original alive" if orig_ok else " + original skipped")
    return node


def build_openclash_yaml(nodes: list[ProxyNode], interval: int, tolerance: int, test_url: str, health_timeout: int = DEFAULT_HEALTH_TIMEOUT_MS, rule_mode: str = "Lengkap") -> str:
    names = [node.clash["name"] for node in nodes]
    direct_or_names = names or ["DIRECT"]

    def selector(defaults: list[str] | None = None) -> list[str]:
        defaults = defaults or ["AUTO-FAST", "FALLBACK", "LOAD-BALANCE", "DIRECT"]
        return defaults + names

    domain_provider = {
        "type": "http",
        "interval": 86400,
        "behavior": "domain",
        "format": "mrs",
    }
    ip_provider = {
        "type": "http",
        "interval": 86400,
        "behavior": "ipcidr",
        "format": "mrs",
    }
    classical_provider = {
        "type": "http",
        "interval": 86400,
        "behavior": "classical",
        "format": "yaml",
    }

    rule_providers: dict[str, Any] = {
        # Block iklan, tracking, privacy-leak, dan hijacking/malware ringan.
        "ads_domain": {
            **domain_provider,
            "path": "./rule_providers/ads_domain.mrs",
            "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/category-ads-all.mrs",
        },
        "ads_classical": {
            **classical_provider,
            "path": "./rule_providers/Advertising.yaml",
            "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Advertising/Advertising.yaml",
        },
        "privacy_classical": {
            **classical_provider,
            "path": "./rule_providers/Privacy.yaml",
            "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Privacy/Privacy.yaml",
        },
        "hijacking_classical": {
            **classical_provider,
            "path": "./rule_providers/Hijacking.yaml",
            "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Hijacking/Hijacking.yaml",
        },

        # YouTube dipisah agar bisa diberi jalur berbeda dari Google umum.
        "youtube_domain": {
            **domain_provider,
            "path": "./rule_providers/youtube.mrs",
            "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/youtube.mrs",
        },
        "youtube_ip": {
            **ip_provider,
            "path": "./rule_providers/youtube_ip.mrs",
            "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/google.mrs",
        },

        # Sosial media.
        "telegram_domain": {
            **domain_provider,
            "path": "./rule_providers/telegram.mrs",
            "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/telegram.mrs",
        },
        "twitter_domain": {
            **domain_provider,
            "path": "./rule_providers/twitter.mrs",
            "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/twitter.mrs",
        },
        "tiktok_domain": {
            **domain_provider,
            "path": "./rule_providers/tiktok.mrs",
            "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/tiktok.mrs",
        },
        "facebook_domain": {
            **domain_provider,
            "path": "./rule_providers/facebook.mrs",
            "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/facebook.mrs",
        },
        "telegram_ip": {
            **ip_provider,
            "path": "./rule_providers/telegram_ip.mrs",
            "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/telegram.mrs",
        },
        "twitter_ip": {
            **ip_provider,
            "path": "./rule_providers/twitter_ip.mrs",
            "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/twitter.mrs",
        },

        # Edukasi / research / developer learning.
        "scholar_domain": {
            **domain_provider,
            "path": "./rule_providers/scholar.mrs",
            "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/category-scholar-!cn.mrs",
        },
        "github_domain": {
            **domain_provider,
            "path": "./rule_providers/github.mrs",
            "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/github.mrs",
        },

        # Streaming selain YouTube.
        "netflix_domain": {
            **domain_provider,
            "path": "./rule_providers/netflix.mrs",
            "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/netflix.mrs",
        },
        "spotify_domain": {
            **domain_provider,
            "path": "./rule_providers/spotify.mrs",
            "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/spotify.mrs",
        },
        "biliintl_domain": {
            **domain_provider,
            "path": "./rule_providers/biliintl.mrs",
            "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/biliintl.mrs",
        },
        "netflix_ip": {
            **ip_provider,
            "path": "./rule_providers/netflix_ip.mrs",
            "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/netflix.mrs",
        },
    }

    proxy_groups: list[dict[str, Any]] = [
        {
            "name": "GLOBAL",
            "type": "select",
            # AUTO-FAST tetap di pilihan pertama agar fresh import langsung otomatis cepat.
            "proxies": ["AUTO-FAST", "FALLBACK", "LOAD-BALANCE", "DIRECT", "SOCIAL-MEDIA", "YOUTUBE", "EDUKASI", "STREAMING", "CLEAN"] + names,
        },
        {
            "name": "PROXY",
            "type": "select",
            "proxies": ["GLOBAL", "AUTO-FAST", "SOCIAL-MEDIA", "YOUTUBE", "EDUKASI", "STREAMING", "CLEAN", "FALLBACK", "LOAD-BALANCE", "DIRECT"] + names,
        },
        {
            "name": "SOCIAL-MEDIA",
            "type": "select",
            "proxies": selector(["AUTO-FAST", "FALLBACK", "LOAD-BALANCE", "DIRECT"]),
        },
        {
            "name": "YOUTUBE",
            "type": "select",
            "proxies": selector(["AUTO-FAST", "FALLBACK", "LOAD-BALANCE", "DIRECT"]),
        },
        {
            "name": "EDUKASI",
            "type": "select",
            "proxies": selector(["AUTO-FAST", "DIRECT", "FALLBACK", "LOAD-BALANCE"]),
        },
        {
            "name": "STREAMING",
            "type": "select",
            "proxies": selector(["AUTO-FAST", "FALLBACK", "LOAD-BALANCE", "DIRECT"]),
        },
        {
            "name": "CLEAN",
            "type": "select",
            "proxies": ["AUTO-FAST", "DIRECT", "FALLBACK"],
        },
        {
            "name": "AUTO-FAST",
            "type": "url-test",
            "proxies": direct_or_names,
            "url": test_url,
            "interval": interval,
            "tolerance": tolerance,
            "lazy": False,
            "timeout": health_timeout,
            "expected-status": 204,
        },
        {
            "name": "FALLBACK",
            "type": "fallback",
            "proxies": direct_or_names,
            "url": test_url,
            "interval": interval,
            "lazy": False,
            "timeout": health_timeout,
            "expected-status": 204,
        },
        {
            "name": "LOAD-BALANCE",
            "type": "load-balance",
            "strategy": "consistent-hashing",
            "proxies": direct_or_names,
            "url": test_url,
            "interval": max(interval, 120),
            "lazy": False,
            "timeout": health_timeout,
            "expected-status": 204,
        },
    ]

    rules = [
        # LAN/private harus direct sebelum ruleset lain.
        "DOMAIN-SUFFIX,local,DIRECT",
        "DOMAIN-SUFFIX,lan,DIRECT",
        "DOMAIN-SUFFIX,localhost,DIRECT",
        "IP-CIDR,127.0.0.0/8,DIRECT",
        "IP-CIDR,10.0.0.0/8,DIRECT",
        "IP-CIDR,172.16.0.0/12,DIRECT",
        "IP-CIDR,192.168.0.0/16,DIRECT",
        "IP-CIDR,169.254.0.0/16,DIRECT",
        "GEOIP,LAN,DIRECT,no-resolve",

        # Block iklan, tracker, privacy leak, hijacking/malware sebelum kategori lain.
        "RULE-SET,ads_domain,REJECT",
        "RULE-SET,ads_classical,REJECT",
        "RULE-SET,privacy_classical,REJECT",
        "RULE-SET,hijacking_classical,REJECT",
        "DOMAIN-SUFFIX,doubleclick.net,REJECT",
        "DOMAIN-SUFFIX,googlesyndication.com,REJECT",
        "DOMAIN-SUFFIX,googleadservices.com,REJECT",
        "DOMAIN-SUFFIX,pagead2.googlesyndication.com,REJECT",
        "DOMAIN-KEYWORD,adservice,REJECT",
        "DOMAIN-KEYWORD,analytics,REJECT",
        "DOMAIN-KEYWORD,tracker,REJECT",

        # YouTube khusus, sebelum Google umum/edukasi.
        "RULE-SET,youtube_domain,YOUTUBE",
        "DOMAIN-SUFFIX,youtube.com,YOUTUBE",
        "DOMAIN-SUFFIX,youtu.be,YOUTUBE",
        "DOMAIN-SUFFIX,ytimg.com,YOUTUBE",
        "DOMAIN-SUFFIX,googlevideo.com,YOUTUBE",
        "DOMAIN-SUFFIX,youtubei.googleapis.com,YOUTUBE",

        # Sosial media.
        "RULE-SET,telegram_domain,SOCIAL-MEDIA",
        "RULE-SET,twitter_domain,SOCIAL-MEDIA",
        "RULE-SET,tiktok_domain,SOCIAL-MEDIA",
        "RULE-SET,facebook_domain,SOCIAL-MEDIA",
        "DOMAIN-SUFFIX,facebook.com,SOCIAL-MEDIA",
        "DOMAIN-SUFFIX,fbcdn.net,SOCIAL-MEDIA",
        "DOMAIN-SUFFIX,instagram.com,SOCIAL-MEDIA",
        "DOMAIN-SUFFIX,cdninstagram.com,SOCIAL-MEDIA",
        "DOMAIN-SUFFIX,threads.net,SOCIAL-MEDIA",
        "DOMAIN-SUFFIX,tiktok.com,SOCIAL-MEDIA",
        "DOMAIN-SUFFIX,tiktokcdn.com,SOCIAL-MEDIA",
        "DOMAIN-SUFFIX,twitter.com,SOCIAL-MEDIA",
        "DOMAIN-SUFFIX,x.com,SOCIAL-MEDIA",
        "DOMAIN-SUFFIX,t.me,SOCIAL-MEDIA",
        "DOMAIN-SUFFIX,telegram.org,SOCIAL-MEDIA",
        "GEOIP,telegram,SOCIAL-MEDIA,no-resolve",
        "GEOIP,twitter,SOCIAL-MEDIA,no-resolve",

        # Edukasi, riset, kuliah, dan developer learning.
        "RULE-SET,scholar_domain,EDUKASI",
        "RULE-SET,github_domain,EDUKASI",
        "DOMAIN-SUFFIX,edu,EDUKASI",
        "DOMAIN-SUFFIX,ac.id,EDUKASI",
        "DOMAIN-SUFFIX,scholar.google.com,EDUKASI",
        "DOMAIN-SUFFIX,coursera.org,EDUKASI",
        "DOMAIN-SUFFIX,edx.org,EDUKASI",
        "DOMAIN-SUFFIX,khanacademy.org,EDUKASI",
        "DOMAIN-SUFFIX,udemy.com,EDUKASI",
        "DOMAIN-SUFFIX,academia.edu,EDUKASI",
        "DOMAIN-SUFFIX,arxiv.org,EDUKASI",
        "DOMAIN-SUFFIX,github.com,EDUKASI",
        "DOMAIN-SUFFIX,githubusercontent.com,EDUKASI",

        # Streaming umum selain YouTube.
        "RULE-SET,netflix_domain,STREAMING",
        "RULE-SET,spotify_domain,STREAMING",
        "RULE-SET,biliintl_domain,STREAMING",
        "DOMAIN-SUFFIX,netflix.com,STREAMING",
        "DOMAIN-SUFFIX,nflxvideo.net,STREAMING",
        "DOMAIN-SUFFIX,disneyplus.com,STREAMING",
        "DOMAIN-SUFFIX,hotstar.com,STREAMING",
        "DOMAIN-SUFFIX,primevideo.com,STREAMING",
        "DOMAIN-SUFFIX,amazonvideo.com,STREAMING",
        "DOMAIN-SUFFIX,hulu.com,STREAMING",
        "DOMAIN-SUFFIX,hbomax.com,STREAMING",
        "DOMAIN-SUFFIX,max.com,STREAMING",
        "DOMAIN-SUFFIX,spotify.com,STREAMING",
        "DOMAIN-SUFFIX,twitch.tv,STREAMING",
        "DOMAIN-SUFFIX,viu.com,STREAMING",
        "DOMAIN-SUFFIX,wetv.vip,STREAMING",
        "GEOIP,netflix,STREAMING,no-resolve",

        # Sisanya ikut GLOBAL yang defaultnya langsung AUTO-FAST.
        "MATCH,GLOBAL",
    ]

    if rule_mode == "Lite":
        # Rule Lite lebih ringan untuk router/OpenClash kecil: provider lebih sedikit, import lebih cepat,
        # tetapi kategori utama tetap ada.
        rule_providers = {
            "ads_domain": {
                **domain_provider,
                "path": "./rule_providers/ads_domain.mrs",
                "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/category-ads-all.mrs",
            },
            "youtube_domain": {
                **domain_provider,
                "path": "./rule_providers/youtube.mrs",
                "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/youtube.mrs",
            },
        }
        rules = [
            "DOMAIN-SUFFIX,local,DIRECT",
            "DOMAIN-SUFFIX,lan,DIRECT",
            "DOMAIN-SUFFIX,localhost,DIRECT",
            "IP-CIDR,127.0.0.0/8,DIRECT",
            "IP-CIDR,10.0.0.0/8,DIRECT",
            "IP-CIDR,172.16.0.0/12,DIRECT",
            "IP-CIDR,192.168.0.0/16,DIRECT",
            "IP-CIDR,169.254.0.0/16,DIRECT",
            "GEOIP,LAN,DIRECT,no-resolve",
            "RULE-SET,ads_domain,REJECT",
            "DOMAIN-SUFFIX,doubleclick.net,REJECT",
            "DOMAIN-SUFFIX,googlesyndication.com,REJECT",
            "DOMAIN-SUFFIX,googleadservices.com,REJECT",
            "DOMAIN-KEYWORD,adservice,REJECT",
            "DOMAIN-KEYWORD,analytics,REJECT",
            "DOMAIN-KEYWORD,tracker,REJECT",
            "RULE-SET,youtube_domain,YOUTUBE",
            "DOMAIN-SUFFIX,youtube.com,YOUTUBE",
            "DOMAIN-SUFFIX,youtu.be,YOUTUBE",
            "DOMAIN-SUFFIX,ytimg.com,YOUTUBE",
            "DOMAIN-SUFFIX,googlevideo.com,YOUTUBE",
            "DOMAIN-SUFFIX,facebook.com,SOCIAL-MEDIA",
            "DOMAIN-SUFFIX,fbcdn.net,SOCIAL-MEDIA",
            "DOMAIN-SUFFIX,instagram.com,SOCIAL-MEDIA",
            "DOMAIN-SUFFIX,cdninstagram.com,SOCIAL-MEDIA",
            "DOMAIN-SUFFIX,tiktok.com,SOCIAL-MEDIA",
            "DOMAIN-SUFFIX,tiktokcdn.com,SOCIAL-MEDIA",
            "DOMAIN-SUFFIX,twitter.com,SOCIAL-MEDIA",
            "DOMAIN-SUFFIX,x.com,SOCIAL-MEDIA",
            "DOMAIN-SUFFIX,t.me,SOCIAL-MEDIA",
            "DOMAIN-SUFFIX,telegram.org,SOCIAL-MEDIA",
            "MATCH,GLOBAL",
        ]

    config: dict[str, Any] = {
        "mixed-port": 7890,
        "redir-port": 7892,
        "tproxy-port": 7895,
        "allow-lan": True,
        "bind-address": "*",
        "mode": "rule",
        "log-level": "warning",
        "ipv6": False,
        "unified-delay": True,
        "tcp-concurrent": True,
        "find-process-mode": "strict",
        "global-client-fingerprint": "chrome",
        "external-controller": "0.0.0.0:9090",
        "profile": {
            "store-selected": True,
            "store-fake-ip": True,
        },
        "sniffer": {
            "enable": True,
            "sniff": {
                "TLS": {"ports": [443, 8443]},
                "HTTP": {"ports": [80, "8080-8880"], "override-destination": True},
            },
            "force-domain": ["+.v2ex.com"],
            "skip-domain": ["+.lan", "+.local"],
        },
        "dns": {
            "enable": True,
            "ipv6": False,
            "listen": "0.0.0.0:7874",
            "enhanced-mode": "fake-ip",
            "fake-ip-range": "198.18.0.1/16",
            "fake-ip-filter": ["+.lan", "+.local", "time.*.com", "ntp.*.com"],
            "default-nameserver": ["1.1.1.1", "8.8.8.8"],
            "nameserver": ["https://1.1.1.1/dns-query", "https://dns.google/dns-query"],
            "fallback": ["tls://1.1.1.1", "tls://8.8.8.8"],
            "fallback-filter": {"geoip": True, "geoip-code": "ID", "ipcidr": ["240.0.0.0/4"]},
        },
        "proxies": [node.clash for node in nodes],
        "proxy-groups": proxy_groups,
        "rule-providers": rule_providers,
        "rules": rules,
    }
    return yaml.safe_dump(config, allow_unicode=True, sort_keys=False, width=140)

def build_csv(nodes: list[ProxyNode]) -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow([
        "name",
        "original_name",
        "type",
        "network",
        "original_server",
        "bug_sni",
        "output_server",
        "port",
        "status",
        "tier",
        "bug_best_delay_ms",
        "bug_avg_delay_ms",
        "bug_jitter_ms",
        "bug_success_count",
        "ws_upgrade_ms",
        "ws_success_count",
        "ws_status",
        "original_best_delay_ms",
        "original_success_count",
        "attempts",
        "score",
        "source",
        "reason",
    ])
    for node in nodes:
        writer.writerow([
            node.name,
            node.original_name,
            node.type,
            node_network(node),
            node.original_server,
            node.bug_sni,
            TARGET_SERVER,
            node.port,
            node.status,
            node.tier,
            node.bug_best_delay_ms if node.bug_best_delay_ms is not None else "",
            node.bug_avg_delay_ms if node.bug_avg_delay_ms is not None else "",
            node.bug_jitter_ms if node.bug_jitter_ms is not None else "",
            node.bug_success_count,
            node.ws_upgrade_ms if node.ws_upgrade_ms is not None else "",
            node.ws_success_count,
            node.ws_status,
            node.original_best_delay_ms if node.original_best_delay_ms is not None else "",
            node.original_success_count,
            node.attempts,
            node.score,
            node.source,
            node.reason,
        ])
    return buffer.getvalue()


def process_sources(
    links_text: str,
    manual_text: str,
    fetch_timeout: int,
    tcp_timeout: float,
    max_workers: int,
    max_nodes: int,
    fast_target_ms: int,
    fill_delay_ms: int,
    min_output_nodes: int,
    attempts: int,
    require_successes: int,
    require_original: bool,
    candidate_multiplier: int = 20,
    candidate_min: int = 500,
    max_jitter_ms: int = 0,
    prefer_ws: bool = True,
    require_ws_upgrade: bool = True,
    force_ws_only: bool = DEFAULT_FORCE_WS_ONLY,
    reserve_pool_nodes: int = DEFAULT_RESERVE_POOL_NODES,
) -> tuple[list[ProxyNode], list[ProxyNode], list[tuple[str, str]], list[str]]:
    fast_target_ms = min(int(fast_target_ms), FAST_TARGET_DELAY_MS)
    fill_delay_ms = min(max(int(fill_delay_ms), fast_target_ms), HARD_MAX_DELAY_MS)
    links = [line.strip().strip(",'\"") for line in links_text.splitlines() if line.strip()]
    fetch_logs: list[tuple[str, str]] = []
    raw_uris: list[tuple[str, str]] = []

    if links:
        with concurrent.futures.ThreadPoolExecutor(max_workers=min(max_workers, len(links))) as executor:
            futures = [executor.submit(fetch_url_cached, url, fetch_timeout) for url in links]
            for future in concurrent.futures.as_completed(futures):
                url, text, status = future.result()
                fetch_logs.append((url, status))
                if text:
                    for uri in extract_uris(text):
                        raw_uris.append((uri, url))

    for uri in extract_uris(manual_text or ""):
        raw_uris.append((uri, "manual"))

    parsed: list[ProxyNode] = []
    seen_keys: set[str] = set()
    skipped: list[str] = []
    for uri, source in raw_uris:
        node = parse_uri(uri, source)
        if not node:
            skipped.append(uri[:140])
            continue
        harden_ws_node(node)
        is_complete, complete_reason = validate_complete_node(node)
        if not is_complete:
            node.status = "incomplete"
            node.reason = complete_reason
            node.score = 999999
            parsed.append(node)
            continue
        if node.key in seen_keys:
            continue
        seen_keys.add(node.key)
        parsed.append(node)

    # In 20-alive mode, non-WS nodes are usually the source of false confidence
    # because the practical target is CF bug-server + TLS + WebSocket. Mark them as
    # skipped before testing when WS-only is enabled.
    if force_ws_only:
        for node in parsed:
            if node.status == "pending" and node_network(node) != "ws":
                node.status = "skipped"
                node.reason = "skipped: mode WS only"
                node.score = 999999

    # Test far more candidates than the final YAML output so the app can keep only
    # the best strict-alive nodes. Example: target 20, candidate_min 2000-3000.
    # If WS priority is enabled, WS nodes enter the test queue first.
    target = max(int(max_nodes), int(min_output_nodes), 20)
    candidate_limit = max(target * int(candidate_multiplier), int(candidate_min), int(reserve_pool_nodes) * 20)
    parsed.sort(
        key=lambda n: (
            0 if n.status == "pending" else 1,
            network_priority_rank(n, bool(prefer_ws)),
            protocol_priority_rank(n),
        )
    )
    parsed = parsed[:candidate_limit]

    testable = [node for node in parsed if node.status == "pending"]
    if testable:
        with concurrent.futures.ThreadPoolExecutor(max_workers=min(max_workers, len(testable))) as executor:
            future_map = {
                executor.submit(check_node_bug_compat, node, tcp_timeout, attempts, require_original, require_ws_upgrade): node
                for node in testable
            }
            for future in concurrent.futures.as_completed(future_map):
                node = future_map[future]
                try:
                    future.result()
                except Exception as exc:
                    node.status = "dead"
                    node.reason = "check error: " + str(exc)[:120]

    candidates = [
        node for node in parsed
        if node.status == "alive"
        and node.best_delay_ms is not None
        and node.success_count >= require_successes
        and (int(max_jitter_ms) <= 0 or (node.jitter_ms is not None and node.jitter_ms <= int(max_jitter_ms)))
    ]

    # Tier 1: very fast target, lower than Baidu 124 ms / GitHub 157 ms / NetEase 211 ms.
    fast = [node for node in candidates if (node.best_delay_ms or 999999) <= fast_target_ms]
    for node in fast:
        node.tier = f"FAST ≤{fast_target_ms}ms"

    # Tier 2: still alive and bug-compatible, used only to prevent the YAML from containing
    # too few accounts when the public sources do not have 20 nodes under 123 ms.
    backup = [
        node for node in candidates
        if (node.best_delay_ms or 999999) > fast_target_ms
        and (node.best_delay_ms or 999999) <= fill_delay_ms
    ]
    for node in backup:
        node.tier = f"BACKUP ≤{fill_delay_ms}ms"

    fast.sort(key=lambda n: node_sort_key(n, bool(prefer_ws)))
    backup.sort(key=lambda n: node_sort_key(n, bool(prefer_ws)))

    # Keep an internal reserve pool first, then write only max_nodes to YAML.
    # This makes the output less fragile because the final 20 are selected from a
    # larger strict-alive pool, not directly from the first 20 that happened to pass.
    strict_pool_limit = max(int(reserve_pool_nodes), int(max_nodes), int(min_output_nodes))
    strict_pool = select_diverse_nodes(fast + backup, strict_pool_limit, bool(prefer_ws))

    # If the fast/backup delay thresholds still do not produce enough nodes, fill
    # from all strict candidates regardless of fill_delay. These nodes already
    # passed WS Upgrade 101 / TLS validation; they are just slower.
    if len(strict_pool) < int(min_output_nodes):
        existing = {id(n) for n in strict_pool}
        slow_fill = [n for n in sorted(candidates, key=lambda n: node_sort_key(n, bool(prefer_ws))) if id(n) not in existing]
        for node in slow_fill:
            node.tier = node.tier or "STRICT-SLOW"
        strict_pool = select_diverse_nodes(strict_pool + slow_fill, strict_pool_limit, bool(prefer_ws))

    selected = select_diverse_nodes(strict_pool, int(max_nodes), bool(prefer_ws))
    selected.sort(key=lambda n: node_sort_key(n, bool(prefer_ws)))
    selected = selected[:max_nodes]
    unique_names(selected)
    return selected, parsed, fetch_logs, skipped

