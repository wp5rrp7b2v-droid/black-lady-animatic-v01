# Character Visual Style Reference V001｜Exact Crop Plan + Deterministic Build Preparation

Date: 2026-10-01

Status: `LOCKED / BUILD PREP READY / FORMAL STYLE BOARD NOT YET BUILT`

Reference ID:

`CHARACTER_VISUAL_STYLE_REFERENCE_V001`

Authority:

- Product Owner authorized progression from V0.1 design review into exact crop locking and deterministic build preparation.
- Design: `docs/project_control/gates/P0_3_video_pipeline/character_visual_style_reference_v0_1_design.md`
- Machine-readable crop plan: `production/style_references/character_visual/CHARACTER_VISUAL_STYLE_REFERENCE_V001.crop_plan.json`

## 1. Source inspection evidence

A non-production source-inspection artifact was built only to inspect the six approved Atomic PNGs.

Successful inspection run:

- workflow: `Story Shot Reference Bundle Builder`
- run: `36820797772`
- artifact: `CHARACTER_VISUAL_STYLE_SOURCE_INSPECTION_V001`
- artifact ID: `11143985053`
- artifact digest: `sha256:255d2801f4307394b2721a128dc8e285f4b9d85b2035131ad97ea2b100d7770c`
- exact source verification: `6/6 PASS`

This Artifact is:

`SOURCE INSPECTION ONLY / NEVER A GENERATION INPUT`

## 2. Builder spec-selection defect discovered and fixed

During inspection, two earlier runs incorrectly fell back to the previous N21 V003 bundle spec because the generic builder attempted to infer the changed spec from a one-commit shallow checkout.

Root cause:

`FETCH_DEPTH_1 DID NOT PROVIDE A RELIABLE HEAD^→HEAD CHANGESET`

Fix:

- workflow checkout now uses `fetch-depth: 2`;
- push-trigger spec selection now uses `git diff --name-only HEAD^ HEAD -- production/bundle_specs/*.json`;
- push path trigger is limited to `production/bundle_specs/*.json`;
- push execution fails closed unless exactly one Bundle spec changed.

Relevant fix sequence:

- `c0e63bd9bd50a9748b030df8047e651097583a49` — first shallow-checkout correction attempt;
- `4a0214450ece8e796c2cffa8378bd3c025561394` — event-payload fail-closed attempt;
- `08ad70049f172a0e2d74e165f3010f2ac954ecf4` — final two-commit checkout/diff implementation;
- `1a7eba6abc0c64b618b7d969ce20664195688817` — successful source-inspection trigger.

No failed inspection run produced or authorized a Story Shot.

## 3. Locked board geometry

Output:

`1536 × 1024 / RGB / PNG`

Canvas background:

`RGB(144,144,144)`

Layout:

- outer margin: `48 px`;
- gutter: `24 px`;
- columns: `3`;
- rows: `2`;
- each panel slot: `464 × 452 px`.

Panel slot origins:

1. `(48, 48)`
2. `(536, 48)`
3. `(1024, 48)`
4. `(48, 524)`
5. `(536, 524)`
6. `(1024, 524)`

No labels or text are rendered into the image.

## 4. Exact crop rectangles

All six source PNGs are `941 × 1672`.

Coordinates use:

`x / y from top-left, width / height in source pixels`

### Panel 1｜Guang Yong face / hair / skin fragment

Source:

`AST_IMG_000010`

Crop:

`x=250 / y=230 / w=300 / h=420`

LTRB:

`[250, 230, 550, 650]`

Resized:

`323 × 452`

Paste origin:

`(118, 48)`

Purpose:

single-side male facial / hair / skin rendering language without a complete identity portrait.

### Panel 2｜Su Xiaoxiao face / hair / skin fragment

Source:

`AST_IMG_000043`

Crop:

`x=420 / y=180 / w=300 / h=420`

LTRB:

`[420, 180, 720, 600]`

Resized:

`323 × 452`

Paste origin:

`(606, 48)`

Purpose:

single-side female facial / hair / skin rendering language without a complete identity portrait.

### Panel 3｜Liao Jian face / hair / skin fragment

Source:

`AST_IMG_000023`

Crop:

`x=360 / y=160 / w=300 / h=420`

LTRB:

`[360, 160, 660, 580]`

Resized:

`323 × 452`

Paste origin:

`(1094, 48)`

Purpose:

second male facial sample with distinct age / skin / hair treatment.

### Panel 4｜Wen Qingya face / hair / skin fragment

Source:

`AST_IMG_000047`

Crop:

`x=340 / y=140 / w=260 / h=420`

LTRB:

`[340, 140, 600, 560]`

Resized:

`280 × 452`

Paste origin:

`(140, 524)`

Purpose:

second female facial sample; crop intentionally excludes a complete two-eye identity portrait.

### Panel 5｜Liao Jian clothing-material / upper-torso fragment

Source:

`AST_IMG_000022`

Crop:

`x=330 / y=430 / w=280 / h=300`

LTRB:

`[330, 430, 610, 730]`

Resized:

`422 × 452`

Paste origin:

`(557, 524)`

Purpose:

fabric weight, folds and layer rendering only.

The crop excludes:

- head;
- hands;
- waist;
- full body;
- complete outfit silhouette.

### Panel 6｜Wen Qingya clothing-material / sleeve fragment

Source:

`AST_IMG_000046`

Crop:

`x=480 / y=370 / w=300 / h=250`

LTRB:

`[480, 370, 780, 620]`

Resized:

`464 × 387`

Paste origin:

`(1024, 556)`

Purpose:

outerwear material, shoulder and sleeve-fold rendering.

The crop excludes:

- face;
- hands;
- waist;
- full torso;
- complete outfit silhouette.

## 5. Deterministic resize contract

Implementation target:

`Python + Pillow`

Required behavior:

- decode source PNG;
- convert source crop to RGB without grading;
- crop exact integer rectangle;
- preserve aspect ratio;
- scale to fit its fixed panel slot;
- resize with `PIL.Image.Resampling.LANCZOS`;
- output dimensions exactly as locked above;
- center crop inside the panel slot;
- paste onto fixed neutral canvas.

Rounding:

`int(round(source_dimension × scale))`

No automatic smart crop, face detector, saliency crop, content-aware adjustment or model inference is permitted during production build.

## 6. Dependency pinning

The formal build implementation must pin:

- Python minor version;
- Pillow exact version.

The build record must capture both runtime versions.

A dependency/version change requires a new builder version and binary re-verification.

## 7. Determinism test

Before canonical publication, the same build must run twice from:

- identical six source binaries;
- identical crop-plan JSON;
- identical script commit;
- identical pinned runtime.

Required:

`RUN_A_OUTPUT_SHA256 == RUN_B_OUTPUT_SHA256`

If not:

`FAIL CLOSED / DO NOT PUBLISH`

## 8. Required production files after build authorization

Builder implementation must eventually create:

- `scripts/build_character_visual_style_reference_v001.py`
- dedicated or controlled GitHub Actions workflow;
- output PNG:
  `production/style_references/character_visual/CHARACTER_VISUAL_STYLE_REFERENCE_V001.png`
- provenance sidecar:
  `production/style_references/character_visual/CHARACTER_VISUAL_STYLE_REFERENCE_V001.manifest.json`

The sidecar must record:

- six source Asset IDs / paths / SHA-256 / byte sizes;
- exact crop rectangles;
- resized dimensions;
- paste origins;
- canvas geometry;
- background RGB;
- runtime versions;
- script SHA / commit;
- output SHA-256 / bytes;
- Git blob after publication;
- two-run determinism evidence;
- Product Owner approval status.

## 9. Visual acceptance boundary

The locked crop plan is designed to ensure:

- no complete Story Shot;
- no complete person;
- no complete outfit;
- no Ning / Jun;
- no group composition;
- no scene composition;
- no full two-eye identity portrait used as the board's primary readable unit;
- male and female face / hair / skin samples;
- two independent clothing-material samples.

The formal PNG still requires Product Owner visual review after the deterministic build.

## 10. Current authorization boundary

Authorized and complete:

- V0.1 design progression;
- source inspection;
- exact 6-panel crop plan;
- deterministic build preparation.

Not yet authorized:

- formal builder script implementation;
- formal Style Board build;
- canonical publication;
- CONTROLLED_REFERENCE Bundle support;
- N21 Bundle V004;
- N21 Candidate 05;
- N22.

Next:

`Product Owner authorization → implement deterministic builder + two-run proof → Style Board visual review`
