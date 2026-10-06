import io
import traceback
from pathlib import Path
from flask import Blueprint, render_template, request, send_file

from common import ok, fail, require_session
from config import PRODUCTION_PROCESS_BOUNDARY
from state_store import default_session, save_session, append_history, list_sessions, now_iso, session_exists
from workflow import transition, candidate_identity, identity_complete, public_session, STAGES
from drive_service import connected as drive_connected, get_bound_folder, exact_upload, drive_download_bytes
from github_service import gh_binary
from qualification import preflight as qualification_preflight, paths_for

bp = Blueprint("session_routes", __name__)

@bp.get("/")
def index():
    return render_template("index.html")


@bp.get("/archive")
def archive_page():
    return render_template("archive.html")


@bp.get("/health")
def health():
    return ok(service="BLACK_LADY_PRODUCTION_CONSOLE_V1_1", release="V1.1_IMPLEMENTATION", production_process_boundary=PRODUCTION_PROCESS_BOUNDARY)


@bp.get("/api/v1/status")
def status():
    binding, folder_id = get_bound_folder()
    try:
        gh = gh_binary()
        github_cli = True
    except Exception:
        gh = None
        github_cli = False
    return ok(
        release="V1.1_IMPLEMENTATION",
        stages=STAGES,
        production_process_boundary=PRODUCTION_PROCESS_BOUNDARY,
        drive_connected=drive_connected(),
        drive_folder_bound=bool(folder_id),
        drive_folder_name=binding.get("folder_name") or binding.get("name"),
        github_cli=github_cli,
        github_cli_path=gh,
        sessions=list_sessions(),
    )


@bp.post("/api/v1/session/start")
def session_start():
    body = request.get_json(silent=True) or {}
    session_id = (body.get("session_id") or "").strip()
    shot_id = (body.get("shot_id") or "").strip()
    mode = (body.get("mode") or "QUALIFICATION").strip().upper()
    if mode != "QUALIFICATION":
        return fail("V1.1 当前只允许 QUALIFICATION mode；Controlled Pilot / Production 尚未授权")
    if not session_id or not shot_id:
        return fail("session_id 与 shot_id 必填", 400)
    try:
        if session_exists(session_id):
            return fail("Session ID 已存在；为避免覆盖历史，请 Load Session 或使用新的 Session ID")
        session = default_session(session_id, shot_id, mode)
        session["bundle"] = body.get("bundle") or {}
        session["design_summary"] = body.get("design_summary") or {}
        append_history(session, "SESSION_STARTED")
        save_session(session)
        return ok(session=public_session(session))
    except Exception as e:
        return fail(str(e), 400)


@bp.get("/api/v1/session")
def session_get():
    try:
        session = require_session()
        return ok(session=public_session(session), qualification_paths=paths_for(session["session_id"]))
    except Exception as e:
        return fail(str(e), 404)


@bp.post("/api/v1/design/approve")
def design_approve():
    try:
        session = require_session()
        if session.get("status") == "DESIGN_APPROVED":
            return ok(idempotent=True, session=public_session(session))
        body = request.get_json(silent=True) or {}
        if body.get("design_summary"):
            session["design_summary"] = body["design_summary"]
        if body.get("bundle"):
            session["bundle"] = body["bundle"]
        transition(session, "DESIGN_APPROVED")
        append_history(session, "DESIGN_APPROVED")
        save_session(session)
        return ok(session=public_session(session))
    except Exception as e:
        return fail(str(e))


@bp.post("/api/v1/preflight")
def preflight():
    try:
        session = require_session()
        if session.get("status") not in ("DESIGN_APPROVED", "PREFLIGHT_FAILED"):
            return fail("当前状态不允许 PREFLIGHT")
        _, folder_id = get_bound_folder()
        result = qualification_preflight(session, drive_connected(), bool(folder_id))
        session["preflight"] = {**result, "checked_at": now_iso()}
        transition(session, "PREFLIGHT_PASS" if result["pass"] else "PREFLIGHT_FAILED")
        append_history(session, "PREFLIGHT_PASS" if result["pass"] else "PREFLIGHT_FAIL", checks=result["checks"])
        if result["pass"]:
            transition(session, "AWAITING_CANDIDATE")
            append_history(session, "GENERATION_AUTHORIZED_FOR_QUALIFICATION")
        save_session(session)
        return ok(session=public_session(session), preflight=result)
    except Exception as e:
        return fail(str(e))


@bp.post("/api/v1/candidate/upload")
def candidate_upload():
    try:
        session = require_session()
        if session.get("status") != "AWAITING_CANDIDATE":
            return fail("当前状态不允许 Candidate upload")
        if session.get("candidate", {}).get("drive_file_id"):
            return fail("当前 Session 已绑定 Candidate binary；禁止覆盖")
        f = request.files.get("file")
        candidate_id = (request.form.get("candidate_id") or "CANDIDATE_01").strip()
        if not f:
            return fail("未收到 Candidate 文件", 400)
        raw = f.read()
        if not raw:
            return fail("Candidate 文件为空", 400)
        ext = Path(f.filename or "candidate.png").suffix.lower() or ".png"
        drive_name = f"{session['shot_id']}_{candidate_id}_{session['session_id']}{ext}"
        uploaded = exact_upload(drive_name, f.mimetype or "application/octet-stream", raw)
        candidate = {
            "shot_id": session["shot_id"],
            "candidate_id": candidate_id,
            **uploaded,
            "status": "CANDIDATE_VERIFIED_PENDING_PO",
            "uploaded_at": now_iso(),
        }
        if not identity_complete(candidate):
            return fail("Candidate immutable identity 不完整")
        session["candidate"] = candidate
        transition(session, "CANDIDATE_VERIFIED_PENDING_PO")
        append_history(session, "CANDIDATE_EXACT_VERIFIED", candidate_identity=candidate_identity(candidate))
        save_session(session)
        return ok(session=public_session(session), candidate=candidate)
    except Exception as e:
        traceback.print_exc()
        return fail(f"{type(e).__name__}: {e}", 500)


@bp.post("/api/v1/candidate/new")
def candidate_new():
    try:
        session = require_session()
        if session.get("status") != "REJECTED":
            return fail("只有 REJECTED 状态可以开启新 Candidate")
        old = session.get("candidate") or {}
        session.setdefault("candidate_history", []).append({
            "candidate": old,
            "approval": session.get("approval") or {},
            "archived_at": now_iso(),
        })
        session["candidate"] = {}
        session["approval"] = {}
        session["publication"] = {}
        session["registration"] = {}
        session["lock"] = {}
        # Deliberate controlled recovery back to GENERATE after an immutable rejected attempt.
        session["status"] = "AWAITING_CANDIDATE"
        session["current_stage"] = "GENERATE"
        append_history(session, "NEW_CANDIDATE_AUTHORIZED_AFTER_REJECTION", previous_candidate_id=old.get("candidate_id"))
        save_session(session)
        return ok(session=public_session(session))
    except Exception as e:
        return fail(str(e))


@bp.get("/api/v1/candidate/media")
def candidate_media():
    try:
        session = require_session()
        candidate = session.get("candidate") or {}
        file_id = candidate.get("drive_file_id")
        if not file_id:
            return fail("Candidate 尚未绑定 Drive 文件", 404)
        raw = drive_download_bytes(file_id)
        return send_file(io.BytesIO(raw), mimetype=candidate.get("mime_type") or "application/octet-stream", download_name=candidate.get("drive_file_name") or "candidate.png", max_age=0)
    except Exception as e:
        return fail(f"{type(e).__name__}: {e}", 500)


@bp.post("/api/v1/candidate/review")
def candidate_review():
    try:
        session = require_session()
        if session.get("status") not in ("CANDIDATE_VERIFIED_PENDING_PO", "REJECTED", "PO_APPROVED_PENDING_PUBLICATION"):
            return fail("当前状态不允许 Candidate review")
        body = request.get_json(silent=True) or {}
        action = (body.get("action") or "").strip().lower()
        reason = (body.get("reason") or "").strip()
        candidate = session.get("candidate") or {}
        if not identity_complete(candidate) or not candidate.get("exact_binary_pass"):
            return fail("Candidate 尚未完成 exact-binary 验证")
        existing = session.get("approval") or {}
        if existing.get("action"):
            expected = "approve" if session.get("status") == "PO_APPROVED_PENDING_PUBLICATION" else "reject"
            if action == expected:
                return ok(idempotent=True, session=public_session(session))
            return fail("Candidate 已有不可变 PO 决策，禁止改写")
        if action not in ("approve", "reject"):
            return fail("action 必须是 approve 或 reject", 400)
        binding = {
            "candidate_id": candidate.get("candidate_id"),
            "drive_file_id": candidate.get("drive_file_id"),
            "sha256": candidate.get("sha256"),
        }
        session["approval"] = {"action": action, "reason": reason, "binding": binding, "decided_at": now_iso()}
        if action == "approve":
            transition(session, "PO_APPROVED_PENDING_PUBLICATION")
            candidate["status"] = "PO_APPROVED_PENDING_PUBLICATION"
            append_history(session, "PO_APPROVE", binding=binding)
        else:
            transition(session, "REJECTED")
            candidate["status"] = "REJECTED"
            append_history(session, "PO_REJECT", binding=binding, reason=reason)
        session["candidate"] = candidate
        save_session(session)
        return ok(session=public_session(session))
    except Exception as e:
        return fail(str(e))


