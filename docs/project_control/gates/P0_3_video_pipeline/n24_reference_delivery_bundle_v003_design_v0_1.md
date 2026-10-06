# N24_REFERENCE_DELIVERY_BUNDLE_V003｜Design V0.1

Date:

`2026-10-06`

Status:

`PRODUCT OWNER APPROVED / LOCKED / SPEC + VALIDATION-ONLY AUTHORIZED / FORMAL BUILD NOT YET AUTHORIZED`

Target:

`N24 Candidate 01｜Clean Regeneration`

Trigger:

Formal Bundle V002 was exact-verified 6/6, but Work stopped before generation because the image-generation interface accepts at most 5 direct referenced images.

## 1. Design principle

Do not weaken the N24 shot design.

Reduce only redundant direct-image evidence.

The direct-image cap is:

`MAX 5`

Therefore V003 uses exactly five direct PNG references.

## 2. Removed reference

Remove:

`N23_APPROVED_STORY_SHOT`

Reason:

- N23 is two edits earlier in the active sequence: `N23 → A06 → N24`;
- A06 is the direct preceding Story Shot;
- A06 already establishes the open-door fact and the immediate movement-away-from-entrance continuity needed by N24;
- N23 contributes earlier entrance-zone continuity but no unique identity or scene fact unavailable elsewhere;
- SCENE_CASTLE_ENTRANCE V002 continues to preserve formal space authority.

N23 remains historical continuity evidence in Project Control, but is no longer a direct image passed to the generation interface.

## 3. V003 direct visual inputs — EXACTLY 5

### 1. A06 Approved Story Shot
Role:

`DIRECT PRECEDING CONTINUITY / OPEN-DOOR PREMISE`

Controls:

- door remains open as already established;
- immediate edit continuity into N24.

Does not control:

- N24 camera;
- door-primary composition.

### 2. AST_IMG_000013｜CHAR_GUANG_YONG｜REAR_3Q_RIGHT V001
Role:

`PRIMARY SPEAKER IDENTITY`

Controls:

- Guang Yong identity;
- short / naturally slightly chubby build;
- rear-3Q turned-back speaking anchor.

### 3. AST_IMG_000066｜CHAR_NEIL｜REAR_3Q_RIGHT V001
Role:

`ADDRESSED CHARACTER IDENTITY`

Controls:

- Neil identity;
- secondary forward / rear-3Q target;
- not speaking yet.

### 4. AST_IMG_000105｜SCENE_CASTLE_ENTRANCE V002
Role:

`SCENE AUTHORITY`

Controls:

- Castle Entrance architecture;
- DAY / DOOR_OPEN scene facts;
- light / material family;
- short interior transition context.

### 5. BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q
Role:

`MOVING CROWD LANGUAGE`

Controls:

- anonymous guest proportions / wardrobe / rear-3Q movement language;
- natural stagger / overlap.

Does not control:

- 2×5 board layout;
- full ten-person inclusion;
- queue.

## 4. Authority order

1. N24 Director Design V0.3
2. N24 Scene Reference Design V0.2
3. Guang Yong identity
4. A06 direct preceding continuity
5. Neil identity
6. Castle Entrance scene facts
7. Generic Guest crowd language

N23 remains a non-delivered historical continuity source only.

## 5. Work handoff core

First read:

`GUANG YONG IS ASKING THE QUESTION`

Dialogue:

`尼尔管家，不需要关城堡大门吗？`

Second read:

`HE IS STILL MOVING WITH THE GROUP AND TURNS BACK TOWARD THE ENTRANCE SIDE`

Third read:

`NEIL IS BEING ADDRESSED BUT HAS NOT STARTED HIS ANSWER`

A06 already established the open door.

Do not repeat A06 as a door-primary composition.

## 6. Hard exclusions

- N23 as direct generation image;
- old Bundle V001;
- Bundle V002 as direct generation input;
- First Hall reference;
- more than 5 direct images;
- door-primary composition;
- Neil-primary composition;
- Neil answering;
- stopped / posed Guang Yong;
- queue / equal spacing / synchronized walking;
- bags / luggage;
- dirty / noisy / cutout rendering.

## 7. Expected production path if approved

1. create V003 Spec with `build_authorized=false`;
2. Validation-only = exactly `5/5`;
3. expected Artifact count = `0`;
4. separate Product Owner authorization for Formal Build;
5. Formal Build + Artifact exact verification;
6. separate / renewed Candidate 01 generation authorization against V003;
7. Work generates exactly 1 PNG and stops.

## 8. Current gate

`PRODUCT OWNER APPROVED / LOCKED / PROCEED TO V003 SPEC + VALIDATION-ONLY`
