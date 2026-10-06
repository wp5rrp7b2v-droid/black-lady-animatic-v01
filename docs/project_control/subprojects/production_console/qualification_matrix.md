# Production Console｜Qualification Matrix

Status: **ACTIVE**

## Gate matrix

| Gate | Requirement | Current status | Scale effect |
|---|---|---|---|
| Q0 | V1.0 Fixed Install Foundation retained and recoverable | PASS | Allows V1.1 design |
| Q1 | Phase A / B / C1 / C2 / D / E qualification evidence | PASS | Allows V1.1 design |
| Q2 | V1.1 Unified Workflow Design V0.1 Product Owner approval | PASS / 2026-10-06 | Allows implementation |
| Q3 | V1.1 implementation complete without changing current formal Story Shot SOP | CORE + LOCAL REGRESSION PASS / FINAL PRE-E2E UX RETEST PENDING | Blocks E2E until UX retest PASS |
| Q4 | V1.1 End-to-End qualification | NOT STARTED / REQUIRED | Blocks production adoption |
| Q5 | Separate Process Change / Production Adoption decision | NOT AUTHORIZED | Production scale locked |

## Q3 acceptance

Implementation must:
- preserve current formal Story Shot SOP;
- preserve existing Story Shot Index and canonical records;
- keep private OAuth/secrets outside GitHub;
- maintain explicit Product Owner gates;
- fail closed on missing identity or preflight evidence;
- preserve Candidate identity and recovery states;
- keep Phase E test archive separate from live production workspace.

## Q4 End-to-End qualification

Run one controlled End-to-End qualification after Q3.

Required path:

`DESIGN → PREFLIGHT → GENERATE → REVIEW → PUBLISH → REGISTER → LOCK → CLOSEOUT`

PASS requires:
- no identity drift;
- exact binary identity remains stable;
- Product Owner approval binds the same Candidate;
- publication/registration/lock bindings remain consistent;
- registration-only recovery works;
- reopening reconstructs the same state from authoritative evidence;
- no unauthorized modification of formal Story Shot SOP / Registry / Project Control.

FAIL on:
- SHA mismatch;
- identity mismatch;
- publication must be repeated merely to recover registration;
- local-only state claims cannot be reconstructed;
- test data contaminates formal Story Shot records;
- any formal production rule changes occur without separate approval.

## Production adoption gate

Even after Q4 PASS, Production Console does not automatically replace the current process.

A separate Product Owner-approved Process Change / Production Adoption phase is mandatory before:
- changing Story Shot canonical storage authority;
- changing publication or registration SOP;
- changing Project Control closeout behavior;
- scaling the Console to routine formal production.
