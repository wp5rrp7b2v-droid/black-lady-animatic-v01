# N21 Reference Delivery Bundle V004｜Build Preparation

Date: 2026-10-01

Status:

`BUILDER SUPPORT IMPLEMENTED / SPEC CREATION AUTHORIZED / BUILD PENDING`

Target:

`N21 Candidate 05｜Clean Regeneration`

Bundle:

`N21_REFERENCE_DELIVERY_BUNDLE_V004`

## 1. Authority

- N21 Scene Reference Design V0.4: `PRODUCT OWNER APPROVED / LOCKED`
- Character Visual Style Reference V001: `PRODUCT OWNER APPROVED / CANONICAL / REMOTE VERIFIED`
- CONTROLLED_REFERENCE + N21 Bundle V004 Design V0.1: `PRODUCT OWNER APPROVED / LOCKED`

## 2. Builder support

Generic builder:

`scripts/story_shot_reference_bundle_builder_v1.py`

CONTROLLED_REFERENCE support commit:

`2afef948bd396dd418a7d6289124c7811f616e09`

Existing `ASSET` and `STORY_SHOT` branches were retained.

New `CONTROLLED_REFERENCE` branch validates fail closed:

- manifest path exists and is readable JSON;
- manifest reference_id;
- classification;
- approval_status;
- lifecycle;
- authority_scope;
- canonical_path;
- manifest output SHA-256;
- manifest output byte size;
- manifest output Git blob;
- optional expected width / height;
- output format = PNG;
- approved_binary SHA / bytes;
- actual canonical file SHA / bytes / Git blob;
- actual PNG signature / dimensions;
- byte-identical artifact copy.

## 3. Locked V004 formal reference set

### REF-01

`AST_IMG_000052`

Purpose:

`CASTLE ENTRANCE / THRESHOLD SPACE AUTHORITY ONLY`

### REF-02

`CHARACTER_VISUAL_STYLE_REFERENCE_V001`

Purpose:

`CHARACTER VISUAL STYLE ONLY`

Canonical path:

`production/style_references/character_visual/CHARACTER_VISUAL_STYLE_REFERENCE_V001.png`

Manifest:

`production/style_references/character_visual/CHARACTER_VISUAL_STYLE_REFERENCE_V001.manifest.json`

Exact identity:

- 1536×1024
- 1301730 bytes
- SHA-256 `8d650483b6e082a80d41d93e14c7957595c451097aac63f3c84cbcc1ddc7ce41`
- Git blob `216b1739db17cb3b183d613e4aefa6374d1088e2`

## 4. Explicit exclusions

Do not deliver:

- N03;
- N20;
- any complete Story Shot;
- any named-character Character Sheet;
- A07;
- N21 Candidate 01–04.

## 5. Required build result

Before Candidate 05 may be sent to Work:

`PASS: 2/2 exact canonical reference binaries verified`

and:

`GENERATION_ALLOWED=TRUE`

Then Chat must independently inspect:

- workflow conclusion;
- Run / Job / Artifact IDs;
- Artifact digest;
- delivery_manifest.json;
- both enclosed PNG identities.

## 6. Current boundary

This authorization covers:

- builder support implementation;
- V004 spec creation;
- GitHub Actions build;
- exact verification.

It does not authorize:

- Candidate 05 generation;
- Candidate 06;
- N22;
- canonical Story Shot publication;
- Story Shot registration.

Next after successful verification:

`Prepare N21 Candidate 05 Work generation instruction for separate Product Owner authorization`
