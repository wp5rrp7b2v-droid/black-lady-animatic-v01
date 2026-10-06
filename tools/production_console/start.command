#!/bin/zsh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
PRIVATE_DIR="${BLACK_LADY_PRIVATE_DIR:-/Users/caroline/诡舍/黑衣夫人/black_lady_short_01/BlackLadyLocalConsolePrivate}"
PID_FILE="$PRIVATE_DIR/production_console_v1_1.pid"
LOG_FILE="$PRIVATE_DIR/production_console_v1_1.log"
URL="http://127.0.0.1:8765/"
mkdir -p "$PRIVATE_DIR"
if [[ ! -x "$ROOT/.venv/bin/python" ]]; then
  echo "V1.1 virtualenv not found. Run: zsh \"$ROOT/install.command\""
  exit 1
fi
if [[ -f "$PID_FILE" ]]; then
  PID="$(cat "$PID_FILE" 2>/dev/null || true)"
  if [[ -n "$PID" ]] && kill -0 "$PID" 2>/dev/null; then
    open -a "Google Chrome" "$URL" 2>/dev/null || open "$URL"
    exit 0
  fi
  rm -f "$PID_FILE"
fi
cd "$ROOT/app"
export BLACK_LADY_PRIVATE_DIR="$PRIVATE_DIR"
nohup "$ROOT/.venv/bin/python" server.py >"$LOG_FILE" 2>&1 &
PID=$!
echo "$PID" > "$PID_FILE"
for i in {1..20}; do
  if curl -fsS "$URL/health" >/dev/null 2>&1; then
    open -a "Google Chrome" "$URL" 2>/dev/null || open "$URL"
    echo "Production Console V1.1 started: $URL"
    exit 0
  fi
  sleep 0.25
done
echo "Server did not become healthy. Log: $LOG_FILE"
exit 1
