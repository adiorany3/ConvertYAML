#!/bin/sh
# Force selector/node readiness after OpenClash/Mihomo reload.
# Tujuan: setelah OpenClash reload, jangan menunggu node siap terlalu lama.
# Script ini menunggu API Mihomo aktif, menjalankan AutoPilot beberapa pass,
# lalu menutup koneksi lama agar traffic baru langsung memakai jalur sehat.

set -u

DEST="/etc/mihomo-autopilot"
MIHOMO_API="${MIHOMO_API:-http://127.0.0.1:9090}"
MIHOMO_SECRET="${MIHOMO_SECRET:-reyre}"
AUTOPILOT_SCRIPT="${AUTOPILOT_SCRIPT:-$DEST/mihomo_autopilot.py}"
WAIT_SECONDS="${FORCE_WAIT_SECONDS:-90}"
PASSES="${FORCE_PASSES:-3}"
SLEEP_BETWEEN="${FORCE_SLEEP_BETWEEN:-5}"
DELAY_TIMEOUT_MS="${FORCE_DELAY_TIMEOUT_MS:-3000}"
MAX_DELAY_MS="${FORCE_MAX_DELAY_MS:-1500}"
LOG_FILE="${FORCE_LOG_FILE:-/tmp/mihomo_force_after_reload.log}"
FLUSH_FLAG=""
AVOID_DIRECT_FLAG=""

if [ "${FORCE_FLUSH_FAKEIP:-0}" = "1" ]; then
  FLUSH_FLAG="--flush-fakeip"
fi

# Default: setelah reload jangan izinkan selector jatuh ke DIRECT.
# Ubah FORCE_AVOID_DIRECT=0 hanya kalau benar-benar ingin DIRECT sebagai emergency fallback.
if [ "${FORCE_AVOID_DIRECT:-1}" = "1" ]; then
  AVOID_DIRECT_FLAG="--avoid-direct"
fi

log() {
  printf '%s %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*" | tee -a "$LOG_FILE"
}

has_cmd() {
  command -v "$1" >/dev/null 2>&1
}

api_ready() {
  if has_cmd curl; then
    if [ -n "$MIHOMO_SECRET" ]; then
      curl -fsS --max-time 4 -H "Authorization: Bearer $MIHOMO_SECRET" "$MIHOMO_API/proxies" >/dev/null 2>&1
    else
      curl -fsS --max-time 4 "$MIHOMO_API/proxies" >/dev/null 2>&1
    fi
    return $?
  fi

  # Fallback wget bawaan BusyBox. Wget BusyBox tidak selalu support header panjang,
  # tapi tetap dicoba supaya router minimal masih bisa mengecek API tanpa curl.
  if has_cmd wget; then
    if [ -n "$MIHOMO_SECRET" ]; then
      wget -qO- --header="Authorization: Bearer $MIHOMO_SECRET" "$MIHOMO_API/proxies" >/dev/null 2>&1
    else
      wget -qO- "$MIHOMO_API/proxies" >/dev/null 2>&1
    fi
    return $?
  fi

  return 1
}

wait_api() {
  i=0
  while [ "$i" -lt "$WAIT_SECONDS" ]; do
    if api_ready; then
      return 0
    fi
    sleep 2
    i=$((i + 2))
  done
  return 1
}

run_autopilot_pass() {
  pass="$1"
  if [ ! -f "$AUTOPILOT_SCRIPT" ]; then
    log "[ERROR] AutoPilot tidak ditemukan: $AUTOPILOT_SCRIPT"
    return 2
  fi
  if ! has_cmd python3; then
    log "[ERROR] python3 belum ada. Install: opkg update && opkg install python3"
    return 2
  fi

  log "[FORCE] AutoPilot pass $pass/$PASSES"
  MIHOMO_API="$MIHOMO_API" MIHOMO_SECRET="$MIHOMO_SECRET" \
    python3 "$AUTOPILOT_SCRIPT" --once --close-connections $FLUSH_FLAG $AVOID_DIRECT_FLAG \
      --delay-timeout-ms "$DELAY_TIMEOUT_MS" \
      --max-delay-ms "$MAX_DELAY_MS" >> "$LOG_FILE" 2>&1
}

main() {
  log "[START] force-after-reload api=$MIHOMO_API wait=${WAIT_SECONDS}s passes=$PASSES avoid_direct=${FORCE_AVOID_DIRECT:-1}"

  if ! wait_api; then
    log "[ERROR] Mihomo API belum siap setelah ${WAIT_SECONDS}s. Cek OpenClash/external-controller/secret."
    exit 2
  fi

  log "[OK] Mihomo API siap. Memaksa selector masuk jalur sehat."

  p=1
  while [ "$p" -le "$PASSES" ]; do
    run_autopilot_pass "$p"
    [ "$p" -lt "$PASSES" ] && sleep "$SLEEP_BETWEEN"
    p=$((p + 1))
  done

  log "[DONE] force-after-reload selesai"
}

main "$@"
