# N11｜Neil Abnormal Portrait｜Director Shot Design V0.2

Status: `PRODUCT OWNER APPROVED / REBUILD FROM SCRATCH / BUNDLE V002 BUILT`

Date: 2026-09-27

## 1. Why V0.2 exists

N11 Candidate 01 and subsequent corrective attempts demonstrated a repeatable failure mode:

- over-emphasis on proving “Neil is inside the door” caused the camera to pull back;
- the doorway / architecture became the primary composition;
- Neil shifted from an observational portrait into a formal full/half-body doorway portrait;
- the cross became an unintended focal point;
- the image became more ceremonial and less like Ning Qiushui quietly scrutinizing a person.

V0.2 therefore resets the shot composition while preserving the approved narrative function.

This is a **shot redesign**, not a project-process reset.

## 2. Narrative function — unchanged

N11 corresponds to the narration that Neil is extremely pale and appears to be around fifty years old.

The audience should feel:

`the welcoming butler is now being quietly examined as a person, and something about him feels subtly wrong`.

This is not:

- an entrance establishing shot;
- a doorway hero portrait;
- a religious-symbol shot;
- a new action beat;
- a supernatural reveal.

## 3. Spatial continuity — locked but visually subordinate

Neil has already crossed the threshold and is standing inside the castle.

That continuity must remain true, but it must **not dominate composition**.

Required spatial logic:

`camera outside / near threshold → one foreground door-edge cue → Neil one to two steps behind that plane → darker interior farther behind`

The image does **not** need to show:

- the full doorway;
- the full threshold;
- the floor boundary;
- steps;
- both door leaves symmetrically;
- a large architectural frame around Neil.

The inside/outside relationship should be read through foreground occlusion and depth, not through a wide architectural view.

## 4. Shot scale — hard lock

Target:
`tight medium close-up / upper chest-up`

Hard framing rule:

- top: modest headroom;
- bottom: crop around upper chest / high sternum;
- no waist;
- no lower torso;
- no hands;
- no thighs / floor / threshold slab.

Neil’s face must occupy the visual priority.

If the framing becomes half-body or wider, N11 fails.

## 5. Camera placement

- camera remains on the outside / threshold-facing side;
- near eye level;
- mild 3/4 observation angle;
- avoid full frontal ID-photo symmetry;
- avoid centered ceremonial doorway composition.

Preferred composition:

- Neil slightly off-center;
- one doorframe / open-door edge may appear as a narrow foreground strip on one side;
- the opposite side should not mirror it into a symmetrical portal;
- interior background remains soft / subordinate.

## 6. Foreground depth cue

Use **one-sided foreground occlusion** to prove Neil is inside.

Examples of acceptable cue:

- a narrow vertical slice of the open door;
- a slim doorframe edge;
- a soft foreground architectural edge.

The foreground cue should occupy only a small minority of the frame.

It must not become an architectural subject.

## 7. Neil performance

Neil remains:

- upright;
- still;
- controlled;
- waiting;
- mouth closed;
- gaze directed outward toward the arriving guests;
- expression neutral to slightly over-controlled.

Do not show:

- greeting gesture;
- speaking;
- turn / step;
- hands behind back as a new formal pose;
- hands clasped in front;
- exaggerated smile;
- horror expression.

## 8. Appearance

Preserve canonical Neil:

- approximately fifty;
- pale, low-blood-color skin;
- same face / hair / grooming;
- same formal black butler clothing;
- no monsterization;
- no corpse-blue skin;
- no theatrical whitening;
- no overexposed face.

Pallor should read through natural skin tone, not makeup.

## 9. Cross handling — new hard rule

For N11 V0.2:

`the cross should preferably not be visible at all`.

Reason:

- repeated generations turned the cross into a visual focal point;
- N12 owns “cross + rigid smile” as the next escalation.

If any chain or pendant appears incidentally, it must be cropped, obscured, or too subtle to attract attention.

A clearly visible centered cross = FAIL.

## 10. Background

Background should communicate only:

- darker castle interior;
- vertical stone / Gothic interior depth;
- subtle warm practical lights if already consistent with scene continuity.

It must remain soft and secondary.

Do not generate:

- grand symmetrical hall showcase;
- centered chandeliers;
- ornate architectural hero framing;
- excessive depth that pulls attention away from Neil.

## 11. Reference strategy for Rebuild

For the next Bundle V002:

Keep:
- Neil FACE_FRONT;
- Neil FACE_3Q_LEFT;
- Neil BODY_FRONT;
- Castle Entrance Scene Master;
- N01 immediate Opening end-state continuity.

Remove:
- A03.

Reason:
A03 provides useful spatial facts but appears to over-bias the generator toward a doorway / interior-reverse composition. For N11, the N01 continuity state plus the Director lock is sufficient.

Do not use failed N11 candidates as image references for the rebuild.

## 12. Hard negatives

N11 V0.2 fails if any of the following occur:

- full doorway composition;
- both open doors visible symmetrically;
- obvious threshold / stair / floor foreground;
- half-body or full-body Neil;
- hands visible as a pose;
- centered hero portrait;
- religious-symbol emphasis;
- clearly visible centered cross;
- formal “butler at attention” pose;
- Neil outside the entrance;
- wide architecture dominating the frame;
- overt horror styling.

## 13. Acceptance criteria

A rebuilt N11 candidate is acceptable only if:

1. Neil face is the dominant visual subject;
2. framing is upper-chest-up;
3. Neil is clearly inside, but spatial proof is subtle;
4. one-sided foreground depth cue is enough to imply the doorway;
5. no large doorway / threshold architecture dominates;
6. cross is absent or visually negligible;
7. Neil is still, closed-mouth, waiting;
8. pallor and age read naturally;
9. image feels like quiet scrutiny rather than formal portraiture;
10. N12 still has room to escalate.

## 14. Bundle V002 result

- Product Owner approved V0.2 and the V002 bundle design.
- Bundle: `N11_REFERENCE_DELIVERY_BUNDLE_V002`
- Source commit: `e2b8568f20ba8ee4e044a725d56624e6cbd9b733`
- Run: `36305485637`
- Artifact ID: `10927315457`
- Artifact digest: `sha256:a00cb07e9875afd5f63b1303c8722955d8cf25800aab4990946c5dc9f2df2b7e`
- Exact verification: `5/5 PASS`

Build record:

`docs/project_control/gates/P0_3_video_pipeline/n11_reference_delivery_bundle_v002_build_record_2026-09-27.md`

## 15. Current boundary

Bundle V002 is complete. Authorized next step: Work generates exactly one fresh N11 Rebuild Candidate 01 from Bundle V002. No N12 work or Story Shot registration before Product Owner review.
