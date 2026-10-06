import json

from config import GITHUB_REPO, QUALIFICATION_BRANCH, QUALIFICATION_ROOT, LEGACY_PHASE_E_STATE
from github_service import branch_meta, main_meta, get_file, decode_content, exact_create_or_read
from state_store import read_json
from workflow import candidate_identity, binding_matches


def paths_for(session_id: str):
    root = f"{QUALIFICATION_ROOT}/{session_id}"
    return {
        "publication": f"{root}/publication.json",
        "registration": f"{root}/registration.json",
        "lock": f"{root}/lock.json",
        "closeout": f"{root}/closeout.json",
    }


def deterministic_bytes(payload):
    return (json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def _json_from_meta(meta):
    if not meta:
        return None
    raw = decode_content(meta)
    return json.loads((raw or b"{}").decode("utf-8"))


def publication_payload(session):
    candidate = session.get("candidate") or {}
    approval = session.get("approval") or {}
    paths = paths_for(session["session_id"])
    payload = {
        "schema": "BLACK_LADY_PRODUCTION_CONSOLE_V1_1_QUALIFICATION_PUBLICATION_V001",
        "qualification_only": True,
        "session_id": session["session_id"],
        "shot_id": session.get("shot_id"),
        "bundle": session.get("bundle") or {},
        "recovery_snapshot": {
            "design_summary": session.get("design_summary"),
            "preflight": session.get("preflight") or {},
        },
        "candidate": candidate_identity(candidate),
        "approval_binding": approval.get("binding") or {},
        "github_target": {"repo": GITHUB_REPO, "branch": QUALIFICATION_BRANCH, "path": paths["publication"]},
        "safety": {
            "formal_story_shot": False,
            "main_branch_write": False,
            "project_control_write": False,
            "formal_sop_change": False,
        },
    }
    return deterministic_bytes(payload), payload


def registration_payload(session, publication_meta):
    paths = paths_for(session["session_id"])
    payload = {
        "schema": "BLACK_LADY_PRODUCTION_CONSOLE_V1_1_QUALIFICATION_REGISTRATION_V001",
        "qualification_only": True,
        "session_id": session["session_id"],
        "shot_id": session.get("shot_id"),
        "candidate_identity": candidate_identity(session.get("candidate") or {}),
        "publication_binding": {"path": paths["publication"], "blob_sha": (publication_meta or {}).get("sha")},
        "github_target": {"repo": GITHUB_REPO, "branch": QUALIFICATION_BRANCH, "path": paths["registration"]},
        "safety": {
            "formal_story_shot": False,
            "main_branch_write": False,
            "project_control_write": False,
            "formal_sop_change": False,
        },
    }
    return deterministic_bytes(payload), payload


def lock_payload(session, publication_meta, registration_meta):
    paths = paths_for(session["session_id"])
    payload = {
        "schema": "BLACK_LADY_PRODUCTION_CONSOLE_V1_1_QUALIFICATION_LOCK_V001",
        "qualification_only": True,
        "session_id": session["session_id"],
        "shot_id": session.get("shot_id"),
        "lock_status": "QUALIFICATION_LOCKED",
        "immutable_identity": candidate_identity(session.get("candidate") or {}),
        "publication_binding": {"path": paths["publication"], "blob_sha": (publication_meta or {}).get("sha")},
        "registration_binding": {"path": paths["registration"], "blob_sha": (registration_meta or {}).get("sha")},
        "github_target": {"repo": GITHUB_REPO, "branch": QUALIFICATION_BRANCH, "path": paths["lock"]},
        "safety": {
            "formal_story_shot": False,
            "main_branch_write": False,
            "project_control_write": False,
            "formal_sop_change": False,
        },
    }
    return deterministic_bytes(payload), payload


def closeout_payload(session, lock_meta):
    paths = paths_for(session["session_id"])
    payload = {
        "schema": "BLACK_LADY_PRODUCTION_CONSOLE_V1_1_QUALIFICATION_CLOSEOUT_V001",
        "qualification_only": True,
        "session_id": session["session_id"],
        "shot_id": session.get("shot_id"),
        "closeout_status": "QUALIFICATION_CLOSED",
        "immutable_identity": candidate_identity(session.get("candidate") or {}),
        "lock_binding": {"path": paths["lock"], "blob_sha": (lock_meta or {}).get("sha")},
        "github_target": {"repo": GITHUB_REPO, "branch": QUALIFICATION_BRANCH, "path": paths["closeout"]},
        "safety": {
            "formal_story_shot": False,
            "main_branch_write": False,
            "project_control_write": False,
            "formal_sop_change": False,
        },
    }
    return deterministic_bytes(payload), payload


def remote_evidence(session_id: str):
    paths = paths_for(session_id)
    records = {}
    for key, path in paths.items():
        meta = get_file(QUALIFICATION_BRANCH, path)
        records[key] = {
            "exists": bool(meta),
            "path": path,
            "blob_sha": (meta or {}).get("sha"),
            "payload": _json_from_meta(meta) if meta else None,
        }

    if records["registration"]["exists"] and not records["publication"]["exists"]:
        raise RuntimeError("Remote evidence invalid: registration exists without publication")
    if records["lock"]["exists"] and not records["registration"]["exists"]:
        raise RuntimeError("Remote evidence invalid: lock exists without registration")
    if records["closeout"]["exists"] and not records["lock"]["exists"]:
        raise RuntimeError("Remote evidence invalid: closeout exists without lock")

    if records["closeout"]["exists"]:
        highest = "CLOSED"
    elif records["lock"]["exists"]:
        highest = "LOCKED_PENDING_CLOSEOUT"
    elif records["registration"]["exists"]:
        highest = "REGISTERED_PENDING_LOCK"
    elif records["publication"]["exists"]:
        highest = "PUBLISHED_NOT_REGISTERED"
    else:
        highest = None

    return {
        "repo": GITHUB_REPO,
        "branch": QUALIFICATION_BRANCH,
        "records": records,
        "highest_remote_status": highest,
    }


def preflight(session, drive_connected: bool, drive_folder_bound: bool):
    bundle = session.get("bundle") or {}
    paths = paths_for(session["session_id"])
    checks = {
        "session_identity": bool(session.get("session_id") and session.get("shot_id")),
        "design_approved": session.get("status") in ("DESIGN_APPROVED", "PREFLIGHT_FAILED"),
        "bundle_id": bool(bundle.get("bundle_id")),
        "run_id": bundle.get("run_id") not in (None, ""),
        "artifact_id": bundle.get("artifact_id") not in (None, ""),
        "artifact_digest": bool(bundle.get("artifact_digest")),
        "reference_count": isinstance(bundle.get("reference_count"), int) and bundle.get("reference_count") > 0,
        "references_exact": bundle.get("references_exact") is True,
        "delivery_manifest_verified": bundle.get("delivery_manifest_verified") is True,
        "generation_allowed": bundle.get("generation_allowed") is True,
        "drive_connected": bool(drive_connected),
        "drive_folder_bound": bool(drive_folder_bound),
        "no_locked_candidate": not bool((session.get("lock") or {}).get("locked_at")),
    }
    external = {}
    try:
        b = branch_meta(QUALIFICATION_BRANCH)
        m = main_meta()
        remote_paths_clear = all(not get_file(QUALIFICATION_BRANCH, p) for p in paths.values())
        external = {
            "github_ok": True,
            "qualification_branch": QUALIFICATION_BRANCH,
            "qualification_branch_head": ((b.get("commit") or {}).get("sha")),
            "main_head": ((m.get("commit") or {}).get("sha")),
            "qualification_paths_clear": remote_paths_clear,
        }
        checks["github_qualification_branch_available"] = True
        checks["qualification_paths_clear"] = remote_paths_clear
    except Exception as e:
        external = {"github_ok": False, "error": f"{type(e).__name__}: {e}"}
        checks["github_qualification_branch_available"] = False
        checks["qualification_paths_clear"] = False
    return {"pass": all(checks.values()), "checks": checks, "external": external}


def publish(session):
    candidate = session.get("candidate") or {}
    approval = session.get("approval") or {}
    if not binding_matches(candidate, approval.get("binding") or {}):
        raise RuntimeError("PO approval binding 与 Candidate identity 不一致")
    desired, _ = publication_payload(session)
    path = paths_for(session["session_id"])["publication"]
    main_before = ((main_meta().get("commit") or {}).get("sha"))
    result = exact_create_or_read(
        QUALIFICATION_BRANCH,
        path,
        desired,
        "test(production-console): V1.1 qualification publication",
    )
    main_after = ((main_meta().get("commit") or {}).get("sha"))
    if not result["readback_exact"]:
        raise RuntimeError("Publication readback FAIL")
    if main_before != main_after:
        raise RuntimeError("Safety FAIL: main changed during qualification publication")
    result.update({
        "path": path,
        "remote_blob_sha": (result.get("meta") or {}).get("sha"),
        "main_before": main_before,
        "main_after": main_after,
    })
    return result


def register(session):
    paths = paths_for(session["session_id"])
    pub_meta = get_file(QUALIFICATION_BRANCH, paths["publication"])
    desired_pub, _ = publication_payload(session)
    if not pub_meta or decode_content(pub_meta) != desired_pub:
        raise RuntimeError("Publication readback 不一致，禁止 Registration")
    desired, _ = registration_payload(session, pub_meta)
    publication_blob_before = pub_meta.get("sha")
    main_before = ((main_meta().get("commit") or {}).get("sha"))
    result = exact_create_or_read(
        QUALIFICATION_BRANCH,
        paths["registration"],
        desired,
        "test(production-console): V1.1 qualification registration",
    )
    pub_after = get_file(QUALIFICATION_BRANCH, paths["publication"])
    main_after = ((main_meta().get("commit") or {}).get("sha"))
    if not result["readback_exact"]:
        raise RuntimeError("Registration readback FAIL")
    if publication_blob_before != (pub_after or {}).get("sha"):
        raise RuntimeError("Recovery FAIL: publication 被改写")
    if main_before != main_after:
        raise RuntimeError("Safety FAIL: main changed during qualification registration")
    result.update({
        "path": paths["registration"],
        "remote_blob_sha": (result.get("meta") or {}).get("sha"),
        "publication_blob_before": publication_blob_before,
        "publication_blob_after": (pub_after or {}).get("sha"),
        "main_before": main_before,
        "main_after": main_after,
    })
    return result


def lock(session):
    paths = paths_for(session["session_id"])
    pub = get_file(QUALIFICATION_BRANCH, paths["publication"])
    reg = get_file(QUALIFICATION_BRANCH, paths["registration"])
    desired_pub, _ = publication_payload(session)
    desired_reg, _ = registration_payload(session, pub or {})
    if not pub or decode_content(pub) != desired_pub:
        raise RuntimeError("Publication readback FAIL")
    if not reg or decode_content(reg) != desired_reg:
        raise RuntimeError("Registration readback FAIL")
    desired, _ = lock_payload(session, pub, reg)
    main_before = ((main_meta().get("commit") or {}).get("sha"))
    result = exact_create_or_read(
        QUALIFICATION_BRANCH,
        paths["lock"],
        desired,
        "test(production-console): V1.1 qualification lock",
    )
    main_after = ((main_meta().get("commit") or {}).get("sha"))
    if not result["readback_exact"]:
        raise RuntimeError("Lock readback FAIL")
    if main_before != main_after:
        raise RuntimeError("Safety FAIL: main changed during qualification lock")
    result.update({
        "path": paths["lock"],
        "remote_blob_sha": (result.get("meta") or {}).get("sha"),
        "main_before": main_before,
        "main_after": main_after,
    })
    return result


def closeout(session):
    paths = paths_for(session["session_id"])
    lock_meta = get_file(QUALIFICATION_BRANCH, paths["lock"])
    pub_meta = get_file(QUALIFICATION_BRANCH, paths["publication"])
    reg_meta = get_file(QUALIFICATION_BRANCH, paths["registration"])
    if not (pub_meta and reg_meta and lock_meta):
        raise RuntimeError("Closeout 前 remote publication / registration / lock 必须全部存在")

    desired_lock, _ = lock_payload(session, pub_meta, reg_meta)
    if decode_content(lock_meta) != desired_lock:
        raise RuntimeError("Lock readback FAIL，禁止 Closeout")

    desired, _ = closeout_payload(session, lock_meta)
    main_before = ((main_meta().get("commit") or {}).get("sha"))
    result = exact_create_or_read(
        QUALIFICATION_BRANCH,
        paths["closeout"],
        desired,
        "test(production-console): V1.1 qualification closeout",
    )
    main_after = ((main_meta().get("commit") or {}).get("sha"))
    if not result["readback_exact"]:
        raise RuntimeError("Closeout readback FAIL")
    if main_before != main_after:
        raise RuntimeError("Safety FAIL: main changed during qualification closeout")
    result.update({
        "path": paths["closeout"],
        "remote_blob_sha": (result.get("meta") or {}).get("sha"),
        "main_before": main_before,
        "main_after": main_after,
    })
    return result


def legacy_phase_e_archive():
    local = read_json(LEGACY_PHASE_E_STATE, {})
    branch = "test/local-console-phase-e-e2e-v001"
    root = "staging/local_console_tests/TEST_SHOT_UI_001"
    remote = {}
    try:
        remote["branch_head"] = ((branch_meta(branch).get("commit") or {}).get("sha"))
        for key, path in {
            "publication": f"{root}/phase_e_publication.json",
            "registration": f"{root}/phase_e_registration.json",
            "lock": f"{root}/phase_e_lock.json",
        }.items():
            meta = get_file(branch, path)
            remote[key] = {"exists": bool(meta), "blob_sha": (meta or {}).get("sha"), "path": path}
    except Exception as e:
        remote["error"] = f"{type(e).__name__}: {e}"
    return {"local_state": local, "github": {"repo": GITHUB_REPO, "branch": branch, **remote}}
