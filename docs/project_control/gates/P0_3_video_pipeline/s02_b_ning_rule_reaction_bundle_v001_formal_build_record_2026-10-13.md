# S02-B 宁秋水「夫人的要求」反应插镜｜Bundle V001 Formal Build & Exact Binary Verification

Date: 2026-10-13

**Status: FORMAL BUNDLE BUILD PASS / ARCHIVE ZIP DIGEST MATCH / 3 OF 3 EMBEDDED PNG EXACT MATCH / WORK GENERATION NOT AUTHORIZED**

## Authorization boundary

Product Owner approved formal reference Bundle V001 build and subsequent artifact exact verification only, following Validation-only run 38328900831 (3/3 PASS, 0 artifacts). No Work generation, candidate PNG, video edits, canonical publication, or Story Shot registration was authorized.

Bundle ID: `TAIL_NING_REACTION_TEST_01_REFERENCE_DELIVERY_BUNDLE_V001`  
Temporary editorial test shot ID: `TAIL_NING_REACTION_TEST_01` (NOT an approved or registered Story Shot).  
Spec: `production/bundle_specs/TAIL_NING_REACTION_TEST_01_REFERENCE_DELIVERY_BUNDLE_V001.json`  
Spec prior Validation-only blob: `1a59a929f5212b4029c0f8f4209456826a94aada`  
Formal-build active Spec blob: `76b2ed4fe4c2c5fec0ffd01bebdf9111d215050e`  
Formal build authorization commit: `de4d0442800e19d87680406bd5b80d8efeac49e7`  
Spec `build_authorized`: `true`, strictly enabling reference Bundle generation; `formal_build_authorization.candidate_01_generation_authorized`: `false`.

## GitHub Actions

- Workflow: Story Shot Reference Bundle Builder
- Run ID: `38333161748`
- Job ID: `115087255648`
- Run URL: https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/38333161748
- Head SHA: `de4d0442800e19d87680406bd5b80d8efeac49e7`
- Run status / conclusion: `completed / success`
- Build verified reference bundle: `success`
- Upload verified bundle: `success`
- Job log: `PASS: 3/3 exact canonical reference binaries verified`
- Builder log `GENERATION_ALLOWED=TRUE` = machine package readiness only, **not PO permission to run Work**.

## Published workflow Artifact and downloaded archive

- Artifact ID: `11783891178`
- Artifact name: `TAIL_NING_REACTION_TEST_01_REFERENCE_DELIVERY_BUNDLE_V001`
- Artifact count for run: `1`
- ZIP byte size: `5398660`
- GitHub-reported artifact digest: `sha256:314b5bdac45e8cde34f90c3c195bff5544fedbaec69d45264f07051088dca5c6`
- Independently computed SHA-256 from downloaded ZIP: `314b5bdac45e8cde34f90c3c195bff5544fedbaec69d45264f07051088dca5c6`
- **ZIP digest: MATCH**
- ZIP integrity: `testzip() == None`, entries unique, no traversal/absolute paths.

Downloaded ZIP file was inspected in the current execution container. Contains **exactly 5 entries**:
- `delivery_manifest.json`
- `WORK_HANDOFF.md`
- `ning_global_identity/AST_IMG_000060__CHAR_NING_QIUSHUI_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `ning_face_identity/AST_IMG_000071__CHAR_NING_QIUSHUI_FACE_3Q_LEFT_DEFAULT_DEFAULT_V001.png`
- `inner_lobby_scene/AST_IMG_000108__SCENE_CASTLE_ENTRANCE_INNER_LOBBY_SCENE_MASTER_DEFAULT_DEFAULT_V001.png`

Manifest:
- `reference_count:3`
- `all_reference_checks_pass:true`
- `overall_result:PASS`
- `manual_product_owner_reference_upload:0`
- `generation_allowed:true` — a technical manifest flag, NOT human authorization.

## Independent embedded PNG binary audit

Each embedded ZIP PNG was loaded and independently hashed from bytes, with Git-style SHA-1 blob calculation, byte-size comparison, 8-byte PNG signature, IHDR dimensions and comparison to manifest expected/computed fields:

| Reference | bytes | dimensions | SHA-256 expected and actual | Git blob expected and actual | Result |
|---|---:|---|---|---|---|
| `AST_IMG_000060` | 1,123,635 | 1440×1620 | `15ec6c2682da0fe2502267bde21e9bc0bd7104bbf3e6041521121cc69a0e77be` | `b674733242ab5d603dc42c53b8f7582003064499` | EXACT MATCH |
| `AST_IMG_000071` | 1,761,408 | 941×1672 | `8d92bcc601220654499f7be57fc83411c57dedccc44e8f764cc65ce1b840334e` | `31cfa62e27233b2a955e3201d5a88f96ad1dc6c3` | EXACT MATCH |
| `AST_IMG_000108` | 2,541,370 | 1448×1086 | `f16d98a977eb73c75249cd3692ebfce9e3cd12cfbcbdb171d5b652149cb7c1a3` | `91471e32dab1c7b51b7e718ffd539305d81daf85` | EXACT MATCH |

Total = **3/3 independent SHA-256 + bytes + blob + dimensions + PNG-signature match**.

WORK_HANDOFF.md is present and readable; explicitly states Bundle readiness is not authorization to generate, direct-input limit exactly 3, and N25/N26 pixel-level axis review must be done before Work generation. No candidate output present.

## Unchanged safeguards / next gate

- Formal Bundle package build complete; no need to re-run this same build.
- **N25/N26 actual approved pixel-level image review for movement direction, camera axis, architectural and lighting continuity is still PENDING**. Previously verified Git blob identities are not a substitute for picture inspection.
- **Work Candidate 01 generation = NOT AUTHORIZED**; separately obtain PO approval after N25/N26 picture review.
- N25 and N26 approved PNGs, N27 absorbed decision, 64.25s approved S02-B V001 master, N16–N17 21.95s V004 segment, Story Shot Index, Video Index all remain unchanged.
- Tail V001/V002 remain NOT APPROVED; P0.3 remains IN PROGRESS.
