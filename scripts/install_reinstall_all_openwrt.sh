#!/bin/sh
# One-click install/reinstall untuk ConvertYAML OpenWrt toolkit.
# Aman dijalankan berulang.
# Prinsip utama:
# - Tidak menimpa, menghapus, atau mengubah /etc/mihomo-autopilot/github.env jika file sudah ada.
# - Mem-backup crontab lama sebelum menulis ulang baris cron project.
# - Menghapus duplikasi cron project lama, lalu memasang block cron standar.
# - Menyalin ulang semua script terbaru ke /etc/mihomo-autopilot.
# - Memeriksa dependency, file wajib, wrapper, cron, dan akses Mihomo API.

set -u

BASE="${BASE:-/etc/mihomo-autopilot}"
ENV_FILE="${ENV_FILE:-$BASE/github.env}"
BACKUP_DIR="$BASE/backups"
SRC_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
ACTION="${1:-install}"
INSTALL_PACKAGES="${INSTALL_PACKAGES:-1}"
MIHOMO_DEFAULT_API="${MIHOMO_API:-http://127.0.0.1:9090}"
MIHOMO_DEFAULT_SECRET="${MIHOMO_SECRET:-reyre}"
AUTOPILOT_INTERVAL="${AUTOPILOT_INTERVAL:-2}"
REPORT_INTERVAL="${REPORT_INTERVAL:-15}"
CONFIG_PULL_HOUR_STEP="${CONFIG_PULL_HOUR_STEP:-3}"
FRESH_GUARD_INTERVAL="${FRESH_GUARD_INTERVAL:-5}"

say() { printf '%s\n' "$*"; }
ok() { printf '[OK] %s\n' "$*"; }
warn() { printf '[WARN] %s\n' "$*"; }
err() { printf '[ERROR] %s\n' "$*" >&2; }

usage() {
  cat <<USAGE
Usage:
  sh install_reinstall_all_openwrt.sh            # install/reinstall + check
  sh install_reinstall_all_openwrt.sh install    # sama seperti default
  sh install_reinstall_all_openwrt.sh check      # hanya periksa, tidak menyalin/cron

Environment opsional:
  BASE='/etc/mihomo-autopilot'
  ENV_FILE='/etc/mihomo-autopilot/github.env'
  INSTALL_PACKAGES='1'   # 1=install python3/curl/ca-certificates kalau hilang, 0=skip
  MIHOMO_API='http://127.0.0.1:9090'
  MIHOMO_SECRET='reyre'  # hanya dipakai saat github.env belum ada
USAGE
}

case "$ACTION" in
  install|reinstall|check|-h|--help) ;;
  *) warn "Aksi tidak dikenal: $ACTION, memakai install."; ACTION="install" ;;
esac
if [ "$ACTION" = "-h" ] || [ "$ACTION" = "--help" ]; then
  usage
  exit 0
fi

require_or_install_packages() {
  missing=""
  command -v python3 >/dev/null 2>&1 || missing="$missing python3"
  command -v curl >/dev/null 2>&1 || missing="$missing curl"

  if [ -z "$missing" ]; then
    ok "Dependency utama tersedia: python3 dan curl."
    return 0
  fi

  warn "Dependency belum lengkap:$missing"
  if [ "$INSTALL_PACKAGES" = "1" ] && command -v opkg >/dev/null 2>&1; then
    say "Mencoba install dependency via opkg..."
    opkg update || warn "opkg update gagal, lanjut cek manual."
    opkg install python3 curl ca-certificates || warn "opkg install gagal, install manual mungkin diperlukan."
  else
    warn "INSTALL_PACKAGES=0 atau opkg tidak tersedia. Install manual: opkg update && opkg install python3 curl ca-certificates"
  fi

  command -v python3 >/dev/null 2>&1 || { err "python3 masih belum tersedia."; return 1; }
  command -v curl >/dev/null 2>&1 || warn "curl masih belum tersedia. Beberapa test API/GitHub akan dilewati."
  return 0
}

create_env_if_missing() {
  mkdir -p "$BASE" "$BACKUP_DIR"

  if [ -f "$ENV_FILE" ]; then
    cp "$ENV_FILE" "$BACKUP_DIR/github.env.backup.$(date +%Y%m%d-%H%M%S)" 2>/dev/null || true
    chmod 600 "$ENV_FILE" 2>/dev/null || true
    ok "Env sudah ada dan TIDAK ditimpa: $ENV_FILE"
    return 0
  fi

  warn "Env belum ada. Membuat template baru: $ENV_FILE"
  cat > "$ENV_FILE" <<EOFENV
# Router <-> GitHub Sync configuration
# File ini aman: installer/reinstaller tidak akan menimpa file ini kalau sudah ada.

GITHUB_REPO='username/repo'
GITHUB_BRANCH='main'
GITHUB_TOKEN=''
ROUTER_NAME='openwrt-home'

MIHOMO_API='$MIHOMO_DEFAULT_API'
MIHOMO_SECRET='$MIHOMO_DEFAULT_SECRET'
OPENCLASH_CONFIG_DIR='/etc/openclash/config'
CONFIG_NAME='openclash_auto.yaml'
FRESH_CONFIG_NAME='openclash_fresh_pool.yaml'

FRESH_FAIL_THRESHOLD='6'
FRESH_PULL_COOLDOWN_SECONDS='900'
FRESH_TRIGGER_REBUILD='1'

FORCE_WAIT_SECONDS='90'
FORCE_PASSES='3'
FORCE_SLEEP_BETWEEN='5'
FORCE_AVOID_DIRECT='1'
EOFENV
  chmod 600 "$ENV_FILE" 2>/dev/null || true
  ok "Template env dibuat. Edit nanti: vi $ENV_FILE"
}

copy_scripts() {
  mkdir -p "$BASE" "$BACKUP_DIR"

  required="mihomo_autopilot.py mihomo_force_ping_all.py force_after_openclash_reload.sh openclash_reload_guard.sh openwrt_pull_config.sh openwrt_report_status.py openwrt_download_fresh_candidates.sh openwrt_fresh_guard.sh openwrt_pull_fresh_pool.sh trigger_github_rebuild.sh rollback_openclash_config.sh run_autopilot_once.sh"
  optional="install_autopilot_openwrt.sh install_force_after_reload_openwrt.sh install_router_github_sync_openwrt.sh install_reinstall_all_openwrt.sh"

  for f in $required; do
    if [ ! -f "$SRC_DIR/$f" ]; then
      err "File wajib tidak ditemukan di $SRC_DIR/$f"
      return 1
    fi
  done

  for f in $required $optional; do
    if [ -f "$SRC_DIR/$f" ]; then
      cp "$SRC_DIR/$f" "$BASE/$f" || return 1
      chmod +x "$BASE/$f" 2>/dev/null || true
    fi
  done

  ok "Semua script utama disalin ulang ke $BASE"
}

install_wrapper() {
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
  chmod +x /usr/bin/openclash-reload-autopilot 2>/dev/null || true
  ok "Wrapper terpasang: /usr/bin/openclash-reload-autopilot"
}

install_cron_block() {
  mkdir -p "$BACKUP_DIR"
  old="$BACKUP_DIR/crontab.backup.$(date +%Y%m%d-%H%M%S)"
  tmp1="/tmp/mihomo_cron_current.$$"
  tmp2="/tmp/mihomo_cron_new.$$"

  crontab -l 2>/dev/null > "$tmp1" || true
  cp "$tmp1" "$old" 2>/dev/null || true

  # Hapus block managed dan baris lama project agar tidak dobel.
  awk '
    /BEGIN MIHOMO_AUTOPILOT_MANAGED/ {skip=1; next}
    /END MIHOMO_AUTOPILOT_MANAGED/ {skip=0; next}
    skip==1 {next}
    {print}
  ' "$tmp1" \
  | grep -v "mihomo_autopilot.py" \
  | grep -v "mihomo_force_ping_all.py" \
  | grep -v "openwrt_report_status.py" \
  | grep -v "openwrt_pull_config.sh" \
  | grep -v "openwrt_fresh_guard.sh" \
  | grep -v "openwrt_pull_fresh_pool.sh" \
  | grep -v "openwrt_download_fresh_candidates.sh" \
  | grep -v "force_after_openclash_reload.sh" \
  | grep -v "openclash_reload_guard.sh" \
  > "$tmp2" || true

  cat >> "$tmp2" <<EOFCRON
# BEGIN MIHOMO_AUTOPILOT_MANAGED
# AutoPilot self-healing, setiap $AUTOPILOT_INTERVAL menit
*/$AUTOPILOT_INTERVAL * * * * . $ENV_FILE; python3 $BASE/mihomo_autopilot.py --once --close-connections >> /tmp/mihomo_autopilot.log 2>&1
# Force ping semua akun/node, setiap 10 menit agar OpenClash punya data delay
*/10 * * * * . $ENV_FILE; python3 $BASE/mihomo_force_ping_all.py >> /tmp/mihomo_force_ping_all.log 2>&1
# Router -> GitHub feedback, setiap $REPORT_INTERVAL menit
*/$REPORT_INTERVAL * * * * . $ENV_FILE; python3 $BASE/openwrt_report_status.py --upload >> /tmp/router_github_sync.log 2>&1
# GitHub -> Router config pull, setiap $CONFIG_PULL_HOUR_STEP jam di menit 5
5 */$CONFIG_PULL_HOUR_STEP * * * . $ENV_FILE; sh $BASE/openwrt_pull_config.sh >> /tmp/router_github_sync.log 2>&1
# Emergency fresh pool guard, setiap $FRESH_GUARD_INTERVAL menit
*/$FRESH_GUARD_INTERVAL * * * * . $ENV_FILE; sh $BASE/openwrt_fresh_guard.sh >> /tmp/mihomo_fresh_guard.log 2>&1
# Force node siap saat router/OpenClash baru boot
@reboot sleep 70; . $ENV_FILE; sh $BASE/force_after_openclash_reload.sh >> /tmp/mihomo_force_after_reload.log 2>&1
# Deteksi reload dari LuCI/OpenClash lalu paksa node siap
* * * * . $ENV_FILE; sh $BASE/openclash_reload_guard.sh >/dev/null 2>&1
# END MIHOMO_AUTOPILOT_MANAGED
EOFCRON

  crontab "$tmp2" || return 1
  rm -f "$tmp1" "$tmp2"
  /etc/init.d/cron enable >/dev/null 2>&1 || true
  /etc/init.d/cron restart >/dev/null 2>&1 || true
  ok "Cron project dipasang ulang tanpa menyentuh env. Backup crontab: $old"
}

load_env_safely() {
  if [ -f "$ENV_FILE" ]; then
    # shellcheck disable=SC1090
    . "$ENV_FILE"
  fi
}

check_files() {
  missing="0"
  for f in mihomo_autopilot.py mihomo_force_ping_all.py force_after_openclash_reload.sh openclash_reload_guard.sh openwrt_pull_config.sh openwrt_report_status.py openwrt_fresh_guard.sh rollback_openclash_config.sh; do
    if [ -f "$BASE/$f" ]; then
      ok "Ada: $BASE/$f"
    else
      err "Hilang: $BASE/$f"
      missing="1"
    fi
  done
  [ "$missing" = "0" ] || return 1
  return 0
}

check_cron() {
  if crontab -l 2>/dev/null | grep -q "BEGIN MIHOMO_AUTOPILOT_MANAGED"; then
    ok "Cron managed block aktif."
  else
    warn "Cron managed block belum ditemukan."
  fi
  count="$(crontab -l 2>/dev/null | grep -c "mihomo_autopilot.py" || true)"
  say "Jumlah baris mihomo_autopilot.py di cron: $count"
}

check_api() {
  load_env_safely
  API="${MIHOMO_API:-$MIHOMO_DEFAULT_API}"
  SECRET="${MIHOMO_SECRET:-$MIHOMO_DEFAULT_SECRET}"

  if ! command -v curl >/dev/null 2>&1; then
    warn "curl tidak ada, skip test API Mihomo."
    return 0
  fi

  if [ -n "$SECRET" ]; then
    code="$(curl -sS -m 6 -o /tmp/mihomo_api_test.out -w '%{http_code}' -H "Authorization: Bearer $SECRET" "$API/proxies" 2>/tmp/mihomo_api_test.err || true)"
  else
    code="$(curl -sS -m 6 -o /tmp/mihomo_api_test.out -w '%{http_code}' "$API/proxies" 2>/tmp/mihomo_api_test.err || true)"
  fi

  case "$code" in
    200) ok "Mihomo API bisa diakses: $API" ;;
    401) warn "Mihomo API 401 Unauthorized. Cek MIHOMO_SECRET di $ENV_FILE" ;;
    000) warn "Mihomo API belum bisa diakses. OpenClash mungkin belum aktif atau port bukan 9090." ;;
    *) warn "Mihomo API memberi HTTP $code. Cek /tmp/mihomo_api_test.err" ;;
  esac
}

check_openclash() {
  if [ -x /etc/init.d/openclash ]; then
    ok "OpenClash init script ditemukan."
  else
    warn "OpenClash init script tidak ditemukan di /etc/init.d/openclash."
  fi
  if [ -x /usr/bin/openclash-reload-autopilot ]; then
    ok "Wrapper reload tersedia: openclash-reload-autopilot"
  else
    warn "Wrapper reload belum tersedia."
  fi
}

run_check() {
  say "=== CHECK OPENWRT INSTALL ==="
  [ -f "$ENV_FILE" ] && ok "Env ada dan tidak diubah: $ENV_FILE" || warn "Env belum ada: $ENV_FILE"
  command -v python3 >/dev/null 2>&1 && ok "python3 tersedia." || warn "python3 belum tersedia."
  command -v curl >/dev/null 2>&1 && ok "curl tersedia." || warn "curl belum tersedia."
  check_files || true
  check_cron || true
  check_openclash || true
  check_api || true
  say "=== CHECK SELESAI ==="
}

if [ "$ACTION" = "check" ]; then
  run_check
  exit 0
fi

say "=== INSTALL/REINSTALL CONVERTYAML OPENWRT TOOLKIT ==="
say "Base    : $BASE"
say "Env     : $ENV_FILE"
say "Source  : $SRC_DIR"
say "Catatan : env yang sudah ada tidak akan ditimpa/diubah."

require_or_install_packages || exit 1
create_env_if_missing || exit 1
copy_scripts || exit 1
install_wrapper || exit 1
install_cron_block || exit 1
run_check

say ""
ok "Install/reinstall selesai."
say "Perintah penting:"
say "  sh $BASE/install_reinstall_all_openwrt.sh check"
say "  openclash-reload-autopilot restart"
say "  tail -f /tmp/mihomo_autopilot.log"
say "  tail -f /tmp/mihomo_force_after_reload.log"
say "  tail -f /tmp/mihomo_fresh_guard.log"
say ""
say "Env kamu tetap aman di: $ENV_FILE"
