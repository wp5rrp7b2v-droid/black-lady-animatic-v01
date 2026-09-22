# D-070｜Published Binary Adoption + 21-Asset Automatic Ingest｜Closeout

Status: `ENGINEERING COMPLETE / FORMAL ADOPTION COMPLETE / RESCUE REMOTE PUBLICATION READY / PRODUCT OWNER REVIEW REQUIRED`

Source baseline: `3d3aebba8ca458dcdb133c77e3611f037f2fc49a / R071`

## Scope

D-070 closes the formal-ingest gap for the 21 Product Owner-approved Character Core PNGs that were already published byte-for-byte to canonical GitHub paths in commit `b9bafa2af4b9be8aadf2bd2abe79b724837eff88`.

No PNG is regenerated, resized, re-encoded, copied, deleted, replaced, or rewritten by the adoption path.

## Controller

`scripts/automatic_ingest_controller_v0_1.py` now includes fail-closed `--adopt-existing` behavior:

- source must be the exact canonical target;
- target must be a regular file;
- target must already be Git-tracked;
- target must have no uncommitted changes;
- SHA is verified before Registry/Audit mutation;
- adoption excludes the PNG itself from the touched/staged set;
- explicit version reservation is required for intentional contiguous gaps;
- unacknowledged version skipping remains blocked.

Jun Luyuan `PROFILE_LEFT V002` uses explicit reservation of rejected/do-not-ingest `V001`.

## Formal admission

- New Asset IDs: `AST_IMG_000063–AST_IMG_000083`
- New formal assets: `21`
- Registry count: `62 → 83`
- Required D-070 Audit events: `42`
  - `ASSET_APPROVED = 21`
  - `ASSET_INGESTED = 21`
- D-070 relations: `0`
- Formal Character Core Coverage: `42/63 → 63/63`
- Formal Core gap: `21 → 0`
- Single Current: `63/63 PASS`

No supersession relation is required because all 21 admissions fill previously empty formal slots.

## Derived Reference Sheet boundary

The builder expected live coverage is refreshed to the complete Tier distribution:

- Tier A: `9/9/9/9`
- Tier B: `6/6/6/6`
- Tier C: `3`

Existing derived PNGs are not modified, regenerated, or re-approved by D-070. Any visual regeneration remains a separate controlled update.

## Rescue publication note

The original Codex Cloud engineering result completed successfully but its task environment lacked a working real GitHub publication channel. The validated result was therefore reconstructed on a real GitHub rescue branch from the R071 canonical baseline and the already-published 21 binary identities.

This rescue does not claim byte-for-byte identity with the unavailable Codex squash tree; it restores the same governed D-070 outcome from current GitHub SSOT and the validated D-070 execution summary.

## Gate boundary

D-070 does **not** close P0.2.

- AO-06 / D-069 remains OPEN and mandatory.
- P0.2 remains ACTIVE.
- P0.3 remains QUEUED / DO NOT START EARLY.
- Product Owner review is required before merge.


## Formal PR Review｜2026-09-22

PR: `#11｜D-070: adopt and formally ingest 21 published Character Core binaries`

Final review status: `PASS / READY_FOR_PRODUCT_OWNER_MERGE_APPROVAL`

Review Patch corrected three issues before approval:

1. adoption rollback remained incomplete if the final PNG invariant check failed after commit; the invariant check now occurs before commit, preserving fail-closed rollback;
2. version reservation was initially too broad and changed normal supersession behavior; `--reserve-version` is now scoped to `--adopt-existing`, while normal ingest/supersession retains its prior version-safety behavior;
3. rescue Registry/Audit records initially used a reconstruction placeholder time and generic source reference; they now preserve the locked PO decision IDs / date-only approval precision and actual rescue-ingest/audit commit times.

Project Control current-state contradictions were also corrected; dated historical checkpoints remain unchanged.

Dynamic validation:

- GitHub Actions run: `35678375411`
- validated head: `d68ed8e0582a4316023f56ed89e06c034e45c40c`
- targeted controller tests: `15/15 PASS`
- full regression suite: `86/86 PASS`
- Registry / Audit / Relations: `83 / 120 / 44`
- D-070 assets / Audit / Relations: `21 / 42 / 0`
- 21 canonical PNG storage paths, byte sizes and SHA-256: `21/21 PASS`
- mandatory Character Core Single Current: `63/63 PASS`
- Black Lady LEFT/RIGHT rear mapping: `PASS / NOT SWAPPED`
- Derived Reference Sheet live-coverage contract: `PASS`
- Project Control JSON: `PASS`
- diff hygiene / forbidden PNG-audio-ZIP additions: `PASS`

The temporary validation workflow was removed after the successful run; final PR scope returns to the intended 13 files.

Merge method requirement for this rescue PR: `SQUASH`. The rescue branch contains intermediate review/reconstruction commits whose transient states must not become canonical main history.
