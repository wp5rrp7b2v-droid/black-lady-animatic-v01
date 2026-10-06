#!/bin/bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
PRIVATE_DEFAULT="$HOME/诡舍/黑衣夫人/black_lady_short_01/BlackLadyLocalConsolePrivate"
export BLACK_LADY_PRIVATE_DIR="${BLACK_LADY_PRIVATE_DIR:-$PRIVATE_DEFAULT}"
URL="http://127.0.0.1:8765"
cd "$ROOT/app"
if [ ! -x "$ROOT/.venv/bin/python" ]; then
  echo "Missing .venv. Run install.command first."; exit 1
fi
if curl -fsS "$URL/health" 2>/dev/null | grep -q "BLACK_LADY_PRODUCTION_CONSOLE_V1_1"; then
  open -a "Google Chrome" "$URL" 2>/dev/null || open "$URL"; exit 0
fi
"$ROOT/.venv/bin/python" server.py &
PID=$!
mkdir -p "$BLACK_LADY_PRIVATE_DIR"
echo "$PID" > "$BLACK_LADY_PRIVATE_DIR/v1_1_console.pid"
for _ in {1..40}; do
  if curl -fsS "$URL/health" 2>/dev/null | grep -q "BLACK_LADY_PRODUCTION_CONSOLE_V1_1"; then
    open -a "Google Chrome" "$URL" 2>/dev/null || open "$URL"
    wait "$PID"; exit $?
  fi
  sleep 0.5
done
echo "Console did not become healthy."; kill "$PID" 2>/dev/null || true; exit 1
