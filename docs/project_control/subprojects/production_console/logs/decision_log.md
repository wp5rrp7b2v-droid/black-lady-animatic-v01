# Production Console｜Decision Log

## PC-D001｜2026-10-06｜Register as Black Lady subproject

**Decision:** Production Console is registered as a formal subproject of 《诡舍·黑衣夫人》 in GitHub Project Control.

**Reason:** Chat-only retention is insufficient for durable project continuity. The subproject needs canonical design, state, qualification and decision records.

**Boundary:** Subproject registration does not change the current formal Story Shot production workflow.

## PC-D002｜2026-10-06｜V1.1 Unified Workflow Design V0.1 approved

**Decision:** Product Owner approved V1.1 Unified Workflow Design V0.1.

**State machine:**

`DESIGN → PREFLIGHT → GENERATE → REVIEW → PUBLISH → REGISTER → LOCK → CLOSEOUT`

**Boundary:** This is a UI/workflow qualification design. It is not a production SOP change.

## PC-D003｜2026-10-06｜End-to-End qualification mandatory

**Decision:** V1.1 implementation completion alone is insufficient.

A full End-to-End qualification must PASS before Production Adoption can even be considered.

## PC-D004｜2026-10-06｜Process change deferred

**Decision:** Current formal Story Shot process remains unchanged during UI design, implementation and testing.

Any future change to production storage, publication, registration or closeout is a separate Process Change / Production Adoption program requiring explicit Product Owner approval after qualification.

## PC-D005｜2026-10-06｜V1.1 Core Refactor continuation approved

**Decision:** Product Owner approved continuing V1.1 implementation from the established engineering branch.

**Authorized engineering scope:**
- generic Shot Session;
- workflow state machine;
- immutable Candidate identity;
- qualification-only GitHub branch/path adapters;
- unified V1.1 UI implementation;
- regression testing.

**Not authorized:** any change to the current formal Story Shot SOP, canonical Story Shot records, Story Shot Index, or production adoption.
