#!/bin/sh
# Download fresh_candidates.txt/json from GitHub for inspection or manual import.
set -eu
ENV_FILE="${ENV_FILE:-/etc/mihomo-autopilot/github.env}"
[ -f "$ENV_FILE" ] && . "$ENV_FILE"
GITHUB_REPO="${GITHUB_REPO:-}"
GITHUB_BRANCH="${GITHUB_BRANCH:-main}"
GITHUB_TOKEN="${GITHUB_TOKEN:-}"
DEST_DIR="${DEST_DIR:-/etc/mihomo-autopilot/fresh_pool}"
RAW_BASE="${GITHUB_RAW_BASE:-}"
[ -n "$GITHUB_REPO" ] || [ -n "$RAW_BASE" ] || { echo "GITHUB_REPO belum diisi"; exit 1; }
mkdir -p "$DEST_DIR"
base="${RAW_BASE:-https://raw.githubusercontent.com/$GITHUB_REPO/$GITHUB_BRANCH}"
for f in fresh_candidates.txt fresh_candidates_strict.txt fresh_candidates.json fresh_candidates_report.md; do
  url="$base/fresh_pool/$f"
  echo "Download $url"
  if command -v curl >/dev/null 2>&1; then
    if [ -n "$GITHUB_TOKEN" ]; then curl -fsSL -H "Authorization: Bearer $GITHUB_TOKEN" "$url" -o "$DEST_DIR/$f"; else curl -fsSL "$url" -o "$DEST_DIR/$f"; fi
  else
    if [ -n "$GITHUB_TOKEN" ]; then wget -q --header="Authorization: Bearer $GITHUB_TOKEN" -O "$DEST_DIR/$f" "$url"; else wget -q -O "$DEST_DIR/$f" "$url"; fi
  fi
done
ls -lh "$DEST_DIR"
