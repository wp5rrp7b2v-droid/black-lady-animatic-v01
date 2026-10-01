# N21 Reference Delivery Bundle V004｜Builder Support + Spec Preparation

Date: 2026-10-01

Status:

`BUILDER SUPPORT FORMALLY AUTHORIZED / SPEC LOCKED / VALIDATION-ONLY PASS / FORMAL BUILD NOT AUTHORIZED`

Target:

`N21 Candidate 05｜Clean Regeneration`

Bundle:

`N21_REFERENCE_DELIVERY_BUNDLE_V004`

## 1. Product Owner authorization boundary

Product Owner explicitly authorized:

- `CONTROLLED_REFERENCE Builder Support`;
- `N21 Bundle V004 Spec`.

This authorization does **not** authorize:

- formal V004 Bundle build;
- production Artifact publication;
- `GENERATION_ALLOWED=TRUE`;
- Work generation;
- Candidate 05;
- N22.

Formal V004 Build requires a separate Product Owner authorization.

## 2. Authority baseline

- N21 Scene Reference Design V0.4: `PRODUCT OWNER APPROVED / LOCKED`
- Character Visual Style Reference V001: `PRODUCT OWNER APPROVED / CANONICAL / REMOTE VERIFIED`
- CONTROLLED_REFERENCE + N21 Bundle V004 Design V0.1: `PRODUCT OWNER APPROVED / LOCKED`

## 3. Builder support

Generic builder:

`scripts/story_shot_reference_bundle_builder_v1.py`

Initial CONTROLLED_REFERENCE implementation:

`2afef948bd396dd418a7d6289124c7811f616e09`

Authorization-hardening commits:

- `b636a2de2a63ddfb119c9c795b002e8a322650bd` — validation-only mode + builder-level `build_authorized` gate;
- `4c124dad017cbc05ad6604098b7f28f35e1d0529` — workflow-level authorization gate / skip build + upload when unauthorized.

Existing `ASSET` and `STORY_SHOT` validation branches remain intact.

CONTROLLED_REFERENCE validates fail closed:

- manifest path exists and is readable JSON;
- manifest reference_id;
- classification;
- approval_status;
- lifecycle;
- authority_scope;
- canonical_path;
- manifest output SHA-256;
- manifest output byte size;
- manifest output Git blob;
- expected width / height when declared;
- output format = PNG;
- approved_binary SHA / bytes;
- actual canonical file SHA / bytes / Git blob;
- actual PNG signature / dimensions;
- byte-identical copy if/when a formal Bundle is later built.

## 4. Locked V004 Spec

Path:

`production/bundle_specs/N21_REFERENCE_DELIVERY_BUNDLE_V004.json`

Current revision:

`V004-R2`

Current build gate:

`build_authorized=false`

Authorization note:

`PRODUCT_OWNER_AUTHORIZED_BUILDER_SUPPORT_AND_SPEC_ONLY / BUNDLE_BUILD_NOT_AUTHORIZED / CANDIDATE_05_NOT_AUTHORIZED`

Formal reference set remains exactly two references.

### REF-01

`AST_IMG_000052`

Purpose:

`CASTLE ENTRANCE / THRESHOLD SPACE AUTHORITY ONLY`

### REF-02

`CHARACTER_VISUAL_STYLE_REFERENCE_V001`

Purpose:

`CHARACTER VISUAL STYLE ONLY`

Exact identity:

- 1536×1024
- 1301730 bytes
- SHA-256 `8d650483b6e082a80d41d93e14c7957595c451097aac63f3c84cbcc1ddc7ce41`
- Git blob `216b1739db17cb3b183d613e4aefa6374d1088e2`

## 5. Explicit exclusions

Do not deliver:

- N03;
- N20;
- any complete Story Shot;
- any named-character Character Sheet;
- A07;
- N21 Candidate 01–04.

## 6. Formal validation-only evidence

Spec gate commit:

`81d3ca4d80f745f6cf370f18567df2d9cb6460c5`

Validation-only workflow:

- Run: `36826494510`
- Job: `110253232876`
- Conclusion: `SUCCESS`

Observed result:

- `VALIDATION_PASS: 2/2 exact canonical references verified`
- `BUILD_AUTHORIZED=FALSE`
- `GENERATION_ALLOWED=FALSE`
- formal build step: `SKIPPED`
- Artifact upload step: `SKIPPED`
- Artifact count from this run: `0`

This is the intended current state.

## 7. Historical auto-trigger incident

Before the new authorization gate was added, the earlier V004 spec commit automatically triggered the generic Builder under the old workflow behavior.

Historical run:

- Run: `36825856946`
- Artifact: `N21_REFERENCE_DELIVERY_BUNDLE_V004`
- Artifact ID: `11144634603`

Disposition:

`PRE-GATE AUTO-TRIGGER / NOT FORMAL BUILD AUTHORIZATION / DO NOT USE FOR PRODUCTION`

This historical Artifact does not authorize Candidate 05 and must not be supplied to Work.

## 8. Required result after future formal Build authorization

Only after a separate Product Owner Build authorization may `build_authorized` be changed to `true`.

Required production result:

`PASS: 2/2 exact canonical reference binaries verified`

and:

`GENERATION_ALLOWED=TRUE`

Then Chat must independently inspect:

- workflow conclusion;
- Run / Job / Artifact IDs;
- Artifact digest;
- delivery_manifest.json;
- both enclosed PNG exact identities.

## 9. Current boundary

Completed:

- CONTROLLED_REFERENCE support;
- fail-closed authorization gate;
- V004 formal spec;
- validation-only 2/2 canonical reference check.

Not authorized:

- formal V004 Bundle build;
- production Artifact;
- Candidate 05 generation;
- N22;
- Story Shot publication / registration.

Next:

`Product Owner authorization → Formal N21_REFERENCE_DELIVERY_BUNDLE_V004 Build + Exact Verification`
