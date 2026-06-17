#!/usr/bin/env python3
"""Collect Mihomo/OpenClash runtime status and optionally upload it to GitHub.

Designed for OpenWrt + Python3 only, no third-party dependency.
"""
from __future__ import annotations

import argparse
import base64
import datetime as dt
import json
import os
import re
import socket
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, Optional

DEFAULT_GROUPS = [
    "GLOBAL",
    "PROXY",
    "WARM-UP",
    "WARM-UP-CF",
    "AUTO-FAST",
    "STREAMING",
    "STREAMING-FAST",
    "SOCIAL-MEDIA",
    "YOUTUBE",
    "EDUKASI",
    "FALLBACK",
]


def load_env(path: str) -> None:
    p = Path(path)
    if not p.exists():
        return
    for raw in p.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k = k.strip()
        v = v.strip().strip('"').strip("'")
        if k and k not in os.environ:
            os.environ[k] = v


def http_json(url: str, secret: str = "", method: str = "GET", data: Optional[dict] = None, timeout: int = 15) -> Any:
    body = None if data is None else json.dumps(data).encode("utf-8")
    headers = {"User-Agent": "openwrt-mihomo-autopilot", "Accept": "application/json"}
    if secret:
        headers["Authorization"] = f"Bearer {secret}"
    if body is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        text = resp.read().decode("utf-8", "replace")
        if not text:
            return None
        return json.loads(text)


def github_request(url: str, token: str, method: str = "GET", data: Optional[dict] = None, timeout: int = 30) -> Any:
    body = None if data is None else json.dumps(data).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "openwrt-mihomo-autopilot",
    }
    if body is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        text = resp.read().decode("utf-8", "replace")
        return json.loads(text) if text else None


def summarize_log(path: str, max_lines: int = 300) -> Dict[str, Any]:
    p = Path(path)
    if not p.exists():
        return {"exists": False}
    lines = p.read_text(encoding="utf-8", errors="ignore").splitlines()[-max_lines:]
    switches = []
    group_counts: Dict[str, int] = {}
    fail_counts: Dict[str, int] = {}
    delays: Dict[str, list[int]] = {}
    for line in lines:
        m = re.search(r"\[OK\]\s+([^\s]+)\s+->\s+([^\s]+)", line)
        if m:
            switches.append({"group": m.group(1), "selected": m.group(2), "line": line[-180:]})
        for g in DEFAULT_GROUPS:
            if f"[{g}]" in line:
                group_counts[g] = group_counts.get(g, 0) + 1
        for g, value in re.findall(r"([A-Z0-9_-]+):([0-9]+)ms", line):
            delays.setdefault(g, []).append(int(value))
        for g in re.findall(r"([A-Z0-9_-]+):FAIL", line):
            fail_counts[g] = fail_counts.get(g, 0) + 1
    delay_summary = {
        k: {"min": min(v), "avg": round(sum(v) / len(v), 1), "max": max(v), "samples": len(v)}
        for k, v in delays.items()
        if v
    }
    return {
        "exists": True,
        "lines_checked": len(lines),
        "unauthorized_401_count": sum("401" in x or "Unauthorized" in x for x in lines),
        "gateway_503_504_count": sum("503" in x or "504" in x for x in lines),
        "group_log_counts": group_counts,
        "fail_counts": fail_counts,
        "delay_summary": delay_summary,
        "recent_switches": switches[-10:],
        "last_lines": lines[-20:],
    }


def collect_status(api: str, secret: str, groups: list[str]) -> Dict[str, Any]:
    status: Dict[str, Any] = {
        "router": os.environ.get("ROUTER_NAME") or socket.gethostname() or "openwrt-router",
        "timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "mihomo_api": api,
        "groups": {},
        "api_ok": False,
    }
    try:
        proxies = http_json(f"{api.rstrip('/')}/proxies", secret=secret, timeout=20)
    except urllib.error.HTTPError as e:
        status["api_error"] = f"HTTP {e.code}: {e.reason}"
        return status
    except Exception as e:  # noqa: BLE001
        status["api_error"] = repr(e)
        return status

    status["api_ok"] = True
    all_proxies = proxies.get("proxies", {}) if isinstance(proxies, dict) else {}
    for name in groups:
        item = all_proxies.get(name)
        if not isinstance(item, dict):
            continue
        status["groups"][name] = {
            "type": item.get("type"),
            "now": item.get("now"),
            "all_count": len(item.get("all", []) or []),
            "udp": item.get("udp"),
            "history_last_delay": None,
        }
        history = item.get("history") or []
        if history and isinstance(history[-1], dict):
            status["groups"][name]["history_last_delay"] = history[-1].get("delay")
    return status


def upload_to_github(repo: str, branch: str, token: str, rel_path: str, content: str, message: str) -> None:
    encoded_path = "/".join(urllib.parse.quote(part) for part in rel_path.split("/"))
    base = f"https://api.github.com/repos/{repo}/contents/{encoded_path}"
    sha = None
    try:
        existing = github_request(f"{base}?ref={urllib.parse.quote(branch)}", token=token, method="GET")
        if isinstance(existing, dict):
            sha = existing.get("sha")
    except urllib.error.HTTPError as e:
        if e.code != 404:
            body = e.read().decode("utf-8", "replace")
            raise RuntimeError(f"GitHub GET gagal: HTTP {e.code} {body}") from e
    payload = {
        "message": message,
        "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
        "branch": branch,
    }
    if sha:
        payload["sha"] = sha
    github_request(base, token=token, method="PUT", data=payload)


def dispatch_github(repo: str, token: str, payload: dict, event_type: str = "router_feedback") -> None:
    url = f"https://api.github.com/repos/{repo}/dispatches"
    github_request(url, token=token, method="POST", data={"event_type": event_type, "client_payload": payload})


def main() -> int:
    parser = argparse.ArgumentParser(description="Report Mihomo/OpenClash status to local JSON and GitHub.")
    parser.add_argument("--env", default=os.environ.get("ENV_FILE", "/etc/mihomo-autopilot/github.env"))
    parser.add_argument("--output", default=os.environ.get("ROUTER_STATUS_OUTPUT", "/tmp/router_status.json"))
    parser.add_argument("--upload", action="store_true", help="upload status JSON to GitHub contents API")
    parser.add_argument("--trigger", action="store_true", help="send repository_dispatch after upload/status")
    parser.add_argument("--groups", default=",".join(DEFAULT_GROUPS))
    args = parser.parse_args()

    load_env(args.env)
    api = os.environ.get("MIHOMO_API", "http://127.0.0.1:9090")
    secret = os.environ.get("MIHOMO_SECRET", "reyre")
    repo = os.environ.get("GITHUB_REPO", "")
    branch = os.environ.get("GITHUB_BRANCH", "main")
    token = os.environ.get("GITHUB_TOKEN", "")
    router = os.environ.get("ROUTER_NAME") or socket.gethostname() or "openwrt-router"
    safe_router = re.sub(r"[^A-Za-z0-9_.-]+", "-", router).strip("-") or "openwrt-router"
    groups = [x.strip() for x in args.groups.split(",") if x.strip()]

    status = collect_status(api, secret, groups)
    status["router"] = router
    status["log_summary"] = summarize_log(os.environ.get("AUTOPILOT_LOG", "/tmp/mihomo_autopilot.log"))
    status["generated_by"] = "openwrt_report_status.py"

    text = json.dumps(status, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    Path(args.output).write_text(text, encoding="utf-8")
    print(f"Status saved: {args.output}")

    if args.upload:
        if not repo or not token:
            print("Skip upload: GITHUB_REPO/GITHUB_TOKEN belum diisi.", file=sys.stderr)
        else:
            rel_path = f"router_feedback/{safe_router}_latest_status.json"
            upload_to_github(repo, branch, token, rel_path, text, f"router feedback: {safe_router}")
            print(f"Uploaded to GitHub: {rel_path}")

    if args.trigger:
        if not repo or not token:
            print("Skip dispatch: GITHUB_REPO/GITHUB_TOKEN belum diisi.", file=sys.stderr)
        else:
            dispatch_payload = {
                "router": router,
                "api_ok": status.get("api_ok"),
                "reason": "router-status-report",
                "timestamp_utc": status.get("timestamp_utc"),
                "groups": {k: v.get("now") for k, v in status.get("groups", {}).items() if isinstance(v, dict)},
            }
            dispatch_github(repo, token, dispatch_payload)
            print("GitHub repository_dispatch sent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
