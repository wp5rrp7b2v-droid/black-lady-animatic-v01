# CONTROLLED_REFERENCE Delivery Support + N21 Bundle V004 Design V0.1

Date: 2026-10-01

Status:

`PRODUCT OWNER APPROVED / LOCKED / BUILDER SUPPORT + SPEC COMPLETED / FORMAL BUILD NOT AUTHORIZED`

Target:

`N21｜Cohort Enters — Into the Unknown`

Future candidate:

`N21 Candidate 05｜Clean Regeneration`

Future bundle:

`N21_REFERENCE_DELIVERY_BUNDLE_V004`

## 1. Design purpose

N21 Candidate 04 proved that a complete approved Story Shot can transmit unwanted shot content when used as a style reference.

The replacement strategy is now locked:

`SCENE AUTHORITY + STYLE-ONLY CONTROLLED REFERENCE`

No complete Story Shot will be used as the human-style generation input.

## 2. New delivery source type

Add one explicit P0.3 delivery source type:

`CONTROLLED_REFERENCE`

Purpose:

deliver a canonically published, provenance-bound production reference that is not semantically an Entity Asset and not a Story Shot.

This does not alter or silently extend the P0.2 Entity / Asset Registry schema.

A CONTROLLED_REFERENCE must be validated against:

- canonical path;
- canonical provenance manifest;
- approval status;
- lifecycle;
- authority scope;
- SHA-256;
- byte size;
- Git blob;
- readable PNG signature and dimensions.

Fail closed on any mismatch.

## 3. Locked CONTROLLED_REFERENCE

Reference:

`CHARACTER_VISUAL_STYLE_REFERENCE_V001`

Classification:

`P0.3_CONTROLLED_PRODUCTION_REFERENCE`

Authority scope:

`CHARACTER_VISUAL_STYLE_ONLY`

Canonical PNG:

`production/style_references/character_visual/CHARACTER_VISUAL_STYLE_REFERENCE_V001.png`

Canonical manifest:

`production/style_references/character_visual/CHARACTER_VISUAL_STYLE_REFERENCE_V001.manifest.json`

Exact identity:

- dimensions: `1536 × 1024`
- bytes: `1301730`
- SHA-256: `8d650483b6e082a80d41d93e14c7957595c451097aac63f3c84cbcc1ddc7ce41`
- Git blob: `216b1739db17cb3b183d613e4aefa6374d1088e2`
- approval: `PRODUCT_OWNER_APPROVED`
- lifecycle: `CURRENT`

It may control only:

- facial rendering language;
- skin treatment;
- hair realism;
- adult age variation;
- cinematic human realism;
- clothing / fabric material rendering.

It must not control:

- named-character identity;
- complete outfit;
- complete body pose;
- group composition;
- scene;
- Story Shot composition.

## 4. N21 Bundle V004 formal reference set

The formal generation input set is locked to exactly two references.

### REF-01｜Castle Entrance Scene Master

Reference ID:

`AST_IMG_000052`

Source type:

`ASSET`

Role:

`SCENE_MASTER`

Authority:

`SPACE / ARCHITECTURE / OPEN-DOOR THRESHOLD FACTS ONLY`

Canonical path:

`production/image_library/scene_masters/castle_entrance/SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`

Expected SHA-256:

`d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961`

Expected bytes:

`2305753`

Expected Git blob:

`e4dafe096f5c5c8782257030a5a659aeec7808f9`

### REF-02｜Character Visual Style Reference V001

Reference ID:

`CHARACTER_VISUAL_STYLE_REFERENCE_V001`

Source type:

`CONTROLLED_REFERENCE`

Authority:

`CHARACTER_VISUAL_STYLE_ONLY`

Canonical path:

`production/style_references/character_visual/CHARACTER_VISUAL_STYLE_REFERENCE_V001.png`

Manifest path:

`production/style_references/character_visual/CHARACTER_VISUAL_STYLE_REFERENCE_V001.manifest.json`

Expected SHA-256:

`8d650483b6e082a80d41d93e14c7957595c451097aac63f3c84cbcc1ddc7ce41`

Expected bytes:

`1301730`

Expected Git blob:

`216b1739db17cb3b183d613e4aefa6374d1088e2`

## 5. Explicit exclusions

Do not include in Bundle V004:

- N03;
- N20;
- any complete Story Shot;
- Ning Qiushui Character Sheet;
- Jun Luyuan Character Sheet;
- any named-character Character Sheet;
- N21 Candidate 01;
- N21 Candidate 02;
- N21 Candidate 03;
- N21 Candidate 04;
- A07;
- unrelated castle interiors.

Candidate 01–04 remain:

`NEGATIVE DIRECTOR LESSONS ONLY`

They are not generation inputs, edit bases, style inputs or composition references.

## 6. Candidate 05 generation mode

If later authorized:

`N21 Candidate 05 = CLEAN REGENERATION`

It must not edit Candidate 04 or any earlier N21 candidate.

The N21 V0.4 narrative scope remains unchanged:

`THRESHOLD TRANSITION + UNKNOWN-SPACE MOOD`

Character visual-style continuity remains a hard Director gate.

## 7. Generic Bundle Builder design change

The generic builder may be extended to recognize:

`source_type = CONTROLLED_REFERENCE`

The implementation must not weaken existing ASSET / STORY_SHOT checks.

For CONTROLLED_REFERENCE, validation must independently verify:

1. the canonical PNG exists;
2. the sidecar manifest exists;
3. manifest reference_id matches spec reference_id;
4. manifest classification = `P0.3_CONTROLLED_PRODUCTION_REFERENCE`;
5. manifest approval_status = `PRODUCT_OWNER_APPROVED`;
6. manifest lifecycle = `CURRENT`;
7. manifest authority_scope matches the spec;
8. manifest output path matches canonical_path;
9. PNG SHA-256 matches both manifest and bundle spec;
10. PNG byte size matches both manifest and bundle spec;
11. Git blob matches both manifest and bundle spec;
12. PNG signature and dimensions are readable;
13. copied Artifact binary remains byte-identical.

Any mismatch:

`FAIL CLOSED / GENERATION_ALLOWED=FALSE`

## 8. Artifact layout

Future V004 Artifact:

`N21_REFERENCE_DELIVERY_BUNDLE_V004/`

contains:

- `delivery_manifest.json`
- `WORK_HANDOFF.md`
- `scene_authority/AST_IMG_000052__SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`
- `character_visual_style_authority/CHARACTER_VISUAL_STYLE_REFERENCE_V001.png`

Product Owner manual reference upload:

`0`

Transport remains:

`GitHub Actions → Artifact → Work automatic acquisition`

## 9. Required build result

Before Work may generate Candidate 05:

`PASS: 2/2 EXACT CANONICAL REFERENCES VERIFIED`

and:

`GENERATION_ALLOWED=TRUE`

The two references must have separate authority semantics:

- Scene Master = spatial facts;
- Style Reference = human visual language only.

## 10. Current authorization boundary

Approved / locked now:

- explicit `CONTROLLED_REFERENCE` delivery semantics;
- exact two-reference Bundle V004 design;
- exclusion of N03 / N20 / all prior N21 candidates;
- fail-closed validation contract.

Completed after separate Product Owner authorization:

- generic builder CONTROLLED_REFERENCE support;
- builder/workflow build_authorization gate;
- V004 bundle spec creation;
- validation-only 2/2 canonical reference check.

Not authorized yet:

- formal V004 GitHub Actions build;
- Work generation;
- Candidate 05;
- N22.

Current formal Spec: `production/bundle_specs/N21_REFERENCE_DELIVERY_BUNDLE_V004.json` / `build_authorized=false`.

Validation-only run: `36826494510` / `2/2 PASS` / `GENERATION_ALLOWED=FALSE` / no Artifact.

Next:

`Product Owner authorization → Formal N21_REFERENCE_DELIVERY_BUNDLE_V004 Build + Exact Verification`

A separate Product Owner authorization is required before formal Build.
