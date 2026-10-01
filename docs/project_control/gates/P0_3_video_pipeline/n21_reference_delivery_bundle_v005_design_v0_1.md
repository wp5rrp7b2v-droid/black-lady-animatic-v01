# N21 Reference Delivery Bundle V005｜Design V0.1

Date: 2026-10-01

Status:

`PRODUCT OWNER APPROVED / LOCKED / SPEC CREATED / VALIDATION-ONLY PASS / FORMAL BUILD NOT AUTHORIZED / CANDIDATE 07 NOT AUTHORIZED`

Target:

`N21｜Cohort Enters — Into the Unknown`

Future candidate:

`N21 Candidate 07｜Clean Regeneration`

Future bundle:

`N21_REFERENCE_DELIVERY_BUNDLE_V005`

## 1. Design purpose

Candidate 05 and Candidate 06 showed that the previous direct Scene Master input did not sufficiently constrain the generator toward the intended threshold-transition space.

A new controlled environment reference has now been Product Owner approved, canonically published and exact-binary verified:

`N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001`

V005 therefore changes the input structure from:

`Scene Master + Character Visual Style Reference`

to:

`Controlled Environment Reference + Character Visual Style Reference`

The goal is to separate:

- environment / threshold / lighting / tonal control;
- human rendering-language control.

No complete Story Shot is delivered to generation.

No complete Scene Master is delivered directly to generation.

## 2. Formal reference count

V005 shall contain exactly:

`2 formal image references`

No third image is proposed.

## 3. REF-01｜Threshold Environment Reference

Reference ID:

`N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001`

Source type:

`CONTROLLED_REFERENCE`

Classification:

`P0.3_CONTROLLED_PRODUCTION_REFERENCE`

Approval:

`PRODUCT_OWNER_APPROVED`

Lifecycle:

`CURRENT`

Authority scope:

`N21_THRESHOLD_TRANSITION_ENVIRONMENT_ONLY`

Canonical PNG:

`production/environment_references/n21_threshold_transition/N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001.png`

Manifest:

`production/environment_references/n21_threshold_transition/N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001.manifest.json`

Exact binary identity:

- width: `941`
- height: `1672`
- mode: `RGBA`
- byte size: `3394494`
- SHA-256: `dd1b2dc6b831b2e22d8dc249859af1b4f65da6a20437cd8821627144e89a4f13`
- Git blob: `358057948ec222bbe63a47a07022de4453e20fc8`

May control:

- threshold-transition spatial staging;
- usable doorway width and perceived scale;
- interior-to-interior threshold relationship;
- warm low-key environmental continuity;
- stone / wood / floor environmental language;
- partial concealment of deeper space;
- partial / incomplete First Hall visibility.

Must NOT control:

- strict reverse-angle geometry of AST_IMG_000052;
- complete First Hall layout;
- character identity;
- character wardrobe;
- crowd pose;
- exact final Story Shot composition.

## 4. REF-02｜Character Visual Style Reference

Reference ID:

`CHARACTER_VISUAL_STYLE_REFERENCE_V001`

Source type:

`CONTROLLED_REFERENCE`

Classification:

`P0.3_CONTROLLED_PRODUCTION_REFERENCE`

Approval:

`PRODUCT_OWNER_APPROVED`

Lifecycle:

`CURRENT`

Authority scope:

`CHARACTER_VISUAL_STYLE_ONLY`

Canonical PNG:

`production/style_references/character_visual/CHARACTER_VISUAL_STYLE_REFERENCE_V001.png`

Manifest:

`production/style_references/character_visual/CHARACTER_VISUAL_STYLE_REFERENCE_V001.manifest.json`

Exact binary identity:

- width: `1536`
- height: `1024`
- mode: `RGB`
- byte size: `1301730`
- SHA-256: `8d650483b6e082a80d41d93e14c7957595c451097aac63f3c84cbcc1ddc7ce41`
- Git blob: `216b1739db17cb3b183d613e4aefa6374d1088e2`

May control:

- realistic adult human rendering;
- facial realism;
- natural skin treatment;
- hair realism;
- adult age variation;
- believable body realism;
- clothing / fabric material rendering.

Must NOT control:

- named-character identity;
- complete outfit;
- pose;
- crowd arrangement;
- scene;
- shot composition.

## 5. Explicitly excluded generation inputs

Do not include in V005:

- `AST_IMG_000052` as a direct image input;
- N20 as a direct image input;
- N19;
- N03;
- N08;
- any complete Story Shot;
- any complete Scene Master;
- any named-character Character Sheet;
- any Ning Qiushui Character Sheet or Atomic appearance reference;
- any Jun Luyuan Character Sheet or Atomic appearance reference;
- N21 Candidate 01–06;
- any rejected threshold-environment proof;
- A07;
- unrelated castle interiors.

These may remain Project Control / Director history only.

## 6. Candidate 07 generation mode

If separately authorized after V005 formal build and exact verification:

`N21 Candidate 07 = CLEAN REGENERATION`

Candidate 01–06 are not edit bases.

They are not style inputs.

They are not composition inputs.

## 7. Candidate 07 core narrative function

The N21 single-frame responsibility remains:

`THRESHOLD TRANSITION + UNKNOWN-SPACE MOOD`

First read:

`A GROUP OF PARTICIPANTS HAS JUST CROSSED INTO A DARKER, UNKNOWN CASTLE INTERIOR`

The shot does NOT need to prove all 16 participants in one frame.

Preferred readable complexity:

`approximately 4–6 people`

Remaining cohort presence may be implied through:

- partial bodies;
- crop;
- occlusion;
- deeper figures;
- off-frame continuation.

## 8. Environment execution lock

The environment reference is now the primary visual authority for space.

Candidate 07 should preserve:

- wide enough threshold for multiple people to pass naturally;
- interior-to-interior relationship;
- no outdoor / blue-sky reading;
- low-key warm castle interior;
- visible practical warm lights;
- deeper space becoming darker;
- incomplete knowledge of the space ahead;
- no complete First Hall reveal.

Do NOT re-invent the entrance as:

- narrow side door;
- cathedral;
- monumental symmetrical portal;
- bright exterior entrance;
- large daylight-flooded architecture showcase.

The approved environment reference is not a strict reverse-angle reconstruction; Candidate 07 must not claim geometric precision beyond what the reference actually establishes.

## 9. Crowd blocking lock

The crowd must not form a single-file queue.

Preferred state:

`STAGGERED THRESHOLD CLUSTER / NATURAL DEPTH VARIATION`

Required behavior:

- different lateral positions;
- different depths;
- different stride phases;
- some figures already slightly deeper inside;
- some nearer the threshold;
- no central leader axis;
- no repeated equal spacing;
- no synchronized walk cycle;
- no collective turn toward camera.

Body posture:

- upright spine;
- natural pelvis / torso alignment;
- relaxed shoulders;
- cautious but not hunched.

Hard accessory exclusion:

`NO BACKPACKS / NO SHOULDER BAGS / NO CROSSBODY BAGS / NO LUGGAGE`

Wardrobe should read as varied ordinary contemporary clothing, not an organized hiking / expedition team.

## 10. Character identity policy

Ning Qiushui and Jun Luyuan are not mandatory identity targets in N21.

They must not be deliberately staged as a hero pair.

No named-character seeding is required in this shot.

If any figure incidentally becomes recognizable enough for identity judgment, it must not visibly contradict the established project visual world.

N22 remains the downstream node responsible for more deliberate named-character seeding.

## 11. Lighting / color lock

Primary target:

`APPROVED THRESHOLD ENVIRONMENT REFERENCE VISUAL WORLD`

Required:

- warm low-key interior;
- practical lamps / sconces as believable local sources;
- restrained saturation;
- dark areas retain material texture;
- no large daylight field;
- no blue reset;
- no orange wash;
- no commercial advertising light;
- no theatrical god-rays;
- no bright polished lobby look.

## 12. Artifact layout

Future V005 Artifact should contain:

`N21_REFERENCE_DELIVERY_BUNDLE_V005/`

- `delivery_manifest.json`
- `WORK_HANDOFF.md`
- `environment_authority/N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001.png`
- `character_visual_style_authority/CHARACTER_VISUAL_STYLE_REFERENCE_V001.png`

Product Owner manual reference upload:

`0`

Transport:

`GitHub Actions → Artifact → Work automatic acquisition`

## 13. Builder validation contract

Both references are `CONTROLLED_REFERENCE`.

The existing fail-closed CONTROLLED_REFERENCE verification contract applies independently to both.

For each reference, Builder must verify:

1. canonical PNG exists;
2. sidecar manifest exists;
3. manifest reference_id matches;
4. classification matches;
5. approval_status = PRODUCT_OWNER_APPROVED;
6. lifecycle = CURRENT;
7. authority_scope matches;
8. canonical path matches;
9. expected SHA-256 matches manifest and actual file;
10. expected byte size matches manifest and actual file;
11. expected Git blob matches manifest and actual file;
12. PNG signature / dimensions readable;
13. Artifact copy remains byte-identical.

Any mismatch:

`FAIL CLOSED / GENERATION_ALLOWED=FALSE`

## 14. Build authorization boundary

This design does NOT authorize:

- creation of V005 Bundle Spec;
- formal GitHub Actions build;
- Artifact creation;
- Work generation;
- Candidate 07;
- Candidate 08;
- N22;
- canonical Story Shot publication;
- Story Shot registration.

Product Owner approved this design on 2026-10-01.

V005 Spec was then created and validation-only executed successfully.

Formal build remains a separate authorization.

## 15. Current recommendation

`V005 TWO-CONTROLLED-REFERENCE STRUCTURE APPROVED / LOCKED`

Reason:

V005 is the first N21 input structure in which:

- environment is represented by an approved shot-specific controlled environment reference;
- human visual style is represented by an approved content-minimized style reference;
- complete Scene Master and complete Story Shot content are both removed from direct generation input.

This isolates the remaining real generation risk to:

`CROWD STAGING / BODY PERFORMANCE`

rather than repeatedly forcing the generator to reconstruct space, lighting and character style simultaneously.

RISK-003 remains ACTIVE until Candidate 07 provides real evidence.
