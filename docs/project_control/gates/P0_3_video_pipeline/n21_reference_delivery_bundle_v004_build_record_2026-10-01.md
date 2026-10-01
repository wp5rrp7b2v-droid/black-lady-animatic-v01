# N21 Reference Delivery Bundle V004｜Formal Build + Exact Verification

Date: 2026-10-01

Status:

`FORMAL BUILD PASS / 2 OF 2 EXACT VERIFIED / GENERATION_ALLOWED=TRUE AT BUNDLE LEVEL / CANDIDATE 05 NOT YET AUTHORIZED`

Bundle:

`N21_REFERENCE_DELIVERY_BUNDLE_V004`

Target:

`N21 Candidate 05｜Clean Regeneration`

## 1. Product Owner authorization

Product Owner authorized:

`Formal N21_REFERENCE_DELIVERY_BUNDLE_V004 Build + Exact Verification`

This authorization did not automatically authorize:

- Work generation;
- Candidate 05;
- N22;
- Story Shot publication / registration.

## 2. Formal Spec

Spec:

`production/bundle_specs/N21_REFERENCE_DELIVERY_BUNDLE_V004.json`

Formal build revision:

`V004-R3`

Build gate:

`build_authorized=true`

Authorization commit:

`b0dd5dc00b70b953974e3580d6e4cb671c836848`

Formal references:

1. `AST_IMG_000052` — Scene / threshold spatial authority only
2. `CHARACTER_VISUAL_STYLE_REFERENCE_V001` — human visual-style authority only

## 3. GitHub Actions result

Workflow:

`Story Shot Reference Bundle Builder`

Run:

`36826967264`

Job:

`110254694293`

Conclusion:

`SUCCESS`

Builder output:

- `BUILD_AUTHORIZED=true`
- `PASS: 2/2 exact canonical reference binaries verified`
- `GENERATION_ALLOWED=TRUE`
- `BUNDLE_ID=N21_REFERENCE_DELIVERY_BUNDLE_V004`

Artifact:

`N21_REFERENCE_DELIVERY_BUNDLE_V004`

Artifact ID:

`11145497260`

Artifact size:

`3596063 bytes`

Artifact digest:

`sha256:0b3227f30d8156ed7be3f421f5b43d9233aba4fc609dedd09d76f4f1dc0ea27d`

Expires:

`2026-10-08T06:50:53Z`

## 4. Independent Artifact ZIP verification

Chat independently downloaded Artifact `11145497260`.

Downloaded ZIP:

- byte size: `3596063`
- SHA-256: `0b3227f30d8156ed7be3f421f5b43d9233aba4fc609dedd09d76f4f1dc0ea27d`

GitHub Artifact digest:

`sha256:0b3227f30d8156ed7be3f421f5b43d9233aba4fc609dedd09d76f4f1dc0ea27d`

Result:

`MATCH`

## 5. Artifact contents

Exactly four files were present:

- `WORK_HANDOFF.md`
- `delivery_manifest.json`
- `scene_authority/AST_IMG_000052__SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`
- `character_visual_style_authority/CHARACTER_VISUAL_STYLE_REFERENCE_V001__CHARACTER_VISUAL_STYLE_REFERENCE_V001.png`

No:

- N03;
- N20;
- A07;
- named-character Character Sheet;
- N21 Candidate 01–04;
- extra PNG input.

## 6. Independent exact binary verification

### REF-01｜AST_IMG_000052

Artifact copy:

- PNG: `PASS`
- dimensions: `941 × 1672`
- mode: `RGB`
- bytes: `2305753`
- SHA-256: `d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961`
- Git blob: `e4dafe096f5c5c8782257030a5a659aeec7808f9`

Result:

`EXACT MATCH`

### REF-02｜CHARACTER_VISUAL_STYLE_REFERENCE_V001

Artifact copy:

- PNG: `PASS`
- dimensions: `1536 × 1024`
- mode: `RGB`
- bytes: `1301730`
- SHA-256: `8d650483b6e082a80d41d93e14c7957595c451097aac63f3c84cbcc1ddc7ce41`
- Git blob: `216b1739db17cb3b183d613e4aefa6374d1088e2`

Result:

`EXACT MATCH`

## 7. delivery_manifest verification

Observed:

- `bundle_id = N21_REFERENCE_DELIVERY_BUNDLE_V004`
- `target_shot_id = N21`
- `target_candidate = N21 Candidate 05`
- `reference_count = 2`
- `all_reference_checks_pass = true`
- `generation_allowed = true`
- `manual_product_owner_reference_upload = 0`
- `overall_result = PASS`

Both reference rows report:

- expected identity = actual identity;
- `png_signature = PASS`;
- `byte_identical_copy = PASS`.

## 8. Historical pre-gate Artifact disposition

Historical auto-trigger:

- run: `36825856946`
- Artifact: `11144634603`

Disposition remains:

`DO NOT USE / PRE-GATE AUTO-TRIGGER / NOT FORMAL PRODUCTION BUNDLE`

The only formal V004 production Artifact is:

`11145497260`

## 9. Current production boundary

Technical Bundle result:

`READY FOR WORK DELIVERY`

But Product Owner generation authorization remains separate.

Therefore:

- Bundle V004: `FORMAL / VERIFIED / GENERATION_ALLOWED=TRUE`
- Candidate 05: `NOT YET AUTHORIZED`
- N22: `NOT STARTED`
- RISK-003: `ACTIVE`

Next:

`Product Owner authorization → N21 Candidate 05 Work generation instruction`
