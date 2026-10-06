# Black Lady Production Console｜V1.1 Engineering

Branch: `feature/production-console-v1-1`

This directory is the source-control home for the Production Console engineering implementation.

## Current engineering state

- Parent subproject: `docs/project_control/subprojects/production_console/`
- V1.1 Design V0.1: Product Owner approved
- V1.1 Implementation Spec V0.1: baseline ready
- Current formal Story Shot workflow: unchanged
- Production Process Change: not authorized
- V1.1 E2E qualification: required before any production-adoption decision

## Source baseline

The implementation starts from the verified V1.0 Fixed Install Foundation source snapshot dated 2026-10-03.

The V1.0 source tree was independently hash-checked against the retained manifest before V1.1 implementation preparation.

See `BASELINE_MANIFEST.json`.

## Security boundary

Never commit:

- `BlackLadyLocalConsolePrivate/`
- `credentials.json`
- `token.json`
- private OAuth material
- live Drive account bindings
- session files containing secrets

Local private state remains outside this source tree.

## Engineering rule

Qualification code may use dedicated test branches and test paths only.

Merely version-controlling this Console does not change the parent project's active Story Shot SOP.
