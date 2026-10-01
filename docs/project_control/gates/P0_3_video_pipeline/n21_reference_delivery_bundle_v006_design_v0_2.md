# N21 Reference Delivery Bundle V006｜Design V0.2

Date: 2026-10-01

Status:

`PRODUCT OWNER APPROVED / LOCKED / SPEC PREPARATION AUTHORIZED / FORMAL BUILD NOT AUTHORIZED / CANDIDATE 08 NOT AUTHORIZED`

Target:

`N21｜Cohort Enters — Into the Unknown`

Future candidate:

`N21 Candidate 08｜Clean Regeneration`

Future bundle:

`N21_REFERENCE_DELIVERY_BUNDLE_V006`

## 1. Design objective

V005 established a viable controlled threshold-environment input and a two-reference delivery mechanism, but the remaining production risk is human-body / wardrobe / crowd performance.

The newly approved controlled reference:

`N21_CROWD_BODY_WARDROBE_REFERENCE_V001`

shall replace `CHARACTER_VISUAL_STYLE_REFERENCE_V001` in the next N21 generation test.

V006 changes only one major input variable:

`Environment Reference + Crowd Body/Wardrobe Reference`

The purpose is to test whether a dedicated human-body / wardrobe reference improves:

- natural adult body proportions;
- natural upright walking posture;
- head / neck / shoulder relationships;
- ordinary contemporary wardrobe;
- staggered crowd behavior;
- absence of expedition-style bags or luggage.

## 2. Formal reference count

V006 shall contain exactly:

`2 formal image references`

### REF-01｜Threshold Environment

Reference:

`N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001`

Authority:

`N21_THRESHOLD_TRANSITION_ENVIRONMENT_ONLY`

Canonical PNG:

`production/environment_references/n21_threshold_transition/N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001.png`

Manifest:

`production/environment_references/n21_threshold_transition/N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001.manifest.json`

Expected exact identity:

- width: `941`
- height: `1672`
- mode: `RGBA`
- bytes: `3394494`
- SHA-256: `dd1b2dc6b831b2e22d8dc249859af1b4f65da6a20437cd8821627144e89a4f13`
- Git blob: `358057948ec222bbe63a47a07022de4453e20fc8`

May control:

- threshold-transition spatial staging;
- doorway scale;
- interior-to-interior relationship;
- warm low-key castle environment;
- stone / wood / floor language;
- deeper space becoming darker;
- incomplete First Hall visibility.

Must not control:

- character identity;
- wardrobe;
- body proportions;
- crowd blocking;
- exact final composition.

### REF-02｜Crowd Body / Wardrobe

Reference:

`N21_CROWD_BODY_WARDROBE_REFERENCE_V001`

Authority:

`N21_CROWD_BODY_WARDROBE_ONLY`

Canonical PNG:

`production/human_references/n21_crowd_body_wardrobe/N21_CROWD_BODY_WARDROBE_REFERENCE_V001.png`

Manifest:

`production/human_references/n21_crowd_body_wardrobe/N21_CROWD_BODY_WARDROBE_REFERENCE_V001.manifest.json`

Expected exact identity:

- width: `1536`
- height: `1024`
- mode: `RGBA`
- bytes: `1418940`
- SHA-256: `73bb645e5a22cccb53faf8eb2d4b8fc0b876980e7520a2bc54daab1207439dc6`
- Git blob: `2b86ab207ee60ba0cd2de277bb55900b8854099c`

May control:

- natural adult body proportions;
- upright walking posture;
- natural head / neck / shoulder relationship;
- contemporary everyday wardrobe era;
- project-consistent human silhouette;
- rear / side / rear-three-quarter human-body language;
- absence of backpack / shoulder bag / crossbody bag / luggage.

Must not control:

- named-character identity;
- exact face;
- exact complete outfit;
- scene environment;
- lighting;
- Story Shot camera composition;
- final person count;
- left/right order;
- relative placement;
- crowd travel direction;
- the exact four-person cast visible in the reference image.

## 3. Human Reference Decoupling Lock

`N21_CROWD_BODY_WARDROBE_REFERENCE_V001` is:

`BODY / WARDROBE / NATURAL HUMAN LANGUAGE REFERENCE`

It is not an N21 cast sheet and not a blocking blueprint.

Candidate 08 must not copy:

- the four-person cast;
- the count of four;
- named identities;
- exact clothing combinations;
- left/right order;
- relative spacing;
- original facing directions;
- exact poses;
- four-person composition.

The four people visible in the reference do not imply that those four people appear in N21.

The directions visible in the reference do not constitute final N21 direction authority.

## 4. Direction / Blocking Authority Lock

Candidate 08 direction is independently controlled by:

`N21 STORY SHOT BLOCKING`

Overall motion must read:

`THRESHOLD → DEEPER CASTLE INTERIOR`

Preferred visible orientations:

- back;
- rear three-quarter;
- natural side view.

Do not:

- make the main group walk toward camera;
- make the group collectively turn toward camera;
- reverse the threshold relationship to follow the human reference;
- mirror the entire scene because of reference-facing directions.

Authority priority:

1. N21 Story Shot blocking controls crowd movement direction.
2. Environment Reference controls space / threshold relationship.
3. Body/Wardrobe Reference controls only human naturalness and wardrobe language.

The Human Reference must never override 1 or 2.

## 5. Explicit exclusions

V006 must not include:

- `CHARACTER_VISUAL_STYLE_REFERENCE_V001`;
- any complete Scene Master;
- N20;
- N19;
- N03;
- N08;
- N21 Candidate 01–07;
- named-character Character Sheets;
- Atomic character appearance references;
- a third image reference.

Reason:

The experiment must isolate whether the new Human Body / Wardrobe Reference improves the remaining N21 human-performance problem.

## 6. Candidate 08 generation mode

If separately authorized after V006 formal build and verification:

`N21 Candidate 08 = CLEAN REGENERATION`

Candidate 01–07 are not edit bases, style references, or composition inputs.

## 7. Story function

N21 single-frame responsibility remains:

`THRESHOLD TRANSITION + UNKNOWN-SPACE MOOD`

First read:

`A GROUP OF PARTICIPANTS HAS JUST CROSSED THE THRESHOLD AND IS MOVING INTO A DARKER UNKNOWN CASTLE INTERIOR`

It is not:

- a 16-person proof frame;
- a hero-pair portrait;
- a four-person reference recreation;
- a single-file queue;
- a complete hall reveal;
- an architectural showcase.

## 8. Crowd execution target

Readable complexity:

`approximately 4–6 people`

This number comes from Story Shot needs and is unrelated to the four people shown in the Human Reference.

Preferred state:

`STAGGERED THRESHOLD CLUSTER / NATURAL DEPTH VARIATION`

Required:

- different lateral positions;
- different depths;
- different stride phases;
- natural small facing variations;
- some figures deeper inside;
- some nearer the threshold;
- no central leader axis;
- no equal spacing;
- no synchronized walking;
- no recreation of the four-person reference layout.

Hard accessory exclusion:

`NO BACKPACKS / NO SHOULDER BAGS / NO CROSSBODY BAGS / NO LUGGAGE`

## 9. Human-body hard targets

Candidate 08 review must check:

- natural adult proportions;
- no obvious oversized heads;
- no obvious shortened legs;
- no overly long / thick torso;
- natural shoulders and necks;
- coherent pelvis / torso alignment;
- natural walking posture;
- no generalized hunching;
- no NPC-like queue behavior;
- ordinary contemporary wardrobe;
- suitable wardrobe variation;
- no copied four-person outfit set;
- no expedition-team read.

## 10. Critical assumptions

`WORKING HYPOTHESIS A`

Previous N21 human problems were at least partly caused by insufficient body / wardrobe control.

`WORKING HYPOTHESIS B`

The Human Reference can transfer body / wardrobe language without copying its four-person cast, exact outfits, layout or facing directions.

Neither hypothesis is currently a fact.

Candidate 08 is the minimum end-to-end proof.

## 11. Minimum proof

Generate exactly one:

`N21 Candidate 08`

Do not generate Candidate 09 unless Candidate 08 is first evaluated and a specific failure cause is identified.

Do not advance N22.

## 12. PASS / FAIL

### PASS

Candidate 08 must show:

- approved threshold-world continuity;
- group motion clearly toward deeper castle interior;
- no direction reversal;
- natural adult body proportions;
- natural 4–6 person staggered grouping;
- no single-file queue;
- ordinary contemporary wardrobe;
- no prohibited accessories;
- no direct recreation of the Human Reference four-person cast;
- no obvious copied left/right order or complete outfit set;
- no hero-pair staging;
- immediate narrative read of entering an unknown space.

### FAIL

Candidate 08 fails if any structural issue appears, including:

- generalized oversized heads / shortened legs;
- continued body-proportion distortion;
- direct recreation of the Human Reference four-person cast;
- crowd direction incorrectly inherited from the Human Reference;
- threshold travel direction reversed;
- single-file queue;
- major environment drift;
- prohibited bags / luggage;
- new human-style distortion caused by the reference;
- first read becomes a group portrait instead of an unknown-space transition.

If FAIL, stop before Candidate 09 and diagnose whether the failure is:

1. Human Reference attribute leakage;
2. Human Reference identity / direction contamination;
3. inability to obey Environment + Human authorities together;
4. Prompt / Blocking Contract failure.

## 13. Scale gate

Before Candidate 08 PASS:

- do not start N22;
- do not produce a series of additional candidates;
- do not canonically publish N21;
- do not expand the reference-governance system.

## 14. Authorization boundary

Product Owner approved Design V0.2 on 2026-10-01.

This approval authorizes:

- V006 formal Spec preparation;
- validation-only exact-reference verification.

This approval does not authorize:

- formal V006 Bundle build;
- production Artifact;
- Work generation;
- Candidate 08;
- N22;
- Story Shot publication / registration.

Next gate after validation-only PASS:

`PRODUCT OWNER AUTHORIZATION → FORMAL V006 BUILD + EXACT VERIFICATION`
