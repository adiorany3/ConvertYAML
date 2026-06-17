#!/bin/sh
# Pull OpenClash config from GitHub with backup + rollback.
# Env file: /etc/mihomo-autopilot/github.env
set -eu

ENV_FILE="${ENV_FILE:-/etc/mihomo-autopilot/github.env}"
[ -f "$ENV_FILE" ] && . "$ENV_FILE"

GITHUB_REPO="${GITHUB_REPO:-}"
GITHUB_BRANCH="${GITHUB_BRANCH:-main}"
GITHUB_TOKEN="${GITHUB_TOKEN:-}"
CONFIG_NAME="${CONFIG_NAME:-openclash_auto.yaml}"
OPENCLASH_CONFIG_DIR="${OPENCLASH_CONFIG_DIR:-/etc/openclash/config}"
BACKUP_DIR="${BACKUP_DIR:-/etc/mihomo-autopilot/backups}"
MIHOMO_API="${MIHOMO_API:-http://127.0.0.1:9090}"
MIHOMO_SECRET="${MIHOMO_SECRET:-reyre}"
MIHOMO_BIN="${MIHOMO_BIN:-}"
RAW_BASE="${GITHUB_RAW_BASE:-}"
RESTART_OPENCLASH="${RESTART_OPENCLASH:-1}"
ROLLBACK_ON_FAIL="${ROLLBACK_ON_FAIL:-1}"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"; }
fail() { log "ERROR: $*"; exit 1; }

if [ -z "$GITHUB_REPO" ] && [ -z "$RAW_BASE" ]; then
  fail "GITHUB_REPO belum diisi di $ENV_FILE. Contoh: GITHUB_REPO='username/repo'"
fi

mkdir -p "$OPENCLASH_CONFIG_DIR" "$BACKUP_DIR"
TMP="/tmp/openclash_pull_${CONFIG_NAME}.$$"
DEST="$OPENCLASH_CONFIG_DIR/$CONFIG_NAME"
STAMP="$(date '+%Y%m%d-%H%M%S')"
BACKUP="$BACKUP_DIR/${CONFIG_NAME}.${STAMP}.bak"

if [ -n "$RAW_BASE" ]; then
  URL="$RAW_BASE/$CONFIG_NAME"
else
  URL="https://raw.githubusercontent.com/$GITHUB_REPO/$GITHUB_BRANCH/$CONFIG_NAME"
fi

log "Download config: $URL"
if command -v curl >/dev/null 2>&1; then
  if [ -n "$GITHUB_TOKEN" ]; then
    curl -fsSL -H "Authorization: Bearer $GITHUB_TOKEN" "$URL" -o "$TMP"
  else
    curl -fsSL "$URL" -o "$TMP"
  fi
elif command -v wget >/dev/null 2>&1; then
  if [ -n "$GITHUB_TOKEN" ]; then
    wget -q --header="Authorization: Bearer $GITHUB_TOKEN" -O "$TMP" "$URL"
  else
    wget -q -O "$TMP" "$URL"
  fi
else
  fail "curl/wget tidak ditemukan. Install: opkg update && opkg install curl"
fi

[ -s "$TMP" ] || fail "file hasil download kosong"
grep -q "proxy-groups:" "$TMP" || fail "validasi gagal: proxy-groups tidak ditemukan"
grep -q "proxies:" "$TMP" || fail "validasi gagal: proxies tidak ditemukan"

if [ -z "$MIHOMO_BIN" ]; then
  for b in /etc/openclash/core/clash_meta /etc/openclash/core/mihomo /usr/bin/mihomo /usr/bin/clash; do
    if [ -x "$b" ]; then MIHOMO_BIN="$b"; break; fi
  done
fi

if [ -n "$MIHOMO_BIN" ] && [ -x "$MIHOMO_BIN" ]; then
  log "Test syntax dengan $MIHOMO_BIN"
  if ! "$MIHOMO_BIN" -t -d /tmp -f "$TMP" >/tmp/openclash_pull_test.log 2>&1; then
    cat /tmp/openclash_pull_test.log || true
    fail "syntax test gagal, config tidak dipasang"
  fi
else
  log "Mihomo binary tidak ditemukan, skip syntax test core. Basic YAML check saja."
fi

if [ -f "$DEST" ]; then
  cp "$DEST" "$BACKUP"
  log "Backup config lama: $BACKUP"
fi

cp "$TMP" "$DEST"
log "Config baru dipasang ke $DEST"

api_ok() {
  if command -v curl >/dev/null 2>&1; then
    if [ -n "$MIHOMO_SECRET" ]; then
      curl -fsS -H "Authorization: Bearer $MIHOMO_SECRET" "$MIHOMO_API/proxies" >/tmp/openclash_pull_api.json 2>/tmp/openclash_pull_api.err
    else
      curl -fsS "$MIHOMO_API/proxies" >/tmp/openclash_pull_api.json 2>/tmp/openclash_pull_api.err
    fi
  else
    if [ -n "$MIHOMO_SECRET" ]; then
      wget -q --header="Authorization: Bearer $MIHOMO_SECRET" -O /tmp/openclash_pull_api.json "$MIHOMO_API/proxies" 2>/tmp/openclash_pull_api.err
    else
      wget -q -O /tmp/openclash_pull_api.json "$MIHOMO_API/proxies" 2>/tmp/openclash_pull_api.err
    fi
  fi
}

if [ "$RESTART_OPENCLASH" = "1" ]; then
  log "Restart OpenClash"
  /etc/init.d/openclash restart || true
  sleep 10
  if api_ok; then
    log "API Mihomo OK setelah update."
  else
    log "API Mihomo gagal setelah update."
    cat /tmp/openclash_pull_api.err 2>/dev/null || true
    if [ "$ROLLBACK_ON_FAIL" = "1" ] && [ -f "$BACKUP" ]; then
      log "Rollback ke backup: $BACKUP"
      cp "$BACKUP" "$DEST"
      /etc/init.d/openclash restart || true
      sleep 8
      fail "config baru gagal, sudah rollback ke config lama"
    fi
  fi
fi

rm -f "$TMP"
log "Pull config selesai."
