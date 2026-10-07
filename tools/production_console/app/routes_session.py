import io
import json
import traceback
from pathlib import Path

from flask import Blueprint, render_template, request, send_file

from common import ok, fail, require_session
from config import PRODUCTION_PROCESS_BOUNDARY
from state_store import default_session, save_session, append_history, list_sessions, now_iso, session_exists, load_session, acquire_candidate_lock, release_candidate_lock
from workflow import transition, candidate_identity, identity_complete, public_session, STAGES, stage_for
from drive_service import (
    connected as drive_connected,
    get_bound_folder,
    exact_upload,
    drive_download_bytes,
    image_meta,
    sha256,
)
from github_service import gh_binary, main_meta
from qualification import preflight as qualification_preflight, paths_for, remote_evidence
from project_resolver import resolve_project_design_package

bp = Blueprint("session_routes", __name__)


@bp.get("/")
def index():
    return render_template("index.html")


@bp.get("/archive")
def archive_page():
    return render_template("archive.html")


@bp.get("/health")
def health():
    return ok(
        service="BLACK_LADY_PRODUCTION_CONSOLE_V1_1",
        release="V1.1_IMPLEMENTATION",
        production_process_boundary=PRODUCTION_PROCESS_BOUNDARY,
    )


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
        github_main_sha=(((main_meta().get("commit") or {}).get("sha")) if github_cli else None),
        sessions=list_sessions(),
    )


@bp.get("/api/v1/design-package/resolve")
def design_package_resolve():
    try:
        shot_id = (request.args.get("shot_id") or "").strip() or None
        resolved = resolve_project_design_package(shot_id=shot_id)
        return ok(resolved=resolved)
    except Exception as e:
        return fail(str(e), 404)


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
        return ok(
            session=public_session(session),
            qualification_paths=paths_for(session["session_id"]),
        )
    except Exception as e:
        return fail(str(e), 404)



def _verified_remote_recovery(session_id: str):
    evidence = remote_evidence(session_id)
    highest = evidence.get("highest_remote_status")
    if not highest:
        raise RuntimeError("无法恢复：该 Session 尚未建立 GitHub qualification evidence。请先完成 Publication，或确认 Session ID。")

    records = evidence["records"]
    pub_payload = records["publication"].get("payload") or {}
    reg_payload = records["registration"].get("payload") or {}
    lock_payload = records["lock"].get("payload") or {}
    closeout_payload = records["closeout"].get("payload") or {}

    identities = [
        x for x in (
            pub_payload.get("candidate"),
            reg_payload.get("candidate_identity"),
            lock_payload.get("immutable_identity"),
            closeout_payload.get("immutable_identity"),
        ) if x
    ]
    if not identities:
        raise RuntimeError("Remote qualification evidence 缺少 Candidate identity")

    base = identities[0]
    identity_fields = ("shot_id", "candidate_id", "drive_file_id", "sha256", "byte_size", "width", "height")
    for other in identities[1:]:
        if any(other.get(k) != base.get(k) for k in identity_fields):
            raise RuntimeError("Remote qualification identity drift detected")

    file_id = base.get("drive_file_id")
    if not file_id:
        raise RuntimeError("Remote identity 缺少 Drive File ID")
    raw = drive_download_bytes(file_id)
    meta = image_meta(raw)
    drive_checks = {
        "sha256_match": sha256(raw) == base.get("sha256"),
        "byte_size_match": len(raw) == base.get("byte_size"),
        "dimensions_match": (meta["width"], meta["height"]) == (base.get("width"), base.get("height")),
        "png_format": meta.get("format") == "PNG",
    }
    if not all(drive_checks.values()):
        raise RuntimeError(f"Drive authoritative readback 与 remote identity 不一致: {drive_checks}")

    shot_id = base.get("shot_id") or pub_payload.get("shot_id")
    if not shot_id:
        raise RuntimeError("Remote evidence 缺少 shot_id")

    session = default_session(session_id, shot_id, "QUALIFICATION")
    session["bundle"] = pub_payload.get("bundle") or {}
    recovery_snapshot = pub_payload.get("recovery_snapshot") or {}
    if recovery_snapshot:
        session["design_summary"] = recovery_snapshot.get("design_summary")
        session["preflight"] = recovery_snapshot.get("preflight") or {}
        session["recovery_fidelity"] = "FULL"
    else:
        session["design_summary"] = "Not recoverable from legacy remote evidence."
        session["preflight"] = {
            "pass": None,
            "recovered": True,
            "evidence_status": "NOT_AVAILABLE_FROM_LEGACY_REMOTE_EVIDENCE",
        }
        session["recovery_fidelity"] = "PARTIAL_LEGACY_EVIDENCE"
    session["candidate"] = {
        **base,
        "mime_type": base.get("mime_type") or "image/png",
        "exact_binary_pass": True,
        "exact_binary_checks": drive_checks,
        "status": highest,
        "recovered_from_external": True,
    }
    approval_binding = pub_payload.get("approval_binding") or {}
    if approval_binding:
        expected = {
            "candidate_id": base.get("candidate_id"),
            "drive_file_id": base.get("drive_file_id"),
            "sha256": base.get("sha256"),
        }
        if any(approval_binding.get(k) != v for k, v in expected.items()):
            raise RuntimeError("Remote approval binding 与 Candidate identity 不一致")
        session["approval"] = {
            "action": "approve",
            "binding": approval_binding,
            "recovered_from_external": True,
        }

    for key in ("publication", "registration", "lock", "closeout"):
        record = records[key]
        if record.get("exists"):
            session[key] = {
                "path": record.get("path"),
                "remote_blob_sha": record.get("blob_sha"),
                "remote_payload": record.get("payload"),
                "recovered_from_external": True,
            }

    session["status"] = highest
    session["current_stage"] = stage_for(highest)
    append_history(
        session,
        "SESSION_RECOVERED_FROM_EXTERNAL_EVIDENCE",
        remote_status=highest,
        drive_checks=drive_checks,
    )
    return session, evidence, drive_checks


@bp.post("/api/v1/session/recover")
def session_recover():
    try:
        body = request.get_json(silent=True) or {}
        session_id = (body.get("session_id") or "").strip()
        if not session_id:
            return fail("缺少 session_id", 400)
        if session_exists(session_id):
            return fail("本地 Session 仍存在；请使用 Load / Reconcile，而不是 External Recovery")
        session, evidence, drive_checks = _verified_remote_recovery(session_id)
        save_session(session)
        return ok(
            recovered=True,
            session=public_session(session),
            remote=evidence,
            drive_checks=drive_checks,
        )
    except Exception as e:
        traceback.print_exc()
        return fail(f"{type(e).__name__}: {e}", 500)


@bp.post("/api/v1/session/reconcile")
def session_reconcile():
    try:
        session = require_session()
        before_status = session.get("status")
        before_identity = candidate_identity(session.get("candidate") or {})
        evidence = remote_evidence(session["session_id"])
        highest = evidence.get("highest_remote_status")
        if not highest:
            return ok(
                changed=False,
                reason="NO_REMOTE_QUALIFICATION_EVIDENCE",
                session=public_session(session),
                remote=evidence,
            )

        identities = []
        records = evidence["records"]
        pub_payload = (records["publication"].get("payload") or {})
        reg_payload = (records["registration"].get("payload") or {})
        lock_payload = (records["lock"].get("payload") or {})
        closeout_payload = (records["closeout"].get("payload") or {})

        for identity in (
            pub_payload.get("candidate"),
            reg_payload.get("candidate_identity"),
            lock_payload.get("immutable_identity"),
            closeout_payload.get("immutable_identity"),
        ):
            if identity:
                identities.append(identity)

        if not identities:
            return fail("Remote qualification evidence 缺少 Candidate identity")

        base = identities[0]
        identity_fields = ("shot_id", "candidate_id", "drive_file_id", "sha256", "byte_size", "width", "height")
        for other in identities[1:]:
            if any(other.get(k) != base.get(k) for k in identity_fields):
                return fail("Remote qualification identity drift detected")

        if base.get("shot_id") != session.get("shot_id"):
            return fail("Remote shot_id 与当前 Session 不一致")

        file_id = base.get("drive_file_id")
        if not file_id:
            return fail("Remote identity 缺少 Drive File ID")
        raw = drive_download_bytes(file_id)
        meta = image_meta(raw)
        drive_checks = {
            "sha256_match": sha256(raw) == base.get("sha256"),
            "byte_size_match": len(raw) == base.get("byte_size"),
            "dimensions_match": (meta["width"], meta["height"]) == (base.get("width"), base.get("height")),
            "png_format": meta.get("format") == "PNG",
        }
        if not all(drive_checks.values()):
            return fail("Drive authoritative readback 与 remote identity 不一致", drive_checks=drive_checks)

        session["candidate"] = {
            **(session.get("candidate") or {}),
            **base,
            "mime_type": base.get("mime_type") or "image/png",
            "exact_binary_pass": True,
            "exact_binary_checks": drive_checks,
            "status": highest,
        }

        approval_binding = pub_payload.get("approval_binding") or {}
        if approval_binding:
            expected = {
                "candidate_id": base.get("candidate_id"),
                "drive_file_id": base.get("drive_file_id"),
                "sha256": base.get("sha256"),
            }
            if any(approval_binding.get(k) != v for k, v in expected.items()):
                return fail("Remote approval binding 与 Candidate identity 不一致")
            session["approval"] = {
                **(session.get("approval") or {}),
                "action": "approve",
                "binding": approval_binding,
                "reconciled_from_remote": True,
            }

        for key in ("publication", "registration", "lock", "closeout"):
            record = records[key]
            if record.get("exists"):
                session[key] = {
                    **(session.get(key) or {}),
                    "path": record.get("path"),
                    "remote_blob_sha": record.get("blob_sha"),
                    "remote_payload": record.get("payload"),
                    "reconciled_from_remote": True,
                }

        session["status"] = highest
        session["current_stage"] = stage_for(highest)
        after_identity = candidate_identity(session.get("candidate") or {})
        changed = before_status != highest or before_identity != after_identity
        if changed:
            append_history(
                session,
                "EXTERNAL_EVIDENCE_RECONCILED",
                remote_status=highest,
                drive_checks=drive_checks,
            )
        save_session(session)
        return ok(
            changed=changed,
            verified=True,
            session=public_session(session),
            remote=evidence,
            drive_checks=drive_checks,
        )
    except Exception as e:
        traceback.print_exc()
        return fail(f"{type(e).__name__}: {e}", 500)


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
        binding, folder_id = get_bound_folder()
        folder_name = binding.get("folder_name") or binding.get("name")
        result = qualification_preflight(session, drive_connected(), bool(folder_id), folder_name)
        session["preflight"] = {**result, "checked_at": now_iso()}
        transition(session, "PREFLIGHT_PASS" if result["pass"] else "PREFLIGHT_FAILED")
        append_history(
            session,
            "PREFLIGHT_PASS" if result["pass"] else "PREFLIGHT_FAIL",
            checks=result["checks"],
        )
        if result["pass"]:
            transition(session, "AWAITING_CANDIDATE")
            append_history(session, "GENERATION_AUTHORIZED_FOR_QUALIFICATION")
        save_session(session)
        return ok(session=public_session(session), preflight=result)
    except Exception as e:
        return fail(str(e))


@bp.get("/api/v1/work-handoff")
def work_handoff():
    try:
        session = require_session()
        if session.get("status") not in (
            "AWAITING_CANDIDATE",
            "CANDIDATE_VERIFIED_PENDING_PO",
            "REJECTED",
        ):
            return fail("Work Handoff 仅在 GENERATE / REVIEW qualification 阶段可导出")
        candidate_id = (request.args.get("candidate_id") or "CANDIDATE_01").strip()
        payload = {
            "schema": "BLACK_LADY_PRODUCTION_CONSOLE_V1_1_WORK_HANDOFF_V001",
            "qualification_only": True,
            "session_id": session["session_id"],
            "shot_id": session["shot_id"],
            "candidate_id": candidate_id,
            "mode": session["mode"],
            "design_summary": session.get("design_summary") or {},
            "bundle": session.get("bundle") or {},
            "execution_rules": {
                "output": "EXACTLY_1_PNG",
                "stop_after_one_candidate": True,
                "formal_story_shot_publication": False,
                "formal_project_control_write": False,
                "production_process_change": False,
            },
            "production_process_boundary": PRODUCTION_PROCESS_BOUNDARY,
        }
        raw = (json.dumps(payload, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        return send_file(
            io.BytesIO(raw),
            mimetype="application/json",
            as_attachment=True,
            download_name=f"{session['session_id']}_{candidate_id}_WORK_HANDOFF.json",
        )
    except Exception as e:
        return fail(str(e), 404)


@bp.post("/api/v1/candidate/upload")
def candidate_upload():
    lock_path = None
    try:
        session = require_session()
        f = request.files.get("file")
        candidate_id = (request.form.get("candidate_id") or "CANDIDATE_01").strip()
        if not f:
            return fail("未收到 Candidate 文件", 400)

        lock_path = acquire_candidate_lock(session["session_id"], candidate_id)
        session = load_session(session["session_id"])

        existing = session.get("candidate") or {}
        if existing.get("drive_file_id"):
            if existing.get("candidate_id") == candidate_id:
                return ok(idempotent=True, session=public_session(session), candidate=existing)
            return fail("当前 Session 已绑定其他 Candidate binary；禁止覆盖")
        if session.get("status") != "AWAITING_CANDIDATE":
            return fail("当前状态不允许 Candidate upload")
        raw = f.read()
        if not raw:
            return fail("Candidate 文件为空", 400)
        if len(raw) > 50 * 1024 * 1024:
            return fail("Candidate 测试限制为 50 MB 以下", 400)

        ext = Path(f.filename or "candidate.png").suffix.lower()
        if ext != ".png":
            return fail("Candidate 必须是原始 PNG；不接受 JPG / WebP / screenshot substitution", 400)
        local_meta = image_meta(raw)
        if local_meta.get("format") != "PNG":
            return fail("文件扩展名为 PNG，但实际内容不是 PNG", 400)

        drive_name = f"{session['shot_id']}_{candidate_id}_{session['session_id']}.png"
        uploaded = exact_upload(drive_name, "image/png", raw)
        candidate = {
            "shot_id": session["shot_id"],
            "candidate_id": candidate_id,
            **uploaded,
            "mime_type": "image/png",
            "status": "CANDIDATE_VERIFIED_PENDING_PO",
            "uploaded_at": now_iso(),
        }
        if not identity_complete(candidate):
            return fail("Candidate immutable identity 不完整")
        session["candidate"] = candidate
        transition(session, "CANDIDATE_VERIFIED_PENDING_PO")
        append_history(
            session,
            "CANDIDATE_EXACT_VERIFIED",
            candidate_identity=candidate_identity(candidate),
        )
        save_session(session)
        return ok(session=public_session(session), candidate=candidate)
    except Exception as e:
        traceback.print_exc()
        return fail(f"{type(e).__name__}: {e}", 500)
    finally:
        if lock_path is not None:
            release_candidate_lock(lock_path)


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
        session["closeout"] = {}
        session["status"] = "AWAITING_CANDIDATE"
        session["current_stage"] = "GENERATE"
        append_history(
            session,
            "NEW_CANDIDATE_AUTHORIZED_AFTER_REJECTION",
            previous_candidate_id=old.get("candidate_id"),
        )
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
        return send_file(
            io.BytesIO(raw),
            mimetype="image/png",
            download_name=candidate.get("drive_file_name") or "candidate.png",
            max_age=0,
        )
    except Exception as e:
        return fail(f"{type(e).__name__}: {e}", 500)


@bp.post("/api/v1/candidate/review")
def candidate_review():
    try:
        session = require_session()
        if session.get("status") not in (
            "CANDIDATE_VERIFIED_PENDING_PO",
            "REJECTED",
            "PO_APPROVED_PENDING_PUBLICATION",
        ):
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
        session["approval"] = {
            "action": action,
            "reason": reason,
            "binding": binding,
            "decided_at": now_iso(),
        }
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
