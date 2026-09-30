# N21 Reference Delivery Bundle V001｜Build Record

Date: 2026-09-30

Status: `PASS / GENERATION_ALLOWED=TRUE`

## Bundle identity

- Bundle ID: `N21_REFERENCE_DELIVERY_BUNDLE_V001`
- Target: `N21 Candidate 01`
- Spec: `production/bundle_specs/N21_REFERENCE_DELIVERY_BUNDLE_V001.json`
- Spec commit: `a3058fe38b2fca462094fbe4df38b41e9ecf5b7b`

## GitHub Actions

- Workflow: `Story Shot Reference Bundle Builder`
- Workflow file: `.github/workflows/story-shot-reference-bundle-builder.yml`
- Run ID: `36669436051`
- Job ID: `109741045220`
- Conclusion: `SUCCESS`

Builder output:

`PASS: 6/6 exact canonical reference binaries verified`

`GENERATION_ALLOWED=TRUE`

## Artifact

- Artifact name: `N21_REFERENCE_DELIVERY_BUNDLE_V001`
- Artifact ID: `11076819801`
- ZIP size: `6762818 bytes`
- Artifact digest: `sha256:a141ad98c50538c470901ef40ff7a9baa9e0ae8586703c6e82b617ad346308c1`
- Expires: `2026-10-07T04:34:26Z`

## Formal references

1. `AST_IMG_000052` — Castle Entrance Scene Master
2. `N20` — approved immediate Story Shot continuity
3. `AST_IMG_000061` — Su Xiaoxiao Character Reference Sheet
4. `AST_IMG_000058` — Liao Jian Character Reference Sheet
5. `AST_IMG_000062` — Wen Qingya Character Reference Sheet
6. `AST_IMG_000056` — Guang Yong Character Reference Sheet

## Independent Artifact verification

Chat independently downloaded the Artifact and verified the exact ZIP and all six enclosed PNG binaries.

ZIP:

- downloaded ZIP SHA-256: `a141ad98c50538c470901ef40ff7a9baa9e0ae8586703c6e82b617ad346308c1`
- GitHub Artifact digest: `sha256:a141ad98c50538c470901ef40ff7a9baa9e0ae8586703c6e82b617ad346308c1`
- result: `MATCH`

Reference verification:

| Reference | Bytes | SHA-256 | Git blob | PNG signature | Result |
|---|---:|---|---|---|---|
| AST_IMG_000052 | 2305753 | d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961 | e4dafe096f5c5c8782257030a5a659aeec7808f9 | PASS | PASS |
| N20 | 2022630 | a61ab1310e86938b2a416516138981aafaf421add44c1a9d5a80d0ff9ec59a9e | 58e145a51c3f993827e5e47964ad0e7f9dd9f0aa | PASS | PASS |
| AST_IMG_000061 | 700794 | e869d118e22e50cfe6e6280632da4534e660dc74ec96cf3871099b87cf42701a | 2b584d4172484216478319025440b16ba7c2859a | PASS | PASS |
| AST_IMG_000058 | 650562 | 3f2f01fea63401a3726abdf5053e75361d5d43091830ce8e1636883bd1cd6817 | f8b600e49c0bd40177c723d9c0abd474678f41c2 | PASS | PASS |
| AST_IMG_000062 | 641800 | 09551f02ad9cd4d3ae8e4483d017c230877165c4b88346ff9762527246569f0c | e391622643034485dc4e9a862ba29cde72cdeefd | PASS | PASS |
| AST_IMG_000056 | 475761 | 2a98e74ddba60a259758643b56ffddafd5a7cb30de040880f991fb47216b45fb | e37ad60d933c3fdc434768bb449019146eb9333e | PASS | PASS |

Independent result:

`6/6 PASS`

Manifest:

- bundle_id: `N21_REFERENCE_DELIVERY_BUNDLE_V001`
- reference_count: `6`
- generation_allowed: `true`
- overall_result: `PASS`

## Production disposition

`N21 Candidate 01 Work generation is now authorized.`

Work must automatically download the verified Artifact and revalidate all six inputs before generation.

Manual Product Owner reference upload:

`0`

Do not start N22.
