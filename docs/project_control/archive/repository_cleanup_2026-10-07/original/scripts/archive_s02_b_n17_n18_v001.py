from pathlib import Path
import hashlib, json, os, struct, subprocess

RUN_ID = os.environ.get("GITHUB_RUN_ID", "UNKNOWN")
DATE = "2026-09-29"

SPECS = {
    "N17": {
        "src": "N17_Candidate_03_APPROVED.png",
        "dst": "production/image_library/approved/story_shots/N17_BLOOD_DOOR_WARNING_APPROVED_V001.png",
        "size": 1671344,
        "sha256": "bd31599978d927cbd3748dc77073503c78cf87ccc68b21458de08625ebbfa3a3",
        "blob": "c5020af8fa61225f0e4a88104990c1663fddcec9",
        "title": "Blood-Door Warning",
        "timeline": "01:28.120-01:40.700",
        "characters": ["NING_QIUSHUI", "JUN_LUYUAN"],
        "bundle": "N17_REFERENCE_DELIVERY_BUNDLE_V001",
        "artifact": 11018019993,
        "candidate": "N17 Candidate 03",
    },
    "N18": {
        "src": "城堡门外的晴天.png",
        "dst": "production/image_library/approved/story_shots/N18_CLEAR_SKY_DOUBT_APPROVED_V001.png",
        "size": 2158626,
        "sha256": "18746fdde8a3b7699061fd6f4a8a6b666d50001250a2df902bb3b5995e7e2613",
        "blob": "039471efd721fa5f822c4fb8ec933b4893f91641",
        "title": "Clear-Sky Doubt",
        "timeline": "01:40.700-01:46.720",
        "characters": ["JUN_LUYUAN"],
        "bundle": "N18_REFERENCE_DELIVERY_BUNDLE_V001",
        "artifact": 11025373622,
        "candidate": "N18 Candidate 04｜Clean Regeneration",
    },
}

def sh(*args):
    return subprocess.check_output(args, text=True).strip()

def verify_png(path, spec, label):
    p = Path(path)
    assert p.is_file(), f"{label}_MISSING: {path}"
    b = p.read_bytes()
    assert b[:8] == b"\x89PNG\r\n\x1a\n", f"{label}_PNG_SIGNATURE_FAIL"
    assert struct.unpack(">II", b[16:24]) == (941, 1672), f"{label}_DIMENSIONS_FAIL"
    assert len(b) == spec["size"], f"{label}_BYTE_SIZE_FAIL"
    assert hashlib.sha256(b).hexdigest() == spec["sha256"], f"{label}_SHA256_FAIL"
    assert sh("git", "hash-object", str(p)) == spec["blob"], f"{label}_GIT_BLOB_FAIL"
    print(f"{label}_PASS SHA_MATCH=YES BLOB_MATCH=YES DIMENSIONS_MATCH=YES")

def git_commit(message, paths):
    subprocess.check_call(["git", "add", *paths])
    subprocess.check_call(["git", "commit", "-m", message])
    return sh("git", "rev-parse", "HEAD")

subprocess.check_call(["git", "config", "user.name", "github-actions[bot]"])
subprocess.check_call(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"])

for shot, spec in SPECS.items():
    verify_png(spec["src"], spec, f"{shot}_SOURCE_EXACT_BINARY")
print("EXACT_BINARY_VERIFICATION=PASS")

for spec in SPECS.values():
    assert not Path(spec["dst"]).exists(), f"CANONICAL_ALREADY_EXISTS: {spec['dst']}"

Path("production/image_library/approved/story_shots").mkdir(parents=True, exist_ok=True)
for shot, spec in SPECS.items():
    subprocess.check_call(["git", "mv", spec["src"], spec["dst"]])
    verify_png(spec["dst"], spec, f"{shot}_CANONICAL_EXACT_BINARY")

publication_commit = git_commit(
    "P0.3 S02-B N17 N18 canonical exact-blob publication",
    [spec["dst"] for spec in SPECS.values()],
)
print(f"PUBLICATION_COMMIT={publication_commit}")
print("CANONICAL_PUBLICATION=PASS")

idx = Path("production/story_shots/story_shot_index.jsonl")
rows = [json.loads(x) for x in idx.read_text(encoding="utf-8").splitlines() if x.strip()]
existing = {x.get("shot_id") for x in rows}
assert "N17" not in existing, "N17_ALREADY_REGISTERED"
assert "N18" not in existing, "N18_ALREADY_REGISTERED"

records = [
    {
        "shot_id": "N17",
        "asset_class": "STORY_SHOT",
        "approval_status": "APPROVED",
        "lifecycle": "CURRENT",
        "historical_prefix": "N",
        "title": "Blood-Door Warning",
        "canonical_path": SPECS["N17"]["dst"],
        "filename": Path(SPECS["N17"]["dst"]).name,
        "byte_size": SPECS["N17"]["size"],
        "dimensions": {"width": 941, "height": 1672},
        "github_blob_sha": SPECS["N17"]["blob"],
        "sha256_locked_identity": SPECS["N17"]["sha256"],
        "sha256_verification_status": "VERIFIED_MATCH_BY_GITHUB_ACTIONS_2026-09-29",
        "binary_verification_run": int(RUN_ID) if RUN_ID.isdigit() else RUN_ID,
        "rename_preserved_exact_git_blob": True,
        "story_beat": "Ning Qiushui stops the sister discussion and gives Jun Luyuan restrained, practical Blood Door survival reminders; Jun listens and acknowledges.",
        "timeline": SPECS["N17"]["timeline"],
        "characters": SPECS["N17"]["characters"],
        "scene": "CASTLE_ENTRANCE",
        "continuity_tags": ["S02_B", "INTERIOR_THRESHOLD", "NING_QIUSHUI", "JUN_LUYUAN", "BLOOD_DOOR_WARNING", "SURVIVAL_RULES", "DAY_DOOR_OPEN"],
        "approved_at": DATE,
        "provenance": f"PO-approved N17 Candidate 03 exact source; exact-binary verification and canonical publication performed by GitHub Actions run {RUN_ID}; publication commit {publication_commit}; N17 Reference Delivery Bundle artifact 11018019993.",
    },
    {
        "shot_id": "N18",
        "asset_class": "STORY_SHOT",
        "approval_status": "APPROVED",
        "lifecycle": "CURRENT",
        "historical_prefix": "N",
        "title": "Clear-Sky Doubt",
        "canonical_path": SPECS["N18"]["dst"],
        "filename": Path(SPECS["N18"]["dst"]).name,
        "byte_size": SPECS["N18"]["size"],
        "dimensions": {"width": 941, "height": 1672},
        "github_blob_sha": SPECS["N18"]["blob"],
        "sha256_locked_identity": SPECS["N18"]["sha256"],
        "sha256_verification_status": "VERIFIED_MATCH_BY_GITHUB_ACTIONS_2026-09-29",
        "binary_verification_run": int(RUN_ID) if RUN_ID.isdigit() else RUN_ID,
        "rename_preserved_exact_git_blob": True,
        "story_beat": "Jun Luyuan looks toward the bright, still-open castle entrance and naturally questions the likelihood of rain because the weather visibly appears calm and clear.",
        "timeline": SPECS["N18"]["timeline"],
        "characters": SPECS["N18"]["characters"],
        "scene": "CASTLE_ENTRANCE",
        "continuity_tags": ["S02_B", "INTERIOR_THRESHOLD", "JUN_LUYUAN", "CLEAR_SKY_DOUBT", "DAY_DOOR_OPEN", "OPEN_DOOR", "BODY_PERFORMANCE_DIVERSITY"],
        "approved_at": DATE,
        "provenance": f"PO-approved N18 Candidate 04 Clean Regeneration exact source; exact-binary verification and canonical publication performed by GitHub Actions run {RUN_ID}; publication commit {publication_commit}; N18 Reference Delivery Bundle artifact 11025373622.",
    },
]
with idx.open("a", encoding="utf-8") as f:
    for rec in records:
        f.write(json.dumps(rec, ensure_ascii=False, separators=(",", ":")) + "\n")

rows2 = [json.loads(x) for x in idx.read_text(encoding="utf-8").splitlines() if x.strip()]
for shot, spec in SPECS.items():
    hits = [x for x in rows2 if x.get("shot_id") == shot]
    assert len(hits) == 1, f"{shot}_INDEX_COUNT_FAIL"
    r = hits[0]
    assert r["canonical_path"] == spec["dst"]
    assert r["sha256_locked_identity"] == spec["sha256"]
    assert r["github_blob_sha"] == spec["blob"]
    assert r["byte_size"] == spec["size"]
    assert r["dimensions"] == {"width": 941, "height": 1672}
    assert r["approval_status"] == "APPROVED"
    assert r["lifecycle"] == "CURRENT"
    assert r["title"] == spec["title"]
    assert r["timeline"] == spec["timeline"]
    assert r["characters"] == spec["characters"]
    verify_png(spec["dst"], spec, f"{shot}_REGISTRATION_BINARY_RECHECK")
    print(f"{shot}_INDEX_MATCH=YES")

registration_commit = git_commit(
    "P0.3 S02-B register N17 N18 Story Shots",
    [str(idx)],
)
print(f"REGISTRATION_COMMIT={registration_commit}")
print("REGISTRATION_VERIFICATION=PASS")

gate = Path("docs/project_control/gates/P0_3_video_pipeline")
for shot, spec in SPECS.items():
    closeout = f"""# S02-B｜{shot} Story Shot Registration Closeout

Status: COMPLETE / PRODUCT OWNER APPROVED / CANONICAL / REGISTERED / VERIFIED

Date: {DATE}

- shot: {shot}｜{spec["title"]}
- selected candidate: {spec["candidate"]}
- canonical path: {spec["dst"]}
- dimensions: 941x1672
- byte_size: {spec["size"]}
- SHA-256: {spec["sha256"]}
- Git blob: {spec["blob"]}
- exact blob preserved: YES
- archival workflow run: {RUN_ID}
- canonical publication commit: {publication_commit}
- registration commit: {registration_commit}
- registration verification: PASS
- Bundle: {spec["bundle"]}
- Bundle artifact: {spec["artifact"]}

{shot} = FORMALLY CLOSED
"""
    if shot == "N18":
        closeout += "\nNext production step:\n\nN19 Scene Reference Design\n"
    (gate / f"s02_b_{shot.lower()}_story_shot_registration_closeout_2026-09-29.md").write_text(closeout, encoding="utf-8")

deferred = gate / "s02_b_deferred_archival_checkpoint_2026-09-29.md"
deferred.write_text(
    deferred.read_text(encoding="utf-8")
    + f"\n\n## Evening closeout resolution\n\nN17 and N18 completed Exact Binary Verification → Canonical Publication → Story Shot Registration → Registration Verification in GitHub Actions run {RUN_ID}. Deferred archival is resolved for these two shots.\n",
    encoding="utf-8",
)

ps_path = Path("docs/project_control/core/project_state.json")
ps = json.loads(ps_path.read_text(encoding="utf-8"))
ps["state_revision"] = "R133"
ps["last_updated"] = DATE
ps["current_task"] = "P0.3｜S02-B｜N19 Scene Reference Design"
ps["next_action"] = "Design and lock N19 Scene Reference Design V0.1 before any N19 Reference Delivery Bundle construction."
ps["latest_checkpoint"] = {
    "id": "2026-09-29-N17-N18-ARCHIVAL-R133",
    "status": "N17 + N18 FORMALLY CLOSED / N19 READY FOR SCENE REFERENCE DESIGN",
    "completed": [
        "N17 Candidate 03 exact source verified, canonically published, registered, and registration-verified.",
        "N18 Candidate 04 Clean Regeneration exact source verified, canonically published, registered, and registration-verified.",
        "Exact Git blobs preserved with no re-encode or resize.",
        "Deferred archival checkpoint resolved for N17 and N18."
    ],
    "resume_from": "N19 Scene Reference Design V0.1.",
    "blockers": []
}
ps["n17_candidate_03"] = {
    "status": "PRODUCT OWNER APPROVED / CANONICAL PUBLISHED / FORMALLY REGISTERED / REGISTRATION VERIFIED / CLOSED",
    "selected_candidate": SPECS["N17"]["candidate"],
    "dimensions": "941x1672",
    "byte_size": SPECS["N17"]["size"],
    "sha256": SPECS["N17"]["sha256"],
    "github_blob_sha": SPECS["N17"]["blob"],
    "canonical_path": SPECS["N17"]["dst"],
    "archival_workflow_run": int(RUN_ID) if RUN_ID.isdigit() else RUN_ID,
    "canonical_publication_commit": publication_commit,
    "registration_commit": registration_commit,
    "closeout_path": "docs/project_control/gates/P0_3_video_pipeline/s02_b_n17_story_shot_registration_closeout_2026-09-29.md"
}
ps["n18_candidate_04"] = {
    "status": "PRODUCT OWNER APPROVED / CANONICAL PUBLISHED / FORMALLY REGISTERED / REGISTRATION VERIFIED / CLOSED",
    "selected_candidate": SPECS["N18"]["candidate"],
    "dimensions": "941x1672",
    "byte_size": SPECS["N18"]["size"],
    "sha256": SPECS["N18"]["sha256"],
    "github_blob_sha": SPECS["N18"]["blob"],
    "canonical_path": SPECS["N18"]["dst"],
    "archival_workflow_run": int(RUN_ID) if RUN_ID.isdigit() else RUN_ID,
    "canonical_publication_commit": publication_commit,
    "registration_commit": registration_commit,
    "closeout_path": "docs/project_control/gates/P0_3_video_pipeline/s02_b_n18_story_shot_registration_closeout_2026-09-29.md"
}
ps_path.write_text(json.dumps(ps, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

for logname, entry in [
    ("docs/project_control/logs/decision_log.md", f"\n- {DATE}｜S02-B｜N17/N18: Product Owner-approved exact binaries formally archived. N17/N18 are canonical, registered, and verified. Next: N19 Scene Reference Design. Archival run {RUN_ID}.\n"),
    ("docs/project_control/logs/execution_log.md", f"\n- {DATE}｜P0.3 S02-B｜N17/N18 formal archival closeout: exact verification PASS; exact-blob publication commit {publication_commit}; Story Shot registration commit {registration_commit}; registration verification PASS; archival run {RUN_ID}.\n")
]:
    lp = Path(logname)
    lp.write_text(lp.read_text(encoding="utf-8") + entry, encoding="utf-8")

closeout_paths = [
    str(gate / "s02_b_n17_story_shot_registration_closeout_2026-09-29.md"),
    str(gate / "s02_b_n18_story_shot_registration_closeout_2026-09-29.md"),
    str(deferred),
    str(ps_path),
    "docs/project_control/logs/decision_log.md",
    "docs/project_control/logs/execution_log.md"
]
closeout_commit = git_commit(
    "project-control: close N17 N18 formal archival",
    closeout_paths,
)
print(f"CLOSEOUT_COMMIT={closeout_commit}")

ps2 = json.loads(ps_path.read_text(encoding="utf-8"))
assert ps2["n17_candidate_03"]["status"].endswith("CLOSED")
assert ps2["n18_candidate_04"]["status"].endswith("CLOSED")
assert ps2["next_action"].startswith("Design and lock N19")
for shot, spec in SPECS.items():
    verify_png(spec["dst"], spec, f"{shot}_FINAL_CANONICAL")
assert (gate / "s02_b_n17_story_shot_registration_closeout_2026-09-29.md").exists()
assert (gate / "s02_b_n18_story_shot_registration_closeout_2026-09-29.md").exists()
print("N17_FORMAL_CLOSEOUT=PASS")
print("N18_FORMAL_CLOSEOUT=PASS")
print("PROJECT_CONTROL_CLOSEOUT=PASS")
print("OVERALL_RESULT=PASS")

subprocess.check_call(["git", "push", "origin", "HEAD:main"])
