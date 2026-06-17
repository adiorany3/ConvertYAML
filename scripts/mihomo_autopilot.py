#!/usr/bin/env python3
"""
Mihomo/OpenClash AutoPilot Self-Healing
======================================

Tujuan:
- Mengecek group utama secara otomatis.
- Memilih jalur paling sehat untuk selector GLOBAL/PROXY/STREAMING.
- Memberi cooldown sementara untuk group yang gagal berulang.
- Opsional menutup koneksi lama saat berpindah jalur agar koneksi yang macet cepat pulih.

Default aman untuk config ini:
- Controller: http://127.0.0.1:9090
- Secret default untuk paket ini: reyre. Bisa dioverride dengan env MIHOMO_SECRET.

Contoh OpenWrt/OpenClash:
  python3 /etc/mihomo-autopilot/mihomo_autopilot.py --once
  python3 /etc/mihomo-autopilot/mihomo_autopilot.py --loop --interval 120

Environment:
  MIHOMO_API=http://127.0.0.1:9090
  MIHOMO_SECRET=reyre  # sesuaikan kalau secret OpenClash diganti
  AUTOPILOT_STATE=/tmp/mihomo_autopilot_state.json
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

def _clean_secret(value: str) -> str:
    value = (value or "").strip()
    if not value:
        return ""
    # Hilangkan quote YAML dan komentar di belakangnya.
    value = value.split("#", 1)[0].strip()
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        value = value[1:-1].strip()
    return value


def _detect_mihomo_secret() -> str:
    """Deteksi secret OpenClash/Mihomo tanpa dependency PyYAML.

    Ini membantu di OpenWrt karena paket python3-yaml sering tidak tersedia.
    Env MIHOMO_SECRET tetap prioritas tertinggi.
    """
    explicit = _clean_secret(os.environ.get("MIHOMO_SECRET", ""))
    if explicit:
        return explicit

    candidates: list[str] = []
    env_config = os.environ.get("OPENCLASH_CONFIG") or os.environ.get("MIHOMO_CONFIG")
    if env_config:
        candidates.append(env_config)
    patterns = [
        "/etc/openclash/config/config.yaml",
        "/etc/openclash/config/*.yaml",
        "/etc/openclash/*.yaml",
        "/etc/mihomo/config.yaml",
        "/etc/clash/config.yaml",
    ]
    for pattern in patterns:
        candidates.extend(glob.glob(pattern))

    seen: set[str] = set()
    for path in candidates:
        if not path or path in seen:
            continue
        seen.add(path)
        try:
            raw = Path(path).read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        match = re.search(r"(?m)^\s*secret\s*:\s*(.+?)\s*$", raw)
        if match:
            secret = _clean_secret(match.group(1))
            if secret:
                return secret
    return ""


DEFAULT_API = os.environ.get("MIHOMO_API", "http://127.0.0.1:9090").rstrip("/")
DEFAULT_SECRET = _detect_mihomo_secret() or "reyre"
DEFAULT_STATE = os.environ.get("AUTOPILOT_STATE", "/tmp/mihomo_autopilot_state.json")

TEST_URL_GSTATIC = "https://www.gstatic.com/generate_204"
TEST_URL_CF = "https://cp.cloudflare.com"

# Policy urutan selector. Selector hanya akan dipindahkan ke nama yang memang ada di group tersebut.
POLICIES: Dict[str, List[Tuple[str, str]]] = {
    "GLOBAL": [
        ("WARM-UP", TEST_URL_GSTATIC),
        ("WARM-UP-CF", TEST_URL_CF),
        ("AUTO-FAST", TEST_URL_GSTATIC),
        ("FALLBACK", TEST_URL_GSTATIC),
    ],
    "PROXY": [
        ("WARM-UP", TEST_URL_GSTATIC),
        ("WARM-UP-CF", TEST_URL_CF),
        ("AUTO-FAST", TEST_URL_GSTATIC),
        ("FALLBACK", TEST_URL_GSTATIC),
    ],
    "STREAMING": [
        ("WARM-UP-CF", TEST_URL_CF),
        ("STREAMING-FAST", TEST_URL_CF),
        ("WARM-UP", TEST_URL_GSTATIC),
        ("AUTO-FAST", TEST_URL_GSTATIC),
        ("FALLBACK", TEST_URL_GSTATIC),
    ],
}

# Cadangan selector tambahan. Script akan skip otomatis kalau selector tidak ada.
OPTIONAL_SELECTORS = ["SOCIAL-MEDIA", "YOUTUBE", "EDUKASI"]
for selector in OPTIONAL_SELECTORS:
    POLICIES[selector] = [
        ("WARM-UP", TEST_URL_GSTATIC),
        ("WARM-UP-CF", TEST_URL_CF),
        ("AUTO-FAST", TEST_URL_GSTATIC),
        ("FALLBACK", TEST_URL_GSTATIC),
    ]


@dataclass
class DelayResult:
    name: str
    ok: bool
    delay_ms: Optional[int]
    error: str = ""


class MihomoClient:
    def __init__(self, base_url: str, secret: str = "", timeout: float = 5.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.secret = secret
        self.timeout = timeout

    def _headers(self) -> Dict[str, str]:
        headers = {"Content-Type": "application/json"}
        if self.secret:
            headers["Authorization"] = f"Bearer {self.secret}"
        return headers

    def request(self, method: str, path: str, body: Optional[Dict[str, Any]] = None) -> Any:
        url = f"{self.base_url}{path}"
        data = None
        if body is not None:
            data = json.dumps(body).encode("utf-8")
        req = Request(url, data=data, headers=self._headers(), method=method)
        with urlopen(req, timeout=self.timeout) as resp:
            raw = resp.read()
            if not raw:
                return None
            ctype = resp.headers.get("Content-Type", "")
            if "json" in ctype or raw[:1] in (b"{", b"["):
                return json.loads(raw.decode("utf-8"))
            return raw.decode("utf-8", errors="replace")

    def proxies(self) -> Dict[str, Any]:
        data = self.request("GET", "/proxies")
        return data.get("proxies", {}) if isinstance(data, dict) else {}

    def delay(self, name: str, url: str, timeout_ms: int) -> DelayResult:
        if name == "DIRECT":
            return DelayResult(name=name, ok=True, delay_ms=0)
        q = urlencode({"timeout": str(timeout_ms), "url": url})
        path = f"/proxies/{quote(name, safe='')}/delay?{q}"
        try:
            data = self.request("GET", path)
            delay = None
            if isinstance(data, dict):
                value = data.get("delay")
                if isinstance(value, (int, float)):
                    delay = int(value)
            if delay is not None and delay >= 0:
                return DelayResult(name=name, ok=True, delay_ms=delay)
            return DelayResult(name=name, ok=False, delay_ms=None, error=f"delay kosong: {data}")
        except Exception as exc:  # noqa: BLE001 - sengaja toleran untuk router runtime
            return DelayResult(name=name, ok=False, delay_ms=None, error=str(exc))

    def select(self, selector: str, target: str) -> bool:
        path = f"/proxies/{quote(selector, safe='')}"
        try:
            self.request("PUT", path, {"name": target})
            return True
        except Exception as exc:  # noqa: BLE001
            print(f"[WARN] gagal memilih {selector} -> {target}: {exc}")
            return False

    def close_connections(self) -> bool:
        try:
            self.request("DELETE", "/connections")
            return True
        except Exception as exc:  # noqa: BLE001
            print(f"[WARN] gagal menutup koneksi lama: {exc}")
            return False

    def flush_fakeip(self) -> bool:
        # Endpoint bisa berbeda antar versi core. Coba beberapa kemungkinan, abaikan kalau tidak didukung.
        for path in ["/cache/fakeip/flush", "/cache/fakeip"]:
            try:
                self.request("DELETE", path)
                return True
            except Exception:
                continue
        return False


class State:
    def __init__(self, path: str) -> None:
        self.path = Path(path)
        self.data: Dict[str, Any] = {"failures": {}, "cooldown_until": {}, "last_selected": {}}
        self.load()

    def load(self) -> None:
        try:
            if self.path.exists():
                loaded = json.loads(self.path.read_text(encoding="utf-8"))
                if isinstance(loaded, dict):
                    self.data.update(loaded)
        except Exception:
            pass

    def save(self) -> None:
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            tmp = self.path.with_suffix(".tmp")
            tmp.write_text(json.dumps(self.data, indent=2, sort_keys=True), encoding="utf-8")
            tmp.replace(self.path)
        except Exception as exc:  # noqa: BLE001
            print(f"[WARN] gagal simpan state: {exc}")

    def failure_count(self, name: str) -> int:
        return int(self.data.get("failures", {}).get(name, 0) or 0)

    def mark_ok(self, name: str) -> None:
        self.data.setdefault("failures", {})[name] = 0
        self.data.setdefault("cooldown_until", {}).pop(name, None)

    def mark_fail(self, name: str, cooldown_seconds: int, failures_before_cooldown: int) -> None:
        failures = self.failure_count(name) + 1
        self.data.setdefault("failures", {})[name] = failures
        if failures >= failures_before_cooldown:
            self.data.setdefault("cooldown_until", {})[name] = time.time() + cooldown_seconds
            self.data.setdefault("failures", {})[name] = 0

    def in_cooldown(self, name: str) -> bool:
        until = float(self.data.get("cooldown_until", {}).get(name, 0) or 0)
        if until <= time.time():
            self.data.setdefault("cooldown_until", {}).pop(name, None)
            return False
        return True

    def cooldown_remaining(self, name: str) -> int:
        until = float(self.data.get("cooldown_until", {}).get(name, 0) or 0)
        return max(0, int(until - time.time()))

    def last_selected(self, selector: str) -> Optional[str]:
        value = self.data.get("last_selected", {}).get(selector)
        return str(value) if value else None

    def set_last_selected(self, selector: str, target: str) -> None:
        self.data.setdefault("last_selected", {})[selector] = target


def available_targets(selector_info: Dict[str, Any]) -> List[str]:
    values = selector_info.get("all") or []
    return [str(x) for x in values]


def current_target(selector_info: Dict[str, Any]) -> Optional[str]:
    now = selector_info.get("now")
    return str(now) if now else None


def choose_target(
    client: MihomoClient,
    state: State,
    selector: str,
    selector_info: Dict[str, Any],
    policy: List[Tuple[str, str]],
    timeout_ms: int,
    max_delay_ms: int,
    cooldown_seconds: int,
    failures_before_cooldown: int,
    avoid_direct: bool = False,
) -> Tuple[Optional[str], List[DelayResult]]:
    allowed = set(available_targets(selector_info))
    candidates = [(name, url) for name, url in policy if name in allowed]
    if avoid_direct:
        candidates = [(name, url) for name, url in candidates if name != "DIRECT"]
    results: List[DelayResult] = []

    if avoid_direct and current_target(selector_info) == "DIRECT":
        results.append(DelayResult(name="DIRECT", ok=False, delay_ms=None, error="blocked by --avoid-direct"))

    for name, url in candidates:
        if state.in_cooldown(name):
            results.append(DelayResult(name=name, ok=False, delay_ms=None, error=f"cooldown {state.cooldown_remaining(name)}s"))
            continue
        result = client.delay(name, url, timeout_ms)
        results.append(result)
        if result.ok and result.delay_ms is not None and result.delay_ms <= max_delay_ms:
            state.mark_ok(name)
            return name, results
        state.mark_fail(name, cooldown_seconds, failures_before_cooldown)

    # Kalau semua gagal, pilih kandidat pertama yang tersedia dan tidak cooldown. Ini mencegah selector kosong.
    for name, _url in candidates:
        if not state.in_cooldown(name):
            return name, results

    # Kalau semua cooldown, pilih fallback paling akhir yang tersedia.
    return candidates[-1][0] if candidates else None, results


def run_once(args: argparse.Namespace) -> int:
    client = MihomoClient(args.api, args.secret, timeout=args.http_timeout)
    state = State(args.state)

    try:
        proxies = client.proxies()
    except HTTPError as exc:
        if exc.code == 401:
            print(f"[ERROR] Mihomo API 401 Unauthorized di {args.api}.")
            print("[FIX] Secret API salah/kosong. Untuk paket ini gunakan: MIHOMO_SECRET='reyre'")
            print("[FIX] Pastikan YAML OpenClash berisi: secret: \"reyre\" lalu restart OpenClash.")
        else:
            print(f"[ERROR] tidak bisa akses Mihomo API {args.api}: HTTP {exc.code} {exc.reason}")
        return 2
    except (URLError, TimeoutError, OSError) as exc:
        print(f"[ERROR] tidak bisa akses Mihomo API {args.api}: {exc}")
        print("[FIX] Pastikan OpenClash aktif dan external-controller memakai 127.0.0.1:9090 atau 0.0.0.0:9090.")
        return 2

    changed = False
    checked_any = False

    for selector, policy in POLICIES.items():
        selector_info = proxies.get(selector)
        if not isinstance(selector_info, dict):
            continue
        if selector_info.get("type") != "Selector":
            # Beberapa core menulis type select/Selector berbeda. Tetap coba selama ada field all.
            if not selector_info.get("all"):
                continue

        checked_any = True
        selected, results = choose_target(
            client=client,
            state=state,
            selector=selector,
            selector_info=selector_info,
            policy=policy,
            timeout_ms=args.delay_timeout_ms,
            max_delay_ms=args.max_delay_ms,
            cooldown_seconds=args.cooldown_seconds,
            failures_before_cooldown=args.failures_before_cooldown,
            avoid_direct=args.avoid_direct,
        )

        current = current_target(selector_info)
        result_text = ", ".join(
            f"{r.name}:{r.delay_ms}ms" if r.ok else f"{r.name}:FAIL({r.error})" for r in results
        )
        print(f"[{selector}] current={current} selected={selected} checks=[{result_text}]")

        if selected and selected != current:
            if client.select(selector, selected):
                changed = True
                state.set_last_selected(selector, selected)
                print(f"[OK] {selector} -> {selected}")

    if not checked_any:
        print("[WARN] selector utama tidak ditemukan. Pastikan config memakai group GLOBAL/PROXY/STREAMING.")

    if changed and args.close_connections:
        client.close_connections()
    if changed and args.flush_fakeip:
        if client.flush_fakeip():
            print("[OK] fake-ip cache flush")
        else:
            print("[INFO] fake-ip flush tidak didukung core ini, diabaikan")

    state.save()
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Mihomo/OpenClash AutoPilot Self-Healing")
    parser.add_argument("--api", default=DEFAULT_API, help="Mihomo external-controller URL")
    parser.add_argument("--secret", default=DEFAULT_SECRET, help="Mihomo API secret. Default paket ini: reyre; bisa dioverride env MIHOMO_SECRET")
    parser.add_argument("--state", default=DEFAULT_STATE, help="Path state cooldown AutoPilot")
    parser.add_argument("--once", action="store_true", help="Jalankan sekali lalu keluar")
    parser.add_argument("--loop", action="store_true", help="Jalankan terus-menerus")
    parser.add_argument("--interval", type=int, default=120, help="Interval loop dalam detik")
    parser.add_argument("--delay-timeout-ms", type=int, default=3000, help="Timeout delay test Mihomo")
    parser.add_argument("--max-delay-ms", type=int, default=1500, help="Delay maksimum yang dianggap sehat")
    parser.add_argument("--cooldown-seconds", type=int, default=900, help="Cooldown group gagal berulang")
    parser.add_argument("--failures-before-cooldown", type=int, default=2, help="Jumlah gagal sebelum cooldown")
    parser.add_argument("--http-timeout", type=float, default=6.0, help="Timeout request API")
    parser.add_argument("--close-connections", action="store_true", help="Tutup koneksi lama saat selector berpindah")
    parser.add_argument("--flush-fakeip", action="store_true", help="Coba flush fake-ip saat selector berpindah")
    parser.add_argument("--avoid-direct", action="store_true", help="Jangan pilih DIRECT sebagai target selector. Pada paket no-selector, DIRECT memang tidak dipakai di proxy-group.")
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.once and not args.loop:
        args.once = True

    if args.once:
        return run_once(args)

    while True:
        started = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n=== AutoPilot tick {started} ===")
        run_once(args)
        time.sleep(max(15, args.interval))


if __name__ == "__main__":
    raise SystemExit(main())
