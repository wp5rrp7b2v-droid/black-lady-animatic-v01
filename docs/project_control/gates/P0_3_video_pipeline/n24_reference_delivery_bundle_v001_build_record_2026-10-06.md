# N24_REFERENCE_DELIVERY_BUNDLE_V001｜Formal Build Record

Date:

`2026-10-06`

Status:

`FORMAL BUILD PASS / ARTIFACT EXACT VERIFIED / 5 OF 5 MATCH / CANDIDATE 01 NOT AUTHORIZED`

Bundle:

`N24_REFERENCE_DELIVERY_BUNDLE_V001`

Target:

`N24 Candidate 01｜Clean Regeneration`

Spec:

`production/bundle_specs/N24_REFERENCE_DELIVERY_BUNDLE_V001.json`

Spec revision:

`V001-R2`

Formal-build authorization record:

`docs/project_control/gates/P0_3_video_pipeline/n24_reference_delivery_bundle_v001_formal_build_authorization_2026-10-06.md`

Spec authorization commit:

`0a85e35037556fa671338e02249f3b6bf706264e`

## GitHub Actions

Workflow:

`Story Shot Reference Bundle Builder`

Run:

`37414975422`

Job:

`112111492358`

Conclusion:

`SUCCESS`

Builder log:

- `BUILD_AUTHORIZED=true`
- `PASS: 5/5 exact canonical reference binaries verified`
- `GENERATION_ALLOWED=TRUE`
- `BUNDLE_ID=N24_REFERENCE_DELIVERY_BUNDLE_V001`

Interpretation of `GENERATION_ALLOWED=TRUE`:

This is a technical Bundle manifest flag only. Product Owner governance remains authoritative; N24 Candidate 01 generation is still NOT authorized until a separate explicit Product Owner approval.

## Artifact

Artifact ID:

`11390787884`

Artifact name:

`N24_REFERENCE_DELIVERY_BUNDLE_V001`

Artifact size:

`12,614,829 bytes`

Artifact digest:

`sha256:e9b40bcd5daa77f482d1a440824408884c77dd73b6fdba3d5759cd35c437a391`

Retention expiry:

`2026-10-13T04:42:50Z`

## Independent Artifact ZIP verification

Downloaded Artifact ZIP was independently hashed after retrieval.

Downloaded ZIP:

- byte size: `12,614,829`
- SHA-256: `e9b40bcd5daa77f482d1a440824408884c77dd73b6fdba3d5759cd35c437a391`

GitHub Artifact digest:

- SHA-256: `e9b40bcd5daa77f482d1a440824408884c77dd73b6fdba3d5759cd35c437a391`

Result:

`ZIP DIGEST MATCH = YES`

Artifact contains exactly:

- `delivery_manifest.json`
- `WORK_HANDOFF.md`
- 5 direct PNG references

Total entries:

`7`

## Exact reference verification

### 1. AST_IMG_000105｜SCENE_CASTLE_ENTRANCE V002

- dimensions: `1448 × 1086`
- bytes: `3,495,795`
- SHA-256: `85b1a6020caba327f88541a2ea75d676da08f491e0534ef9fd30425f846a0fd9`
- Git blob: `052b42bf9459f70cb39679c5e2ef73475057547e`
- result: `MATCH`

### 2. N23_APPROVED_STORY_SHOT

- dimensions: `941 × 1672`
- bytes: `2,697,400`
- SHA-256: `2d94488e36d878ccb6ae7c3f9f3bf2a122eebca5ae01ad0e5b3105de4d535973`
- Git blob: `649ed97addf97f126a05e12d43325720a624ea19`
- result: `MATCH`

### 3. AST_IMG_000037｜NING REAR_3Q_RIGHT V002

- dimensions: `941 × 1672`
- bytes: `2,395,616`
- SHA-256: `c56e30657c65942899caa1f5e36e21f8f835a5835325fa68c70b64d754fa70d2`
- Git blob: `f03493d845b3f1c7194075781217d97f1e1e9b35`
- result: `MATCH`

### 4. AST_IMG_000066｜NEIL REAR_3Q_RIGHT V001

- dimensions: `941 × 1672`
- bytes: `1,656,490`
- SHA-256: `7f8cb635945e20035ba1b39dafecdf4caecc520d8e8794f67e39c2cfa1a6dad6`
- Git blob: `7616c7ccce52f0754e3e4c11f89a288db2186330`
- result: `MATCH`

### 5. GENERIC GUEST REAR_3Q

- dimensions: `1536 × 1024`
- bytes: `2,373,958`
- SHA-256: `52ae779b86ca28e38c50bdf7bf935d08e25769d6ec9bcc73e71b9701f6604756`
- Git blob: `3b72a8b8f0230231f3e2a6b0f7947f3c96b4a400`
- result: `MATCH`

Overall:

`5/5 EXACT MATCH`

## Handoff verification

`delivery_manifest.json`:

- bundle_id = `N24_REFERENCE_DELIVERY_BUNDLE_V001`
- reference_count = `5`
- all_reference_checks_pass = `true`
- overall_result = `PASS`

`WORK_HANDOFF.md`:

`PRESENT / INCLUDED`

## Governance boundary

Completed:

- Formal Bundle V001 Build;
- GitHub Actions build PASS;
- Artifact created;
- Artifact ZIP exact digest verified;
- 5/5 reference binaries independently exact-verified;
- manifest / handoff presence verified.

Still NOT authorized:

- Work Candidate 01 generation;
- Candidate 02;
- Canonical Publication;
- Story Shot Registration;
- N25.

Next gate:

`PRODUCT OWNER AUTHORIZATION → N24 CANDIDATE 01 / EXACTLY 1 PNG / CLEAN REGENERATION`
