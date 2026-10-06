# Production Console V1.1｜Unified Workflow Design V0.1

Status: **PRODUCT OWNER APPROVED**  
Approval date: **2026-10-06**  
Implementation status: **NOT STARTED**

## 1. Design goal

Unify the already validated Console capabilities into one coherent operating surface:

`DESIGN → PREFLIGHT → GENERATE → REVIEW → PUBLISH → REGISTER → LOCK → CLOSEOUT`

The objective is to test whether the Console can safely orchestrate and expose the complete production lifecycle with immutable identity, explicit Product Owner gates and recoverable failure states.

## 2. Critical scope boundary

This document is a **Console design / qualification baseline only**.

It does **not** change the current formal Story Shot production SOP, current canonical Story Shot binary authority, Story Shot Index rules, Registry rules or Project Control closeout rules.

During V1.1 design, implementation and End-to-End testing:

- current formal Story Shot workflow remains unchanged;
- existing approved Story Shots remain untouched;
- test metadata must not be represented as formal Story Shot registration;
- no production-process migration is implied by successful UI testing.

Only after V1.1 End-to-End qualification PASS may a separate **Process Change / Production Adoption** phase be proposed. That later phase requires separate Product Owner authorization.

## 3. State model

### DESIGN
Chat owns Director Design. Console may display the approved design summary but does not originate creative authority.

Exit: `DESIGN_APPROVED`.

### PREFLIGHT
Console verifies the required Bundle and execution prerequisites, including available bundle identity, artifact/run information, manifest, exact references and required services.

Fail closed on missing or inconsistent prerequisites.

Exit: `PREFLIGHT_PASS`.

### GENERATE
Console prepares or exposes the Work handoff for exactly the authorized Candidate. Story Shot image generation remains Work responsibility.

Exit: `AWAITING_CANDIDATE`.

### REVIEW
Candidate is ingested into the Console qualification path. Exact identity is established and bound to Product Owner review.

Immutable identity target:

`Shot ID + Candidate ID + Drive File ID + SHA256 + byte size + dimensions`

Possible exits:
- `PO_APPROVED_PENDING_PUBLICATION`
- `REJECTED`

Rejected Candidates are not overwritten; a new Candidate receives a new Candidate ID.

### PUBLISH
Qualification UI performs or simulates only the publication operation explicitly authorized for the current test environment.

The current parent-project formal Story Shot publication contract remains authoritative until a future separately authorized process change.

Exit: `PUBLISHED_NOT_REGISTERED`.

### REGISTER
Registration must bind the same approved identity and publication evidence.

If registration fails after valid publication, recovery is **Retry Registration Only**.

Exit: `REGISTERED_PENDING_LOCK`.

### LOCK
Re-verify Candidate identity, publication identity and registration binding before lock.

Exit: `LOCKED_PENDING_CLOSEOUT`.

### CLOSEOUT
Closeout is allowed only after LOCK.

For qualification tests, closeout must remain isolated from formal Story Shot Project Control unless the Product Owner explicitly authorizes a controlled real-production pilot under the then-current production rules.

Exit: `CLOSED`.

## 4. UI layout baseline

- Top: Shot Identity / task identity / mode / current state.
- Flow bar: the eight workflow states.
- Center: one Active Stage Panel only.
- Right: Immutable Identity Card.
- Bottom: Evidence & Recovery.
- Historical Phase E Qualification Archive remains separate from the Production workspace.

## 5. Product Owner gates

Manual gates:
- Design Approval
- Candidate upload/ingest trigger
- Candidate Approve / Reject
- Publish
- Register
- Lock
- Closeout

Automatic checks:
- Preflight validation
- Exact-binary verification
- identity/binding verification
- readback/recovery verification

No one-click production-wide write is authorized during the controlled qualification stage.

## 6. Prohibited behavior

- Generate when PREFLIGHT fails.
- Approve when exact identity verification fails.
- Use filename alone as identity.
- Overwrite a reviewed Candidate binary.
- Re-run publication merely because registration failed.
- Replace a locked binary.
- Treat local JSON as canonical production truth.
- Promote TEST_SHOT metadata into formal Story Shot records.
- Change current formal production SOP merely because V1.1 design or implementation exists.

## 7. Qualification requirement

V1.1 is not production-ready after implementation alone.

A complete End-to-End qualification must be executed after implementation. PASS requires, at minimum:

- stable identity through every stage;
- exact-binary checks succeed;
- Product Owner approval binds the same Candidate;
- publication and registration bindings remain consistent;
- registration-only recovery works;
- lock proves the same identity;
- reopening the Console reconstructs the same state from authoritative evidence;
- no unauthorized formal production or Project Control writes occur.

Any identity drift, premature canonical write, unrecoverable state conflict or scope leakage is FAIL.

## 8. Scale gate

`V1.0 Foundation PASS → V1.1 Design APPROVED → V1.1 Implementation → V1.1 E2E Qualification → [separate PO decision] Process Change / Production Adoption`

Production scale remains locked until the later adoption decision.
