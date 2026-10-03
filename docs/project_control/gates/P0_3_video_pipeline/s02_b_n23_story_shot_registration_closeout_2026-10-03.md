# S02-B｜N23 Story Shot Registration Closeout

Status:

`COMPLETE / PRODUCT OWNER APPROVED / CANONICAL / REGISTERED / VERIFIED`

Date:

`2026-10-03`

Shot:

`N23｜Neil at the Open Door — Watches the Group Enter`

Selected final result:

`N23 Candidate 03｜Clean Regeneration + Product Owner Localized Edits`

## Product Owner approval

The Product Owner approved the final N23 image after two localized edit rounds performed in Work.

Edit lineage:

1. delete person near `x=14.3%, y=48.9%`;
2. delete person near `x=93.5%, y=30.4%`;
3. person near `x=57.7%, y=47.3%` looks upper-right;
4. person near `x=79.9%, y=31.1%` looks lower-left.

These edits remain within Candidate 03 lineage and do not create Candidate 04.

## Exact approved binary

- dimensions: `941 × 1672`
- mode: `RGBA`
- byte size: `2,697,400`
- SHA-256: `2d94488e36d878ccb6ae7c3f9f3bf2a122eebca5ae01ad0e5b3105de4d535973`
- Git blob: `649ed97addf97f126a05e12d43325720a624ea19`

Initial GitHub upload commit:

`312c1c8ceb2ffa1ef76f8cc0ccf3588a54e7ad5a`

Uploaded staging path:

`staging/story_shot_candidates/N23/N23_Candidate_03_APPROVED.png`

## Candidate Intake Verification

The first automatically triggered intake run failed because no N23 Candidate Delivery Spec existed yet:

- run: `37114455419`
- job: `111178426597`
- failure: `SPEC_CARDINALITY_FAIL=0`
- interpretation: specification absence only; no binary mismatch.

Delivery Spec:

`production/candidate_delivery_specs/N23_CANDIDATE_03_DELIVERY_V001.json`

Spec commit:

`c38b9c7212510c8865338f77d1b11d369db51340`

Formal intake verification:

- workflow: `Story Shot Candidate Intake Verifier`
- run: `37114574502`
- job: `111178760205`
- artifact ID: `11271013272`
- artifact digest: `sha256:b1a6fda2d398b7731eb3223183a6e286aedab5f41c9b0a58970ceffffe6508a6`

Verified expected = actual:

- width: `941`
- height: `1672`
- byte size: `2,697,400`
- SHA-256: `2d94488e36d878ccb6ae7c3f9f3bf2a122eebca5ae01ad0e5b3105de4d535973`
- Git blob: `649ed97addf97f126a05e12d43325720a624ea19`

Overall:

`CANDIDATE_INTAKE_VERIFIED = TRUE`

## Canonical Publication

Canonical path:

`production/image_library/approved/story_shots/N23_NEIL_AT_OPEN_DOOR_APPROVED_V001.png`

Publication workflow:

`N23 Canonical Exact-Blob Publication V001`

Publication run:

`37114635199`

Publication job:

`111178938708`

Publication commit:

`471c1784295e68a6b45d2869ab62ecdbea8cd014`

Exact Git blob preserved:

`YES`

Canonical Git blob:

`649ed97addf97f126a05e12d43325720a624ea19`

No resize, re-encode, recompression, screenshot substitution or pixel modification occurred during canonicalization.

Staging candidate PNG was removed by exact-blob move.

## Story Shot Registration

Story Shot Index:

`production/story_shots/story_shot_index.jsonl`

Registration commit:

`3887854fb622f90b9bf2c86e9954dbd0c1c33988`

Registered identity:

- shot_id: `N23`
- asset_class: `STORY_SHOT`
- approval_status: `APPROVED`
- lifecycle: `CURRENT`
- title: `Neil at the Open Door — Watches the Group Enter`
- scene: `CASTLE_ENTRANCE`
- characters: `NEIL / GUANG_YONG`
- timeline: `after N22 / exact N23 micro-cut deferred`

## Registration Verification

Workflow:

`N23 Story Shot Registration Verification V001`

Run:

`37114733431`

Job:

`111179226534`

Result:

- `N23_PASS`
- `SHA_MATCH=YES`
- `BLOB_MATCH=YES`
- `INDEX_MATCH=YES`
- `DIMENSIONS_MATCH=YES`
- `STAGING_CLEANUP_PASS`
- `OVERALL_RESULT=PASS`

## Bundle provenance

Formal Candidate 03 generation bundle:

`N23_REFERENCE_DELIVERY_BUNDLE_V003`

- workflow run: `37108188787`
- Artifact ID: `11268607749`
- Artifact digest: `sha256:674228ac21d51f47d8d0bbd2bc3c5463b1190d47e754f9a5e720b8d833e7554f`
- exact reference verification: `4/4 PASS`

Direct visual inputs:

1. `N23_CASTLE_ENTRANCE_DOOR_CONTROL_REFERENCE_V001`
2. `AST_IMG_000073｜Neil FACE_3Q_RIGHT`
3. `AST_IMG_000011｜Guang FACE_FRONT`
4. `BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q`

## Final disposition

`N23 = FORMALLY CLOSED / CANONICAL / REGISTERED / VERIFIED`

N21 remains:

`HOLD / UNRESOLVED`

N22 remains:

`CLOSED / CANONICAL / REGISTERED / VERIFIED`

Next downstream unstarted node:

`N24 / UNSTARTED`
