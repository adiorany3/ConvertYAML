from __future__ import annotations

import base64
import concurrent.futures
import csv
import html
import io
import json
import re
import socket
import statistics
import time
from dataclasses import dataclass, field
from typing import Any
from urllib.parse import parse_qs, unquote, urlparse

import requests
import streamlit as st
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
]

TARGET_SERVER = "104.17.3.81"
ONLY_PORT = 443
USER_AGENT = "Mozilla/5.0 SumberYAML-OpenClash-AntiDelay/2.0"
URI_RE = re.compile(r"(?:vless|vmess|trojan|ss)://[^\s<'\"`]+", re.IGNORECASE)
FAST_TEST_URL = "http://www.gstatic.com/generate_204"
ALT_TEST_URL = "https://www.google.com/generate_204"


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
    text = unquote(name or "").strip()
    text = re.sub(r"[\r\n\t]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = text[:70].strip(" -_|/")
    return text or fallback


def unique_names(nodes: list[ProxyNode]) -> None:
    seen: dict[str, int] = {}
    for i, node in enumerate(nodes, start=1):
        delay_part = f" {node.best_delay_ms}ms" if node.best_delay_ms is not None else ""
        base = normalize_name(node.name, f"FAST-{i:03d}")
        # Add a small readable prefix so OpenClash list is easy to scan.
        base = f"{i:02d}-{base}{delay_part}"
        count = seen.get(base, 0)
        seen[base] = count + 1
        name = base if count == 0 else f"{base}-{count + 1}"
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


def build_openclash_yaml(nodes: list[ProxyNode], interval: int, tolerance: int, test_url: str) -> str:
    names = [node.clash["name"] for node in nodes]
    direct_or_names = names or ["DIRECT"]
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
        "proxy-groups": [
            {
                "name": "🚀 PROXY",
                "type": "select",
                "proxies": ["⚡ AUTO-FAST", "🛟 FALLBACK", "🔁 LOAD-BALANCE", "DIRECT"] + names,
            },
            {
                "name": "⚡ AUTO-FAST",
                "type": "url-test",
                "proxies": direct_or_names,
                "url": test_url,
                "interval": interval,
                "tolerance": tolerance,
                "lazy": False,
                "timeout": 3000,
            },
            {
                "name": "🛟 FALLBACK",
                "type": "fallback",
                "proxies": direct_or_names,
                "url": test_url,
                "interval": interval,
                "lazy": False,
                "timeout": 3000,
            },
            {
                "name": "🔁 LOAD-BALANCE",
                "type": "load-balance",
                "strategy": "consistent-hashing",
                "proxies": direct_or_names,
                "url": test_url,
                "interval": max(interval, 120),
                "lazy": False,
                "timeout": 3000,
            },
        ],
        "rules": [
            "DOMAIN-SUFFIX,local,DIRECT",
            "DOMAIN-SUFFIX,lan,DIRECT",
            "IP-CIDR,127.0.0.0/8,DIRECT",
            "IP-CIDR,10.0.0.0/8,DIRECT",
            "IP-CIDR,172.16.0.0/12,DIRECT",
            "IP-CIDR,192.168.0.0/16,DIRECT",
            "GEOIP,LAN,DIRECT,no-resolve",
            "MATCH,🚀 PROXY",
        ],
    }
    return yaml.safe_dump(config, allow_unicode=True, sort_keys=False, width=140)


def build_csv(nodes: list[ProxyNode]) -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow([
        "name",
        "type",
        "original_server",
        "output_server",
        "port",
        "status",
        "best_delay_ms",
        "avg_delay_ms",
        "jitter_ms",
        "success_count",
        "attempts",
        "score",
        "source",
        "reason",
    ])
    for node in nodes:
        writer.writerow([
            node.name,
            node.type,
            node.original_server,
            TARGET_SERVER,
            node.port,
            node.status,
            node.best_delay_ms if node.best_delay_ms is not None else "",
            node.avg_delay_ms if node.avg_delay_ms is not None else "",
            node.jitter_ms if node.jitter_ms is not None else "",
            node.success_count,
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
    max_delay_ms: int,
    attempts: int,
    require_successes: int,
) -> tuple[list[ProxyNode], list[ProxyNode], list[tuple[str, str]], list[str]]:
    links = [line.strip().strip(",'\"") for line in links_text.splitlines() if line.strip()]
    fetch_logs: list[tuple[str, str]] = []
    raw_uris: list[tuple[str, str]] = []

    if links:
        with concurrent.futures.ThreadPoolExecutor(max_workers=min(max_workers, len(links))) as executor:
            futures = [executor.submit(fetch_url, url, fetch_timeout) for url in links]
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
        if node.key in seen_keys:
            continue
        seen_keys.add(node.key)
        parsed.append(node)

    # Do not test millions of entries on free Streamlit; keep enough candidates for a useful fast set.
    candidate_limit = max_nodes * 12 if max_nodes > 0 else 600
    parsed = parsed[: max(candidate_limit, 100)]

    if parsed:
        with concurrent.futures.ThreadPoolExecutor(max_workers=min(max_workers, len(parsed))) as executor:
            future_map = {
                executor.submit(stability_check, node.original_server, node.port, tcp_timeout, attempts): node
                for node in parsed
            }
            for future in concurrent.futures.as_completed(future_map):
                node = future_map[future]
                ok, info = future.result()
                node.status = "alive" if ok else "dead"
                node.best_delay_ms = info["best_delay_ms"]
                node.avg_delay_ms = info["avg_delay_ms"]
                node.jitter_ms = info["jitter_ms"]
                node.success_count = info["success_count"]
                node.attempts = info["attempts"]
                node.score = info["score"]
                node.reason = info["reason"]

    alive = [
        node
        for node in parsed
        if node.status == "alive"
        and node.best_delay_ms is not None
        and node.best_delay_ms <= max_delay_ms
        and node.success_count >= require_successes
    ]
    alive.sort(key=lambda n: (n.score, n.best_delay_ms or 999999, n.jitter_ms or 999999))
    if max_nodes > 0:
        alive = alive[:max_nodes]
    unique_names(alive)
    return alive, parsed, fetch_logs, skipped


st.set_page_config(page_title="OpenClash Anti Delay", page_icon="⚡", layout="wide")
st.title("⚡ SumberYAML OpenClash Anti Delay")
st.caption(
    "Ambil subscription publik, pakai hanya port 443, cek link hidup, tes node berulang, pilih node tercepat/stabil, "
    "ubah server ke 104.17.3.81, lalu buat YAML OpenClash/Mihomo."
)

with st.expander("Pengaturan cepat anti delay", expanded=True):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.text_input("Server output", value=TARGET_SERVER, disabled=True)
    with col2:
        st.text_input("Port wajib", value=str(ONLY_PORT), disabled=True)
    with col3:
        max_nodes = st.number_input("Maksimal node tercepat", min_value=1, max_value=300, value=30, step=5)
    with col4:
        max_delay_ms = st.number_input("Maks delay masuk YAML/ms", min_value=50, max_value=3000, value=900, step=50)

    col5, col6, col7, col8 = st.columns(4)
    with col5:
        attempts = st.number_input("Tes ulang per node", min_value=1, max_value=5, value=3, step=1)
    with col6:
        require_successes = st.number_input("Minimal sukses", min_value=1, max_value=5, value=2, step=1)
    with col7:
        tcp_timeout = st.number_input("Timeout node/detik", min_value=0.5, max_value=10.0, value=2.5, step=0.5)
    with col8:
        max_workers = st.number_input("Concurrency", min_value=1, max_value=100, value=36, step=1)

    col9, col10, col11 = st.columns(3)
    with col9:
        fetch_timeout = st.number_input("Timeout fetch link/detik", min_value=5, max_value=60, value=20, step=5)
    with col10:
        urltest_interval = st.number_input("Interval url-test OpenClash/detik", min_value=30, max_value=900, value=60, step=30)
    with col11:
        tolerance = st.number_input("Toleransi auto-switch/ms", min_value=5, max_value=300, value=25, step=5)

    test_url = st.selectbox(
        "URL health check OpenClash",
        [FAST_TEST_URL, ALT_TEST_URL, "http://cp.cloudflare.com/generate_204"],
        index=0,
    )

links_text = st.text_area(
    "Link subscription bawaan",
    value="\n".join(DEFAULT_LINKS),
    height=230,
    help="Satu URL per baris. Link mati otomatis diabaikan saat proses berjalan.",
)

manual_text = st.text_area(
    "Tambahan node manual, opsional",
    value="",
    height=100,
    placeholder="Tempel vless://, vmess://, trojan://, atau ss:// di sini jika ada tambahan.",
)

run = st.button("Proses & buat YAML anti delay", type="primary")

if run:
    require_successes = min(int(require_successes), int(attempts))
    with st.spinner("Mengecek link, menyaring port 443, menguji delay/stabilitas, dan memilih node tercepat..."):
        alive_nodes, all_nodes, fetch_logs, skipped = process_sources(
            links_text=links_text,
            manual_text=manual_text,
            fetch_timeout=int(fetch_timeout),
            tcp_timeout=float(tcp_timeout),
            max_workers=int(max_workers),
            max_nodes=int(max_nodes),
            max_delay_ms=int(max_delay_ms),
            attempts=int(attempts),
            require_successes=int(require_successes),
        )

    total_parsed = len(all_nodes)
    total_alive_any = len([n for n in all_nodes if n.status == "alive"])
    total_fast = len(alive_nodes)
    total_dead = len([n for n in all_nodes if n.status == "dead"])
    live_links = len([1 for _, status in fetch_logs if status.startswith("alive")])
    dead_links = len([1 for _, status in fetch_logs if status.startswith("dead")])

    m1, m2, m3, m4, m5 = st.columns(5)
    m1.metric("Link hidup", live_links)
    m2.metric("Parsed port 443", total_parsed)
    m3.metric("Node hidup", total_alive_any)
    m4.metric("Lolos anti delay", total_fast)
    m5.metric("Dead dibuang", total_dead)

    if fetch_logs:
        with st.expander("Status link subscription", expanded=False):
            st.dataframe(
                [{"url": url, "status": status, "dipakai": "ya" if status.startswith("alive") else "tidak"} for url, status in fetch_logs],
                use_container_width=True,
                hide_index=True,
            )

    if not alive_nodes:
        st.error(
            "Belum ada node yang lolos filter anti delay. Coba naikkan 'Maks delay masuk YAML', turunkan 'Minimal sukses', atau jalankan ulang karena sumber publik sering berubah."
        )
        if all_nodes:
            with st.expander("Detail node yang gagal/lambat"):
                st.dataframe(
                    [
                        {
                            "name": n.name,
                            "type": n.type,
                            "original_server": n.original_server,
                            "status": n.status,
                            "best_delay_ms": n.best_delay_ms,
                            "avg_delay_ms": n.avg_delay_ms,
                            "jitter_ms": n.jitter_ms,
                            "success": f"{n.success_count}/{n.attempts}",
                            "score": n.score,
                            "reason": n.reason,
                            "source": n.source,
                        }
                        for n in sorted(all_nodes, key=lambda x: x.score)[:300]
                    ],
                    use_container_width=True,
                    hide_index=True,
                )
    else:
        yaml_text = build_openclash_yaml(alive_nodes, int(urltest_interval), int(tolerance), test_url)
        csv_text = build_csv(all_nodes)

        st.success(
            f"Berhasil membuat YAML anti delay dari {len(alive_nodes)} node tercepat/stabil. "
            "Grup ⚡ AUTO-FAST akan otomatis memilih node respons terbaik di OpenClash."
        )
        c1, c2 = st.columns(2)
        with c1:
            st.download_button(
                "Download openclash_anti_delay.yaml",
                data=yaml_text.encode("utf-8"),
                file_name="openclash_anti_delay.yaml",
                mime="application/x-yaml",
            )
        with c2:
            st.download_button(
                "Download report CSV",
                data=csv_text.encode("utf-8"),
                file_name="openclash_anti_delay_report.csv",
                mime="text/csv",
            )

        st.subheader("Node tercepat yang masuk YAML")
        st.dataframe(
            [
                {
                    "rank": i,
                    "name": n.name,
                    "type": n.type,
                    "original_server": n.original_server,
                    "server_output": TARGET_SERVER,
                    "best_delay_ms": n.best_delay_ms,
                    "avg_delay_ms": n.avg_delay_ms,
                    "jitter_ms": n.jitter_ms,
                    "success": f"{n.success_count}/{n.attempts}",
                    "score": n.score,
                    "source": n.source,
                }
                for i, n in enumerate(alive_nodes, start=1)
            ],
            use_container_width=True,
            hide_index=True,
        )

        with st.expander("Preview YAML"):
            st.code(yaml_text, language="yaml")

st.info(
    "Catatan penting: aplikasi ini memilih node yang respons TCP-nya cepat dan stabil, lalu OpenClash melakukan url-test/fallback otomatis. "
    "Karena akun berasal dari subscription publik, tidak ada cara menjamin 100% anti delay setiap waktu. Jalankan ulang proses dan Health Check OpenClash jika kualitas berubah."
)
