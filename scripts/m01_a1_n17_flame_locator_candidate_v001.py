#!/usr/bin/env python3
"""N17 F550-F645 actual-candle source localization, no video generation.
Candidate coordinates are appearance-guided, not PO-verified flame Ground Truth.
"""
import base64,hashlib,io,json,math,pathlib,subprocess
import numpy as np
from PIL import Image,ImageDraw,ImageFont
ROOT=pathlib.Path(__file__).resolve().parents[1]
SRC=ROOT/"production/video_candidates/assets/S02_B_V006_CINEMATIC_ROUGH_RECONSTRUCTED_CANDIDATE_V001.mp4"
MAN=ROOT/"production/environment_dynamic/benchmarks/m01_stage_a_v002/evidence/M01_STAGE_A_MACHINE_BENCHMARK_V002.json"
PERSON=ROOT/"production/environment_dynamic/benchmarks/m01_stage_a_v002/evidence/person_mask_proposals/PERSON_PROPOSAL_N17_F0601.png"
OUT=ROOT/"_m01_a1_n17_flames_candidate_v001"
OUT.mkdir(exist_ok=True)
W,H=720,1280
FRAMES=[550,580,601,630,645]
# Physically plausible seeds picked from the F601 source image; objective is to
# reveal, not silently accept, candidate positions. Do not use them as GT.
VISUAL_SEEDS=[(616,87),(630,70),(645,47),(689,83)]
def digest(b):return hashlib.sha256(b).hexdigest()
def font(n):
 p="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
 return ImageFont.truetype(p,n) if pathlib.Path(p).exists() else ImageFont.load_default()
def exact(indices):
 exp="+".join(f"eq(n\\,{i})" for i in sorted(indices))
 p=subprocess.Popen(["ffmpeg","-hide_banner","-loglevel","error","-xerror",
   "-i",str(SRC),"-vf","select="+exp,"-vsync","vfr","-pix_fmt","rgb24","-f","rawvideo","pipe:1"],
   stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 result={}
 try:
  for i in sorted(indices):
   block=[];remaining=W*H*3
   while remaining:
    b=p.stdout.read(remaining)
    if not b:raise RuntimeError("SHORT_FRAME_"+str(i))
    block.append(b);remaining-=len(b)
   raw=b"".join(block)
   result[i]=(np.frombuffer(raw,dtype=np.uint8).reshape(H,W,3).copy(),digest(raw))
  assert p.stdout.read(1)==b""
 finally:p.stdout.close()
 err=p.stderr.read().decode(errors="replace");p.stderr.close()
 assert p.wait()==0,err[-700:]
 return result

def refine_source(rgb,seed):
 x,y=seed
 x0,x1=max(0,x-20),min(W,x+21)
 y0,y1=max(0,y-23),min(H,y+24)
 a=rgb[y0:y1,x0:x1].astype(np.int16)
 yy,xx=np.mgrid[y0:y1,x0:x1]
 red,green,blue=a[:,:,0],a[:,:,1],a[:,:,2]
 candle=(red>=200)&(green>=143)&(red>=green-12)&((green-blue)>=12)&((red-blue)>=32)
 # Seed proximity enforces one physical flame per manually examined neighborhood.
 photometric=(red*.49+green*.44-blue*.09).astype(float)
 dist=(xx-x)**2+(yy-y)**2
 score=np.where(candle,photometric-0.22*dist,-1e6)
 index=np.unravel_index(np.argmax(score),score.shape)
 if not candle.any():return None,0
 return [int(xx[index]),int(yy[index])],int(candle.sum())

def group_overlay(rgb,points,protection=None):
 crop=Image.fromarray(rgb,"RGB").crop((525,0,720,240)).resize((585,720),Image.Resampling.NEAREST)
 if protection is not None:
  m=Image.fromarray(protection.astype("uint8")*255,"L").crop((525,0,720,240)).resize((585,720),Image.Resampling.NEAREST)
  px=np.asarray(crop).copy();blocked=np.asarray(m)>0
  px[blocked]=(px[blocked].astype("float32")*.50+np.array([36,108,248])*.50).astype("uint8")
  crop=Image.fromarray(px,"RGB")
 d=ImageDraw.Draw(crop)
 for i,c in enumerate(points):
  seed=VISUAL_SEEDS[i]
  if c is not None:
   x,y=(c[0]-525)*3,c[1]*3
   r=16
   d.ellipse((x-r-3,y-r-3,x+r+3,y+r+3),outline="black",width=9)
   d.ellipse((x-r,y-r,x+r,y+r),outline="white",width=6)
   d.ellipse((x-r+3,y-r+3,x+r-3,y+r-3),outline=(255,28,206),width=5)
   lx=max(8,min(x+27,417));ly=max(8,min(y-65,654))
   if i==0:ly=max(8,y+28)
   d.line((x,y,lx+5,ly+20),fill=(255,28,206),width=5)
   label=f"F{i+1}: {c[0]},{c[1]}"
   d.rounded_rectangle((lx,ly,lx+len(label)*15+18,ly+35),radius=7,
      fill=(255,28,206),outline="white",width=2)
   d.text((lx+6,ly+4),label,font=font(22),fill="black")
  else:
   x,y=(seed[0]-525)*3,seed[1]*3
   d.ellipse((x-14,y-14,x+14,y+14),outline=(255,182,56),width=5)
 return crop

def main():
 manifest=json.loads(MAN.read_text())
 srcsha=manifest["source_video_sha256"]
 assert digest(SRC.read_bytes())==srcsha
 n17=next(x for x in manifest["samples"] if x["shot_id"]=="N17")
 assert digest(PERSON.read_bytes())==n17["frames"][2]["person_mask_sha256"]
 protect=np.asarray(Image.open(PERSON).convert("L"))>0
 assert protect.shape==(H,W)
 decoded=exact(FRAMES)
 assert decoded[601][1]==n17["frames"][2]["decoded_rgb_sha256"]
 source_panel=Image.new("RGB",(5*605,790),(13,13,16))
 d=ImageDraw.Draw(source_panel)
 tracks=[]
 for k,idx in enumerate(FRAMES):
  rgb,rawsha=decoded[idx]
  choices=[refine_source(rgb,seed) for seed in VISUAL_SEEDS]
  points=[c for c,_ in choices]
  counts=[n for _,n in choices]
  # person map from F601 applies ONLY to F601, no unverified all-frame safety claims
  mask=protect if idx==601 else None
  overlay=group_overlay(rgb,points,mask)
  source_panel.paste(overlay,(k*605+10,48))
  d.text((k*605+14,9),f"F{idx}  t={(idx+.5)/30:.2f}s",font=font(23),fill="white")
  tracks.append({"frame":idx,"time_seconds":round((idx+.5)/30,3),
   "rgb_sha256":rawsha,"detected_local_bright_core_pixels":counts,
   "flames":[{"flame_id":f"N17_RIGHT_SCONCE_01_FLAME_{n+1:02d}",
     "rough_visual_seed_px":list(VISUAL_SEEDS[n]),
     "brightness_peak_candidate_px":point,
     "normalized_coordinate":[round(point[0]/W,6),round(point[1]/H,6)] if point else None,
     "peak_found":point is not None,
     "overlap_F601_machine_person_mask":bool(protect[point[1],point[0]]) if idx==601 and point else None,
     "ground_truth_approved":False
   } for n,point in enumerate(points)]})
 name="M01_A1_N17_F550_F645_FOUR_FLAME_LOCATORS_V001.jpg"
 p=OUT/name;p0=p
 source_panel.save(p,"JPEG",quality=86,optimize=True)
 (OUT/(p.name+".b64.txt")).write_text(base64.b64encode(p.read_bytes()).decode()+"\n")
 single=Image.new("RGB",(1240,790),(12,12,14))
 f601=decoded[601][0]
 original=Image.fromarray(f601,"RGB").crop((525,0,720,240)).resize((585,720),Image.Resampling.NEAREST)
 single.paste(original,(10,55))
 single.paste(group_overlay(f601,[x["brightness_peak_candidate_px"] for x in tracks[2]["flames"]],protect),(635,55))
 pen=ImageDraw.Draw(single)
 pen.text((12,8),"N17  F601 | ORIGINAL ACTUAL CANDLE FLAMES",font=font(26),fill="white")
 pen.text((636,8),"CANDIDATES F1-F4 + PERSON MASK IN BLUE",font=font(22),fill="white")
 p2=OUT/"M01_A1_N17_F601_EXACT_FLAME_CORES_V001.jpg"
 single.save(p2,"JPEG",quality=86,optimize=True)
 (OUT/(p2.name+".b64.txt")).write_text(base64.b64encode(p2.read_bytes()).decode()+"\n")
 result={"schema":"M01_STAGE_A1_N17_LATE_CANDLE_LOCATOR_V001",
 "status":"SOURCE_LOCALIZED_CANDIDATES_PO_VISUAL_REVIEW_PENDING",
 "source_video_sha256":srcsha,
 "fixture_id":"N17_RIGHT_SCONCE_01",
 "physical_fixture_groups":1,
 "source_flames_count_candidate":4,
 "flame_locators_method":"F601 original frame rough visual seeds refined to nearest plausible warm high-luminance core, repeated on F550 F580 F601 F630 F645",
 "visible_window_hypothesis":"F520 not visible, F550 and later visible in inspected frames; exact onset not yet measured",
 "timing_note":"Indices are absolute V006 frames; the whole V006 source is 30 fps",
 "machine_human_protection_F601_sha256":n17["frames"][2]["person_mask_sha256"],
 "human_protection_on_all_frames_approved":False,
 "individual_flame_ground_truth_approved":False,
 "machine_pixel_candidates_not_verified_flame_shapes":True,
 "additional_light_in_background_or_crop_not_ruled_out":True,
 "source_tracks":tracks,
 "annotated_overview":name,"annotated_overview_sha256":digest(p.read_bytes()),
 "f601_review_image":p2.name,"f601_review_image_sha256":digest(p2.read_bytes()),
 "no_video_rendered":True,"no_main_merge":True,
 "atlas_promotion_authorized":False,"m01_batch_gate":"HOLD"}
 (OUT/"M01_A1_N17_LATE_CANDLE_LOCATOR_V001.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
 assert digest(SRC.read_bytes())==srcsha
 print("N17_F601_FOUR_FLAME_CANDIDATE_SOURCE_LOCATED; NO_GT; PERSON_PROTECTION_PENDING",json.dumps({
 "F601_candidates":[x["brightness_peak_candidate_px"] for x in tracks[2]["flames"]],
 "F601_person_collisions":[x["overlap_F601_machine_person_mask"] for x in tracks[2]["flames"]]},ensure_ascii=False))
if __name__=="__main__":main()
