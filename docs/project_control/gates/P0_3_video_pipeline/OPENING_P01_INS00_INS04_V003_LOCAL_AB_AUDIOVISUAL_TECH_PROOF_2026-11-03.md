# 《诡舍·黑衣夫人》｜Opening P01｜INS-00 + INS-04 局部声画 A/B｜V003 技术验证记录
日期：2026-11-03
状态：**LOCAL AVI PROOF TECHNICAL PASS / PO EDITORIAL REVIEW PENDING / NEW STORY SHOT REGISTRATION HOLD / NOT FORMAL VIDEO**

## 1. Product Owner 当前约束

PO 选择此前两方案中的「B」：**用已经由PO视觉批准但尚未登记的 INS-00 无人住宅入口 + INS-04 宁秋水靠背后轻搭君鹭远肩膀**，进行局部 A/B 声画测试，保留全部原始声音和七张正式镜头，不发布、登记或正式替换。INS-01/INS-02 及较早错误站位 INS-04 V001均视觉FAIL，不参与。

**IMPORTANT：**本次两个新增图像的PO批准仅限用户指定的 exact images，本次 Chat 对其二进制读取与记录不是 Github Canonical 的正式资产登记。

## 2. 输入独立验证

- Approved full original audio: `OPENING_P01_P04_NEIL_COMPACT_AUDIO_PROOF_V001.m4a`; 192.257 s; 4647911 bytes; SHA256 `1701f3a8140775550a30ac788b9221486349c058278d1ef0c2c5163664d6c4ac`; on-disk rehash PASS.
- Previously delivered technical V002 audiovisual baseline: `P01_SEVEN_SHOTS_AUDIOVISUAL_PROOF_V002.mp4`; 63.375 s; SHA256 `e30d0604ef26ed95d4496e7996d18262c84c1827211cf554e879b9856079b7b3`; on-disk rehash PASS.
- PO Approved INS-00 image original name `OPENING_P01_INS_00_RESIDENCE_GATE_ESTABLISH_CANDIDATE_01(1).png`; 941×1672; 2152581 bytes; SHA256 `9f5b55574e417c002aab20472277f6b413b50be06106c23e95bb520bb70b21e7`.
- PO Approved INS-04 final relaxed shoulder original name `暖光下轻搭肩膀(1).png`; 941×1672; 1803413 bytes; SHA256 `a9ca228f99f70b0ebf38852002b408808a2d43aceb184fdc918732d3e4abd96d`.
- Original P01 OPEN01 JPEG extracted from previously independently exact-verified 7-image GitHub Actions bundle (one nested ZIP). SHA256 `4ccebb6a903b9cbeac1dfdc2e8b05c7f5dafa05e31cff53e775dfa2f37945452`, 864×1536. This is a temporary derivative input; original canonical JPEG unchanged.

## 3. V003 editorial pilot — test-only EDL

All times absolute on already-approved compact audio.

| Time | V002 original rough cut A | V003 insertion B |
|---|---|---|
| 00:00–00:07.500 | V002 existing interior/narrative cuts | INS-00 stationary empty residence entrance, unseen Bai/Jun speech continues |
| 00:07.500–00:10.500 | V002 original edited shots | Approved OPEN-01 three-person establishing view for interior reveal |
| 00:10.500–00:31.750 | Unchanged V002 | Unchanged V002 |
| 00:31.750–00:37.000 | V002 existing Bai→Ning→relationship cut | INS-04 approved image: Ning from sofa-rear naturally touches seated Jun's near shoulder |
| 00:37.000–01:03.375 | Unchanged V002 | Unchanged V002 |

**Working hypothesis**: 7.5s entrance-to-interior cut roughly follows the early Jun “decided” statement, and 31.75–37s roughly spans Ning volunteering; the original Cue Sheet is approximate, no exact Mandarin word timing or lip-sync ground truth has been verified. These cut points are candidates, not authoritative production EDL. Only PO audiovisual listening can determine aesthetic PASS.

**Constraint pass**: no source audio excerpt reordered or omitted; video is normal chronological 00:00–01:03.375. Audio is encoded into the MP4 from the exact M4A without word insertion. Approved source M4A unchanged, although output AAC is a new derivative encoding.

## 4. Actually generated deliverables and QC

### Full V003 63.375-second local video

- `P01_V003_GATE_SHOULDER_AV_AB_PROOF_V001.mp4` — 942×1672, 24fps, H.264/yuv420p + 48000Hz stereo AAC, 1521 frames, size **7860439 bytes**.
- SHA256 `3e38dbd8db9e00f4c866bf86b343a2b6d1fa8b9dcae47de0b46cdd7334ab667f`.
- FFmpeg full-video and audio decode **PASS**.
- Eleven timepoint frames extracted; key static-video image comparisons at 1.0s gate MAE=2.293/255, 7.75s approved OPEN01 MAE=1.928/255, 32.5s approved INS04 MAE=7.367/255 (lossy H.264); reference visual match PASS.
- Output mono 8kHz decoded PCM versus same excerpt of original approved source: Pearson correlation **0.999845**, no detected wholesale reordering/replacement; this correlation alone does NOT establish word-level speech timing.
- `P01_V003_AB_KEYFRAMES_REVIEW.jpg` contains 11 chronological frame samples of V003 for quick visual inspection.

### Local A/B comparison clips

These samples play the A cut (V002) first, then the B cut (V003), repeat the same 12s/13s original-audio interval in each half for comparison only. A/B file repeats sound intentionally; the full V003 file never repeats sound.

- `P01_AB_OPENING_A_THEN_B_V002_V003.mp4`: A(00:00–00:12) then B(00:00–00:12), 24.021333s, 9740934 bytes; SHA256 `79a5fd21b4b0c3c95a47311589d64d9ab1ed7b370c4f6e19f37900effaf864ce`; full decode PASS.
- `P01_AB_SHOULDER_A_THEN_B_V002_V003.mp4`: A(00:29–00:42) then B(00:29–00:42), 26.021333s, 14374610 bytes; SHA256 `04aa1015cf7a9a0c7d2e0e9ebd6578e2d24c578f7592abcc096964a13df05668`; full decode PASS.

Comparisons contain small English A/B overlay labels only for distinguishing the two clips; these are not part of a new canonical movie. All artifacts are **local user-visible Chat session outputs only**; not committed to the private GitHub repo, and not yet a formal video.

## 5. PO editorial gate and current status

**Confirmed FACT:** both newly PO approved exact-image originals used only as video derivatives; original audio sequence continuous; image segments map correctly at test timepoints; V003 full and two A/B snippets have fully passed technical decode and show expected footage.

**Still UNKNOWN:** whether the clip at 7.5s falls exactly after Jun's intended words, whether INS04 31.75s starts on Ning's true speaking onset, whether introducing a roughly 7.5s static exterior adds too much screen time, and whether added static INS04 visibly improves performance without additional gesture movement.

**PASS for editorial:** PO hears no character speech/shot misalignment and prefers new establishing and shoulder beat in actual A/B watch. **FAIL:** cut happens within clause, outside gate overlong, shoulder pose unnatural in montage, or spatial/performance issue persists; revise only the failing cut points/segment length before authorizing more artwork.

Current GitHub Canonical control unchanged: Story Shot index **42**, formal Video Index **3**, `P0.3 IN PROGRESS`, accepted INS-00/INS-04 **HOLD for later joint registration**. This record is a test log only, not a publication/approval/control-closeout.
