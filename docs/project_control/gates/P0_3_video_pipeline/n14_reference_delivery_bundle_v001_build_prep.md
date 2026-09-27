# N14｜Reference Delivery Bundle V001｜Build Prep

Status: `EXECUTED / BUILD SUCCESS / 5 OF 5 PASS`

Date: 2026-09-27

## 1. Authorized target

- Bundle: `N14_REFERENCE_DELIVERY_BUNDLE_V001`
- Target generation: `N14 Candidate 01`
- Workflow: `.github/workflows/p03-n14-reference-delivery-bundle-v001.yml`
- Retention: `7 days`
- Product Owner manual reference upload: `0`

## 2. Locked reference set

1. A04 immediate continuity
2. AST_IMG_000034 / Ning FACE_FRONT
3. AST_IMG_000032 / Ning BODY_FRONT
4. AST_IMG_000026 / Neil BODY_FRONT secondary referent
5. AST_IMG_000052 / Castle Entrance Scene Master

## 3. Locked exclusions

- N11 Candidate 03
- N12 Candidate 02
- N13 Candidate 01
- N13_REFERENCE_DELIVERY_BUNDLE_V001
- A05
- N15
- key / waist / pocket / lock symbolism
- all rejected / superseded candidates

## 4. Validation contract

Build fails closed unless all five canonical PNGs pass:

- Registry / Story Shot index cardinality
- identity / role / authority
- APPROVED status
- CURRENT lifecycle
- canonical path
- byte size
- SHA-256 where locked
- Git blob
- PNG signature / readable dimensions
- regular file / no symlink
- byte-identical copy
- final artifact revalidation

For A04, the build verifies locked path + byte size + Git blob and computes the exact SHA-256 into the manifest.

Expected success line:

`PASS: 5/5 exact canonical reference binaries verified`

## 5. Execution result

- Product Owner authorized construction.
- Source commit: `ae34a3a5722473f1888d23db2f1f9a596f6978bb`
- Workflow run: `36317403211`
- Job: `108614612409`
- Conclusion: `SUCCESS`
- Artifact ID: `10931321832`
- Artifact digest: `sha256:40236e5e4d33f1d0a5b76eef455ff51ca688238fef42fdb054987ecc60bc317a`
- Artifact size: `12618491` bytes
- Expires: `2026-10-04T11:57:56Z`
- Verification: `5/5 exact canonical reference binaries verified`

Build record:

`docs/project_control/gates/P0_3_video_pipeline/n14_reference_delivery_bundle_v001_build_record_2026-09-27.md`

## 6. Boundary

Build is complete.

Authorized next step:

`Work automatic artifact acquisition + 5/5 revalidation → generate exactly one N14 Candidate 01`

Do not begin N15 or Story Shot registration before Product Owner review of N14.
