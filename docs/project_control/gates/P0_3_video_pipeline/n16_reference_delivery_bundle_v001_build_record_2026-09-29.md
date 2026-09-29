# N16 Reference Delivery Bundle V001 Build Record｜2026-09-29

Status: `BUILT / 6 OF 6 EXACT VERIFICATION PASS / READY FOR WORK GENERATION`

## 1. Generic Builder authority

Workflow:

`.github/workflows/story-shot-reference-bundle-builder.yml`

Builder:

`scripts/story_shot_reference_bundle_builder_v1.py`

Bundle Spec:

`production/bundle_specs/N16_REFERENCE_DELIVERY_BUNDLE_V001.json`

The Generic Story Shot Reference Bundle Builder replaces new per-shot workflow creation for subsequent Story Shots.

## 2. Build identity

- bundle_id: `N16_REFERENCE_DELIVERY_BUNDLE_V001`
- target_shot_id: `N16`
- sequence_id: `S02-B`
- target_candidate: `N16 Candidate 01`
- source commit: `4a9df630c36e2fc92ada929fcd80403ab57c74e3`
- workflow run ID: `36514238747`
- job ID: `109232868440`
- result: `SUCCESS`

## 3. Artifact identity

- artifact name: `N16_REFERENCE_DELIVERY_BUNDLE_V001`
- artifact ID: `11010505345`
- artifact digest: `sha256:e44c4fc8e9b8d1499af8866ac601137dd315ac1f386a544eec19b709ac5cd0ff`
- artifact size: `11932780` bytes
- expires at: `2026-10-06T02:47:42Z`
- retention: `7 days`

## 4. Exact reference verification

GitHub Actions builder result:

`PASS: 6/6 exact canonical reference binaries verified`

`GENERATION_ALLOWED=TRUE`

References:

1. `AST_IMG_000057`
   - SHA-256: `e8a0410cfc176ec9d6446b84f89b2c12d0683ec32b927c90353e850c416d909e`
   - bytes: `969995`
2. `AST_IMG_000072`
   - SHA-256: `be9f1f39ae303a61a79746b25a0f9f8153797b179ef85d07a5c2fdf1ce02d01b`
   - bytes: `2002451`
3. `AST_IMG_000060`
   - SHA-256: `15ec6c2682da0fe2502267bde21e9bc0bd7104bbf3e6041521121cc69a0e77be`
   - bytes: `1123635`
4. `AST_IMG_000033`
   - SHA-256: `7d2292494ab010b324e608f792912fd2d49766318e279bbe22170445464a5c1e`
   - bytes: `2688985`
5. `AST_IMG_000052`
   - SHA-256: `d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961`
   - bytes: `2305753`
6. `A03`
   - build-computed SHA-256: `5dc075a6f917fb7fdc05cf299315675bfdd5db4a0d737518ef4aafeacc78ee1e`
   - bytes: `2875484`
   - Git blob: `94d11064522425d908b1756fb0d845107c46a4e1`

## 5. Independent post-artifact verification

Chat downloaded Artifact ID `11010505345` after upload and independently re-read all delivered PNG binaries.

Result:

- file count: `6 PNG + delivery_manifest.json + WORK_HANDOFF.md`
- six delivered PNG SHA-256 values: `ALL MATCH`
- six delivered PNG byte sizes: `ALL MATCH`
- manifest: `all_reference_checks_pass=true`
- manifest: `generation_allowed=true`
- downloaded ZIP SHA-256: `e44c4fc8e9b8d1499af8866ac601137dd315ac1f386a544eec19b709ac5cd0ff`
- downloaded ZIP bytes: `11932780`

Artifact digest and downloaded ZIP identity therefore match exactly.

## 6. Transport result

- GitHub canonical references → Generic Builder: `PASS`
- exact binary verification: `6/6 PASS`
- short-lived Artifact publication: `PASS`
- Product Owner manual reference upload: `0`
- Work automatic artifact acquisition: `READY / NOT YET EXECUTED`

## 7. Current boundary

N16 Bundle construction is complete.

Authorized by this record:

`N16_REFERENCE_DELIVERY_BUNDLE_V001 = VALID PRODUCTION BUNDLE`

Not yet executed:

- Work image generation;
- N16 Candidate 01 Product Owner review;
- exact binary publication;
- Story Shot registration.

Next stage:

`Work automatic artifact acquisition + 6/6 revalidation → N16 Candidate 01`
