# N26｜Scene Reference Design V0.2 — Identity Rescue

Date:

`2026-10-06`

Status:

`PRODUCT OWNER APPROVED / LOCKED`

Supersedes for future generation:

`N26 Scene Reference Design V0.1`

Reason:

`Candidate 01 failed named-character identity preservation for Ning Qiushui and Jun Luyuan.`

Upper authorities retained:

- N26 Node-Level Director Shot Design V0.1 = PRODUCT OWNER APPROVED / LOCKED
- N26 / N27 Merge Decision = PRODUCT OWNER APPROVED / LOCKED
- N27 = ABSORBED INTO N26
- active sequence tail = `N23 → N24 → A06 → N25 → N26`
- direct-image cap = `<= 5`

## 1. V0.2 redesign objective

Prioritize:

`NEIL CONTINUITY + NING FACE/IDENTITY + JUN FACE/IDENTITY`

over:

`SCENE MASTER REDUNDANCY + GENERIC GUEST REFERENCE COMPLETENESS`

Candidate 01 proved that a crowd-heavy rear-view composition can erase named-character identity even when Reference Sheets are supplied.

Therefore V0.2 changes both:

1. direct-reference allocation;
2. camera / blocking grammar.

## 2. Direct-reference strategy — EXACTLY 5

### 1. N25 Approved Story Shot

Canonical:

`production/image_library/approved/story_shots/N25_RAIN_DAY_RULE_NEIL_ANSWERS_WITHOUT_TURNING_APPROVED_V001.png`

Purpose:

`NEIL + IMMEDIATE SCENE / LIGHTING / COHORT CONTINUITY`

N25 now carries:

- Neil identity and wardrobe;
- immediate inner-lobby architecture;
- warm low-key lighting;
- generic cohort visual family.

This allows V0.2 to remove separate Scene Master and Generic Guest board from the direct-reference set.

Important:

`CONTINUITY AUTHORITY ONLY / DO NOT COPY N25 COMPOSITION`

### 2. AST_IMG_000060｜Ning Qiushui Character Reference Sheet

Purpose:

`NING GLOBAL IDENTITY / WARDROBE / BODY PROPORTION`

Exact:

- SHA-256: `15ec6c2682da0fe2502267bde21e9bc0bd7104bbf3e6041521121cc69a0e77be`
- byte size: `1123635`
- Git blob: `b674733242ab5d603dc42c53b8f7582003064499`

Hard rule:

`NING QIUSHUI MUST NOT PUT HANDS IN POCKETS`

### 3. AST_IMG_000071｜Ning Qiushui FACE_3Q_LEFT

Canonical:

`production/image_library/character_references/ning_qiushui/CHAR_NING_QIUSHUI_FACE_3Q_LEFT_DEFAULT_DEFAULT_V001.png`

Purpose:

`NING FACE-IDENTITY RESCUE / READABLE 3Q FACE`

Exact:

- approval: `APPROVED`
- lifecycle: `CURRENT`
- role: `FACE_3Q_LEFT`
- SHA-256: `8d92bcc601220654499f7be57fc83411c57dedccc44e8f764cc65ce1b840334e`
- byte size: `1761408`

V0.2 camera must give Ning enough 3/4 facial visibility for this reference to matter.

### 4. AST_IMG_000057｜Jun Luyuan Character Reference Sheet

Purpose:

`JUN GLOBAL IDENTITY / WARDROBE / BODY PROPORTION`

Exact:

- SHA-256: `e8a0410cfc176ec9d6446b84f89b2c12d0683ec32b927c90353e850c416d909e`
- byte size: `969995`
- Git blob: `d11db79f4ceab2bb52139bfb8805f7c8f09b0cfc`

### 5. AST_IMG_000072｜Jun Luyuan FACE_3Q_LEFT

Canonical:

`production/image_library/character_references/jun_luyuan/CHAR_JUN_LUYUAN_FACE_3Q_LEFT_DEFAULT_DEFAULT_V001.png`

Purpose:

`JUN FACE-IDENTITY RESCUE / READABLE 3Q FACE`

Exact:

- approval: `APPROVED`
- lifecycle: `CURRENT`
- role: `FACE_3Q_LEFT`
- SHA-256: `be9f1f39ae303a61a79746b25a0f9f8153797b179ef85d07a5c2fdf1ce02d01b`
- byte size: `2002451`

V0.2 camera must give Jun enough 3/4 facial visibility for this reference to matter.

## 3. References deliberately removed from direct input

Removed:

- `AST_IMG_000108｜Castle Entrance Inner Lobby`
- `BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q`

Reason:

`NAMED CHARACTER IDENTITY RESCUE TAKES PRIORITY`

N25 already provides adequate immediate environment / lighting / cohort continuity for this regeneration.

These removed references remain contextual authority but are not direct generation images in V0.2.

## 4. Camera redesign

Candidate 01 used a too-back-dominant view.

V0.2 must NOT repeat that.

Preferred:

`OBLIQUE SIDE / SIDE-FRONT GROUP TRANSITION`

The cohort should move diagonally across or away through the frame rather than straight away from camera.

Required:

- Neil still leads;
- Neil may remain side-back / rear-3Q;
- Ning must show a readable 3/4 face;
- Jun must show a readable 3/4 face;
- Ning and Jun do not both need to face the same direction;
- no direct camera stare.

This is not a portrait setup.

It is:

`WALKING CHARACTERS WITH READABLE IDENTITY`

## 5. Named-character blocking

Neil:

- first subject;
- slight forward lead;
- still moving;
- no stop-and-address pose.

Ning:

- key secondary follower;
- clearly recognizable;
- 3/4 face visible;
- natural walking posture;
- hands out of pockets.

Jun:

- key secondary follower;
- clearly recognizable;
- 3/4 face visible;
- natural walking posture.

Ning + Jun:

- different depths;
- different screen positions;
- not shoulder-to-shoulder;
- not symmetrical;
- not a frontal pair.

## 6. Crowd simplification

V0.2 does NOT need to maximize anonymous guest count.

Preferred:

`2–4 GENERIC SUPPORTING GUESTS`

rather than 3–5 if more guests weaken Ning / Jun identity.

Use guests as:

- partial foreground bodies;
- deeper silhouettes;
- soft secondary movement.

Do not let them compete with Ning / Jun.

## 7. Motion

Still locked:

`NEIL LEADS / GROUP BEGINS FOLLOWING`

Do not regress to:

`GROUP MOSTLY PAUSED`

But avoid a procession / queue.

## 8. Scene continuity

Still:

`CASTLE_ENTRANCE_INNER_LOBBY / MOVING TOWARD DEEPER CASTLE`

Use N25 as immediate visual continuity.

Do not invent:

- a completely new hall;
- First Hall;
- fireplace;
- grand staircase;
- exterior;
- main door;
- rain.

## 9. Lighting

Match N25:

- warm low-key;
- restrained amber/tungsten;
- natural skin;
- dark environment;
- no brightness lift;
- no studio look.

## 10. Hard fail

Automatic FAIL if:

- Ning does not resemble AST_IMG_000060 + AST_IMG_000071;
- Jun does not resemble AST_IMG_000057 + AST_IMG_000072;
- Ning / Jun are shown almost purely from the back with identity unreadable;
- Ning puts hands in pockets;
- Ning + Jun become a frontal paired portrait;
- Neil + Ning + Jun become a poster;
- crowd overwhelms named characters;
- queue / synchronized gait;
- bags / luggage;
- new hall / First Hall / fireplace / main door / rain;
- cutout / pasted-on layers.

## 11. V0.2 priority order

1. Neil continuity from N25
2. Ning identity
3. Jun identity
4. walking/group-follow logic
5. inner-lobby continuity
6. generic crowd count

## 12. Proposed next Bundle

If approved:

`N26_REFERENCE_DELIVERY_BUNDLE_V002`

Exactly 5 direct images:

1. N25 Approved Story Shot
2. AST_IMG_000060
3. AST_IMG_000071
4. AST_IMG_000057
5. AST_IMG_000072

Candidate target:

`N26 Candidate 02｜Clean Regeneration / Identity Rescue`

## 13. Current gate

`PRODUCT OWNER APPROVED / LOCKED / NEXT: N26_REFERENCE_DELIVERY_BUNDLE_V002 DESIGN`
