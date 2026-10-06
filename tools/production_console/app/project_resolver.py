import json
import re

from github_service import get_file, decode_content, main_meta

PROJECT_STATE_PATH = "docs/project_control/core/project_state.json"


def _approved(status):
    text = str(status or "").upper()
    return "PRODUCT OWNER APPROVED" in text and "LOCKED" in text


def _exact_reference_pass(value, expected_count):
    if value is True:
        return True
    text = str(value or "").strip().upper()
    if text in ("PASS", "TRUE", "EXACT PASS"):
        return True
    m = re.search(r"(\d+)\s*/\s*(\d+)", text)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        return a == b and (not expected_count or a == expected_count)
    return False


def _latest_versioned(state, prefix):
    rows = []
    rx = re.compile(r"^" + re.escape(prefix) + r"_v(\d+(?:_\d+)*)$", re.I)
    for key, value in (state or {}).items():
        m = rx.match(key)
        if m and isinstance(value, dict):
            score = tuple(int(part) for part in m.group(1).split("_"))
            rows.append((score, key, value))
    return max(rows, default=(None, None, None), key=lambda x: x[0] if x[0] is not None else (-1,))


def infer_current_shot_id(state):
    for key in ("current_task", "session_status", "next_action"):
        text = str((state or {}).get(key) or "")
        m = re.search(r"\b([NA]\d{2})\b", text, re.I)
        if m:
            return m.group(1).upper()
    return None


def resolve_from_state(state, shot_id=None):
    shot_id = (shot_id or infer_current_shot_id(state) or "").upper()
    if not shot_id:
        raise RuntimeError("无法从 Project Control 确定当前 Shot ID")

    prefix = shot_id.lower()
    _, director_key, director = _latest_versioned(state, f"{prefix}_director_design")
    _, scene_key, scene = _latest_versioned(state, f"{prefix}_scene_reference_design")
    _, bundle_key, bundle = _latest_versioned(state, f"{prefix}_reference_delivery_bundle")

    if not bundle:
        raise RuntimeError(f"Project Control 未找到 {shot_id} 的 Reference Delivery Bundle")

    ref_count = int(bundle.get("direct_image_count") or 0)
    bundle_id = bundle.get("artifact_name")
    if not bundle_id:
        bundle_id = (bundle_key or "").upper()

    formal_build_verified = (
        "FORMAL BUILD PASS" in str(bundle.get("status") or "").upper()
        and "ARTIFACT EXACT VERIFIED" in str(bundle.get("status") or "").upper()
        and bool(bundle.get("downloaded_zip_digest_match"))
        and str(bundle.get("manifest_result") or "").upper() == "PASS"
        and bool(bundle.get("handoff_verified"))
    )

    references_exact = _exact_reference_pass(bundle.get("reference_exact_match"), ref_count)
    generation_authorized = bool(
        bundle.get("candidate_01_generation_authorized")
        or bundle.get("generation_authorized")
    )

    package_ready = bool(
        director and scene
        and _approved(director.get("status"))
        and _approved(scene.get("status"))
        and formal_build_verified
        and references_exact
    )

    return {
        "shot_id": shot_id,
        "package_ready": package_ready,
        "generation_authorized": generation_authorized,
        "design_package": {
            "director_design": {
                "key": director_key,
                "status": (director or {}).get("status"),
                "path": (director or {}).get("path"),
            },
            "scene_reference": {
                "key": scene_key,
                "status": (scene or {}).get("status"),
                "path": (scene or {}).get("path"),
            },
            "bundle": {
                "key": bundle_key,
                "status": bundle.get("status"),
                "build_record": bundle.get("build_record"),
            },
        },
        "bundle": {
            "bundle_id": bundle_id,
            "run_id": bundle.get("run_id"),
            "artifact_id": bundle.get("artifact_id"),
            "artifact_digest": bundle.get("artifact_digest"),
            "reference_count": ref_count,
            "references_exact": references_exact,
            "delivery_manifest_verified": str(bundle.get("manifest_result") or "").upper() == "PASS",
            "generation_allowed": generation_authorized,
        },
        "project_control": {
            "session_status": state.get("session_status"),
            "current_task": state.get("current_task"),
            "next_action": state.get("next_action"),
        },
        "source": {
            "project_state_path": PROJECT_STATE_PATH,
        },
    }


def resolve_project_design_package(shot_id=None):
    meta = get_file("main", PROJECT_STATE_PATH)
    if not meta:
        raise RuntimeError("无法读取 GitHub main Project Control")
    raw = decode_content(meta)
    state = json.loads((raw or b"{}").decode("utf-8"))
    result = resolve_from_state(state, shot_id=shot_id)
    result["source"]["project_state_blob_sha"] = meta.get("sha")
    result["source"]["main_commit_sha"] = ((main_meta().get("commit") or {}).get("sha"))
    return result
