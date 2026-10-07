# Black Lady Animatic v01

Canonical repository for the `诡舍·黑衣夫人` production project.

## Current production layout

- `production/` — canonical approved assets, Story Shots, registries, bundle specs, and approved video outputs.
- `docs/project_control/` — project state, governance, approvals, verification records, and closeout evidence.
- `scripts/` — currently retained production / registry / verification tooling.
- `.github/workflows/` — active GitHub Actions workflows only.
- `staging/` — controlled temporary inputs that are still required by an active workflow or regression fixture.
- `tests/` — retained regression tests for the production toolchain.

## Story Shot production baseline

Formal Story Shot work follows:

`Director Design → Scene Reference → Bundle → Work generation → Product Owner approval → Exact Binary Verification → Canonical Publication → Story Shot Registration → Registration Verification → Project Control Closeout`

GitHub `main` remains the canonical repository baseline.

## Historical experiments

Completed proof-of-concept implementations and retired one-off workflows are kept under:

`docs/project_control/archive/`

They are historical evidence only and are not active production entry points.

## Repository cleanup note

The original Base64 cloud animatic smoke-test transport was retired on 2026-10-07. Its workflow, payload fragments, and render helper are no longer part of the repository working tree. Historical Git commits preserve that experiment if reconstruction is ever required.
