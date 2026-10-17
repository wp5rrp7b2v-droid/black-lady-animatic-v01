#!/usr/bin/env python3
"""Stage A1: priority-source evidence plates, machine masks and review drafts.
No rendering, no approved ground truth, never alter source frames.
"""
import base64, hashlib, io, json, pathlib, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT=pathlib.Path(__file__).resolve().parents[1]
SPEC=ROOT/"production/environment_dynamic/benchmarks/m01_stage_a_v002/M01_STAGE_A_CASE_SPEC_V002.json"
BENCH=ROOT/"production/environment_dynamic/benchmarks/m01_stage_a_v002/evidence/M01_STAGE_A_MACHINE_BENCHMARK_V002.json"
EVIDENCE=BENCH.parent
INPUT=ROOT/"production/video_candidates/assets/S02_B_V006_CINEMATIC_ROUGH_RECONSTRUCTED_CANDIDATE_V001.mp4"
OUT=ROOT/"_m01_stage_a1_priority_calibration"
W,H=720,1280
SIDS=["N24","V006_NEW_01","N18"]
WANTED=["first","middle","last"]
def sha(b):
    return hashlib.sha256(b).hexdigest()
def font(s):
    path="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(path,s) if pathlib.Path(path).exists() else ImageFont.load_default()

def grab_exact(indices):
    assert len(indices)==len(set(indices))
    indices=sorted(indices)
    selector="+".join(f"eq(n\\,{x})" for x in indices)
    p=subprocess.Popen(["ffmpeg","-hide_banner","-loglevel","error","-xerror","-i",str(INPUT),
        "-map","0:v:0","-vf","select="+selector,"-vsync","vfr","-pix_fmt","rgb24",
        "-f","rawvideo","pipe:1"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    frames={}
    size=W*H*3
    try:
        for i in indices:
            all_bytes=p.stdout.read(size)
            assert len(all_bytes)==size,f"SHORT_{i}"
            frames[i]=all_bytes
        assert p.stdout.read(1)==b""
    finally:
        p.stdout.close()
    err=p.stderr.read().decode(errors="replace");p.stderr.close()
    assert p.wait()==0,err[-400:]
    return frames

def crop_top(src,mask=None,centers=None):
    # work at 2x source pixels and include 0..38% height, making all candle cores easy to mark.
    y_end=510
    im=Image.fromarray(src,"RGB").crop((0,0,W,y_end)).resize((1080,765),Image.Resampling.NEAREST)
    if mask is not None:
        m=Image.fromarray(mask,"L").crop((0,0,W,y_end)).resize((1080,765),Image.Resampling.NEAREST)
        r=np.asarray(im).copy();human=np.asarray(m)>0
        r[human]=(r[human].astype(np.float32)*.50+np.array([28,103,241])*.50).astype("uint8")
        im=Image.fromarray(r)
    d=ImageDraw.Draw(im)
    # 0.1 grid guides reviewed coordinates, not localization truth.
    for x in range(0,W+1,72):
        px=round(x*1.5)
        d.line((px,0,px,765),fill=(255,255,255,35),width=1)
        d.text((px+3,3),str(x),font=font(17),fill=(220,230,230),stroke_width=1,stroke_fill="black")
    for y in range(0,y_end,64):
        py=round(y*1.5)
        d.line((0,py,1080,py),fill=(255,255,255,35),width=1)
        d.text((5,py+3),str(y),font=font(17),fill=(220,230,230),stroke_width=1,stroke_fill="black")
    for j,center in enumerate(centers or []):
        x=round(center[0]*W*1.5);y=round(center[1]*H*1.5)
        if y>=765:continue
        d.ellipse((x-11,y-11,x+11,y+11),outline=(255,30,198),width=4)
        d.line((x-18,y,x+18,y),fill=(255,30,198),width=3)
        d.line((x,y-18,x,y+18),fill=(255,30,198),width=3)
        d.text((max(5,min(x+16,1000)),max(18,y-26)),f"P{j+1}",
            font=font(22),fill="white",stroke_width=2,stroke_fill="black")
    return im

def person_full(src,mask):
    pic=Image.fromarray(src,"RGB")
    m=Image.fromarray(mask,"L")
    tinted=np.asarray(pic).copy()
    selected=np.asarray(m)>0
    tinted[selected]=(tinted[selected].astype("float32")*.55+np.array([31,112,250])*.45).astype("uint8")
    return Image.fromarray(tinted,"RGB").resize((720,1280),Image.Resampling.LANCZOS)

def main():
    spec=json.loads(SPEC.read_text());record=json.loads(BENCH.read_text())
    assert sha(INPUT.read_bytes())==spec["source_video_sha256"]
    by={s["shot_id"]:s for s in record["samples"]}
    assert set(SIDS).issubset(by)
    wanted={f["frame_index"] for sid in SIDS for f in by[sid]["frames"]}
    rawframes=grab_exact(wanted)
    OUT.mkdir(parents=True,exist_ok=True)
    candidates=[]
    for sid in SIDS:
        item=by[sid]
        source_points=[s["center"] for s in item["source_core_proposals"] if s["center"] is not None]
        fileprefix="M01_A1_"+sid
        plate=Image.new("RGB",(2190,3*835),(14,14,16))
        d=ImageDraw.Draw(plate)
        cases=[]
        for i,f in enumerate(item["frames"]):
            frameindex=f["frame_index"];raw=rawframes[frameindex]
            assert sha(raw)==f["decoded_rgb_sha256"],f"EXACT_SOURCE_FRAME_IDENTITY_{sid}_{frameindex}"
            src=np.frombuffer(raw,dtype=np.uint8).reshape(H,W,3)
            maskpath=EVIDENCE/f["person_mask_proposal"]
            assert sha(maskpath.read_bytes())==f["person_mask_sha256"]
            mask=np.asarray(Image.open(maskpath).convert("L"))
            assert mask.shape==(H,W)
            clean=crop_top(src)
            overlay=crop_top(src,mask,source_points if i==1 else [])
            y0=i*835
            plate.paste(clean,(4,y0+56));plate.paste(overlay,(1100,y0+56))
            d.text((6,y0+6),f"{sid} | F{frameindex} | FLAME CORES RAW SOURCE - left",font=font(24),fill="white")
            d.text((1102,y0+6),"BLUE PERSON PROPOSAL + MAGENTA OLD CORE HINTS - right",font=font(19),fill="white")
            cases.append({
                "frame_index":frameindex,
                "decoded_rgb_sha256":f["decoded_rgb_sha256"],
                "person_mask_path":f["person_mask_proposal"],
                "person_mask_sha256":f["person_mask_sha256"],
                "human_protection_ground_truth":"PENDING",
                "flame_core_ground_truth":"PENDING",
                "source_status":"UNVERIFIED_VISUAL_CALIBRATION" })
        jpg=OUT/(fileprefix+"_THREE_FRAMES_ZOOM_V001.jpg")
        plate.save(jpg,"JPEG",quality=82,optimize=True)
        b64=OUT/(jpg.name+".b64.txt")
        b64.write_text(base64.b64encode(jpg.read_bytes()).decode()+"\n")
        # Separate mid-frame double panel keeps GitHub text transport below large-file limits.
        midplate=plate.crop((0,835,2190,1670))
        midfile=OUT/(fileprefix+"_MIDFRAME_ZOOM_V001.jpg")
        midplate.save(midfile,"JPEG",quality=81,optimize=True)
        (OUT/(midfile.name+".b64.txt")).write_text(base64.b64encode(midfile.read_bytes()).decode()+"\n")
        # Full-frame person review at one sampled frame, distinct to top zoom.
        mid=item["frames"][1];fr=mid["frame_index"]
        src=np.frombuffer(rawframes[fr],dtype=np.uint8).reshape(H,W,3)
        pm=np.array(Image.open(EVIDENCE/mid["person_mask_proposal"]).convert("L"))
        person=person_full(src,pm)
        perimg=OUT/(fileprefix+"_PERSON_FULLFRAME_MID_V001.jpg")
        person.save(perimg,"JPEG",quality=78,optimize=True)
        (OUT/(perimg.name+".b64.txt")).write_text(base64.b64encode(perimg.read_bytes()).decode()+"\n")
        candidates.append({"shot":sid,"source_type":"V006_LOCKED_EXACT_FRAMES",
             "source_proposals":item["source_core_proposals"],
             "three_sample_frames":cases,
             "zoom_plate":jpg.name,"zoom_plate_sha256":sha(jpg.read_bytes()),
             "person_fullframe":perimg.name,"person_fullframe_sha256":sha(perimg.read_bytes()),
             "mid_zoom":midfile.name,"mid_zoom_sha256":sha(midfile.read_bytes()),
             "source_geometry_approved":False,
             "human_protection_approved":False,
             "calibration_work_queue":"Use source flames visible in left panels, not magenta hints; verify all visible people incl hair, faces, clothing, background."})
    output={
       "schema":"M01_STAGE_A1_PRIORITY_CALIBRATION_EVIDENCE_V001",
       "status":"EVIDENCE_BUILT_VISUAL_LABELS_NOT_YET_APPROVED",
       "source_video_sha256":spec["source_video_sha256"],
       "stage_A_spec_sha256":sha(SPEC.read_bytes()),
       "stage_A_machine_benchmark_sha256":sha(BENCH.read_bytes()),
       "priority_shots":SIDS,
       "image_markings":"left source exact pixels; right YOLO human protection blue and previous experiment PO-unverified magenta source hints",
       "no_video_rendered":True,"no_main_merge":True,
       "person_masks_not_ground_truth":True,"light_proposals_not_ground_truth":True,
       "cases":candidates}
    j=OUT/"M01_STAGE_A1_PRIORITY_CALIBRATION_EVIDENCE_V001.json"
    j.write_text(json.dumps(output,indent=2,ensure_ascii=False)+"\n")
    print("M01_A1_PRIORITY_SOURCE_EVIDENCE_READY",json.dumps({
        "shots":len(SIDS),"frames":len(wanted),"plates":len(candidates),
        "label_approval":False,
        "source_frames_hash_validated":True,
        "person_ground_truth":False,"flame_ground_truth":False}))
if __name__=="__main__":
    main()
