# N23 Candidate 02｜Correction Strategy V0.1

Status: `DRAFT / WAITING PRODUCT OWNER APPROVAL / BUNDLE V002 NOT AUTHORIZED`

Date: 2026-10-02

Target:

`N23｜Neil at the Open Door — Watches the Group Enter`

Current camera authority:

`N23 Scene Reference Design V0.2.1`

Candidate 01 status:

`NOT APPROVED / DIAGNOSTIC EVIDENCE ONLY`

---

## 1. CORRECTION GOAL

Candidate 02 must prove that N23 can become structurally different from N22 while preserving:

- same event / same cohort feeling;
- Castle Entrance identity;
- Neil identity;
- Guang Yong's subtle behavioral continuity;
- warm-dark interior continuity.

The correction must not reopen already-valid facts:

- door remains open;
- Neil remains beside the door;
- group is entering the castle;
- A06 remains later payoff.

---

## 2. CANDIDATE 01 ROOT-CAUSE EVIDENCE

Candidate 01 established:

### VALID

- movement broadly read as entering the castle;
- Neil remained beside the open door;
- door remained open.

### FAILED

- camera family remained too similar to N22;
- N22 direct Story Shot pixels pulled the result back toward a face-readable ensemble;
- Su / Liao / Guang became overly readable;
- Guang Yong carried too much visual weight;
- exterior brightness and floor reflection were excessive;
- ambiguous bag-like foreground element appeared.

Working conclusion:

`THE PRIMARY CORRECTION SHOULD REDUCE DIRECT NAMED-CHARACTER / PRIOR-STORY-SHOT PIXEL PRESSURE, NOT ADD MORE PROMPT RULES.`

---

## 3. CANDIDATE 02 CAMERA CONTRACT — UNCHANGED FROM V0.2.1

Hard geometry:

`LEFT = OPEN DOOR + CONTROLLED EXTERIOR LIGHT`

`CROWD = LEFT → RIGHT`

`RIGHT = DEEPER CASTLE INTERIOR`

`NEIL = BESIDE DOOR / NEAR-FRONTAL / HEAD-EYES SLIGHTLY RIGHT`

Story moment:

`TAIL END OF ENTRY / ALMOST EVERYONE ALREADY INSIDE`

Most visible crowd mass should be middle-right / right of Neil.

Camera family:

`SIDE / BROADSIDE THRESHOLD VIEW / MILDLY ELEVATED`

Do not return to:

`INTERIOR LOOKING BACK TOWARD PEOPLE APPROACHING LENS`

---

## 4. PROPOSED BUNDLE V002 REFERENCE ARCHITECTURE

Proposed formal input count:

`3`

### Reference 01｜AST_IMG_000052

Entity:

`SCENE_CASTLE_ENTRANCE`

Role:

`SCENE_MASTER / DAY_DOOR_OPEN`

Purpose:

`DOOR IDENTITY / MATERIAL / SCALE / OPEN STATE ONLY`

It must NOT control:

- screen-center placement;
- camera axis;
- doorway brightness;
- N23 composition.

The V0.2.1 text authority overrides Scene Master photography.

---

### Reference 02｜AST_IMG_000059

Entity:

`CHAR_NEIL`

Role:

`CHARACTER_REFERENCE_SHEET`

Purpose:

`NEIL IDENTITY / COSTUME / BODY PROPORTION`

N23 shot authority controls:

- beside-door position;
- near-frontal body;
- slight RIGHT head/eye direction;
- no door contact;
- no walking away.

---

### Reference 03｜AST_IMG_000013

Entity:

`CHAR_GUANG_YONG`

Role:

`REAR_3Q_RIGHT`

Asset class:

`ATOMIC / AUXILIARY`

Resolver usage:

`CONDITIONAL`

Purpose:

`LOW-WEIGHT GUANG YONG CONTINUITY WITHOUT FULL CHARACTER-SHEET PROMINENCE`

This replaces:

`AST_IMG_000056 / GUANG_YONG_CHARACTER_REFERENCE_SHEET`

Reason:

Candidate 01 showed that the full Guang Yong Character Sheet created too much identity / face pressure.

Candidate 02 should use only one rear-three-quarter identity cue so Guang can remain recognizable enough for continuity while staying visually subordinate.

---

## 5. DIRECT INPUTS TO REMOVE

### Remove N22 canonical Story Shot from Bundle V002

N22 remains:

`DIRECTOR-LEVEL CONTINUITY CHECK ONLY`

It does NOT enter Work as a generation image.

Reason:

Candidate 01 proved that the model interpreted the N22 pixel reference too strongly and recreated the N22 named-character ensemble.

Continuity retained without direct N22 pixels:

- same CASTLE_ENTRANCE event;
- same time;
- same warm-dark world;
- same contemporary everyday clothing language;
- Guang Yong as one low-weight continuity anchor;
- Product Owner visual review against N22 after generation.

### Remove AST_IMG_000056

Full Guang Yong Character Reference Sheet is excluded.

### Do not add CHARACTER_VISUAL_STYLE_REFERENCE_V001

Reason:

It contains multiple named-character face/body panels and could reintroduce ensemble identity pressure.

### Do not reuse N21_CROWD_BODY_WARDROBE_REFERENCE_V001

Reason:

Its canonical authority scope is explicitly:

`N21_CROWD_BODY_WARDROBE_ONLY`

Using it directly for N23 would exceed its approved authority scope.

No silent scope extension is allowed.

---

## 6. ANONYMOUS CROWD STRATEGY

Other crowd members are intentionally unseeded.

Work should generate:

- approximately 4–6 visible people / partial bodies;
- mostly middle-right / right of Neil;
- side / side-back / partial-profile bodies;
- different stride phases;
- natural overlap;
- ordinary contemporary clothing;
- no bags / luggage.

They should feel like the same cohort through:

- same scene and time;
- same clothing era;
- same lighting world;
- same crowd density;
- same movement continuity.

They do NOT need to repeat the exact N22 named faces.

Hard rule:

`SAME COHORT FEELING ≠ SAME READABLE NAMED ENSEMBLE`

---

## 7. GUANG YONG PLACEMENT

If visible:

- place Guang in the middle-right / right crowd;
- smaller than Neil;
- not foreground;
- rear-3Q / side-back preferred;
- body continues rightward;
- only a subtle backward-awareness cue if natural.

Do not require a clean face.

Do not force an exaggerated backward turn.

His role is:

`VISUAL ECHO FOR A06`

not:

`N23 SUBJECT`

---

## 8. LIGHTING CORRECTION

Door / exterior light stays on frame-left.

Compared with Candidate 01:

- reduce exterior bright area;
- no white sky-dominant opening;
- no broad floor reflection;
- no glossy light strip;
- preserve warm low-key interior dominance.

Recommended visual target:

`EXTERIOR = SMALL LEFT-EDGE SPATIAL CUE`

`INTERIOR = DOMINANT EXPOSURE WORLD`

---

## 9. ACCESSORY CORRECTION

Hard prohibit:

- backpack;
- shoulder bag;
- handbag;
- luggage;
- travel bag;
- crossbody strap;
- ambiguous bag-like foreground prop.

If any such element appears:

`SELF-CHECK = FAIL`

---

## 10. CANDIDATE 02 MODE

If later authorized:

`CLEAN REGENERATION`

Candidate 01 is:

`NEGATIVE / DIAGNOSTIC EVIDENCE ONLY`

Do not edit Candidate 01 pixels.

Planned output:

`EXACTLY 1 × PNG / 941 × 1672`

Then stop for Product Owner review.

---

## 11. CRITICAL ASSUMPTION

Critical assumption:

`REMOVING N22 DIRECT PIXELS + NARROWING GUANG YONG TO ONE REAR-3Q ATOMIC REFERENCE IS ENOUGH TO BREAK THE N22 ENSEMBLE BIAS WHILE PRESERVING CONTINUITY.`

Minimum proof:

`ONE CANDIDATE`

If Candidate 02 still collapses toward a frontal ensemble or centered doorway despite this reduced reference set, then the next step should be a dedicated N23 controlled composition/environment reference rather than more prompt accumulation.

---

## 12. PASS

Candidate 02 would pass the strategy test if:

1. door and controlled exterior light are clearly on LEFT;
2. people move LEFT → RIGHT;
3. most people are already right of Neil;
4. camera is side/broadside, not N22-like;
5. Neil is near-frontal beside door;
6. Neil looks slightly RIGHT toward group tail;
7. Neil does not touch/close door or leave;
8. Guang Yong remains tertiary;
9. no Su/Liao named-character reset;
10. no frontal ensemble;
11. warm-dark interior dominates;
12. no bags / luggage;
13. A06 remains unspent.

---

## 13. FAIL

Automatic fail if:

- N22-like frontal group composition returns;
- people approach camera;
- door shifts away from left-side role;
- crowd direction is not left→right;
- Neil looks left toward door/outside;
- Neil becomes hero portrait;
- Guang Yong becomes clearly readable co-lead;
- multiple named faces dominate;
- exterior / floor brightness dominates;
- any bag-like item appears;
- Neil walks away or closes the door.

---

## 14. CURRENT GATE

Status:

`DRAFT / WAITING PRODUCT OWNER APPROVAL`

If approved, next step:

`N23 REFERENCE DELIVERY BUNDLE V002 DESIGN`

Proposed V002 inputs:

1. `AST_IMG_000052`
2. `AST_IMG_000059`
3. `AST_IMG_000013`

Still not authorized:

- Bundle V002 Spec;
- validation-only run;
- formal Artifact build;
- Candidate 02 Work generation;
- N24;
- publication;
- registration.
