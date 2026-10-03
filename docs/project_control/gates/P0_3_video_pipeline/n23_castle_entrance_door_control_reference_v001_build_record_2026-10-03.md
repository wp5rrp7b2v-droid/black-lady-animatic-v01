# N23_CASTLE_ENTRANCE_DOOR_CONTROL_REFERENCE_V001｜Deterministic Build Record

Date:

`2026-10-03`

Status:

`BUILD PASS / TWO-RUN BYTE IDENTITY PASS / PRODUCT OWNER VISUAL REVIEW REQUIRED / NOT YET CANONICAL`

Reference:

`N23_CASTLE_ENTRANCE_DOOR_CONTROL_REFERENCE_V001`

Source:

`AST_IMG_000052｜SCENE_CASTLE_ENTRANCE｜SCENE_MASTER｜DAY_DOOR_OPEN`

Approved crop authority:

`Exact Crop Plan V0.2 / PRODUCT OWNER APPROVED / LOCKED`

Locked crop rectangle:

- x1 = 615
- y1 = 75
- x2 = 930
- y2 = 1340
- resulting size = 315 × 1265
- output mode = RGB
- resize = forbidden

## GitHub Actions proof

Workflow:

`N23 Door Control Reference V001 Determinism Proof`

Run:

`37106490989`

Job:

`111155937737`

Trigger commit:

`5966cd3f304dad90c2a78f429b74cb89bb786fdd`

Result:

`SUCCESS`

Artifact:

`N23_CASTLE_ENTRANCE_DOOR_CONTROL_REFERENCE_V001_TWO_RUN_PROOF`

Artifact ID:

`11267754516`

Artifact size:

`1,096,665 bytes`

Artifact digest:

`sha256:0507f74362e8f35a89c15329731ead15344c3632bd20de1f6745b4195c3263fb`

Artifact expiry:

`2026-10-10T07:29:20Z`

## Runtime pinning

- Python: `3.12.14`
- Pillow: `11.3.0`

## Source verification

Expected / actual:

- source SHA-256: `d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961`
- source bytes: `2,305,753`
- source dimensions: `941 × 1672`
- source mode: `RGB`

Result:

`PASS`

## Two-run exact verification

Run A:

- SHA-256: `5718ce8c68069ca41143d666406a8c4cec3c285837a861337da758769bbfb652`
- bytes: `546,543`
- dimensions: `315 × 1265`
- mode: `RGB`

Run B:

- SHA-256: `5718ce8c68069ca41143d666406a8c4cec3c285837a861337da758769bbfb652`
- bytes: `546,543`
- dimensions: `315 × 1265`
- mode: `RGB`

Binary comparison:

`SHA MATCH / BYTE COUNT MATCH / CMP PASS`

Overall:

`TWO_RUN_BYTE_IDENTITY = PASS`

## Authorization boundary

This build proves that the approved crop plan can be reproduced deterministically.

It does NOT yet authorize:

- canonical publication of the controlled reference;
- Bundle V003 Design / Spec;
- Candidate 03 Work generation;
- Candidate 04;
- N24.

Next gate:

`PRODUCT OWNER VISUAL REVIEW OF THE BUILT DOOR CONTROL REFERENCE`
