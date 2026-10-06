# N24｜Scene Reference Design V0.3

Date:

`2026-10-06`

Status:

`DESIGN COMPLETE / WAITING PRODUCT OWNER APPROVAL`

Upper authority:

- `N24 Node-Level Director Shot Design V0.4｜PRODUCT OWNER APPROVED / LOCKED`
- active sequence: `N23 → A06 → N24 → N25 → N26 → N27`
- Work direct-image limit: `<= 5`

## 1. Scene-reference objective

N24 V0.4 is no longer a moving rear-3Q group shot.

It is a front-facing Guang Yong question shot:

- the group has already entered and paused;
- Guang Yong is the first subject;
- other guests are dispersed behind him;
- Neil remains on the entrance side / behind the group;
- the door position is communicated mainly through entrance-side light and spatial orientation;
- the door itself does not need to dominate or even appear clearly.

Therefore the Scene Reference strategy must prioritize:

`GUANG YONG IDENTITY > PAUSED-GROUP RELATION > CASTLE ENTRANCE LIGHT / SPACE > NEIL DIRECT VISIBILITY`

## 2. Key correction from V0.2 / Bundle V003

Do not reuse the old V003 reference balance.

Old V003 allocated direct slots to:

- A06
- Guang Yong REAR_3Q_RIGHT
- Neil REAR_3Q_RIGHT
- Castle Entrance V002
- Generic Guest REAR_3Q

That balance was appropriate for the old rear-moving composition but is not appropriate for V0.4.

For V0.4:

- Guang Yong requires stronger frontal identity control;
- rear-3Q Guang Yong alone is insufficient;
- Neil does not need to be a second strong visible subject;
- A06 can remain editorial continuity evidence instead of consuming a direct generation slot;
- crowd reference should support a paused background facing the entrance side, not walking away from camera.

## 3. Recommended reference strategy

### A. Guang Yong identity — highest priority

Use multiple direct Guang Yong references.

Recommended:

#### 1. Guang Yong Character Reference Sheet
`AST_IMG_000056｜CHAR_GUANG_YONG_CHARACTER_REFERENCE_SHEET V001`

Purpose:

- overall identity consolidation;
- face / body / wardrobe consistency;
- reduce generic middle-aged-man substitution.

This should become the strongest identity overview reference.

#### 2. Guang Yong FACE_3Q_RIGHT
`AST_IMG_000010｜CHAR_GUANG_YONG_FACE_3Q_RIGHT V001`

Purpose:

- face structure;
- hair;
- age;
- speaking-face identity;
- slight 3Q frontal angle suitable for addressing entrance-side Neil.

#### 3. Guang Yong BODY_FRONT
`AST_IMG_000009｜CHAR_GUANG_YONG_BODY_FRONT V001`

Purpose:

- short / naturally slightly chubby body proportion;
- wardrobe;
- frontal body identity;
- prevent tall / athletic / generic reinterpretation.

These three references together should have higher priority than crowd completeness.

## 4. Scene authority

#### 4. SCENE_CASTLE_ENTRANCE V002
`AST_IMG_000105`

Purpose:

- immediate interior architecture;
- entrance-side light direction;
- DAY / DOOR_OPEN scene state;
- material / tonal family;
- spatial opening cues.

Important:

This reference controls scene facts and light family only.

It must NOT force:

- a large visible door;
- bright exterior;
- doorway-primary composition;
- exact camera match.

The preferred N24 shot can keep the door off-screen and use only directional light to imply the entrance.

## 5. Background crowd reference

For V0.4, the background guests are behind Guang Yong and generally oriented toward the entrance / Neil side.

Therefore the preferred crowd authority should be:

`Generic Guest FRONT / FRONT-3Q compatible authority`

rather than REAR_3Q walking-away authority.

Purpose:

- secondary guest identity / wardrobe family;
- paused group behind Guang Yong;
- irregular spacing;
- no queue;
- no synchronized pose.

The crowd reference is subordinate to Guang Yong identity.

If a suitable approved FRONT board is used, its 2×5 board layout is NOT compositional authority.

## 6. Neil visibility decision

Neil does NOT need to consume a direct-image slot unless later blocking requires him visibly in frame.

Preferred first attempt:

`NEIL OFF-SCREEN OR EXTREMELY WEAK EDGE PRESENCE`

Reason:

- camera is effectively located on / near the entrance-side Neil axis;
- Guang Yong can address Neil toward camera / just off-camera;
- this protects Guang Yong as sole first-read subject;
- it avoids the Candidate 01 failure where Neil became a competing large figure.

Neil remains narratively present but may be visually off-screen.

If Neil must later become visible, a future Bundle revision can trade one lower-priority reference slot for Neil identity.

## 7. A06 role

A06 remains important editorial continuity evidence:

`A06 = THE DOOR IS STILL OPEN`

But A06 does NOT need to be a direct generation image in the next Bundle.

Reason:

- the open-door fact has already been established by editing;
- V0.4 specifically avoids repeating A06 visually;
- Castle Entrance V002 already supplies scene / light authority;
- direct slots are more valuable for Guang Yong identity.

Therefore:

`A06 = PROJECT CONTROL / EDITORIAL CONTINUITY EVIDENCE, NOT REQUIRED DIRECT IMAGE`

## 8. Recommended direct-image set for next Bundle

Target:

`EXACTLY 5 DIRECT IMAGES`

Recommended set:

1. `AST_IMG_000056｜GUANG YONG CHARACTER REFERENCE SHEET`
2. `AST_IMG_000010｜GUANG YONG FACE_3Q_RIGHT`
3. `AST_IMG_000009｜GUANG YONG BODY_FRONT`
4. `AST_IMG_000105｜SCENE_CASTLE_ENTRANCE V002`
5. `GENERIC GUEST FRONT AUTHORITY`

No A06 direct image.

No N23 direct image.

No Neil direct image for the first V0.4 attempt.

## 9. Expected composition supported by this reference set

The next generation should read as:

- Guang Yong in foreground / near-midground;
- frontal or slight 3Q;
- stopped and speaking;
- other guests dispersed behind him;
- guests have already entered and paused;
- group is facing generally toward entrance-side Neil;
- entrance direction is implied through light / tonal gradient;
- no large door required;
- Neil may remain off-screen;
- background remains secondary.

## 10. Hard reference-governance rules

- Work-direct reference count must stay `<=5`.
- Do not silently add A06, N23 or Neil as a sixth image.
- Do not merge or collage references without a separately approved controlled-reference design.
- Reference Sheet controls identity, not sheet layout.
- Generic Guest board controls identity / wardrobe family, not grid layout.
- Castle Entrance controls scene facts / light family, not camera composition.

## 11. No new dedicated environment reference

No new N24-specific environment image is required at this stage.

Reason:

- Castle Entrance V002 already contains sufficient scene authority;
- the main failure was character identity and blocking, not environment ambiguity;
- adding a new environment reference would consume scarce direct-image capacity.

## 12. Current recommendation

Proceed with the five-reference strategy above.

If Product Owner approves:

`N24_REFERENCE_DELIVERY_BUNDLE_V004 Design V0.1`

should be created around:

- 3× Guang Yong identity
- 1× Castle Entrance V002
- 1× paused-background Generic Guest FRONT authority

with A06 / N23 / Neil retained as non-delivered Project Control evidence.

## 13. Current gate

`WAITING PRODUCT OWNER APPROVAL`
