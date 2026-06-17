#!/bin/sh
# Guard ringan untuk mendeteksi core Mihomo/Clash restart/reload.
# Dipanggil cron tiap 1 menit. Jika PID core berubah, jalankan force-after-reload.

set -u

DEST="/etc/mihomo-autopilot"
ENV_FILE="$DEST/github.env"
STATE_FILE="/tmp/mihomo_last_core_pid"
FORCE_SCRIPT="$DEST/force_after_openclash_reload.sh"
LOG_FILE="/tmp/mihomo_reload_guard.log"

[ -f "$ENV_FILE" ] && . "$ENV_FILE"

log() {
  printf '%s %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*" >> "$LOG_FILE"
}

get_pid() {
  pidof mihomo 2>/dev/null || pidof clash 2>/dev/null || pidof clash.meta 2>/dev/null || true
}

PID="$(get_pid | awk '{print $1}')"
[ -n "$PID" ] || exit 0

LAST=""
[ -f "$STATE_FILE" ] && LAST="$(cat "$STATE_FILE" 2>/dev/null || true)"

if [ "$PID" != "$LAST" ]; then
  echo "$PID" > "$STATE_FILE"
  log "[DETECT] core PID berubah: old=${LAST:-none} new=$PID. Jalankan force-after-reload."
  if [ -x "$FORCE_SCRIPT" ]; then
    # Tunggu pendek agar external-controller selesai bind setelah reload.
    ( sleep 10; sh "$FORCE_SCRIPT" >> /tmp/mihomo_force_after_reload.log 2>&1 ) &
  else
    log "[WARN] force script belum ada: $FORCE_SCRIPT"
  fi
fi
