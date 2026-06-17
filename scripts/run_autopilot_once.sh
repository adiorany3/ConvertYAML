#!/bin/sh
DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
python3 "$DIR/mihomo_autopilot.py" --once --close-connections "$@"
