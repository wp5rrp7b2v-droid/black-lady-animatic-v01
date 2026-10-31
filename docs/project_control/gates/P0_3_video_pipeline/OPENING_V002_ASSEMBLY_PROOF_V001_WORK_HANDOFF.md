# Opening V002 — Assembly Proof V001 | Work Execution Handoff
Date: 2026-10-31
Status: AUTHORIZED FOR ISOLATED PROOF ONLY / NOT CANONICAL VIDEO APPROVAL
Source state: main R379, Story Shot Index 35; all three Opening P03A/P03B/P04C PO approved, published, verified.

## Goal
Build one reviewable Opening V002 MP4 proof from exactly the three approved images followed by the existing Neil welcome sequence, synchronized to the PO-approved 40.260 second P03/P04→Neil original-audio bridge. Do not replace or edit original Opening V001 or any existing approved video.

## Inputs (exact canonical image files)
- `production/image_library/approved/story_shots/OPENING_P03A_BLOOD_DOOR_ESTABLISH_APPROVED_V001.png` — 941×1672; SHA256 `7aebf80c713389df929b99071f7d48b9f8ce71195b95ae37d9b6efd6c2635884`
- `production/image_library/approved/story_shots/OPENING_P03B_TASK_MAIN_APPROVED_V001.png` — **941×1670**; SHA256 `ad7ae095a11fcce8772c1d2694683bc0f15336294a35bd7a3d12480c6d58e98e`
- `production/image_library/approved/story_shots/OPENING_P04C_HINTS_MAIN_APPROVED_V001.png` — 941×1672; SHA256 `6a00e7a76ed8a7e228dc2ab334e93a7f907b586293a144649773f4f9c29628be`
- Original **private** Drive audio: `OPENING_CONTENT_P03P04_TO_NEIL_WELCOME_AUDIO_PROOF_V001.m4a`, file ID `1kbuay1kxY8Tmnhr880GMtL0hTNdV_AXS` (974875 bytes in Drive metadata), PO approved for listening 2026-10-28. Its duration is 40.260 s according to recorded technical verification.
- Original Opening V001: locate the registered canonical video and source before assembly. Never replace V001.

## Execution / safety
1. Verify image SHA256 locally from GitHub canonical source, Drive audio source identity against prior verified archive hashes, and V001 video provenance. Fail closed on absent/unverified input.
2. **Private original audio must remain private.** Do not commit it, its bytes, public download links, authentication tokens or private transient exports to this public repository or GitHub Actions artifacts. Use an approved private runtime/transfer with authorized access for assembly; public GitHub Actions alone cannot read a private Drive source without an explicitly approved safe access method.
3. Establish actual dialogue-aligned P03A→P03B→P04C→Neil cut times from original audio. No invented, equally split or dialogue-clipping times. Preserve exact audio stream content where feasible; verify decoded audio integrity.
4. Compose still frames with restrained editorial timing (no fake character animation, unnecessary black fades, or new imagery). P03B 2px height discrepancy is handled **only** in derived video canvas via padding/crop/conform; never modify canonical PNG.
5. Output **one proof MP4** to a private review destination; output a compact QC JSON with duration, fps, video dimensions, audio identity/continuity, exact cut timecodes, image source hashes, and any conform choices. If private destination cannot be verified, hold delivery rather than publishing audio publicly.
6. PO judges readability, rhythm, task/warning comprehension, and transition to Neil. No canonical publication / Video Index update / replacement of V001 without explicit PO approval.
7. After PO approval: Chat manages exact proof binary verification, authorized publication strategy, video registration, and Project Control closeout.

## PASS/FAIL
Technical PASS requires verified sources, uninterrupted authentic narration, valid video playback, correct order and aligned cue times; aesthetic PASS additionally requires PO approval. Otherwise FAIL/PENDING; preserve existing assets. No reopening old blood-door A/B project.
