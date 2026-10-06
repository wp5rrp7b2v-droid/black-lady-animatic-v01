#!/bin/bash
set -u
ROOT="$(cd "$(dirname "$0")" && pwd)"
PRIVATE_DEFAULT="$HOME/诡舍/黑衣夫人/black_lady_short_01/BlackLadyLocalConsolePrivate"
PRIVATE="${BLACK_LADY_PRIVATE_DIR:-$PRIVATE_DEFAULT}"
echo "=== BLACK LADY PRODUCTION CONSOLE V1.1 DIAGNOSTICS ==="
echo "Root: $ROOT"
echo "Private: $PRIVATE"
if [ -x "$ROOT/.venv/bin/python" ]; then
  "$ROOT/.venv/bin/python" --version
  "$ROOT/.venv/bin/python" - <<'PY'
mods=["flask","google.auth","google_auth_oauthlib","PIL","requests"]
for m in mods:
    try: __import__(m); print("PASS",m)
    except Exception as e: print("FAIL",m,type(e).__name__)
PY
else echo "VENV MISSING"; fi
echo "=== PRIVATE FILES (existence only) ==="
for f in credentials.json token.json drive_binding.json; do [ -f "$PRIVATE/$f" ] && echo "FOUND $f" || echo "MISS  $f"; done
echo "=== PORT 8765 ==="
lsof -nP -iTCP:8765 -sTCP:LISTEN || echo "FREE"
echo "=== GITHUB CLI ==="
gh --version 2>/dev/null | head -n1 || echo "gh MISSING"
