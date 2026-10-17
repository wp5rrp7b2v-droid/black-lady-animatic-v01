#!/usr/bin/env python3
"""M01 V002 Gate 1C: flame-like luminous source clustering + person-mask exclusion.
Diagnosis and Scene-Light-Atlas *draft*, never approved or passed for batch.
"""
import base64,hashlib,importlib.util,io,json,math,pathlib,platform
import numpy as np,cv2
from PIL import Image,ImageDraw,ImageFont
from ultralytics import YOLO

ROOT=pathlib.Path(__file__).resolve().parents[1]
PILOT=ROOT/"scripts/m01_v002_light_person_refine_v002.py"
LAST=ROOT/"production/environment_dynamic/review_candidates/M01_V002_LIGHT_PERSON_REFINE_V002/M01_V002_FLAME_PERSON_MASK_REFINEMENT_V002.json"
OUT=ROOT/"_m01_v002_multiscale_core_v003"
PIC="M01_V002_CANDLE_SOURCE_CLUSTER_AND_PERSON_SAFE_V003.jpg"
JSON="M01_V002_CANDLE_SOURCE_CLUSTER_AND_PERSON_SAFE_V003.json"
ATLAS="M01_V002_SCENE_LIGHT_ATLAS_CANDIDATES_V001.json"

def h(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def font(size):
    p="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(p,size) if pathlib.Path(p).exists() else ImageFont.load_default()
def load_module(path,key):
    spec=importlib.util.spec_from_file_location(key,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

def multiscale_luminous_cores(rgb,person_mask):
    a=rgb.astype(np.int16)
    r,g,b=a[:,:,0],a[:,:,1],a[:,:,2]
    # More inclusive than old r-b>=55: candle cores can be near-white/saturated.
    bright=(r>=199)&(g>=149)&((r-b)>=23)&((g-b)>=11)&((r-g)>=-14)
    bright|=(r>=240)&(g>=216)&((r-b)>=12)&((g-b)>=8)&((r-g)>=-18)
    bright[int(.43*rgb.shape[0]):,:]=False
    bright &= ~person_mask
    image=bright.astype(np.uint8)*255
    n,labels,stats,centers=cv2.connectedComponentsWithStats(image,connectivity=8)
    out=[]
    for i in range(1,n):
        x,y,w,h,area=map(int,stats[i])
        if area<2 or area>250 or w>36 or h>58:continue
        cx,cy=centers[i]
        # A compact bright core (not a continuous bright sandstone region).
        box=rgb[y:y+h,x:x+w]
        peak=int(box[:,:,0].max())
        if peak<215:continue
        out.append({"x":float(cx),"y":float(cy),"area":area,"box":[x,y,w,h],"peak_r":peak})
    return out, image

def merge_nearby(cores):
    # A candelabra may have multiple independently moving flames in one practical.
    if not cores:return []
    parent=list(range(len(cores)))
    def find(x):
        while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
        return x
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra!=rb:parent[rb]=ra
    for i,a in enumerate(cores):
        for j in range(i+1,len(cores)):
            b=cores[j]
            if abs(a["x"]-b["x"])<=32 and abs(a["y"]-b["y"])<=39:
                union(i,j)
    groups={}
    for i,c in enumerate(cores):groups.setdefault(find(i),[]).append(c)
    result=[]
    for members in groups.values():
        weights=np.array([max(1,c["area"]) for c in members],dtype=float)
        pts=np.array([[c["x"],c["y"]] for c in members])
        x,y=np.average(pts,axis=0,weights=weights)
        if len(members)>15:continue
        result.append({"center_px":[round(float(x),2),round(float(y),2)],
          "members":len(members),"bright_pixel_area":int(sum(c["area"] for c in members)),
          "flame_core_candidates":[[round(c["x"],2),round(c["y"],2)] for c in members],
          "cluster_bbox":[round(float(min(c["x"] for c in members)),1),
                          round(float(min(c["y"] for c in members)),1),
                          round(float(max(c["x"] for c in members)),1),
                          round(float(max(c["y"] for c in members)),1)]})
    return result

def choose_cluster(groups,hint):
    # Coordinates are a search aid, not truth. Prefer a cluster close to the
    # directionally adjusted hint, with multiple discrete small bright components.
    ranking=[]
    for c in groups:
        x,y=c["center_px"]
        dx=x/720-hint[0];dy=y/1280-hint[1]
        if abs(dx)>.13 or abs(dy)>.13:continue
        proximity=math.exp(-.5*((dx/.064)**2+(dy/.061)**2))
        count_bonus=(1+.16*min(c["members"],5))
        score=round(proximity*count_bonus,4)
        ranking.append({**c,"score":score})
    ranking.sort(key=lambda x:x["score"],reverse=True)
    if not ranking:return None,[],"NO_CLUSTER_WITHIN_SOURCE_WINDOW"
    best=ranking[0]
    if best["score"]<.35:return None,ranking[:3],"LOW_EVIDENCE"
    if len(ranking)>1 and ranking[1]["score"]>.82*best["score"]:
        label="AMBIGUOUS_MULTI_GROUP"
    else:
        label="UNVERIFIED_CANDIDATE"
    # The selected center must represent flame cores, not wall halo.
    return [round(best["center_px"][0]/720,5),
            round(best["center_px"][1]/1280,5)],ranking[:3],label

def main():
    base=load_module(PILOT,"pilot")
    previous=json.loads(LAST.read_text())
    refs={n["shot_id"]:n for n in previous["nodes"]}
    assert len(refs)==7
    assert base.digest(base.SRC)==base.SHA
    model=YOLO("yolo11n-seg.pt")
    assert base.digest(pathlib.Path("yolo11n-seg.pt"))==previous["detection_model_sha256"]
    shots={s["id"]:s for s in json.loads(base.EDL.read_text())["timeline"]}
    cw,ch=1070,580
    large=Image.new("RGB",(cw,7*ch),(16,17,18))
    painter=ImageDraw.Draw(large)
    results=[]
    atlas={}
    for n,sid in enumerate(base.FRAMES):
        sh=shots[sid];fr=(sh["start_frame"]+sh["end_frame_exclusive"]-1)//2
        rgb=base.frame_at(fr)
        protected,bboxes,person_boxes,instances=base.individuals(rgb,model)
        cores,threshold=multiscale_luminous_cores(rgb,protected)
        groups=merge_nearby(cores)
        source_results=[]
        # person mask exclusion applies AFTER constructing a local proposed
        # candle footprint; no video effects or flame geometry edits.
        valid_render_sources=0
        safe_union=np.zeros(protected.shape,dtype=bool)
        for idx,old in enumerate(refs[sid]["source_candidates"]):
            hint=old["po_directional_hint"]
            chosen,top,status=choose_cluster(groups,hint)
            limited=np.zeros(protected.shape,dtype=np.uint8)
            if chosen is not None:
                x=int(chosen[0]*720);y=int(chosen[1]*1280)
                cv2.ellipse(limited,(x,y),(24,37),0,0,360,1,-1)
                preliminary=int(np.count_nonzero(limited))
                lost=int(np.count_nonzero((limited>0)&protected))
                limited=limited & (~protected)
                valid_render_sources+=int(np.count_nonzero(limited)>0)
                safe_union|=limited
            else:
                preliminary=lost=0
            source_results.append({"fixture_index":idx+1,"po_directional_search_hint":hint,
                "candidate_center":chosen,
                "status":"CALIBRATION_REQUIRED" if status!="UNVERIFIED_CANDIDATE" else "VISUAL_REVIEW_REQUIRED",
                "diagnostic_group_ranking":top,
                "core_cluster_algorithm_flag":status,
                "person_exclusion_applied":True,
                "hypothetical_core_halo_pre_exclusion_pixels":preliminary,
                "hypothetical_core_halo_excluded_person_pixels":lost,
                "proposed_source_registration_approved":False})
        assert np.count_nonzero(safe_union & protected)==0,"PROTECTED_PEOPLE_INTERSECT_DRAFT_LIGHT"
        # The proposed protected mask is only a diagnostic footprint,
        # not a precise flame segmentation or a production-approved halo.
        out=rgb.astype(float).copy()
        out[protected]=out[protected]*.53+np.array([28,103,255])*.47
        out[safe_union]=out[safe_union]*.56+np.array([40,250,140])*.44
        composited=Image.fromarray(np.clip(out,0,255).astype(np.uint8))
        draw=ImageDraw.Draw(composited)
        for s in source_results:
            hint=s["po_directional_search_hint"]
            x=int(hint[0]*720);y=int(hint[1]*1280)
            draw.ellipse((x-9,y-9,x+9,y+9),outline=(255,30,202),width=3)
            if s["candidate_center"]:
                x=int(s["candidate_center"][0]*720)
                y=int(s["candidate_center"][1]*1280)
                draw.line((x-10,y,x+10,y),fill="white",width=3)
                draw.line((x,y-10,x,y+10),fill="white",width=3)
        x0=n*ch
        orig=Image.fromarray(rgb).crop((0,0,720,760)).resize((515,530),Image.Resampling.LANCZOS)
        modified=composited.crop((0,0,720,760)).resize((515,530),Image.Resampling.LANCZOS)
        large.paste(orig,(5,x0+33));large.paste(modified,(547,x0+33))
        painter.text((5,x0+3),f"{sid} | original",font=font(20),fill="white")
        painter.text((547,x0+3),"Blue: person / Green: safe pilot halo",font=font(17),fill="white")
        record={
            "shot_id":sid,"frame_index":fr,"person_segmentation_mask_pct":refs[sid]["segmentation_protected_area_pct"],
            "bright_pixel_components":len(cores),"grouped_source_clusters":len(groups),
            "source_results":source_results,
            "proposed_halo_mask_and_person_overlap_pixels":0,
            "source_registration_gate":"HOLD",
            "person_gate":"HOLD_PENDING_UNDETECTED_PERSON_REVIEW"}
        results.append(record)
        atlas[sid]={"frame_index":fr,"sources":source_results,
            "profile_status":"DRAFT_UNAPPROVED_DO_NOT_RENDER",
            "personal_protection_method":"YOLO instance masks dilated 13px, unknown misses to visually review"}
    OUT.mkdir(parents=True,exist_ok=True)
    pic=OUT/PIC;large.save(pic,"JPEG",quality=80,optimize=True)
    (OUT/(PIC+".b64.txt")).write_text(base64.b64encode(pic.read_bytes()).decode()+"\n")
    report={"gate":"M01_V002_LIGHT_AND_PERSON_REGISTRATION_G1C_DIAGNOSTIC",
        "status":"DIAGNOSTIC_COMPLETED_PRODUCTION_BLOCKED",
        "source_sha256":base.SHA,
        "person_model_sha256":previous["detection_model_sha256"],
        "candidate_detection":"warm and near-white compact luminous cores, clustered by nearby geometry",
        "exclusions":"13px dilated segmentation subtracted from each diagnostic candidate",
        "compliance_caveat":"mask-person zero overlap is by construction; does not establish missed-person protection or correct flame localization",
        "candidate_atlas_is_approved":False,"stop_on_unknown_or_ambiguous":True,
        "modified_v007_or_master":False,"rendered_mp4":False,
        "source_frames":7,"source_reports":results,
        "preview_file":PIC,"preview_sha256":h(pic)}
    (OUT/JSON).write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    (OUT/ATLAS).write_text(json.dumps({
        "schema":"M01_V002_SCENE_LIGHT_ATLAS_CANDIDATES_V001",
        "status":"DRAFT_UNAPPROVED","no_batch_render_authority":True,
        "source_video_sha256":base.SHA,"profiles":atlas},ensure_ascii=False,indent=2)+"\n")
    print("LIGHT_G1C_DIAGNOSTIC_CREATED")
    print("SOURCE_NODES",len(results))
    print("CANDIDATE_PRESENT",sum(s["candidate_center"] is not None for r in results for s in r["source_results"]))
    print("CANDIDATE_MISSING",sum(s["candidate_center"] is None for r in results for s in r["source_results"]))
    print("PRODUCTION_READY=FALSE")
    print("PREVIEW_SHA256",h(pic))
if __name__=="__main__":main()
