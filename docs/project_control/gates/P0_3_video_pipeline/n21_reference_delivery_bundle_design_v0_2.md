# N21｜Reference Delivery Bundle Design V0.2

Status: `PRODUCT OWNER APPROVED / LOCKED / BUILT / 2 OF 2 PASS / TECHNICALLY VALID / FURTHER USE PAUSED`

Date: 2026-09-30

Target shot:

`N21｜Cohort Enters — Scale Reveal`

Target candidate:

`N21 Candidate 01`

Target bundle:

`N21_REFERENCE_DELIVERY_BUNDLE_V002`

Scene authority:

`N21 Scene Reference Design V0.3 / PRODUCT OWNER APPROVED + LOCKED`

Director authority:

`N21 Node-Level Director Shot Design V0.1 / PRODUCT OWNER APPROVED + LOCKED`

Supersedes for generation:

`N21_REFERENCE_DELIVERY_BUNDLE_V001`

## 1. Design objective

Build the smallest practical formal generation reference set for N21.

Primary design principle:

`MINIMUM NECESSARY AUTHORITY / REDUCE CROWD REFERENCE CONFLICT`

Formal generation reference count:

`2`

The Bundle must support only:

1. castle entrance / open-door scene authority;
2. immediate N20→N21 continuity.

Crowd count, crowd movement and crowd-complexity rules remain Director / Work instruction authority and are not represented by extra image references.

## 2. Formal reference set

### REF-01｜Castle Entrance Scene Master

- reference_id: `AST_IMG_000052`
- entity_id: `SCENE_CASTLE_ENTRANCE`
- role: `SCENE_MASTER`
- state: `DAY_DOOR_OPEN`
- authority_class: `MASTER`
- approval / lifecycle: `APPROVED / CURRENT`
- canonical_path: `production/image_library/scene_masters/castle_entrance/SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`
- expected SHA-256: `d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961`
- expected byte_size: `2305753`
- expected Git blob: `e4dafe096f5c5c8782257030a5a659aeec7808f9`
- destination_group: `scene_authority`

Authority purpose:

- castle entrance architecture;
- open-door state;
- material / spatial facts.

Must NOT force:

- exact camera angle;
- empty-scene composition;
- exterior-dominant lighting.

### REF-02｜N20 Canonical Story Shot

- reference_id: `N20`
- source_type: `STORY_SHOT`
- approval / lifecycle: `APPROVED / CURRENT`
- canonical_path: `production/image_library/approved/story_shots/N20_DO_NOT_TOUCH_THINGS_APPROVED_V001.png`
- expected SHA-256: `a61ab1310e86938b2a416516138981aafaf421add44c1a9d5a80d0ff9ec59a9e`
- expected byte_size: `2022630`
- expected Git blob: `58e145a51c3f993827e5e47964ad0e7f9dd9f0aa`
- dimensions: `941x1672`
- destination_group: `immediate_story_continuity`

Authority purpose:

- immediate visual continuity;
- current Ning / Jun appearance and wardrobe;
- warm low-key color / lighting baseline;
- entrance-to-interior transition state.

Must NOT control:

- two-person dominance;
- exact N20 pose;
- exact camera;
- private-dialogue staging.

Hard rule:

`PRESERVE CONTINUITY / EXPAND TO GROUP SCALE`

## 3. Removed from V001

The following V001 references are removed from N21 generation:

- `AST_IMG_000061` — Su Xiaoxiao
- `AST_IMG_000058` — Liao Jian
- `AST_IMG_000062` — Wen Qingya
- `AST_IMG_000056` — Guang Yong

Reason:

`NAMED CHARACTER SEEDING MOVED TO N22`

Keeping them in N21 would create unnecessary identity pressure and increase the risk of a promotional ensemble / rigid group composition.

## 4. Why Ning / Jun Character Sheets remain excluded

N20 is the immediate approved preceding Story Shot and already carries:

- both characters together;
- current wardrobe;
- current production appearance;
- correct scene / lighting state.

N21 intentionally lowers their prominence.

Therefore separate Ning / Jun Character Sheets are not added pre-emptively.

If a future Candidate shows material identity drift, targeted Bundle augmentation may be considered then.

## 5. A03 disposition

`A03｜门内反拍`

remains:

`DIRECTOR / SPATIAL REVIEW AUTHORITY ONLY`

It is not a generation input because:

- AST_IMG_000052 already supplies scene facts;
- N20 supplies current continuity;
- A03 would add another camera/composition influence and reduce the composition freedom approved under V0.3.

## 6. Prior group-shot disposition

Previously approved group shots are not formal generation references for N21.

Reason:

Product Owner has judged earlier group staging only marginally acceptable and specifically wants better crowd movement / naturalism from N21 onward.

Those shots may inform:

`LESSONS LEARNED / NEGATIVE REVIEW`

but must not teach Work the target crowd composition.

## 7. Work handoff constraints

The eventual Work handoff must explicitly state:

- 16 total participants as story truth;
- visual group scale must plausibly support all 16;
- do not force 16 equally clear faces / bodies;
- prefer only ~4–6 comparatively readable figures;
- global movement direction = entrance → interior;
- local gait / body states must be asynchronous;
- use natural occlusion / depth / cropping;
- avoid lineup / publicity-photo staging;
- avoid clone faces / repeated bodies;
- avoid synchronized strides;
- keep clear frontal faces limited;
- reduce exposed complex hand gestures;
- Ning / Jun remain continuity figures but secondary;
- Neil absent;
- no named-character-seeding task;
- no First Hall reveal;
- match N20 visual world.

## 8. Planned artifact structure

`N21_REFERENCE_DELIVERY_BUNDLE_V002/`

- `delivery_manifest.json`
- `WORK_HANDOFF.md`
- `scene_authority/AST_IMG_000052__SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`
- `immediate_story_continuity/N20__N20_DO_NOT_TOUCH_THINGS_APPROVED_V001.png`

Product Owner manual reference upload:

`0`

Transport:

`GitHub Actions → Artifact → Work automatic acquisition`

## 9. Builder contract

Use existing fixed workflow only:

`.github/workflows/story-shot-reference-bundle-builder.yml`

Do not create an N21-specific builder.

Future build must fail closed unless both references pass:

- canonical path;
- approval / lifecycle where applicable;
- byte size;
- SHA-256;
- Git blob;
- PNG signature;
- readable dimensions;
- byte-identical artifact copy;
- post-assembly revalidation.

Required future output:

`PASS: 2/2 exact canonical reference binaries verified`

Only then may the Bundle report:

`GENERATION_ALLOWED=TRUE`

## 10. Old Bundle V001 disposition

`N21_REFERENCE_DELIVERY_BUNDLE_V001`

remains:

`TECHNICALLY VALID / 6 OF 6 PASS / VERIFIED HISTORICAL ARTIFACT`

but becomes:

`SUPERSEDED FOR N21 GENERATION / DO NOT SEND TO WORK`

Its exact verification history is preserved.

## 11. Current boundary

`N21 REFERENCE DELIVERY BUNDLE DESIGN V0.2 = PRODUCT OWNER APPROVED / LOCKED / BUILT / 2 OF 2 PASS / TECHNICALLY VALID`

Build result:

- spec: `production/bundle_specs/N21_REFERENCE_DELIVERY_BUNDLE_V002.json`
- spec commit: `26aebca839ec5016762bed92bc9b52a5aa430b99`
- workflow run: `36699004641`
- job: `109833744730`
- artifact id: `11088797193`
- artifact digest: `sha256:e3ec3be6f1a75eae6507801a776bcf2a6e07312d2a26a91909466a73b805f4dc`
- exact verification: `2/2 PASS`
- independent artifact verification: `2/2 PASS`
- generation gate: `GENERATION_ALLOWED=TRUE`
- build record: `docs/project_control/gates/P0_3_video_pipeline/n21_reference_delivery_bundle_v002_build_record_2026-09-30.md`

Post-build production history:

- Candidate 01 generated / not accepted;
- Candidate 02 generated / not accepted;
- Candidate 03 generated / not accepted.

Current disposition:

`FURTHER BUNDLE USE PAUSED PENDING N21 TASK-SCOPE SIMPLIFICATION REVIEW`

- Candidate 04: `NOT AUTHORIZED`;
- N22: `NOT STARTED`;
- do not send V002 to Work again until N21's revised single-frame responsibility is locked and Bundle compatibility is re-reviewed.
