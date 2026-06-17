#!/bin/sh
# Restore latest OpenClash config backup made by openwrt_pull_config.sh
set -eu
ENV_FILE="${ENV_FILE:-/etc/mihomo-autopilot/github.env}"
[ -f "$ENV_FILE" ] && . "$ENV_FILE"
CONFIG_NAME="${CONFIG_NAME:-openclash_auto.yaml}"
OPENCLASH_CONFIG_DIR="${OPENCLASH_CONFIG_DIR:-/etc/openclash/config}"
BACKUP_DIR="${BACKUP_DIR:-/etc/mihomo-autopilot/backups}"
DEST="$OPENCLASH_CONFIG_DIR/$CONFIG_NAME"

LATEST="$(ls -1t "$BACKUP_DIR"/${CONFIG_NAME}.*.bak 2>/dev/null | head -n 1 || true)"
if [ -z "$LATEST" ]; then
  echo "Tidak ada backup untuk $CONFIG_NAME di $BACKUP_DIR"
  exit 1
fi
cp "$LATEST" "$DEST"
echo "Rollback: $LATEST -> $DEST"
/etc/init.d/openclash restart || true
