#!/usr/bin/env python3
"""M01 V002 second light/people diagnostic; never generates video, never auto-approves.
Reusable scene-local registration candidate logic; no blanket boxes in protective
segmentation. Proof that a light candidate and its human exclusions are independent.
"""
from __future__ import annotations
import base64,hashlib,io,json,pathlib,subprocess,importlib.util,platform,math
import numpy as np,cv2,ultralytics
from ultralytics import YOLO
from PIL import Image, ImageDraw, ImageFont

ROOT=pathlib.Path(__file__).resolve().parents[1]
SRC=ROOT/"production/video_candidates/assets/S02_B_V006_CINEMATIC_ROUGH_RECONSTRUCTED_CANDIDATE_V001.mp4"
OLD_REPORT=ROOT/"production/environment_dynamic/review_candidates/M01_V002_LIGHT_PERSON_DETECTION_PILOT_V001/M01_V002_AUTO_LIGHT_AND_PERSON_PROTECTION_PILOT_V001.json"
EDL=ROOT/"production/editorial_specs/S02_B_V006_CINEMATIC_ROUGH_EDL_V001.json"
OLD_RENDER=ROOT/"scripts/s02b_v007_full_m01_with_ab_20261017.py"
OUT=ROOT/"_m01_v002_registration_refine_v002"
SHA="7af0982385c877b159f053233378b98c2c035ce19df257a6e65077dfbaa33402"
W,H=720,1280
PIC="M01_V002_FLAME_PERSON_MASK_REFINEMENT_V002.jpg"
REPORT="M01_V002_FLAME_PERSON_MASK_REFINEMENT_V002.json"
FRAMES=["N16_PART_1","N18","N20_FIRST","V006_NEW_01","N21","A06","N24"]
LABEL={ "N16_PART_1":"N16","N18":"N18","N20_FIRST":"N20",
        "V006_NEW_01":"NEW-01","N21":"N21","A06":"A06","N24":"N24" }
def digest(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for blk in iter(lambda:f.read(1048576),b""):h.update(blk)
    return h.hexdigest()

def frame_at(fr):
    t=(fr+.5)/30
    raw=subprocess.check_output(["ffmpeg","-v","error","-ss",f"{t:.6f}",
        "-i",str(SRC),"-frames:v","1","-f","image2pipe","-vcodec","png","-"])
    pic=np.array(Image.open(io.BytesIO(raw)).convert("RGB"))
    assert pic.shape==(H,W,3)
    return pic

def individuals(rgb,net):
    results=net.predict(rgb,classes=[0],imgsz=960,conf=.14,iou=.55,retina_masks=True,
        verbose=False,device="cpu")[0]
    seg=np.zeros((H,W),np.uint8)
    bbox=np.zeros((H,W),np.uint8)
    details=[]
    n=len(results.boxes) if results.boxes is not None else 0
    arr=results.masks.data.cpu().numpy() if results.masks is not None else np.empty((0,H,W))
    matched_seg=0
    for j in range(n):
        d=results.boxes[j]
        xy=np.array(d.xyxy[0].cpu()).astype(int)
        x0,y0,x1,y1=[int(v) for v in xy]
        x0=max(0,x0-10);y0=max(0,y0-10);x1=min(W,x1+10);y1=min(H,y1+10)
        bbox[y0:y1,x0:x1]=255
        if j<len(arr):
            m=arr[j]
            if m.shape!=(H,W):m=cv2.resize(m.astype(np.float32),(W,H),interpolation=cv2.INTER_NEAREST)
            seg[m>.45]=255
            matched_seg+=1
        details.append({"box_id":j+1,"confidence":round(float(d.conf[0]),3),"expanded_box":[x0,y0,x1,y1],
            "has_instance_mask":j<len(arr)})
    # Tight but cautious 13-pixel dilation around actually segmented human silhouettes.
    seg=cv2.dilate(seg,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(27,27)))
    # Do NOT mark all bbox pixels as people; huge bboxes in prior pilot hid lights.
    # Instead record areas that only bbox would protect and fail-closed until visual review.
    return seg>0,bbox>0,details,matched_seg

def candidate_flames(rgb,person_mask):
    a=rgb.astype(np.int16)
    r,g,b=a[:,:,0],a[:,:,1],a[:,:,2]
    # Flame cores: bright yellow/amber, high warm chroma, limited geometry.
    pixels=(r>=181)&(g>=121)&((r-b)>=55)&((g-b)>=25)&(r>=g+3)
    pixels&=(np.indices((H,W))[0]<.42*H)
    pixels&=~person_mask
    mask=(pixels.astype(np.uint8)*255)
    n,lab,stats,centroids=cv2.connectedComponentsWithStats(mask,8)
    out=[]
    for i in range(1,n):
        x,y,w,h,area=[int(v) for v in stats[i]]
        if area<2 or area>330 or w>42 or h>64:continue
        patch=rgb[y:y+h,x:x+w]
        rmax=int(patch[:,:,0].max());gmax=int(patch[:,:,1].max())
        if rmax<199 or gmax<133:continue
        cx,cy=centroids[i]
        out.append({"x":round(float(cx),2),"y":round(float(cy),2),"area":area,
             "bbox":[x,y,w,h],"peak_r":rmax,"peak_g":gmax})
    return out,mask

def locate_sources(components,hints,seg,bbox):
    results=[]
    for j,(hx,hy) in enumerate(hints):
        candidates=[]
        for c in components:
            dx=(c["x"]/W-hx);dy=(c["y"]/H-hy)
            if abs(dx)>.15 or abs(dy)>.14:continue
            # More weight to compact luminous flame core than soft wall halo.
            dist=(dx/.07)**2+(dy/.065)**2
            score=math.exp(-.5*dist)*(.7+.3*min(c["area"],18)/18)
            candidates.append((score,c))
        candidates.sort(reverse=True,key=lambda x:x[0])
        ranked=[{"center_px":[z["x"],z["y"]],
            "normalized_center":[round(z["x"]/W,5),round(z["y"]/H,5)],
            "score_rank":round(float(s),4),"area":z["area"]} for s,z in candidates[:5]]
        if candidates:
            best=candidates[0][1]
            center=[round(best["x"]/W,5),round(best["y"]/H,5)]
            px,py=int(best["x"]),int(best["y"])
            # Protect up to 13px beyond instance mask when determining proximity.
            min_dist=float(cv2.distanceTransform((~seg).astype(np.uint8),cv2.DIST_L2,5)[py,px]) if 0<=px<W and 0<=py<H else 0.
            ambiguous=len(candidates)>1 and candidates[1][0]>=candidates[0][0]*.85
            flag="MULTIPLE_CANDIDATES" if ambiguous else "VISUAL_CONFIRM_REQUIRED"
            # Lack of segmentation for nearby human and bbox-only zones are ambiguous.
            box_collision=bool(bbox[py,px] and not seg[py,px])
            if box_collision:flag="PERSON_BOX_PROXIMITY_REVIEW_REQUIRED"
        else:
            center=None;min_dist=None;box_collision=False;flag="NO_FLAME_CANDIDATE"
        results.append({
            "source_index":j+1,"po_directional_hint":[hx,hy],
            "candidate_core_center":center,"candidate_status":flag,
            "candidate_center_not_auto_approved":True,
            "possible_human_bbox_overlap":box_collision,
            "distance_to_person_mask_px":round(min_dist,1) if min_dist is not None else None,
            "ranked_candidates":ranked})
    return results

def font(size):
    p="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(p,size) if pathlib.Path(p).exists() else ImageFont.load_default()

def main():
    assert digest(SRC)==SHA
    old=json.loads(OLD_REPORT.read_text())
    assert len(old["shots"])==7
    old_by={s["node"]:s for s in old["shots"]}
    assert set(FRAMES)==set(old_by)
    shots={s["id"]:s for s in json.loads(EDL.read_text())["timeline"]}
    assert set(FRAMES).issubset(shots)
    spec=importlib.util.spec_from_file_location("oldv007",OLD_RENDER)
    old_module=importlib.util.module_from_spec(spec);spec.loader.exec_module(old_module)
    net=YOLO("yolo11n-seg.pt")
    weights=pathlib.Path("yolo11n-seg.pt")
    assert weights.is_file()
    assert digest(weights)==old["segmentation_model_sha256"],"MODEL_CHANGED"
    CW,CH=1040,600
    sheet=Image.new("RGB",(CW,len(FRAMES)*CH),(18,19,21));pen=ImageDraw.Draw(sheet)
    records=[]
    for i,sid in enumerate(FRAMES):
        sh=shots[sid]
        fr=(sh["start_frame"]+sh["end_frame_exclusive"]-1)//2
        rgb=frame_at(fr)
        person,bbox,boxes,instances=individuals(rgb,net)
        cores,pixel_candidates=candidate_flames(rgb,person)
        hints=[o["proposal"] for o in old_by[sid]["source_results"]]
        lights=locate_sources(cores,hints,person,bbox)
        # Old V007 actual pixel effect mask; compare collision against independently
        # segmented people to expose defects without claiming all people are found.
        oldmask=old_module.manual_mask(old_module.ANCHORS[sid])>.08
        unsafe_old=int(np.count_nonzero(oldmask & person))
        unsafe_old_bboxes=int(np.count_nonzero(oldmask & bbox))
        affected_area=int(np.count_nonzero(oldmask))
        # Candidate flame-core masks are sparse raw connected components; never
        # silently allow effect on person, even in regions inside the old mask.
        assert not np.any((pixel_candidates>0)&person)
        canvas=rgb.astype(np.float32).copy()
        canvas[person]=.55*canvas[person]+.45*np.array([25,125,255],dtype=float)
        # Compare old red region, gated after person segmentation.
        unsafe=oldmask & person
        canvas[unsafe]=.50*canvas[unsafe]+.50*np.array([240,26,40],dtype=float)
        overlay=Image.fromarray(np.clip(canvas,0,255).astype(np.uint8))
        draw=ImageDraw.Draw(overlay)
        # Draw old anchor red circle; PO hint magenta; detected source green cross.
        for xy in old_module.ANCHORS[sid]:
            x=int(xy[0]*W);y=int(xy[1]*H)
            draw.ellipse((x-10,y-10,x+10,y+10),outline=(254,42,52),width=4)
        for light in lights:
            x=int(light["po_directional_hint"][0]*W)
            y=int(light["po_directional_hint"][1]*H)
            draw.ellipse((x-13,y-13,x+13,y+13),outline=(254,10,217),width=4)
            p=light["candidate_core_center"]
            if p is not None:
                cx,cy=int(p[0]*W),int(p[1]*H)
                draw.line((cx-14,cy,cx+14,cy),fill=(65,255,102),width=4)
                draw.line((cx,cy-14,cx,cy+14),fill=(65,255,102),width=4)
        # Input + annotation in side-by-side upper 600px crop, source whole frame mini.
        original=Image.fromarray(rgb).crop((0,0,W,760)).resize((498,526))
        proposed=overlay.crop((0,0,W,760)).resize((498,526))
        x0=i*CH
        sheet.paste(original,(5,x0+38));sheet.paste(proposed,(530,x0+38))
        pen.text((6,x0+8),f"{i+1} {LABEL[sid]} Original",font=font(20),fill="white")
        pen.text((531,x0+8),"Detection + person segmentation",font=font(18),fill="white")
        pen.text((7,x0+571),f"old mask-human overlap: {unsafe_old}px | candidates:{len(cores)} | persons:{len(boxes)}",font=font(14),fill=(225,225,230))
        record={
          "shot_id":sid,"frame_index":fr,"time_seconds":round((fr+.5)/30,3),
          "segmentation_person_instances":instances,
          "detected_person_boxes":boxes,
          "segmentation_protected_area_pct":round(np.mean(person)*100,3),
          "legacy_bbox_protected_area_pct":round(np.mean(bbox)*100,3),
          "bbox_only_not_instance_mask_pct":round(np.mean(bbox & ~person)*100,3),
          "old_v007_mask_pixels":affected_area,
          "old_v007_mask_overlapping_segmentation_pixels":unsafe_old,
          "old_v007_mask_overlapping_detection_boxes_pixels":unsafe_old_bboxes,
          "source_candidates":lights,
          "unmatched_person_risk":"UNKNOWN_REQUIRES_VISUAL_CONFIRMATION",
          "source_localization_pass":False,
          "human_protection_pass":False
        }
        records.append(record)
    OUT.mkdir(exist_ok=True)
    p=OUT/PIC
    sheet.save(p,"JPEG",quality=81,optimize=True)
    (OUT/(PIC+".b64.txt")).write_text(base64.b64encode(p.read_bytes()).decode()+"\n")
    rep={
      "schema":"M01_V002_LIGHT_REGISTRATION_PERSON_PROTECTION_GATE1_V002",
      "status":"DIAGNOSTIC_PASS_FOR_INFORMATION__PRODUCTION_GATE_FAIL",
      "source_video_sha256":SHA,
      "detection_model_sha256":digest(weights),
      "segmentation_version":ultralytics.__version__,
      "python_version":platform.python_version(),
      "person_protection":"instance segmentation enlarged 13px, full bboxes retained as separate diagnostics only",
      "person_bbox_problem":"Full YOLO person bboxes can cover real candles; do not default to bbox as precise segmentation",
      "light_candidates":"warm high-luminance compact components in upper .42 height, PO hints used as search area",
      "not_actual_flame_or_people_truth":"both detectors subject to misses and false positives",
      "visual_core_protection_gate":"NOT_APPROVED",
      "human_safety_gate":"NOT_APPROVED",
      "project_batch_m01":"HOLD",
      "no_video_or_original_png_modified":True,
      "no_main_merge":True,
      "image_file":PIC,"image_sha256":digest(p),
      "total_nodes":len(records),
      "nodes":records,
    }
    (OUT/REPORT).write_text(json.dumps(rep,ensure_ascii=False,indent=2)+"\n")
    print("PILOT_V002_DIAGNOSTIC_SUCCESS_NOT_PRODUCTION_PASS")
    print("OLD_MASK_OVERLAP_COUNT",sum(r["old_v007_mask_overlapping_segmentation_pixels"] for r in records))
    print("CORE_UNRESOLVED",sum(not a["candidate_core_center"] for r in records for a in r["source_candidates"]))
    print("IMAGE_SHA256",digest(p))
if __name__=="__main__":main()
