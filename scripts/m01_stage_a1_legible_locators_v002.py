#!/usr/bin/env python3
"""M01 A1 V002 - legible candidate locator overlays for 8 pending shots.

Displays PRE-EXISTING UNVERIFIED location suggestions, not newly measured
flame cores. 8 exact mid frames except N17 last for visible light transition.
Source video, machine people masks, and original review JPEGs remain unchanged.
"""
import base64,hashlib,io,json,pathlib,subprocess
import numpy as np
from PIL import Image,ImageDraw,ImageFont

ROOT=pathlib.Path(__file__).resolve().parents[1]
BASE=ROOT/"production/environment_dynamic/benchmarks/m01_stage_a_v002"
SOURCE=ROOT/"production/video_candidates/assets/S02_B_V006_CINEMATIC_ROUGH_RECONSTRUCTED_CANDIDATE_V001.mp4"
MANIFEST=BASE/"evidence/M01_STAGE_A_MACHINE_BENCHMARK_V002.json"
OUT=ROOT/"_m01_a1_legible_locators_v002"
W,H=720,1280
SIDS=["N16_PART_1","N20_FIRST","N21","A06","N23","V006_NEW_02","N16_PART_2","N17"]
MAGENTA=(255,21,205)
def sha(x):
    h=hashlib.sha256()
    if isinstance(x,(str,pathlib.Path)):
        with pathlib.Path(x).open("rb") as f:
            for b in iter(lambda:f.read(1048576),b""):h.update(b)
    else:h.update(x)
    return h.hexdigest()
def font(size):
    p="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(p,size) if pathlib.Path(p).exists() else ImageFont.load_default()
def exact(indices):
    ordered=sorted(set(indices))
    exp="+".join(f"eq(n\\,{idx})" for idx in ordered)
    p=subprocess.Popen(["ffmpeg","-hide_banner","-v","error","-xerror","-i",str(SOURCE),
       "-map","0:v:0","-vf","select="+exp,"-vsync","vfr",
       "-pix_fmt","rgb24","-f","rawvideo","pipe:1"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    size=W*H*3
    results={}
    try:
        for index in ordered:
            parts=[];n=size
            while n:
                b=p.stdout.read(n)
                if not b:raise RuntimeError("SHORT_FRAME_"+str(index))
                n-=len(b);parts.append(b)
            raw=b"".join(parts)
            results[index]=(np.frombuffer(raw,dtype=np.uint8).reshape(H,W,3).copy(),sha(raw))
        assert p.stdout.read(1)==b""
    finally:p.stdout.close()
    stderr=p.stderr.read().decode(errors="replace")
    p.stderr.close()
    assert p.wait()==0,stderr[-400:]
    return results
def enhanced_top(src,mask,points):
    # Crop top 560px; scale exactly 1.5x, then put generously large ring / label.
    crop=Image.fromarray(src,"RGB").crop((0,0,720,560)).resize((1080,840),Image.Resampling.LANCZOS)
    pixels=np.asarray(crop).copy()
    p_mask=Image.fromarray(mask.astype(np.uint8)*255,"L").crop((0,0,720,560)).resize((1080,840),Image.Resampling.NEAREST)
    people=np.asarray(p_mask)>0
    pixels[people]=(pixels[people].astype(np.float32)*.62+np.array([38,108,235])*.38).astype(np.uint8)
    result=Image.fromarray(pixels,"RGB")
    d=ImageDraw.Draw(result)
    for i,pt in enumerate(points):
        xy=pt.get("center")
        if xy is None:continue
        fx=float(xy[0])*W;fy=float(xy[1])*H
        px,py=fx*1.5,fy*1.5
        if py>840:continue
        # Exterior thick white outline plus magenta circle to remain visible on candles.
        rad=25
        d.ellipse((px-rad-3,py-rad-3,px+rad+3,py+rad+3),outline="black",width=10)
        d.ellipse((px-rad,py-rad,px+rad,py+rad),outline="white",width=6)
        d.ellipse((px-rad+3,py-rad+3,px+rad-3,py+rad-3),outline=MAGENTA,width=5)
        d.line((px-11,py,px+11,py),fill=MAGENTA,width=5)
        d.line((px,py-11,px,py+11),fill=MAGENTA,width=5)
        # Pull label inside visible canvas even at hard right / top boundaries.
        right_edge=px>800
        lx=int(max(8,min(px-205 if right_edge else px+32,850)))
        ly=int(max(8,min(py+35 if py<75 else py-68,778)))
        anchor=(lx+2,ly+18)
        d.line((px,py,anchor[0],anchor[1]),fill="black",width=9)
        d.line((px,py,anchor[0],anchor[1]),fill=MAGENTA,width=5)
        title=f"P{i+1}  ({int(round(fx))},{int(round(fy))})"
        width=int(d.textbbox((0,0),title,font=font(25))[2])+24
        d.rounded_rectangle((lx,ly,lx+width,ly+40),radius=7,fill=MAGENTA,outline="white",width=2)
        d.text((lx+11,ly+7),title,font=font(25),fill=(0,0,0))
    return result

def main():
    r=json.loads(MANIFEST.read_text())
    cases={x["shot_id"]:x for x in r["samples"]}
    assert len(SIDS)==8 and all(sid in cases for sid in SIDS)
    assert sha(SOURCE)==r["source_video_sha256"]
    selected={}
    for sid in SIDS:
        frames=cases[sid]["frames"]
        # N17 is temporally mixed: show frame with real candle visible.
        sample=frames[-1] if sid=="N17" else frames[1]
        selected[sid]=sample
    originals=exact([p["frame_index"] for p in selected.values()])
    OUT.mkdir(exist_ok=True)
    shot_panels={}
    photos=[]
    for sid in SIDS:
        item=cases[sid]
        frame=selected[sid]
        idx=frame["frame_index"]
        source,source_sha=originals[idx]
        assert source_sha==frame["decoded_rgb_sha256"],"EXACT_SOURCE_CHANGED_"+sid
        mask_file=BASE/"evidence"/frame["person_mask_proposal"]
        assert sha(mask_file)==frame["person_mask_sha256"]
        mask=np.asarray(Image.open(mask_file).convert("L"))>0
        props=[x for x in item["source_core_proposals"] if x["center"] is not None]
        unlocated=[x for x in item["source_core_proposals"] if x["center"] is None]
        annotated=enhanced_top(source,mask,props)
        clean=Image.fromarray(source,"RGB").crop((0,0,720,560)).resize((1080,840),Image.Resampling.LANCZOS)
        panel=Image.new("RGB",(2240,1005),(15,15,18))
        d=ImageDraw.Draw(panel)
        panel.paste(clean,(20,112))
        panel.paste(annotated,(1140,112))
        d.text((20,18),f"{sid}  F{idx}  |  EXACT SOURCE  /  NO ANNOTATIONS",font=font(32),fill="white")
        d.text((1140,18),"PINK = CURRENT CANDIDATE CENTER  (NOT APPROVED)",font=font(25),fill=MAGENTA)
        if props:
            note=f"{len(props)} candidate center(s) | not verified flame cores"
            # Even if the example light ROIs are only halos, don't mislabel as a flame.
            d.text((1140,60),note,font=font(22),fill=(235,230,230))
        elif sid=="N23":
            d.rounded_rectangle((1140,57,2110,104),radius=9,fill=(77,60,17),outline=(245,193,65),width=2)
            d.text((1150,68),"NO REGISTERED CORE  -  calibration required",font=font(22),fill="white")
        elif sid=="N17":
            d.rounded_rectangle((1140,57,2150,104),radius=9,fill=(77,60,17),outline=(245,193,65),width=2)
            d.text((1150,68),"LATE FRAME: VISIBLE FLAME, CENTER NOT REGISTERED",font=font(19),fill="white")
        elif sid=="N16_PART_2":
            d.rounded_rectangle((1140,57,2150,104),radius=9,fill=(45,63,43),outline=(205,233,190),width=2)
            d.text((1150,68),"DAYLIGHT NEGATIVE: NO CANDLE LOCATION PROPOSED",font=font(19),fill="white")
        d.text((20,960), "Blue overlay: machine person-mask proposal; P#: old experimental location, not confirmed.",font=font(22),fill=(224,223,223))
        output=OUT/f"M01_A1_{sid}_LOCATORS_LARGE_V002.jpg"
        panel.save(output,"JPEG",quality=82,optimize=True)
        shot_panels[sid]=output
        photos.append({"shot_id":sid,"source_frame":idx,
           "exact_raw_rgb_sha256":source_sha,"source_person_proposal_sha256":frame["person_mask_sha256"],
           "legacy_candidate_count":len(props),"unlocated_candidate_count":len(unlocated),
           "marker_location_data":[{"index":i+1,"normalized":pt["center"],"basis":pt["kind"]} for i,pt in enumerate(props)],
           "marking_policy":"VISIBLE_BRIGHT_MAGENTA_RING_NUMERIC_LABEL_WITH_LEADER; NOT_APPROVED",
           "image":output.name,"image_sha256":sha(output),"ground_truth_approved":False})
    # 2 groups of 4. Larger review image, readable on zoom, not a tiny 8x mosaic.
    for group in range(2):
        selected_ids=SIDS[group*4:group*4+4]
        overview=Image.new("RGB",(1540,1815),(12,12,15))
        d=ImageDraw.Draw(overview)
        for n,sid in enumerate(selected_ids):
            # Show legible 740x835 crop of the marked RIGHT panel only.
            src=Image.open(shot_panels[sid]).convert("RGB")
            source_top=src.crop((1140,112,2220,952))
            view=source_top.resize((740,575),Image.Resampling.LANCZOS)
            x=(n%2)*770+15
            y=(n//2)*890+65
            overview.paste(view,(x,y))
            d.text((x,y-48),f"{sid}  F{selected[sid]['frame_index']}",font=font(31),fill="white")
            count=len([v for v in cases[sid]["source_core_proposals"] if v["center"] is not None])
            if count:
                txt=f"{count} PINK proposed locator(s) - confirm position"
                col=MAGENTA
            else:
                txt="NO CORE REGISTERED - DO NOT ASSUME SUCCESS"
                col=(255,220,101)
            d.text((x,y+595),txt,font=font(19),fill=col)
        filename=f"M01_A1_LOCATORS_OVERVIEW_GROUP_{group+1}_V002.jpg"
        path=OUT/filename
        overview.save(path,"JPEG",quality=81,optimize=True)
        (OUT/(filename+".b64.txt")).write_text(base64.b64encode(path.read_bytes()).decode()+"\n")
    report={"schema":"M01_STAGE_A1_LEGIBLE_MARKER_REVIEW_V002",
        "status":"PRESENTATION_FIX_ONLY_ANNOTATIONS_NOT_GROUND_TRUTH",
        "source_sha256":r["source_video_sha256"],
        "original_benchmark_sha256":sha(MANIFEST),
        "purpose":"Make hard-to-see magenta candidate centers visibly labeled and mark missing sources explicitly.",
        "source_marker_positions_not_changed":True,
        "person_masks_not_changed":True,
        "input_png_and_mp4_not_changed":True,
        "no_video_render":True,
        "no_gt_promotion":True,
        "output_files":[x.name for x in shot_panels.values()],
        "overview":["M01_A1_LOCATORS_OVERVIEW_GROUP_1_V002.jpg","M01_A1_LOCATORS_OVERVIEW_GROUP_2_V002.jpg"],
        "shots":photos}
    (OUT/"M01_A1_LOCATORS_LEGIBILITY_QA_V002.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print("M01_A1_CANDIDATE_LABEL_LEGIBILITY_PASS_SOURCE_UNCHANGED; 8 shot-specific review panels and two overviews")
if __name__=="__main__":main()
