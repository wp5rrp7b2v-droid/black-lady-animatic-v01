# N21_CASTLE_ENTRANCE_DOOR_IDENTITY_REFERENCE_V001｜Exact Crop Plan V0.1

Date:

`2026-10-03`

Status:

`PRODUCT OWNER APPROVED / LOCKED / CROP EXECUTION NOT YET AUTHORIZED`

Target:

`N21 Candidate 09｜Cohort Enters — Inside the Flow`

Source authority:

`AST_IMG_000052｜SCENE_CASTLE_ENTRANCE｜SCENE_MASTER｜DAY_DOOR_OPEN`

Source canonical path:

`production/image_library/scene_masters/castle_entrance/SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`

Source exact identity:

- dimensions: `941 × 1672`
- byte size: `2,305,753`
- SHA-256: `d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961`

Related existing controlled reference:

`N23_CASTLE_ENTRANCE_DOOR_CONTROL_REFERENCE_V001`

N21 does NOT reuse the N23 controlled reference directly because N23 retained extra wall / sconce / armor / local standing-zone information for Neil placement. N21 requires a narrower identity-only crop.

## 1. Crop objective

Preserve only enough pixels to establish:

- physical right-side carved wooden door leaf;
- carved-panel sequence / wood material identity;
- the leaf's open oblique angle;
- a very narrow opening / exterior edge proving the door remains open.

Suppress as much as practical:

- full portal geometry;
- opposite door leaf;
- centered arch composition;
- broad sky / exterior;
- wall sconce;
- armor;
- reflective interior floor;
- broad interior wall;
- any Neil-placement cue.

This reference is an identity control, not an environment reference.

## 2. Exact crop rectangle

Coordinate system:

- source origin = top-left;
- x increases rightward;
- y increases downward;
- left / top inclusive;
- right / bottom exclusive.

Proposed rectangle:

- `x1 = 640`
- `y1 = 130`
- `x2 = 800`
- `y2 = 1340`

Resulting crop size:

`160 × 1210 px`

No resize.

No re-encode beyond deterministic PNG crop construction.

No retouch.

No relight.

No recolor.

## 3. Why this rectangle

Compared with the N23 Door Control crop `615,75 → 930,1340`, this N21 crop:

- removes the right-side wall-sconce composition;
- removes armor;
- removes nearly all Neil standing-zone context;
- reduces exterior opening to a narrow sliver;
- keeps the carved door panels readable from upper to lower leaf;
- preserves the visible open-edge / oblique leaf relationship;
- removes most broad environment information that could push Work back toward an architecture-first frame.

## 4. Direct-pixel authority

May control only:

- same physical right-side door-leaf identity;
- carved wooden panel language;
- wood material / color family;
- door-leaf thickness / visible edge;
- open state / oblique leaf angle;
- fact that a narrow exterior opening remains beside the leaf.

Must NOT control:

- N21 camera;
- screen placement;
- exact crop-like framing in final Story Shot;
- complete doorway width;
- complete arch;
- full entrance geometry;
- exterior scenery;
- outdoor brightness;
- floor;
- castle interior layout;
- crowd position;
- crowd direction;
- lighting composition.

## 5. Candidate 09 intended usage

Written shot authority, not this crop, determines:

- door appears only as a partial extreme screen-left cue;
- participant flow = left-rear threshold → right-forward deeper interior;
- camera among / beside people;
- warm low-key interior;
- narrow daylight edge only;
- no complete portal;
- no centered vanishing point.

The reference pixels establish identity only.

## 6. PASS criteria

Approve this crop if:

1. the correct physical right-side door leaf is unmistakable;
2. carved-panel identity remains readable;
3. open-door state remains readable;
4. exterior cue is narrow rather than composition-dominant;
5. no armor is present;
6. no wall sconce is present;
7. no complete portal / opposite door is present;
8. no broad reflective floor is present;
9. the crop is narrow enough not to function as an environment composition template.

## 7. FAIL / revise if

- door identity becomes too abstract to recognize;
- exterior area is still visually dominant;
- crop includes architecture unrelated to door identity;
- crop encourages a complete threshold composition;
- source side is ambiguous;
- the crop no longer proves the door is open.

## 8. Authorization boundary

Current:

`EXACT CROP PLAN V0.1 / PRODUCT OWNER APPROVED / LOCKED`

Not authorized:

- executing deterministic crop build;
- canonical controlled-reference publication;
- manifest finalization;
- Bundle V007 Spec;
- Candidate 09 generation.

Next gate:

`DETERMINISTIC CROP BUILD PREPARATION / SEPARATE EXECUTION AUTHORIZATION`
