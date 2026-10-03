# N23 Candidate 03｜Correction Strategy V0.1

Status:

`DIRECTOR DESIGN PREPARED / SLOT 3 MICRO-CORRECTION PRODUCT OWNER APPROVED AND INCORPORATED / FINAL STRATEGY APPROVAL STILL REQUIRED / REFERENCE CONTROLS NOT YET BUILT / CANDIDATE 03 NOT AUTHORIZED`

Date:

`2026-10-03`

Target:

`N23｜Neil at the Open Door — Watches the Group Enter｜Candidate 03`

Previous candidate:

`Candidate 02 = PRODUCT OWNER REJECTED / STRUCTURAL FAIL`

Primary authority:

- `N23 Scene Reference Design V0.2.1`
- Product Owner structural rejection of Candidate 02
- `BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001`

Proposed generation mode after all later gates:

`CLEAN REGENERATION`

Candidate 02 pixels:

`NEGATIVE / DIAGNOSTIC ONLY / NOT AN EDIT BASE`

---

## 1. PURPOSE

Candidate 03 must correct four failures exposed by Candidate 02:

1. crowd motion did not read as N22-continuous screen-left → screen-right travel;
2. Neil identity drifted materially;
3. Guang Yong lost the walking-with-backward-awareness behavior;
4. exterior / floor daylight remained too dominant.

This correction must NOT be solved by adding more and more direct reference images.

Hard production constraint:

`MAXIMUM DIRECT VISUAL INPUTS = 5`

The Candidate 03 architecture must fit inside five direct visual reference slots.

If additional evidence is required, it must be compressed into approved controlled references rather than increasing direct-image count beyond five.

---

## 2. MOTION CONTINUITY — REDEFINED HARD LOCK

Candidate 02 proved that:

`PEOPLE ENDING UP ON THE RIGHT SIDE OF FRAME`

is NOT equivalent to:

`PEOPLE VISIBLY MOVING LEFT → RIGHT`

Candidate 03 must make screen-space travel readable in the bodies themselves.

First motion read:

`LATERAL SCREEN-RIGHT TRAVEL`

Second motion read:

`GRADUAL RECESSION INTO THE INTERIOR`

Hard rule:

`LATERAL COMPONENT MUST DOMINATE THE FIRST READ; DEPTH COMPONENT IS SECONDARY`

Required body evidence:

- hips / torso travel toward frame-right;
- stride and feet support frame-right travel;
- shoulders are side / side-back / rear-3Q rather than mostly full-back;
- crowd path crosses the frame from left-center toward right;
- the group may recede modestly, but must not primarily read as walking straight away from camera.

Do NOT accept:

- full-back procession into depth;
- people simply shrinking toward a vanishing point;
- crowd mass on frame-right with no readable rightward travel vector.

---

## 3. CAMERA INTERPRETATION — BROADSIDE FIRST

Retain the N23 side / broadside threshold concept, but Candidate 03 tightens the interpretation:

`BROADSIDE FIRST / DEPTH SECOND`

The camera must observe people crossing the threshold zone laterally.

The deeper interior may open toward right-rear, but the crowd path may not align mainly with the camera-to-depth axis.

Preferred spatial grammar:

`LEFT DOOR / NEIL LEFT-CENTER / CROWD CROSSING LEFT→RIGHT / DEEPER INTERIOR RIGHT-REAR`

Not:

`LEFT DOOR / NEIL / CROWD WALKING STRAIGHT AWAY INTO CENTER-RIGHT DEPTH`

---

## 4. NEIL IDENTITY — STRONGER ANGLE-SPECIFIC LOCK

Candidate 02 showed that the composite Neil Character Reference Sheet alone was insufficient.

Candidate 03 removes the full Character Sheet from direct Work input.

New direct Neil identity anchor:

`AST_IMG_000073｜CHAR_NEIL｜FACE_3Q_RIGHT`

Reason:

- N23 requires near-frontal Neil with head / eyes slightly toward frame-right;
- FACE_3Q_RIGHT is closer to the required identity presentation;
- reducing the reference to an angle-specific face anchor increases identity pressure while avoiding an additional full-sheet slot.

Important:

`AST_IMG_000073 CONTROLS IDENTITY, NOT EXACT HEAD ROTATION OR SCREEN POSITION`

Shot design still controls:

- Neil beside the door;
- near-frontal body;
- subtle rightward head / eye turn;
- no door contact;
- no walk-away.

Hard fail:

`POSE CORRECT BUT NEIL IDENTITY DRIFTS`

---

## 5. GUANG YONG — BODY CONTINUES / HEAD OBSERVES

Candidate 02 used:

`AST_IMG_000013 / REAR_3Q_RIGHT`

but the output lost the N22 behavioral bridge.

Candidate 03 removes AST_IMG_000013 from direct input.

New direct Guang identity-only anchor:

`AST_IMG_000011｜CHAR_GUANG_YONG｜FACE_FRONT`

Reason for the micro-correction:

- project orientation governance defines RIGHT as face/nose toward screen-right;
- Candidate 03 requires Guang's body to continue screen-right while his head / attention retains a small backward cue toward frame-left / Neil / the open door;
- therefore `FACE_3Q_RIGHT` would introduce avoidable head-direction pressure opposite to the intended backward-awareness cue.

`AST_IMG_000011 CONTROLS GUANG IDENTITY ONLY / IT MUST NOT CONTROL SHOT-SPECIFIC HEAD DIRECTION`

The complete action is controlled by the N22-derived motion/observation reference plus written shot authority.

The complete behavioral lock is:

`BODY CONTINUES SCREEN-RIGHT WITH THE GROUP / HEAD-NECK RETAINS A SMALL BACKWARD OBSERVATION TOWARD FRAME-LEFT / NEIL / OPEN DOOR`

Guang must NOT:

- stop walking;
- rotate his whole torso back;
- become a reaction portrait;
- become a co-lead with Neil;
- speak;
- make an exaggerated over-the-shoulder pose.

Correct read:

`HE IS STILL MOVING WITH THE FLOW, BUT HE HAS NOT FULLY STOPPED WATCHING BEHIND HIM`

This behavior must be supported visually by a dedicated N22-derived controlled reference defined below.

---

## 6. GENERIC GUEST STRATEGY — REAR_3Q ONLY

Keep:

`BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q`

as the only direct Generic Guest board.

Remove from Candidate 03 direct inputs:

`BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_BACK`

Reason:

Candidate 02 indicates that REAR_3Q + BACK together over-reinforced:

`PEOPLE WALKING AWAY INTO DEPTH`

Candidate 03 should favor:

- side-back;
- rear-3Q;
- lateral body travel;
- partially readable side orientation.

Generic Guest FRONT remains:

`NON-DELIVERED GLOBAL IDENTITY AUTHORITY / FRONT WINS`

Generic Guest LEFT_PROFILE remains non-delivered.

Target anonymous crowd:

`APPROXIMATELY 3–5 GENERIC GUESTS / PARTIAL BODIES`

plus Guang Yong if visible.

Do not force all ten.

---

## 7. NEW CONTROLLED REFERENCE A — N22 MOTION + OBSERVATION

Required new controlled reference:

`N23_N22_MOTION_OBSERVATION_REFERENCE_V001`

Source authority:

`N22_PEOPLE_IN_THE_FLOW_APPROVED_V001.png`

Source must be the exact approved N22 canonical binary.

Purpose:

`N22→N23 MOTION CONTINUITY + GUANG YONG BACKWARD-AWARENESS BEHAVIOR ONLY`

This controlled reference should be built deterministically from exact N22 pixels, not regenerated.

Proposed single-image / two-panel structure:

### Panel A｜Motion Continuity

A crop that proves the N22 movement language:

- lateral flow;
- asynchronous stride;
- people moving while observing;
- no formal queue.

It should suppress unnecessary readable named faces as much as possible.

### Panel B｜Guang Observation Behavior

A tighter crop proving the specific behavior Product Owner requires:

`WALKING WITH THE GROUP WHILE STILL OBSERVING BACK / SIDE`

This panel is behavioral evidence, not a new Guang identity authority.

Exact crop rectangles are NOT locked by this strategy.

They require a separate:

`CONTROLLED REFERENCE EXACT CROP PLAN + PRODUCT OWNER VISUAL APPROVAL`

before build.

Hard boundary:

`DO NOT DELIVER THE FULL N22 STORY SHOT TO WORK`

Reason:

Candidate 01 proved that full N22 pixels create excessive ensemble / composition pressure.

---

## 8. NEW CONTROLLED REFERENCE B — DOOR IDENTITY WITHOUT LIGHTING BIAS

Candidate 02 still showed excessive exterior / floor daylight while using the full Castle Entrance Scene Master.

Therefore Candidate 03 should NOT directly deliver the complete AST_IMG_000052 Scene Master.

Required new controlled reference:

`N23_CASTLE_ENTRANCE_DOOR_CONTROL_REFERENCE_V001`

Source authority:

`AST_IMG_000052 / SCENE_CASTLE_ENTRANCE / DAY_DOOR_OPEN`

Purpose:

`DOOR MATERIAL / GEOMETRY / SCALE / OPEN-STATE ONLY`

Build method:

`DETERMINISTIC CROP FROM APPROVED SCENE MASTER / NO GENERATION`

The crop must emphasize:

- door leaf;
- frame / threshold identity;
- material;
- scale;
- open-door fact.

It must suppress as much as practicable:

- broad exterior sky / daylight area;
- reflective floor;
- photographic lighting pattern.

Exact crop rectangle is NOT locked here.

It requires separate Product Owner approval.

The full Scene Master remains parent authority but is NOT a direct Candidate 03 Work image.

---

## 9. LIGHTING

Candidate 03 keeps the lighting contract:

`INTERIOR DOMINANT / WARM LOW-KEY / EXTERIOR = SMALL LEFT-EDGE CUE`

Required:

- warm practical sources dominate;
- floor is dark / warm / low-reflectance;
- exterior remains readable but spatially small;
- no broad cool reflection.

Automatic fail:

- cool floor band becomes a compositional feature;
- exterior is a second dominant exposure world;
- glossy floor reflection pulls first glance.

No separate lighting reference image is allocated because of the five-image cap.

Lighting must be controlled through:

- N22 Motion/Observation controlled reference;
- Door Control reference;
- written shot authority.

---

## 10. CANDIDATE 03 DIRECT-REFERENCE CAP

Hard cap:

`5 DIRECT VISUAL INPUTS MAXIMUM`

Proposed direct inputs:

1. `N23_CASTLE_ENTRANCE_DOOR_CONTROL_REFERENCE_V001`
2. `AST_IMG_000073｜Neil FACE_3Q_RIGHT`
3. `AST_IMG_000011｜Guang Yong FACE_FRONT / IDENTITY ONLY`
4. `BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q`
5. `N23_N22_MOTION_OBSERVATION_REFERENCE_V001`

No sixth direct image.

---

## 11. DIRECT INPUTS REMOVED FROM V002

Remove:

- full `AST_IMG_000052` Scene Master;
- `AST_IMG_000059` Neil Character Reference Sheet;
- `AST_IMG_000013` Guang Yong REAR_3Q_RIGHT;
- `AST_IMG_000010` Guang Yong FACE_3Q_RIGHT as a direct Candidate 03 input, because its screen-right facial orientation conflicts with the intended backward-attention direction;
- Generic Guest BACK;
- full N22 canonical Story Shot.

These remain historical / parent authorities where applicable but are not direct Candidate 03 Work inputs.

---

## 12. CANDIDATE 03 PASS TEST

Candidate 03 may pass only if:

1. first motion read is visibly LEFT → RIGHT;
2. depth recession is secondary, not dominant;
3. crowd bodies are mostly side / side-back / rear-3Q rather than full-back;
4. most people are already to Neil's right;
5. Neil remains beside the open door;
6. Neil identity matches approved Neil authority;
7. Neil body is near-frontal with head / eyes subtly right;
8. Guang continues moving rightward while retaining a small backward-observation cue;
9. Guang remains tertiary;
10. Generic Guest identities remain consistent without 2×5 board behavior;
11. no single-file procession;
12. no synchronized stride;
13. warm-dark interior dominates;
14. no broad cool floor reflection;
15. no bags / luggage;
16. A06 remains unspent.

---

## 13. FAIL TEST

Automatic fail if:

- crowd mainly walks straight away into depth;
- final screen position is right but body motion is not;
- Neil identity drifts;
- Guang simply walks away with no backward-awareness cue;
- Guang stops and turns fully back;
- Generic Guest BACK-like procession returns;
- full N22 ensemble composition returns;
- all ten Guests are forced into frame;
- exterior / floor brightness dominates;
- bag-like item appears.

---

## 14. CURRENT GATE

Status:

`DIRECTOR DESIGN PREPARED / SLOT 3 MICRO-CORRECTION INCORPORATED / WAITING PRODUCT OWNER FINAL APPROVAL`

If approved, next steps are NOT Bundle V003 immediately.

First:

1. design `N23_N22_MOTION_OBSERVATION_REFERENCE_V001` exact crop plan;
2. design `N23_CASTLE_ENTRANCE_DOOR_CONTROL_REFERENCE_V001` exact crop plan;
3. Product Owner visually approves both controlled-reference plans;
4. deterministic GitHub Actions build + exact binary verification for both controlled references;
5. then design `N23_REFERENCE_DELIVERY_BUNDLE_V003` with exactly five direct visual references.

Product Owner decision already recorded for this revision:

`SLOT 3 MICRO-CORRECTION APPROVED: AST_IMG_000010 FACE_3Q_RIGHT → AST_IMG_000011 FACE_FRONT / IDENTITY ONLY`

This decision does not itself approve the complete Candidate 03 strategy or authorize the next gate.

Still not authorized:

- controlled reference build;
- Bundle V003 Spec;
- validation;
- formal Bundle build;
- Candidate 03 generation;
- N24;
- publication;
- registration.
