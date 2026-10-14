# S02-B V006 NEW-02｜Exact Binary Canonical Publication & Story Shot Registration Closeout

Date: 2026-10-14

**FINAL: PO APPROVED / ORIGINAL PNG EXACT CANONICAL PUBLISHED / STORY SHOT REGISTERED / REGISTRATION EXACT VERIFIED / REVIEW BRANCH ONLY / NO VIDEO CHANGE / NO MAIN MERGE**

## Product Owner authorization

The Product Owner explicitly approved NEW-02 Candidate 01 Exact Binary Canonical Publication, Story Shot Registration and Registration Verification while prohibiting re-encoding, changes to any S02-B video master, or merging main. Approval is scoped to the previously exact-verified upload with SHA-256 `d1866a667d7a24b8c5ae5b7670486b8b312e6f4a8fbce457763668e84d843bd4`, Git blob `d8feba3692ebe25afd0e51f5e3ab32358ea19ded`.

## Identity and provenance

- Shot ID: `S02B_V006_CROWD_INTERIOR_SIDE_DEPTH_TEST_01`.
- Approved source Chat filename: `城堡幽暗拱廊中的穿行人群(1).png`.
- Actual GitHub staging filename: `城堡幽暗拱廊中的穿行人群.png`.
- Final canonical location: `production/image_library/approved/story_shots/S02B_V006_NEW02_CROWD_INTERIOR_SIDE_DEPTH_APPROVED_V001.png`.
- Format: PNG; dimensions: **941 × 1672**; size **1,963,410 bytes**.
- SHA-256: **`d1866a667d7a24b8c5ae5b7670486b8b312e6f4a8fbce457763668e84d843bd4`**.
- Git blob: **`d8feba3692ebe25afd0e51f5e3ab32358ea19ded`**.
- Formal source Bundle V001 GitHub Actions `38553600591` (Artifact `11887079610`) 5/5 exact references validated; N21 941×1671 PO dimension exception preserved.
- Approved original GitHub staging candidate exact intake `38558807970`, evidence Artifact `11890872274`, SUCCESS.
- Git tree exact-blob move only; the original PNG bytes were not re-encoded, resized or edited.

## Canonical publication

- Branch `review/s02b-jun-nod-insert-20261014`.
- Publication commit: **`155fd65184e578a00513042a13e0081f700868b1`**.
- Canonical PNG Git blob exactly reuses staging Git blob `d8feba3692ebe25afd0e51f5e3ab32358ea19ded`.
- Original staging PNG removed.
- Dedicated publication workflow: `.github/workflows/s02b-v006-new02-canonical-exact-publication-v001.yml`.
- Independent publication verification run: **`38567423616`**, job **`115863567880`**, **SUCCESS**.
- URL: https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/38567423616
- Publication evidence Artifact **`11895932182`**, ZIP sha256 `f90a42413f35f97d3d4d1005a55b052e8b2f8e9b644dab77683b9f925a296faf`.
- Verifier compares source blob in previous commit to canonical blob and independently recomputes SHA256, bytes, dimensions, and verifies only staging deletion + canonical addition changed.
- The previous candidate-intake workflow may re-run on staging PNG deletion and fail because its expected input is now absent; this does **not** invalidate the prior staging intake PASS. This should be improved in later pipeline design to only trigger intake on PNG addition/modification.

## Story Shot registration

- Story Shot Index: `production/story_shots/story_shot_index.jsonl`.
- Registration commit: **`35ae896fbf021209e58370c4080369280fa67e73`**.
- New shot ID: **`S02B_V006_CROWD_INTERIOR_SIDE_DEPTH_TEST_01`**.
- Registered `asset_class=STORY_SHOT`, `approval_status=APPROVED`, `lifecycle=CURRENT`.
- `scene=CASTLE_ENTRANCE_INNER_LOBBY`, characters `GENERIC_GUEST_CROWD`.
- Existing 33 Story Shot registrations preserved, new total **34**.
- Shot placement into V006 EDL (43.300–45.533 seconds) remains **provisional**. This is registration of the still asset, not authorization to render or publish the V006 video.

## Independent registration verification

- Workflow: `.github/workflows/s02b-v006-new02-story-shot-registration-verification-v001.yml`.
- Run **`38567636494`**, job **`115864296340`**, all steps **SUCCESS**.
- URL: https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/38567636494
- Evidence Artifact **`11896372489`**, ZIP sha256 **`e92af898978c4a09f86549a09f184da61ef5676a6cf47a707423ad8477f1a43d`**.
- Checked against actual registered canonical original PNG bytes:
  - 1 registered unique NEW-02 shot ID.
  - SHA256, Git blob, image dimensions and byte size all match PO-approved original.
  - All preceding 33 index rows unchanged.
  - Registration commit changes only Story Shot Index.
  - Original staging PNG absent.
  - No video master changes.

## Governance and closeout

**S02-B V006 NEW-02 Canonical Publication / Registration / Exact Registration Verification = CLOSED / PASS.**

- Repository: `wp5rrp7b2v-droid/black-lady-animatic-v01`.
- Branch: `review/s02b-jun-nod-insert-20261014`.
- `main` was **not merged**; artifacts remain on review branch.
- The source PNG, N21/N22/N23 originals, NEW-01, audio and video master have not been modified.
- Do not treat NEW-02 image approval/registration as approval of S02-B V006 edited video.

Next phase, after separately authorized: review / render S02-B V006 editorial test using NEW-01 and NEW-02 registered stills and preexisting audio, with exact continuity and PO video approval gate.
