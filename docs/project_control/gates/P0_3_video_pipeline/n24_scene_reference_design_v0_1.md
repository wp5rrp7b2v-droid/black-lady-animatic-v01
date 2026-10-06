# N24｜Scene Reference Design V0.1

Status: `PRODUCT OWNER APPROVED / LOCKED / BUNDLE DESIGN NEXT`

Date: `2026-10-06`

Shot:

`N24｜Following the Guide — Ning Spatial POV`

Director authority:

- `N24 Node-Level Director Shot Design V0.2`
- Product Owner explicit approval in Chat on 2026-10-06

## 1. Decision

No dedicated N24 environment reference will be generated at this stage.

N24 will use a minimal mixed-authority reference architecture:

1. current Castle Entrance Scene Master for stable entrance-space facts;
2. approved N23 Story Shot for immediate spatial / crowd / lighting continuity;
3. current Ning Qiushui rear-3Q authority for POV-anchor identity;
4. current Neil rear-3Q authority for guide identity;
5. Generic Guest Crowd REAR_3Q authority for anonymous cohort identity / wardrobe continuity.

`SCENE_FIRST_HALL V002` is explicitly excluded from direct N24 generation references.

Reason:

N24 must remain in the entrance-adjacent short interior transition zone and must not prematurely spend the formal First Hall establishment or N27's deeper-unknown transition.

## 2. Scene authority

Primary stable environment authority:

`AST_IMG_000105｜SCENE_CASTLE_ENTRANCE｜SCENE_MASTER｜DAY_DOOR_OPEN｜V002`

Canonical path:

`production/image_library/scene_masters/castle_entrance/SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V002.png`

Controls:

- Castle Entrance architectural identity;
- entrance / interior boundary;
- DAY / DOOR_OPEN state;
- material / spatial family;
- restrained entrance-light relationship.

Must NOT control:

- exact final camera;
- exact screen placement;
- exact character blocking;
- exact final depth;
- centered entrance showcase.

## 3. Immediate continuity authority

`N23_NEIL_AT_OPEN_DOOR_APPROVED_V001`

Canonical path:

`production/image_library/approved/story_shots/N23_NEIL_AT_OPEN_DOOR_APPROVED_V001.png`

Controls only:

- immediate N23→N24 continuity;
- Neil has just been at the open door;
- tail of cohort has just completed entry;
- warm low-key interior family;
- open entrance remains perceptually nearby.

Must NOT be copied as:

- identical camera;
- identical character positions;
- exact N23 composition;
- freeze-frame continuation.

N24 must visibly advance the action by one small step:

`NEIL HAS JUST STARTED LEADING / GROUP HAS JUST STARTED FOLLOWING`

## 4. Character / crowd authority

Ning:

`AST_IMG_000037｜CHAR_NING_QIUSHUI｜REAR_3Q_RIGHT｜V002`

Purpose:

`NING IDENTITY + REAR-3Q POV ANCHOR ONLY`

Neil:

`AST_IMG_000066｜CHAR_NEIL｜REAR_3Q_RIGHT｜V001`

Purpose:

`NEIL IDENTITY + REAR-3Q GUIDE ORIENTATION ONLY`

Generic cohort:

`BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q`

Purpose:

`ANONYMOUS GUEST IDENTITY / WARDROBE / SIDE-BACK SILHOUETTE CONTINUITY ONLY`

No direct Jun reference is required for N24 V001 Bundle.

Jun remains optional in written shot authority but is not necessary for minimum proof.

## 5. Spatial interpretation

Required final spatial read:

`CASTLE ENTRANCE → ONLY A FEW STEPS INWARD → SHORT INTERIOR TRANSITION`

Not:

`CASTLE ENTRANCE → DEEP CASTLE`

At least one restrained entrance-proximity cue must survive:

- partial doorway/door cue; or
- rear entrance glow; or
- obvious short reverse-depth relationship to the threshold.

The open door itself does not need to be the visual subject.

## 6. First Hall exclusion

Do not directly deliver:

`AST_IMG_000106｜SCENE_FIRST_HALL V002`

Do not show:

- full First Hall;
- fireplace establishment;
- major hall composition;
- destination reveal.

## 7. Dedicated reference escalation rule

A new:

`N24_INTERIOR_TRANSITION_REFERENCE`

shall be created only if Bundle / Candidate evidence demonstrates that the current authorities cannot keep the group near the entrance while showing the first inward movement.

It is not pre-authorized merely as a precaution.

## 8. Current gate

Status:

`PRODUCT OWNER APPROVED / LOCKED`

Approved:

`2026-10-06 / Product Owner explicit Chat approval`

Authorized next:

`N24_REFERENCE_DELIVERY_BUNDLE_V001 DESIGN`

Not yet authorized:

- Bundle V001 Spec;
- validation-only run;
- formal build;
- Work generation;
- Candidate 01.
