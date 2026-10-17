#!/usr/bin/env python3
"""M01 V002 seven-direction alignment proposals; no animation / no output video.
Old red masks come from exact V007 script. Cyan targets are PO-directional
candidates ONLY, not automatically registered flame cores.
"""
import base64
import hashlib
import importlib.util
import io
import json
import pathlib
import subprocess

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT=pathlib.Path(__file__).resolve().parents[1]
VIDEO=ROOT/"production/video_candidates/assets/S02_B_V006_CINEMATIC_ROUGH_RECONSTRUCTED_CANDIDATE_V001.mp4"
EDL=ROOT/"production/editorial_specs/S02_B_V006_CINEMATIC_ROUGH_EDL_V001.json"
ENGINE=ROOT/"scripts/s02b_v007_full_m01_with_ab_20261017.py"
OUT=ROOT/"_m01_v002_directional_candidate"
ORIGINAL_SHA="7af0982385c877b159f053233378b98c2c035ce19df257a6e65077dfbaa33402"
# Explicit, non-canonical direction-only estimates from PO visual feedback.
# Delta x/y in normalized frame units. Do NOT regard as exact automatically detected flames.
DELTAS={
 "N16_PART_1":{"0":[0,-.05]},
 "N18":{"0":[.100,-.025],"1":[.065,-.025]},
 "N20_FIRST":{"0":[.075,0],"1":[.060,0],"2":[.105,0]},
 "V006_NEW_01":{"0":[.080,0],"1":[.120,0],"2":[.040,0]},
 "N21":{"0":[-.090,0],"1":[-.045,0]},
 "A06":{"0":[.060,-.085],"1":[.065,-.075]},
 "N24":{"1":[.085,0]},
}
ORDER=list(DELTAS)
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def f(t):
    raw=subprocess.check_output(["ffmpeg","-hide_banner","-loglevel","error",
      "-ss",f"{t:.6f}","-i",str(VIDEO),"-frames:v","1","-f","image2pipe","-vcodec","mjpeg","-"])
    return Image.open(io.BytesIO(raw)).convert("RGB").resize((720,1280))
def oldmask(sid,m):
    return m.manual_mask(m.ANCHORS[sid])
def getfont(size):
    for path in ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",):
        if pathlib.Path(path).exists():return ImageFont.truetype(path,size)
    return ImageFont.load_default()
def main():
    assert sha(VIDEO)==ORIGINAL_SHA
    spec=importlib.util.spec_from_file_location("v007_render",str(ENGINE))
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    seq={s["id"]:s for s in json.loads(EDL.read_text())["timeline"]}
    assert all(s in seq for s in ORDER)
    W=1060; panel_w=515; panel_h=550; row_h=588
    canvas=Image.new("RGB",(W,len(ORDER)*row_h),(14,14,15))
    draw=ImageDraw.Draw(canvas)
    labels=getfont(21)
    small=getfont(14)
    rows=[]
    for i,sid in enumerate(ORDER):
        shot=seq[sid]
        middle=(shot["start_frame"]+(shot["end_frame_exclusive"]-shot["start_frame"]-1)/2+.5)/30
        frame=f(middle)
        crop=frame.crop((0,0,720,760))
        base=np.array(frame)
        mask=oldmask(sid,mod)
        base[mask>.08]=(base[mask>.08].astype(np.float32)*.44+np.array([255,24,37])*.56).astype(np.uint8)
        old=Image.fromarray(base).crop((0,0,720,760)).resize((panel_w,panel_h),Image.Resampling.LANCZOS)
        proposed=crop.resize((panel_w,panel_h),Image.Resampling.LANCZOS)
        pd=ImageDraw.Draw(proposed)
        anchors=[]
        for j,(x,y,sx,sy) in enumerate(mod.ANCHORS[sid]):
            dx,dy=DELTAS[sid].get(str(j),(0,0))
            nx,ny=x+dx,y+dy
            assert .01<nx<.99 and .01<ny<.45
            # Small center ring to inspect source registration, NOT an approved effect mask.
            xx=nx*panel_w; yy=ny*1280*(panel_h/760)
            r=10
            pd.ellipse((xx-r,yy-r,xx+r,yy+r),outline=(25,245,234),width=3)
            pd.line((xx-16,yy,xx+16,yy),fill=(25,245,234),width=2)
            pd.line((xx,yy-16,xx,yy+16),fill=(25,245,234),width=2)
            pd.text((xx+12,yy-20),str(j+1),font=small,fill="white",
                    stroke_width=2,stroke_fill=(0,0,0))
            anchors.append({"source_index":j+1,"old_normalized_center":[x,y],
                "suggested_normalized_center":[round(nx,4),round(ny,4)],
                "normalized_delta":[dx,dy],"proposed_status":"DRAFT_CALIBRATION_PENDING"})
        y0=i*row_h
        canvas.paste(old,(0,y0+30))
        canvas.paste(proposed,(545,y0+30))
        draw.text((8,y0+4),f"{i+1:02d} {sid} / old V007 red",font=labels,fill="white")
        draw.text((545,y0+4),"DRAFT proposed cyan centers",font=labels,fill="white")
        rows.append({"shot":sid,"mid_time_seconds":round(middle,3),
                     "status":"NOT_LIGHT_ALIGNMENT_APPROVED",
                     "manual_adjustments":anchors})
    OUT.mkdir(parents=True,exist_ok=True)
    p=OUT/"M01_V002_SEVEN_SHOT_DIRECTIONAL_ALIGNMENT_DRAFT_V001.jpg"
    canvas.save(p,"JPEG",quality=84,optimize=True)
    (OUT/"M01_V002_SEVEN_SHOT_DIRECTIONAL_ALIGNMENT_DRAFT_V001.jpg.b64.txt").write_text(
        base64.b64encode(p.read_bytes()).decode()+"\n")
    report={
        "gate":"M01_V002_SEVEN_SHOT_DIRECTIONAL_CALIBRATION_DRAFT",
        "status":"DRAFT_REQUIRES_VISUAL_ALIGNMENT_AND_HUMAN_PROTECTION_APPROVAL",
        "source_sha256":ORIGINAL_SHA,
        "affected_shots":ORDER,
        "interpretation":"PO notes describe old mask offset; candidate shifts are opposite direction",
        "mask_geometry":"old red = original V007 mask; cyan = candidate point, not an approved mask",
        "person_protection_gate":"FAILED_NOT_YET_REMEDIATED",
        "confidence":"NOT_MEASURED",
        "fully_automatic_batch_authorized":False,
        "v007_or_any_video_changed":False,
        "source_video_unchanged":True,
        "overlay_file":p.name,
        "overlay_sha256":sha(p),
        "candidates":rows
    }
    (OUT/"M01_V002_SEVEN_SHOT_DIRECTIONAL_ALIGNMENT_DRAFT_V001.json").write_text(
        json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print("M01_V002_DIRECTIONAL_PROPOSALS=7")
    print("NO_FLAME_REGISTRATION_PASS_CLAIM=TRUE")
    print("NO_VIDEO_RENDER=TRUE")
    print("OVERLAY_SHA256",report["overlay_sha256"])
if __name__=="__main__":
    main()
