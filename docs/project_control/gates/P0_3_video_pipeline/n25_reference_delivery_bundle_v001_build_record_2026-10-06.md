# N25_REFERENCE_DELIVERY_BUNDLE_V001｜Formal Build + Artifact Exact Verification Record

Date: `2026-10-06`

Status: `FORMAL BUILD PASS / ARTIFACT EXACT VERIFIED / 5 OF 5 MATCH / CANDIDATE 01 NOT YET AUTHORIZED`

Bundle: `N25_REFERENCE_DELIVERY_BUNDLE_V001`

Target: `N25 Candidate 01｜Clean Regeneration`

Spec:
`production/bundle_specs/N25_REFERENCE_DELIVERY_BUNDLE_V001.json`

Spec revision:
`V001-R2`

Formal-build spec commit:
`b98a2a60f30bbfff4a81490c7d46105bf7ac1f62`

Authorization record:
`docs/project_control/gates/P0_3_video_pipeline/n25_reference_delivery_bundle_v001_formal_build_authorization_2026-10-06.md`

## GitHub Actions

- Workflow: `Story Shot Reference Bundle Builder`
- Run: `37460860156`
- Job: `112259771222`
- Run number: `62`
- Conclusion: `SUCCESS`
- Build authorization: `true`

Builder output:
`PASS: 5/5 exact canonical reference binaries verified`

## Artifact

- Artifact name: `N25_REFERENCE_DELIVERY_BUNDLE_V001`
- Artifact ID: `11411667773`
- Artifact size: `9,062,019 bytes`
- GitHub digest: `sha256:59da1121cfce98eb22bedebce2787498cceb4e31a3235b266ec52d2e7ca25ee7`
- Downloaded ZIP computed SHA-256: `59da1121cfce98eb22bedebce2787498cceb4e31a3235b266ec52d2e7ca25ee7`
- ZIP digest result: `MATCH`

## ZIP contents

Exactly 7 files:

1. `WORK_HANDOFF.md`
2. `delivery_manifest.json`
3. `primary_neil_identity/AST_IMG_000059__CHAR_NEIL_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
4. `primary_neil_profile/AST_IMG_000065__CHAR_NEIL_PROFILE_RIGHT_DEFAULT_DEFAULT_V001.png`
5. `primary_neil_rear_3q/AST_IMG_000066__CHAR_NEIL_REAR_3Q_RIGHT_DEFAULT_DEFAULT_V001.png`
6. `scene_authority/AST_IMG_000108__SCENE_CASTLE_ENTRANCE_INNER_LOBBY_SCENE_MASTER_DEFAULT_DEFAULT_V001.png`
7. `secondary_paused_crowd/BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q__BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q.png`

## delivery_manifest.json

- bundle_id = `N25_REFERENCE_DELIVERY_BUNDLE_V001`
- target_shot_id = `N25`
- target_candidate = `N25 Candidate 01`
- reference_count = `5`
- all_reference_checks_pass = `true`
- generation_allowed = `true`
- overall_result = `PASS`

## Five-reference exact verification

- `AST_IMG_000059` — SHA / bytes / Git blob MATCH
- `AST_IMG_000066` — SHA / bytes / Git blob MATCH
- `AST_IMG_000065` — SHA / bytes / Git blob MATCH
- `AST_IMG_000108` — SHA / bytes / Git blob MATCH
- `BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q` — SHA / bytes / Git blob MATCH

Overall:
`5 / 5 EXACT MATCH`

## WORK_HANDOFF verification

Confirmed active handoff:

- sequence = `N23 → N24 → A06 → N25 → N26 → N27`;
- A06 immediately precedes N25 editorially but is not a direct generation image;
- Neil is first subject;
- Neil moves toward deeper interior;
- Neil does not turn back and does not look at camera;
- group remains mostly paused / subtly reorienting;
- motion ownership = `NEIL MOVES / GROUP MOSTLY REMAINS PAUSED`;
- no main door / exterior / rain;
- no First Hall / fireplace;
- Exactly 5 direct references.

## Governance boundary

Completed:

- V001 Formal Build;
- exactly one Artifact;
- Artifact ZIP exact verification;
- five direct-reference exact verification;
- manifest verification;
- Work handoff verification.

Not authorized by this step:

- N25 Candidate 01 Work generation;
- Candidate 02;
- Canonical Publication;
- Story Shot Registration;
- N26 production.

## Next gate

`PRODUCT OWNER AUTHORIZATION → N25 CANDIDATE 01 FORMAL WORK EXECUTION / EXACTLY 1 PNG`
