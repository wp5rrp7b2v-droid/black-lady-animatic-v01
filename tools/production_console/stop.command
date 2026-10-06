#!/bin/bash
set -euo pipefail
PRIVATE_DEFAULT="$HOME/诡舍/黑衣夫人/black_lady_short_01/BlackLadyLocalConsolePrivate"
PRIVATE="${BLACK_LADY_PRIVATE_DIR:-$PRIVATE_DEFAULT}"
PIDFILE="$PRIVATE/v1_1_console.pid"
if [ ! -f "$PIDFILE" ]; then echo "No V1.1 PID file."; exit 0; fi
PID="$(cat "$PIDFILE")"
CMD="$(ps -p "$PID" -o command= 2>/dev/null || true)"
if [[ "$CMD" == *"server.py"* ]]; then kill "$PID" 2>/dev/null || true; rm -f "$PIDFILE"; echo "Stopped Production Console V1.1."; else echo "PID is not a Console server; refusing to kill."; exit 1; fi
