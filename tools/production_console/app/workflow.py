from copy import deepcopy
from typing import Dict, Any

STAGES = ["DESIGN", "PREFLIGHT", "GENERATE", "REVIEW", "PUBLISH", "REGISTER", "LOCK", "CLOSEOUT"]

STATUS_STAGE = {
    "DESIGN_PENDING": "DESIGN",
    "DESIGN_APPROVED": "PREFLIGHT",
    "PREFLIGHT_FAILED": "PREFLIGHT",
    "PREFLIGHT_PASS": "GENERATE",
    "AWAITING_CANDIDATE": "GENERATE",
    "CANDIDATE_VERIFIED_PENDING_PO": "REVIEW",
    "REJECTED": "REVIEW",
    "PO_APPROVED_PENDING_PUBLICATION": "PUBLISH",
    "PUBLISHED_NOT_REGISTERED": "REGISTER",
    "REGISTERED_PENDING_LOCK": "LOCK",
    "LOCKED_PENDING_CLOSEOUT": "CLOSEOUT",
    "CLOSED": "CLOSEOUT",
}

ALLOWED = {
    "DESIGN_PENDING": {"DESIGN_APPROVED"},
    "DESIGN_APPROVED": {"PREFLIGHT_PASS", "PREFLIGHT_FAILED"},
    "PREFLIGHT_FAILED": {"PREFLIGHT_PASS", "PREFLIGHT_FAILED"},
    "PREFLIGHT_PASS": {"AWAITING_CANDIDATE"},
    "AWAITING_CANDIDATE": {"CANDIDATE_VERIFIED_PENDING_PO"},
    "CANDIDATE_VERIFIED_PENDING_PO": {"PO_APPROVED_PENDING_PUBLICATION", "REJECTED"},
    "REJECTED": set(),
    "PO_APPROVED_PENDING_PUBLICATION": {"PUBLISHED_NOT_REGISTERED"},
    "PUBLISHED_NOT_REGISTERED": {"REGISTERED_PENDING_LOCK"},
    "REGISTERED_PENDING_LOCK": {"LOCKED_PENDING_CLOSEOUT"},
    "LOCKED_PENDING_CLOSEOUT": {"CLOSED"},
    "CLOSED": set(),
}


def stage_for(status: str) -> str:
    if status not in STATUS_STAGE:
        raise ValueError(f"未知状态: {status}")
    return STATUS_STAGE[status]


def transition(session: Dict[str, Any], new_status: str) -> Dict[str, Any]:
    current = session.get("status")
    if new_status == current:
        session["current_stage"] = stage_for(new_status)
        return session
    allowed = ALLOWED.get(current, set())
    if new_status not in allowed:
        raise ValueError(f"非法状态转换: {current} -> {new_status}")
    session["status"] = new_status
    session["current_stage"] = stage_for(new_status)
    return session


def candidate_identity(candidate: Dict[str, Any]) -> Dict[str, Any]:
    fields = ["shot_id", "candidate_id", "drive_file_id", "sha256", "byte_size", "width", "height", "mime_type"]
    return {k: candidate.get(k) for k in fields}


def identity_complete(candidate: Dict[str, Any]) -> bool:
    ident = candidate_identity(candidate)
    required = ["shot_id", "candidate_id", "drive_file_id", "sha256", "byte_size", "width", "height"]
    return all(ident.get(k) not in (None, "") for k in required)


def binding_matches(candidate: Dict[str, Any], binding: Dict[str, Any]) -> bool:
    ident = candidate_identity(candidate)
    return (
        binding.get("candidate_id") == ident.get("candidate_id")
        and binding.get("drive_file_id") == ident.get("drive_file_id")
        and binding.get("sha256") == ident.get("sha256")
    )


def public_session(session: Dict[str, Any]) -> Dict[str, Any]:
    out = deepcopy(session)
    # No OAuth or token material is ever stored in a session, but keep this defensive.
    for key in list(out.keys()):
        if "token" in key.lower() or "credential" in key.lower():
            out.pop(key, None)
    return out
