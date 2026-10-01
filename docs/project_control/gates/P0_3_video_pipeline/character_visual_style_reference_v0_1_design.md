# Character Visual Style Reference V0.1｜Design

Status: `DIRECTOR DESIGN LOCK / PRODUCT OWNER REVIEW REQUIRED / NOT YET BUILT`

Date: 2026-10-01

Reference ID:

`CHARACTER_VISUAL_STYLE_REFERENCE_V001`

Purpose:

Create a style-only human visual reference for N21 and similar multi-person Story Shots without transmitting a complete Story Shot composition, named-character showcase, scene background, or reusable cast / wardrobe grouping.

Authority source:

- N21 Scene Reference Design V0.4
- N21 Candidate 04 Review｜2026-10-01
- BL-D-093
- RISK-003 mitigation redesign

## 1. Core rule

`STYLE ONLY / NO SHOT CONTENT`

This reference may communicate:

- realistic human facial rendering language;
- natural skin texture;
- believable hair rendering;
- adult age variation;
- restrained cinematic human realism;
- clothing / fabric material rendering.

It must not communicate:

- a complete character identity target;
- a complete outfit;
- a complete body pose;
- a group arrangement;
- a scene;
- camera composition;
- story action;
- named-character prominence.

## 2. Construction method

The reference must be a deterministic derived contact sheet.

Allowed operations only:

1. read exact approved source PNG bytes;
2. crop fixed rectangular regions;
3. resize those crops with one documented deterministic algorithm;
4. place them on a fixed neutral canvas;
5. write one PNG;
6. record the complete provenance manifest.

Forbidden:

- image generation;
- generative fill;
- inpainting;
- face reconstruction;
- retouching;
- color correction;
- relighting;
- skin smoothing;
- sharpening;
- denoising;
- style transfer;
- wardrobe alteration;
- background synthesis.

`NO NEW VISUAL PIXELS EXCEPT CANVAS / GEOMETRIC RESAMPLING`

## 3. Source-selection principle

Do not use Ning Qiushui or Jun Luyuan.

Reason:

N21 must not reintroduce hero-pair weight or copy their current wardrobe configuration.

Do not use:

- any Story Shot;
- any Character Reference Sheet;
- Neil;
- Black Lady;
- Castle Young Master.

Use only current approved Atomic Character assets from ordinary participant characters.

## 4. Locked source set

### SRC-01｜Guang Yong facial-rendering source

- Asset ID: `AST_IMG_000010`
- Entity: `CHAR_GUANG_YONG`
- Role: `FACE_3Q_RIGHT`
- Asset Class: `ATOMIC`
- Authority: `MASTER`
- Approval / Lifecycle: `APPROVED / CURRENT`
- Path: `production/image_library/character_references/guang_yong/CHAR_GUANG_YONG_FACE_3Q_RIGHT_DEFAULT_DEFAULT_V001.png`
- SHA-256: `ee8f6e72345046f2c96376d932565533fd3c3c4a96035458dd768083a639ab4b`
- Bytes: `2928885`

Use only a partial face / hair / skin crop.

### SRC-02｜Liao Jian facial-rendering source

- Asset ID: `AST_IMG_000023`
- Entity: `CHAR_LIAO_JIAN`
- Role: `FACE_3Q_LEFT`
- Asset Class: `ATOMIC`
- Authority: `MASTER`
- Approval / Lifecycle: `APPROVED / CURRENT`
- Path: `production/image_library/character_references/liao_jian/CHAR_LIAO_JIAN_FACE_3Q_LEFT_DEFAULT_DEFAULT_V001.png`
- SHA-256: `935fa830c88ef76fbe286e96caff613e2bf8cfee7a2f23d81fa65056669f7e49`
- Bytes: `2850109`

Use only a partial face / hair / skin crop.

### SRC-03｜Su Xiaoxiao facial-rendering source

- Asset ID: `AST_IMG_000043`
- Entity: `CHAR_SU_XIAOXIAO`
- Role: `FACE_3Q_LEFT`
- Asset Class: `ATOMIC`
- Authority: `MASTER`
- Approval / Lifecycle: `APPROVED / CURRENT`
- Path: `production/image_library/character_references/su_xiaoxiao/CHAR_SU_XIAOXIAO_FACE_3Q_LEFT_DEFAULT_DEFAULT_V001.png`
- SHA-256: `dbeecd9656cdeba342717f15f7a07b53f6fb39331ed9d15a4d4cad907eb26b25`
- Bytes: `3063603`

Use only a partial face / hair / skin crop.

### SRC-04｜Wen Qingya facial-rendering source

- Asset ID: `AST_IMG_000047`
- Entity: `CHAR_WEN_QINGYA`
- Role: `FACE_3Q_LEFT`
- Asset Class: `ATOMIC`
- Authority: `MASTER`
- Approval / Lifecycle: `APPROVED / CURRENT`
- Path: `production/image_library/character_references/wen_qingya/CHAR_WEN_QINGYA_FACE_3Q_LEFT_DEFAULT_DEFAULT_V001.png`
- SHA-256: `fb1a64777052d2bf1506ab4bffe1f75dad433bd45f3caec3c25e13d115fb9c6d`
- Bytes: `2934893`

Use only a partial face / hair / skin crop.

### SRC-05｜Liao Jian clothing-material source

- Asset ID: `AST_IMG_000022`
- Entity: `CHAR_LIAO_JIAN`
- Role: `BODY_FRONT`
- Asset Class: `ATOMIC`
- Authority: `MASTER`
- Approval / Lifecycle: `APPROVED / CURRENT`
- Path: `production/image_library/character_references/liao_jian/CHAR_LIAO_JIAN_BODY_FRONT_DEFAULT_DEFAULT_V001.png`
- SHA-256: `5af9e7fccfe332b096147c2623ff9b17676b5d3b65dcc21dfee49f2958761acc`
- Bytes: `2735616`

Use only a tight shoulder / sleeve / torso-material crop.

Must exclude:

- head;
- hands;
- waist;
- complete garment silhouette;
- bag / accessory;
- full outfit combination.

### SRC-06｜Wen Qingya clothing-material source

- Asset ID: `AST_IMG_000046`
- Entity: `CHAR_WEN_QINGYA`
- Role: `BODY_FRONT`
- Asset Class: `ATOMIC`
- Authority: `MASTER`
- Approval / Lifecycle: `APPROVED / CURRENT`
- Path: `production/image_library/character_references/wen_qingya/CHAR_WEN_QINGYA_BODY_FRONT_DEFAULT_DEFAULT_V001.png`
- SHA-256: `b30c8cf2a4c44652eff4c531e84f4e317eb1073aea833c73ecb7d6f5a5796c80`
- Bytes: `2718495`

Use only a tight shoulder / sleeve / torso-material crop.

Must exclude:

- head;
- hands;
- waist;
- complete garment silhouette;
- bag / accessory;
- full outfit combination.

## 5. Face-crop rule

Each of SRC-01..SRC-04 must show only a fragment of the source face.

Required:

- approximately 35–50% of the visible head / face region;
- include a useful combination of hair + skin + one facial-feature region;
- avoid a complete frontal or three-quarter identity portrait;
- do not show both eyes + full nose + full mouth together;
- do not show the full head silhouette;
- keep source background to the minimum practical area.

Goal:

`FACIAL RENDERING LANGUAGE WITHOUT A COMPLETE IDENTITY TEMPLATE`

## 6. Material-crop rule

SRC-05 and SRC-06 must be texture / material examples rather than outfit examples.

Required:

- shoulder / upper torso fragment only;
- enough visible fold / fabric weight / seam behavior to communicate material rendering;
- no complete torso;
- no garment outline;
- no accessory;
- no recognizable full outfit.

Goal:

`FABRIC / CLOTHING RENDERING LANGUAGE WITHOUT WARDROBE COPYING`

## 7. Board layout

Target output:

`1536 × 1024 PNG`

Orientation:

`LANDSCAPE / NON-SHOT FORMAT`

Reason:

A landscape contact-sheet form makes it visually distinct from the project's 9:16 Story Shot format and reduces the risk that the board itself is interpreted as a shot composition.

Layout:

`3 columns × 2 rows / 6 equal-weight panels`

Panel order:

1. Guang Yong face fragment
2. Su Xiaoxiao face fragment
3. Liao Jian face fragment
4. Wen Qingya face fragment
5. Liao Jian material fragment
6. Wen Qingya material fragment

Canvas:

- fixed neutral middle-gray background;
- equal outer margins;
- equal gutters;
- no decorative frame;
- no captions inside the image;
- no names;
- no asset IDs;
- no text that could be interpreted by the image model as visual instructions.

No panel may dominate in size.

## 8. Color rule

Preserve source RGB appearance.

Do not:

- grade;
- normalize skin tone;
- desaturate;
- recolor;
- equalize exposure.

Reason:

The board must document existing approved visual language, not create a new one.

## 9. Governance classification

This cross-character board does not fit the current P0.2 Entity / Asset Registry schema cleanly.

Current schema requires a `DERIVED_REFERENCE` to bind to one Entity, while this board intentionally derives from multiple Character Entities.

Therefore V001 must not be falsely registered as:

- Ning Qiushui Character Reference Sheet;
- Jun Luyuan Character Reference Sheet;
- any other single Character Entity;
- Story Shot;
- Scene Master;
- Costume Asset.

Proposed classification:

`P0.3 CONTROLLED_PRODUCTION_REFERENCE`

Proposed canonical path:

`production/style_references/character_visual/CHARACTER_VISUAL_STYLE_REFERENCE_V001.png`

Required sidecar:

`production/style_references/character_visual/CHARACTER_VISUAL_STYLE_REFERENCE_V001.manifest.json`

This classification is operational and P0.3-specific. It does not silently alter the approved P0.2 Registry Schema V0.3.

## 10. Provenance manifest requirements

The sidecar manifest must record:

- reference ID;
- build version;
- output path;
- output dimensions;
- output SHA-256;
- output Git blob after publication;
- every source Asset ID;
- every source canonical path;
- every source expected SHA-256;
- every source expected byte size;
- exact crop rectangle for every panel;
- resize algorithm;
- board canvas dimensions;
- panel order;
- background RGB;
- no-generative-processing declaration;
- build commit;
- workflow run;
- approval status.

## 11. Build rule

The board should be constructed by GitHub Actions from canonical source assets.

Build must fail closed unless all 6 source assets pass:

- Registry Asset ID match;
- APPROVED / CURRENT;
- canonical path;
- expected SHA-256;
- expected byte size;
- readable PNG.

The build must be deterministic.

The same source bytes + same crop manifest + same builder version must produce the same output bytes.

No Product Owner manual image editing is part of the baseline.

## 12. Future Bundle integration

The current generic Story Shot bundle builder supports only:

- `ASSET`
- `STORY_SHOT`

The new cross-entity controlled reference must not be misdeclared as either.

Before a future N21 Bundle V004 can use it, the delivery system must add an explicit controlled source type, tentatively:

`CONTROLLED_REFERENCE`

That support must validate:

- canonical style-reference path;
- style-reference manifest;
- output SHA-256 / byte size / Git blob;
- provenance source set.

This is a future implementation step after the Style Reference itself is approved.

## 13. Acceptance criteria for V001 board

The board passes Director / Product Owner review only if:

1. no complete Story Shot composition exists;
2. no complete person is visible;
3. no complete outfit is visible;
4. no panel functions as a full named-character portrait;
5. male and female human-rendering samples are both present;
6. face / hair / skin rendering language is clearly readable;
7. clothing material behavior is clearly readable;
8. no single named character dominates;
9. no Ning / Jun hero-pair cues exist;
10. no scene background is meaningfully encoded;
11. all visible source pixels are traceable to approved canonical Atomic Assets;
12. no generative image processing is used.

## 14. Current boundary

`CHARACTER VISUAL STYLE REFERENCE V0.1 DESIGN = DIRECTOR LOCK / PRODUCT OWNER REVIEW REQUIRED`

Not authorized yet:

- build script implementation;
- crop-coordinate finalization;
- GitHub Actions build;
- formal PNG publication;
- N21 Bundle V004;
- Candidate 05;
- N22.

Next after Product Owner approval:

`Character Visual Style Reference V001｜Exact Crop Plan + Deterministic Build Preparation`
