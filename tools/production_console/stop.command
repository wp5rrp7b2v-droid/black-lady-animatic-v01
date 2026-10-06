#!/bin/zsh
set -euo pipefail
PRIVATE_DIR="${BLACK_LADY_PRIVATE_DIR:-/Users/caroline/诡舍/黑衣夫人/black_lady_short_01/BlackLadyLocalConsolePrivate}"
PID_FILE="$PRIVATE_DIR/production_console_v1_1.pid"
if [[ ! -f "$PID_FILE" ]]; then
  echo "Production Console V1.1 is not recorded as running."
  exit 0
fi
PID="$(cat "$PID_FILE" 2>/dev/null || true)"
if [[ -n "$PID" ]] && kill -0 "$PID" 2>/dev/null; then
  kill "$PID"
  for i in {1..20}; do
    if ! kill -0 "$PID" 2>/dev/null; then break; fi
    sleep 0.1
  done
fi
rm -f "$PID_FILE"
echo "Production Console V1.1 stopped."
