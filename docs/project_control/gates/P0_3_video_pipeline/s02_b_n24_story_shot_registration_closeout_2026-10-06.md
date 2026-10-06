# S02-B｜N24 Story Shot Registration Closeout

Status:

`COMPLETE / PRODUCT OWNER APPROVED / CANONICAL / REGISTERED / VERIFIED`

Date:

`2026-10-06`

Shot:

`N24｜Guang Yong Questions the Open Door`

Selected final result:

`N24 Candidate 03｜Controlled Modification`

## Product Owner approval

The Product Owner approved Candidate 03 after Candidate 02 was rejected for:

- strong cutout / composited appearance;
- foreground and background reading as separate layers;
- overly empty framing;
- Guang Yong gaze not sufficiently aligned to the camera / Neil axis.

Candidate 03 preserved the accepted Guang Yong identity while tightening the dialogue framing, integrating the group into one shared depth field, and moving Guang Yong's gaze directly toward the camera / entrance-side Neil axis.

## Exact approved binary

- dimensions: `972 × 1619`
- mode: `RGBA`
- byte size: `2,734,305`
- SHA-256: `e6604ec6a66151bc68bbd443812a538e2cd92820b6d5a601a98e3c4b90c13f34`
- Git blob: `5541be10e8f679dd87df94b63d35eaa3d9482def`

Approved source filename:

`N24_Candidate_03_APPROVED.png`

Approved dimension exception:

`972 × 1619 / PRODUCT OWNER APPROVED EXACT BINARY / RESIZE FORBIDDEN`

## Bundle provenance

Formal generation bundle:

`N24_REFERENCE_DELIVERY_BUNDLE_V004`

- workflow run: `37441781229`
- job: `112197010394`
- Artifact ID: `11400539916`
- Artifact digest: `sha256:7df5acb788a06a80f0b4a0ad78bf15323d7d51949e8880fef9d7e2354c4cb917`
- exact reference verification: `5/5 PASS`

Direct visual inputs:

1. `AST_IMG_000056｜Guang Yong Character Reference Sheet`
2. `AST_IMG_000010｜Guang Yong FACE_3Q_RIGHT`
3. `AST_IMG_000009｜Guang Yong BODY_FRONT`
4. `AST_IMG_000108｜SCENE_CASTLE_ENTRANCE_INNER_LOBBY`
5. `BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_FRONT`

## Candidate Intake Verification

Delivery Spec:

`production/candidate_delivery_specs/N24_CANDIDATE_03_DELIVERY_V001.json`

Staging path:

`staging/story_shot_candidates/N24/N24_Candidate_03_APPROVED.png`

Intake workflow:

`Story Shot Candidate Intake Verifier`

- run: `37454268409`
- job: `112237908693`
- artifact ID: `11408906165`
- artifact digest: `sha256:193411119b5ec5387db527823371a88ea7fa1074eb7e93490f49d546b8979f8c`

Verified actual:

- byte size: `2,734,305`
- SHA-256: `e6604ec6a66151bc68bbd443812a538e2cd92820b6d5a601a98e3c4b90c13f34`
- Git blob: `5541be10e8f679dd87df94b63d35eaa3d9482def`
- dimensions: `972 × 1619`

Result:

`CANDIDATE_INTAKE_VERIFIED = TRUE`

## Canonical Publication

Canonical path:

`production/image_library/approved/story_shots/N24_GUANG_YONG_QUESTIONS_OPEN_DOOR_APPROVED_V001.png`

Publication workflow:

`N24 Canonical Exact-Blob Publication V001`

- run: `37454405467`
- job: `112238355820`
- publication commit: `88df6088471ac936fc81ca506310eb9d00d6161e`

Exact Git blob preserved:

`YES`

Canonical Git blob:

`5541be10e8f679dd87df94b63d35eaa3d9482def`

Canonical byte size:

`2,734,305`

No resize, re-encode, recompression, screenshot substitution, crop, color change, or pixel modification occurred during canonicalization.

Staging PNG was removed by exact-blob move.

## Story Shot Registration

Story Shot Index:

`production/story_shots/story_shot_index.jsonl`

Registration commit:

`387b7fc63418ab10aa36dae02d23690df0307345`

Registered identity:

- shot_id: `N24`
- asset_class: `STORY_SHOT`
- approval_status: `APPROVED`
- lifecycle: `CURRENT`
- title: `Guang Yong Questions the Open Door`
- scene: `CASTLE_ENTRANCE_INNER_LOBBY`
- characters: `GUANG_YONG`
- timeline: `02:11.500-02:15.500`

Story beat:

Guang Yong stands with the group after they have entered and paused in the inner lobby, looks directly toward the entrance-side Neil / camera axis, and asks whether the castle door needs to be closed. Neil remains off-screen.

## Registration Verification

Workflow:

`N24 Story Shot Registration Verification V001`

- run: `37454566636`
- job: `112238890955`

Result:

- `N24_PASS`
- `SHA_MATCH=YES`
- `BLOB_MATCH=YES`
- `INDEX_MATCH=YES`
- `DIMENSIONS_MATCH=YES`
- `STAGING_CLEANUP_PASS`
- `OVERALL_RESULT=PASS`

## Final disposition

`N24 = FORMALLY CLOSED / CANONICAL / REGISTERED / VERIFIED`

Next downstream node:

`N25｜Neil Response — Castle Door Only Closes on Rainy Days`

N25 remains:

`NOT YET AUTHORIZED FOR PRODUCTION`
