#!/bin/sh
DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
MIHOMO_API="${MIHOMO_API:-http://127.0.0.1:9090}" MIHOMO_SECRET="${MIHOMO_SECRET:-reyre}" \
  python3 "$DIR/mihomo_autopilot.py" --once --close-connections "$@"
