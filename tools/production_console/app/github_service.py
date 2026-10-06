import base64
import json
import shutil
import subprocess
import urllib.parse
from pathlib import Path

from config import GITHUB_REPO


def gh_binary():
    for item in (shutil.which("gh"), "/usr/local/bin/gh", "/opt/homebrew/bin/gh"):
        if item and Path(item).exists():
            return item
    raise RuntimeError("未找到 GitHub CLI (gh)")


def run_gh_json(args, input_obj=None, timeout=45, allow_404=False):
    cmd = [gh_binary(), *args]
    input_text = json.dumps(input_obj, ensure_ascii=False) if input_obj is not None else None
    proc = subprocess.run(cmd, input=input_text, capture_output=True, text=True, timeout=timeout)
    if proc.returncode != 0:
        err = (proc.stderr or proc.stdout or "").strip()
        if allow_404 and ("HTTP 404" in err or "Not Found" in err):
            return None
        raise RuntimeError(f"gh command failed: {err[:1200]}")
    raw = (proc.stdout or "").strip()
    return json.loads(raw) if raw else {}


def branch_meta(branch):
    encoded = urllib.parse.quote(branch, safe="")
    return run_gh_json(["api", "--method", "GET", f"repos/{GITHUB_REPO}/branches/{encoded}"])


def main_meta():
    return branch_meta("main")


def get_file(branch, path):
    encoded_ref = urllib.parse.quote(branch, safe="")
    return run_gh_json(["api", "--method", "GET", f"repos/{GITHUB_REPO}/contents/{path}?ref={encoded_ref}"], allow_404=True)


def decode_content(meta):
    if not meta:
        return None
    encoded = (meta.get("content") or "").replace("\n", "")
    return base64.b64decode(encoded) if encoded else b""


def create_file(branch, path, content_bytes, message):
    body = {
        "message": message,
        "content": base64.b64encode(content_bytes).decode("ascii"),
        "branch": branch,
    }
    return run_gh_json(["api", "--method", "PUT", f"repos/{GITHUB_REPO}/contents/{path}", "--input", "-"], input_obj=body, timeout=60)


def exact_create_or_read(branch, path, desired_bytes, message):
    before = get_file(branch, path)
    if before:
        if decode_content(before) != desired_bytes:
            raise RuntimeError(f"GitHub path 已存在不同内容，拒绝覆盖: {path}")
        return {"outcome": "ALREADY_EXISTS", "github_write": 0, "commit_sha": None, "meta": before, "readback_exact": True}
    created = create_file(branch, path, desired_bytes, message)
    after = get_file(branch, path)
    exact = bool(after) and decode_content(after) == desired_bytes
    return {
        "outcome": "CREATED",
        "github_write": 1,
        "commit_sha": ((created.get("commit") or {}).get("sha")),
        "meta": after,
        "readback_exact": exact,
    }
