from __future__ import annotations

import os
import sys
from datetime import datetime, timezone
from pathlib import Path

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


def build_akun_txt(nodes) -> str:
    """Simpan link asli akun aktif yang masuk YAML.

    Hanya protocol vless/vmess/trojan yang ditulis karena format ini mudah
    diimport ke client lain. Shadowsocks tidak ditulis ke akun.txt sesuai
    kebutuhan utama file ini.
    """
    lines: list[str] = []
    seen: set[str] = set()
    for node in nodes:
        raw = str(getattr(node, "raw", "") or "").strip()
        proto = raw.split("://", 1)[0].lower() if "://" in raw else ""
        if proto not in {"vless", "vmess", "trojan"}:
            continue
        if raw and raw not in seen:
            seen.add(raw)
            lines.append(raw)
    return "\n".join(lines) + ("\n" if lines else "")


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
        f"Akun txt: {len([line for line in akun_text.splitlines() if line.strip()])}\n"
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
