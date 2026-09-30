# N20｜Reference Delivery Bundle Design V0.2

Status: `PRODUCT OWNER APPROVED / LOCKED / BUNDLE BUILD AUTHORIZED`

Date: 2026-09-30

Purpose:

`CHARACTER CONTINUITY REINFORCEMENT AFTER V001 CANDIDATE FAILURES`

Target bundle:

`N20_REFERENCE_DELIVERY_BUNDLE_V002`

Target generation after approval + successful build:

`N20 Candidate 04｜Clean Regeneration`

Supersedes for future N20 generation:

`N20_REFERENCE_DELIVERY_BUNDLE_V001`

V001 remains historical evidence and must not be deleted.

## 1. Trigger / observed failure evidence

N20 Candidate 01:

`REJECTED — WALKING DIRECTION / SPATIAL AXIS FAILURE`

N20 Candidate 02:

`REJECTED — RELATIONAL WALKING / CHARACTER CONTINUITY / INTERIOR LIGHTING FAILURE`

N20 Candidate 03:

`REJECTED — CHARACTER IDENTITY / VISUAL CONTINUITY FAILURE`

Candidate 03 improved:

-同行关系;
- slow conversational walking;
- gait phase separation;
- dim warm interior lighting;
- removal of direct exterior sunlight;
- limited transition-zone depth.

However both characters no longer read reliably as the approved Ning Qiushui / Jun Luyuan production identities. The failure is therefore no longer treated as a prompt-only problem.

## 2. V0.2 reference-strategy decision

V001 relied on:

- two Character Reference Sheets;
- two rear-3Q atomic anchors;
- Castle Entrance Scene Master.

That set was sufficient for angle / scene construction but did not preserve the actual approved on-screen character appearance strongly enough across repeated clean generations.

V0.2 changes one reference:

`REMOVE AST_IMG_000052 Scene Master from generation image inputs`

and replaces it with:

`ADD N19 Canonical Story Shot as current-production visual continuity authority`

The reference count remains:

`5`

## 3. Canonical reference set V002

### REF-01｜Ning Qiushui Character Reference Sheet

- reference_id: `AST_IMG_000060`
- source_type: `ASSET`
- entity_id: `CHAR_NING_QIUSHUI`
- role: `CHARACTER_REFERENCE_SHEET`
- asset_class: `DERIVED_REFERENCE`
- authority_class: `DERIVED`
- approval / lifecycle / resolver: `APPROVED / CURRENT / DEFAULT`
- canonical_path: `production/image_library/derived_reference_sheets/ning_qiushui/CHAR_NING_QIUSHUI_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- SHA-256: `15ec6c2682da0fe2502267bde21e9bc0bd7104bbf3e6041521121cc69a0e77be`
- byte_size: `1123635`
- Git blob: `b674733242ab5d603dc42c53b8f7582003064499`
- destination_group: `character_authority`
- authority_purpose: `NING_PRIMARY_IDENTITY_WARDROBE_CONTINUITY`

Responsibility:

- Ning identity;
- face / head proportions;
- hairstyle;
- wardrobe;
- body proportion.

### REF-02｜Jun Luyuan Character Reference Sheet

- reference_id: `AST_IMG_000057`
- source_type: `ASSET`
- entity_id: `CHAR_JUN_LUYUAN`
- role: `CHARACTER_REFERENCE_SHEET`
- asset_class: `DERIVED_REFERENCE`
- authority_class: `DERIVED`
- approval / lifecycle / resolver: `APPROVED / CURRENT / DEFAULT`
- canonical_path: `production/image_library/derived_reference_sheets/jun_luyuan/CHAR_JUN_LUYUAN_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- SHA-256: `e8a0410cfc176ec9d6446b84f89b2c12d0683ec32b927c90353e850c416d909e`
- byte_size: `969995`
- Git blob: `d11db79f4ceab2bb52139bfb8805f7c8f09b0cfc`
- destination_group: `character_authority`
- authority_purpose: `JUN_PRIMARY_IDENTITY_WARDROBE_CONTINUITY`

Responsibility:

- Jun identity;
- face / head proportions;
- hairstyle;
- wardrobe;
- body proportion.

### REF-03｜N19 Canonical Story Shot

- reference_id: `N19`
- source_type: `STORY_SHOT`
- shot_id: `N19`
- title: `Conditions Can Change — Entrance Response`
- approval / lifecycle: `APPROVED / CURRENT`
- canonical_path: `production/image_library/approved/story_shots/N19_CONDITIONS_CAN_CHANGE_APPROVED_V001.png`
- SHA-256: `5cc7e09716adf91a56b52f4714cc84945c73a4cbc5ed6162d90f2f3a9b351c7a`
- byte_size: `2052606`
- dimensions: `941x1672`
- Git blob: `c842ad1a0b84b2d504b1e681dd327b01bb57c159`
- destination_group: `production_visual_continuity`
- authority_purpose: `CURRENT_ON_SCREEN_CHARACTER_APPEARANCE_WARDROBE_BODY_PROPORTION_RENDER_STYLE_CONTINUITY`

N19 controls:

- the actual current-production appearance of Ning and Jun;
- current hair mass / silhouette;
- current clothing appearance;
- relative body proportion;
- the established cinematic/render language of the immediately preceding approved Story Shot.

N19 MUST NOT control:

- pose;
- shoulder contact;
- shared outward gaze;
- doorway pause;
- camera angle;
- character placement;
- framing;
- exterior-dominant composition.

Hard interpretation:

`COPY APPEARANCE CONTINUITY, NOT POSE OR COMPOSITION`

### REF-04｜Ning Qiushui REAR_3Q_RIGHT V002

- reference_id: `AST_IMG_000037`
- source_type: `ASSET`
- entity_id: `CHAR_NING_QIUSHUI`
- role: `REAR_3Q_RIGHT`
- asset_class: `ATOMIC`
- authority_class: `AUXILIARY`
- approval / lifecycle / resolver: `APPROVED / CURRENT / DEFAULT`
- canonical_path: `production/image_library/character_references/ning_qiushui/CHAR_NING_QIUSHUI_REAR_3Q_RIGHT_DEFAULT_DEFAULT_V002.png`
- SHA-256: `c56e30657c65942899caa1f5e36e21f8f835a5835325fa68c70b64d754fa70d2`
- byte_size: `2395616`
- Git blob: `f03493d845b3f1c7194075781217d97f1e1e9b35`
- destination_group: `character_angle_authority`
- authority_purpose: `NING_REAR_3Q_IDENTITY_ORIENTATION_SUPPORT`

Responsibility:

- rear-side head silhouette;
- rear-3Q orientation;
- body-direction support.

It does not override N19 / Character Reference Sheet appearance.

### REF-05｜Jun Luyuan REAR_3Q_LEFT V001

- reference_id: `AST_IMG_000064`
- source_type: `ASSET`
- entity_id: `CHAR_JUN_LUYUAN`
- role: `REAR_3Q_LEFT`
- asset_class: `ATOMIC`
- authority_class: `AUXILIARY`
- approval / lifecycle / resolver: `APPROVED / CURRENT / DEFAULT`
- canonical_path: `production/image_library/character_references/jun_luyuan/CHAR_JUN_LUYUAN_REAR_3Q_LEFT_DEFAULT_DEFAULT_V001.png`
- SHA-256: `97ad38c259274eced5be61035cda4c28df72babe084fc452fbbc927a2a6da21e`
- byte_size: `1941468`
- Git blob: `6ebfadfa333159f1ae3871f4a61fd39526360fee`
- destination_group: `character_angle_authority`
- authority_purpose: `JUN_REAR_3Q_IDENTITY_ORIENTATION_SUPPORT`

Responsibility:

- rear-side head silhouette;
- rear-3Q orientation;
- body-direction support.

It does not override N19 / Character Reference Sheet appearance.

## 4. Why Scene Master is removed from generation inputs

`AST_IMG_000052` remains canonical scene authority in Project Control and N20 Scene Reference Design.

It is removed only from the five-image generation input set.

Reason:

Current highest-risk failure is:

`CHARACTER IDENTITY LOSS`

not:

`SCENE IDENTITY LOSS`

Candidate 03 already demonstrated that the environment can be constrained successfully through the Work execution lock:

- dim warm castle interior;
- no direct exterior sunlight on walking floor or bodies;
- limited entrance-to-interior transition depth;
- no full hall establishment;
- no long corridor;
- Gothic stone architecture;
- warm wall / candle / chandelier lighting.

Within the five-reference input ceiling, N19 contributes more production-critical information than the Scene Master.

## 5. Scene facts remain locked without Scene Master image input

Removing the Scene Master from the generation Bundle does NOT authorize scene redesign.

N20 environment remains:

`CASTLE_ENTRANCE → INTERIOR TRANSITION ZONE`

Hard scene locks:

- interior Gothic stone architecture continuous with the castle;
- characters have moved beyond the direct entrance sunlight zone;
- no direct exterior sunbeam across floor;
- no direct sunlight illuminating character backs;
- primary illumination = dim warm wall sconces / candles / chandeliers;
- only weak ambient evidence of brighter exterior may remain far behind;
- no full First Hall establishment;
- no mural corridor;
- no long repetitive corridor;
- no new architectural theme;
- no daylight-dominated interior.

## 6. Candidate 04 performance lock

Target:

`N20 Candidate 04｜Clean Regeneration`

The successful Candidate 03 relational improvements must be preserved conceptually, not pixel-wise:

- slow conversational walking;
- Ning only slightly ahead;
- difference = approximately half a shoulder / small natural offset, not a full stride;
- Jun is同行, not追赶;
- both travel at the same apparent speed;
- gait phases differ naturally;
- modest step length;
- no N19 shoulder contact;
- no camera-facing turn for facial visibility;
- rear / rear-3Q conversational walking view;
- warm dim interior;
- no direct exterior sunlight.

Candidate 03 itself is NOT an image reference and is NOT an edit base.

## 7. Character identity hard gate

Before accepting composition quality, Work must compare Candidate 04 against:

- AST_IMG_000060;
- AST_IMG_000057;
- N19 canonical;
- rear-3Q anchors.

Identity must win over pose convenience.

For each character check:

### Ning Qiushui

- face / jaw contour when visible;
- hair silhouette / mass;
- black jacket design and length;
- black trousers;
- dark shoes;
- shoulder width / body proportions;
- overall mature, restrained character read.

### Jun Luyuan

- face / jaw contour when visible;
- hair silhouette / mass;
- light blue-gray jacket;
- white inner layer;
- dark blue jeans;
- canonical dark footwear;
- shoulder width / body proportions;
- younger, less hardened character read.

Any obvious redesign of either person:

`FAIL`

## 8. Authority precedence V002

1. S02-B Director Shot Design V0.2
2. N20 Scene Reference Design V0.1
3. AST_IMG_000060 — Ning identity
4. AST_IMG_000057 — Jun identity
5. N19 canonical — current on-screen appearance / wardrobe / proportion / render-language continuity
6. AST_IMG_000037 — Ning rear-3Q orientation support
7. AST_IMG_000064 — Jun rear-3Q orientation support

Conflict rules:

- Character Reference Sheets win identity conflicts.
- N19 reinforces actual current-production appearance and style.
- Rear-3Q anchors control orientation only; they may not redesign the characters.
- Director / Scene Reference locks control action, composition and scene facts.
- N19 pose / shoulder contact / outward gaze must never be copied into N20.

## 9. Explicit exclusions

Do not include in `N20_REFERENCE_DELIVERY_BUNDLE_V002`:

- AST_IMG_000052 as a generation image input;
- N18;
- N17;
- Candidate 01;
- Candidate 02;
- Candidate 03;
- any rejected / working N20 candidate;
- superseded Ning / Jun anchors;
- Neil references;
- A03 / A05 / A06 / A07;
- First Hall Scene Master;
- mural corridor references;
- MANOR_GATE Scene Master;
- N21–N23;
- internet / non-canonical imagery.

## 10. Planned artifact layout

`N20_REFERENCE_DELIVERY_BUNDLE_V002/`

- `delivery_manifest.json`
- `WORK_HANDOFF.md`
- `character_authority/AST_IMG_000060__CHAR_NING_QIUSHUI_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `character_authority/AST_IMG_000057__CHAR_JUN_LUYUAN_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `production_visual_continuity/N19__N19_CONDITIONS_CAN_CHANGE_APPROVED_V001.png`
- `character_angle_authority/AST_IMG_000037__CHAR_NING_QIUSHUI_REAR_3Q_RIGHT_DEFAULT_DEFAULT_V002.png`
- `character_angle_authority/AST_IMG_000064__CHAR_JUN_LUYUAN_REAR_3Q_LEFT_DEFAULT_DEFAULT_V001.png`

Retention target:

`7 days`

Product Owner manual reference upload:

`0`

Transport:

`GitHub Actions → short-lived Artifact → Work automatic acquisition`

Codex:

`NOT PART OF THIS STORY SHOT BUNDLE PATH`

## 11. Planned Bundle Spec

After Product Owner approval:

`production/bundle_specs/N20_REFERENCE_DELIVERY_BUNDLE_V002.json`

Use only:

`.github/workflows/story-shot-reference-bundle-builder.yml`

No N20-specific workflow may be created.

## 12. Build validation

Build must fail closed unless all 5/5 references pass:

- exact source identity;
- APPROVED / CURRENT state;
- canonical path;
- byte size;
- SHA-256;
- Git blob;
- PNG signature;
- readable dimensions;
- byte-identical artifact copy;
- post-assembly revalidation.

Required:

`PASS: 5/5 exact canonical reference binaries verified`

then:

`GENERATION_ALLOWED=TRUE`

## 13. Current boundary

Current disposition:

`N20 REFERENCE DELIVERY BUNDLE DESIGN V0.2 = PRODUCT OWNER APPROVED / LOCKED / BUNDLE BUILD AUTHORIZED`

Authorized next:

- create V002 Bundle Spec;
- run Generic Story Shot Reference Bundle Builder V1;
- verify 5/5 canonical inputs;
- if and only if `GENERATION_ALLOWED=TRUE`, hand off to Work for N20 Candidate 04.

Still not authorized:

- Candidate 04 generation before verification;
- N21 production;
- Story Shot publication / registration before Product Owner approves a candidate.


## 14. Product Owner approval

On 2026-09-30, the Product Owner explicitly approved N20 Reference Delivery Bundle Design V0.2.

Authorized next steps:

1. create `production/bundle_specs/N20_REFERENCE_DELIVERY_BUNDLE_V002.json`;
2. run the existing Generic Story Shot Reference Bundle Builder V1;
3. verify all 5 canonical inputs exactly.

Image generation remains blocked until Bundle verification returns:

`GENERATION_ALLOWED=TRUE`
