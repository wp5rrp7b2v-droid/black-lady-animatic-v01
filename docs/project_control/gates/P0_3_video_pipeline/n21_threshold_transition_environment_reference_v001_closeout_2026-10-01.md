# N21 Threshold Transition Environment Reference V001｜Formal Closeout

Date: 2026-10-01

Status:

`PRODUCT OWNER APPROVED / CANONICAL PUBLISHED / EXACT BINARY VERIFIED / CONTROLLED REFERENCE REGISTERED / CLOSED`

## 1. Formal identity

Reference ID:

`N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001`

Classification:

`P0.3_CONTROLLED_PRODUCTION_REFERENCE`

Asset role:

`CONTROLLED_ENVIRONMENT_REFERENCE`

Authority scope:

`N21_THRESHOLD_TRANSITION_ENVIRONMENT_ONLY`

Canonical PNG:

`production/environment_references/n21_threshold_transition/N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001.png`

Canonical manifest:

`production/environment_references/n21_threshold_transition/N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001.manifest.json`

This reference is:

- not a Story Shot;
- not a primary Scene Master;
- not a strict 180-degree reverse-angle reconstruction;
- not a replacement for `AST_IMG_000052`;
- approved for controlled N21 threshold-transition environment use.

## 2. Product Owner approval + source intake

Product Owner explicitly approved the selected environment image on 2026-10-01.

Staging upload path:

`staging/n21_threshold_transition_environment_reference_v001_intake/N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001_APPROVED.png`

Product Owner upload commit:

`5ecc61e112180fa55b5b8b7a15f093b17e075b08`

Uploaded source Git blob:

`358057948ec222bbe63a47a07022de4453e20fc8`

Staging source was removed after successful canonical publication and verification.

## 3. Approved exact binary

- dimensions: `941 × 1672`
- format: `PNG`
- PNG mode: `RGBA`
- byte size: `3394494`
- SHA-256: `dd1b2dc6b831b2e22d8dc249859af1b4f65da6a20437cd8821627144e89a4f13`
- Git blob: `358057948ec222bbe63a47a07022de4453e20fc8`

## 4. Canonical publication

Publication method:

`EXACT_GIT_BLOB_REUSE_NO_REENCODE`

Publication commit:

`7108530b3bbed4bf01aac73c164978210545e4a9`

The canonical PNG reused the exact approved staging Git blob.

No resize, re-export, recolor, compression rewrite, or pixel modification occurred.

Manifest finalization commit:

`b4ea39622242363a43af723e12091b62192cbfe4`

## 5. Post-publication exact verification

Workflow run:

`36857195935`

Job:

`110352417813`

Result:

`SUCCESS / EXACT_BINARY_MATCH=YES / OVERALL_RESULT=PASS`

Verified checks:

- byte size: PASS
- SHA-256: PASS
- Git blob: PASS
- dimensions: PASS
- PNG mode: PASS
- manifest SHA: PASS
- manifest Git blob: PASS
- manifest byte size: PASS
- manifest dimensions: PASS
- manifest mode: PASS

Verified canonical identity:

- SHA-256: `dd1b2dc6b831b2e22d8dc249859af1b4f65da6a20437cd8821627144e89a4f13`
- Git blob: `358057948ec222bbe63a47a07022de4453e20fc8`
- bytes: `3394494`
- dimensions: `941x1672`
- mode: `RGBA`

## 6. Registration model

This reference is formally registered by its canonical PNG + canonical sidecar manifest.

It is intentionally NOT inserted into P0.2 `production/asset_registry/asset_registry.jsonl`.

Reason:

P0.2 Entity / Asset Registry Schema V0.3 is locked and currently supports `ATOMIC / DERIVED_REFERENCE / SHOT` with the existing Scene role vocabulary centered on `SCENE_MASTER`. Silently inserting a new controlled-environment asset class or role would constitute an unapproved schema extension.

Therefore the formal registration model is the same P0.3 Controlled Reference pattern already used by the Character Visual Style Reference:

`canonical binary + controlled manifest + exact verification + Project Control audit`

## 7. Authority / usage boundary

May control:

- N21 threshold-transition spatial staging;
- usable doorway width and perceived scale;
- interior-to-interior threshold relationship;
- warm low-key environmental continuity;
- stone / wood / floor environmental language;
- partial concealment of deeper space.

Must NOT control:

- strict reverse-angle geometry of `AST_IMG_000052`;
- complete First Hall layout;
- named-character identity;
- character wardrobe;
- crowd pose;
- unrelated Story Shot composition.

## 8. Source lineage

Scene-fact origin:

`AST_IMG_000052`

Tonal / lighting continuity:

`N20_DO_NOT_TOUCH_THINGS_APPROVED_V001`

Interpretation boundary:

This reference is a controlled production environment asset derived for N21 staging. It is not evidence that the unseen reverse geometry of `AST_IMG_000052` has been reconstructed exactly.

## 9. Cleanup

Completed:

- approved staging PNG removed after verification;
- staging intake README removed;
- one-time exact verifier workflow removed.

Canonical PNG and manifest remain the formal production records.

## 10. Closeout

`N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001 = FORMALLY CLOSED`

Next formal step:

`N21_REFERENCE_DELIVERY_BUNDLE_V005 DESIGN`

Proposed V005 image-input structure:

1. `N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001`
   - environment / threshold / lighting / tonal authority;
2. `CHARACTER_VISUAL_STYLE_REFERENCE_V001`
   - human visual-style authority.

Candidate 07 remains:

`NOT YET GENERATED / REQUIRES SEPARATE PRODUCT OWNER AUTHORIZATION`

N22 remains:

`NOT STARTED`

RISK-003 remains ACTIVE until real Candidate 07 evidence exists.
