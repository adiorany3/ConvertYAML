#!/bin/sh
# Fresh guard: if AutoPilot sees repeated failures, pull GitHub fresh pool before all nodes die.
set -eu

ENV_FILE="${ENV_FILE:-/etc/mihomo-autopilot/github.env}"
[ -f "$ENV_FILE" ] && . "$ENV_FILE"
BASE="${BASE:-/etc/mihomo-autopilot}"
LOG="${FRESH_GUARD_LOG:-/tmp/mihomo_fresh_guard.log}"
AUTOPILOT_LOG="${AUTOPILOT_LOG:-/tmp/mihomo_autopilot.log}"
STATE="${FRESH_GUARD_STATE:-/tmp/mihomo_fresh_guard_state}"
THRESHOLD="${FRESH_FAIL_THRESHOLD:-6}"
WINDOW_LINES="${FRESH_LOG_WINDOW_LINES:-80}"
COOLDOWN_SECONDS="${FRESH_PULL_COOLDOWN_SECONDS:-900}"
TRIGGER_REBUILD="${FRESH_TRIGGER_REBUILD:-1}"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG"; }
now() { date +%s; }

LAST=0
[ -f "$STATE" ] && LAST="$(cat "$STATE" 2>/dev/null || echo 0)"
case "$LAST" in ''|*[!0-9]*) LAST=0;; esac
AGE=$(( $(now) - LAST ))

if [ "$AGE" -lt "$COOLDOWN_SECONDS" ]; then
  log "Skip fresh pull: cooldown ${AGE}/${COOLDOWN_SECONDS}s"
  exit 0
fi

if [ ! -s "$AUTOPILOT_LOG" ]; then
  log "AutoPilot log belum ada, skip."
  exit 0
fi

FAILS="$(tail -n "$WINDOW_LINES" "$AUTOPILOT_LOG" | grep -E "FAIL|timeout|Timeout|503|504|Unauthorized|ERROR" | wc -l | tr -d ' ')"
case "$FAILS" in ''|*[!0-9]*) FAILS=0;; esac
log "Fresh guard check: fails=$FAILS threshold=$THRESHOLD"

if [ "$FAILS" -lt "$THRESHOLD" ]; then
  exit 0
fi

# Prevent repeated emergency pulls.
date +%s > "$STATE"

if [ "$TRIGGER_REBUILD" = "1" ] && [ -x "$BASE/trigger_github_rebuild.sh" ]; then
  log "Trigger GitHub rebuild karena fail berulang."
  sh "$BASE/trigger_github_rebuild.sh" >> "$LOG" 2>&1 || true
fi

# Give GitHub a little time if rebuild was triggered; still pull existing fresh pool immediately.
log "Pull fresh pool sekarang."
sh "$BASE/openwrt_pull_fresh_pool.sh" >> "$LOG" 2>&1 || exit 1
