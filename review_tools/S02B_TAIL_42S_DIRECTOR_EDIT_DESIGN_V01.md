# S02-B｜后半段 42.30s 剪辑试剪设计 V0.1

Date: 2026-10-12
Status: DIRECTOR EDITORIAL TRIAL / NONCANONICAL / NOT PRODUCT OWNER APPROVED

Parent S02-B V001 approved and locked. N16–N17 V004 (first 21.95s) accepted by Product Owner, no change proposed. This experiment touches **only N18–N26 and A06 in S02-B relative 21.950–64.250 s**, using the canonical audio 100.700–143.000 seconds.

### Director design

The original ten approved images already contain meaningful variation. Do not mechanically fragment all shots. Add two deliberately motivated within-image visual phases:
- N18: Jun looks outside -> camera softly moves the reading toward open doorway / apparently clear sky; stable source and smooth continuous movement.
- N23: Neil near door + group -> camera reads the group direction deeper inside; continuous path, not a gratuitous jump cut.

Retain clean narrative transitions:
- N19 reply at entrance -> N20 start walking inward;
- N20 pair walking -> N21 wider crowd scale;
- N21 cohort -> N22 individual guest POV;
- N23 following Neil -> N24 Guang Yong questions door;
- N24 speaker -> A06 open-door physical fact -> N25 Neil rain-day answer -> N26 lady rule / renewed forward movement.

Preserve V004 quality standard: approved stills from original PNG only, crop width >=720px and <=1.29 relative zoom, once-only video encoding, original audio present, restrained smooth virtual camera, no invented character movement, no heavy crossfades/face ghosts.

### Locked test-only timeline

| S02-B relative time | Story Shot | Visual purpose | Frames |
|---|---|---|---:|
| 21.950–25.050 | N18 | Jun's observation | 93 |
| 25.050–27.983 | N18 | Reframe toward daylight | 88 |
| 27.983–31.650 | N19 | Ning's response | 110 |
| 31.650–35.950 | N20 | Pair starts inward | 129 |
| 35.950–40.750 | N21 | Group scale | 144 |
| 40.750–45.550 | N22 | Individual participants | 144 |
| 45.550–49.150 | N23 | Neil guides movement | 108 |
| 49.150–52.217 | N23 | Group direction / spatial read | 92 |
| 52.217–54.383 | N24 | Guang Yong asks | 65 |
| 54.383–56.483 | A06 | Door remains open | 63 |
| 56.483–60.350 | N25 | Rain-only door rule | 116 |
| 60.350–64.250 | N26 | Lady's requirement / forward hook | 117 |

Timing is frame-quantized editorial test, not word-level transcript authority. All 1269 frames must align to the first 658 frames V004 block to reach the original 1927-frame S02-B runtime in later integration. Video output 720x1280, 30fps H.264, AAC-LC stereo 44.1kHz plus MP3 independent audio.

**Approval boundary:** This is not a revised full movie and is not to replace V001 or register a new Video Index entry. Product Owner reviews tail and may request further changes before approving an integrated noncanonical 64.25s edit. Cloud GitHub Actions only; RC-029 defers Mac synchronization to evening closeout.

## GitHub Actions Render + Verification | 2026-10-12

- GitHub Actions SUCCESS: https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/38257096875
- Artifact: `S02B_TAIL_42S_EDITORIAL_REVIEW_V001`, ID `11750723234`.
- ZIP digest: `sha256:0741d3dbeac212bdd678e31f09fc6e6327dd65f4ad8c8fb7a5009a2a763c627d`. Independently downloaded, ZIP_SHA MATCH and ZIP integrity PASS.
- MP4: `S02B_TAIL_42S_EDITORIAL_REVIEW_V001.mp4`, 16,141,546 bytes; SHA-256 `193b4619b738cdd75a278783059f910ab390adfd054ea7c96542976d419e29d7`; independent hash vs manifest MATCH.
- Original N18/N19/N20/N21/N22/N23/N24/A06/N25/N26 PNGs passed canonical Story Shot Index byte-size and Git blob verification; locked SHA-256 verified when present.
- Original canonical audio SHA-256 `8d0d12d3af5e2c15032912605c0d1b3f3e892fe24918a7064864b136987737a0` verified.
- 720×1280 / 30fps / **1269 frames** / 42.300s / H.264 + AAC 44.1k stereo. Full decode PASS; audio mean volume −14.6 dB, **not silent**.
- V004 approved first 658 frames + verified tail 1269 frames were **locally concatenated for context-only review**, video stream-copy with no additional encoding, and the already-approved S02-B V001 audio stream was mapped unchanged; context-only MP4 yielded 1927 decoded video frames, 64.250s container duration, full video/audio decode PASS. This contextual output is explicitly *noncanonical*, and is **not** automatically registered or published.
- Before PO approval, no Gate, Video Index, Story Shot, or canonical state changes may be inferred from this review.
