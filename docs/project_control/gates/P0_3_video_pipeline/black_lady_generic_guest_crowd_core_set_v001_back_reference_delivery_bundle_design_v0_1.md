# BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001｜BACK Reference Delivery Bundle Design V0.1

Date: 2026-10-03

Status:

`PRODUCT OWNER APPROVED / LOCKED`

## 1. Bundle identity

Bundle ID:

`BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_BACK_REFERENCE_DELIVERY_BUNDLE_V001`

Target:

`BACK Candidate 01`

Target format:

`1536 × 1024 / LANDSCAPE / 2 × 5`

Target orientation:

`FULL BACK / APPROXIMATELY 180° FROM FRONT`

## 2. Formal reference set

Exactly three controlled visual references are allowed.

### Reference 01 — Primary

Reference ID:

`BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_FRONT`

Source type:

`CONTROLLED_REFERENCE`

Authority role:

`PRIMARY_GLOBAL_IDENTITY_AUTHORITY`

Canonical path:

`production/human_references/generic_guest_crowd_core_set_v001/BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_FRONT.png`

Manifest path:

`production/human_references/generic_guest_crowd_core_set_v001/BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_FRONT.manifest.json`

Exact canonical identity:

- width: `1536`
- height: `1024`
- byte size: `2,335,288`
- SHA-256: `ef6c1b65c8d2f41db70b77b8621ec5d9ade41ad43811d2ddda88a2c14c357a23`
- Git blob: `d8ff2d789a352475daa945d22a0a65112c72a682`

Purpose:

Controls global Guest A–J identity, apparent age, body build, hairstyle identity, garment identity, footwear and identity-defining body markings.

### Reference 02 — Secondary

Reference ID:

`BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q`

Source type:

`CONTROLLED_REFERENCE`

Authority role:

`SECONDARY_REAR_GEOMETRY_CONTINUITY_AUTHORITY`

Canonical path:

`production/human_references/generic_guest_crowd_core_set_v001/BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q.png`

Manifest path:

`production/human_references/generic_guest_crowd_core_set_v001/BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q.manifest.json`

Exact canonical identity:

- width: `1536`
- height: `1024`
- byte size: `2,373,958`
- SHA-256: `52ae779b86ca28e38c50bdf7bf935d08e25769d6ec9bcc73e71b9701f6604756`
- Git blob: `3b72a8b8f0230231f3e2a6b0f7947f3c96b4a400`

Purpose:

Supports rear-side silhouette, shoulder/back geometry, rear hair fall, rear garment geometry and continuity when rotating from REAR_3Q to full BACK.

### Reference 03 — Tertiary

Reference ID:

`BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_LEFT_PROFILE`

Source type:

`CONTROLLED_REFERENCE`

Authority role:

`TERTIARY_SIDE_GEOMETRY_CONTINUITY_AUTHORITY`

Canonical path:

`production/human_references/generic_guest_crowd_core_set_v001/BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_LEFT_PROFILE.png`

Manifest path:

`production/human_references/generic_guest_crowd_core_set_v001/BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_LEFT_PROFILE.manifest.json`

Exact canonical identity:

- width: `1536`
- height: `1024`
- byte size: `1,686,189`
- SHA-256: `15cc28a4cc54dd32ba9fdf7825be6a9402f22b1be19d59e74d1ad1656d238ba1`
- Git blob: `67d07640938163d53af347c4cd4988c2554ffe91`

Purpose:

Supports side hair volume, garment thickness and body-proportion continuity.

## 3. Authority conflict rule

If any reference conflicts on an identity-defining global trait:

`FRONT WINS`

REAR_3Q and LEFT_PROFILE must not override FRONT-locked:

- body build;
- hairstyle identity;
- garment identity;
- footwear identity;
- identity-defining tattoo/body-marking family.

Orientation-specific tolerated differences in LEFT_PROFILE or REAR_3Q do not become new global identity definitions.

## 4. Excluded references

Do not include:

- original named-character style parents;
- named-character Atomic assets;
- Story Shots;
- N21;
- N22;
- N23;
- Scene Masters;
- external imagery.

Reason:

FRONT + REAR_3Q + LEFT_PROFILE already provide sufficient controlled identity and geometry continuity for the final BACK orientation proof.

## 5. Work interpretation

Work must interpret:

`THE SAME TEN PEOPLE FROM ANOTHER VIEW`

More specifically:

`Take the exact same Guest A–J identities, continue naturally from the approved REAR_3Q toward full BACK by approximately another 45 degrees, and produce a true 180-degree back view.`

These are not ten new people.

This is not a REAR_3Q board.

Do not turn heads back toward camera to expose faces.

## 6. Board structure

Fixed:

- 1536 × 1024;
- 2 rows × 5 columns;
- top row A–E;
- bottom row F–J;
- A–F female;
- G–J male;
- complete head / body / feet;
- no overlap;
- no merged people.

## 7. Guest I hard lock

Guest I global identity must resolve from FRONT:

- male;
- clearly muscular;
- black sleeveless top;
- short stiff / brush-cut hairstyle;
- identity-defining tattoo/body-marking family where naturally visible from the back.

LEFT_PROFILE / REAR_3Q accepted tattoo-rendering variations are orientation tolerances only.

Do not propagate those variations as new tattoo designs.

## 8. Bundle transport behavior

Reference count:

`3`

Expected validation:

`3/3 EXACT CANONICAL REFERENCES VERIFIED`

Controlled Reference manifests remain builder-side validation authorities.

Formal visual delivery to Work consists of the canonical PNGs plus generated Bundle metadata / handoff files.

No manual Product Owner reference upload is required.

## 9. Build / generation gating

Initial formal Spec must use:

`build_authorized=false`

Bundle Design approval does not by itself authorize:

- Validation-only;
- Formal Bundle Build;
- Work Candidate generation;
- Candidate 02;
- N21;
- N23 Candidate 02.

## 10. Current gate

Status:

`PRODUCT OWNER APPROVED / LOCKED`

Next formal step:

`BACK Bundle Spec V001 + Validation-only Preparation`

Separate authorization remains required before:

- Validation-only;
- Formal Bundle Build;
- BACK Candidate 01 generation.
