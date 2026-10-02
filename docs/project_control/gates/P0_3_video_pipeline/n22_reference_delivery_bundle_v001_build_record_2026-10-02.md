# N22 Reference Delivery Bundle V001｜Formal Build Record

Date: 2026-10-02

Status:

`FORMAL BUILD PASS / 5 OF 5 EXACT VERIFIED / INDEPENDENT ARTIFACT VERIFIED / GENERATION_ALLOWED=TRUE / CANDIDATE 01 NOT YET AUTHORIZED`

Bundle:

`N22_REFERENCE_DELIVERY_BUNDLE_V001`

Spec path:

`production/bundle_specs/N22_REFERENCE_DELIVERY_BUNDLE_V001.json`

Validation-only baseline:

- spec commit: `a3975de9e8e781b103936654676647d8db588a44`
- run: `36962064841`
- job: `110697691495`
- result: `VALIDATION_PASS: 5/5 exact canonical references verified`
- `BUILD_AUTHORIZED=FALSE`
- `GENERATION_ALLOWED=FALSE`
- Artifact: none

Formal build authorization:

- Product Owner explicit authorization in Chat: 2026-10-02
- authorization commit: `8cc4a9dbc959c8fa9f49d5e6a2b36649a53d58d3`
- spec revision: `V001-R2`
- `build_authorized=true`

Formal build:

- workflow: `.github/workflows/story-shot-reference-bundle-builder.yml`
- run: `36962281468`
- job: `110698343917`
- conclusion: `SUCCESS`
- builder result: `PASS: 5/5 exact canonical reference binaries verified`
- `GENERATION_ALLOWED=TRUE`
- Bundle ID: `N22_REFERENCE_DELIVERY_BUNDLE_V001`

Artifact:

- Artifact ID: `11208576712`
- size: `4,752,815 bytes`
- digest: `sha256:301a127df57e197580c0b87aa0beb7d59c2687d3edd16686c10caa8f841f5c58`
- expires: `2026-10-09T03:55:37Z`

## Independent Artifact Verification

The formal Artifact ZIP was downloaded independently after the workflow completed.

Downloaded ZIP:

- size: `4,752,815 bytes`
- SHA-256: `301a127df57e197580c0b87aa0beb7d59c2687d3edd16686c10caa8f841f5c58`
- result: `MATCH`

Archive contents:

- `delivery_manifest.json`
- `WORK_HANDOFF.md`
- `identity_primary/AST_IMG_000061__CHAR_SU_XIAOXIAO_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `identity_primary/AST_IMG_000058__CHAR_LIAO_JIAN_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `identity_secondary/AST_IMG_000062__CHAR_WEN_QINGYA_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `identity_secondary/AST_IMG_000056__CHAR_GUANG_YONG_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `scene_authority/AST_IMG_000052__SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`

Independent exact verification of all 5 PNGs:

1. `AST_IMG_000061` — size / SHA-256 / Git blob / PNG signature = PASS
2. `AST_IMG_000058` — size / SHA-256 / Git blob / PNG signature = PASS
3. `AST_IMG_000062` — size / SHA-256 / Git blob / PNG signature = PASS
4. `AST_IMG_000056` — size / SHA-256 / Git blob / PNG signature = PASS
5. `AST_IMG_000052` — size / SHA-256 / Git blob / PNG signature = PASS

Independent result:

`5/5 PASS`

## Boundary

This build proves that the formal reference package is technically valid and may be used by Work.

It does NOT itself authorize image generation.

Current boundary:

- formal Bundle: READY
- Work automatic acquisition: technically available
- Candidate 01 generation: `NOT AUTHORIZED`
- required next authority: `PRODUCT OWNER N22 CANDIDATE 01 WORK GENERATION AUTHORIZATION`
