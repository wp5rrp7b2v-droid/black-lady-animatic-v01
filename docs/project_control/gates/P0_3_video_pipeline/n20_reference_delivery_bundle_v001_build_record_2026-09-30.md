# N20 Reference Delivery Bundle V001｜Build Record

Status: `PASS / 5 OF 5 EXACT CANONICAL REFERENCES VERIFIED / GENERATION_ALLOWED=TRUE`

Date: 2026-09-30

## Authority

- N20 Scene Reference Design V0.1: PRODUCT OWNER APPROVED / LOCKED
- N20 Reference Delivery Bundle Design V0.1: PRODUCT OWNER APPROVED / LOCKED
- Bundle Spec: `production/bundle_specs/N20_REFERENCE_DELIVERY_BUNDLE_V001.json`
- Spec commit: `c3ac5d3d848a8823a13770636a033eb2636e68e9`

## Build

- builder: `STORY_SHOT_REFERENCE_BUNDLE_BUILDER_V1`
- workflow: `.github/workflows/story-shot-reference-bundle-builder.yml`
- workflow run: `36654654071`
- job: `109696257939`
- result: `SUCCESS`
- artifact: `N20_REFERENCE_DELIVERY_BUNDLE_V001`
- artifact ID: `11072080675`
- artifact ZIP size: `8701679`
- artifact digest: `sha256:203f866487808d99aeb7a408a91e5c599c919b889372444e78e1fbc3d11b3230`
- expiration: `2026-10-07T01:20:53Z`

## Reference verification

1. `AST_IMG_000060` — Ning Character Reference Sheet — PASS
2. `AST_IMG_000037` — Ning REAR_3Q_RIGHT V002 — PASS
3. `AST_IMG_000057` — Jun Character Reference Sheet — PASS
4. `AST_IMG_000064` — Jun REAR_3Q_LEFT V001 — PASS
5. `AST_IMG_000052` — Castle Entrance Scene Master / DAY_DOOR_OPEN — PASS

Builder output:

`PASS: 5/5 exact canonical reference binaries verified`

`GENERATION_ALLOWED=TRUE`

## Independent Artifact verification

Chat downloaded the produced Artifact ZIP and independently verified:

- downloaded ZIP SHA-256 equals GitHub artifact digest;
- manifest bundle_id = `N20_REFERENCE_DELIVERY_BUNDLE_V001`;
- target shot = `N20`;
- target candidate = `N20 Candidate 01`;
- reference_count = `5`;
- all_reference_checks_pass = `true`;
- generation_allowed = `true`;
- manual_product_owner_reference_upload = `0`;
- all five delivered PNGs match the manifest's expected byte size;
- all five delivered PNGs match expected SHA-256;
- all five delivered PNGs match expected Git blob;
- all five PNG signatures valid.

Independent result:

`5/5 PASS`

## Production boundary

`N20_REFERENCE_DELIVERY_BUNDLE_V001 = READY FOR WORK`

No N20 candidate has been generated in this step.

Next:

`Work automatic Artifact acquisition → revalidate delivery_manifest.json → generate exactly N20 Candidate 01 → stop for Product Owner review`.
