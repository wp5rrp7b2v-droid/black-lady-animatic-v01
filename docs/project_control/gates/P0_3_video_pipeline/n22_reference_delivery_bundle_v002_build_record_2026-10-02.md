# N22 Reference Delivery Bundle V002｜Formal Build Record

Date: 2026-10-02

Status:

`FORMAL BUILD PASS / 4 OF 4 EXACT VERIFIED / INDEPENDENT ARTIFACT VERIFIED / GENERATION_ALLOWED=TRUE / CANDIDATE 02 NOT YET AUTHORIZED`

Bundle:

`N22_REFERENCE_DELIVERY_BUNDLE_V002`

Spec path:

`production/bundle_specs/N22_REFERENCE_DELIVERY_BUNDLE_V002.json`

Validation-only baseline:

- spec commit: `3f7d6c573807f139a646c46e7f0eab1a444cd123`
- run: `36965661777`
- job: `110708748486`
- result: `VALIDATION_PASS: 4/4 exact canonical references verified`
- `BUILD_AUTHORIZED=FALSE`
- `GENERATION_ALLOWED=FALSE`
- Artifact: none

Formal build authorization:

- Product Owner explicit authorization in Chat: 2026-10-02
- authorization commit: `42d48adf8841d19da51a64dadcb2e2b6e85dee7f`
- spec revision: `V002-R2`
- `build_authorized=true`

Formal build:

- workflow: `.github/workflows/story-shot-reference-bundle-builder.yml`
- run: `36982776916`
- job: `110760847742`
- conclusion: `SUCCESS`
- builder result: `PASS: 4/4 exact canonical reference binaries verified`
- `GENERATION_ALLOWED=TRUE`
- Bundle ID: `N22_REFERENCE_DELIVERY_BUNDLE_V002`

Artifact:

- Artifact ID: `11216560996`
- size: `4,115,447 bytes`
- digest: `sha256:28190d5b103b8c39409630d244aeb767d1c87930b31d24046325bd0b985e33c2`
- expires: `2026-10-09T08:13:08Z`

## Independent Artifact Verification

The formal Artifact ZIP was independently downloaded after workflow completion.

Downloaded ZIP:

- size: `4,115,447 bytes`
- SHA-256: `28190d5b103b8c39409630d244aeb767d1c87930b31d24046325bd0b985e33c2`
- result: `MATCH`

Archive contents:

- `WORK_HANDOFF.md`
- `delivery_manifest.json`
- `identity_primary/AST_IMG_000061__CHAR_SU_XIAOXIAO_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `identity_secondary/AST_IMG_000058__CHAR_LIAO_JIAN_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `identity_tertiary/AST_IMG_000056__CHAR_GUANG_YONG_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `scene_authority/AST_IMG_000052__SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`

Independent exact verification:

1. `AST_IMG_000061` — size / SHA-256 / Git blob / PNG signature = PASS
2. `AST_IMG_000058` — size / SHA-256 / Git blob / PNG signature = PASS
3. `AST_IMG_000056` — size / SHA-256 / Git blob / PNG signature = PASS
4. `AST_IMG_000052` — size / SHA-256 / Git blob / PNG signature = PASS

Independent result:

`4/4 PASS`

## Boundary

This build proves that Bundle V002 is technically valid and ready for Work acquisition.

It does NOT itself authorize image generation.

Current boundary:

- formal Bundle V002: READY
- Work automatic acquisition: technically available
- Candidate 02 generation: `NOT AUTHORIZED`
- required next authority: `PRODUCT OWNER N22 CANDIDATE 02 WORK GENERATION AUTHORIZATION`
