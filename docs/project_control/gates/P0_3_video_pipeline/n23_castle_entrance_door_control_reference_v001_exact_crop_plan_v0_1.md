# N23_CASTLE_ENTRANCE_DOOR_CONTROL_REFERENCE_V001｜Exact Crop Plan V0.1

Date:

`2026-10-03`

Status:

`REJECTED / WRONG DOOR SIDE / SUPERSEDED BY V0.2 / CROP EXECUTION NOT AUTHORIZED`

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
- Git blob: `fetched from canonical source at build time / must be exact-verified before crop execution`

## 1. Visual finding

The Scene Master places a large bright exterior opening in the center of the full double-door geometry.

A single rectangular crop cannot simultaneously:

1. retain the complete double-door / full portal geometry; and
2. strongly suppress the exterior daylight and reflective-floor photographic pressure.

Therefore the proposed controlled reference intentionally narrows direct-pixel authority.

## 2. Proposed direct-pixel authority

The controlled crop may directly control:

- left door-leaf material;
- carved-panel design language;
- door-leaf vertical scale;
- door thickness / oblique open-angle cue;
- local frame / threshold relationship;
- fact that the door is open.

It must NOT be treated as complete direct-pixel authority for:

- full double-door width;
- complete portal symmetry;
- whole arch geometry;
- exterior scene composition;
- scene lighting;
- interior floor lighting.

Those broader scene facts remain governed by the locked N23 Scene Reference / Scene Master parent authority.

## 3. Exact crop rectangle

Coordinate system:

- source origin = top-left;
- x increases rightward;
- y increases downward;
- crop convention = left/top inclusive, right/bottom exclusive.

Proposed rectangle:

- `x1 = 130`
- `y1 = 120`
- `x2 = 325`
- `y2 = 1335`

Resulting crop size:

`195 × 1215 px`

No resize is permitted during deterministic crop construction.

## 4. Why this rectangle

The rectangle retains almost the full visible height of the left open door leaf while excluding:

- nearly all of the right door leaf;
- most of the central sky opening;
- the broad reflective interior floor;
- most symmetric full-portal composition pressure.

A narrow exterior sliver remains intentionally visible so the crop still reads as an open door rather than an isolated wooden panel.

## 5. PASS criteria

The proposed crop plan passes Product Owner visual review only if:

- the selected region clearly reads as the same approved Castle Entrance door;
- carved wood material and door-leaf identity remain readable;
- open-state / oblique door angle remains readable;
- exterior is subordinate rather than dominant;
- reflective interior floor is absent or negligible;
- the crop does not imply a new door design.

## 6. FAIL criteria

Reject / redesign the crop plan if:

- the crop is too narrow to read as an open door;
- loss of full portal geometry is unacceptable for Candidate 03;
- remaining exterior brightness is still too dominant;
- the crop creates misleading single-door architecture;
- door scale / material cannot be read reliably.

## 7. Authorization boundary

Current authorization:

`EXACT CROP PLAN DESIGN ONLY`

Not authorized:

- executing the crop;
- publishing the controlled reference;
- deterministic build;
- exact binary verification;
- Bundle V003 Design / Spec;
- Candidate 03 generation.

Next gate:

`PRODUCT OWNER VISUAL APPROVAL OF THIS EXACT CROP PLAN`


## 8. Rejection record

Product Owner correction:

`Neil is beside the opposite / right-side door leaf in N23, not beside the left-side door leaf selected by this plan.`

Therefore the V0.1 crop would introduce incorrect local spatial pressure between Neil and the door.

Disposition:

`REJECTED / DO NOT BUILD / DO NOT DELIVER`

Superseded by:

`N23_CASTLE_ENTRANCE_DOOR_CONTROL_REFERENCE_V001｜Exact Crop Plan V0.2`
