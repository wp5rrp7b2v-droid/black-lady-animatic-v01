import io
import json
import traceback

from flask import Blueprint, send_file

from common import ok, fail, require_session
from config import PRODUCTION_PROCESS_BOUNDARY
from state_store import save_session, append_history, now_iso
from workflow import transition, candidate_identity, public_session
from qualification import (
    publish as qualification_publish,
    register as qualification_register,
    lock as qualification_lock,
    closeout as qualification_closeout,
    legacy_phase_e_archive,
    paths_for,
    remote_evidence,
)

bp = Blueprint("qualification_routes", __name__)


@bp.post("/api/v1/publish")
def publish():
    try:
        session = require_session()
        if session.get("status") != "PO_APPROVED_PENDING_PUBLICATION":
            return fail("当前状态不允许 qualification publication")
        result = qualification_publish(session)
        session["publication"] = {**result, "published_at": now_iso()}
        transition(session, "PUBLISHED_NOT_REGISTERED")
        append_history(
            session,
            "QUALIFICATION_PUBLICATION",
            outcome=result.get("outcome"),
            path=result.get("path"),
        )
        save_session(session)
        return ok(session=public_session(session), publication=result)
    except Exception as e:
        traceback.print_exc()
        return fail(f"{type(e).__name__}: {e}", 500)


@bp.post("/api/v1/register")
def register():
    try:
        session = require_session()
        if session.get("status") != "PUBLISHED_NOT_REGISTERED":
            return fail("当前状态不允许 Registration；必须保持 PUBLISHED_NOT_REGISTERED")
        result = qualification_register(session)
        session["registration"] = {**result, "registered_at": now_iso()}
        transition(session, "REGISTERED_PENDING_LOCK")
        append_history(
            session,
            "QUALIFICATION_REGISTRATION",
            outcome=result.get("outcome"),
            path=result.get("path"),
        )
        save_session(session)
        return ok(session=public_session(session), registration=result)
    except Exception as e:
        traceback.print_exc()
        return fail(f"{type(e).__name__}: {e}", 500)


@bp.post("/api/v1/lock")
def lock():
    try:
        session = require_session()
        if session.get("status") != "REGISTERED_PENDING_LOCK":
            return fail("当前状态不允许 LOCK")
        result = qualification_lock(session)
        session["lock"] = {
            **result,
            "locked_at": now_iso(),
            "identity": candidate_identity(session.get("candidate") or {}),
        }
        transition(session, "LOCKED_PENDING_CLOSEOUT")
        append_history(
            session,
            "QUALIFICATION_LOCK",
            outcome=result.get("outcome"),
            path=result.get("path"),
        )
        save_session(session)
        return ok(session=public_session(session), lock=result)
    except Exception as e:
        traceback.print_exc()
        return fail(f"{type(e).__name__}: {e}", 500)


@bp.post("/api/v1/closeout")
def closeout():
    try:
        session = require_session()
        if session.get("status") != "LOCKED_PENDING_CLOSEOUT":
            return fail("必须先完成 LOCK 才能 Closeout")
        result = qualification_closeout(session)
        session["closeout"] = {
            **result,
            "closed_at": now_iso(),
            "qualification_only": True,
            "formal_story_shot_written": False,
            "project_control_story_shot_write": False,
            "formal_sop_changed": False,
        }
        transition(session, "CLOSED")
        append_history(
            session,
            "QUALIFICATION_CLOSEOUT",
            outcome=result.get("outcome"),
            path=result.get("path"),
        )
        save_session(session)
        return ok(session=public_session(session), closeout=result)
    except Exception as e:
        traceback.print_exc()
        return fail(f"{type(e).__name__}: {e}", 500)


@bp.get("/api/v1/qualification/evidence")
def qualification_evidence():
    try:
        session = require_session()
        return ok(remote=remote_evidence(session["session_id"]))
    except Exception as e:
        return fail(f"{type(e).__name__}: {e}", 500)


@bp.get("/api/v1/receipt")
def receipt():
    try:
        session = require_session()
        payload = {
            "schema": "BLACK_LADY_PRODUCTION_CONSOLE_V1_1_QUALIFICATION_RECEIPT_V001",
            "production_process_boundary": PRODUCTION_PROCESS_BOUNDARY,
            "session": public_session(session),
            "qualification_paths": paths_for(session["session_id"]),
            "remote_evidence": remote_evidence(session["session_id"]),
        }
        raw = (json.dumps(payload, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        return send_file(
            io.BytesIO(raw),
            mimetype="application/json",
            as_attachment=True,
            download_name=f"{session['session_id']}_V1_1_QUALIFICATION_RECEIPT.json",
        )
    except Exception as e:
        return fail(str(e), 404)


@bp.get("/api/v1/archive/phase-e")
def phase_e_archive():
    return ok(archive=legacy_phase_e_archive())
