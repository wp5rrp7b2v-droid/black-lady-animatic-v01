# N21 Crowd Body / Wardrobe Reference V001｜Design + Build Spec

Date: 2026-10-01

Status:

`PRODUCT OWNER DIRECTION CONFIRMED / INPUT DESIGN LOCKED / SPEC + VALIDATION-ONLY PREP`

Reference target:

`N21_CROWD_BODY_WARDROBE_REFERENCE_V001`

Generation target:

`N21_CROWD_BODY_WARDROBE_REFERENCE_V001 Candidate 01`

Purpose:

`BODY POSTURE + CONTEMPORARY WARDROBE + PROJECT HUMAN-WORLD REFERENCE ONLY`

## 1. Why this reference exists

N21 Candidate 07 exposed a repeatable failure pattern in full-scene crowd generation:

- forward-head / shrunken-neck walking posture;
- hunched or rounded upper back;
- old-fashioned / 1970s–1980s-feeling wardrobe silhouettes;
- generic crowd appearance that does not read as the existing Black Lady human visual world.

The production response is to isolate the human problem before returning to N21 scene generation.

This reference is NOT a Story Shot and NOT an N21 candidate.

## 2. Formal source set

Use exactly four CURRENT APPROVED Atomic character anchors.

### REF-01｜Ning Qiushui rear 3/4 left

- asset: `AST_IMG_000051`
- role: `REAR_3Q_LEFT`
- authority: `AUXILIARY`
- path: `production/image_library/character_references/ning_qiushui/CHAR_NING_QIUSHUI_REAR_3Q_LEFT_DEFAULT_DEFAULT_V001.png`
- bytes: `1510968`
- SHA-256: `e3cbe5ca8be8584e1b3c48d3da6bb2555a619bf36f761ebeefa78734efcbfaf8`
- Git blob: `88e5908d1fcb003ee25dfb02d57e775a0671e307`

### REF-02｜Jun Luyuan rear 3/4 left

- asset: `AST_IMG_000064`
- role: `REAR_3Q_LEFT`
- authority: `AUXILIARY`
- path: `production/image_library/character_references/jun_luyuan/CHAR_JUN_LUYUAN_REAR_3Q_LEFT_DEFAULT_DEFAULT_V001.png`
- bytes: `1941468`
- SHA-256: `97ad38c259274eced5be61035cda4c28df72babe084fc452fbbc927a2a6da21e`
- Git blob: `6ebfadfa333159f1ae3871f4a61fd39526360fee`

### REF-03｜Su Xiaoxiao rear 3/4 left

- asset: `AST_IMG_000068`
- role: `REAR_3Q_LEFT`
- authority: `AUXILIARY`
- path: `production/image_library/character_references/su_xiaoxiao/CHAR_SU_XIAOXIAO_REAR_3Q_LEFT_DEFAULT_DEFAULT_V001.png`
- bytes: `2096951`
- SHA-256: `1fb43ffef96d36bebef05a6d08f297108684c026b9bd64a11543cd9614bd06f7`
- Git blob: `1628a3578c2ef356fb9e8354c109f107427c94be`

### REF-04｜Wen Qingya rear 3/4 left

- asset: `AST_IMG_000075`
- role: `REAR_3Q_LEFT`
- authority: `AUXILIARY`
- path: `production/image_library/character_references/wen_qingya/CHAR_WEN_QINGYA_REAR_3Q_LEFT_DEFAULT_DEFAULT_V001.png`
- bytes: `1902463`
- SHA-256: `2f52fe5067671d52f5b35eb9dc83567dbcd9bd76030ef1280a35e88e102c7344`
- Git blob: `50756c82f2ce2475db188c8d122b5a78419be4a9`

## 3. Source authority boundary

These four images are used to communicate:

- contemporary project wardrobe era;
- believable body proportions;
- project-consistent human silhouette;
- rear / rear-three-quarter body language;
- fabric and clothing realism.

They are NOT used to require:

- exact identity reproduction;
- exact face reproduction;
- exact outfit duplication;
- exact pose duplication;
- named-character casting of the four generated people.

The output may contain generic adults, but they must visibly belong to the same contemporary human world as the approved anchors.

## 4. Output design

Generate exactly one PNG reference board containing:

- four adults;
- full body visible;
- separated from one another;
- no overlap;
- no environment narrative;
- neutral plain background or transparent background;
- no castle;
- no doorway;
- no props.

Preferred viewpoint mix:

1. rear 3/4;
2. side;
3. rear 3/4;
4. side / partial profile.

The four people should be in different natural walking phases.

## 5. Posture lock

Every readable figure must show:

- naturally extended neck;
- neutral chin;
- relaxed lowered shoulders;
- open but not exaggerated chest;
- upright spine;
- neutral pelvis;
- normal walking stride;
- natural arm swing.

Hard fail:

- hunched back;
- forward-head posture;
- tucked / shrunken neck;
- shrugged shoulders;
- crouched gait;
- stealth-like gait;
- timid compressed posture;
- collective body lean.

## 6. Wardrobe lock

Target:

`CONTEMPORARY EVERYDAY VISITORS`

Use present-day casual / semi-casual clothing.

Avoid:

- 1970s / 1980s period feeling;
- retro-heavy silhouettes;
- repeated old-fashioned dark long coats;
- conservative period-looking outerwear;
- uniform gray-brown crowd styling;
- expedition-team styling.

Hard accessory exclusion:

- backpack;
- shoulder bag;
- crossbody bag;
- luggage;
- hiking equipment;
- expedition equipment.

## 7. Emotional / movement state

Do NOT express:

- fear;
- stealth;
- exploration;
- danger;
- cautious crouching.

The people are simply:

`NORMAL ADULTS WALKING NATURALLY`

This is intentional. Unknown-space emotion will be reintroduced later at Story Shot stage through environment and shot design, not through compressed body posture.

## 8. Governance classification if later approved

Proposed classification:

`P0.3_CONTROLLED_PRODUCTION_REFERENCE`

Proposed authority scope:

`N21_CROWD_BODY_WARDROBE_ONLY`

Proposed asset role:

`CONTROLLED_HUMAN_BODY_WARDROBE_REFERENCE`

It must NOT enter the locked P0.2 Asset Registry unless a separate schema decision is made.

If Product Owner later approves the generated binary, it should follow the same controlled-reference lifecycle:

`PO Approval → Exact Binary Verification → Canonical Publication → Controlled Reference Manifest → Project Control Closeout`

## 9. Current authorization boundary

This step authorizes:

- creation of the formal input bundle spec;
- validation-only exact input verification.

This step does NOT yet authorize:

- formal Bundle build;
- Work generation;
- canonical publication of the new reference;
- N21 Candidate 08;
- N22.

Next after validation-only PASS:

`Product Owner authorization → Formal input Bundle build → Work Candidate 01 generation`
