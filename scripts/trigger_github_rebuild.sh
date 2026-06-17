#!/bin/sh
# Trigger GitHub Actions from OpenWrt using repository_dispatch.
set -eu
ENV_FILE="${ENV_FILE:-/etc/mihomo-autopilot/github.env}"
[ -f "$ENV_FILE" ] && . "$ENV_FILE"

GITHUB_REPO="${GITHUB_REPO:-}"
GITHUB_TOKEN="${GITHUB_TOKEN:-}"
EVENT_TYPE="${EVENT_TYPE:-router_feedback}"
ROUTER_NAME="${ROUTER_NAME:-openwrt-router}"
REASON="${1:-manual-trigger}"

[ -n "$GITHUB_REPO" ] || { echo "GITHUB_REPO belum diisi di $ENV_FILE"; exit 1; }
[ -n "$GITHUB_TOKEN" ] || { echo "GITHUB_TOKEN belum diisi di $ENV_FILE"; exit 1; }

python3 - <<PY
import json, os, urllib.request
repo = os.environ.get('GITHUB_REPO', '$GITHUB_REPO')
token = os.environ.get('GITHUB_TOKEN', '$GITHUB_TOKEN')
event_type = os.environ.get('EVENT_TYPE', '$EVENT_TYPE')
router = os.environ.get('ROUTER_NAME', '$ROUTER_NAME')
reason = os.environ.get('REASON', '$REASON')
url = f'https://api.github.com/repos/{repo}/dispatches'
payload = {
    'event_type': event_type,
    'client_payload': {
        'router': router,
        'reason': reason,
        'source': 'openwrt',
    },
}
req = urllib.request.Request(
    url,
    data=json.dumps(payload).encode('utf-8'),
    headers={
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
        'Content-Type': 'application/json',
        'User-Agent': 'openwrt-mihomo-autopilot',
    },
    method='POST',
)
try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        print(f'GitHub dispatch OK: HTTP {resp.status}')
except urllib.error.HTTPError as e:
    body = e.read().decode('utf-8', 'replace')
    raise SystemExit(f'GitHub dispatch gagal: HTTP {e.code} {body}')
PY
