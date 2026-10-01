# N21 Crowd Body / Wardrobe Reference V001｜Closeout

Date: 2026-10-01

Status:

`PRODUCT OWNER APPROVED / CANONICAL / EXACT VERIFIED / MANIFESTED / CLOSED`

Reference:

`N21_CROWD_BODY_WARDROBE_REFERENCE_V001`

Classification:

`P0.3_CONTROLLED_PRODUCTION_REFERENCE`

Authority scope:

`N21_CROWD_BODY_WARDROBE_ONLY`

Asset role:

`CONTROLLED_HUMAN_BODY_WARDROBE_REFERENCE`

## 1. Product Owner approval

Approved candidate:

`Candidate 03`

Approval record:

`docs/project_control/gates/P0_3_video_pipeline/n21_crowd_body_wardrobe_reference_v001_candidate_03_approval_2026-10-01.md`

Approval record commit:

`59c6615b79636dca98793a389e4824cb0a8e7330`

Candidate 01 and Candidate 02 are not approved.

## 2. Exact approved binary identity

Canonical PNG:

`production/human_references/n21_crowd_body_wardrobe/N21_CROWD_BODY_WARDROBE_REFERENCE_V001.png`

Exact identity:

- format: `PNG`
- dimensions: `1536 × 1024`
- mode: `RGBA`
- bit depth: `8`
- byte size: `1418940`
- SHA-256: `73bb645e5a22cccb53faf8eb2d4b8fc0b876980e7520a2bc54daab1207439dc6`
- Git blob: `2b86ab207ee60ba0cd2de277bb55900b8854099c`

## 3. Exact intake verification

Actual uploaded staging source:

`staging/n21_crowd_body_wardrobe_reference_v001_intake/N21_CROWD_BODY_WARDROBE_REFERENCE_V001_CANDIDATE_03_APPROVED.png`

Uploaded staging byte size:

`1418940`

Uploaded staging Git blob:

`2b86ab207ee60ba0cd2de277bb55900b8854099c`

Verifier workflow:

`N21 Crowd Body Wardrobe Reference V001 Intake Verify`

Workflow creation commit:

`55a5eaf0aa2930cb63e6d53503d04cf9a5e53e8a`

Run:

`36873981603`

Job:

`110408581874`

Result:

- byte size: PASS
- SHA-256: PASS
- Git blob: PASS
- dimensions: PASS
- mode: PASS
- bit depth: PASS
- `EXACT_BINARY_MATCH=YES`
- `OVERALL_RESULT=PASS`

## 4. Canonical publication

Publication request:

`production/publication_requests/N21_CROWD_BODY_WARDROBE_REFERENCE_V001.json`

Request commit:

`3791888f5f063211d2e3268de44e4b327734d693`

Publication method:

`EXACT_GIT_BLOB_REUSE_NO_REENCODE`

Canonical publication commit:

`e1d3a82da4b96eb0f20f2a629ef1140d4668b650`

The canonical PNG reuses exact Git blob:

`2b86ab207ee60ba0cd2de277bb55900b8854099c`

No image re-encoding, resize, color conversion or re-export occurred.

## 5. Canonical exact verification

Verifier workflow:

`N21 Crowd Body Wardrobe Reference V001 Canonical Verify`

Workflow creation commit:

`810c817e711e1fbd2a3c64bf03947b599597a0b5`

Run:

`36874219371`

Job:

`110409384685`

Result:

- byte size: PASS
- SHA-256: PASS
- Git blob: PASS
- dimensions: PASS
- mode: PASS
- bit depth: PASS
- `EXACT_BINARY_MATCH=YES`
- `OVERALL_RESULT=PASS`

## 6. Controlled Reference Manifest

Manifest:

`production/human_references/n21_crowd_body_wardrobe/N21_CROWD_BODY_WARDROBE_REFERENCE_V001.manifest.json`

Manifest finalization commit:

`3ca26550b9afc03940728495439af5cfb31adda1`

The manifest records:

- Product Owner approval;
- exact approved binary identity;
- four Atomic source anchors;
- input Bundle lineage;
- exact intake verification;
- exact canonical publication;
- exact canonical verification;
- usage boundaries.

## 7. Governance boundary

This reference may control:

- natural adult body proportions;
- upright walking posture;
- natural head / neck / shoulder relationship;
- contemporary everyday wardrobe era;
- project-consistent human silhouette;
- rear / side / rear-three-quarter body language;
- absence of backpack / shoulder bag / crossbody bag / luggage / expedition equipment.

It must NOT control:

- named-character identity;
- exact face;
- exact complete outfit;
- scene environment;
- scene lighting;
- Story Shot camera composition;
- unrelated crowd blocking.

It is NOT:

- a Story Shot;
- a Character Sheet;
- an Atomic character reference;
- a replacement for any existing character anchor.

It is not inserted into the locked P0.2 Asset Registry because Schema V0.3 has no controlled human body / wardrobe reference class.

## 8. Source lineage

Input Bundle:

`N21_CROWD_BODY_WARDROBE_REFERENCE_INPUT_BUNDLE_V001`

Artifact:

`11163447680`

Formal source anchors:

- `AST_IMG_000051` — Ning Qiushui rear 3/4
- `AST_IMG_000064` — Jun Luyuan rear 3/4
- `AST_IMG_000068` — Su Xiaoxiao rear 3/4
- `AST_IMG_000075` — Wen Qingya rear 3/4

The output is a controlled human-world reference, not a requirement to cast those four named characters in N21.

## 9. Cleanup

Completed:

- approved staging PNG removed: `5f198b069df4b34b75502ccbfe7a2eaee3d7c085`
- staging README removed: `e68def8de100ca7be2b901fc381a58a00a5b893b`
- intake verifier removed: `f52346b2c8c666c57adf499eec82ae0c0e0dc3bc`
- canonical verifier removed: `7ad6b247d9a9b852f79214741da1edd5750cec4c`

Cross-check after cleanup:

- canonical PNG: PRESENT
- canonical manifest: PRESENT
- canonical Git blob: `2b86ab207ee60ba0cd2de277bb55900b8854099c`
- staging intake directory: ABSENT
- temporary intake verifier: ABSENT
- temporary canonical verifier: ABSENT

## 10. N21 continuation boundary

N21 Candidate 08:

`NOT STARTED`

N22:

`NOT STARTED`

Director recommendation for the next N21 Bundle design:

Use exactly two controlled references:

1. `N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001`
2. `N21_CROWD_BODY_WARDROBE_REFERENCE_V001`

Do not automatically include `CHARACTER_VISUAL_STYLE_REFERENCE_V001` in the next generation input set. This is a design recommendation only and requires separate Product Owner approval before formal Bundle construction.

RISK-003 remains active until a new full-scene N21 generation provides real evidence.
