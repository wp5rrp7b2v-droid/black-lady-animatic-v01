# Opening V002 Assembly Proof V003 — Editorial QC, 2026-10-31

Status: **TECHNICAL PASS / PRODUCT OWNER VISUAL REVIEW PENDING**.

This is an isolated review derivative; official Opening V001 and registered Story Shots are unchanged. V003 corrects **only** P04-C visual hold from 15.5 to 15.0 seconds and extends the subsequent approved Opening visual extract to maintain total duration and unchanged audio.

## Exact output evidence
- File: `OPENING_V002_ASSEMBLY_PROOF_V003_PO_REVIEW.mp4` (private session delivery; **not published to GitHub and not registered as canonical**).
- SHA256: `60a7127cabd4f6a73c45a131cf634f966ee9985fca5f19d4028e4a7796345d1c`.
- Bytes: 4,180,381; 1080×1920; 30fps; 1208 frames; H.264 + AAC; container 40.266667 s.
- Original approved 40.260s audio binary unchanged; decoded PCM in output is **bit-identical** to source, SHA256 `896b1b7ec03fc7fc45e5fd0f98a7967fe9b8fcf4d81c53ca7873ba08fb462717`.
- Audio stays private (Drive `1kbuay1kxY8Tmnhr880GMtL0hTNdV_AXS`), no public Github audio/media publication.
- Timings: P03A [0,3), P03B [3,18), P04C [18,33), original Opening Neil [33,40.266667); original Opening visual extraction starts +0.2s to skip its darkest first few frames.
- The sound narrative crosses to Neil at roughly 33.689 s; the `33.0` cut starts the next visual slightly ahead of speech (visual lead-in). This is an editorial cut, **not** verified word-level sync.
- The observed original Opening first exterior visual is noticeably softer than newly approved stills; this revision does not claim image resolution restoration.

## New Product Owner review observation (not a new design approval)

Product Owner asked whether the opening "has no sense of an opening". The current proof indeed starts directly with two characters already at the blood door, then task text and two warnings, with no prior contract/arrival context. **Working interpretation:** missing narrative lead-in (previously designed P01/P02 beats), not a mere transition or title defect.

**Recommended next small proof, not yet authorized**: verify availability of a short, authentic, story-grounded P01/P02 contract/arrival lead-in, then test an introductory beat before P03A rather than adding cosmetic black fades or generic title cards. Preserve approved P03A/P03B/P04C and audio until separately approved. Do not infer missing original P01 audio or invent dialogue.

## Gate
Pending PO assessment of V003 timing and separate approval of any new opening content; no formal Master replacement, no Video Index change.

## 2026-10-31 | P01 minimal narrative-entry audio test (not V004 video)

Original CH133 source privately fetched and exact SHA-256 checked: `26d41ab241228f0de10531ceb6e67129f530a25589aa89a4c3417b884b7b9b20` (duration `290.689002s`).
Source's first ~11 seconds contains partial P01 companion/context narration; original key quote `我带你吧` precedes source start and remains **unavailable**. P02 contract event takes about `02:08–03:28`; it is not demonstrably compressible to 4 seconds.

A **sound-only**, provisional, one-path minimum test was created from original CH133 `[0,11.57)` (cut near measured low-amplitude `11.489–11.667s`) followed by the unchanged-in-content previously PO-approved `40.260s` P03/P04→Neil audio bridge. Encoding necessarily converts CH133 44.1kHz and existing bridge 48kHz to a single new 48kHz AAC stream; it does **not** preserve the approved bridge exact bytes and is **not** canonical audio.
- Review asset: `OPENING_P01_MINIMUM_AUDIO_INTRO_PROOF_V001.m4a`, SHA256 `d792512aa9eeb84788c8940d28060ca75398c82d7fb10c0e756fc27c2156b593`; 1,257,886 bytes; 51.847s; decode PASS.
- Private ChatGPT Library folder: `/诡舍-黑衣夫人/Opening音频试验/`; no copyrighted sound uploaded to public GitHub.
- **Purpose**: falsify/test whether a short P01 context opening actually helps before P03 task without new media/character artwork, and whether the omission of P02 creates an unacceptable jump. This is exploratory **not** a cancellation or modification of PO-approved P01/P02→P03/P04 narrative baseline.
- **Unknown**: exact word-level boundary at 11.57s; semantic/audio continuity and opening effect require PO listening.
- Next decision: If the isolated hook fails because P02 is necessary, verify a genuinely cuttable P02 original-audio mini-beat or request missing earlier P01 voice excerpt before building any new Story Shot. If a hook passes, still seek PO design approval before new images/video. No changes to original V001, V003, Story Shot Index, P0.3 Gate or video register.
