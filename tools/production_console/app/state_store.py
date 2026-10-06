import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

from config import SESSIONS_DIR


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_json(path: Path, default=None):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {} if default is None else default


def write_json(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    try:
        os.chmod(path, 0o600)
    except Exception:
        pass


def safe_session_id(value: str) -> str:
    value = (value or "").strip()
    if not value or any(ch not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_" for ch in value):
        raise ValueError("session_id 仅允许字母、数字、-、_")
    return value


def session_path(session_id: str) -> Path:
    return SESSIONS_DIR / f"{safe_session_id(session_id)}.json"


def default_session(session_id: str, shot_id: str, mode: str = "QUALIFICATION") -> Dict[str, Any]:
    t = now_iso()
    return {
        "schema": "BLACK_LADY_PRODUCTION_CONSOLE_SESSION_V1_1",
        "session_id": safe_session_id(session_id),
        "shot_id": (shot_id or "").strip(),
        "mode": mode,
        "current_stage": "DESIGN",
        "status": "DESIGN_PENDING",
        "design_summary": {},
        "bundle": {},
        "preflight": {},
        "candidate": {},
        "approval": {},
        "publication": {},
        "registration": {},
        "lock": {},
        "closeout": {},
        "history": [],
        "created_at": t,
        "updated_at": t,
    }


def session_exists(session_id: str) -> bool:
    return session_path(session_id).exists()


def load_session(session_id: str) -> Dict[str, Any]:
    path = session_path(session_id)
    data = read_json(path, {})
    if not data:
        raise FileNotFoundError(f"Session 不存在: {session_id}")
    return data


def save_session(session: Dict[str, Any]) -> None:
    session["updated_at"] = now_iso()
    write_json(session_path(session["session_id"]), session)


def append_history(session: Dict[str, Any], action: str, **extra) -> None:
    row = {"at": now_iso(), "action": action, "status": session.get("status")}
    row.update(extra)
    session.setdefault("history", []).append(row)


def list_sessions():
    SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    for path in sorted(SESSIONS_DIR.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True):
        data = read_json(path, {})
        if data:
            rows.append({
                "session_id": data.get("session_id"),
                "shot_id": data.get("shot_id"),
                "mode": data.get("mode"),
                "status": data.get("status"),
                "updated_at": data.get("updated_at"),
            })
    return rows
