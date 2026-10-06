# N24_REFERENCE_DELIVERY_BUNDLE_V002｜Formal Build Record

Date:

`2026-10-06`

Status:

`FORMAL BUILD PASS / ARTIFACT EXACT VERIFIED / 6 OF 6 MATCH / CANDIDATE 01 NOT AUTHORIZED`

Bundle:

`N24_REFERENCE_DELIVERY_BUNDLE_V002`

Target:

`N24 Candidate 01｜Clean Regeneration`

Spec:

`production/bundle_specs/N24_REFERENCE_DELIVERY_BUNDLE_V002.json`

Spec revision:

`V002-R2`

Formal-build authorization record:

`docs/project_control/gates/P0_3_video_pipeline/n24_reference_delivery_bundle_v002_formal_build_authorization_2026-10-06.md`

Spec authorization commit:

`8c94428ffc531b18a3744db194998a5c12ea3d04`

## GitHub Actions

Workflow:

`Story Shot Reference Bundle Builder`

Run:

`37420742768`

Job:

`112129308908`

Conclusion:

`SUCCESS`

Builder log:

- `BUILD_AUTHORIZED=true`
- `PASS: 6/6 exact canonical reference binaries verified`
- `GENERATION_ALLOWED=TRUE`
- `BUNDLE_ID=N24_REFERENCE_DELIVERY_BUNDLE_V002`

Interpretation of `GENERATION_ALLOWED=TRUE`:

This is a technical Bundle-manifest flag only. Product Owner governance remains authoritative. N24 Candidate 01 generation is still NOT authorized until a separate explicit Product Owner authorization.

## Artifact

Artifact ID:

`11392483673`

Artifact name:

`N24_REFERENCE_DELIVERY_BUNDLE_V002`

Artifact size:

`16,266,150 bytes`

Artifact digest:

`sha256:dee66ea50062daefbf85ce1e0485a69e30128197dcd93e6ea180ef8494620313`

Retention expiry:

`2026-10-13T05:53:06Z`

## Independent Artifact ZIP verification

Downloaded Artifact ZIP was independently hashed after retrieval.

Downloaded ZIP:

- byte size: `16,266,150`
- SHA-256: `dee66ea50062daefbf85ce1e0485a69e30128197dcd93e6ea180ef8494620313`

GitHub Artifact digest:

- SHA-256: `dee66ea50062daefbf85ce1e0485a69e30128197dcd93e6ea180ef8494620313`

Result:

`ZIP DIGEST MATCH = YES`

Artifact contains exactly:

- `delivery_manifest.json`
- `WORK_HANDOFF.md`
- 6 direct PNG references

Total entries:

`8`

## Exact reference verification

### 1. A06_APPROVED_STORY_SHOT

- dimensions: `941 × 1672`
- bytes: `3,139,664`
- SHA-256: `fdfa27c14f09425c04785808ecd7432aca7c1d29870a8a5f33cba9a38b62e827`
- Git blob: `1023a67d96a8820def1259e3b0568c259ee55433`
- result: `MATCH`

### 2. N23_APPROVED_STORY_SHOT

- dimensions: `941 × 1672`
- bytes: `2,697,400`
- SHA-256: `2d94488e36d878ccb6ae7c3f9f3bf2a122eebca5ae01ad0e5b3105de4d535973`
- Git blob: `649ed97addf97f126a05e12d43325720a624ea19`
- result: `MATCH`

### 3. AST_IMG_000013｜GUANG_YONG REAR_3Q_RIGHT V001

- dimensions: `941 × 1672`
- bytes: `2,906,146`
- SHA-256: `848d350468f67704d932fbdfe030201dbd815b333db22e874864cd82f9755f60`
- Git blob: `d4b9bb9dec872a35fb8ca8524bd8dfa059dfdfd6`
- result: `MATCH`

### 4. AST_IMG_000066｜NEIL REAR_3Q_RIGHT V001

- dimensions: `941 × 1672`
- bytes: `1,656,490`
- SHA-256: `7f8cb635945e20035ba1b39dafecdf4caecc520d8e8794f67e39c2cfa1a6dad6`
- Git blob: `7616c7ccce52f0754e3e4c11f89a288db2186330`
- result: `MATCH`

### 5. AST_IMG_000105｜SCENE_CASTLE_ENTRANCE V002

- dimensions: `1448 × 1086`
- bytes: `3,495,795`
- SHA-256: `85b1a6020caba327f88541a2ea75d676da08f491e0534ef9fd30425f846a0fd9`
- Git blob: `052b42bf9459f70cb39679c5e2ef73475057547e`
- result: `MATCH`

### 6. GENERIC GUEST REAR_3Q

- dimensions: `1536 × 1024`
- bytes: `2,373,958`
- SHA-256: `52ae779b86ca28e38c50bdf7bf935d08e25769d6ec9bcc73e71b9701f6604756`
- Git blob: `3b72a8b8f0230231f3e2a6b0f7947f3c96b4a400`
- result: `MATCH`

Overall:

`6/6 EXACT MATCH`

## Handoff verification

`delivery_manifest.json`:

- bundle_id = `N24_REFERENCE_DELIVERY_BUNDLE_V002`
- reference_count = `6`
- all_reference_checks_pass = `true`
- overall_result = `PASS`

`WORK_HANDOFF.md`:

`PRESENT / INCLUDED / N24 V0.3 GUANG YONG QUESTION HANDOFF CONFIRMED`

## Governance boundary

Completed:

- Formal Bundle V002 Build;
- GitHub Actions build PASS;
- Artifact created;
- Artifact ZIP exact digest independently verified;
- 6/6 reference binaries independently exact-verified;
- manifest / handoff verified.

Still NOT authorized:

- Work Candidate 01 generation;
- Candidate 02;
- Canonical Publication;
- Story Shot Registration;
- N25 production.

Historical:

- N24 Bundle V001 remains preserved as verified history for the superseded "Following the Guide" design and is not a generation input.

Next gate:

`PRODUCT OWNER AUTHORIZATION → N24 CANDIDATE 01 / EXACTLY 1 PNG / CLEAN REGENERATION`
