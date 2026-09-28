# S02-A Assembly V001 Formal Closeout｜2026-09-28

Status: `PRODUCT_OWNER APPROVED / CANONICAL / REGISTERED / VERIFIED / FORMALLY CLOSED`

## 1. Scope

This closeout covers the approved S02-A assembly sequence:

`N11 → N12 → A04 → N14 → N15 → A05`

Narrative/audio scope:

- canonical audio start: `00:33.020`
- canonical audio end: `01:18.750`
- approved duration: `45.730s`
- A05 retains the explicit no-key reveal ownership.

This closeout does **not** mark the whole P0.3 Gate as PASS. P0.3 remains active for subsequent production/pipeline validation.

## 2. Audio boundary correction

The first assembly proof was rejected by the Product Owner because the audible content boundary was incomplete.

The corrected audio-only QC proof used:

`00:33.020 → 01:18.750`

The Product Owner explicitly listened to the corrected proof and confirmed the content was complete.

Therefore the corrected boundary is the S02-A authority.

## 3. Product Owner approved assembly

Source proof:

`S02_A_ASSEMBLY_PROOF_V002`

The Product Owner explicitly approved the V002 edit after full-context viewing.

The first Work-rendered V002 file was technically decodable but used a low-compatibility delivery combination (H.264 4:4:4 / 100fps / ALAC). It was therefore **not** selected as the canonical delivery binary.

A compatibility master was produced with the approved narrative/edit content preserved and only delivery encoding normalized.

Selected canonical source binary:

`S02_A_ASSEMBLY_PROOF_V002_COMPAT.mp4`

Identity:

- SHA-256: `937008e11d20892ea0a17be64719a19cb131d174871930bc29004a678bb58ed1`
- byte size: `6822004`
- Git blob: `bcd3fef7a8d600c95cb4d7242d411cc0df41859c`
- resolution: `942×1672`
- frame rate: `30 fps`
- video: `H.264 / yuv420p`
- audio: `AAC / 48 kHz / stereo`
- duration: `45.730s`
- full video decode: PASS
- full audio decode: PASS

The 942-pixel width is the compatibility delivery width; the approved image content was not cropped.

## 4. Exact Binary Verification

Workflow:

`S02-A Approved Assembly Exact Binary Verification V001`

- run ID: `36427746113`
- job ID: `108945798299`
- upload commit: `8ca8358a8bdb49b9c57f6a24df75fe7cec7f6381`
- result: `SUCCESS / OVERALL_RESULT=PASS`
- verification artifact: `S02_A_APPROVED_UPLOAD_VERIFICATION_V001`
- artifact ID: `10972091936`
- artifact digest: `sha256:a1df96fdb852c8cc8097a1316cfd22a461fe5515d0cb3eecb232061203a6d239`

Verified:

- SHA match
- Git blob match
- byte size match
- media metadata match
- full video decode
- full audio decode

## 5. Canonical Publication

Workflow:

`S02-A Canonical Exact-Blob Publication V001`

- run ID: `36428710030`
- job ID: `108949038095`
- publication commit: `e577cd09c5ba333b7659dc08bc0898a5596edbb5`
- result: `SUCCESS / EXACT_BLOB_PRESERVED=YES / OVERALL_RESULT=PASS`

Canonical identity:

- video ID: `S02_A_ASSEMBLY_V001`
- canonical path: `production/video/approved/s02_a/S02_A_ASSEMBLY_APPROVED_V001.mp4`
- SHA-256: `937008e11d20892ea0a17be64719a19cb131d174871930bc29004a678bb58ed1`
- Git blob: `bcd3fef7a8d600c95cb4d7242d411cc0df41859c`
- byte size: `6822004`

Canonical publication preserved the selected compatibility binary exactly; no further re-encode occurred.

## 6. Video Index Registration

Registered in:

`production/video/video_index.jsonl`

Registration commit:

`ed99eba7b780f6455323d035fdb4148f5c465dc1`

Registered status:

- approval_status: `APPROVED`
- approved_by: `PRODUCT_OWNER`
- lifecycle: `CURRENT`
- exact_binary_no_reencode: `true`

## 7. Registration Verification

Workflow:

`S02-A Video Registration Verification V001`

- run ID: `36430256742`
- job ID: `108954308923`
- workflow authority commit: `795174904a700b8ad7e5374ab75ec1c2f9d4986f`
- result: `SUCCESS / OVERALL_RESULT=PASS`

Returned:

- `SHA_MATCH=YES`
- `BLOB_MATCH=YES`
- `INDEX_MATCH=YES`
- `BYTE_SIZE_MATCH=YES`
- `MEDIA_METADATA_MATCH=YES`
- `APPROVAL_LIFECYCLE_MATCH=YES`
- `FULL_VIDEO_DECODE=PASS`
- `FULL_AUDIO_DECODE=PASS`
- `STAGING_CLEANUP_PASS`

## 8. Final disposition

`S02_A_ASSEMBLY_V001 = PRODUCT_OWNER APPROVED / CANONICAL / REGISTERED / VERIFIED / FORMALLY CLOSED`

Historical/non-canonical items remain evidence only:

- rejected V001 assembly proof with incorrect/incomplete audio boundary
- original V002 high-compatibility-risk render
- Opening + S02-A combined preview used for full-context review

None of those replace the canonical S02-A master above.

## 9. Resume point

S02-A is no longer an active production task.

Next production work should start from the canonical story/audio immediately after `01:18.750`, under a new director/edit design and Product Owner authorization.

P0.3 remains `IN PROGRESS`; this closeout is sequence-level, not Gate-level approval.
