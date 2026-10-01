# N21 Reference Delivery Bundle V006｜Spec + Validation-Only Build Preparation

Date: 2026-10-01

Status:

`PRODUCT OWNER APPROVED DESIGN / LOCKED / SPEC CREATED / VALIDATION-ONLY PASS / FORMAL BUILD NOT AUTHORIZED / CANDIDATE 08 NOT AUTHORIZED`

Bundle:

`N21_REFERENCE_DELIVERY_BUNDLE_V006`

Target:

`N21 Candidate 08｜Clean Regeneration`

## 1. Product Owner approval

Product Owner approved:

`N21 Reference Delivery Bundle V006｜Design V0.2`

Approval locks the Human Reference decoupling rule:

- the Human Reference is not an N21 cast sheet;
- the four people visible in the Human Reference are not required N21 characters;
- their count, identities, exact outfits, left/right order, spacing, poses and facing directions must not be copied;
- N21 movement direction is independently controlled by Story Shot blocking;
- overall movement must read `THRESHOLD → DEEPER CASTLE INTERIOR`.

Design record:

`docs/project_control/gates/P0_3_video_pipeline/n21_reference_delivery_bundle_v006_design_v0_2.md`

Design commit:

`48a46ceabfaf7c2eafa1771ac42abd306ec057bf`

## 2. Formal Spec

Spec:

`production/bundle_specs/N21_REFERENCE_DELIVERY_BUNDLE_V006.json`

Spec revision:

`V006-R1`

Spec commit:

`18ce4dc6bcf11753351e6dc062630e6bebe5eb16`

Build authorization:

`false`

Authorization note:

`PRODUCT_OWNER_APPROVED_V006_DESIGN_V0_2 / VALIDATION_ONLY_AUTHORIZED / FORMAL_BUILD_NOT_AUTHORIZED / CANDIDATE_08_NOT_AUTHORIZED / N22_NOT_STARTED`

## 3. Formal reference set

Exactly two controlled references:

### REF-01

`N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001`

Authority:

`N21_THRESHOLD_TRANSITION_ENVIRONMENT_ONLY`

Expected:

- 941 × 1672
- 3394494 bytes
- SHA-256 `dd1b2dc6b831b2e22d8dc249859af1b4f65da6a20437cd8821627144e89a4f13`
- Git blob `358057948ec222bbe63a47a07022de4453e20fc8`

### REF-02

`N21_CROWD_BODY_WARDROBE_REFERENCE_V001`

Authority:

`N21_CROWD_BODY_WARDROBE_ONLY`

Expected:

- 1536 × 1024
- 1418940 bytes
- SHA-256 `73bb645e5a22cccb53faf8eb2d4b8fc0b876980e7520a2bc54daab1207439dc6`
- Git blob `2b86ab207ee60ba0cd2de277bb55900b8854099c`

Explicitly excluded:

- `CHARACTER_VISUAL_STYLE_REFERENCE_V001`;
- complete Scene Master;
- complete Story Shot;
- N20 / N19 / N03 / N08;
- N21 Candidate 01–07;
- named-character Character Sheets;
- Atomic character appearance references;
- third reference image.

## 4. Human Reference decoupling lock

The Human Reference may control:

- natural adult proportions;
- upright walking posture;
- head / neck / shoulder relationship;
- ordinary contemporary wardrobe language;
- rear / side / rear-three-quarter body language;
- absence of backpack / shoulder bag / crossbody bag / luggage.

It must not control:

- cast identity;
- exact person count;
- exact outfits;
- left/right order;
- relative position;
- final crowd blocking;
- final travel direction.

Authority priority:

1. N21 Story Shot blocking → crowd movement direction.
2. Environment Reference → threshold / space relationship.
3. Human Reference → body naturalness / wardrobe language only.

## 5. Validation-only workflow

Workflow:

`Story Shot Reference Bundle Builder`

Run:

`36878776156`

Job:

`110424919156`

Conclusion:

`SUCCESS`

Observed validation output:

- `VALIDATION_PASS: 2/2 exact canonical references verified`
- `BUILD_AUTHORIZED=FALSE`
- `GENERATION_ALLOWED=FALSE`

Artifact count:

`0`

This is the required current state.

No production Bundle Artifact was created.

## 6. What this step proves

FACT:

- both proposed V006 controlled references exist canonically;
- both exact identities satisfy the Builder validation contract;
- the V006 two-reference structure is technically resolvable;
- the new Human Reference can be transported through the existing controlled-reference contract;
- the formal build authorization gate remains closed.

NOT PROVEN:

- that the generator will use the Human Reference only for body / wardrobe attributes;
- that it will not copy the visible four-person cast;
- that final N21 person direction will remain correct;
- that body proportions will improve;
- that Candidate 08 will pass visually.

Those questions require the real Candidate 08 end-to-end test.

## 7. Current boundary

Completed:

- V006 Design V0.2 approved and locked;
- V006 Spec R1 created;
- validation-only exact-reference verification PASS.

Not authorized:

- formal V006 Build;
- production Artifact;
- `GENERATION_ALLOWED=TRUE`;
- Work generation;
- Candidate 08;
- Candidate 09;
- N22;
- Story Shot publication / registration.

Next gate:

`PRODUCT OWNER AUTHORIZATION → FORMAL N21_REFERENCE_DELIVERY_BUNDLE_V006 BUILD + EXACT VERIFICATION`
