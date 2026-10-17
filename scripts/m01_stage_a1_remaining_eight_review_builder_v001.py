#!/usr/bin/env python3
"""M01 Stage A1: inspect eight remaining cases (3 verified source frames each).

This is the unapproved person + light proposal package; no visual review is
automatically marked as passed. No new image generation, video, official
publication, main merge, or promotion of Ground Truth.
"""
import base64,hashlib,io,json,pathlib,subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT=pathlib.Path(__file__).resolve().parents[1]
BASE=ROOT/"production/environment_dynamic/benchmarks/m01_stage_a_v002"
SOURCE=ROOT/"production/video_candidates/assets/S02_B_V006_CINEMATIC_ROUGH_RECONSTRUCTED_CANDIDATE_V001.mp4"
MANIFEST=BASE/"evidence/M01_STAGE_A_MACHINE_BENCHMARK_V002.json"
SPEC=BASE/"M01_STAGE_A_CASE_SPEC_V002.json"
OUT=ROOT/"_m01_a1_remaining_eight_v001"
SHOTS=["N16_PART_1","N20_FIRST","N21","A06","N23","V006_NEW_02","N16_PART_2","N17"]
W,H=720,1280
def sha(payload):
    return hashlib.sha256(payload).hexdigest()
def ft(size):
    path="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(path,size) if pathlib.Path(path).exists() else ImageFont.load_default()
def get_exact_frames(indices):
    assert len(indices)==len(set(indices))==24
    indices=sorted(indices)
    expr="+".join("eq(n\\,%d)"%i for i in indices)
    cmd=["ffmpeg","-hide_banner","-loglevel","error","-xerror",
         "-i",str(SOURCE),"-map","0:v:0","-vf","select="+expr,
         "-vsync","vfr","-f","rawvideo","-pix_fmt","rgb24","pipe:1"]
    p=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out={}
    try:
        for idx in indices:
            size=W*H*3
            blocks=[]
            while size>0:
                bit=p.stdout.read(size)
                if not bit:raise RuntimeError(f"TRUNCATED_FRAME_{idx}")
                blocks.append(bit)
                size-=len(bit)
            raw=b"".join(blocks)
            out[idx]=(np.frombuffer(raw,dtype=np.uint8).reshape(H,W,3).copy(),sha(raw))
        assert p.stdout.read(1)==b""
    finally:
        p.stdout.close()
    err=p.stderr.read().decode(errors="replace")
    p.stderr.close()
    assert p.wait()==0,err[-600:]
    return out
def mask_plus_uncertain(rgb,mask,boxes):
    person=mask>0
    bbox=np.zeros(person.shape,dtype=bool)
    for b in boxes:
        x0,y0,x1,y1=b["bbox"]
        bbox[y0:y1,x0:x1]=True
    unknown=bbox & (~person)
    arr=rgb.astype(np.float32).copy()
    arr[person]=arr[person]*.52+np.array([26,102,249])*.48
    yy,xx=np.ogrid[:H,:W]
    hatching=unknown & ((xx+yy)%15<2)
    arr[hatching]=arr[hatching]*.25+np.array([250,144,30])*.75
    return Image.fromarray(np.clip(arr,0,255).astype(np.uint8)),unknown

def draw_markers(im,proposals,sid,idx):
    # Machine suggestions are guides only. Negative and mixed cases must not
    # inherit a fictitious source point from a shot-wide rule.
    canvas=im.copy()
    d=ImageDraw.Draw(canvas)
    for j,prop in enumerate(proposals):
        xy=prop["center"]
        if xy is None:continue
        x,y=round(float(xy[0])*W),round(float(xy[1])*H)
        if not 0<=x<W or not 0<=y<H:continue
        d.ellipse([x-10,y-10,x+10,y+10],outline=(253,28,207),width=3)
        d.line([x-14,y,x+14,y],fill=(253,28,207),width=2)
        d.line([x,y-14,x,y+14],fill=(253,28,207),width=2)
        d.text([max(0,min(x+10,W-50)),max(0,y-25)],f"P{j+1}",font=ft(19),
               fill="white",stroke_fill="black",stroke_width=2)
    if sid=="N17":
        d.text([20,80],"N17: source visible in last sample",font=ft(24),
               fill=(255,235,155),stroke_width=2,stroke_fill="black")
    if sid=="N16_PART_2":
        d.text([20,80],"DAYLIGHT NEGATIVE: VERIFY",font=ft(23),
               fill=(255,235,155),stroke_width=2,stroke_fill="black")
    return canvas

def main():
    spec=json.loads(SPEC.read_text())
    sourcebytes=SOURCE.read_bytes()
    assert sha(sourcebytes)==spec["source_video_sha256"]
    manifest=json.loads(MANIFEST.read_text())
    cases={s["shot_id"]:s for s in manifest["samples"]}
    assert set(SHOTS).issubset(cases)
    chosen=[f for sid in SHOTS for f in cases[sid]["frames"]]
    frames=get_exact_frames({x["frame_index"] for x in chosen})
    OUT.mkdir(exist_ok=True)
    records=[]
    collage=Image.new("RGB",(4*320,2*460),(16,16,18))
    drawcol=ImageDraw.Draw(collage)
    for slot,sid in enumerate(SHOTS):
        shot=cases[sid]
        panel=Image.new("RGB",(760,3*745),(14,14,15))
        d=ImageDraw.Draw(panel)
        framereports=[]
        for i,fr in enumerate(shot["frames"]):
            ix=fr["frame_index"]
            rgb,rgb_sha=frames[ix]
            assert rgb_sha==fr["decoded_rgb_sha256"],f"RGB_HASH_CHANGED_{sid}_{ix}"
            maskp=BASE/"evidence"/fr["person_mask_proposal"]
            maskbytes=maskp.read_bytes()
            assert sha(maskbytes)==fr["person_mask_sha256"],f"PERSON_MASK_HASH_CHANGED_{sid}_{ix}"
            mask=np.asarray(Image.open(io.BytesIO(maskbytes)).convert("L"))
            assert mask.shape==(H,W)
            annotated,uncertain=mask_plus_uncertain(rgb,mask,fr["person_boxes"])
            if i==1:
                annotated=draw_markers(annotated,shot["source_core_proposals"],sid,ix)
            sourceimg=Image.fromarray(rgb,"RGB")
            y=i*745
            d.text((10,y+4),f"{sid} | exact frame F{ix} | clean",font=ft(21),fill="white")
            d.text((390,y+4),"blue persons / orange uncertain / magenta guess",font=ft(13),fill="white")
            panel.paste(sourceimg.resize((372,662),Image.Resampling.LANCZOS),(4,y+32))
            panel.paste(annotated.resize((372,662),Image.Resampling.LANCZOS),(384,y+32))
            d.text((8,y+700),f"Detected people {fr['people_detected']}; person mask {fr['segmentation_proposal_area_pct']}%",
                   font=ft(17),fill=(230,230,230))
            framereports.append({"index":ix,"rgb_sha256":rgb_sha,
                "person_mask_sha256":fr["person_mask_sha256"],
                "person_proposal_mask_area_pct":fr["segmentation_proposal_area_pct"],
                "bbox_only_uncertainty_pct":round(float(np.mean(uncertain))*100,4),
                "visible_light_hypothesis":fr["frame_light_hypothesis"],
                "person_mask_human_approved":False,
                "flame_position_approved":False})
            if i==1:
                # Photo overview prioritizes candles / nearby humans
                upper=annotated.crop((0,0,720,900)).resize((308,386),Image.Resampling.LANCZOS)
                cx=(slot%4)*320
                cy=(slot//4)*460
                collage.paste(upper,(cx+6,cy+36))
                drawcol.text((cx+6,cy+5),sid,font=ft(18),fill="white")
                drawcol.text((cx+6,cy+425),f"F{ix} | no ground truth",font=ft(15),fill=(220,220,220))
        filename=f"M01_STAGE_A1_{sid}_ALL_THREE_FRAMES_REVIEW_V001.jpg"
        path=OUT/filename
        panel.save(path,"JPEG",quality=78,optimize=True)
        records.append({"shot_id":sid,"group":shot["group"],"file":filename,
            "file_sha256":sha(path.read_bytes()),
            "frames":framereports,"machine_source_proposals":shot["source_core_proposals"],
            "flame_sources_approved":False,"all_frame_person_protection_approved":False})
    overview=OUT/"M01_STAGE_A1_REMAINING_EIGHT_OVERVIEW_V001.jpg"
    collage.save(overview,"JPEG",quality=82,optimize=True)
    (OUT/(overview.name+".b64.txt")).write_text(base64.b64encode(overview.read_bytes()).decode()+"\n")
    report={
       "schema":"M01_STAGE_A1_REMAINING_EIGHT_REVIEW_V001",
       "status":"SOURCE_PROTECTION_DIAGNOSTICS_READY_NOT_GROUND_TRUTH",
       "source_video_sha256":spec["source_video_sha256"],
       "source_manifest_sha256":sha(MANIFEST.read_bytes()),
       "reviewed_priority_three_visual_record":"production/environment_dynamic/benchmarks/m01_stage_a_v002/A1_PO_VISUAL_FEEDBACK_PRIORITY_THREE_20261017.json",
       "remaining_shots":SHOTS,"frames":24,
       "test_groups":{"po_alignment_failure":4,"accepted_style_reference":2,"daylight_negative":1,"temporal_mixed_visibility":1},
       "remaining_frames_approved":False,
       "not_yet_confirmed_flame_mask_geometry":True,
       "protect_all_people_not_yet_verified":True,
       "n17_warning":"daylight close-up to visible candles; shot-level no-light status is invalid",
       "machine_position_status":"DIAGNOSTIC_HINTS_NEVER_GROUND_TRUTH",
       "visual_overview":overview.name,
       "visual_overview_sha256":sha(overview.read_bytes()),
       "no_video_render":True,
       "main_unchanged":True,"m01_batch_gate":"HOLD",
       "cases":records
    }
    (OUT/"M01_STAGE_A1_REMAINING_EIGHT_REVIEW_V001.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    assert sha(SOURCE.read_bytes())==spec["source_video_sha256"]
    print("M01_A1_REMAINING_EIGHT_REVIEW_DATASET_PASS_ONLY",json.dumps({
        "shots":8,"frames":24,"mask_verified_against_original_sha":True,
        "ground_truth_approved":False,"engine_batch_unlocked":False}))
if __name__=="__main__":main()
