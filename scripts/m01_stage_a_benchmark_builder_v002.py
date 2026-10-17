#!/usr/bin/env python3
"""Build M01 Stage A V002 corrected reproducible dataset (not a flame detection pass).

11 benchmark clips, 33 video-source snapshots, 33 YOLO person-mask proposals,
two contact sheets, machine-readable review queue. Existing candidate core
positions are explicitly NOT ground truth. FAIL-CLOSED for production.
"""
import base64, hashlib, importlib.util, io, json, pathlib, subprocess, sys
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from ultralytics import YOLO
import ultralytics

ROOT=pathlib.Path(__file__).resolve().parents[1]
SPEC=ROOT/"production/environment_dynamic/benchmarks/m01_stage_a_v002/M01_STAGE_A_CASE_SPEC_V002.json"
OUT=ROOT/"_m01_stage_a_v002"
SAMPLES=OUT/"person_mask_proposals"
REPORT=OUT/"M01_STAGE_A_MACHINE_BENCHMARK_V002.json"
QUEUE=OUT/"M01_STAGE_A_GROUND_TRUTH_REVIEW_QUEUE_V002.json"
W,H=720,1280

def digest(path):
    h=hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda:stream.read(1048576),b""):h.update(block)
    return h.hexdigest()
def bytesha(payload):
    return hashlib.sha256(payload).hexdigest()
def ft(size):
    p="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(p,size) if pathlib.Path(p).exists() else ImageFont.load_default()

def sample_frames(shot):
    begin=shot["start_frame"];length=shot["end_frame_exclusive"]-begin
    return [begin+round((length-1)*p) for p in (0.15,0.50,0.85)]

def extract_frame_batch(source,indices):
    # Decode exact VIDEO FRAME INDICES, not approximate -ss seek times.
    assert len(indices)==len(set(indices))==33
    expr="+".join("eq(n\\,%d)"%index for index in sorted(indices))
    cmd=["ffmpeg","-hide_banner","-loglevel","error","-xerror",
         "-i",str(source),"-map","0:v:0","-vf","select="+expr,
         "-vsync","vfr","-f","rawvideo","-pix_fmt","rgb24","pipe:1"]
    proc=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    frames={}
    n=W*H*3
    try:
        for idx in sorted(indices):
            pieces=[];need=n
            while need:
                chunk=proc.stdout.read(need)
                if not chunk:raise RuntimeError(f"SHORT_EXACT_VIDEO_FRAME_{idx}")
                pieces.append(chunk);need-=len(chunk)
            raw=b"".join(pieces)
            assert len(raw)==n
            frames[idx]=(np.frombuffer(raw,dtype=np.uint8).reshape(H,W,3).copy(),bytesha(raw))
        assert proc.stdout.read(1)==b""
    finally:
        proc.stdout.close()
    err=proc.stderr.read().decode(errors="replace")
    proc.stderr.close()
    rc=proc.wait()
    if rc:raise RuntimeError(f"FFMPEG_EXACT_INDEX_DECODE_ERROR_{rc}: {err[:900]}")
    return frames

def mask_person(img,net):
    result=net.predict(img,classes=[0],imgsz=960,conf=0.14,iou=.55,
        retina_masks=True,device="cpu",verbose=False)[0]
    segmentation=np.zeros((H,W),dtype=np.uint8)
    count=len(result.boxes) if result.boxes is not None else 0
    masks=result.masks.data.cpu().numpy() if result.masks is not None else np.empty((0,H,W))
    human_proposals=[]
    bboxmask=np.zeros((H,W),dtype=np.uint8)
    for index in range(count):
        box=result.boxes[index]
        x0,y0,x1,y1=(int(v) for v in box.xyxy[0].cpu().numpy())
        x0=max(0,x0-10);y0=max(0,y0-10);x1=min(W,x1+10);y1=min(H,y1+10)
        bboxmask[y0:y1,x0:x1]=255
        has_instance=index<len(masks)
        if has_instance:
            pm=masks[index]
            if pm.shape!=(H,W):
                pm=cv2.resize(pm.astype(np.float32),(W,H),interpolation=cv2.INTER_NEAREST)
            segmentation[pm>.45]=255
        human_proposals.append({"bbox":[x0,y0,x1,y1],
            "confidence":round(float(box.conf[0]),5),
            "has_instance_segmentation":has_instance})
    segmentation=cv2.dilate(segmentation,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(27,27)))
    # Mark BOTH confident silhouette and unprotected bbox-only uncertainty.
    # This is NOT a verified all-person protection mask.
    bbox_uncertainty=(bboxmask>0)&(segmentation==0)
    return segmentation,bbox_uncertainty,human_proposals

def overlay(original,mask,uncertain,crosses):
    arr=original.astype(np.float32).copy()
    inside=mask>0
    arr[inside]=arr[inside]*.57+np.array([35,98,249],dtype=np.float32)*.43
    # Thin orange grid indicates bbox-only areas where the silhouette detector
    # may have missed a person. Do not mistake these for proven safe pixels.
    y,x=np.indices((H,W),dtype=np.int32)
    hatch=uncertain & ((x+y)%20<2)
    arr[hatch]=arr[hatch]*.20+np.array([250,137,20],dtype=np.float32)*.80
    pic=Image.fromarray(np.clip(arr,0,255).astype("uint8"))
    d=ImageDraw.Draw(pic)
    for i,item in enumerate(crosses):
        p=item["center"]
        if p is None:continue
        x,y=round(p[0]*W),round(p[1]*H)
        d.ellipse((x-11,y-11,x+11,y+11),outline=(252,35,205),width=3)
        d.line((x-16,y,x+16,y),fill=(252,35,205),width=2)
        d.line((x,y-16,x,y+16),fill=(252,35,205),width=2)
        d.text((max(2,min(x+12,W-44)),max(2,y-20)),f"P{i+1}",
               fill="white",stroke_fill=(0,0,0),stroke_width=2,font=ft(19))
    return pic

def candidates_for_case(sid,atlas,profile):
    if sid in atlas["profiles"]:
        src=atlas["profiles"][sid]["sources"]
        return [{"source_index":a["fixture_index"],
                 "kind":"UNVERIFIED_MACHINE_CORE_POINT",
                 "center":a["candidate_center"],
                 "review_status":"NEEDS_PO_OR_INDEPENDENT_VISUAL_CONFIRMATION",
                 "machine_status":a["status"]} for a in src]
    if sid=="V006_NEW_02":
        return [{"source_index":i+1,"kind":"LEGACY_LIGHTING_ROI_CENTER_NOT_FLAME_CORE",
                 "center":a["center"],"name":a["name"],
                 "review_status":"NOT_GROUND_TRUTH"} for i,a in enumerate(profile["candlelight"]["anchors"])]
    if sid=="N23":
        return [{"source_index":1,"kind":"NO_REGISTERED_PIXEL_CORE",
                 "center":None,"review_status":"NEEDS_MANUAL_CALIBRATION"}]
    return []

def make_sheet(records,names,output_path,title):
    cellw,cellh=310,576
    bg=Image.new("RGB",(cellw*4,cellh*len(names)),(13,13,15))
    d=ImageDraw.Draw(bg)
    f19=ft(19);f15=ft(15)
    for row,sid in enumerate(names):
        rec=records[sid]; yy=row*cellh
        for i,frame in enumerate(rec["frames"]):
            # Contact JPEG crops are rebuilt directly from in-memory preview
            # images created in the frame loop and stored under OUT/previews.
            origin=Image.open(OUT/frame["internal_original_jpeg"]).convert("RGB")
            composite=Image.open(OUT/frame["internal_overlay_jpeg"]).convert("RGB")
            shown=origin if i==1 else composite
            shown=shown.resize((296,526),Image.Resampling.LANCZOS)
            xx=cellw*i
            bg.paste(shown,(xx+7,yy+37))
            d.text((xx+7,yy+4),f"{sid}  f{frame['frame_index']}",fill="white",font=f15)
            d.text((xx+7,yy+19),["15% + mask","50% CLEAN","85% + mask"][i],
                  fill=(210,210,214),font=f15)
        mid=rec["frames"][1]
        annotated=Image.open(OUT/mid["internal_overlay_jpeg"]).convert("RGB").resize((296,526),Image.Resampling.LANCZOS)
        x0=3*cellw
        bg.paste(annotated,(x0+7,yy+37))
        d.text((x0+7,yy+4),f"50% ANNOTATED",fill="white",font=f19)
        d.text((x0+7,yy+22),rec["group"],fill=(227,198,196),font=f15)
    bg.save(output_path,"JPEG",quality=76,optimize=True)
    return digest(output_path)

def main():
    spec=json.loads(SPEC.read_text())
    source=ROOT/spec["source_video"]
    assert spec["schema"]=="M01_STAGE_A_CASE_SPEC_V002"
    assert digest(source)==spec["source_video_sha256"]
    assert (spec["width"],spec["height"],spec["fps"],spec["total_frames"])==(W,H,30,1927)
    edl=json.loads((ROOT/spec["source_edl"]).read_text())["timeline"]
    by_id={s["id"]:s for s in edl}
    cases=spec["cases"]
    assert len(cases)==11 and len({c["shot_id"] for c in cases})==11
    assert all(c["shot_id"] in by_id for c in cases)
    atlas=json.loads((ROOT/spec["baseline_candidate_atlas"]).read_text())
    profile=json.loads((ROOT/spec["NEW02_stylistic_reference_profile"]).read_text())
    sel={c["shot_id"]:sample_frames(by_id[c["shot_id"]]) for c in cases}
    idxs=[p for group in sel.values() for p in group]
    allframes=extract_frame_batch(source,idxs)
    if len(allframes)!=33:raise RuntimeError("FRAME_COUNT_NOT_33")
    model=YOLO("yolo11n-seg.pt")
    weights=pathlib.Path("yolo11n-seg.pt")
    assert weights.exists() and digest(weights)==spec["labeling_policy"]["model_sha256"]
    OUT.mkdir(exist_ok=True);SAMPLES.mkdir(exist_ok=True)
    (OUT/"previews").mkdir(exist_ok=True)
    records={}
    review={}
    for case in cases:
        sid=case["shot_id"]
        light_proposals=candidates_for_case(sid,atlas,profile)
        record={"shot_id":sid,"group":case["group"],"expected_light":case["expected_light"],
            "source_alignment_status":"NOT_VERIFIED",
            "human_ground_truth_status":"NOT_VERIFIED",
            "source_core_proposals":light_proposals,
            "frames":[]}
        review[sid]={"shot_id":sid,"role":case["group"],
            "expected_light":case["expected_light"],
            "fixture_review_status":"PENDING",
            "person_review_status":"PENDING",
            "proposed_fixtures_mid_frame":light_proposals,
            "calibration_instructions":"For each actual candle flame, verify/adjust core center or mark false positive. Validate face, hair, clothing and partial people on all 3 frames; approve or request correction.",
            "po_notes":case["issue"],
            "frame_light_hypotheses":case.get("frame_light_hypotheses",["UNKNOWN_PENDING_VISUAL_REVIEW"]*3),
            "approved":False,
            "first_priority":sid in {"N24","V006_NEW_01","N18"}}
        for ci,frame in enumerate(sel[sid]):
            img,rawsha=allframes[frame]
            mask,uncertain,people=mask_person(img,model)
            assert mask.shape==(H,W) and mask.dtype==np.uint8
            assert not np.any((mask>0) & uncertain), "MACHINE_PERSON_MASK_AND_BBOX_UNCERTAINTY_OVERLAP"
            outfile=f"PERSON_PROPOSAL_{sid}_F{frame:04d}.png"
            pp=SAMPLES/outfile
            Image.fromarray(mask,mode="L").save(pp,optimize=True)
            original=Image.fromarray(img,"RGB")
            showmarkers=light_proposals if ci==1 else []
            view=overlay(img,mask,uncertain,showmarkers)
            # Small source JPEG previews are temporary, with the full source identified by hash.
            origfile=f"previews/ORIGINAL_{sid}_F{frame:04d}.jpg"
            overfile=f"previews/ANNOTATED_{sid}_F{frame:04d}.jpg"
            original.save(OUT/origfile,"JPEG",quality=72,optimize=True)
            view.save(OUT/overfile,"JPEG",quality=73,optimize=True)
            record["frames"].append({
                "frame_index":frame,
                "absolute_time_seconds":round((frame+.5)/30,5),
                "decoded_rgb_sha256":rawsha,
                "person_mask_proposal":f"person_mask_proposals/{outfile}",
                "person_mask_sha256":digest(pp),
                "person_mask_origin":"YOLO11N_SEG_MACHINE_PROPOSAL_NOT_GROUND_TRUTH",
                "people_detected":len(people),
                "person_boxes":people,
                "segmentation_proposal_area_pct":round(float(np.mean(mask>0))*100,4),
                "bbox_only_uncertainty_area_pct":round(float(np.mean(uncertain))*100,4),
                "human_review_status":"PENDING",
                "frame_light_hypothesis":case.get("frame_light_hypotheses",["UNKNOWN_PENDING_VISUAL_REVIEW"]*3)[ci],
                "internal_original_jpeg":origfile,
                "internal_overlay_jpeg":overfile})
        records[sid]=record
    # Summaries always put PO-known failures first.
    fail=[x["shot_id"] for x in cases if x["group"]=="PO_REPORTED_ALIGNMENT_ERROR"]
    control=[x["shot_id"] for x in cases if x["group"]!="PO_REPORTED_ALIGNMENT_ERROR"]
    contact_names=[]
    for label,names in (("M01_STAGE_A_CONTACT_FAIL7_V002.jpg",fail),
                        ("M01_STAGE_A_CONTACT_CONTROLS4_V002.jpg",control)):
        file=OUT/label
        contact_names.append({"file":label,"sha256":make_sheet(records,names,file,label),
             "source_cases":names})
        (OUT/(label+".b64.txt")).write_text(base64.b64encode(file.read_bytes()).decode()+"\n")
    # Remove preview jpeg intermediates so only 33 masks + 2 contact sheets
    # + manifest/review worksheet are copied to permanent GitHub branch.
    for r in records.values():
        for entry in r["frames"]:
            (OUT/entry.pop("internal_original_jpeg")).unlink()
            (OUT/entry.pop("internal_overlay_jpeg")).unlink()
    (OUT/"previews").rmdir()
    ffmpeg_v=subprocess.check_output(["ffmpeg","-version"],text=True).splitlines()[0]
    full={
        "schema":"M01_STAGE_A_MACHINE_BENCHMARK_V002",
        "date":"2026-10-17","dataset_status":"MACHINE_CANDIDATE_GENERATED_NOT_GROUND_TRUTH",
        "first_goal":"S02B_GROUND_TRUTH_BENCHMARK_CONSTRUCTION",
        "ultimate_goal":"CROSS_SCENE_REUSABLE_CANDLE_ENGINE",
        "source_video":spec["source_video"],
        "source_video_sha256":spec["source_video_sha256"],
        "source_edl_sha256":digest(ROOT/spec["source_edl"]),
        "case_spec_sha256":digest(SPEC),
        "decoded_frame_method":"Exact 0-based ffmpeg select=eq(n,index) frame indices",
        "ffmpeg_version":ffmpeg_v,
        "segmentation_model":"Ultralytics YOLO11n-seg",
        "segmentation_model_sha256":digest(weights),
        "ultralytics_version":ultralytics.__version__,
        "person_mask_policy":"machine instance segmentation; dilated by 13px; unreviewed, not final protection",
        "light_proposals":"previous experimental flame source candidates and approved-style ROIs; NOT calibrated ground truth",
        "cases":len(cases),
        "source_frames":33,"supersedes_previous_dataset":"m01_stage_a_v001/evidence", "supersession_reason":spec.get("supersession_reason"),
        "machine_person_proposals":33,
        "known_po_alignment_failures":len(fail),
        "style_reference_shots":2,"negative_control_shots":1,"temporal_mixed_visibility_shots":1,
        "all_frame_annotations_approved":False,
        "all_light_core_labels_approved":False,
        "s02b_engine_ready":False,
        "cross_scene_engine_ready":False,
        "no_video_production":True,
        "no_official_video_index_update":True,
        "no_main_merge":True,
        "contact_sheets":contact_names,
        "samples":[records[x["shot_id"]] for x in cases]}
    REPORT.write_text(json.dumps(full,indent=2,ensure_ascii=False)+"\n")
    QUEUE.write_text(json.dumps({
        "schema":"M01_STAGE_A_GROUND_TRUTH_REVIEW_QUEUE_V002",
        "status":"HUMAN_REVIEW_REQUIRED_TO_LOCK_GROUND_TRUTH",
        "first_pass_acceptance":"Flame-core and protected-person masks per frame; no missing candle, no person spill",
        "cross_scene_acceptance_not_granted":True,
        "cases":[review[c["shot_id"]] for c in cases]
    },indent=2,ensure_ascii=False)+"\n")
    assert digest(source)==spec["source_video_sha256"]
    assert sum(len(s["frames"]) for s in full["samples"])==33
    assert len(list(SAMPLES.glob("PERSON_PROPOSAL_*.png")))==33
    print("M01_STAGE_A_REFERENCE_SET_GENERATED",json.dumps({
         "cases":11,"frames":33,"visible_practical_shots":9,"negative_shots":1,"mixed_visibility_shots":1,
         "source_sha256":digest(source),
         "all_labels":"PENDING_INDEPENDENT_REVIEW",
         "flame_core_gt":False,"person_gt":False,
         "s02b_pass":False,"reusable_engine_pass":False},ensure_ascii=False))
if __name__=="__main__":
    main()
