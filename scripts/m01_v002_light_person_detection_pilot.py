#!/usr/bin/env python3
"""M01 V002 source localization and person protection pilot, seven known failures.
No rendering or changing approved shots. Candidate flame centers are not approved
until visual review. Model detect/segmentation must be available; no fake PASS.
"""
import hashlib,io,json,math,pathlib,subprocess,platform
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import cv2
from ultralytics import YOLO
import ultralytics

ROOT=pathlib.Path(__file__).resolve().parents[1]
INPUT=ROOT/"production/video_candidates/assets/S02_B_V006_CINEMATIC_ROUGH_RECONSTRUCTED_CANDIDATE_V001.mp4"
EDL=ROOT/"production/editorial_specs/S02_B_V006_CINEMATIC_ROUGH_EDL_V001.json"
OUTPUT=ROOT/"_m01_v002_flame_person_detection_pilot"
BASE_SHA="7af0982385c877b159f053233378b98c2c035ce19df257a6e65077dfbaa33402"
W,H=720,1280
# Current V007 anchor coordinates, used as *search vicinity*, never trusted identities.
OLD={
 "N16_PART_1":[(.894,.105)],
 "N18":[(.810,.180),(.875,.195)],
 "N20_FIRST":[(.116,.183),(.479,.217),(.835,.208)],
 "V006_NEW_01":[(.125,.188),(.494,.206),(.926,.168)],
 "N21":[(.608,.172),(.893,.182)],
 "A06":[(.086,.355),(.894,.311)],
 "N24":[(.091,.179),(.888,.208)],
}
# Draft PO direction adjustments (not exact flame positions).
PROPOSED={
 "N16_PART_1":[(.894,.055)],
 "N18":[(.910,.155),(.940,.170)],
 "N20_FIRST":[(.191,.183),(.539,.217),(.940,.208)],
 "V006_NEW_01":[(.205,.188),(.614,.206),(.966,.168)],
 "N21":[(.518,.172),(.848,.182)],
 "A06":[(.146,.270),(.959,.236)],
 "N24":[(.091,.179),(.973,.208)],
}
assert set(OLD)==set(PROPOSED)
OUT_NAME="M01_V002_AUTO_LIGHT_AND_PERSON_PROTECTION_PILOT_V001.jpg"
REPORT_NAME="M01_V002_AUTO_LIGHT_AND_PERSON_PROTECTION_PILOT_V001.json"

def get_sha(path):
    s=hashlib.sha256()
    with open(path,"rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""):s.update(b)
    return s.hexdigest()

def snap(frame_index):
    t=(frame_index+.5)/30
    raw=subprocess.check_output(["ffmpeg","-hide_banner","-loglevel","error",
        "-ss",f"{t:.6f}","-i",str(INPUT),"-frames:v","1",
        "-f","image2pipe","-vcodec","png","-"])
    rgb=np.array(Image.open(io.BytesIO(raw)).convert("RGB"))
    assert rgb.shape==(H,W,3)
    return rgb

def person_protection(rgb,model):
    detections=model.predict(rgb,conf=.14,iou=.55,classes=[0],imgsz=960,
        retina_masks=True,verbose=False,device="cpu")[0]
    hard=np.zeros((H,W),dtype=np.uint8)
    boxes=[]
    if detections.boxes is None:return hard,boxes
    for j,bb in enumerate(detections.boxes):
        conf=float(bb.conf[0])
        x0,y0,x1,y1=[int(round(float(z))) for z in bb.xyxy[0]]
        x0=max(0,x0-12);x1=min(W,x1+12);y0=max(0,y0-16);y1=min(H,y1+16)
        # Conservative bbox exclusion: even if segmentation misses dark face or coat,
        # keep entire detected person rectangle protected.
        hard[y0:y1,x0:x1]=255
        boxes.append({"id":j+1,"score":round(conf,3),"bbox":[x0,y0,x1,y1]})
    # Also include expanded instance masks if the model supports masks, for proof.
    if detections.masks is not None:
        kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(17,17))
        for m in detections.masks.data.cpu().numpy():
            if m.shape!=(H,W):m=cv2.resize(m.astype("float32"),(W,H),interpolation=cv2.INTER_NEAREST)
            dilated=cv2.dilate((m>.4).astype(np.uint8),kernel)
            hard[dilated>0]=255
    return hard,boxes

def core_candidates(rgb,block):
    # Warm, high-luminance practical-light pixel candidates, excluding people,
    # window daylight (roughly neutral or bluish) and large uniform wall areas.
    f=rgb.astype(np.int16)
    red=f[:,:,0];green=f[:,:,1];blue=f[:,:,2]
    warm=(red>=180)&(green>=132)&(red>=green+7)&(green>=blue+16)
    warm&=(red-green<=110)&(green-blue<=140)
    # strong compact cores and near flame edges, not any warm shadow.
    warm&=(((red+green)//2)>=171)
    warm&=(block==0)
    bin=(warm.astype(np.uint8)*255)
    n,labels,stats,centroids=cv2.connectedComponentsWithStats(bin,8)
    out=[]
    for i in range(1,n):
        x,y,w,h,area=[int(v) for v in stats[i]]
        if not 1<=area<=280:continue
        if w>35 or h>58:continue
        cx,cy=centroids[i]
        if cy>650:continue # pilot flames only in architecture-upper half
        sample=rgb[max(0,y-2):min(H,y+h+2),max(0,x-2):min(W,x+w+2)]
        peak=int(sample.max(axis=2).max())
        color_mean=np.mean(sample.reshape(-1,3),axis=0).tolist()
        out.append({"center":[float(cx),float(cy)],"rect":[x,y,w,h],
                    "area":area,"peak":peak,"mean_rgb":[round(v,1) for v in color_mean]})
    return out,bin

def locate_one(components,hint,source_number):
    hx,hy=hint
    # Search 0.13 * W horizontally and 0.12 * H vertically, clamp to frame.
    # Proposals merely guide ROI; no confident match means human review.
    x0,y0=hx*W,hy*H
    scored=[]
    for c in components:
        dx=(c["center"][0]-x0)/W;dy=(c["center"][1]-y0)/H
        if abs(dx)>.135 or abs(dy)>.135:continue
        prox=math.exp(-.5*((dx/.066)**2+(dy/.065)**2))
        area=min(c["area"],20)
        bright=c["peak"]/255
        score=round(prox*(.7+.3*bright)*(1+min(area,12)/18),4)
        scored.append({**c,"match_score":score,
                       "distance_normalized":[round(dx,4),round(dy,4)]})
    scored.sort(key=lambda x:x["match_score"],reverse=True)
    top=scored[:3]
    if not top:return{"id":source_number,"proposal":[hx,hy],"status":"NO_FLAME_CORE_FOUND",
                       "candidates":[],"flame_core_center":None}
    # Pixel-level centers are candidates only. Confidence is NOT calibrated.
    best=top[0]
    ambiguity=len(top)>1 and top[1]["match_score"]>.80*best["match_score"]
    return{"id":source_number,"proposal":[hx,hy],
        "status":"MULTIPLE_CORE_CANDIDATES" if ambiguity else "SINGLE_UNVERIFIED_CANDIDATE",
        "flame_core_center":[round(best["center"][0]/W,5),
                             round(best["center"][1]/H,5)],
        "candidates":top}

def main():
    assert get_sha(INPUT)==BASE_SHA
    edl=json.loads(EDL.read_text())["timeline"]
    lookup={s["id"]:s for s in edl}
    model=YOLO("yolo11n-seg.pt")
    weight=pathlib.Path("yolo11n-seg.pt")
    assert weight.is_file(),"DETECTION_WEIGHT_MISSING_STOP"
    model_sha=get_sha(weight)
    WIDE=1100;ROW=638
    canvas=Image.new("RGB",(WIDE,ROW*len(OLD)),(16,17,18))
    pen=ImageDraw.Draw(canvas)
    report=[]
    for i,sid in enumerate(OLD):
        shot=lookup[sid]
        fr=(shot["start_frame"]+shot["end_frame_exclusive"]-1)//2
        rgb=snap(fr)
        protected,people=person_protection(rgb,model)
        components,core_bin=core_candidates(rgb,protected)
        srcs=[locate_one(components,p,j+1) for j,p in enumerate(PROPOSED[sid])]
        # Actual protection masks rendered cyan-blue translucent; warm source cores yellow.
        viz=rgb.copy().astype("float32")
        blue=np.array([38,110,250],dtype=np.float32)
        viz[protected>0]=viz[protected>0]*.52+blue*.48
        # Raw source color hit components, only to diagnose false positives.
        viz[core_bin>0]=viz[core_bin>0]*.3+np.array([255,247,35])*.7
        vis=Image.fromarray(np.clip(viz,0,255).astype(np.uint8))
        painter=ImageDraw.Draw(vis)
        # old points red and proposed search hints magenta; actual detected cores green.
        for j,xy in enumerate(OLD[sid]):
            px,py=int(xy[0]*W),int(xy[1]*H)
            painter.ellipse((px-9,py-9,px+9,py+9),outline=(255,46,52),width=4)
        for j,xy in enumerate(PROPOSED[sid]):
            px,py=int(xy[0]*W),int(xy[1]*H)
            painter.ellipse((px-14,py-14,px+14,py+14),outline=(252,28,210),width=3)
            painter.text((px+14,py-18),f"P{j+1}",fill=(255,255,255),stroke_width=2,stroke_fill="black")
        for loc in srcs:
            xy=loc["flame_core_center"]
            if xy is None:continue
            px,py=int(xy[0]*W),int(xy[1]*H)
            painter.line((px-12,py,px+12,py),fill=(55,255,94),width=3)
            painter.line((px,py-12,px,py+12),fill=(55,255,94),width=3)
            painter.text((px+14,py+4),f"D{loc['id']}",fill=(90,255,95),stroke_width=2,stroke_fill="black")
        # show full image at smaller scale next to readable upper-half detail crop
        thumb=vis.resize((352,626),Image.Resampling.LANCZOS)
        upper=vis.crop((0,0,W,650)).resize((720,590),Image.Resampling.LANCZOS)
        yy=i*ROW
        canvas.paste(thumb,(5,yy+6))
        canvas.paste(upper,(366,yy+6))
        pen.text((371,yy+598),f"{sid} | sources={len(srcs)} | person_boxes={len(people)} | detection cores={len(components)}",
                 fill=(255,255,255))
        report.append({"node":sid,"mid_frame":fr,"sample_time":round((fr+.5)/30,3),
            "protection_method":"YOLO11N_SEG_INSTANCE_UNION_WITH_EXPANDED_PERSON_BOUNDING_BOXES",
            "person_boxes":people,
            "person_protected_pixel_count":int(np.count_nonzero(protected)),
            "person_protected_fraction":round(float(np.mean(protected>0)),5),
            "candidate_warm_components":len(components),
            "source_results":srcs,
            "light_registration":"NOT_APPROVED",
            "human_mask_quality":"VISUAL_REVIEW_PENDING",
            "auto_render_eligible":False})
    OUTPUT.mkdir(exist_ok=True)
    imgpath=OUTPUT/OUT_NAME
    canvas.save(imgpath,"JPEG",quality=82,optimize=True)
    statement={
      "task":"M01_V002_AUTO_LIGHT_PERSON_LOCALIZATION_PILOT",
      "status":"DIAGNOSTIC_ONLY_FAIL_CLOSED",
      "source_video_sha256":BASE_SHA,
      "segmentation_model":"ultralytics:yolo11n-seg.pt",
      "segmentation_model_sha256":model_sha,
      "ultralytics_version":ultralytics.__version__,
      "python_version":platform.python_version(),
      "light_core_detector":"deterministic warm high-value localized connected components",
      "flame_candidate_confidence":"NOT_VALIDATED_CALIBRATION",
      "person_protection_policy":"union detected person instance masks + expanded human boxes",
      "human_protection_is_complete":"UNVERIFIED_PENDING_VISUAL_REVIEW",
      "person_undetected_risk":"YES",
      "source_registration_pass":False,
      "reuse_as_production_light_atlas":False,
      "full_video_render_allowed":False,
      "no_new_video_or_story_shot":True,
      "originals_unchanged":get_sha(INPUT)==BASE_SHA,
      "no_main_merge":True,
      "contact_sheet":OUT_NAME,
      "contact_sheet_sha256":get_sha(imgpath),
      "legend":{
        "red_ring":"old V007 estimated anchor",
        "magenta_ring":"PO direction corrected search hint, not confirmed",
        "green_cross":"detected candidate warm bright source, not visually approved",
        "yellow_pixels":"warm high-luminance classifier proposals; includes false positives",
        "blue_regions":"person protection regions (detected people only)"
      },
      "shots":report}
    (OUTPUT/REPORT_NAME).write_text(json.dumps(statement,ensure_ascii=False,indent=2)+"\n")
    print("M01_V002_LIGHT_AND_PERSON_DIAGNOSTIC_ONLY=TRUE")
    print("PERSON_CANDIDATES",sum(len(x["person_boxes"]) for x in report))
    print("FLAME_CANDIDATES",sum(len(x["source_results"]) for x in report))
    print("MODEL_WEIGHT_SHA256",model_sha)
    print("STILL_NEEDS_PO_ALIGNMENT_AND_HUMAN_PROTECTION_REVIEW=TRUE")
if __name__=="__main__":main()
