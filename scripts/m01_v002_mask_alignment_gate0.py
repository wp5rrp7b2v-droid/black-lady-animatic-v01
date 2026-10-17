#!/usr/bin/env python3
"""Gate 0 diagnostic only: overlay V007 M01 masks onto actual V006 source frames.
Never equate estimated mask positions to proven flame registration.
"""
import hashlib
import importlib.util
import io
import json
import pathlib
import subprocess

import numpy as np
from PIL import Image, ImageDraw

ROOT=pathlib.Path(__file__).resolve().parents[1]
VIDEO=ROOT/"production/video_candidates/assets/S02_B_V006_CINEMATIC_ROUGH_RECONSTRUCTED_CANDIDATE_V001.mp4"
EDL=ROOT/"production/editorial_specs/S02_B_V006_CINEMATIC_ROUGH_EDL_V001.json"
ENGINE=ROOT/"scripts/s02b_v007_full_m01_with_ab_20261017.py"
OUT=ROOT/"_m01_v002_gate0"
EXPECTED="7af0982385c877b159f053233378b98c2c035ce19df257a6e65077dfbaa33402"
COLS=4
CELL_W,CELL_H=324,608
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def getframe(t):
    blob=subprocess.check_output(["ffmpeg","-hide_banner","-loglevel","error",
        "-ss",f"{t:.6f}","-i",str(VIDEO),"-frames:v","1",
        "-f","image2pipe","-vcodec","mjpeg","-"])
    return Image.open(io.BytesIO(blob)).convert("RGB").resize((720,1280))
def main():
    assert digest(VIDEO)==EXPECTED
    spec=importlib.util.spec_from_file_location("existing_v007",str(ENGINE))
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    timeline=json.loads(EDL.read_text())["timeline"]
    assert len(timeline)==17
    sheet=Image.new("RGB",(COLS*CELL_W,5*CELL_H),(8,8,9))
    pen=ImageDraw.Draw(sheet)
    facts=[]
    for i,seg in enumerate(timeline):
        sid=seg["id"]
        t=(seg["start_frame"]+(seg["end_frame_exclusive"]-seg["start_frame"]-1)/2+.5)/30
        frame=getframe(t)
        mask=(module.new02_mask() if sid=="V006_NEW_02" else
              module.n23_mask() if sid=="N23" else module.manual_mask(module.ANCHORS[sid]))
        assert mask.shape==(1280,720)
        original=np.array(frame)
        overlay=original.copy()
        ink=mask>.10
        overlay[ink]=(original[ink]*.43+
            np.array([255,25,40],dtype=float)*.57).astype("uint8")
        img=Image.fromarray(overlay).resize((316,562),Image.Resampling.LANCZOS)
        ix=(i%COLS)*CELL_W; iy=(i//COLS)*CELL_H
        sheet.paste(img,(ix+4,iy+32))
        pen.text((ix+5,iy+5),f"{i+1:02d} {sid}",fill="white")
        count=int(np.count_nonzero(mask))
        pen.text((ix+5,iy+18),f"t={t:.2f}s; mask={count/(720*1280)*100:.1f}%",fill="white")
        facts.append({
            "node":sid,"sample_time_seconds":round(t,3),
            "mask_pixels":count,"mask_pct":round(count/(720*1280)*100,3),
            "light_geometry_grounding":"V007_ESTIMATED_NOT_CALIBRATED",
            "visual_alignment":"REQUIRES_VISUAL_CHECK",
            "flame_core_mask_present":False,
            "flame_movement_supported_by_v007":False,
            "overlay_color":"RED denotes old V007 effect mask, not detected flame",
            "manual_source_anchors":module.ANCHORS[sid] if isinstance(module.ANCHORS[sid],list) else "legacy per-shot custom mask",
        })
    OUT.mkdir(parents=True,exist_ok=True)
    imagepath=OUT/"S02B_V007_M01_MASKS_ON_REAL_FRAMES_GATE0_V001.jpg"
    sheet.save(imagepath,"JPEG",quality=84,optimize=True)
    report={
        "gate":"M01_V002_ALIGNMENT_GATE0",
        "status":"PRELIMINARY_DIAGNOSTIC_ONLY__NOT_LIGHT_REGISTRATION_PASS",
        "baseline_sha256":EXPECTED,
        "source_frames_extracted_from_original_V006":True,
        "no_new_image_generation":True,
        "visible_red_masks":"EXISTING_V007_WALL_AND_LIGHT_MASKS",
        "proven_flame_core_positions":0,
        "per_shot_automatic_reuse_authorized":False,
        "no_video_created":True,
        "no_main_merge":True,
        "sheet_file":imagepath.name,
        "sheet_sha256":digest(imagepath),
        "nodes":facts}
    (OUT/"S02B_V007_M01_MASK_ALIGNMENT_GATE0_V001.json").write_text(
        json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print("M01_V002_GATE0_DIAGNOSTIC_CREATED")
    print("LIGHT_REGISTRATION_PASS=FALSE")
    print("VISUAL_REVIEW_REQUIRED=TRUE")
    print("SHEET_SHA256",report["sheet_sha256"])
if __name__=="__main__":main()
