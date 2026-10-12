# S02-B｜后半段 42.30s「信息驱动的切片剪辑」V002｜导演设计

Date: 2026-10-12

**Source of revision:** Product Owner said “后面几个镜头感觉就是在重复的拉近拉远”. This critique rejects the mechanically repetitive visual language in the tail V001 experiment; **do not call tail V001 approved**.

**Treatment shift:** Camera motion is not visual content. Cut to informative compositions, not change crop scale merely because seconds are passing. In this V002 test:
- N18: 3.10 sec held view of Jun observing; direct motivated cut to 2.93 sec held composition favoring clear sky. Same PO-approved image, two *different viewing purposes*, not an automatic zoom.
- N19: deliberate held reaction to dialogue.
- N20: one slight lateral follow of the pair (fixed shot size, no zoom).
- N21: stable group-scale view and doorway spatial continuity.
- N22: locked observational participant frame.
- N23: 3.60 sec held emphasis on Neil at threshold, 3.07 sec held crowd traffic in a different area of the approved same source; a **subject change**, not push/pull.
- **N24/A06/N25/N26:** locked reaction → architectural door evidence → Neil's response → group moves deeper. **Zero animated zoom**, preserve dialogue rhythm and clear narration.
- Straight cuts between speakers, places and evidence. No uniform dissolves, faux dolly, artificial motion, masks or new character features. Keep quality from V004: crop >=720 native source pixels, relative zoom max 1.29; each source PNG exact SHA + blob verified; one video encode from PNG originals, unaltered source audio window [100.700, 143.000], AAC non-silent check, 1269 frames.

This is editorial noncanonical review ONLY. Previously approved N16–N17 V004 first 658 frames unchanged. Official complete S02-B V001 (64.250 sec) remains current and immutable. No Video Index, Story Shot or P0.3 status change. Submit V002 tail and side-by-side with tail V001 before further production / integrated review.

Artifacts expire after 7 days; do not promote to canonical storage without Product Owner approval and separate publication verification.

## 2026-10-12 Verified V002 Deliverables / A-B Technical Check

- GitHub Actions SUCCESS: https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/38260416254
- Artifact: ID `11751264976`, ZIP SHA-256 `b1ef4edebc3726c470025f4fa36c3d4087655e898a0b4ffa0d86e17b2702f096`, independently downloaded and ZIP integrity + digest PASS.
- Tail candidate `S02B_TAIL_42S_CONTENT_CUT_V002.mp4`: **5,861,790 bytes**, SHA-256 `4c14231e50ede2d8c9c7cd8eec56e823943ff8d763e141d19d241867ccccd788`, matched `RENDER_MANIFEST.json`. 720×1280, H264/AAC, 1269 frames, 42.300s; full decode PASS, AAC mean -14.6 dB.
- Local test-only editorial A/B: `S02B_TAIL_V001_V002_NARRATIVE_CUT_AB.mp4`, SHA-256 `37e3a00ab743384b33394b0a589870fd87e01642ca90cb20db8330533c8b5dbc`, 1269 frames, 42.300s, full decode PASS. Left=V001 repetitive push-pull; right=V002 static subject cutaways.
- Local 64.250-second context preview: `S02B_FULL_64S_CONTENT_CUT_V002_CONTEXT_REVIEW.mp4`, SHA-256 `138e440d09dd188709721e9274b0b60660e84b849b73040c0bc84d5e8de64a6e`, 1927 frames, full decode PASS. Exact approved opening V004 and independently rendered tail V002 video stream-copy; original S02-B V001 AAC track preserved. No canonical publish.
- Director self-check caveat: The static N23 Neil/crowd crops share considerable visual content, so perceived variation may remain modest. If PO asks for truly different framing, do not simulate another zoom: propose 1–2 new identity-controlled reaction or architectural detail Story Shots via the locked Chat→GitHub Actions→Work→PO workflow.
- **PO verdict pending**; no replacement of current V001, no Video Index changes, no Gate promotion. Mac sync remains EOD.
