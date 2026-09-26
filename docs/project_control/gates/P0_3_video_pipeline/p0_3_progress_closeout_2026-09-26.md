# P0.3 Progress Closeout｜2026-09-26

Status: `PAUSED FOR DAY / P0.3 IN PROGRESS / OPENING V2 STORY-SHOT EXPANSION ACTIVE / N06-N07 NEXT`

## 1. Opening V1 proof result

The first real 30-second Opening Audio-Comic Proof was assembled from the then-locked seven-shot chain:

`A01 → A02 → N02 → N03 → N04 → N05 → N01`

Technical render passed. Formal evidence:

- PR #16: `D-071: Opening Audio-Comic Proof V001`
- workflow run: `36235214156`
- artifact: `P03_OPENING_AUDIO_COMIC_PROOF_V001`
- artifact ID: `10904156261`
- MP4 SHA-256: `c27d06a745b7ae6814453bbcdf3dd7fcec7cace584d10445f957755a061a3922`

Product Owner artistic review did not approve the proof as final. Main findings:

- visual coverage was insufficient for the narration;
- N05 and N01 were placed too early relative to the narrated action;
- the frozen N05 action state stayed on screen too long;
- restrained 2D motion avoided character deformation but repeated push-ins felt templated when overused.

Therefore PR #16 remains OPEN / NOT MERGED. The proof is retained as technical evidence only and does not constitute P0.3 PASS.

## 2. Opening V2 directorial structure

The revised 12-shot Opening plan is:

`A01 → A02 → N06 → N02 → N07 → N03 → N04 → N08 → N09 → N10 → N05 → N01`

Current narrative functions:

- N06: Neil speaking state A during “莫妮卡夫人正在教堂祈祷……”
- N07: Neil speaking state C during “等夫人祈祷结束后……”
- N08: castle architecture emphasis for “巨大的褐色古堡前……”
- N09: formal butler descriptor for “一名西装笔挺的管家……”
- N10: restrained subtle-smile beat for “对着面前的众人微微一笑”
- N05: turn / threshold action for “旋身迈进了古堡大门”
- N01: post-action / interior continuation

N06 and N07 are still pending.

## 3. N08 production and approval

N08 formal reference delivery followed the locked Work image-generation chain:

`GitHub canonical assets → Registry / Resolver validation → Actions Delivery Artifact → Work automatic download + revalidation → generation`

Delivery evidence:

- Bundle: `N08_REFERENCE_DELIVERY_BUNDLE_V001`
- workflow run: `36239171848`
- artifact ID: `10904692728`
- manual Product Owner reference upload: `0`

Product Owner approved:

`N08 Candidate 01｜Castle Entrance Architecture`

Final canonical file:

`production/image_library/approved/story_shots/N08_CASTLE_ENTRANCE_ARCHITECTURE_APPROVED_V001.png`

Locked SHA-256:

`6bda5a8cb4d04d15071f95c6b3fdce09b10230ac95100d59aabf5bad4aef1bb4`

## 4. N09 production and approval

N09 formal delivery evidence:

- Bundle: `N09_REFERENCE_DELIVERY_BUNDLE_V001`
- workflow run: `36240331178`
- artifact ID: `10904648974`
- manual Product Owner reference upload: `0`

Review history:

- Candidate 01: rejected because composition / body state were too close to N04 and read as a formal portrait.
- Candidate 02: identity and descriptor function improved, but the door / arch / threshold composition made Neil read as standing inside the castle.
- Candidate 03: corrected the spatial relationship. Neil stands clearly on the exterior stone platform with the open double doors behind him.

Product Owner approved:

`N09 Candidate 03｜Neil Formal Butler Descriptor`

Final canonical file:

`production/image_library/approved/story_shots/N09_NEIL_FORMAL_BUTLER_DESCRIPTOR_APPROVED_V001.png`

Locked SHA-256:

`5e76be2c9815a6caa2d8688d1879bb5ddaad78352b6440ed220dd08332a5e0ac`

## 5. N10 production and approval

N10 formal delivery evidence:

- Bundle: `N10_REFERENCE_DELIVERY_BUNDLE_V001`
- workflow run: `36246674607`
- artifact ID: `10908280143`
- manual Product Owner reference upload: `0`

N10 was designed as a micro-expression shot only. The locked performance boundary is:

- restrained closed-mouth slight smile;
- no teeth;
- no speaking;
- no turn;
- no step;
- no sinister / exaggerated expression;
- still readable as exterior castle-entrance context.

Product Owner approved:

`N10 Candidate 01｜Neil Subtle Smile`

Final canonical file:

`production/image_library/approved/story_shots/N10_NEIL_SUBTLE_SMILE_APPROVED_V001.png`

Locked SHA-256:

`14dbf276dbf9ef6c7de84570d46f40230daa3ba53a304ccdc05645c58e9f6e54`

## 6. Formal registration result

N08 / N09 / N10 are formally registered as approved/current Story Shots.

Registration / verification evidence includes:

- upload verification run: `36247789055`
- additional closeout verification run: `36248526501`
- all three PNGs: 941 × 1672
- SHA-256 / byte size / Git blob verification: PASS
- canonical rename: exact Git blob reuse, no re-encode

Approved Story Shot count is now:

`15`

Current approved set:

`A01–A07 + N01–N05 + N08–N10`

N06 / N07 remain unproduced and unregistered.

## 7. Engineering rule confirmation

The formal Work image-generation delivery chain was executed as locked for N08, N09 and N10:

`GitHub canonical assets → Resolver / Registry validation → Reference Delivery Bundle → Work automatic PNG acquisition → Work revalidation → generation`

No routine manual Product Owner reference upload was required.

Temporary N08 / N09 / N10 delivery and verification workflows were removed from `main` after evidence capture.

## 8. P0.3 gate status

P0.3 remains:

`IN PROGRESS / CINEMATIC AUDIO-COMIC ROUTE ACTIVE / NOT YET VALIDATED`

No P0.3 PASS claim is made.

## 9. Resume point

Next session:

1. design N06;
2. build and verify N06 Reference Delivery Bundle;
3. generate / review / approve / register N06;
4. design and produce N07 through the same locked pipeline;
5. when N06 and N07 are both formally registered, assemble the revised 12-shot Opening V2 Proof;
6. review audio/action alignment, shot rhythm, narrative readability and restrained 2D motion;
7. only then determine whether P0.3 is ready for approval or needs another revision.

## 10. Repository / local sync boundary

End-of-day remote truth must remain GitHub `main`.

PR #16 stays OPEN / NOT MERGED as historical technical-proof evidence.

Before the next local formal-production session:

`git status`

then, if no tracked local changes:

`git pull --ff-only origin main`

Known local-only exclusions / untracked working material must not be staged or deleted mechanically.
