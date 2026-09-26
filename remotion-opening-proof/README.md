# D-071 Opening Audio-Comic Proof V001

Independent engineering proof based on canonical R085 commit
`4417fc03af1c19827fa8211d94a5837d8f46e4df`. Historical `remotion-sh05/`
and canonical Project Control are unchanged.

`src/timeline.json` records the locked seven-shot order, half-open frame ranges,
input paths and linear scale endpoints. The composition is 1080 × 1920, 30 fps,
901 frames. It uses straight cuts and one continuous source-audio layer at
original speed and level. No additional sound or effects are added.

All stills use portrait cover. N05 uses a bottom-center zoom origin to preserve
the feet and threshold; N01 uses a lower-center origin to preserve the visitor
grouping during the restrained pull-back. The other shots use center anchors.
N03 has no optional horizontal drift.

## Local static validation

```sh
python3 remotion-opening-proof/scripts/prepare_inputs.py --validate-only
cd remotion-opening-proof
npm ci
npm run typecheck
```

Input validation requires Git and FFprobe (`FFPROBE` may name an executable).
For `--validate-only` on macOS without FFprobe, native `afinfo` reads audio
metadata; the formal Actions runner always uses FFprobe.
It checks the baseline control documents, approved/current registry, exact
canonical paths, Git blobs, PNG signatures, byte sizes, dimensions, locked N-shot
hashes, and canonical audio hash and metadata. A01/A02 SHA-256 values are computed
from the index-authorized binaries, without invented expected hashes.

## Formal render

Use `.github/workflows/p03-opening-audio-comic-proof-v001.yml` on the proof branch.
Pushes restricted to this branch and engineering paths trigger the initial run;
`workflow_dispatch` supports subsequent runs. The runner performs validation,
byte-identical runtime copies, `npm ci`, typecheck and the official
[`npx remotion browser ensure`](https://www.remotion.dev/docs/cli/browser/ensure)
before rendering. No local Mac render is formal evidence.

Output QC probes stream properties, counts decoded frames, verifies audio
coverage, fully decodes video and audio with FFmpeg, verifies MP4 faststart and
calculates SHA-256. Only a successful QC run uploads the seven-day artifact:

```text
P03_OPENING_AUDIO_COMIC_PROOF_V001/
  P03_OPENING_AUDIO_COMIC_PROOF_V001.mp4
  opening_proof_input_manifest.json
  technical_qc.txt
```

Runtime media, dependencies and outputs are ignored and must not be committed.
Engineering success means `TECHNICAL_RENDER_PASS` and readiness for Product
Owner artistic review. It does not approve the proof or pass P0.3. Do not merge.
