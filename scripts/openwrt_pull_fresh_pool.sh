#!/bin/sh
# Pull emergency fresh OpenClash config from GitHub.
# Use when active nodes start dying before connection fully drops.
set -eu

ENV_FILE="${ENV_FILE:-/etc/mihomo-autopilot/github.env}"
[ -f "$ENV_FILE" ] && . "$ENV_FILE"
BASE="${BASE:-/etc/mihomo-autopilot}"
LOG="${FRESH_PULL_LOG:-/tmp/mihomo_fresh_pool.log}"
FRESH_CONFIG_NAME="${FRESH_CONFIG_NAME:-openclash_fresh_pool.yaml}"
FRESH_FALLBACK_CONFIGS="${FRESH_FALLBACK_CONFIGS:-openclash_auto.yaml openclash_lite.yaml}"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG"; }

pull_one() {
  name="$1"
  log "Mencoba pull fresh config: $name"
  if CONFIG_NAME="$name" ROLLBACK_ON_FAIL=1 RESTART_OPENCLASH=1 sh "$BASE/openwrt_pull_config.sh" >> "$LOG" 2>&1; then
    log "Config berhasil dipasang: $name"
    if [ -x "$BASE/force_after_openclash_reload.sh" ]; then
      FORCE_AVOID_DIRECT=1 sh "$BASE/force_after_openclash_reload.sh" >> "$LOG" 2>&1 || true
    fi
    return 0
  fi
  log "Gagal pull/install: $name"
  return 1
}

if pull_one "$FRESH_CONFIG_NAME"; then
  exit 0
fi

for cfg in $FRESH_FALLBACK_CONFIGS; do
  if pull_one "$cfg"; then
    exit 0
  fi
done

log "ERROR: semua fresh/fallback config gagal dipasang"
exit 1
