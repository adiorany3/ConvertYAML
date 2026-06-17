#!/bin/sh
# Install Router <-> GitHub sync helper scripts on OpenWrt.
set -eu
SRC_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
BASE="${BASE:-/etc/mihomo-autopilot}"
ENV_FILE="$BASE/github.env"
mkdir -p "$BASE" "$BASE/backups"

for f in \
  mihomo_autopilot.py \
  openwrt_pull_config.sh \
  openwrt_report_status.py \
  openwrt_download_fresh_candidates.sh \
  openwrt_fresh_guard.sh \
  openwrt_pull_fresh_pool.sh \
  trigger_github_rebuild.sh \
  rollback_openclash_config.sh \
  run_autopilot_once.sh \
  force_after_openclash_reload.sh \
  openclash_reload_guard.sh; do
  if [ -f "$SRC_DIR/$f" ]; then
    cp "$SRC_DIR/$f" "$BASE/$f"
    chmod +x "$BASE/$f"
  fi
done

if [ ! -f "$ENV_FILE" ]; then
  cat > "$ENV_FILE" <<'EOF'
# Router <-> GitHub Sync configuration
# Isi GITHUB_TOKEN dengan fine-grained token/PAT yang punya Contents: read/write.
# Untuk trigger workflow, token juga perlu akses Actions/workflows atau repo sesuai jenis token.
GITHUB_REPO='username/repo'
GITHUB_BRANCH='main'
GITHUB_TOKEN=''
ROUTER_NAME='openwrt-home'

# OpenClash/Mihomo
MIHOMO_API='http://127.0.0.1:9090'
MIHOMO_SECRET='reyre'
OPENCLASH_CONFIG_DIR='/etc/openclash/config'
CONFIG_NAME='openclash_auto.yaml'
FRESH_CONFIG_NAME='openclash_fresh_pool.yaml'
FRESH_FAIL_THRESHOLD='6'
FRESH_PULL_COOLDOWN_SECONDS='900'
FRESH_TRIGGER_REBUILD='1'

# Force-after-reload: paksa selector/node sehat setelah OpenClash reload/restart
FORCE_WAIT_SECONDS='90'
FORCE_PASSES='3'
FORCE_SLEEP_BETWEEN='5'

# Opsional: kalau repo private dan raw.githubusercontent.com gagal, tetap isi GITHUB_TOKEN.
# Opsional: override raw base, contoh:
# GITHUB_RAW_BASE='https://raw.githubusercontent.com/username/repo/main'
EOF
  chmod 600 "$ENV_FILE"
  echo "Template env dibuat: $ENV_FILE"
  echo "Edit dulu: vi $ENV_FILE"
else
  chmod 600 "$ENV_FILE"
  echo "Env sudah ada, tidak ditimpa: $ENV_FILE"
fi

# Remove old entries to avoid duplicates.
TMP_CRON="/tmp/router_github_sync_cron.$$"
crontab -l 2>/dev/null | grep -v "mihomo_autopilot.py" | grep -v "openwrt_report_status.py" | grep -v "openwrt_pull_config.sh" | grep -v "openwrt_fresh_guard.sh" | grep -v "openwrt_pull_fresh_pool.sh" | grep -v "openwrt_download_fresh_candidates.sh" | grep -v "force_after_openclash_reload.sh" | grep -v "openclash_reload_guard.sh" > "$TMP_CRON" || true
cat >> "$TMP_CRON" <<EOF
# mihomo autopilot self-healing, every 2 minutes
*/2 * * * * . $ENV_FILE; python3 $BASE/mihomo_autopilot.py --once --close-connections >> /tmp/mihomo_autopilot.log 2>&1
# router -> github feedback, every 15 minutes
*/15 * * * * . $ENV_FILE; python3 $BASE/openwrt_report_status.py --upload >> /tmp/router_github_sync.log 2>&1
# github -> router config pull, every 3 hours at minute 5
5 */3 * * * . $ENV_FILE; sh $BASE/openwrt_pull_config.sh >> /tmp/router_github_sync.log 2>&1
# emergency fresh pool guard, every 5 minutes
*/5 * * * * . $ENV_FILE; sh $BASE/openwrt_fresh_guard.sh >> /tmp/mihomo_fresh_guard.log 2>&1
# force selector/node readiness on boot after OpenClash starts
@reboot sleep 70; . $ENV_FILE; sh $BASE/force_after_openclash_reload.sh >> /tmp/mihomo_force_after_reload.log 2>&1
# detect OpenClash/Mihomo core reload from LuCI and force selector/node readiness
* * * * . $ENV_FILE; sh $BASE/openclash_reload_guard.sh >/dev/null 2>&1
EOF
crontab "$TMP_CRON"
rm -f "$TMP_CRON"
/etc/init.d/cron restart || true

echo "Install selesai."
echo "1) Edit token/repo: vi $ENV_FILE"
echo "2) Test report: python3 $BASE/openwrt_report_status.py --upload"
echo "3) Test pull: sh $BASE/openwrt_pull_config.sh"
echo "4) Lihat log sync: tail -f /tmp/router_github_sync.log"
echo "5) Force setelah reload: sh $BASE/force_after_openclash_reload.sh"
echo "6) Pull fresh pool: sh $BASE/openwrt_pull_fresh_pool.sh"
echo "7) Log fresh guard: tail -f /tmp/mihomo_fresh_guard.log"
echo "8) Log force reload: tail -f /tmp/mihomo_force_after_reload.log"
