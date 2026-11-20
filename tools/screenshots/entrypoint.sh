#!/usr/bin/env bash
# Start a virtual display, then run the given command on it.
set -euo pipefail
Xvfb :99 -screen 0 1024x768x24 -nolisten tcp >/dev/null 2>&1 &
sleep 1
exec "$@"
