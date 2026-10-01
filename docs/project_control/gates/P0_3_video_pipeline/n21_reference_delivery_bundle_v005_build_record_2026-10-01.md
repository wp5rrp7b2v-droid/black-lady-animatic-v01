# N21 Reference Delivery Bundle V005｜Formal Build + Exact Verification

Date: 2026-10-01

Status:

`FORMAL BUILD PASS / 2 OF 2 EXACT VERIFIED / INDEPENDENT ARTIFACT VERIFIED / GENERATION_ALLOWED=TRUE AT BUNDLE LEVEL / CANDIDATE 07 NOT YET AUTHORIZED`

Bundle:

`N21_REFERENCE_DELIVERY_BUNDLE_V005`

Target:

`N21 Candidate 07｜Clean Regeneration`

## 1. Product Owner authorization

Product Owner authorized:

`Formal N21_REFERENCE_DELIVERY_BUNDLE_V005 Build + Exact Verification`

This authorization did not automatically authorize:

- Work generation;
- Candidate 07;
- N22;
- Story Shot publication / registration.

## 2. Formal Spec

Spec:

`production/bundle_specs/N21_REFERENCE_DELIVERY_BUNDLE_V005.json`

Formal build revision:

`V005-R2`

Build gate:

`build_authorized=true`

Authorization commit:

`5dcb51deb9f00b01ee36a1e9290a23dbb60c6e8f`

Formal references:

1. `N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001` — threshold environment / lighting / tonal authority only
2. `CHARACTER_VISUAL_STYLE_REFERENCE_V001` — human visual-style authority only

No complete Scene Master or complete Story Shot is a formal V005 generation input.

## 3. GitHub Actions result

Workflow:

`Story Shot Reference Bundle Builder`

Run:

`36859705482`

Job:

`110360617971`

Conclusion:

`SUCCESS`

Builder output:

- `BUILD_AUTHORIZED=true`
- `PASS: 2/2 exact canonical reference binaries verified`
- `GENERATION_ALLOWED=TRUE`
- `BUNDLE_ID=N21_REFERENCE_DELIVERY_BUNDLE_V005`

Artifact:

`N21_REFERENCE_DELIVERY_BUNDLE_V005`

Artifact ID:

`11161920411`

Artifact size:

`4697710 bytes`

Artifact digest:

`sha256:358ea894249d88e93047eabbfeb760196a34c29afdfa2a82277fc875560ecb58`

Expires:

`2026-10-08T12:07:52Z`

## 4. Independent Artifact ZIP verification

Chat independently downloaded Artifact `11161920411`.

Downloaded ZIP:

- byte size: `4697710`
- SHA-256: `358ea894249d88e93047eabbfeb760196a34c29afdfa2a82277fc875560ecb58`

GitHub Artifact digest:

`sha256:358ea894249d88e93047eabbfeb760196a34c29afdfa2a82277fc875560ecb58`

Result:

`MATCH`

## 5. Artifact contents

Exactly four files were present:

- `WORK_HANDOFF.md`
- `delivery_manifest.json`
- `environment_authority/N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001__N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001.png`
- `character_visual_style_authority/CHARACTER_VISUAL_STYLE_REFERENCE_V001__CHARACTER_VISUAL_STYLE_REFERENCE_V001.png`

No:

- `AST_IMG_000052` direct image input;
- N20 direct image input;
- complete Story Shot;
- complete Scene Master;
- named-character Character Sheet;
- N21 Candidate 01–06;
- extra PNG input.

## 6. Independent exact binary verification

### REF-01｜N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001

Artifact copy:

- PNG signature: `PASS`
- dimensions: `941 × 1672`
- mode: `RGBA`
- bytes: `3394494`
- SHA-256: `dd1b2dc6b831b2e22d8dc249859af1b4f65da6a20437cd8821627144e89a4f13`
- Git blob: `358057948ec222bbe63a47a07022de4453e20fc8`

Result:

`EXACT MATCH`

### REF-02｜CHARACTER_VISUAL_STYLE_REFERENCE_V001

Artifact copy:

- PNG signature: `PASS`
- dimensions: `1536 × 1024`
- mode: `RGB`
- bytes: `1301730`
- SHA-256: `8d650483b6e082a80d41d93e14c7957595c451097aac63f3c84cbcc1ddc7ce41`
- Git blob: `216b1739db17cb3b183d613e4aefa6374d1088e2`

Result:

`EXACT MATCH`

## 7. delivery_manifest verification

Observed:

- `bundle_id = N21_REFERENCE_DELIVERY_BUNDLE_V005`
- `target_shot_id = N21`
- `target_candidate = N21 Candidate 07`
- `reference_count = 2`
- `all_reference_checks_pass = true`
- `generation_allowed = true`
- `manual_product_owner_reference_upload = 0`
- `overall_result = PASS`

Both reference rows report:

- expected identity = actual identity;
- `png_signature = PASS`;
- `byte_identical_copy = PASS`.

## 8. WORK_HANDOFF verification

The Artifact handoff correctly carries the approved V005 execution boundaries:

- Clean Regeneration;
- one Candidate 07 PNG only;
- approximately 4–6 readable people;
- staggered threshold cluster rather than single-file queue;
- upright natural posture;
- no backpacks / shoulder bags / crossbody bags / luggage;
- both sides read as castle interior;
- no outdoor / blue-sky / strong daylight interpretation;
- no cathedral / monumental symmetrical portal / complete First Hall reveal;
- environment reference controls threshold environment only;
- character style reference controls human visual language only.

## 9. Current production boundary

Technical Bundle result:

`READY FOR WORK DELIVERY`

But Product Owner generation authorization remains separate.

Therefore:

- Bundle V005: `FORMAL / VERIFIED / GENERATION_ALLOWED=TRUE`
- Candidate 07: `NOT YET AUTHORIZED`
- N22: `NOT STARTED`
- RISK-003: `ACTIVE`

Next:

`Product Owner authorization → N21 Candidate 07 Work generation instruction`
