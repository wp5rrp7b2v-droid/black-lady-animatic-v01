# N23 Reference Delivery Bundle V003｜Formal Build + Exact Artifact Verification

Date:

`2026-10-03`

Status:

`FORMAL BUILD PASS / ARTIFACT EXACT VERIFIED / 4 OF 4 MATCH / CANDIDATE 03 GENERATION NOT YET PRODUCT OWNER AUTHORIZED`

Bundle:

`N23_REFERENCE_DELIVERY_BUNDLE_V003`

Target:

`N23 Candidate 03`

Spec:

`production/bundle_specs/N23_REFERENCE_DELIVERY_BUNDLE_V003.json`

Spec revision:

`V003-R3`

Formal-build authorization commit:

`c01fb71417442ee6c49ff3ee2aa7e899249f9038`

## GitHub Actions

Workflow:

`Story Shot Reference Bundle Builder`

Run:

`37108188787`

Job:

`111160732008`

Conclusion:

`SUCCESS`

Artifact:

`N23_REFERENCE_DELIVERY_BUNDLE_V003`

Artifact ID:

`11268607749`

Artifact size:

`7,554,791 bytes`

Artifact digest:

`sha256:674228ac21d51f47d8d0bbd2bc3c5463b1190d47e754f9a5e720b8d833e7554f`

Artifact expiry:

`2026-10-10T07:59:56Z`

## Independent ZIP verification

Downloaded Artifact ZIP SHA-256:

`674228ac21d51f47d8d0bbd2bc3c5463b1190d47e754f9a5e720b8d833e7554f`

Result:

`MATCHES GITHUB ARTIFACT DIGEST`

Files:

- `WORK_HANDOFF.md`
- `delivery_manifest.json`
- 4 direct PNG references

## 4/4 exact delivered binaries

### 1. Door Control

`N23_CASTLE_ENTRANCE_DOOR_CONTROL_REFERENCE_V001`

- SHA-256: `5718ce8c68069ca41143d666406a8c4cec3c285837a861337da758769bbfb652`
- bytes: `546,543`
- Git blob authority: `88eaa11f441a4c7c341dcbde04cb9f529f9ca6af`
- exact result: `PASS`

### 2. Neil

`AST_IMG_000073｜FACE_3Q_RIGHT`

- SHA-256: `92ef0fc973093c7cc99f3b70f3aab1fabd09d2d82c29921e72065f0d7b9ac366`
- bytes: `1,738,212`
- Git blob: `8179b112aae5253c0f8d9dffe4cfe451d94dacbc`
- exact result: `PASS`

### 3. Guang Yong

`AST_IMG_000011｜FACE_FRONT`

- SHA-256: `7f88a3f8d68dbfea0058ff0379d0164380722d96ae1774364bcd8b79367ad6f5`
- bytes: `2,903,455`
- Git blob: `5490cd3101d0d878ef77b4a3a164ea2231bf3817`
- exact result: `PASS`

### 4. Generic Guest REAR_3Q

`BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q`

- SHA-256: `52ae779b86ca28e38c50bdf7bf935d08e25769d6ec9bcc73e71b9701f6604756`
- bytes: `2,373,958`
- Git blob: `3b72a8b8f0230231f3e2a6b0f7947f3c96b4a400`
- exact result: `PASS`

Overall:

`4/4 EXACT MATCH`

## Work handoff verification

The Artifact's `WORK_HANDOFF.md` explicitly contains:

- camera inside castle;
- oblique view toward Neil at physical right-side entrance door;
- physical right-side door does not imply screen-right placement;
- Door Control does not control camera / perspective / screen placement / lighting composition;
- `INTERIOR-SIDE / OBLIQUE / BROADSIDE-FIRST / DEPTH-SECOND`;
- Candidate 03 remains separately gated;
- Work must revalidate Bundle V003 `4/4` before any later generation.

Result:

`PASS`

## Important governance interpretation

The builder log emits:

`GENERATION_ALLOWED=TRUE`

This means only:

`THE FORMAL BUNDLE IS INTERNALLY VALID FOR USE IF A LATER PRODUCT OWNER GENERATION AUTHORIZATION IS GIVEN`

It does NOT itself constitute Product Owner authorization to generate Candidate 03.

Project-level Candidate 03 generation remains:

`NOT AUTHORIZED`

## Next gate

`PRODUCT OWNER AUTHORIZATION → WORK N23 CANDIDATE 03 CLEAN REGENERATION / EXACTLY ONE 941×1672 PNG / STOP FOR REVIEW`
