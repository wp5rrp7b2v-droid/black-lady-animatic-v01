import os
from pathlib import Path

HOST = "127.0.0.1"
PORT = 8765
SCOPES = ["https://www.googleapis.com/auth/drive.file"]
GITHUB_REPO = "wp5rrp7b2v-droid/black-lady-animatic-v01"
DEFAULT_PRIVATE_DIR = "/Users/caroline/诡舍/黑衣夫人/black_lady_short_01/BlackLadyLocalConsolePrivate"
PRIVATE_DIR = Path(os.environ.get("BLACK_LADY_PRIVATE_DIR", DEFAULT_PRIVATE_DIR)).expanduser()
CREDENTIALS = PRIVATE_DIR / "credentials.json"
TOKEN = PRIVATE_DIR / "token.json"
CONFIG = PRIVATE_DIR / "config.json"
BINDING = PRIVATE_DIR / "drive_binding.json"
SESSIONS_DIR = PRIVATE_DIR / "sessions"
LOCKS_DIR = PRIVATE_DIR / "locks"
LEGACY_PHASE_E_STATE = PRIVATE_DIR / "phase_e_e2e_state.json"
FOLDER_MIME = "application/vnd.google-apps.folder"
QUALIFICATION_BRANCH = os.environ.get("BLACK_LADY_CONSOLE_TEST_BRANCH", "test/local-console-v1-1-e2e-v001")
QUALIFICATION_ROOT = "staging/local_console_v1_1"
PRODUCTION_PROCESS_BOUNDARY = "FORMAL_STORY_SHOT_WORKFLOW_UNCHANGED"
