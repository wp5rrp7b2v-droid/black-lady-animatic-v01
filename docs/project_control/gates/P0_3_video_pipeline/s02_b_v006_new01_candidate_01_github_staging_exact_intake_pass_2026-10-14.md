# S02-B V006｜NEW-01｜Candidate 01 GitHub Staging Original PNG Exact Intake Verification

Date: 2026-10-14

**State: PRODUCT OWNER VISUALLY APPROVED / ORIGINAL GITHUB UPLOAD EXACT BINARY VERIFIED / STAGING GATE CLOSED / NO CANONICAL PUBLICATION OR STORY SHOT REGISTRATION.**

## Source authority and PO choice

The Product Owner said **“这张为批准图”** and uploaded the original NEW-01 image with conversation filename `烛光回廊里的轻声提醒(1).png`.

- Task ID: `S02B_V006_NING_WARNING_JUN_SHOULDER_OTS_TEST_01`
- Candidate: `Candidate 01`
- Intended editorial purpose: Jun's rear-shoulder OTS toward Ning Qiushui giving the final warning during N20, before the separately PO-approved Jun B V002 close-up.
- Original image identity captured at approval: **941×1672, 1,840,569 bytes, SHA-256 `f3002984a377a31e05cd7490e914c0da4009509c8ddb5eaf45a5d45144775989`, Git blob `7fedcdc93f2b366d1a8597e86ffe8c99006ce027`**.
- Original reference Bundle run `38541197812` Artifact `11882167307`, five references 5/5 exact PASS.

## Actual GitHub staging upload

- Branch `review/s02b-jun-nod-insert-20261014`
- Actual path:
  `staging/story_shot_candidates/S02B_V006_NING_WARNING_JUN_SHOULDER_OTS_TEST_01/烛光回廊里的轻声提醒.png`
- Actual user-upload commit: `41e12b488a5b4715c3c4e60241c37eebcc1b55dc`
- Source basename difference: the GitHub upload omits **`(1)`** compared to the chat attachment filename. The GitHub blob remains `7fedcdc93f2b366d1a8597e86ffe8c99006ce027`; **no image bytes changed**.

## Failure and recovery audit

- Initial candidate intake Run **`38549001354` FAILED** due solely to candidate path mismatch: the initial delivery Spec and workflow pointed to `烛光回廊里的轻声提醒(1).png` while the uploaded real file was `烛光回廊里的轻声提醒.png`; the first job's pathname precondition failed before invoking the binary verifier.
- Recovered by changing only target path in `production/candidate_delivery_specs/S02B_V006_NING_WARNING_JUN_SHOULDER_OTS_TEST_01_CANDIDATE_01_DELIVERY_V001.json`, the dedicated workflow `.github/workflows/s02b-v006-new01-po-candidate-intake-v001.yml` and staging README. Retained all exact identity fields unchanged; the workflow config change self-triggered re-verification.
- **No reupload, rename or edit of user PNG was necessary.**

## Final successful GitHub Actions exact verification

- Run: **`38549255960`**
- Job: **`115802904615`**
- Workflow triggering commit: `129b3882c48ac7c38f4c93d14b8cdd0312a8a195`
- Run URL: https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/38549255960
- Run result: **`completed / success`**.
- Verified output:
  - `PO_APPROVED_NEW01_EXACT_CANDIDATE=TRUE`
  - `CANDIDATE_PATH=staging/story_shot_candidates/S02B_V006_NING_WARNING_JUN_SHOULDER_OTS_TEST_01/烛光回廊里的轻声提醒.png`
  - `BYTE_SIZE=1840569`
  - `SHA256=f3002984a377a31e05cd7490e914c0da4009509c8ddb5eaf45a5d45144775989`
  - `GIT_BLOB=7fedcdc93f2b366d1a8597e86ffe8c99006ce027`
  - `DIMENSIONS=941x1672`
  - `CANDIDATE_INTAKE_VERIFIED=TRUE`
  - `NEW01_PO_CANDIDATE_EXACT_INTAKE=PASS`
  - `CANDIDATE_ONLY_NO_PUBLICATION=TRUE`
  - `CANONICAL_PUBLICATION=FORBIDDEN`
  - `STORY_SHOT_REGISTRATION=FORBIDDEN`
  - `VIDEO_MASTER_MODIFICATION=FORBIDDEN`.
- Evidence Artifact ID: **`11885418671`**
- Evidence Artifact name: `S02B_V006_NEW01_PO_APPROVED_PNG_EXACT_INTAKE_EVIDENCE_ONLY`
- Evidence ZIP size: **844 bytes**.
- ZIP digest: **`sha256:ace9ff436b8925cdfe92dbaf5d8784d879b8743b097ad6393032886986d971d8`**.
- Expires on **2026-11-13T10:24:08Z**.

## Gate conclusion

**NEW-01 Candidate 01 STAGING + EXACT INTAKE = PASS / CLOSED.**

No further image upload required. PO visual approval and original binary identity are both established.

**NOT authorized or executed:** copy/move source into `production/image_library/approved/story_shots/`, Story Shot Index registration, registration readback, Video Index change, V006 review video render, modification to N16–N17 V004 / Jun B V002 / Ning reaction / approved S02-B video, Project Control canonical closeout or main merge.

Next explicit gate: **Product Owner authorizes or declines formal exact-binary canonical publication and subsequent Story Shot registration for NEW-01.** Alternatively, the project can hold this exact staging image for V006 editorial testing without formal publication only if such a scope is separately approved.
