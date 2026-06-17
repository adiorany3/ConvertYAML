#!/bin/sh
set -eu

DEST="/etc/mihomo-autopilot"
SRC_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
SCRIPT_SRC="$SRC_DIR/mihomo_autopilot.py"
SCRIPT_DST="$DEST/mihomo_autopilot.py"
AUTOPILOT_API="${MIHOMO_API:-http://127.0.0.1:9090}"
AUTOPILOT_SECRET="${MIHOMO_SECRET:-reyre}"
AUTOPILOT_INTERVAL="${AUTOPILOT_INTERVAL:-2}"

sh_quote() {
  # Safe single-quote for crontab env values.
  printf "'%s'" "$(printf "%s" "$1" | sed "s/'/'\\\\''/g")"
}

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 belum ada. Install dulu di OpenWrt: opkg update && opkg install python3"
  exit 1
fi

if [ ! -f "$SCRIPT_SRC" ]; then
  echo "File $SCRIPT_SRC tidak ditemukan. Jalankan installer dari folder scripts di ZIP repo."
  exit 1
fi

case "$AUTOPILOT_INTERVAL" in
  ''|*[!0-9]*) AUTOPILOT_INTERVAL=2 ;;
esac
if [ "$AUTOPILOT_INTERVAL" -lt 1 ]; then
  AUTOPILOT_INTERVAL=1
fi

mkdir -p "$DEST"
cp "$SCRIPT_SRC" "$SCRIPT_DST"
chmod +x "$SCRIPT_DST"

API_Q=$(sh_quote "$AUTOPILOT_API")
SECRET_Q=$(sh_quote "$AUTOPILOT_SECRET")
CRON_LINE="*/$AUTOPILOT_INTERVAL * * * * MIHOMO_API=$API_Q MIHOMO_SECRET=$SECRET_Q python3 $SCRIPT_DST --once --close-connections >> /tmp/mihomo_autopilot.log 2>&1"

# Backup crontab lama
crontab -l 2>/dev/null > /tmp/current_cron_autopilot || true
# Hapus baris autopilot lama agar tidak dobel
grep -v "mihomo_autopilot.py" /tmp/current_cron_autopilot > /tmp/new_cron_autopilot || true
printf '%s\n' "$CRON_LINE" >> /tmp/new_cron_autopilot
crontab /tmp/new_cron_autopilot
/etc/init.d/cron enable >/dev/null 2>&1 || true
/etc/init.d/cron restart >/dev/null 2>&1 || true

echo "AutoPilot terpasang."
echo "API    : $AUTOPILOT_API"
echo "Secret : $AUTOPILOT_SECRET"
echo "Cron   : setiap $AUTOPILOT_INTERVAL menit"
echo "Tes manual:"
echo "MIHOMO_SECRET='$AUTOPILOT_SECRET' python3 $SCRIPT_DST --once --close-connections"
echo "Log otomatis: tail -f /tmp/mihomo_autopilot.log"
