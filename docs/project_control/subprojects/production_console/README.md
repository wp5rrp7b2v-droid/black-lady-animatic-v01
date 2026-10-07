# Black Lady Production Console｜Subproject Control

Status: **ACTIVE / Q3 COMPLETE / Q4 V1.1 END-TO-END QUALIFICATION ACTIVE / Q5 PRODUCTION ADOPTION LOCKED**

Parent project: 《诡舍·黑衣夫人》  
Canonical repo: `wp5rrp7b2v-droid/black-lady-animatic-v01`  
Subproject ID: `BLACK_LADY_PRODUCTION_CONSOLE`  
Project Control root: `docs/project_control/subprojects/production_console/`

## Purpose

Build and qualify a local Production Console that can provide one operational UI for the already-established Black Lady production capabilities: Bundle verification, candidate intake, Google Drive media handling, Product Owner review, exact-binary identity checks, publication/registration test orchestration, recovery, lock and closeout visibility.

The Console is a **tooling / workflow qualification subproject**. It is not a replacement source of truth.

## Authority boundary

Current formal Story Shot production rules remain unchanged.

The active production SOP continues to be:

`Director Design → Reference Delivery Bundle → Work Generation → Product Owner Approval → Original PNG Upload → Binary Verification → Exact-Blob Canonical Rename → Story Shot Index Registration → Registration Verification → Project Control Closeout`

V1.1 design, implementation and qualification work **must not silently modify this SOP**, Story Shot canonical authority, Registry rules, or Project Control closeout rules.

A production-process change may be considered only after:

1. V1.1 implementation is complete;
2. V1.1 End-to-End qualification passes;
3. Product Owner separately authorizes a Process Change / Production Adoption phase.

## Architecture boundary

- GitHub: parent-project canonical Project Control and current formal production authority.
- Google Drive: Console media transport/storage capability under qualification.
- Local Mac: UI, cache, temporary working state and private OAuth material.
- Chat: design, review, decisions and Project Control orchestration.
- Work: formal Story Shot image generation.
- Codex / engineering tooling: Console code and explicit engineering work only.

The Console must never become a third independent truth source.

## Current release line

- V1.0 Fixed Install Foundation: qualification foundation complete.
- Phase A / B / C1 / C2 / D / E: PASS.
- V1.1 Unified Production Workflow Design V0.1: PRODUCT OWNER APPROVED 2026-10-06.
- V1.1 Core implementation + local regression: PASS.
- Auto Metadata Resolve: PASS against exact Project Control revision.
- Operator View one-page layout: VISUAL PASS.
- Q3 Pre-E2E UX qualification: PASS / COMPLETE 2026-10-07.
- V1.1 End-to-End Qualification (Q4): ACTIVE / Session `V11_Q4_E2E_001`.
- Production Process Change: NOT STARTED / NOT AUTHORIZED.
- Production Scale: LOCKED.

## Current target state machine

`DESIGN → PREFLIGHT → GENERATE → REVIEW → PUBLISH → REGISTER → LOCK → CLOSEOUT`

This is the **Console orchestration model under qualification**, not a declaration that the parent project's production SOP has changed.

## Project-control files

- `project_state.json` — current subproject state.
- `design/v1_1_unified_workflow_design_v0_1.md` — approved V1.1 design baseline.
- `qualification_matrix.md` — qualification gates and scale gate.
- `logs/decision_log.md` — Product Owner decisions and major boundary changes.

## Recovery rule

When Chat context is unavailable, restore state from this directory plus the parent Project Control. Local private credentials are never committed to GitHub.


## Next-session resume point

2026-10-06 working session is closed, but the subproject remains **ACTIVE**.

Next session begins with:

`LOCAL SYNC VERIFICATION → OPERATOR VIEW FRESHNESS RETEST → STALE SESSION AUTO RECOVERY RETEST`

If both remaining Q3 checks pass:

`Q3 COMPLETE → FORMAL V1.1 END-TO-END QUALIFICATION (Q4)`

Daily closeout record:
`logs/eod_closeout_2026-10-06.md`

Local sync is required at next session start because both parent `main` and `feature/production-console-v1-1` advanced during the day. Preserve local-only/private folders and credentials; never commit `BlackLadyLocalConsolePrivate/`.


## Q4 active run｜2026-10-07

Product Owner authorized the formal V1.1 End-to-End qualification.

Controlled test identity:

- Session: `V11_Q4_E2E_001`
- Shot: `TEST_UI_V11_Q4_001`
- Bundle: `V11_Q4_E2E_BUNDLE_001`
- Qualification branch: `test/local-console-v1-1-e2e-v001`

Required path:

`DESIGN → PREFLIGHT → GENERATE → REVIEW → PUBLISH → REGISTER → LOCK → CLOSEOUT`

The run includes deliberate local-session-loss recovery after Publication and again after Closeout. Formal Story Shot production remains unchanged. Production Adoption / Q5 remains locked pending a separate Product Owner decision.

Start record: `logs/q4_e2e_qualification_start_2026-10-07.md`
