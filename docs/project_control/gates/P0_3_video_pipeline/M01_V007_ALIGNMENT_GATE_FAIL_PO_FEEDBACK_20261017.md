# M01 V007 光源定位门禁失败 / Product Owner 定位反馈

Date: 2026-10-17
Source: S02B_V007_M01_MASKS_ON_REAL_FRAMES_GATE0_V001.jpg
Status: **LIGHT_REGISTRATION_FAIL**; M01 V007 is NOT a batch-ready candle engine.
This document is a quality hold, not an approval or automatic V007 rollback.

## Product Owner original observations

- N16：偏下
- N18：偏左
- N20：偏左
- NEW-01：偏左
- N21：偏右
- A06：偏左下
- N24：右边的偏左
- 总体准确率不高。

Direction convention: above describes the **current effect mask position relative to the actual candle**. Thus correction direction is the opposite: N16 up; N18/N20/NEW-01 right; N21 left; A06 right and up; N24 right-hand source further right.

## Other critical findings from actual alignment sheet

Inspection shows some broad red effect masks intersect visible people, especially the middle NEW-01 source/face region and some later crowd shots. The prior renderer enforces changes outside the manually set mask == 0 but **does not independently confirm person/skin exclusion**. Therefore previous technical pass is strictly binary/duration/source protection, NOT flame registration or valid human protection.

Seven items reflect Product Owner-flagged misalignment **by shot**, not a statistical estimate of candle detection accuracy; avoid inventing a numerical accuracy percentage.

## Freeze and gates

- Do not promote V007 M01 masks to reusable Scene Light Atlas or production defaults.
- Do not launch another V007 full-length batch with these masks.
- Correct directional issues using actual frame overlay, marking proposals as DRAFT and awaiting positional calibration review.
- Per source, require evidence-backed `flame_core`, `halo`, `wall_receiver`, `protected_people` separate masks; uncertain sources STOP / CALIBRATION_REQUIRED.
- Test candidate alignment and exclusion before any new M01 render.
- Existing user-approved N23/NEW02 style remains a **style reference only**, not blanket approval of all light coordinates.
- Change control: review branch documentation and non-destructive diagnostic only, no formal Story Shot, official Video Index or main modification.
