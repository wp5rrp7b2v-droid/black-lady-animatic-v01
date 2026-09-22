# D-069 / AO-06 Stage 3 engineering checkpoint

Status: `REVIEW PATCH 02 VALIDATED / APPROVED A04 EVIDENCE MATERIALIZED / COSTUME_PROP ASSET BLOCKERS REMOVED BY PO-APPROVED BOUNDARY / REAL USE PENDING`

Date: `2026-09-18`

## Baseline

- Source commit: `0208a31f11885d9072b7f7d979d35e4c35953bfe`.
- Project Control: `R052` before this transaction.
- Regression: `68 tests / OK` after installing the locked `Pillow==11.3.0` dependency.
- Registry before: Asset `62`; Entity `11`; Relations `44`; Audit `76`; Shot/Prop/Costume Assets `0/0/0`.

## Implemented foundation

- Canonical executable `A04_SPEC_V001`, with no guessed photography.
- Reusable Character/Scene resolution plus strict Costume/Prop role resolution.
- Fail-closed Shot package with copied-binary SHA and byte-size verification.
- Append-only use-record validation and Shot/Asset reverse queries.
- Isolated `USES_REFERENCE` forward/reverse query and atomic relation+Audit transaction.
- Stable `COSTUME_NEIL_DEFAULT` and `PROP_NEIL_CROSS` Entities plus paired `ENTITY_CREATED` events. These records do not claim that visual Assets exist.

## Real discovery result

The following required searches were executed against the available repository:

- current-tree filename and content search for `A04`, `A04_REBOOT`, `A04_REBOOT_approved`, `A04_SHOT_MASTER`, Neil, costume, cross, and handkerchief;
- `git log --all --name-only` searches;
- `git rev-list --objects --all` searches;
- inspection of relevant historical names and schema/migration documentation.

Only naming examples, design/history text, and Neil Character assets were found. No exact approved A04 binary or provenance-bearing manifest/handoff that identifies such a binary was found. No dedicated approved Costume or Cross reference was found. Visual content inside Character references is not independent formal authority and was not cropped or formalized.

Therefore:

- formal A04 Shot Asset created: **NO**;
- formal Costume Asset created: **NO**;
- formal Prop Asset created: **NO**;
- live historical/current `USES_REFERENCE` written: **NO**;
- diagnostic package status: `BLOCKED`;
- `generation_allowed = false`.

## Current resolver truth

Resolved:

- `CHAR_NING_QIUSHUI → AST_IMG_000060`;
- `CHAR_NEIL → AST_IMG_000059`;
- `SCENE_CASTLE_ENTRANCE / DAY_DOOR_OPEN → AST_IMG_000052`.

Gaps:

- `COSTUME_NEIL_DEFAULT → REFERENCE_GAP / NO_ELIGIBLE_FORMAL_ASSET`;
- `PROP_NEIL_CROSS → REFERENCE_GAP / NO_ELIGIBLE_FORMAL_ASSET`;
- `A04 → SHOT_EVIDENCE_GAP / APPROVED_A04_SOURCE_NOT_MATERIALIZED`.

## Next gate

Resume the same D-069 only after the Product Owner supplies the byte-exact approved A04 source with reliable provenance and suitable dedicated Costume/Prop evidence or explicit visual-candidate approval. Do not allocate D-070 and do not start Work real validation while the package is blocked.

## Review Patch 01

Status: `D-069 REVIEW PATCH 01 COMPLETE / ENGINEERING FOUNDATION CLEAN / BLOCKED_ON_APPROVED_A04_BINARY / BLOCKED_ON_COSTUME_PROP_EVIDENCE`

Remote publication context supplied by Product Owner:

- PR: `#10` (`OPEN / DO NOT MERGE`);
- remote branch: `codex/a04`;
- remote head at Review Patch 01 start: `351a41b9452eafc01e724fd6f36f9edb6793c627`.

Corrections:

- Project Control nested AO-06/checkpoint fields now reflect the D-069 Stage 3 evidence-blocked checkpoint and resume the same D-069;
- a Character Reference Sheet with `resolver_usage = NEVER` is ineligible even when CURRENT, APPROVED, FRESH, present, and SHA-valid;
- isolated `USES_REFERENCE` rows include the Schema V0.3 `created_by_event_id`, equal to the paired `RELATION_CREATED.event_id` and embedded consistently in that event;
- A04 evidence selection additionally requires `variant = DEFAULT` and `state = DEFAULT`; wrong variant/state and `resolver_usage = NEVER` remain `SHOT_EVIDENCE_GAP`.

This review patch changes no live Registry counts and writes no live `USES_REFERENCE` relation.


## Review Patch 02 — 2026-09-22

Status: `ENGINEERING PATCH VALIDATED / NOT YET MERGED / AO-06 NOT COMPLETE`

Product Owner approved the following evidence-boundary correction on 2026-09-22:

- the exact approved A04 binary is now materialized at
  `staging/d069_a04_intake/A04_REBOOT_approved_v001.png`;
- byte size = `2486659`;
- SHA-256 = `8111a2d80bb68efe99bc723d197a580b5bfed3d64a1ffeb3848db9260bb50398`;
- A04 Shot evidence is authority for composition / blocking / visible Shot facts only;
- Neil black butler attire and visible chest cross are handled as
  `CHAR_NEIL / DEFAULT` canonical appearance-continuity constraints for A04;
- `COSTUME_NEIL_DEFAULT` and `PROP_NEIL_CROSS` no longer block this Shot as required standalone formal visual Assets;
- `WHITE_POCKET_HANDKERCHIEF_VISIBLE` is removed from A04 required continuity facts because the approved Shot does not provide sufficient evidence for that requirement;
- existing Costume/Prop Entity records are retained as historical/model records but are not A04 Resolver blockers;
- no historical `USES_REFERENCE` edge is reconstructed for the approved legacy A04 image.

Executable behavior after this patch:

- Character resolution remains:
  - `CHAR_NING_QIUSHUI → AST_IMG_000060`;
  - `CHAR_NEIL → AST_IMG_000059`;
- Scene resolution remains:
  - `SCENE_CASTLE_ENTRANCE / DAY_DOOR_OPEN → AST_IMG_000052`;
- exact A04 approved evidence is integrity-checked directly against its locked path, byte size, and SHA;
- Reference Package keeps formal resolved Assets separate from approved Shot evidence;
- any missing/corrupt A04 evidence still fail-closes generation;
- any Character/Scene gap still fail-closes generation.

Validation:

- targeted D-069 tests: `13 / 13 PASS`;
- full regression: `86 / 86 PASS`;
- exact A04 binary identity check: `PASS`;
- validation workflow run: `35703125845 / SUCCESS`.

Remaining AO-06 work:

`Shot Spec → Resolver → traceable Reference Package → Actual Production Use → immutable use record → reverse audit`

Therefore this patch removes the obsolete A04 binary and standalone Costume/Prop blockers, but does **not** mark AO-06 complete and does **not** authorize P0.3.
