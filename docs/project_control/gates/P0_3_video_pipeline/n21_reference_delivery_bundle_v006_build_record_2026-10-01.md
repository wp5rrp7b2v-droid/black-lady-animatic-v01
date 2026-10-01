# N21 Reference Delivery Bundle V006｜Formal Build + Exact Verification

Date: 2026-10-01

Status:

`FORMAL BUILD PASS / 2 OF 2 EXACT VERIFIED / INDEPENDENT ARTIFACT VERIFIED / GENERATION_ALLOWED=TRUE AT BUNDLE LEVEL / CANDIDATE 08 NOT YET AUTHORIZED`

Bundle:

`N21_REFERENCE_DELIVERY_BUNDLE_V006`

Target:

`N21 Candidate 08｜Clean Regeneration`

## 1. Product Owner authorization

Product Owner authorized:

`Formal N21_REFERENCE_DELIVERY_BUNDLE_V006 Build + Exact Verification`

This authorization does not automatically authorize:

- Work generation;
- Candidate 08;
- Candidate 09;
- N22;
- Story Shot publication / registration.

## 2. Formal Spec

Spec:

`production/bundle_specs/N21_REFERENCE_DELIVERY_BUNDLE_V006.json`

Formal build revision:

`V006-R2`

Build gate:

`build_authorized=true`

Authorization commit:

`b76b5834290d0b4eda863b63a1cea12c3d07071a`

Formal references:

1. `N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001` — threshold environment / lighting / spatial authority only
2. `N21_CROWD_BODY_WARDROBE_REFERENCE_V001` — human body / wardrobe / natural-human-language authority only

Explicitly excluded:

- `CHARACTER_VISUAL_STYLE_REFERENCE_V001`;
- complete Scene Master;
- complete Story Shot;
- N20 / N19 / N03 / N08;
- named-character Character Sheets;
- Atomic character appearance references;
- N21 Candidate 01–07;
- third image reference.

## 3. GitHub Actions result

Workflow:

`Story Shot Reference Bundle Builder`

Run:

`36879153275`

Job:

`110426184563`

Conclusion:

`SUCCESS`

Builder output:

- `BUILD_AUTHORIZED=true`
- `PASS: 2/2 exact canonical reference binaries verified`
- `GENERATION_ALLOWED=TRUE`
- `BUNDLE_ID=N21_REFERENCE_DELIVERY_BUNDLE_V006`

Artifact:

`N21_REFERENCE_DELIVERY_BUNDLE_V006`

Artifact ID:

`11171365040`

Artifact size:

`4813649 bytes`

Artifact digest:

`sha256:e9e718893de20d86e90352ba7bf2ece0c7fa4f242a3b22f436bf727e9760a0c0`

Expires:

`2026-10-08T14:47:56Z`

## 4. Independent Artifact ZIP verification

Chat independently downloaded Artifact `11171365040`.

Downloaded ZIP:

- byte size: `4813649`
- SHA-256: `e9e718893de20d86e90352ba7bf2ece0c7fa4f242a3b22f436bf727e9760a0c0`

GitHub Artifact digest:

`sha256:e9e718893de20d86e90352ba7bf2ece0c7fa4f242a3b22f436bf727e9760a0c0`

Result:

`MATCH`

## 5. Artifact contents

Exactly four files were present:

- `WORK_HANDOFF.md`
- `delivery_manifest.json`
- `environment_authority/N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001__N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001.png`
- `crowd_body_wardrobe_authority/N21_CROWD_BODY_WARDROBE_REFERENCE_V001__N21_CROWD_BODY_WARDROBE_REFERENCE_V001.png`

No complete Scene Master, complete Story Shot, named-character Character Sheet, Candidate 01–07, Character Visual Style Reference or third PNG input was present.

## 6. Independent exact binary verification

### REF-01｜N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001

Artifact copy:

- PNG signature: `PASS`
- dimensions: `941 × 1672`
- mode: `RGBA`
- bit depth: `8`
- bytes: `3394494`
- SHA-256: `dd1b2dc6b831b2e22d8dc249859af1b4f65da6a20437cd8821627144e89a4f13`
- Git blob: `358057948ec222bbe63a47a07022de4453e20fc8`

Result:

`EXACT MATCH`

### REF-02｜N21_CROWD_BODY_WARDROBE_REFERENCE_V001

Artifact copy:

- PNG signature: `PASS`
- dimensions: `1536 × 1024`
- mode: `RGBA`
- bit depth: `8`
- bytes: `1418940`
- SHA-256: `73bb645e5a22cccb53faf8eb2d4b8fc0b876980e7520a2bc54daab1207439dc6`
- Git blob: `2b86ab207ee60ba0cd2de277bb55900b8854099c`

Result:

`EXACT MATCH`

## 7. delivery_manifest verification

Observed:

- `bundle_id = N21_REFERENCE_DELIVERY_BUNDLE_V006`
- `target_shot_id = N21`
- `target_candidate = N21 Candidate 08`
- `reference_count = 2`
- `all_reference_checks_pass = true`
- `generation_allowed = true`
- `manual_product_owner_reference_upload = 0`
- `overall_result = PASS`

Both reference rows independently report:

- expected SHA = computed SHA;
- expected bytes = actual bytes;
- expected Git blob = actual Git blob;
- PNG signature = PASS;
- byte-identical copy = PASS.

## 8. Human-reference decoupling verification

`WORK_HANDOFF.md` correctly carries the locked V006 design boundary.

It explicitly states:

- Human Reference is limited to natural adult body proportions, posture, head/neck/shoulder relationship, contemporary ordinary wardrobe and general rear/side/rear-three-quarter human language;
- the four-person cast in the Human Reference must not be copied;
- person count, named identities, complete outfits, left/right order, relative spacing, original facing directions, exact poses and four-person composition must not be copied;
- Human Reference facing direction is not N21 direction authority;
- overall movement must read `THRESHOLD → DEEPER CASTLE INTERIOR`;
- main figures should favor back / rear-three-quarter / natural side views;
- the main group must not walk toward camera or collectively turn toward camera;
- authority priority remains:
  1. Story Shot blocking → crowd movement;
  2. Environment Reference → threshold / space;
  3. Human Reference → body naturalness / wardrobe language.

Result:

`HANDOFF BOUNDARY MATCHES APPROVED V006 DESIGN V0.2`

## 9. What this step proves

FACT:

- V006 formal two-reference Bundle can be built deterministically;
- both canonical controlled references survived transport byte-identically;
- the exact approved Human Reference is present in the production Artifact;
- the direction / identity decoupling instructions are present in the Work handoff;
- no unintended third visual authority entered the Artifact.

NOT PROVEN:

- that the generation model will obey the Human Reference boundary;
- that it will not visually copy the four-person cast;
- that movement direction will remain correct in the generated frame;
- that body proportion / wardrobe performance will improve;
- that Candidate 08 will visually PASS.

Those are Candidate 08 end-to-end test questions.

## 10. Current production boundary

Bundle V006:

`FORMAL / VERIFIED / READY FOR WORK DELIVERY`

Bundle-level:

`GENERATION_ALLOWED=TRUE`

Product Owner generation authorization:

`NOT YET GRANTED`

Therefore:

- Candidate 08: `NOT YET AUTHORIZED`
- Candidate 09: `NOT STARTED`
- N22: `NOT STARTED`
- Story Shot publication: `NOT AUTHORIZED`

Next gate:

`PRODUCT OWNER AUTHORIZATION → N21 CANDIDATE 08 WORK GENERATION`
