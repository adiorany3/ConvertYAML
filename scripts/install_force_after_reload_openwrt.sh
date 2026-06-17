#!/bin/sh
# Installer force-after-reload untuk OpenWrt/OpenClash.
# Fitur:
# - Menyalin force_after_openclash_reload.sh dan openclash_reload_guard.sh
# - Menambahkan cron @reboot dan guard tiap 1 menit
# - Membuat wrapper /usr/bin/openclash-reload-autopilot

set -eu

DEST="/etc/mihomo-autopilot"
SRC_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
MIHOMO_API="${MIHOMO_API:-http://127.0.0.1:9090}"
MIHOMO_SECRET="${MIHOMO_SECRET:-reyre}"
FORCE_WAIT_SECONDS="${FORCE_WAIT_SECONDS:-90}"
FORCE_PASSES="${FORCE_PASSES:-3}"
FORCE_SLEEP_BETWEEN="${FORCE_SLEEP_BETWEEN:-5}"
FORCE_AVOID_DIRECT="${FORCE_AVOID_DIRECT:-1}"

sh_quote() {
  printf "'%s'" "$(printf "%s" "$1" | sed "s/'/'\\''/g")"
}

need_file() {
  if [ ! -f "$SRC_DIR/$1" ]; then
    echo "File $SRC_DIR/$1 tidak ditemukan. Jalankan installer dari folder scripts."
    exit 1
  fi
}

need_file "force_after_openclash_reload.sh"
need_file "openclash_reload_guard.sh"
need_file "mihomo_autopilot.py"
need_file "mihomo_force_ping_all.py"

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 belum ada. Install dulu: opkg update && opkg install python3"
  exit 1
fi

mkdir -p "$DEST"
cp "$SRC_DIR/mihomo_autopilot.py" "$DEST/mihomo_autopilot.py"
cp "$SRC_DIR/mihomo_force_ping_all.py" "$DEST/mihomo_force_ping_all.py"
cp "$SRC_DIR/force_after_openclash_reload.sh" "$DEST/force_after_openclash_reload.sh"
cp "$SRC_DIR/openclash_reload_guard.sh" "$DEST/openclash_reload_guard.sh"
chmod +x "$DEST/mihomo_autopilot.py" "$DEST/mihomo_force_ping_all.py" "$DEST/force_after_openclash_reload.sh" "$DEST/openclash_reload_guard.sh"

# Simpan env lokal kalau belum ada. Kalau sudah ada, jangan overwrite token GitHub/user setting lain.
ENV_FILE="$DEST/github.env"
if [ ! -f "$ENV_FILE" ]; then
  cat > "$ENV_FILE" <<ENV
MIHOMO_API='$MIHOMO_API'
MIHOMO_SECRET='$MIHOMO_SECRET'
FORCE_WAIT_SECONDS='$FORCE_WAIT_SECONDS'
FORCE_PASSES='$FORCE_PASSES'
FORCE_SLEEP_BETWEEN='$FORCE_SLEEP_BETWEEN'
FORCE_AVOID_DIRECT='$FORCE_AVOID_DIRECT'
ENV
  chmod 600 "$ENV_FILE"
else
  # Pastikan minimal variabel force ada kalau belum pernah ditulis.
  grep -q '^MIHOMO_API=' "$ENV_FILE" || echo "MIHOMO_API='$MIHOMO_API'" >> "$ENV_FILE"
  grep -q '^MIHOMO_SECRET=' "$ENV_FILE" || echo "MIHOMO_SECRET='$MIHOMO_SECRET'" >> "$ENV_FILE"
  grep -q '^FORCE_WAIT_SECONDS=' "$ENV_FILE" || echo "FORCE_WAIT_SECONDS='$FORCE_WAIT_SECONDS'" >> "$ENV_FILE"
  grep -q '^FORCE_PASSES=' "$ENV_FILE" || echo "FORCE_PASSES='$FORCE_PASSES'" >> "$ENV_FILE"
  grep -q '^FORCE_SLEEP_BETWEEN=' "$ENV_FILE" || echo "FORCE_SLEEP_BETWEEN='$FORCE_SLEEP_BETWEEN'" >> "$ENV_FILE"
  grep -q '^FORCE_AVOID_DIRECT=' "$ENV_FILE" || echo "FORCE_AVOID_DIRECT='$FORCE_AVOID_DIRECT'" >> "$ENV_FILE"
  chmod 600 "$ENV_FILE"
fi

# Wrapper reload/restart agar user bisa reload OpenClash sekaligus force node siap.
cat > /usr/bin/openclash-reload-autopilot <<'WRAP'
#!/bin/sh
ACTION="${1:-restart}"
case "$ACTION" in
  start|stop|restart|reload) ;;
  *) ACTION="restart" ;;
esac

if [ -f /etc/mihomo-autopilot/github.env ]; then
  . /etc/mihomo-autopilot/github.env
fi

/etc/init.d/openclash "$ACTION"
( sleep 10; sh /etc/mihomo-autopilot/force_after_openclash_reload.sh >> /tmp/mihomo_force_after_reload.log 2>&1 ) &
echo "OpenClash $ACTION dijalankan. Force-after-reload berjalan di background."
echo "Cek log: tail -f /tmp/mihomo_force_after_reload.log"
WRAP
chmod +x /usr/bin/openclash-reload-autopilot

API_Q=$(sh_quote "$MIHOMO_API")
SECRET_Q=$(sh_quote "$MIHOMO_SECRET")
WAIT_Q=$(sh_quote "$FORCE_WAIT_SECONDS")
PASSES_Q=$(sh_quote "$FORCE_PASSES")
SLEEP_Q=$(sh_quote "$FORCE_SLEEP_BETWEEN")
AVOID_Q=$(sh_quote "$FORCE_AVOID_DIRECT")

BOOT_LINE="@reboot sleep 70; MIHOMO_API=$API_Q MIHOMO_SECRET=$SECRET_Q FORCE_WAIT_SECONDS=$WAIT_Q FORCE_PASSES=$PASSES_Q FORCE_SLEEP_BETWEEN=$SLEEP_Q FORCE_AVOID_DIRECT=$AVOID_Q sh $DEST/force_after_openclash_reload.sh >> /tmp/mihomo_force_after_reload.log 2>&1"
GUARD_LINE="* * * * sh $DEST/openclash_reload_guard.sh >/dev/null 2>&1"

crontab -l 2>/dev/null > /tmp/current_cron_force_reload || true
grep -v "force_after_openclash_reload.sh" /tmp/current_cron_force_reload | grep -v "openclash_reload_guard.sh" > /tmp/new_cron_force_reload || true
printf '%s\n' "$BOOT_LINE" >> /tmp/new_cron_force_reload
printf '%s\n' "$GUARD_LINE" >> /tmp/new_cron_force_reload
crontab /tmp/new_cron_force_reload
/etc/init.d/cron enable >/dev/null 2>&1 || true
/etc/init.d/cron restart >/dev/null 2>&1 || true

echo "Force-after-reload terpasang."
echo "API     : $MIHOMO_API"
echo "Secret  : $MIHOMO_SECRET"
echo "Passes  : $FORCE_PASSES"
echo "NoDirect: $FORCE_AVOID_DIRECT"
echo "Wrapper : openclash-reload-autopilot restart"
echo "Log     : tail -f /tmp/mihomo_force_after_reload.log"
echo "Guard   : aktif tiap 1 menit, mendeteksi PID core berubah setelah reload dari LuCI/OpenClash."
