# BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001｜REAR 3/4 Reference Delivery Bundle Design V0.1

Date: 2026-10-03

Status:

`PRODUCT OWNER APPROVED / LOCKED`

## 1. Bundle identity

Bundle ID:

`BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q_REFERENCE_DELIVERY_BUNDLE_V001`

Target:

`REAR_3Q Candidate 01`

Target format:

`1536 × 1024 / LANDSCAPE / 2 × 5`

Target orientation:

`BACK-DOMINANT REAR_3Q / APPROXIMATELY 135° FROM FRONT`

## 2. Formal reference set

Exactly two controlled visual references are allowed.

### Reference 01 — Primary

Reference ID:

`BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_FRONT`

Source type:

`CONTROLLED_REFERENCE`

Classification:

`P0.3_CONTROLLED_PRODUCTION_REFERENCE`

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

`BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_LEFT_PROFILE`

Source type:

`CONTROLLED_REFERENCE`

Classification:

`P0.3_CONTROLLED_PRODUCTION_REFERENCE`

Authority role:

`SECONDARY_SIDE_GEOMETRY_CONTINUITY_AUTHORITY`

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

Supports side silhouette, side hair volume, garment thickness and side-view body-proportion continuity only.

## 3. Authority conflict rule

If FRONT and LEFT PROFILE appear to disagree on an identity-defining global trait:

`FRONT WINS`

LEFT PROFILE must not override FRONT-locked:

- body build;
- hairstyle identity;
- garment identity;
- footwear identity;
- identity-defining tattoo/body-marking family.

The Product Owner-accepted LEFT PROFILE Guest I tolerance must not propagate as redesign.

## 4. Excluded references

Do not include:

- original named-character FRONT style parents;
- Su Xiaoxiao;
- Liao Jian;
- Wen Qingya;
- Guang Yong;
- Ning Qiushui;
- Jun Luyuan;
- Neil;
- Story Shots;
- N21;
- N22;
- N23;
- Scene Masters;
- external imagery.

Reason:

FRONT + LEFT PROFILE already define the reusable anonymous Guest A–J asset sufficiently for the next controlled orientation proof.

## 5. Work interpretation

Work must interpret the task as:

`THE SAME TEN PEOPLE FROM ANOTHER VIEW`

More specifically:

`Take the exact same Guest A–J identities from FRONT, use LEFT PROFILE only as secondary side geometry continuity, and rotate naturally toward BACK by about another 45 degrees to create a back-dominant REAR_3Q view.`

These are not ten new people.

This is not a front-three-quarter portrait board.

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
- identity-defining tattoo/body-marking family where naturally visible.

LEFT PROFILE's accepted reduced-muscle / tattoo-pattern variation is not a new authority for these global traits.

## 8. Bundle transport behavior

Reference count:

`2`

Expected validation:

`2/2 EXACT CANONICAL REFERENCES VERIFIED`

Controlled Reference manifests remain builder-side validation authorities.

Formal visual delivery to Work consists of the canonical PNGs plus generated Bundle metadata / handoff files.

No manual Product Owner reference upload is required.

## 9. Build / generation gating

Initial formal Spec must use:

`build_authorized=false`

Bundle Design approval does not by itself authorize:

- formal Bundle Build;
- Work Candidate generation;
- Candidate 02;
- BACK;
- N21;
- N23 Candidate 02.

## 10. Current gate

Status:

`PRODUCT OWNER APPROVED / LOCKED`

Next formal step:

`Bundle Spec V001 + Validation-only Preparation`

Separate authorization remains required before:

- formal build;
- REAR_3Q Candidate 01 generation.
