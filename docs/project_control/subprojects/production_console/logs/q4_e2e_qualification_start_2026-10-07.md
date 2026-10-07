# Production Console V1.1｜Q4 End-to-End Qualification Start

Date: 2026-10-07  
Status: **ACTIVE / AUTHORIZED BY PRODUCT OWNER**

## Scope

Controlled qualification only. This run does **not** change or replace the formal Story Shot production SOP.

Required state path:

`DESIGN → PREFLIGHT → GENERATE → REVIEW → PUBLISH → REGISTER → LOCK → CLOSEOUT`

Controlled test identity:

- Session ID: `V11_Q4_E2E_001`
- Shot ID: `TEST_UI_V11_Q4_001`
- Bundle ID: `V11_Q4_E2E_BUNDLE_001`
- Qualification branch: `test/local-console-v1-1-e2e-v001`
- Qualification root: `staging/local_console_v1_1/V11_Q4_E2E_001/`

## Start safety baseline

- main HEAD at authorization: `c05945501a3c0b93f018bbc56e658b30936c8a17`
- engineering branch HEAD: `56cd1d5c6e9ec2885daf396a901ef5a917e3108e`
- qualification branch HEAD: `611992e5f3d4767d2f9813afde8e4d751f24bbe1`
- parent Project Control revision: `R337`
- parent Project Control blob: `6895891002447cabdfba7f3771a77696c36845eb`
- formal Story Shot SOP blob: `b1751704fe98c866d79633fb7c2c84c9a70f8e9e`
- Story Shot Index blob: `aca511a8db47bff458682de7db59101195e62206`
- Story Shot Index record count: `32`
- N26 canonical PNG Git blob: `a5ce429689a99437773385e25b9813745e380f74`

At start, all Q4 qualification record paths are absent:
- publication: ABSENT
- registration: ABSENT
- lock: ABSENT
- closeout: ABSENT

## Qualification design

Q4 must prove, in one controlled session:

1. Design Package qualification gate can start from a fresh test workspace.
2. PREFLIGHT passes only with complete qualification metadata and safety boundaries.
3. Exactly one Candidate PNG is accepted and its immutable identity is established.
4. Product Owner approval binds the same Candidate identity.
5. Publication creates qualification-only evidence.
6. After Publication, local Session loss is intentionally simulated; automatic External Recovery must restore `PUBLISHED_NOT_REGISTERED` without publication rerun.
7. Registration must proceed by registration-only continuation.
8. Lock must bind the same Candidate + Publication + Registration identities.
9. Closeout must bind the same locked identity.
10. After Closeout, local Session loss is simulated again; reopening must reconstruct `CLOSED` from authoritative GitHub + Drive evidence.
11. Formal parent Story Shot SOP, Story Shot Index, N26 canonical binary, and parent Project Control must remain unchanged by the qualification run.

## PASS / FAIL boundary

PASS requires all Q4 matrix conditions and exact external verification.

FAIL if:
- any Candidate SHA/identity drifts;
- publication must be repeated to recover registration;
- reopening cannot reconstruct authoritative state;
- qualification data writes into formal Story Shot records;
- any formal production rule changes occur without a separate Product Owner decision.

Production Adoption remains **LOCKED** after Q4 until a separate Q5 decision.
