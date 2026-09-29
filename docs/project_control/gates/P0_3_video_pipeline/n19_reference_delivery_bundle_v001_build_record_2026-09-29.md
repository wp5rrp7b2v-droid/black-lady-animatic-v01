# N19 Reference Delivery Bundle V001｜Build Record

Status: `BUILT / 5 OF 5 EXACT VERIFICATION PASS / INDEPENDENT ARTIFACT VERIFICATION PASS / GENERATION_ALLOWED=TRUE`

Date: 2026-09-29

## Build identity

- bundle_id: `N19_REFERENCE_DELIVERY_BUNDLE_V001`
- target_shot_id: `N19`
- target_candidate: `N19 Candidate 01`
- source commit / spec commit: `214af57acd778a208361cc5a73a2bd68052736ff`
- workflow: `.github/workflows/story-shot-reference-bundle-builder.yml`
- workflow run: `36576705556`
- job: `109434070260`
- builder: `STORY_SHOT_REFERENCE_BUNDLE_BUILDER_V1`

## Artifact

- artifact name: `N19_REFERENCE_DELIVERY_BUNDLE_V001`
- artifact ID: `11037987128`
- artifact size: `8182280` bytes
- artifact digest: `sha256:b6aa9142bbeded26909c84faacbf69e93dde63f8ba0d3508df54d44402674276`
- created: `2026-09-29T13:39:41Z`
- expires: `2026-10-06T13:39:40Z`
- retention: `7 days`

## Canonical reference verification

Builder result:

`PASS: 5/5 exact canonical reference binaries verified`

`GENERATION_ALLOWED=TRUE`

Verified references:

1. `AST_IMG_000060` — Ning Qiushui Character Reference Sheet
2. `AST_IMG_000057` — Jun Luyuan Character Reference Sheet
3. `N17` — Blood-Door Warning canonical Story Shot
4. `N18` — Clear-Sky Doubt canonical Story Shot
5. `AST_IMG_000052` — Castle Entrance Scene Master / DAY_DOOR_OPEN

For all five references:

- expected SHA-256 = computed SHA-256;
- expected byte_size = actual byte_size;
- expected Git blob = actual Git blob;
- PNG signature = PASS;
- bundle copy byte-identical = PASS.

## Independent post-artifact verification

The downloaded Artifact ZIP was independently opened after upload.

Result:

`INDEPENDENT_ARTIFACT_VERIFICATION=PASS`

The Artifact contains exactly 7 files:

- `WORK_HANDOFF.md`
- `delivery_manifest.json`
- 5 canonical PNG references

The downloaded ZIP SHA-256 independently matched the GitHub Actions artifact digest:

`b6aa9142bbeded26909c84faacbf69e93dde63f8ba0d3508df54d44402674276`

All five PNGs were independently re-hashed from the downloaded ZIP and matched their locked SHA-256 and byte sizes.

## Current boundary

`N19_REFERENCE_DELIVERY_BUNDLE_V001 = VERIFIED / READY FOR WORK GENERATION`

Authorized:

- Work automatic Artifact acquisition;
- Artifact / manifest verification;
- generation of exactly `N19 Candidate 01`.

Not authorized:

- N20 generation;
- Story Shot Registration;
- Canonical Publication;
- Project Control closeout for N19 before Product Owner image approval.
