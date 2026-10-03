# S02-B｜N21 Story Shot Registration Closeout

Status:

`COMPLETE / PRODUCT OWNER APPROVED / CANONICAL / REGISTERED / VERIFIED / RISK-003 RESOLVED FOR N21`

Date:

`2026-10-03`

Shot:

`N21｜Cohort Enters — Inside the Flow`

Selected final result:

`N21 Candidate 09｜Clean Regeneration + Product Owner-directed iterative edits`

## Final Product Owner approval

The Product Owner explicitly approved the final N21 image after Work generation and multiple iterative edits.

The approved visual differs from the earlier Candidate 09 Director concept in several respects, including the final outside-to-inside threshold viewpoint and Neil's visible presence beside the door. These final Product Owner-directed edits supersede earlier generation-only exclusions for the approved Story Shot binary.

## Exact approved binary

- dimensions: `941 × 1671`
- mode: `RGB`
- byte size: `2,215,769`
- SHA-256: `4296383dc3fd330240a1107c004ce22d1c0ae730b193fcba495779308ba1ab0c`
- Git blob: `3224760c7e5bb622679d6b4f10f4817050fa6197`

### Product Owner dimension exception

Original target:

`941 × 1672`

Approved exact binary:

`941 × 1671`

Status:

`PRODUCT OWNER APPROVED EXACT-BINARY DIMENSION EXCEPTION`

Rule:

`DO NOT RESIZE / PAD / CROP / RE-ENCODE TO FORCE 941×1672`

## Generation provenance

Formal generation bundle:

`N21_REFERENCE_DELIVERY_BUNDLE_V007`

- workflow run: `37122780385`
- Artifact ID: `11273732234`
- Artifact digest: `sha256:32cff40068237c64789722d4531f5696f0807c35bce5ee79047ac7fddfe5b064`
- direct reference verification: `2/2 EXACT PASS`

Direct references:

1. `N21_CASTLE_ENTRANCE_DOOR_IDENTITY_REFERENCE_V001`
2. `BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q`

Subsequent Product Owner-directed iterative edits included:

- removing the left foreground person;
- moving to an outside-through-open-door viewpoint looking inward;
- showing the threshold in foreground;
- keeping four people continuing inward;
- adding Neil standing by the door with hands clasped;
- widening the door opening through later revisions;
- orange-jacket man looking upward;
- green-jacket woman looking left;
- bun-haired woman raising her right hand to touch the long-haired woman's shoulder;
- image clarity / cutout-feel refinement.

## GitHub staging intake

Uploaded staging path:

`staging/story_shot_candidates/N21/N21_Candidate_09_APPROVED.png`

Uploaded Git blob:

`3224760c7e5bb622679d6b4f10f4817050fa6197`

The upload was therefore already binary-identical to the approved local file.

### Initial automatic intake run

Run:

`37130483055`

Job:

`111224427573`

Result:

`FAIL / SPEC_CARDINALITY_FAIL=0`

Interpretation:

`DELIVERY SPEC ABSENT ONLY / NOT A BINARY MISMATCH`

No re-upload was required.

### Candidate Delivery Spec

Path:

`production/candidate_delivery_specs/N21_CANDIDATE_09_DELIVERY_V001.json`

Spec commit:

`f5eb162cdcc56e60bb811866ea658137aa28ca87`

The Spec explicitly locks the Product Owner-approved 941×1671 dimension exception.

### Formal Candidate Intake Verification

Workflow:

`Story Shot Candidate Intake Verifier`

Run:

`37130567985`

Job:

`111224676116`

Artifact:

`STORY_SHOT_CANDIDATE_INTAKE_VERIFICATION`

Artifact ID:

`11276561955`

Artifact digest:

`sha256:b184a68cc507629d8fc27ab2acbde4fb535f840f4f958a9481b4c639a5614db7`

Verified:

- `BYTE_SIZE=2215769`
- `SHA256=4296383dc3fd330240a1107c004ce22d1c0ae730b193fcba495779308ba1ab0c`
- `GIT_BLOB=3224760c7e5bb622679d6b4f10f4817050fa6197`
- `DIMENSIONS=941x1671`
- `CANDIDATE_INTAKE_VERIFIED=TRUE`

## Canonical exact-blob publication

Canonical path:

`production/image_library/approved/story_shots/N21_COHORT_ENTERS_INSIDE_THE_FLOW_APPROVED_V001.png`

Publication workflow:

`N21 Canonical Exact-Blob Publication V001`

Run:

`37130670997`

Job:

`111224968709`

Publication commit:

`26fb1612938aeabb19c19afe594faeb6f7bb1f4b`

Verified:

- approved dimension exception 941×1671: `PASS`
- byte size preserved: `2,215,769`
- SHA-256 preserved: `4296383dc3fd330240a1107c004ce22d1c0ae730b193fcba495779308ba1ab0c`
- Git blob preserved: `3224760c7e5bb622679d6b4f10f4817050fa6197`
- `EXACT_BLOB_PRESERVED=YES`
- `OVERALL_RESULT=PASS`

Staging candidate PNG was removed by exact-blob move.

## Story Shot Registration

Story Shot Index:

`production/story_shots/story_shot_index.jsonl`

Registration commit:

`1c8ec42728f05041fb6cafea20c821d034b2fcfe`

Registered identity:

- shot_id: `N21`
- asset_class: `STORY_SHOT`
- approval_status: `APPROVED`
- lifecycle: `CURRENT`
- title: `Cohort Enters — Inside the Flow`
- scene: `CASTLE_ENTRANCE`
- characters: `NEIL`
- timeline: `after N20 / before N22 / exact N21 micro-cut deferred`
- exact dimension exception: `941×1671 / resize forbidden`

The registration describes the final Product Owner-approved visual rather than superseded pre-edit generation instructions.

## Registration Verification

Workflow:

`N21 Story Shot Registration Verification V001`

Run:

`37130794885`

Job:

`111225320453`

Result:

- `N21_PASS`
- `SHA_MATCH=YES`
- `BLOB_MATCH=YES`
- `INDEX_MATCH=YES`
- `DIMENSIONS_941x1671_MATCH=YES`
- `DIMENSION_EXCEPTION_LOCK=PASS`
- `STAGING_CLEANUP_PASS`
- `OVERALL_RESULT=PASS`

## RISK-003 disposition

Prior risk:

`RISK-003｜N21 Multi-Person Generation Stability Tradeoff`

Exit condition required a Product Owner-approved N21 Story Shot followed by canonical publication and registration.

That exit condition is now satisfied.

Disposition:

`RESOLVED / CLOSED FOR N21`

Historical Candidate 01–08 failures remain evidence and are not deleted.

## Final disposition

`N21 = FORMALLY CLOSED / CANONICAL / REGISTERED / VERIFIED`

`N22 = CLOSED / CANONICAL / REGISTERED / VERIFIED`

`N23 = CLOSED / CANONICAL / REGISTERED / VERIFIED`

Next downstream unstarted node:

`N24 / UNSTARTED`
