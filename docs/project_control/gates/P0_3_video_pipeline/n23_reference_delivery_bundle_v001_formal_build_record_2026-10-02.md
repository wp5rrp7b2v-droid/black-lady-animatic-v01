# N23 Reference Delivery Bundle V001｜Formal Build Record

Date: 2026-10-02

Status:

`FORMAL BUILD PASS / 4 OF 4 EXACT / ARTIFACT INDEPENDENTLY VERIFIED`

Bundle:

`N23_REFERENCE_DELIVERY_BUNDLE_V001`

Bundle Spec:

`production/bundle_specs/N23_REFERENCE_DELIVERY_BUNDLE_V001.json`

Authorized Spec commit:

`d88a9b882ebc1ddf78ed3701754ccb0e6791ebe2`

Spec revision:

`V001-R2`

Build authorization:

`build_authorized=true`

Workflow:

`Story Shot Reference Bundle Builder`

Workflow run:

`37006373075`

Job:

`110835506338`

Builder result:

`PASS: 4/4 exact canonical reference binaries verified`

`GENERATION_ALLOWED=TRUE`

Artifact:

- ID: `11225912126`
- Name: `N23_REFERENCE_DELIVERY_BUNDLE_V001`
- ZIP size: `5,426,263 bytes`
- GitHub Artifact digest: `sha256:ffb6ceb327fc405fb000639921188a4ec333d8082d4ec526dc1ecd1e5533b88d`
- Expires: 2026-10-09

Independent Artifact verification:

- ZIP downloaded independently after workflow completion.
- Recomputed ZIP SHA-256: `ffb6ceb327fc405fb000639921188a4ec333d8082d4ec526dc1ecd1e5533b88d` → MATCH.
- `delivery_manifest.json` present and reports `reference_count=4`, `overall_result=PASS`, `generation_allowed=true`.
- All four delivered PNGs independently rechecked for byte size, SHA-256, Git blob and PNG dimensions.
- Result: `4/4 EXACT MATCH`.

Verified delivered references:

1. `STORY_SHOT_N22`
   - 941×1672
   - 1,834,637 bytes
   - SHA-256 `6d1ed04106bb35943d752113e17d5f36fd2d55b29f4234e13177c7f8b6496f3a`
   - Git blob `a0f38041c10e4eb13a5a915a5d2f7bf22f85a2cf`

2. `AST_IMG_000052`
   - 941×1672
   - 2,305,753 bytes
   - SHA-256 `d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961`
   - Git blob `e4dafe096f5c5c8782257030a5a659aeec7808f9`

3. `AST_IMG_000059`
   - 1440×1620
   - 840,092 bytes
   - SHA-256 `964445754ec69dcfeace287d46b2964a6d5044c59950c5ede5553859e1e229de`
   - Git blob `4f818f91f706bf680b455557eefa43c24594b977`

4. `AST_IMG_000056`
   - 1440×540
   - 475,761 bytes
   - SHA-256 `2a98e74ddba60a259758643b56ffddafd5a7cb30de040880f991fb47216b45fb`
   - Git blob `e37ad60d933c3fdc434768bb449019146eb9333e`

Important separation of authority:

`GENERATION_ALLOWED=TRUE` means the verified Bundle is technically usable.

It does NOT authorize Work generation.

N23 Candidate 01 remains:

`NOT AUTHORIZED`

Next required authority:

`PRODUCT OWNER N23 CANDIDATE 01 WORK-GENERATION AUTHORIZATION`
