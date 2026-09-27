# P0.3 libopenshot Camera Motion Proof V001

Purpose: test whether libopenshot curve-based multi-keyframe motion is visibly more cinematic than the current Remotion V003 single-still motion treatment.

Scope is intentionally limited to three approved canonical Story Shots:

- N08 — architecture attraction: short hold → accelerating push → overshoot → settle
- N03 — reaction observation: pull-back + lateral drift → settle
- N05 — action peak: push + directional reframe + brief settle-shake + micro rotation

This proof is motion-only and intentionally has no program audio. It is not an Opening V2 editorial candidate and must not be used to judge audio alignment.

Rendering path:

canonical PNGs → libopenshot Python bindings / Bezier keyframes → PNG frame sequence → FFmpeg H.264 MP4

No 2.5D depth warp, no character deformation, no Story Shot replacement.
