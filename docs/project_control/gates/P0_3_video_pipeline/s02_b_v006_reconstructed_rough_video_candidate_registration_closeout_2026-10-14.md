# S02-B V006｜重构粗剪候选登记 Closeout｜2026-10-14

**FINAL: REGISTERED AS VIDEO CANDIDATE ONLY / PO_REVIEW_PENDING / EXACT GITHUB BINARY VERIFIED / NOT OFFICIAL VIDEO INDEX / NO MAIN MERGE.**

## PO Decision

Product Owner: **「V006先登记为候选，之前关于视频的enhancement，还有哪几点？」**

This decision authorizes a **noncanonical Video Candidate registration only**, not PO full-video visual approval, canonical video publication, master overwrite or merging to main.

## Candidate registration

- Candidate ID: `S02_B_V006_CINEMATIC_ROUGH_RECONSTRUCTED_CANDIDATE_V001`.
- Candidate status: `PO_REVIEW_PENDING`.
- Candidate registry: `production/video_candidates/video_candidate_index.jsonl` (one unique record).
- Persisted original MP4: `production/video_candidates/assets/S02_B_V006_CINEMATIC_ROUGH_RECONSTRUCTED_CANDIDATE_V001.mp4`.
- Review branch: `review/s02b-jun-nod-insert-20261014`.
- Original source render: GitHub Actions Run `38569617657`, Artifact `11897595436`.
- Exact original source MP4 SHA-256: `7af0982385c877b159f053233378b98c2c035ce19df257a6e65077dfbaa33402`.
- Source byte size: **8,712,713**; video **720×1280, 30fps, 1927 frames**; container **64.250s**, AAC **3013 packets**.
- Persisted candidate GitHub blob: **`d92d23ac6b5a542e07572e29a9e648e2c4141854`**.
- Registration Action Run: **`38571991859`** SUCCESS. Added exactly two paths: binary MP4 and candidate registry, in the existing review branch only.
- Independent post-registration verification Run: **`38572320667`** SUCCESS, evidence Artifact **`11897199276`**, digest `sha256:fa3ed99e250399581b364e79ef1bd97640ea069da6dfeac34fd9d9e7409f46c0`.
- Verification confirmed GitHub-stored original MP4 SHA-256, bytes and Git blob; candidate indexed once; NEW-01/NEW-02 original Story Shot blobs remain unchanged; official Video Index Git blob **`84fb0f70ebd92536b95c6b01c6ac69a27a6986c7`** unchanged. main not merged.
- Existing canonical V001 full-video mother remains intact.

**Historical source limitation**: full V005 review MP4 `ffd811370e77293e5f519020d611aeaef37590979d5922d5ce715a1cb508d63c` was not accessible in observed GitHub/Drive records, so V006 is correctly labeled `RECONSTRUCTED_ROUGH_REVIEW_NOT_EXACT_V005`: locked approved V004 N16–N17 658-frame source, subsequent original approved Story Shots, approved V001 continuous AAC packet stream.

## Previously discussed Video Enhancement: disposition / next work

1. **Actual new camera axes, shot-reverse-shot and reaction inserts:** partially implemented. V006 NEW-01 Jun shoulder → Ning warning and NEW-02 crowd side-depth are registered/used; remaining shot diversity should be assessed **after full-context PO review**, not an automatic new still-image batch.
2. **Character performance:** breathing, blink, subtle head turn/gaze, natural walk and cloth response are unresolved. N18 GIF blink local-mask/whole-background continuity experiments failed and are **ON HOLD**; not the default method for V006.
3. **Native audio-driven mouth movement:** still not deployed in V006. Use original voice-only speech as timing reference for an isolated short character-performance pilot; exact lip/identity/face fidelity needs proof; no generated audio replaces novel source.
4. **Environmental movement:** candle flame/flicker, controlled local light changes, distant smoke/air and ambient motion have not been animated. Pilot only at appropriate environmental shots while protecting approved architecture and overall dark exposure.
5. **Physical spatial depth and parallax:** NEW-02 approved still has layered foreground/midground/background composition; actual *moving parallax* is not implemented. Prior still-derived DepthFlow / generic 2.5D figure morph tests were judged unsuitable. Avoid automatic parallax on close faces.
6. **Editorial transition and semantic timing:** N23→A06 on “管家转身,” A06→N24 Guang Yong question, N24→N25 Neil's answer and N25→Ning B V002→N26 need full-context cut rhythm review. V005's uniform five-frame dissolve had not been PO-approved as general grammar; V006 mostly uses motivated clean cuts. Chinese precise word onset remains approximate and requires listening/realignment rather than claiming machine word-level PASS.
7. **Sound enhancement:** distinct antique stone hall room tone, sparse footsteps/cloth, controlled candle ambience and selective J-cut/L-cut/crossfade can improve immersion, but original continuous narration must remain unchanged; extra effects should be separately trialed and PO-reviewed. Original AAC is exactly copied in V006; added SFX not yet adopted.

**Route for future moving shots, not automatically approved**: selected approved Story Shot acts as anchor first frame; controlled Resolver character/environment identity input supports an image-to-video engine limited to per-shot performance; original narration can drive lip sync for speaking shots; editing/rendering stage synchronizes continuous original audio, non-dialogue ambience and transition timing. Prior video-engine approaches need controlled 1-shot pilot due to face/body/background morph risks; current V006 stills alone do not prove image-to-video reliability.

**Disallowed as a primary enhancement:** repetitive digital push/pull, uniform dissolves, same-image crop pretending to be a new angle, failed N18 GIF/character-mask strategy, uncontrolled whole-character 2.5D/DepthFlow deformation.

## Next review gate

Candidate awaiting PO full 64.25s viewing, including the two new cuts and N23→A06→N24. **No automatic V007 enhancement render, no MP4 source replacement, no canonical Video Index change, no main merge** until separate directions.
