#!/bin/zsh
set -u
ROOT="$(cd "$(dirname "$0")" && pwd)"
PRIVATE_DIR="${BLACK_LADY_PRIVATE_DIR:-/Users/caroline/诡舍/黑衣夫人/black_lady_short_01/BlackLadyLocalConsolePrivate}"
echo "== Production Console V1.1 Diagnose =="
echo "Root: $ROOT"
echo "Private: $PRIVATE_DIR"
command -v python3 >/dev/null && python3 --version || echo "python3: MISSING"
command -v gh >/dev/null && gh --version | head -1 || echo "gh: MISSING"
[[ -x "$ROOT/.venv/bin/python" ]] && echo "venv: READY" || echo "venv: NOT INSTALLED"
[[ -f "$PRIVATE_DIR/credentials.json" ]] && echo "OAuth credentials: PRESENT" || echo "OAuth credentials: MISSING"
[[ -f "$PRIVATE_DIR/token.json" ]] && echo "OAuth token: PRESENT" || echo "OAuth token: NOT PRESENT"
if curl -fsS "http://127.0.0.1:8765/health" 2>/dev/null; then
  echo
  echo "health: PASS"
else
  echo "health: NOT RUNNING"
fi
if [[ -x "$ROOT/.venv/bin/python" ]]; then
  cd "$ROOT"
  "$ROOT/.venv/bin/python" -m unittest discover -s tests -p 'test_*.py'
fi
