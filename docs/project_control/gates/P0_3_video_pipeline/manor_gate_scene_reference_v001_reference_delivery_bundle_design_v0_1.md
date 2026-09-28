# MANOR_GATE_SCENE_REFERENCE_V001 Reference Delivery Bundle Design V0.1

Status: PRODUCT_OWNER_APPROVED / AUTHORIZED_FOR_BUILD
Date: 2026-09-28

## 1. Purpose
Create the minimum canonical-reference transport bundle for generating the first formal candidate of MANOR_GATE_SCENE_REFERENCE_V001. This is Scene Reference creation, not an N15 Story Shot generation bundle.

Bundle ID:
MANOR_GATE_SCENE_REFERENCE_V001_REFERENCE_DELIVERY_BUNDLE_V001

Target:
MANOR_GATE_SCENE_REFERENCE_V001_CANDIDATE_01

## 2. Canonical inputs
1. AST_IMG_000052 — SCENE_CASTLE_ENTRANCE Scene Master
   - responsibility: WORLD_MATERIAL_PERIOD_ENVIRONMENT_AUTHORITY
   - must NOT control manor-gate geometry.
2. A01 — approved exterior Story Shot
   - responsibility: EXTERIOR_CINEMATIC_CONTINUITY

Reference policy: MINIMUM_CANONICAL_REFERENCES
Reference count: 2
Product Owner manual reference upload: 0

## 3. Director Scene Identity Lock
MANOR_GATE is a detached estate-perimeter exit, not the castle building entrance.

Required reconstructed visual design:
- detached estate perimeter gate;
- two-leaf wrought-iron gate;
- old masonry gate piers;
- lateral perimeter wall / iron fencing;
- internal estate road approaches gate;
- external road continues beyond gate;
- mature vegetation / trees;
- European old-estate visual language;
- maintained but aged; not ruins.

The gate geometry above is RECONSTRUCTED_VISUAL_DESIGN. It is not asserted as direct story-text fact or pre-existing canonical geometry.

## 4. Scene-reference composition lock
- 9:16 vertical.
- neutral reusable Scene Reference, not N15 final composition.
- camera: INTERIOR_SIDE_3Q_ESTABLISHING, approximately 30–45 degrees.
- clearly show Gate + left/right boundary + internal road + external road.
- gate must not fill the frame.

Base state:
DEFAULT_DAY_CLOSED_V001
- DAY
- DRY
- GATE CLOSED
- NO RAIN
- NO PEOPLE
- NO VEHICLES
- NO KEY
- NO ACTION
- do not visually emphasize LOCKED.

## 5. Authority precedence
1. Director Scene Identity Lock
2. AST_IMG_000052 world / material / period / environment authority
3. A01 exterior cinematic continuity
4. reconstructed gate geometry definition

AST_IMG_000052 is explicitly NOT gate-geometry authority.
DO NOT COPY CASTLE ENTRANCE DOOR AS MANOR GATE.

## 6. Explicit exclusions
Do not use:
- SCENE_FIRST_HALL;
- A02–A07;
- N01–N14 Story Shots;
- character Core References;
- Neil;
- keys / key rings / locks as narrative emphasis;
- church;
- Black Lady;
- rain-state imagery;
- generic external manor-gate references;
- internet reference images;
- rejected or superseded candidates.

## 7. Planned artifact
MANOR_GATE_SCENE_REFERENCE_V001_REFERENCE_DELIVERY_BUNDLE_V001/
- delivery_manifest.json
- WORK_HANDOFF.md
- world_refs/AST_IMG_000052__SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png
- continuity_refs/A01__A01_REBOOT_approved_v001.png

## 8. Build validation
Fail closed unless both canonical binaries pass registry/index identity, approval/lifecycle, canonical path, byte size, Git blob, SHA-256 (locked or computed), PNG signature, dimensions, regular-file/no-symlink checks, byte-identical copy, and final artifact revalidation.

Expected:
PASS: 2/2 exact canonical reference binaries verified

## 9. Boundary
Authorized now:
GitHub Actions real bundle build and verification.

Not authorized:
- Work generation before verified artifact exists;
- N15 candidate generation;
- Scene Master formalization/Registry mutation before Product Owner candidate approval;
- Story Shot registration.
