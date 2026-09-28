# N15｜Reference Delivery Bundle Design V0.1

Status: `PRODUCT OWNER APPROVED / BUILD AUTHORIZED`

Date: 2026-09-28

Target bundle: `N15_REFERENCE_DELIVERY_BUNDLE_V001`
Target generation: `N15 Candidate 01`

## 1. Director lock
N15 = `AUDIENCE-ONLY FORESHADOWING OF THE TRUE FINAL EXIT`.
No character has discovered the gate. No character POV. No key/lock solution reveal.

## 2. Canonical reference set
Reference count: `2`.

### REF-01｜Formal MANOR_GATE Scene Authority
- asset_id: `AST_IMG_000084`
- entity_id: `SCENE_MANOR_GATE`
- role: `SCENE_MASTER`
- variant/state: `DEFAULT / DAY_CLOSED`
- authority: `MASTER`
- path: `production/image_library/scene_masters/manor_gate/SCENE_MANOR_GATE_SCENE_MASTER_DEFAULT_DAY_CLOSED_V001.png`
- SHA-256: `95b3bebce1b2e9be72d5a2bc99665a4a99719eb0f4146e40a562210bd982e278`
- byte_size: `3279563`
- Git blob: `ac1dfb7be2069848917afb9749de6c8ebc54d3e5`
- dimensions: `941x1671`
- responsibility: sole MANOR_GATE identity / geometry authority; Gate + Boundary + Road; estate internal road → gate → external road.

### REF-02｜A01 world / exterior cinematic continuity
- shot_id: `A01`
- path: `production/image_library/approved/A_Series/A01_REBOOT_approved_v001.png`
- approval/lifecycle: `APPROVED / CURRENT`
- byte_size: `3399726`
- Git blob: `35769a40dc1fd559d97908235f6a6024562b71b7`
- responsibility: world, exterior atmosphere, material/weather/cinematic continuity only.
- restriction: no authority over gate geometry, gateposts, boundary or N15 composition.

## 3. Authority precedence
1. N15 Director Shot Design — narrative / photography / knowledge boundary.
2. AST_IMG_000084 — sole MANOR_GATE Scene Identity / Geometry Authority.
3. A01 — world / exterior cinematic continuity only.

Conflict rule: `AST_IMG_000084 wins all MANOR_GATE identity/geometry conflicts.`

## 4. Explicit exclusions
Do not include: AST_IMG_000052 / SCENE_CASTLE_ENTRANCE; any character reference; N14; A05; key/lock imagery; historical MANOR_GATE candidates; internet references.

## 5. WORK_HANDOFF locks
Generate exactly one `N15 Candidate 01`.
- 9:16 vertical.
- View from inside estate toward outer manor gate.
- Preserve AST_IMG_000084 Gate Identity.
- Gate closed.
- Gate + Boundary + Road all readable.
- External road continues beyond gate.
- More cinematic than neutral Scene Master; do not simply copy its 3/4 reference composition.
- Prefer more distance/depth/final-endpoint feeling.
- Gate is sole narrative subject.
- Zero characters; zero Neil; zero keys; zero chains; zero padlock emphasis; zero opening action.
- No character POV or evidence that characters discovered the gate.
- Tone: quiet spatial foreshadowing / restrained unease / distant endpoint.
- Not horror poster, ruin, fantasy gate, or castle entrance.

## 6. Planned artifact layout
`N15_REFERENCE_DELIVERY_BUNDLE_V001/`
- delivery_manifest.json
- WORK_HANDOFF.md
- scene_authority/AST_IMG_000084__SCENE_MANOR_GATE_SCENE_MASTER_DEFAULT_DAY_CLOSED_V001.png
- continuity_refs/A01__A01_REBOOT_approved_v001.png

Retention: 7 days.
Manual Product Owner reference upload: 0.

## 7. Build validation
Fail closed unless 2/2 canonical binaries pass registry/index identity, authority/approval/lifecycle, canonical path, byte size, SHA-256 where locked/computed, Git blob, PNG signature/dimensions, regular-file/no-symlink, byte-identical artifact copy and final artifact revalidation.

Expected: `PASS: 2/2 exact canonical reference binaries verified`.

## 8. Current boundary
Product Owner approved this Bundle Design on 2026-09-28 and authorized Bundle construction only.
Not yet authorized: N15 image generation; Story Shot registration.
