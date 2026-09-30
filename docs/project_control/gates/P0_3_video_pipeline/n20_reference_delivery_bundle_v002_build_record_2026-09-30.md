# N20 Reference Delivery Bundle V002｜Build Record

Status: `PASS / 5 OF 5 EXACT CANONICAL REFERENCES VERIFIED / GENERATION_ALLOWED=TRUE`

Date: 2026-09-30

## Purpose

`CHARACTER CONTINUITY REINFORCEMENT`

V002 supersedes V001 for future N20 generation.

V001 remains historical evidence.

## Authority

- N20 Scene Reference Design V0.1: PRODUCT OWNER APPROVED / LOCKED
- N20 Reference Delivery Bundle Design V0.2: PRODUCT OWNER APPROVED / LOCKED
- Bundle Spec: `production/bundle_specs/N20_REFERENCE_DELIVERY_BUNDLE_V002.json`
- Spec commit: `67c316246fd76b5d039148d524c587ef67899617`

## Reference set

1. `AST_IMG_000060` — Ning Character Reference Sheet
2. `AST_IMG_000057` — Jun Character Reference Sheet
3. `N19` — canonical current-production visual continuity
4. `AST_IMG_000037` — Ning REAR_3Q_RIGHT V002
5. `AST_IMG_000064` — Jun REAR_3Q_LEFT V001

Scene Master `AST_IMG_000052` remains canonical scene authority but is intentionally not a V002 generation image input.

## Build

- builder: `STORY_SHOT_REFERENCE_BUNDLE_BUILDER_V1`
- workflow run: `36658459273`
- job: `109707734342`
- workflow result: `SUCCESS`
- artifact: `N20_REFERENCE_DELIVERY_BUNDLE_V002`
- artifact ID: `11073610356`
- artifact ZIP size: `8448179`
- artifact digest: `sha256:ff3ab2ba9b22bad988cd201972a27236b2a9f7c2730d4109680664ebabcfd4bd`
- expiration: `2026-10-07T02:08:51Z`

Builder output:

`PASS: 5/5 exact canonical reference binaries verified`

`GENERATION_ALLOWED=TRUE`

## Independent verification

Chat independently downloaded the Artifact ZIP.

Results:

- downloaded ZIP SHA-256 equals GitHub Artifact digest: PASS;
- bundle_id = `N20_REFERENCE_DELIVERY_BUNDLE_V002`: PASS;
- reference_count = `5`: PASS;
- generation_allowed = `true`: PASS;
- overall_result = `PASS`;
- AST_IMG_000060 byte size / SHA-256 / Git blob / PNG signature: PASS;
- AST_IMG_000057 byte size / SHA-256 / Git blob / PNG signature: PASS;
- N19 byte size / SHA-256 / Git blob / PNG signature: PASS;
- AST_IMG_000037 byte size / SHA-256 / Git blob / PNG signature: PASS;
- AST_IMG_000064 byte size / SHA-256 / Git blob / PNG signature: PASS.

Independent result:

`5/5 PASS`

## Production boundary

`N20_REFERENCE_DELIVERY_BUNDLE_V002 = READY FOR WORK`

Authorized next:

`N20 Candidate 04｜Clean Regeneration`

Candidate 01–03 remain rejected and must not be used as image references or edit bases.
