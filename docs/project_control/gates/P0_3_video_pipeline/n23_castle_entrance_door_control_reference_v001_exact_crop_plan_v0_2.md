# N23_CASTLE_ENTRANCE_DOOR_CONTROL_REFERENCE_V001｜Exact Crop Plan V0.2

Date:

`2026-10-03`

Status:

`PRODUCT OWNER APPROVED / LOCKED / CROP RECTANGLE AUTHORITY ESTABLISHED / CROP EXECUTION NOT YET AUTHORIZED`

Supersedes:

`Exact Crop Plan V0.1 = REJECTED / WRONG DOOR SIDE`

Target:

`N23 Candidate 03`

Source authority:

`AST_IMG_000052｜SCENE_CASTLE_ENTRANCE｜SCENE_MASTER｜DAY_DOOR_OPEN`

Source canonical path:

`production/image_library/scene_masters/castle_entrance/SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`

Source exact identity:

- dimensions: `941 × 1672`
- byte size: `2,305,753`
- SHA-256: `d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961`

## 1. Correction basis

New Product Owner spatial fact:

`NEIL IS BESIDE THE RIGHT-SIDE DOOR LEAF IN N23`

Therefore the controlled reference must not emphasize the opposite left-side door leaf.

The V0.2 crop is designed to preserve:

- the right-side door leaf;
- its carved wood identity;
- its open angle;
- adjacent interior-side wall / standing zone where Neil belongs;
- a narrow sliver of the opening sufficient to preserve open-door context.

It must still suppress:

- broad exterior sky;
- large central daylight field;
- broad reflective interior floor.

## 2. Exact crop rectangle

Coordinate system:

- source origin = top-left;
- x increases rightward;
- y increases downward;
- crop convention = left/top inclusive, right/bottom exclusive.

Proposed rectangle:

- `x1 = 615`
- `y1 = 75`
- `x2 = 930`
- `y2 = 1340`

Resulting crop size:

`315 × 1265 px`

No resize is permitted during deterministic crop construction.

## 3. Intended direct-pixel authority

This controlled crop may directly control:

- right door-leaf material;
- right door-leaf carved-panel language;
- right door-leaf open-state / oblique angle;
- local door-frame relation;
- adjacent interior-side standing zone relevant to Neil;
- fact that the door is open.

It must NOT directly control:

- complete double-door symmetry;
- full portal width;
- whole arch geometry;
- exterior scene composition;
- scene lighting;
- broad floor lighting.

Those broader facts remain governed by locked N23 Scene Reference / parent Scene Master authority.

## 4. PASS criteria

Product Owner confirmed this V0.2 plan. Locked acceptance basis:

- the selected side is the correct Neil-side door;
- enough of the right door leaf is visible to identify the same approved entrance;
- adjacent local interior space is useful for Neil placement;
- exterior brightness remains subordinate;
- reflective interior floor is absent or negligible;
- the crop does not imply that only one door leaf exists.

## 5. FAIL criteria

Reject / redesign if:

- Neil-side relation is still ambiguous;
- the crop includes too much exterior brightness;
- the crop includes too much reflective floor;
- the right door identity is not sufficiently readable;
- the crop creates misleading architecture.

## 6. Authorization boundary

Current authorization:

`EXACT CROP PLAN V0.2 PRODUCT OWNER APPROVED / LOCKED`

Not authorized:

- executing the crop;
- deterministic controlled-reference build;
- exact binary verification;
- Bundle V003 Design / Spec;
- Candidate 03 generation.

Next gate:

`DETERMINISTIC CROP BUILD PREPARATION / SEPARATE EXECUTION AUTHORIZATION REQUIRED`
