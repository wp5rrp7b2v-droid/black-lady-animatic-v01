#!/usr/bin/env python3
"""Extract midframes from exact S02-B V006 for full-timeline candle atlas extension.

No light coordinates, masks, or video effects are guessed at this stage.
The images are evidence of the actual 720x1280 source frames, source SHA checked.
"""
import base64,hashlib,json,pathlib,subprocess
import numpy as np
from PIL import Image,ImageDraw,ImageFont
ROOT=pathlib.Path(__file__).resolve().parents[1]
SOURCE=ROOT/"production/video_candidates/assets/S02_B_V006_CINEMATIC_ROUGH_RECONSTRUCTED_CANDIDATE_V001.mp4"
SHA="7af0982385c877b159f053233378b98c2c035ce19df257a6e65077dfbaa33402"
EDL=ROOT/"production/editorial_specs/S02_B_V006_CINEMATIC_ROUGH_EDL_V001.json"
OUT=ROOT/"_s02b_v017_registration_frames"
TARGETS={"N16_PART_1","N18","N20_FIRST","V006_NEW_01","JUN_APPROVED_REACTION","N21","N22_FIRST",
 "A06","N24","N25","NING_REACTION_APPROVED","N26"}
W,H,FPS=720,1280,30
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read_exact(stream,n):
 out=[]
 while n:
  x=stream.read(n)
  if not x:raise RuntimeError("INPUT_VIDEO_DECODE_SHORT")
  out.append(x);n-=len(x)
 return b"".join(out)
def save_jpeg(image,path):
 image.save(path,quality=84,optimize=True,subsampling=0)
 data=path.read_bytes()
 encoded=base64.b64encode(data).decode("ascii")
 path.with_suffix(".b64.txt").write_text("\n".join(encoded[i:i+4000] for i in range(0,len(encoded),4000))+"\n")
 return {"file":path.name,"bytes":len(data),"sha256":digest(path),"base64_text":path.with_suffix(".b64.txt").name}
def run():
 OUT.mkdir(exist_ok=True)
 assert digest(SOURCE)==SHA
 edl=json.loads(EDL.read_text())["timeline"]
 assert len(edl)==17 and edl[-1]["end_frame_exclusive"]==1927
 assert TARGETS.issubset({e["id"] for e in edl})
 wanted={e["start_frame"]+(e["end_frame_exclusive"]-e["start_frame"])//2:e for e in edl if e["id"] in TARGETS}
 assert len(wanted)==12
 dec=subprocess.Popen(["ffmpeg","-hide_banner","-v","error","-xerror","-i",str(SOURCE),
  "-map","0:v:0","-vsync","0","-pix_fmt","rgb24","-f","rawvideo","pipe:1"],stdout=subprocess.PIPE)
 files=[];tiles=[]
 try:
  for idx in range(1927):
   buf=read_exact(dec.stdout,W*H*3)
   if idx not in wanted:continue
   seg=wanted[idx];shot=seg["id"]
   image=Image.frombytes("RGB",(W,H),buf)
   shotdir=OUT/shot;shotdir.mkdir(exist_ok=True)
   frame=shotdir/f"{shot}_EXACT_SOURCE_MIDFRAME_{idx}.jpg"
   meta=save_jpeg(image,frame)
   files.append({"shot":shot,"frame_index":idx,"start_frame":seg["start_frame"],
    "end_frame_exclusive":seg["end_frame_exclusive"],"decoded_rgb_sha256":hashlib.sha256(buf).hexdigest(),**meta})
   tile=image.copy().resize((288,512),Image.Resampling.LANCZOS)
   tiles.append((shot,tile))
  assert not dec.stdout.read(1)
 finally:dec.stdout.close()
 assert dec.wait()==0
 try:font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",16)
 except OSError:font=ImageFont.load_default()
 for batch in range(0,len(tiles),6):
  group=tiles[batch:batch+6]
  sheet=Image.new("RGB",(3*294,2*540),(14,14,16))
  for i,(shot,tile) in enumerate(group):
   x=(i%3)*294;y=(i//3)*540
   sheet.paste(tile,(x,y+23))
   ImageDraw.Draw(sheet).text((x+5,y+3),shot,font=font,fill=(255,255,255))
  save_jpeg(sheet,OUT/f"S02B_V017_REGISTRATION_CONTACT_{batch//6+1:02d}.jpg")
 manifest={"schema":"S02B_M01_V017_SOURCE_MIDFRAME_EVIDENCE",
  "status":"EXACT_SOURCE_FRAMES_EXTRACTED_REGISTRATION_GT_NOT_APPROVED",
  "source_sha256":SHA,"frame_shape":[720,1280],"total_frames":1927,
  "full_timeline_nodes":17,"registration_suspect_shots":sorted(TARGETS),
  "registered_existing_shots":["N17","V006_NEW_02","N23"],
  "source_without_candle_or_uncertain":["N16_PART_2","N19"],
  "source_frames":files,"no_guessed_flame_positions":True,
  "no_old_rejected_V007_mask_reuse":True,"no_video_created":True,"no_canonical_publication":True}
 (OUT/"S02B_V017_SOURCE_MIDFRAME_MANIFEST.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
 print("S02B_V017_SOURCE_FRAMES_EXTRACTED",len(files),flush=True)
if __name__=="__main__":run()
