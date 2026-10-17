#!/usr/bin/env python3
"""A1 priority human-guided fixture/flame seed proposals with exact-frame mask checks.
Blue=unapproved YOLO person proposal; orange=possible bbox-only human area.
Cyan=visual flame seed; green=local high-luminance pixel candidate if unique.
Nothing is approved ground truth; no story shot or video changed.
"""
import base64,hashlib,io,json,pathlib,subprocess,math
import numpy as np
from PIL import Image,ImageDraw,ImageFont
ROOT=pathlib.Path(__file__).resolve().parents[1]
SRC=ROOT/"production/video_candidates/assets/S02_B_V006_CINEMATIC_ROUGH_RECONSTRUCTED_CANDIDATE_V001.mp4"
BASE=ROOT/"production/environment_dynamic/benchmarks/m01_stage_a_v002/"
BENCH=BASE/"evidence/M01_STAGE_A_MACHINE_BENCHMARK_V002.json"
DRAFT=BASE/"M01_A1_VISUAL_FLAME_FIXTURE_DRAFT_V001.json"
OUT=ROOT/"_m01_stage_a1_flame_seed_visual_review"
W,H=720,1280
def digest(data):
    h=hashlib.sha256()
    if isinstance(data,pathlib.Path):
        with data.open("rb") as f:
            for chunk in iter(lambda:f.read(1024*1024),b""):h.update(chunk)
    else:h.update(data)
    return h.hexdigest()
def ft(n):
    p="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(p,n) if pathlib.Path(p).exists() else ImageFont.load_default()
def exact(index):
    p=subprocess.Popen(["ffmpeg","-hide_banner","-v","error","-xerror",
        "-i",str(SRC),"-vf",f"select=eq(n\\,{index})","-vsync","vfr",
        "-frames:v","1","-f","rawvideo","-pix_fmt","rgb24","pipe:1"],
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    n=W*H*3
    raw=p.stdout.read(n);p.stdout.close()
    err=p.stderr.read().decode(errors="replace");p.stderr.close()
    assert len(raw)==n and p.wait()==0,("EXACT_SOURCE_DECODE",index,err[-500:])
    return np.frombuffer(raw,dtype=np.uint8).reshape(H,W,3).copy(),digest(raw)
def core_near(rgb,px,py,protected):
    # This is a spectral peak check within each visually located flame seed,
    # not a candle-vs-reflection classifier.
    xmin,xmax=max(0,px-15),min(W,px+16)
    ymin,ymax=max(0,py-18),min(H,py+19)
    crop=rgb[ymin:ymax,xmin:xmax].astype(np.int16)
    r,g,b=crop[:,:,0],crop[:,:,1],crop[:,:,2]
    valid=(r>=207)&(g>=147)&(r>=g-13)&((g-b)>=15)&((r-b)>=26)
    valid &= ~protected[ymin:ymax,xmin:xmax]
    if not valid.any():return None,0,True
    yy,xx=np.where(valid)
    strength=(r[valid]+g[valid]-b[valid]).astype(np.float32)
    bestidx=np.argmax(strength-2*(xx+ xmin-px)**2-2*(yy+ymin-py)**2)
    return [int(xx[bestidx]+xmin),int(yy[bestidx]+ymin)],int(valid.sum()),False
def main():
    bench=json.loads(BENCH.read_text())
    spec=json.loads(DRAFT.read_text())
    assert spec["all_fixtures_approved"] is False
    assert digest(SRC)==spec["source_video_sha256"]
    by={x["shot_id"]:x for x in bench["samples"]}
    results=[]
    OUT.mkdir(parents=True,exist_ok=True)
    for sid,case in spec["cases"].items():
        shot=by[sid];frame_id=case["frame_index"]
        sample=next(s for s in shot["frames"] if s["frame_index"]==frame_id)
        rgb,sha=exact(frame_id)
        assert sha==sample["decoded_rgb_sha256"]
        mpath=BASE/"evidence"/sample["person_mask_proposal"]
        assert digest(mpath)==sample["person_mask_sha256"]
        prot=np.asarray(Image.open(mpath).convert("L"))>0
        full=np.array(rgb)
        shade=full.copy().astype(np.float32)
        shade[prot]=shade[prot]*.55+np.array([20,94,245],dtype=np.float32)*.45
        canv=Image.fromarray(np.clip(shade,0,255).astype(np.uint8)).crop((0,0,W,520))
        up=canv.resize((1080,780),Image.Resampling.LANCZOS)
        draw=ImageDraw.Draw(up)
        lamps=[]
        all_seed_intersections=0
        for i,fixture in enumerate(case["fixtures"]):
            x0,y0,x1,y1=fixture["bbox"]
            assert 0<=x0<x1<=W and 0<=y0<y1<=520
            sx=1080/W;sy=780/520
            color=(255,196,55) if fixture["visibility"]=="SMALL_BACKGROUND_CANDIDATE" else (57,249,225)
            draw.rectangle([x0*sx,y0*sy,x1*sx-1,y1*sy-1],outline=color,width=3)
            tx=min(x0*sx+4,1000);ty=y0*sy+4
            draw.text((tx,ty),f"F{i+1}",font=ft(20),fill=color,stroke_width=2,stroke_fill="black")
            flame_points=[]
            for j,(x,y) in enumerate(fixture["flames"]):
                assert 0<=x<W and 0<=y<H
                auto,num,missing=core_near(rgb,x,y,prot)
                protected_hit=bool(prot[y,x])
                if protected_hit:all_seed_intersections+=1
                cx,cy=x*sx,y*sy
                draw.ellipse([cx-7,cy-7,cx+7,cy+7],outline=(49,249,240),width=3)
                draw.text((min(cx+8,1030),max(8,cy-16)),str(j+1),font=ft(17),
                          fill="white",stroke_fill="black",stroke_width=2)
                if auto:
                    ax,ay=auto
                    draw.line([ax*sx-6,ay*sy,ax*sx+6,ay*sy],fill=(241,250,49),width=3)
                    draw.line([ax*sx,ay*sy-6,ax*sx,ay*sy+6],fill=(241,250,49),width=3)
                flame_points.append({"flame_index":j+1,"visual_estimate_px":[x,y],
                   "bright_pixel_near_seed_px":auto,"nearby_bright_pixels":num,
                   "no_peak_detected":missing,"visual_seed_overlaps_machine_person_mask":protected_hit,
                   "position_verified":False,
                   "flame_core_mask_verified":False})
            lamps.append({"fixture_id":fixture["id"],"visibility":fixture["visibility"],
               "roi_px":fixture["bbox"],"flames":flame_points,
               "calibration_status":"NEEDS_INDEPENDENT_POSITION_AND_HUMAN_CONFIRMATION"})
        # Write one frame-size source crop on left, manual flame center / blue human masks right.
        original=Image.fromarray(rgb,"RGB").crop((0,0,W,520)).resize((1080,780),Image.Resampling.LANCZOS)
        panel=Image.new("RGB",(2160,825),(13,13,15))
        panel.paste(original,(0,40));panel.paste(up,(1080,40))
        d=ImageDraw.Draw(panel)
        d.text((5,6),f"{sid} F{frame_id} | EXACT RAW SOURCE TOP",font=ft(25),fill="white")
        d.text((1085,6),"F# FIXTURE / CYAN SEED / YELLOW BRIGHT PEAK / BLUE PEOPLE",font=ft(18),fill="white")
        imagefile=f"M01_A1_{sid}_FIXTURE_AND_FLAME_PROPOSALS_V001.jpg"
        jpg=OUT/imagefile
        panel.save(jpg,"JPEG",quality=84,optimize=True)
        (OUT/(imagefile+".b64.txt")).write_text(base64.b64encode(jpg.read_bytes()).decode()+"\n")
        results.append({"shot_id":sid,"frame_index":frame_id,"source_rgb_sha256":sha,
            "person_mask_sha256":sample["person_mask_sha256"],
            "fixture_count":len(lamps),
            "individual_flame_seeds":sum(len(x["flames"]) for x in lamps),
            "visual_seed_person_mask_conflicts":all_seed_intersections,
            "candle_position_approval":False,"person_mask_approval":False,
            "lamp_groups":lamps,"image_file":imagefile,"image_sha256":digest(jpg)})
    record={"schema":"M01_STAGE_A1_FLAME_SOURCE_VISUAL_PROPOSALS_V001",
       "status":"VISUAL_FLAME_SEEDS_NOT_VERIFIED_GROUND_TRUTH",
       "source_sha256":spec["source_video_sha256"],
       "draft_source_file":str(DRAFT.relative_to(ROOT)),
       "draft_source_sha256":digest(DRAFT),
       "benchmark_sha256":digest(BENCH),
       "recording_policy":"PO review each flame and silhouette; draft bright points may be reflections; no auto-PASS",
       "light_fixture_atlas_approved":False,"person_mask_approved":False,
       "batch_video_render_authorized":False,"main_merge":False,
       "selected_images":results}
    (OUT/"M01_STAGE_A1_FLAME_SOURCE_VISUAL_PROPOSALS_V001.json").write_text(
        json.dumps(record,ensure_ascii=False,indent=2)+"\n")
    print("M01_A1_VISUAL_FLAME_SEED_QA_ONLY",json.dumps({"shots":len(results),
        "fixtures":sum(s["fixture_count"] for s in results),
        "visual_flame_seeds":sum(s["individual_flame_seeds"] for s in results),
        "seeds_in_person_mask":sum(s["visual_seed_person_mask_conflicts"] for s in results),
        "correct_flame_gt_established":False},ensure_ascii=False))
if __name__=="__main__":main()
