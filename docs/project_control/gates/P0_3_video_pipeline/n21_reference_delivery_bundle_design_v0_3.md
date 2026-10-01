# N21｜Reference Delivery Bundle Design V0.3

Status: `PRODUCT OWNER APPROVED / LOCKED`

Date: 2026-10-01

Target shot:

`N21｜Cohort Enters — Into the Unknown / 队伍进入｜步入未知`

Target candidate:

`N21 Candidate 04｜Clean Regeneration`

Target bundle:

`N21_REFERENCE_DELIVERY_BUNDLE_V003`

Scene authority:

`N21 Scene Reference Design V0.4 / PRODUCT OWNER APPROVED + LOCKED`

## 1. Design objective

V003 uses the minimum necessary formal reference set and separates:

`SPACE AUTHORITY`

from:

`CHARACTER VISUAL STYLE AUTHORITY`

Formal reference count:

`2`

The bundle must support:

1. castle entrance / threshold space facts;
2. established Black Lady human visual language.

It must not reintroduce:

- full sixteen-person single-frame proof;
- Ning / Jun identity anchoring;
- named-character showcase pressure;
- N20 two-person composition bias.

## 2. REF-01｜Castle Entrance Scene Master

- reference_id: `AST_IMG_000052`
- source_type: `ASSET`
- entity_id: `SCENE_CASTLE_ENTRANCE`
- role: `SCENE_MASTER`
- asset_class: `ATOMIC`
- authority_class: `MASTER`
- approval_status: `APPROVED`
- lifecycle: `CURRENT`
- resolver_usage: `CONDITIONAL`
- canonical_path: `production/image_library/scene_masters/castle_entrance/SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`
- expected SHA-256: `d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961`
- expected byte_size: `2305753`
- expected Git blob: `e4dafe096f5c5c8782257030a5a659aeec7808f9`
- destination_group: `scene_authority`

Authority:

- entrance architecture;
- stone / material facts;
- open-door state;
- threshold spatial facts.

Must not control:

- exact camera;
- exact composition;
- character count / placement;
- empty-scene staging.

## 3. REF-02｜N03 Canonical Story Shot

- reference_id: `N03`
- source_type: `STORY_SHOT`
- shot_id: `N03`
- approval_status: `APPROVED`
- lifecycle: `CURRENT`
- canonical_path: `production/image_library/approved/story_shots/N03_VISITOR_REACTION_APPROVED_V001.png`
- expected SHA-256: `0e5022a59d7e33e30e0fdea74c966ff8e84a3084ca869fcbc4d76052e8ec6c22`
- expected byte_size: `2321221`
- expected Git blob: `bd1e3b0879da8dfa88e9ecb229534c92dc96cd07`
- dimensions: `941x1672`
- historical exact verification: `GitHub Actions run 36232083006 / VERIFIED MATCH`
- destination_group: `character_visual_style_authority`

Authority:

- realistic human rendering level;
- face construction language;
- skin treatment;
- hair realism;
- believable adult age variation;
- body proportion language;
- clothing / fabric rendering;
- cinematic integration of multiple people.

Hard boundary:

`COPY VISUAL LANGUAGE / DO NOT COPY SHOT CONTENT`

N03 must not control:

- Ning identity;
- Jun identity;
- hero-pair composition;
- exact people;
- exact wardrobe arrangement;
- pose;
- eyeline;
- camera;
- exterior scene state;
- group staging.

## 4. N20 disposition

`N20_DO_NOT_TOUCH_THINGS_APPROVED_V001.png`

is:

`DIRECTOR CONTINUITY REVIEW ONLY`

It is not a formal V003 generation input.

Use it only after generation to review:

- warm low-key world continuity;
- exposure / black level;
- contrast;
- material continuity.

This exclusion is a risk-control decision, not a proven root-cause finding.

## 5. Character Sheet disposition

No named-character Character Sheet is included.

Reason:

N21 V0.4 does not own named-character identity proof.

Character style remains a hard gate, but named identity pressure is intentionally reduced.

## 6. Candidate 01–03 disposition

N21 Candidate 01 / 02 / 03 are:

`NEGATIVE DIRECTOR LESSONS ONLY`

They must not be used as:

- image inputs;
- edit bases;
- style references;
- composition references.

Candidate 04 must be:

`CLEAN REGENERATION`

## 7. Work handoff principle

The Work handoff must stay concise.

Primary read:

`A GROUP OF PEOPLE CROSSING INTO A DARKER UNKNOWN CASTLE INTERIOR`

Narrative facts:

- 16 participants remain canonical;
- exact single-frame counting is not required;
- approximately 4–6 readable people are sufficient;
- additional cohort presence may be implied by crop / occlusion / silhouettes / deeper figures / off-frame continuation.

Character rule:

`CHARACTER STYLE DRIFT = FAIL`

Do not turn the task back into a sixteen-person or named-character showcase.

## 8. Artifact structure

`N21_REFERENCE_DELIVERY_BUNDLE_V003/`

- `delivery_manifest.json`
- `WORK_HANDOFF.md`
- `scene_authority/AST_IMG_000052__SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`
- `character_visual_style_authority/N03__N03_VISITOR_REACTION_APPROVED_V001.png`

Manual Product Owner reference upload:

`0`

Transport:

`GitHub Actions → Artifact → Work automatic acquisition`

## 9. Builder contract

Use existing generic builder only:

`.github/workflows/story-shot-reference-bundle-builder.yml`

Fail closed on:

- canonical path;
- Registry / Story Shot status;
- byte size;
- SHA-256;
- Git blob;
- PNG signature;
- dimensions;
- byte-identical copy;
- final artifact revalidation.

Required result:

`PASS: 2/2 exact canonical reference binaries verified`

and:

`GENERATION_ALLOWED=TRUE`

## 10. V002 disposition

`N21_REFERENCE_DELIVERY_BUNDLE_V002`

remains:

`TECHNICALLY VALID / HISTORICAL`

but for future N21 generation:

`CREATIVE SCOPE SUPERSEDED / DO NOT SEND TO WORK`

## 11. Current boundary

`N21 REFERENCE DELIVERY BUNDLE DESIGN V0.3 = PRODUCT OWNER APPROVED / LOCKED`

Next:

`N21_REFERENCE_DELIVERY_BUNDLE_V003 SPEC + BUILD`

Candidate 04 generation remains unauthorized until V003 build and independent verification pass.
