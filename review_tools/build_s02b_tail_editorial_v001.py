#!/usr/bin/env python3
"""S02-B remaining 42.30-second PO review; only exact approved PNGs + original audio.
No modification, publication, Video Index or Story Shot registration.
"""
import hashlib, json, os, pathlib, re, subprocess
from PIL import Image, ImageDraw

ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=pathlib.Path(os.environ.get("RUNNER_TEMP","/tmp"))/"S02B_TAIL_42S_EDITORIAL_REVIEW_V001"
OUT.mkdir(parents=True,exist_ok=True)
IDX={x["shot_id"]:x for x in map(json.loads,(ROOT/"production/story_shots/story_shot_index.jsonl").read_text().splitlines())}
AUDIO=ROOT/"staging/p0_3_a01_a02_transition_validation/AUDIO_MVP1_CANONICAL_V001.m4a"
AUDIO_SHA="8d0d12d3af5e2c15032912605c0d1b3f3e892fe24918a7064864b136987737a0"
# Twelve editorial phases, with 10 distinct approved shot images.
# Frame spans exactly match V001: 21.950 sec -> 64.250 sec, i.e. 1269 frames at 30 fps.
# Pose = (zoom relative to largest available 9:16 source region, horizontal pan 0..1, vertical pan 0..1).
# Controlled crop >=730px native when source dimensions allow, no generated pixels.
S=[
 {"sid":"N18","name":"JUN_OBSERVES","n":93,"a":(1.03,.50,.46),"b":(1.12,.30,.50),"lead":10,"tail":0},
 {"sid":"N18","name":"LOOK_TO_CLEAR_SKY","n":88,"a":(1.12,.30,.50),"b":(1.18,.08,.45),"lead":0,"tail":18},
 {"sid":"N19","name":"NING_ENTRANCE_REPLY","n":110,"a":(1.02,.46,.50),"b":(1.13,.56,.55),"lead":12,"tail":25},
 {"sid":"N20","name":"WALK_INTO_CASTLE","n":129,"a":(1.00,.50,.50),"b":(1.10,.52,.56),"lead":16,"tail":16},
 {"sid":"N21","name":"COHORT_SCALE","n":144,"a":(1.00,.50,.50),"b":(1.07,.50,.50),"lead":18,"tail":20},
 {"sid":"N22","name":"PEOPLE_IN_FLOW","n":144,"a":(1.02,.51,.50),"b":(1.12,.31,.48),"lead":12,"tail":28},
 {"sid":"N23","name":"NEIL_GROUP_ORIENTATION","n":108,"a":(1.02,.50,.50),"b":(1.14,.12,.50),"lead":12,"tail":0},
 {"sid":"N23","name":"GROUP_DIRECTION_INWARD","n":92,"a":(1.14,.12,.50),"b":(1.07,.75,.45),"lead":0,"tail":15},
 {"sid":"N24","name":"GUANG_YONG_QUESTION","n":65,"a":(1.02,.50,.50),"b":(1.10,.52,.50),"lead":8,"tail":15},
 {"sid":"A06","name":"OPEN_DOOR_DETAIL","n":63,"a":(1.00,.50,.50),"b":(1.04,.50,.48),"lead":12,"tail":16},
 {"sid":"N25","name":"NEIL_RAIN_RULE","n":116,"a":(1.02,.50,.50),"b":(1.10,.56,.53),"lead":13,"tail":18},
 {"sid":"N26","name":"LADY_RULE_FORWARD_HOOK","n":117,"a":(1.00,.50,.50),"b":(1.07,.55,.52),"lead":15,"tail":22},
]
assert sum(x["n"] for x in S)==1269
assert S[0]["b"]==S[1]["a"] and S[6]["b"]==S[7]["a"]
def sha(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(1048576),b""):h.update(b)
 return h.hexdigest()
def gitblob(p):
 a=p.read_bytes(); return hashlib.sha1(("blob "+str(len(a))+"\0").encode()+a).hexdigest()
def ff(cmd, **k):
 print("RUN "+" ".join(map(str,cmd))[:240],flush=True)
 return subprocess.run(list(map(str,cmd)),check=True,**k)
assert AUDIO.stat().st_size==4957338 and sha(AUDIO)==AUDIO_SHA
images={};src={}
for sid in dict.fromkeys(s["sid"] for s in S):
 d=IDX[sid];p=ROOT/d["canonical_path"]
 assert d["approval_status"]=="APPROVED" and d["lifecycle"]=="CURRENT",sid
 assert p.stat().st_size==d["byte_size"],sid+" length"
 assert gitblob(p)==d["github_blob_sha"],sid+" git blob"
 if d.get("sha256_locked_identity"):assert sha(p)==d["sha256_locked_identity"],sid+" sha"
 im=Image.open(p).convert("RGB")
 if d.get("dimensions"):
  assert (im.width,im.height)==(d["dimensions"]["width"],d["dimensions"]["height"])
 images[sid]=im
 src[sid]={"path":d["canonical_path"],"size":p.stat().st_size,"sha256":sha(p),"git_blob":gitblob(p),"dimensions":[im.width,im.height]}
def smooth(t):
 return t*t*(3-2*t)
def interpolate(s,i):
 length=s["n"];lead=s["lead"];tail=s["tail"]
 q=smooth(max(0,min(1,(i-lead)/max(1,length-1-lead-tail))))
 return [a+(b-a)*q for a,b in zip(s["a"],s["b"])]
def frame(s,i):
 im=images[s["sid"]]
 zm,xp,yp=interpolate(s,i)
 base=min(im.width,im.height*9/16)
 cropw=base/zm; croph=cropw*16/9
 # Allow no more than V004's quality-constrained 1.29x zoom.
 assert cropw>=720-0.00001 and zm<=1.29
 x=(im.width-cropw)*xp;y=(im.height-croph)*yp
 x=max(0,min(im.width-cropw,x)); y=max(0,min(im.height-croph,y))
 return im.transform((720,1280),Image.Transform.EXTENT,(x,y,x+cropw,y+croph),Image.Resampling.BICUBIC)
# ffmpeg receives raw RGB frames; source-to-deliverable is one H.264 encode.
output=OUT/"S02B_TAIL_42S_EDITORIAL_REVIEW_V001.mp4"
cmd=["ffmpeg","-hide_banner","-loglevel","error","-y",
 "-f","rawvideo","-pixel_format","rgb24","-video_size","720x1280","-framerate","30","-i","pipe:0",
 "-i",str(AUDIO),
 "-filter_complex","[1:a:0]atrim=start=100.700:duration=42.300,asetpts=PTS-STARTPTS[a]",
 "-map","0:v:0","-map","[a]","-frames:v","1269",
 "-c:v","libx264","-preset","medium","-crf","16","-pix_fmt","yuv420p","-profile:v","high",
 "-c:a","aac","-profile:a","aac_low","-ar","44100","-ac","2","-b:a","192k",
 "-movflags","+faststart",str(output)]
print("BEGIN single-pass source-PNG tail editorial render; expected 1269 frames",flush=True)
proc=subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
thumbs=[];written=0;nodes=[]
try:
 for k,s in enumerate(S,1):
  begin=written
  for i in range(s["n"]):
   im=frame(s,i)
   if i==s["n"]//2:thumbs.append((k,s["sid"],s["name"],im.copy()))
   proc.stdin.write(im.tobytes());written+=1
  nodes.append({"node":k,"sid":s["sid"],"name":s["name"],"absolute_start_frame":658+begin,
                "relative_tail_start_frame":begin,"frames":s["n"],"ending_frame_exclusive":658+written,
                "initial_pose":s["a"],"end_pose":s["b"]})
except Exception:
 proc.stdin.close();proc.kill();raise
proc.stdin.close();err=proc.stderr.read().decode("utf8","replace")
if proc.wait()!=0:raise RuntimeError("FFmpeg failed "+err[-2000:])
assert written==1269
probe=json.loads(subprocess.check_output(["ffprobe","-v","error","-show_entries",
 "format=duration,size:stream=codec_name,codec_type,width,height,nb_frames,sample_rate,channels","-of","json",str(output)],text=True))
video=[x for x in probe["streams"] if x["codec_type"]=="video"]
audio=[x for x in probe["streams"] if x["codec_type"]=="audio"]
assert len(video)==1 and len(audio)==1
assert video[0]["nb_frames"]=="1269" and video[0]["width"]==720 and video[0]["height"]==1280
assert audio[0]["codec_name"]=="aac" and audio[0]["channels"]==2 and audio[0]["sample_rate"]=="44100"
assert abs(float(probe["format"]["duration"])-42.3)<0.06
ff(["ffmpeg","-hide_banner","-loglevel","error","-xerror","-i",output,"-f","null","-"],stdout=subprocess.DEVNULL)
vol=subprocess.run(["ffmpeg","-hide_banner","-nostats","-i",output,"-vn","-af","volumedetect","-f","null","-"],capture_output=True,text=True,check=True)
mean=re.search(r"mean_volume:\s*([-\d.]+) dB",vol.stderr)
assert mean and float(mean.group(1))>-55,"audio missing or silent"
ff(["ffmpeg","-hide_banner","-loglevel","error","-y","-ss","100.700","-i",AUDIO,"-t","42.300",
 "-vn","-c:a","libmp3lame","-q:a","3",OUT/"S02B_TAIL_42S_AUDIO_REVIEW.mp3"])
# Multi-page contact sheet: 12 genuine rendered midpoint frames, never source reference.
tw,th=180,320;sheet=Image.new("RGB",(tw*6,(th+28)*2),(18,20,24));d=ImageDraw.Draw(sheet)
for j,(k,sid,name,im) in enumerate(thumbs):
 x=(j%6)*tw;y=(j//6)*(th+28)
 sheet.paste(im.resize((tw,th),Image.Resampling.LANCZOS),(x,y+28))
 d.text((x+4,y+8),str(k).zfill(2)+" "+sid,fill="white")
sheet.save(OUT/"S02B_TAIL_12_VISUAL_PHASES.jpg",quality=94)
manifest={"status":"REVIEW ONLY / NOT CANONICAL / AWAITING PRODUCT OWNER",
 "source_images":src,"audio_source_sha256":AUDIO_SHA,
 "source_audio_window":[100.700,143.000],
 "relative_S02_B_window":[21.950,64.250],
 "transitions":"12 visual phases, but 10 distinct image sources; 01->02 and 07->08 continuous exact camera paths; other source changes are dialogue/spatial motivated cuts",
 "quality_policy":"minimum 720 source px crop, relative zoom <=1.29, single H.264 encode, no scene repaint/no GIF/no character animation",
 "timeline":nodes,
 "output":{"file":output.name,"sha256":sha(output),"byte_size":output.stat().st_size,"probe":probe,"full_decode":"PASS","non_silent_audio_mean_db":float(mean.group(1))},
 "V004_first_21_95s":"PO APPROVED AND UNMODIFIED / NOT INCLUDED IN THIS TAIL TEST",
 "V001":"APPROVED CANONICAL FULL MASTER UNCHANGED"}
(OUT/"RENDER_MANIFEST.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"result":"PASS","sha256":sha(output),"bytes":output.stat().st_size,"frames":1269,"duration":probe["format"]["duration"],"mean_db":mean.group(1)},ensure_ascii=False),flush=True)
