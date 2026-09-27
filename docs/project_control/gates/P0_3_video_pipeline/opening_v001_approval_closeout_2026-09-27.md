# Opening V001 Approval + Canonical Archive Closeout｜2026-09-27

Status: `PRODUCT_OWNER APPROVED / CANONICAL MASTER ARCHIVED / LOCKED`

## Product Owner decision

On 2026-09-27, the Product Owner explicitly approved the uploaded file:

`P03_OPENING_V2_PROOF_REVIEW_V002.mp4`

as the formal Opening video for `诡舍·黑衣夫人`.

This approval selects the V002 result as `OPENING_V001`. It does **not** convert V002's exact timing, effects, shot count, or Remotion implementation into a mandatory template for later editing. Future sequences continue to follow RC-026 Editing Workflow Framework V1 and must be designed from their own story/audio context.

## Independent attachment identity check

The uploaded attachment was inspected directly in Chat runtime before archival:

- SHA-256: `70d7922244161dd216a26446fd75531db20eea0ac7fc25f567f6ff14e2746e3a`
- byte size: `18892138`
- video: H.264 / yuv420p
- resolution: 1080×1920
- frame rate: 30 fps
- video frames: 991
- container duration: 33.088 sec
- audio: AAC / 48 kHz / stereo
- full decode: PASS

The SHA-256 and byte size exactly match the previously rendered V002 technical proof.

## Historical V002 source evidence

- source proof: `P03_OPENING_V2_PROOF_REVIEW_V002`
- source workflow run: `36296689531`
- source artifact ID: `10924430609`
- source artifact digest: `sha256:323a48034e45562b5153d635dbe565f51211d81a694c44202b6da92e4deba2ac`
- original V002 output SHA-256: `70d7922244161dd216a26446fd75531db20eea0ac7fc25f567f6ff14e2746e3a`

## Canonical publication

GitHub Actions archive verification run:

- run ID: `36300993520`
- result: PASS
- media identity: PASS
- full decode: PASS
- remote binary verification: PASS
- receipt artifact: `P03_OPENING_V001_APPROVAL_ARCHIVE_RECEIPT`
- receipt artifact ID: `10925990918`

Canonical master:

- video ID: `OPENING_V001`
- canonical path: `production/video/approved/opening/P03_OPENING_V2_APPROVED_V001.mp4`
- SHA-256: `70d7922244161dd216a26446fd75531db20eea0ac7fc25f567f6ff14e2746e3a`
- byte size: `18892138`
- Git blob: `9b4ef42d9eceb5d7f1eb190d508d6749ccf4b70e`
- publication commit: `208566291a5531cb34ad05e50e56e0a9fcc51c02`
- binary treatment: exact V002 bytes / no re-encode

Machine-readable registration:

`production/video/video_index.jsonl`

## Selection result

Selected:

`P03_OPENING_V2_PROOF_REVIEW_V002 → OPENING_V001`

Not selected as Opening master, but retained as historical evidence:

- `P03_OPENING_V2_PROOF_REVIEW_V003`
- `P03_LIBOPENSHOT_CAMERA_MOTION_PROOF_V001`
- `P03_OPENING_V2_LIBOPENSHOT_FULL_PROOF_V001`

These experiments remain useful technical/artistic evidence and are not deleted.

## Lock boundary

`OPENING_V001` is now the approved Opening master and should not be replaced, re-encoded, or re-timed unless the Product Owner explicitly authorizes a revision.

This approval closes the Opening selection task only.

It does **not** constitute P0.3 Gate PASS. P0.3 continues while subsequent production validates and uses the reusable pipeline on later story material.

## Next production step

Proceed to the narrative/audio material immediately after the approved Opening endpoint.

Use RC-026:

`canonical story/audio context → Chat director/edit design → contextual timeline → canonical input verification → engine implementation → scene-specific treatment → GitHub Actions render/QC → full-context PO review → targeted iteration`

The next sequence must be designed from its own story beat rather than copying Opening V001 as a fixed template.
