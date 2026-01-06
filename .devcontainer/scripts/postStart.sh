#!/usr/bin/env bash

# Wanting to edit this for yourself locally without creating a whole new docker image?
# 

set -euo pipefail

echo "Beginning postStart.sh"

# Starts supervisor (responsible for xpra/libresprite and Emulator.js Python server) if it is not already running
if supervisorctl status >/dev/null 2>&1; then
  echo "supervisord already running."
else
  echo "Starting supervisord..."
  /usr/bin/supervisord -c /etc/supervisor/supervisord.conf
fi

echo "Finished postStart.sh"
