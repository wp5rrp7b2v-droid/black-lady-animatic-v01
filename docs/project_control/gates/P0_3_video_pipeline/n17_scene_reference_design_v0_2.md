# N17｜Scene Reference Design V0.2

Status: `DRAFT / READY FOR PRODUCT OWNER REVIEW`

Date: 2026-09-29

Supersedes:

`N17 Scene Reference Design V0.1`

## 1. Shot authority

Parent sequence:

`S02-B Director Shot Design V0.1 / PRODUCT OWNER APPROVED + LOCKED`

Shot:

`N17｜Blood-Door Warning`

Canonical source-audio scope:

`01:28.120 → 01:40.700`

Narrative function:

Ning Qiushui stops the sister discussion and redirects Jun Luyuan to practical Blood Door survival rules. Jun acknowledges that he remembers.

Production status:

`NEW STORY SHOT / NOT YET GENERATED`

This document defines reference authority only.

Not authorized here:

- Reference Delivery Bundle build
- Work image generation
- candidate approval
- Story Shot publication / registration
- S02-B assembly

## 2. Revised composition lock

N17 must create a clear visual break from N16.

N16:

`medium two-shot / Jun speaking emphasis`

N17:

`Ning-dominant close-up / Jun secondary listener`

Locked composition:

- framing: `close-up / tight medium-close`;
- Ning Qiushui is the clear primary subject;
- Ning occupies most of the frame;
- Ning remains oriented toward screen-right, speaking quietly toward Jun;
- Jun remains on screen-right only as:
  - partial cheek / shoulder edge, or
  - soft foreground 3/4 listener,
  depending on generation stability;
- Jun must remain identifiable enough to preserve dialogue ownership, but must not compete with Ning;
- camera is tighter than N16 by a clearly perceptible amount;
- background architecture is strongly subordinated and may be softly out of focus;
- castle entrance DAY / DOOR_OPEN state remains continuity authority even if only a fragment of the doorway / daylight is visible;
- no Neil;
- no rule visualizations;
- no large hand gesture.

Preferred screen impression:

`宁秋水近景 + 君鹭远轻微前景占位`

This should read as a cut-in to Ning's warning rather than another balanced two-person shot.

## 3. Performance lock

Ning:

- calm;
- experienced;
- focused;
- low-key;
- mildly serious;
- no theatrical sternness;
- no heroic exposition;
- mouth state may be neutral / lightly speaking, but avoid exaggerated open-mouth dialogue pose.

Jun:

- listening;
- attentive;
- secondary;
- not frightened;
- not distressed;
- no exaggerated reaction.

The still image should communicate:

`practical warning / restrained vigilance / experienced familiarity`

not:

`lecture / reprimand / panic`.

## 4. Required canonical reference set

### R1｜Ning Qiushui Character Reference Sheet

Asset ID:

`AST_IMG_000060`

Canonical path:

`production/image_library/derived_reference_sheets/ning_qiushui/CHAR_NING_QIUSHUI_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`

Authority:

Primary Ning identity / hairstyle / wardrobe / proportion authority.

Exact identity:

- SHA-256: `15ec6c2682da0fe2502267bde21e9bc0bd7104bbf3e6041521121cc69a0e77be`
- byte_size: `1123635`
- Git blob: `b674733242ab5d603dc42c53b8f7582003064499`

---

### R2｜Ning Qiushui FACE_3Q_RIGHT

Asset ID:

`AST_IMG_000033`

Canonical path:

`production/image_library/character_references/ning_qiushui/CHAR_NING_QIUSHUI_FACE_3Q_RIGHT_DEFAULT_DEFAULT_V001.png`

Authority:

Primary directional face support for Ning speaking toward Jun on screen-right.

Exact identity:

- SHA-256: `7d2292494ab010b324e608f792912fd2d49766318e279bbe22170445464a5c1e`
- byte_size: `2688985`
- Git blob: `6b6a802b67a966f8439c5b000f01d00be422f545`

---

### R3｜Jun Luyuan Character Reference Sheet

Asset ID:

`AST_IMG_000057`

Canonical path:

`production/image_library/derived_reference_sheets/jun_luyuan/CHAR_JUN_LUYUAN_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`

Authority:

Jun identity / wardrobe continuity even when reduced to secondary foreground presence.

Exact identity:

- SHA-256: `e8a0410cfc176ec9d6446b84f89b2c12d0683ec32b927c90353e850c416d909e`
- byte_size: `969995`
- Git blob: `d11db79f4ceab2bb52139bfb8805f7c8f09b0cfc`

---

### R4｜Jun Luyuan FACE_3Q_LEFT

Asset ID:

`AST_IMG_000072`

Canonical path:

`production/image_library/character_references/jun_luyuan/CHAR_JUN_LUYUAN_FACE_3Q_LEFT_DEFAULT_DEFAULT_V001.png`

Authority:

Directional support for Jun listening from screen-right toward Ning.

Exact identity:

- SHA-256: `be9f1f39ae303a61a79746b25a0f9f8153797b179ef85d07a5c2fdf1ce02d01b`
- byte_size: `2002451`
- Git blob: `821c892ffea59ef0739f86585c6c5f8bd1168264`

Boundary:

Jun may be partially visible / softly focused. This reference prevents identity drift if facial features remain visible.

---

### R5｜Castle Entrance Scene Master — DAY / DOOR OPEN

Asset ID:

`AST_IMG_000052`

Canonical path:

`production/image_library/scene_masters/castle_entrance/SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`

Authority:

Scene state:

- castle entrance;
- DAY;
- main door OPEN;
- same threshold / interior-transition environment.

Exact identity:

- SHA-256: `d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961`
- byte_size: `2305753`
- Git blob: `e4dafe096f5c5c8782257030a5a659aeec7808f9`

Boundary:

N17 close-up photography may obscure most architecture. Scene Master controls continuity facts, not the amount of background shown.

---

### R6｜N16 Story Shot — Immediate Continuity

Story Shot:

`N16｜Sister Question`

Canonical path:

`production/image_library/approved/story_shots/N16_SISTER_QUESTION_APPROVED_V001.png`

Exact identity:

- dimensions: `941x1672`
- byte_size: `1942422`
- SHA-256: `b26fb7d64a60fbd28d39b0ae22f7c85df18d4f947f31a3591c847dd5e1acf406`
- Git blob: `44971dd53e37cd1b582bcf5094b0f09cb8e0647d`

Authority:

Immediate continuity only:

- Ning left / Jun right;
- reciprocal conversational eye-line;
- same wardrobe;
- same local lighting;
- same entrance-interior spatial state;
- same quiet conversation.

Required change from N16:

- noticeably tighter framing;
- Ning becomes dominant;
- Jun becomes secondary;
- background becomes less important;
- emotional register shifts from personal question to survival-rule vigilance.

## 5. Minimum reference set decision

N17 V0.2 minimum formal set remains:

`6 references`

1. AST_IMG_000060 — Ning Character Reference Sheet
2. AST_IMG_000033 — Ning FACE_3Q_RIGHT
3. AST_IMG_000057 — Jun Character Reference Sheet
4. AST_IMG_000072 — Jun FACE_3Q_LEFT
5. AST_IMG_000052 — Castle Entrance Scene Master / DAY_DOOR_OPEN
6. N16 — immediate Story Shot continuity

No additional reference is required.

## 6. Explicit exclusions

### A03

`EXCLUDE`

N16 is now the stronger immediate continuity authority.

### N03

`EXCLUDE`

Wrong exterior spatial state.

### N14

`EXCLUDE`

Would reintroduce Neil as a referent and carries a different analytical beat.

### A05

`EXCLUDE`

Key / waist information is no longer relevant.

### A07

`EXCLUDE`

Hall establishment remains reserved for the next narrative sequence.

### N18–N22

`EXCLUDE`

Future material must not back-propagate into N17.

## 7. Generation interpretation locks

Do not turn the close-up into:

- extreme close-up;
- beauty portrait;
- promotional character portrait;
- lecture pose;
- finger-pointing;
- visible rule text;
- fantasy overlays;
- rain visualization;
- dramatic horror reaction.

The shot must still feel embedded in an ongoing conversation.

Target visual language:

`cinematic dialogue cut-in / Ning close-up / Jun soft listener foreground / shallow depth / restrained tension`

## 8. Authority precedence

1. `S02-B Director Shot Design V0.1`
2. `AST_IMG_000060` — Ning identity
3. `AST_IMG_000033` — Ning face direction
4. `AST_IMG_000057` — Jun identity
5. `AST_IMG_000072` — Jun listening direction
6. `AST_IMG_000052` — scene state
7. `N16` — immediate spatial / lighting / wardrobe continuity

Director Shot Design controls shot function and framing.

## 9. Proposed Bundle handoff

If Product Owner approves V0.2:

Next step:

`N17 Reference Delivery Bundle Design V0.1`

Expected Bundle count:

`6 canonical references`

Expected generation target:

`N17 Candidate 01`

No Bundle has been built yet.

## 10. Review gate

Current disposition:

`N17 SCENE REFERENCE DESIGN V0.2 = READY FOR PRODUCT OWNER REVIEW`

Product Owner approval is required before Bundle design/build or Work generation.
