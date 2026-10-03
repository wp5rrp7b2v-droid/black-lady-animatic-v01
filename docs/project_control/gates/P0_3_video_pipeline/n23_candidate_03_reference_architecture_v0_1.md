# N23 Candidate 03｜Reference Architecture V0.1

Status:

`PRODUCT OWNER APPROVED / LOCKED / DIRECT VISUAL CAP = 5 / CURRENT PLANNED INPUTS = 4 / DOOR CONTROL CANONICAL / BUNDLE V003 DESIGN PROPOSED`

Date:

`2026-10-03`

Target:

`N23 Candidate 03`

Parent strategy:

`N23 Candidate 03 Correction Strategy V0.1`

---

## 1. REFERENCE-BUDGET RULE

Direct generation-image budget:

`MAXIMUM 5`

This is a hard Candidate 03 production rule.

No later Bundle design may silently add a sixth direct visual reference.

If more evidence is needed:

`COMPRESS / CROP / CONTROL / REMOVE`

not:

`ADD ANOTHER DIRECT IMAGE`

---

## 2. REFERENCE ARCHITECTURE

### SLOT 1｜Door identity / scene fact

Canonical reference:

`N23_CASTLE_ENTRANCE_DOOR_CONTROL_REFERENCE_V001`

Source:

`AST_IMG_000052`

Type:

`CONTROLLED_REFERENCE / DETERMINISTIC CROP`

Purpose:

`DOOR IDENTITY / MATERIAL / SCALE / OPEN STATE ONLY`

Why not full Scene Master:

`REDUCE EXTERIOR-LIGHT / FLOOR-REFLECTION PHOTOGRAPHIC PRESSURE`

---

### SLOT 2｜Neil identity

Reference:

`AST_IMG_000073`

Entity:

`CHAR_NEIL`

Role:

`FACE_3Q_RIGHT`

Approval:

`APPROVED / CURRENT`

Exact identity:

- byte size: `1,738,212`
- SHA-256: `92ef0fc973093c7cc99f3b70f3aab1fabd09d2d82c29921e72065f0d7b9ac366`
- Git blob: `8179b112aae5253c0f8d9dffe4cfe451d94dacbc`

Purpose:

`ANGLE-SPECIFIC NEIL FACE IDENTITY LOCK`

The reference angle does not override shot-specific subtle gaze / head-turn amount.

---

### SLOT 3｜Guang identity only

Reference:

`AST_IMG_000011`

Entity:

`CHAR_GUANG_YONG`

Role:

`FACE_FRONT`

Authority:

`MASTER`

Approval:

`APPROVED / CURRENT`

Resolver usage:

`DEFAULT`

Exact identity:

- byte size: `2,903,455`
- SHA-256: `7f88a3f8d68dbfea0058ff0379d0164380722d96ae1774364bcd8b79367ad6f5`
- Git blob: `5490cd3101d0d878ef77b4a3a164ea2231bf3817`

Purpose:

`GUANG IDENTITY ONLY`

Why FACE_FRONT replaces FACE_3Q_RIGHT:

- `RIGHT` means face/nose toward screen-right under project orientation governance;
- Candidate 03 requires Guang's body to keep moving screen-right while retaining a small backward-attention cue toward frame-left / Neil / the open door;
- a FACE_3Q_RIGHT image would add unnecessary opposite head-direction pressure;
- FACE_FRONT is the more neutral identity anchor.

Shot-specific head direction and behavior come from written shot authority only. SLOT 3 must not override them.

---

### SLOT 4｜Anonymous crowd identity pool

Reference:

`BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q`

Purpose:

`GENERIC GUEST A–J SIDE-BACK / REAR-3Q IDENTITY CONTINUITY`

Why REAR_3Q only:

- enough rear-side identity evidence;
- avoids the Candidate 02 full-BACK procession pressure;
- preserves more lateral body readability.

Non-delivered governance:

`GENERIC GUEST FRONT = GLOBAL IDENTITY AUTHORITY / FRONT WINS`

---

### SLOT 5｜UNUSED / RESERVED

Previously proposed reference:

`N23_N22_MOTION_OBSERVATION_REFERENCE_V001`

Status:

`CANCELLED / DO NOT BUILD / DO NOT DELIVER`

Reason:

The N22 canonical Story Shot does not provide reliable direct visual proof of the required LEFT → RIGHT lateral movement or Guang's backward-awareness behavior. Cropping cannot manufacture that evidence.

Candidate 03 therefore uses four direct visual inputs, not five.

The hard cap remains five, but there is no requirement to fill every slot.

Movement and Guang behavior are written shot requirements to be tested in Candidate 03. If a later failure proves that a true visual action reference is necessary, a future revision may use the reserved fifth slot only with valid source evidence.

---

## 3. EXCLUDED DIRECT INPUTS

Do not deliver:

- `AST_IMG_000052` full Scene Master;
- `AST_IMG_000059` Neil Character Reference Sheet;
- `AST_IMG_000013` Guang REAR_3Q_RIGHT;
- `AST_IMG_000010` Guang FACE_3Q_RIGHT;
- Generic Guest BACK;
- Generic Guest FRONT;
- Generic Guest LEFT_PROFILE;
- full N22 canonical Story Shot;
- proposed `N23_N22_MOTION_OBSERVATION_REFERENCE_V001`;
- Candidate 02;
- any N21-specific human reference;
- Character Visual Style Reference.

---

## 4. WHY THIS FITS THE FAILURE EVIDENCE

Candidate 02 failure → Candidate 03 slot response:

### Motion axis failed
→ No valid direct visual reference currently proves the desired lateral motion. Candidate 03 tests this through written shot authority; this remains a working hypothesis.

### Guang observation disappeared
→ SLOT 3 locks Guang identity only with a neutral FACE_FRONT anchor. Backward-awareness behavior and shot-specific head direction remain written shot requirements and are not claimed as visually proven.

### Neil identity drifted
→ SLOT 2 replaces broad Character Sheet pressure with angle-specific face identity.

### Crowd became too back-facing
→ SLOT 4 keeps REAR_3Q and removes BACK.

### Lighting remained too bright
→ SLOT 1 replaces full Scene Master with door-only controlled crop.

No failure currently justifies a sixth direct image.

---

## 5. PRIORITY ORDER

Shot-specific authority:

`CANDIDATE 03 STRATEGY + N23 SCENE REFERENCE > REFERENCE PIXEL COMPOSITION`

Direct-reference semantic priority:

1. Neil identity — SLOT 2
2. door identity — SLOT 1
3. Generic Guest identity — SLOT 4
4. Guang identity detail — SLOT 3

Movement / Guang behavior are controlled by shot authority, not by a direct visual slot in the current attempt.

This priority list does NOT imply screen prominence.

---

## 6. BUILD DEPENDENCIES

Door Control now exists, is Product Owner approved, exact-verified, and canonically published. The dependency for Bundle V003 design is satisfied.

Required intermediate gates:

Completed:

- `N23_CASTLE_ENTRANCE_DOOR_CONTROL_REFERENCE_V001｜Exact Crop Plan V0.2｜PRODUCT OWNER APPROVED`
- `Deterministic Build + Exact Binary Verification｜PASS`
- `Canonical publication｜PASS / commit 74c4cea6d52358e038e112427a411f9d348ede52`

Current:

`N23_REFERENCE_DELIVERY_BUNDLE_V003 DESIGN / PRODUCT OWNER REVIEW`

---

## 7. CURRENT GATE

Status:

`PRODUCT OWNER APPROVED / LOCKED / DOOR CONTROL CANONICAL / BUNDLE V003 DESIGN UNDER PRODUCT OWNER REVIEW`

Product Owner has approved two targeted architecture corrections:

- `AST_IMG_000010 FACE_3Q_RIGHT → AST_IMG_000011 FACE_FRONT / IDENTITY ONLY`
- `CANCEL N23_N22_MOTION_OBSERVATION_REFERENCE_V001 / CURRENT ATTEMPT USES 4 DIRECT VISUAL INPUTS`

The complete corrected architecture is Product Owner approved and locked.

Door Control crop/build/publication is complete. Bundle V003 Design V0.1 has been prepared with exactly four direct visual inputs and is waiting Product Owner review. Bundle V003 Spec, validation, formal build, and Candidate 03 generation remain unauthorized.
