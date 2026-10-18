#!/usr/bin/env python3
"""Inspect actual S02-B V018 source frames before choosing Foley cues.
No render candidate and no modifications to approved media.
"""
from pathlib import Path
import hashlib,json,subprocess,io
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"production/environment_dynamic/review_candidates/S02_B_M01_V018_FULL_LENGTH_C_VISIBLE_REVIEW/S02_B_M01_V018_FULL_LENGTH_MORE_VISIBLE_C_GROUP_PREVIEW_V001.mp4"
OUT=ROOT/"production/video_candidates/review/s02b_full_spatial_audio_v001"
FRAMES=[
 ("N16 A",30),("N16 A",115),("N16 B",190),("N16 B",260),
 ("N17",360),("N17",530),("N17",620),("N18",720),
 ("N18",825),("N19",865),("N19",925),("N20",968),
 ("N20",988),("NEW-01",1040),("REACTION",1095),("N21",1170),
 ("A06",1475),("A06",1540),("A06 / Guang Yong J-cut",1571),("N24",1600)]
hash_=hashlib.file_digest(open(SRC,"rb"),"sha256").hexdigest()
assert hash_=="6897b1ac246e4c30d84aca3b80003a58d7bae86eb7631272fe28253b23a01427"
OUT.mkdir(parents=True,exist_ok=True)
w,h=180,320
sheet=Image.new("RGB",(5*w,4*(h+26)),(16,16,16))
draw=ImageDraw.Draw(sheet)
details=[]
for i,(name,n) in enumerate(FRAMES):
    raw=subprocess.run(["ffmpeg","-loglevel","error","-i",str(SRC),"-vf",
       f"select=eq(n\\,{n}),scale={w}:{h}","-frames:v","1","-f","image2pipe","-vcodec","mjpeg","pipe:1"],capture_output=True,check=True).stdout
    im=Image.open(io.BytesIO(raw)).convert("RGB")
    x=(i%5)*w;y=(i//5)*(h+26)
    sheet.paste(im,(x,y+26))
    draw.text((x+4,y+6),f"{name} {n/30:.2f}s",fill="white")
    details.append({"shot":name,"frame":n,"time":n/30})
sheet.save(OUT/"S02B_FOLEY_CUE_EARLY_FRAMES_CONTACT_V001.jpg",quality=88)
(OUT/"S02B_FOLEY_CUE_EARLY_FRAMES_V001.json").write_text(json.dumps({
"input_SHA256":hash_,"frames":details,
"caveat":"Contact sheet is evidence of visible posture only. Static storyboard depiction of walking does not prove audible real-time footsteps; PO audio review required.",
"no_video_or_audio_change":True},ensure_ascii=False,indent=2))
print("FRAME_CONTACT_SUCCESS",len(FRAMES),flush=True)
