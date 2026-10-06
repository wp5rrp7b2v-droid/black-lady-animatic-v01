from flask import jsonify, request
from state_store import load_session


def ok(**kwargs):
    return jsonify({"ok": True, **kwargs})


def fail(message, code=409, **kwargs):
    return jsonify({"ok": False, "error": message, **kwargs}), code


def require_session():
    session_id = (request.args.get("session_id") or request.form.get("session_id") or (request.get_json(silent=True) or {}).get("session_id") or "").strip()
    if not session_id:
        raise ValueError("缺少 session_id")
    return load_session(session_id)
