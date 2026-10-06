# Production Console V1.1｜Implementation Spec V0.1

Status: **IMPLEMENTATION PREPARATION / BASELINE READY**  
Date: **2026-10-06**  
Parent design: `V1.1 Unified Workflow Design V0.1 / PRODUCT OWNER APPROVED`

## 1. Implementation objective

Refactor the validated V1.0 qualification code into one reusable Console runtime without changing the parent project's current formal Story Shot production workflow.

Implementation target:

`DESIGN → PREFLIGHT → GENERATE → REVIEW → PUBLISH → REGISTER → LOCK → CLOSEOUT`

This state machine is the Console orchestration model under qualification.

## 2. V1.0 source findings

The V1.0 Fixed Install source is technically reusable but phase-hardcoded.

### Reusable without redesign

- macOS proxy discovery and environment bridging;
- Google OAuth + Picker flow;
- `AuthorizedSession(requests)` transport;
- Drive folder binding;
- Drive upload;
- Drive readback;
- SHA-256 / byte-size / image-dimension verification;
- GitHub CLI JSON transport;
- GitHub branch / file readback;
- deterministic JSON payload generation;
- exact remote readback comparison;
- idempotent create-or-refuse behavior;
- registration-only recovery concept;
- lock binding concept;
- private state directory separation;
- drag-and-drop handling.

### Phase-hardcoded areas that must be generalized

- `TEST_SHOT_UI_001`;
- `CANDIDATE_01 / CANDIDATE_02 / TEST_CANDIDATE_01`;
- Phase C2 state schema;
- Phase D test branch/path/schema;
- Phase E branch/path/schema;
- Phase E fixed Bundle metadata;
- Phase E-only status progression;
- qualification-only UI copy and four-step Phase E layout.

## 3. Core refactor

### 3.1 Unified Shot Session

Replace phase-specific runtime ownership with a generic local session document:

`PRIVATE_DIR / sessions/<shot_session_id>.json`

Minimum fields:

- session_id
- shot_id
- mode = QUALIFICATION | CONTROLLED_PILOT | future modes
- current_stage
- current_status
- design_summary
- bundle
- preflight
- candidate
- approval
- publication
- registration
- lock
- closeout
- history
- created_at
- updated_at

Local session state is operational cache only and must never override external authoritative evidence.

### 3.2 Candidate identity

Candidate identity is immutable after exact verification:

- shot_id
- candidate_id
- drive_file_id
- sha256
- byte_size
- width
- height
- mime_type

Product Owner approval binds the same identity.

Rejected Candidates remain immutable historical attempts. New output = new Candidate ID.

### 3.3 Stage transitions

Allowed minimum transitions:

- DESIGN → DESIGN_APPROVED
- DESIGN_APPROVED → PREFLIGHT_PASS
- PREFLIGHT_PASS → AWAITING_CANDIDATE
- AWAITING_CANDIDATE → CANDIDATE_VERIFIED_PENDING_PO
- CANDIDATE_VERIFIED_PENDING_PO → PO_APPROVED_PENDING_PUBLICATION
- CANDIDATE_VERIFIED_PENDING_PO → REJECTED
- PO_APPROVED_PENDING_PUBLICATION → PUBLISHED_NOT_REGISTERED
- PUBLISHED_NOT_REGISTERED → REGISTERED_PENDING_LOCK
- REGISTERED_PENDING_LOCK → LOCKED_PENDING_CLOSEOUT
- LOCKED_PENDING_CLOSEOUT → CLOSED

Invalid transitions fail closed.

## 4. Service-layer extraction

Refactor `server.py` into reusable internal layers while preserving the proven transport code.

Suggested modules:

- `app.py` — Flask routes and application boot
- `config.py` — safe paths / mode / repo settings
- `state_store.py` — session state and history
- `drive_service.py` — OAuth, Picker, upload, readback, exact binary
- `github_service.py` — branch/file readback and safe write helpers
- `workflow.py` — state machine and transition validation
- `qualification.py` — Phase E archive + V1.1 E2E qualification logic
- `templates/index.html` — V1.1 workspace
- `templates/archive.html` — Phase E qualification archive

A single-file implementation is acceptable temporarily if behavior is first separated into explicit helper sections, but the release target should not retain C2/D/E as independent production state engines.

## 5. API target

Qualification-safe V1.1 endpoints:

- `GET /api/v1/session`
- `POST /api/v1/session/start`
- `POST /api/v1/design/approve`
- `POST /api/v1/preflight`
- `POST /api/v1/candidate/upload`
- `GET /api/v1/candidate/media`
- `POST /api/v1/candidate/review`
- `POST /api/v1/publish`
- `POST /api/v1/register`
- `POST /api/v1/lock`
- `POST /api/v1/closeout`
- `GET /api/v1/receipt`

Phase E endpoints may remain temporarily under `/api/e/*` as a read-only / regression archive until V1.1 qualification is complete.

## 6. PREFLIGHT V1.1

V1.1 preflight is a real gate, not a decorative UI state.

Minimum checks:

- Shot Session identity present;
- Bundle ID present;
- Run ID present;
- Artifact ID present;
- Artifact digest present;
- delivery manifest information present;
- reference count declared;
- references_exact = true;
- generation_allowed = true;
- Drive connected;
- Drive target folder bound;
- GitHub connectivity available for the qualification environment;
- no locked Candidate already bound to the session;
- no contradictory external qualification record.

Any failure disables GENERATE / Candidate intake progression.

## 7. UI V1.1

### Header
- Subproject / release
- current Shot / Session
- mode
- current state
- production-process boundary badge

### Workflow bar
Eight visible stages:

`DESIGN / PREFLIGHT / GENERATE / REVIEW / PUBLISH / REGISTER / LOCK / CLOSEOUT`

Only the active stage is expanded.

### Active Stage Panel
Shows:
- required inputs;
- current checks;
- allowed action;
- blocked reason;
- Product Owner action when required.

### Immutable Identity Card
Always visible after Candidate upload:
- Shot ID
- Candidate ID
- Drive File ID
- SHA-256
- bytes
- dimensions
- approval status

### Evidence & Recovery
Shows:
- latest readback;
- external bindings;
- retry-safe action;
- history / receipt export.

### Archive
Phase E `TEST_SHOT_UI_001` is moved to a separate Qualification Archive view and no longer acts as the main workspace.

## 8. Safety boundary during implementation

V1.1 implementation and local testing must not:

- modify the current formal Story Shot SOP;
- write formal Story Shot records to main;
- update Story Shot Index;
- publish formal Story Shot binaries;
- update parent Project Control as if a real Story Shot had completed;
- overwrite existing Phase E evidence;
- commit `BlackLadyLocalConsolePrivate`;
- commit OAuth credentials or tokens.

Qualification writes must remain isolated to a dedicated test branch/path until an explicitly authorized controlled pilot.

## 9. Source-control plan

Implementation code should no longer exist only as an untracked local folder.

Create a dedicated engineering branch from current `main`:

`feature/production-console-v1-1`

Sanitized application source may be version-controlled under:

`tools/production_console/`

Never commit:

- `BlackLadyLocalConsolePrivate/`
- `credentials.json`
- `token.json`
- local Drive bindings containing private account data
- generated session state containing private tokens/secrets

The parent production workflow remains unchanged merely because Console source is version-controlled.

## 10. Regression requirements

Before V1.1 E2E qualification, implementation must preserve prior validated capabilities:

- OAuth / Drive Picker works;
- drag-and-drop works;
- Drive exact-binary readback works;
- PO approval binding works;
- GitHub test publication readback works;
- publication idempotency works;
- registration failure can remain `PUBLISHED_NOT_REGISTERED`;
- Registration Retry does not rewrite publication;
- lock verifies the same identity;
- main / formal Story Shot paths remain unchanged in qualification mode.

## 11. Engineering sequence

1. Create implementation branch.
2. Import sanitized V1.0 source as engineering baseline.
3. Preserve V1.0 archive behavior.
4. Introduce generic session/state model.
5. Generalize Candidate identity and Drive intake.
6. Add PREFLIGHT engine.
7. Generalize qualification publication / registration / lock adapters.
8. Replace Phase E main UI with V1.1 workspace.
9. Add archive view.
10. Run local regression.
11. Package V1.1 qualification build.
12. Run mandatory End-to-End qualification.
13. Only after PASS: Product Owner decides whether to start a separate Process Change / Production Adoption program.

## 12. Current gate

Implementation may proceed on the engineering branch.

Formal production-process change remains:

`NOT STARTED / NOT AUTHORIZED`
