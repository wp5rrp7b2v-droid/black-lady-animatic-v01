# M01 V002 ｜定位与人物保护 Gate 1C 诊断记录（2026-10-17）

**Status:** DIAGNOSTIC COMPLETE; **PRODUCTION REGISTRATION FAIL / HOLD**  
**Source:** approved V006 rough review, source SHA-256 `7af0982385c877b159f053233378b98c2c035ce19df257a6e65077dfbaa33402`  
**Workflow:** GitHub Actions #39012195443 attempt 2 SUCCESS (diagnostic code and artifact, **not** production acceptance).  
**Evidence folder:** `production/environment_dynamic/review_candidates/M01_V002_LIGHT_PERSON_CLUSTER_V003`

## 1. What was actually built

1. Reused original V006 mid-frames of the 7 PO-flagged shots; original PNG, V006 video, Video Index and `main` untouched.
2. YOLO instance-segmentation person mask with 13 px dilation replaces visually over-broad protection rectangles; this is a detected-person mask **only**, not a guarantee against misses.
3. Multi-feature high-luminance/warm-white flame-core candidates grouped into approximate fixture clusters. PO's directional feedback narrows source-search windows; the candidates are **not approved flame positions**.
4. One hypothetical per-source small halo is clipped against detected people. Resulting **person-mask overlap=0 by design**. This does not prove complete human detection, exact flame shape, precise wall receiving-light region, or visible M01 motion.
5. Produced one JPEG contact sheet, JSON QA, and unapproved scene light atlas. No new video or Story Shot.

## 2. Objective inspection results

| Shot | Light source candidates | Remaining defect / action |
| --- | --- | --- |
| N16 | 1/1 candidate | Visual calibration to flame(s); PO said old mask too low |
| N18 | 2/2 search hints both map to **one physical cluster** | Deduplicate source groups, inspect separate flame cores, avoid double modulation |
| N20 | 3/3 candidates | Centers shifted upward toward visible flames; confirm masks |
| NEW-01 | 3/3 candidates; left ambiguous | Left group has alternate plausible candidates; a right-edge crop and background occlusion require review |
| N21 | 2/2 candidates | Right group low score relative to original hint; verify visually |
| A06 | 2/2 candidates | Centers shifted upward relative to old masks; verify architectural lighting |
| N24 | **0/2 accepted candidates** | Bright spots exist but score below confidence threshold; user specifically said right-hand mask too far left. **Hard stop** until localized source geometry is checked |

Total old V007 effect-mask overlaps with independently segmented people (7 diagnostic frames):
- N16: 923 px
- N18: 11,014 px
- N20: 6,582 px
- NEW-01: 37,602 px
- N21: 10,023 px
- A06: 3,010 px
- N24: 14,847 px

These are **single sampled frames**, not full-clip person overlap totals. Pixel intersection is against detection output, not absolute person ground truth.

## 3. Production exit criteria

- Every registered fixture maps to true flame core(s) on actual source frame, not only a bright wood/stone highlight; missing/ambiguous sources require local calibration.
- Each physical fixture gets unique stable `fixture_id`, not one center per guessed elliptical mask and not duplicated when two hints find the same cluster.
- Person/face/wardrobe protected on all rendered frames; segmentation masks are conservative and video-framed; missed-person uncertainty remains a blocker.
- Tested source receiving-light masks cannot cross people; movie A/B must show real independently driven flame motion and nearby architecture response.
- Only after PO reviews evidence and the above gates pass may calibrated atlas profiles become approved and reused in a one-click workflow.
- No V008 full re-render until Gate 1 positioning + human protection approved.

## 4. Next engineering action

Use local adaptive ROI and/or visual calibration to resolve N24 right-hand source and NEW-01 ambiguity, deduplicate N18; then audit dynamic per-frame stability and generate a new overlay for PO approval. Keep `M01.batch_gate_status=HOLD` in the module registry.
