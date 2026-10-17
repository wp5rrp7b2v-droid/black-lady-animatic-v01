#!/usr/bin/env python3
"""N17 A1 bounded QA: revisit 35 threshold warnings and F520..F550 onset only.

Review-only: reuses the 377-frame JSON and its exact V006 source.
No segmentation model rerun, no repaint, no new video, no label promotion.
"""
from __future__ import annotations
import hashlib,io,json,pathlib,subprocess
import numpy as np
from PIL import Image,ImageDraw,ImageFont
import base64

ROOT=pathlib.Path(__file__).resolve().parents[1]
BASE=ROOT/"production/environment_dynamic/benchmarks/m01_stage_a_v002"
QA=BASE/"a1_n17_full_frame_masks_v001/M01_A1_N17_ALL_377_FRAMES_PROTECTION_FLAME_QA_V001.json"
SOURCE=ROOT/"production/video_candidates/assets/S02_B_V006_CINEMATIC_ROUGH_RECONSTRUCTED_CANDIDATE_V001.mp4"
OUT=ROOT/"_m01_a1_n17_targeted_qc_v001"
W,H=720,1280
ONSET=list(range(520,551))
WARN_SAMPLES=[550,568,580,590,600,604,610,630]
SHOW_ONSET=[520,525,530,535,540,544,547,550]
SHOW_EXTRA=[568,580,590,600,604,610,630]
SHA="7af0982385c877b159f053233378b98c2c035ce19df257a6e65077dfbaa33402"

def digest(path):
    h=hashlib.sha256()
    with path.open("rb") as p:
        for x in iter(lambda:p.read(1048576),b""): h.update(x)
    return h.hexdigest()

def font(size):
    p="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(p,size) if pathlib.Path(p).is_file() else ImageFont.load_default()

def exact_frames(targets):
    ordered=sorted(set(targets))
    expr="+".join(f"eq(n\\,{i})" for i in ordered)
    run=subprocess.Popen(["ffmpeg","-hide_banner","-loglevel","error","-xerror",
      "-i",str(SOURCE),"-map","0:v:0","-vf","select="+expr,
      "-vsync","vfr","-pix_fmt","rgb24","-f","rawvideo","pipe:1"],
      stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    n=W*H*3
    output={}
    try:
        for frame_idx in ordered:
            fragments=[];remaining=n
            while remaining:
                b=run.stdout.read(remaining)
                if not b:raise RuntimeError(f"FRAME_DECODE_TRUNCATED_{frame_idx}")
                fragments.append(b);remaining-=len(b)
            raw=b"".join(fragments)
            output[frame_idx]=(np.frombuffer(raw,dtype=np.uint8).reshape((H,W,3)).copy(),hashlib.sha256(raw).hexdigest())
        assert run.stdout.read(1)==b"", "UNEXPECTED_SELECTED_FRAMES"
    finally:
        run.stdout.close()
    err=run.stderr.read().decode("utf-8",errors="replace")
    run.stderr.close()
    assert run.wait()==0,err[-800:]
    return output

def flame_area_diagnostics(q):
    active=[row for row in q["frames"] if 550<=row["frame_index"]<=657]
    assert len(active)==108
    warnings=[r for r in active if any(p["core_size_and_visibility_needs_visual_review"] for p in r["flame_core_proposals"])]
    assert len(warnings)==35
    stats=[]
    for i in range(4):
        area=[row["flame_core_proposals"][i]["proposed_core_pixels"] for row in active]
        xy=[row["flame_core_proposals"][i]["proposed_core_centroid_px"] for row in active]
        jumps=[abs(area[j]-area[j-1]) for j in range(1,len(area))]
        moves=[float(np.linalg.norm(np.array(xy[j])-np.array(xy[j-1]))) for j in range(1,len(xy))]
        hits=sum(v>150 for v in area)
        stats.append({"flame":i+1,"pixels_min":min(area),"pixels_max":max(area),
          "frames_over_legacy_150_px":hits,
          "largest_one_frame_pixel_area_change":max(jumps),
          "largest_one_frame_centroid_displacement_px":round(max(moves),4),
          "any_flame_core_missing":any(v==0 for v in area),
          "interpretation":"Old 150px bound triggered; bounded smoothness does not prove shape correctness."})
    return warnings,stats

def positive_core_metric(rgb,core_roi=(595,0,720,125)):
    # Pixel metric is a diagnostic clue, NOT first-visible-frame ground truth:
    # reject bright grey sky by requiring strong warm chroma and high luminance.
    x0,y0,x1,y1=core_roi
    r=rgb[y0:y1,x0:x1,:].astype(np.int16)
    rr,gg,bb=r[:,:,0],r[:,:,1],r[:,:,2]
    warm=(rr>=204)&(gg>=149)&(rr-gg>=-12)&(gg-bb>=19)&(rr-bb>=29)
    return int(warm.sum())

def draw_tiles(rows,frames,title,filename):
    # original right-upper frame crop, 2x larger. No legacy masks on actual source.
    cellw,cellh=580,620
    cols=4
    image=Image.new("RGB",(cols*cellw,((len(rows)+cols-1)//cols)*cellh),(15,15,16))
    dr=ImageDraw.Draw(image)
    for i,frame_idx in enumerate(rows):
        rgb,_=frames[frame_idx]
        source=Image.fromarray(rgb,"RGB")
        # Keep wall region and complete vertical context around top-right fixture.
        roi=source.crop((485,0,720,250)).resize((540,572),Image.Resampling.NEAREST)
        x=(i%cols)*cellw+15
        y=(i//cols)*cellh+36
        image.paste(roi,(x,y))
        dr.text((x,y-31),f"F{frame_idx} | {(frame_idx+.5)/30:.3f}s",font=font(24),fill="white")
    dest=OUT/filename
    image.save(dest,"JPEG",quality=88,optimize=True)
    (OUT/(filename+".b64.txt")).write_text(base64.b64encode(dest.read_bytes()).decode()+"\n")
    return {"file":filename,"sha256":digest(dest),"description":title}

def main():
    assert digest(SOURCE)==SHA
    q=json.loads(QA.read_text())
    assert q["source_video_sha256"]==SHA and q["source_frame_count"]==377
    warnings,per_flame=flame_area_diagnostics(q)
    # Restrict actual source frame decoding to needed 31-frame entry window and 7
    # representative warning/normal cases. No full 377-frame model rerun.
    images=exact_frames(ONSET+SHOW_EXTRA)
    assert images[550][1]==next(x for x in q["frames"] if x["frame_index"]==550)["decoded_source_rgb_sha256"]
    for frame_idx in SHOW_EXTRA:
        assert images[frame_idx][1]==next(x for x in q["frames"] if x["frame_index"]==frame_idx)["decoded_source_rgb_sha256"]
    onset=[{"frame":i,"time_seconds":round((i+.5)/30,3),
            "warm_high_luminance_pixels_in_fixed_right_sconce_ROI":positive_core_metric(images[i][0]),
            "rgb_sha256":images[i][1],
            "first_visible_human_confirmed":False} for i in ONSET]
    OUT.mkdir(parents=True,exist_ok=True)
    sheets=[
      draw_tiles(SHOW_ONSET,images,"Exact source candle appearance, 8 sampled frames F520..F550","M01_N17_ONSET_F520_F550_EIGHT_FRAME_SOURCE_V001.jpg"),
      draw_tiles(WARN_SAMPLES,images,"Legacy 150px cutoff examples F550,F568,F580,F590,F600,F604,F610,F630","M01_N17_LEGACY_THRESHOLD_WARNING_EXAMPLES_V001.jpg")
    ]
    details={
      "schema":"M01_STAGE_A1_N17_TARGETED_QA_V001",
      "source_sha256":SHA,
      "previous_377_frame_audit_sha256":digest(QA),
      "status":"TARGETED_REVIEW_COMPLETE_MACHINE_QA_ONLY",
      "old_warning_frame_count":len(warnings),
      "old_warning_frames":[r["frame_index"] for r in warnings],
      "dominant_cause":"FIXED_150_PIXEL_CANDLE_CORE_SIZE_THRESHOLD",
      "per_flame_stats":per_flame,
      "no_missing_flame_masks_in_F550_F657":all(not v["any_flame_core_missing"] for v in per_flame),
      "frame_to_frame_size_and_centroid_continuity_is_not_segmentation_accuracy":True,
      "warning_resolution":"CLASSIFY_AS_THRESHOLD_WARNING_PENDING_VISUAL_SHAPE_REVIEW; DO_NOT_REPROCESS_35_SEPARATELY",
      "image_QA_sample_count":len(WARN_SAMPLES),
      "onset_inspection_window":"F520_F550",
      "onset_pixel_evidence_roi":[595,0,720,125],
      "onset_warm_pixel_metric_is_not_flame_specific":True,
      "onset_visual_annotation_approved":False,
      "exact_onset_frame":"UNDETERMINED",
      "onset_samples":onset,
      "contact_sheets":sheets,
      "previous_n17_PO_approval_scope":"F601 four source center points only",
      "person_masks_reused_unchanged":True,
      "no_new_human_segmentation_rerun":True,
      "no_video_rendered":True,
      "no_GT_promotion":True,
      "m01_batch_gate":"HOLD",
      "no_main_merge":True}
    (OUT/"M01_N17_TARGETED_35_WARNINGS_AND_ONSET_QA_V001.json").write_text(json.dumps(details,ensure_ascii=False,indent=2)+"\n")
    assert digest(SOURCE)==SHA
    print("N17_TARGETED_A1_WARNING_AND_ONSET_PASS",json.dumps({
        "warn_count":len(warnings),
        "per_flame":per_flame,
        "onset_range":[min(onset,key=lambda x:x["warm_high_luminance_pixels_in_fixed_right_sconce_ROI"]),
                        max(onset,key=lambda x:x["warm_high_luminance_pixels_in_fixed_right_sconce_ROI"])],
        "source_check":"EXACT","m01_batch":"HOLD"},ensure_ascii=False))
if __name__=="__main__":main()
