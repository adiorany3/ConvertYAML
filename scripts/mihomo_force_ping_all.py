#!/usr/bin/env python3
"""Force Mihomo/OpenClash delay checks for all proxy nodes.

Useful after OpenClash reload/import when accounts are grey/no-ping in the UI.
It calls Mihomo API /proxies/<name>/delay so OpenClash has fresh delay data.
"""
from __future__ import annotations

import json
import os
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

API = os.getenv("MIHOMO_API", "http://127.0.0.1:9090").rstrip("/")
SECRET = os.getenv("MIHOMO_SECRET", "reyre").strip().strip('"\'')
URL = os.getenv("PING_CHECK_URL", os.getenv("TEST_URL", "https://www.gstatic.com/generate_204"))
TIMEOUT_MS = int(os.getenv("PING_CHECK_TIMEOUT_MS", "5000"))
LIMIT = int(os.getenv("PING_CHECK_LIMIT", "0"))  # 0 = all
SLEEP = float(os.getenv("PING_CHECK_SLEEP", "0.10"))


def req(path: str, timeout: int = 8):
    headers = {}
    if SECRET:
        headers["Authorization"] = f"Bearer {SECRET}"
    r = Request(API + path, headers=headers)
    with urlopen(r, timeout=timeout) as resp:
        raw = resp.read().decode("utf-8", "replace")
        return json.loads(raw) if raw else {}


def main() -> int:
    try:
        data = req("/proxies")
    except HTTPError as e:
        print(f"[ERROR] tidak bisa akses Mihomo API {API}: HTTP {e.code} {e.reason}")
        return 2
    except Exception as e:
        print(f"[ERROR] tidak bisa akses Mihomo API {API}: {e}")
        return 2

    proxies = data.get("proxies", {}) if isinstance(data, dict) else {}
    names = []
    for name, item in proxies.items():
        if name in ("DIRECT", "REJECT", "GLOBAL"):
            continue
        if not isinstance(item, dict):
            continue
        # Only test real proxy nodes. Skip groups; PING-CHECK will cover grouped probe separately.
        if "history" in item and item.get("type") not in ("Selector", "URLTest", "Fallback", "LoadBalance"):
            names.append(name)
    # Fallback: if type naming differs, test entries that are not known group names.
    if not names:
        group_like = {"GLOBAL", "PROXY", "SOCIAL-MEDIA", "YOUTUBE", "EDUKASI", "STREAMING", "PING-CHECK", "WARM-UP", "WARM-UP-CF", "STREAMING-FAST", "CLEAN", "AUTO-FAST", "FALLBACK", "LOAD-BALANCE", "MANUAL", "DIRECT", "REJECT"}
        names = [n for n in proxies.keys() if n not in group_like]

    if LIMIT > 0:
        names = names[:LIMIT]

    ok = 0
    fail = 0
    print(f"[PING-CHECK] testing {len(names)} node(s), url={URL}, timeout={TIMEOUT_MS}ms")
    qs = urlencode({"timeout": str(TIMEOUT_MS), "url": URL})
    for name in names:
        path = f"/proxies/{quote(name, safe='')}/delay?{qs}"
        try:
            out = req(path, timeout=max(6, int(TIMEOUT_MS / 1000) + 3))
            delay = out.get("delay") if isinstance(out, dict) else None
            print(f"[OK] {name}: {delay}ms")
            ok += 1
        except Exception as e:
            print(f"[FAIL] {name}: {e}")
            fail += 1
        time.sleep(SLEEP)
    print(f"[DONE] ok={ok} fail={fail}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
