# P0.3 Progress Closeout｜2026-09-23

Status: `P0.3 IN PROGRESS / REPRESENTATIVE MOTION PROOFS COMPLETE / NOT YET VALIDATED`

## 1. Today’s objective

Move P0.3 from entry review into real representative validation using approved A-Series material and canonical source audio, with the goal of identifying a practical motion-comic production method rather than assuming prior still-image or Remotion experiments were sufficient.

## 2. Canonical inputs confirmed

- Repo: `wp5rrp7b2v-droid/black-lady-animatic-v01`
- Main baseline used for today’s P0.3 experiments: `83837d888449e3096636df6ff03b06ee835af175`
- A01 canonical:
  - path: `production/image_library/approved/A_Series/A01_REBOOT_approved_v001.png`
  - SHA-256: `a484bc7f34726f6b1c15f80d1b8a840aa5b4cc17804583ca68dc5eddce833c95`
  - bytes: `3399726`
- A02 canonical SHA-256: `a8a9e5c0cc80df95eccaabf378c27457102365dd3df3012e27fb2417e487f4dd`
- Canonical audio: `AUDIO_MVP1_CANONICAL_V001.m4a`
  - SHA-256: `8d0d12d3af5e2c15032912605c0d1b3f3e892fe24918a7064864b136987737a0`

## 3. A01→A02 transition preparation

A verified Reference Delivery Bundle was created for the bridge-shot experiment:

- source commit: `770635048a427ba1343f1bbee6cb5000f72429a9`
- workflow run: `35838222340`
- artifact: `BRIDGE_A01_A02_REFERENCE_DELIVERY_BUNDLE_V001`
- artifact ID: `10740625723`
- 12 references verified by SHA-256 and byte size.

Two non-formal bridge candidates were generated and retained:

- `BRIDGE_A01_A02_WIDE_CANDIDATE`
  - SHA-256: `f60bf3289bb1eadcab770c9f51cc20afae725d282a3f46b78e401949983785ca`
- `BRIDGE_A01_A02_TIGHT_CANDIDATE`
  - SHA-256: `57f960184441c21ae3f881f8efe47ef858d3c87b13824ba689eeb6d3d282c316`

Both remain staging / experimental. Neither is formal Asset Registry content or LOCKED production output.

## 4. Initial edit validation

Three short A01→A02 variants were built against source audio segment 00:00:00.000–00:00:03.250.

The Product Owner preferred the structural idea of `A01 → Wide → Tight → A02`, but judged the result too jumpy and fragmented. Key finding:

> Additional stills alone do not solve motion continuity. Without internal camera movement the result still reads as “有声音的幻灯片”.

This invalidated the assumption that simply increasing the number of static bridge frames would solve the P0.3 motion problem.

## 5. Remotion camera-move proof

Experimental branch:

`codex/p03-a01-a02-remotion-camera-v002`

Final technical commit:

`01f248e182f4998121525b46eba54c58c28021cf`

Successful workflow run:

`35857760082`

Artifact:

- name: `P03_A01_A02_REMOTION_CAMERA_V002`
- artifact ID: `10747314541`
- digest: `sha256:365eb1b3d643faaa4bed576e2132ae313293cf2803678b715ac62c8abde41bda`

Result:

- technical render: PASS
- artistic judgment: NOT APPROVED / not ideal

Finding:

Remotion can animate scale / translation / timing of a bitmap, but cannot reconstruct missing camera views or scene geometry between independently generated stills. Four independent images cannot reliably become one continuous cinematic camera move by 2D transform tuning alone.

Therefore Remotion remains useful as compositor / editor / timing / audio / output layer, not as the primary mechanism for inventing spatial continuity.

## 6. A01 depth-map proof

Experimental branch:

`codex/p03-a01-depthflow-proof-v001`

Gate A successful run:

`35861220002`

Artifact:

- `P03_A01_DEPTH_GATE_A_V001`
- artifact ID: `10750093687`

Depth estimator:

`Depth Anything V2 Small`

Depth map identity:

- file: `A01_DEPTH_DA2_SMALL_PROOF_V001.png`
- SHA-256: `fdcb7844cac2141a4a37f66b82a8c65a0978bd75d457b1302af21d8e24e14fe5`

Visual review found the relative depth structure usable for a 2.5D push-in: foreground figures, ground, entrance, castle body and sky were separated sufficiently for a practical proof.

## 7. A01 DepthFlow Gate B

Two initial Gate B attempts failed because the renderer script used an unsupported `DepthState.quality` field. The failure was implementation-only; canonical input, depth-map identity, runtime setup and FFmpeg/OpenGL initialization all passed.

Final correction commit:

`d6509c43c987646a04c7ac83329252af78f0741d`

Successful Gate B run:

`35867948575`

Result:

- conclusion: SUCCESS
- output: `A01_DEPTHFLOW_CAMERA_PROOF_V001.mp4`
- 720×1280
- 30 fps
- ~2.5 sec
- H.264
- headless CPU software rendering

Artifact:

- name: `P03_A01_DEPTH_GATE_B_V001`
- artifact ID: `10753710981`
- artifact digest: `sha256:dfcb18789addf195998e8ecd72eeb67311dc234fb86dfa80ef89be57e7ca82b5`

Product Owner review:

`可以，值得继续尝试`

This is approval to continue 2.5D experimentation, not approval of P0.3 and not a formal production lock.

## 8. Current production-direction finding

Current best-supported direction is:

- internal motion should occur inside individual shots;
- normal film cuts should remain between independently authored shots;
- 2.5D depth/parallax is worth further validation for still-based shots;
- Remotion remains the edit/compositing/timing/audio/output layer;
- true AI video / first-last-frame interpolation may be reserved for selected action or hero shots if needed;
- do not force independent stills to imitate one continuous spatial camera path.

This is a working P0.3 direction, not yet a final pipeline lock.

## 9. Execution-performance finding

Successful Gate B run took about 3m37s end-to-end, but the actual 75-frame / 2.5-second CPU render took only about 40 seconds.

Most time was consumed by rebuilding the runtime and repeatedly downloading large Python / Torch / CUDA-related dependencies.

Product Owner direction for next iteration:

`已有的就不要重复下载`

Next engineering optimization should therefore:

- cache reusable Python / model dependencies;
- use a CPU-specific dependency path where possible;
- avoid downloading unused CUDA/NVIDIA packages;
- reuse the existing Gate A depth map;
- avoid rebuilding unchanged inputs;
- preserve exact canonical source / depth identity validation.

Goal: reduce routine V002/V003 and Wide/Tight iteration latency before scaling the method.

## 10. Current P0.3 status

P0.3 is **IN PROGRESS / NOT YET VALIDATED**.

What is established:

- representative static-to-motion testing is now real, not design-only;
- “more stills + hard cuts” alone is insufficient;
- pure Remotion 2D transforms are not the main solution for continuous spatial motion;
- A01 single-shot 2.5D DepthFlow is technically viable and visually promising enough to continue.

What is not established:

- A01 V001 is not a final production shot;
- no bridge candidate is formally ingested;
- no final A01→A02 edit is approved;
- P0.3 has not passed;
- no full production ratio between 2.5D and AI video is locked.

## 11. Resume point

Next work session should start from:

1. optimize the GitHub Actions DepthFlow execution chain so unchanged dependencies are not repeatedly downloaded;
2. create `A01_DEPTHFLOW_CAMERA_PROOF_V002` with refined camera parameters / artifact control;
3. if A01 V002 remains acceptable, apply the same internal-motion method to Wide and Tight;
4. rebuild A01 → Wide → Tight → A02 using internal shot motion + normal cuts;
5. only after that decide whether a selected FLF2V/I2V transition test is still necessary.

Do not merge experimental motion branches into production merely because their workflows technically pass.

## 12. End-of-day governance

- P0.1 remains PASS / PO APPROVED.
- P0.2 remains PASS / PO APPROVED.
- P0.3 remains ACTIVE / NOT YET VALIDATED.
- Product Owner retains all Gate / final production approval authority.
- Canonical approved A01/A02, Character Core, Scene Masters and canonical audio remain unchanged.
- Today’s P0.3 outputs are experimental evidence only unless separately approved and formally ingested.
