#!/bin/sh
set -eu

DEST="/etc/mihomo-autopilot"
SRC_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
SCRIPT_SRC="$SRC_DIR/mihomo_autopilot.py"
SCRIPT_DST="$DEST/mihomo_autopilot.py"
CRON_LINE="*/2 * * * * MIHOMO_API=${MIHOMO_API:-http://127.0.0.1:9090} MIHOMO_SECRET=${MIHOMO_SECRET:-} python3 $SCRIPT_DST --once --close-connections >> /tmp/mihomo_autopilot.log 2>&1"

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 belum ada. Install dulu di OpenWrt: opkg update && opkg install python3"
  exit 1
fi

if [ ! -f "$SCRIPT_SRC" ]; then
  echo "File $SCRIPT_SRC tidak ditemukan. Jalankan installer dari folder scripts di ZIP repo."
  exit 1
fi

mkdir -p "$DEST"
cp "$SCRIPT_SRC" "$SCRIPT_DST"
chmod +x "$SCRIPT_DST"

# Backup crontab lama
crontab -l 2>/dev/null > /tmp/current_cron_autopilot || true
# Hapus baris autopilot lama agar tidak dobel
grep -v "mihomo_autopilot.py" /tmp/current_cron_autopilot > /tmp/new_cron_autopilot || true
printf '%s\n' "$CRON_LINE" >> /tmp/new_cron_autopilot
crontab /tmp/new_cron_autopilot
/etc/init.d/cron enable >/dev/null 2>&1 || true
/etc/init.d/cron restart >/dev/null 2>&1 || true

echo "AutoPilot terpasang. Tes manual:"
echo "python3 $SCRIPT_DST --once --close-connections"
echo "Log otomatis: tail -f /tmp/mihomo_autopilot.log"
