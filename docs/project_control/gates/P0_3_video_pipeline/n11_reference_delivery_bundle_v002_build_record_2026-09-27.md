# N11｜Reference Delivery Bundle V002｜Build Record

Status: `BUILT / 5 OF 5 EXACT VERIFICATION PASS / READY FOR WORK GENERATION`

Date: 2026-09-27

## Identity

- Bundle ID: `N11_REFERENCE_DELIVERY_BUNDLE_V002`
- Workflow: `.github/workflows/p03-n11-reference-delivery-bundle-v002.yml`
- Source commit: `e2b8568f20ba8ee4e044a725d56624e6cbd9b733`
- Workflow run ID: `36305485637`
- Job ID: `108581173489`
- Job conclusion: `SUCCESS`
- Artifact ID: `10927315457`
- Artifact name: `N11_REFERENCE_DELIVERY_BUNDLE_V002`
- Artifact digest: `sha256:a00cb07e9875afd5f63b1303c8722955d8cf25800aab4990946c5dc9f2df2b7e`
- Artifact size: `12637145` bytes
- Retention: 7 days / expires 2026-10-04
- Product Owner manual reference upload: `0`

## Exact reference verification

Workflow log result:

`PASS: 5/5 exact canonical reference binaries verified`

| Ref | SHA-256 | Bytes | Git blob |
|---|---|---:|---|
| AST_IMG_000028 / Neil FACE_FRONT | e75f0cba8f48d948069b978d86d46e96f7f5f0abd7a40341a5f92e006cb18939 | 2517908 | f3e74a06562d8751dd84c0d228b486769abdd254 |
| AST_IMG_000027 / Neil FACE_3Q_LEFT | 252f18eff4511a6b1255c751448a7fb667ad68ea2f9ebae49824ce3f453ea037 | 2529346 | 0d2638f02caa2697220f0073109fedac50e68246 |
| AST_IMG_000026 / Neil BODY_FRONT | f78ccfc252d2ed0cb31117ce1dae4c84893c5e52611a27fac161c8e6d014cf3d | 2605161 | 59939fba0a02b9364dbdc2d9ff8203fb57efa7f4 |
| AST_IMG_000052 / Castle Entrance Scene Master | d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961 | 2305753 | e4dafe096f5c5c8782257030a5a659aeec7808f9 |
| N01 / Opening end-state continuity | a96d52410c1645711545c80b7fe4e3eaa3e8f00b088ebaaea210bbdbec84557b | 2687303 | d55d2c218926c0b916c67d34979887315c351a1c |

## V002 exclusions

The bundle explicitly excludes:

- A03;
- N05;
- N09;
- all failed N11 candidates.

## Director lock carried into WORK_HANDOFF

- fresh rebuild; do not imitate any failed N11 candidate;
- tight medium close-up / upper chest-up;
- Neil's face is the absolute visual subject;
- only one narrow doorframe/door-edge may appear as a small foreground depth cue;
- Neil is already inside the threshold, one to two steps behind that plane, facing outward and waiting;
- no full doorway, symmetric double doors, floor, steps, threshold slab, waist, hands or lower torso;
- mouth closed, no speaking, greeting, turn, step or gesture;
- skin naturally pale; no corpse-blue / makeup-white / monsterization;
- cross should preferably not be visible; a clear centered cross is a failure;
- architecture remains subordinate;
- N01 proves continuity only and does not control composition.

## Next production step

Use this exact artifact in ChatGPT Work for one fresh `N11 Rebuild Candidate 01`.

Work must download the artifact automatically, revalidate all five PNGs against `delivery_manifest.json`, and only then generate the candidate.

No N12 work or N11 Story Shot registration before Product Owner review.
