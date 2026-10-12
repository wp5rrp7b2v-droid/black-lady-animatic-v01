#!/usr/bin/env python3
"""S02-B N16/N17 V004 quality-first crop trial; sources never modified."""
import hashlib, json, os, pathlib, re, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = pathlib.Path(os.environ.get("RUNNER_TEMP", "/tmp")) / "S02B_N16_N17_V004_QUALITY_TEST"
OUT.mkdir(parents=True, exist_ok=True)
INDEX = {d["shot_id"]: d for d in map(json.loads, (ROOT/"production/story_shots/story_shot_index.jsonl").read_text().splitlines())}
AUDIO = ROOT/"staging/p0_3_a01_a02_transition_validation/AUDIO_MVP1_CANONICAL_V001.m4a"
AUDIO_SHA = "8d0d12d3af5e2c15032912605c0d1b3f3e892fe24918a7064864b136987737a0"
FPS, SIZE = 30, (720, 1280)
SOURCE_SIZE = (941, 1672)
# Each (x,y,w) describes the visible window of a 941x1672 PO-approved original.
# w>=730 makes every source crop at least 730 native pixels wide for a 720px output;
# max digital relative framing magnification 940/730=1.288, without horizontal upsampling.
SHOTS = [
  {"node": 1, "sid": "N16", "name": "TWO_SHOT_TO_JUN", "frames": 69, "a": (0,0,940), "b": (181,120,760), "lead": 10, "trail": 0},
  {"node": 2, "sid": "N16", "name": "JUN_QUESTION_SLOW_HOLD", "frames": 95, "a": (181,120,760), "b": (196,122,745), "lead": 12, "trail": 18},
  {"node": 3, "sid": "N16", "name": "NING_REPLY_REVERSE", "frames": 117, "a": (0,100,760), "b": (7,112,740), "lead": 11, "trail": 22},
  {"node": 4, "sid": "N17", "name": "RULE_TWO_SHOT_PUSH", "frames": 91, "a": (0,0,940), "b": (0,75,820), "lead": 12, "trail": 0},
  {"node": 5, "sid": "N17", "name": "NING_RULE_GENTLE_CLOSE", "frames": 175, "a": (0,75,820), "b": (0,125,745), "lead": 0, "trail": 55},
  {"node": 6, "sid": "N16", "name": "JUN_ACK_REACTION", "frames": 111, "a": (190,120,750), "b": (207,135,734), "lead": 10, "trail": 18},
]
assert sum(x["frames"] for x in SHOTS) == 658
def sha256(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(1<<20),b""): h.update(b)
 return h.hexdigest()
def gitblob(p):
 data=p.read_bytes()
 return hashlib.sha1(("blob "+str(len(data))+"\0").encode()+data).hexdigest()
def run(args, **kwargs):
 print("RUN "+" ".join(map(str,args))[:500], flush=True)
 return subprocess.run(list(map(str,args)),check=True,**kwargs)
assert AUDIO.stat().st_size==4957338 and sha256(AUDIO)==AUDIO_SHA, "Canonical audio identity failed"
originals={}; raw={}
for sid in ("N16","N17"):
 d=INDEX[sid]; f=ROOT/d["canonical_path"]
 assert d["approval_status"]=="APPROVED" and d["lifecycle"]=="CURRENT"
 assert f.stat().st_size==d["byte_size"], "byte size mismatch"
 assert sha256(f)==d["sha256_locked_identity"],"SHA mismatch"
 assert gitblob(f)==d["github_blob_sha"],"Git blob mismatch"
 im=Image.open(f).convert("RGB")
 assert im.size==SOURCE_SIZE, im.size
 raw[sid]=im
 originals[sid]={"canonical_path":d["canonical_path"],"SHA256":sha256(f),"git_blob":gitblob(f),"byte_size":f.stat().st_size,"dimensions":im.size}
def window(box):
 x,y,w=box; h=w*16/9
 return (x,y,x+w,y+h)
def validate():
 for s in SHOTS:
  for box in (s["a"],s["b"]):
   x,y,w=box;h=w*16/9
   assert w>=730 and w<=940, s
   assert x>=0 and x+w<=SOURCE_SIZE[0] and y>=0 and y+h<=SOURCE_SIZE[1],(s,box)
 assert SHOTS[0]["b"]==SHOTS[1]["a"]
 assert SHOTS[3]["b"]==SHOTS[4]["a"]
validate()
def smooth(p):
 return p*p*(3-2*p)
def pose(spec,i):
 n=spec["frames"]; lead=spec["lead"];trail=spec["trail"]
 p=min(1,max(0,(i-lead)/max(1,n-1-lead-trail)))
 q=smooth(p)
 return tuple(a+(b-a)*q for a,b in zip(spec["a"],spec["b"]))
def make_frame(spec,i):
 crop=window(pose(spec,i))
 return raw[spec["sid"]].transform(SIZE,Image.Transform.EXTENT,crop,resample=Image.Resampling.BICUBIC)
# One PNG-source-to-MP4 video encode, no intermediate MP4 transcodes.
ffmpeg=[
 "ffmpeg","-hide_banner","-loglevel","error","-y",
 "-f","rawvideo","-pixel_format","rgb24","-video_size","720x1280","-framerate","30","-i","pipe:0",
 "-i",str(AUDIO),
 "-filter_complex","[1:a:0]atrim=start=78.750:duration=21.950,asetpts=PTS-STARTPTS[a]",
 "-map","0:v:0","-map","[a]","-frames:v","658",
 "-c:v","libx264","-preset","medium","-crf","16","-pix_fmt","yuv420p","-profile:v","high",
 "-c:a","aac","-profile:a","aac_low","-ar","44100","-ac","2","-b:a","192k",
 "-movflags","+faststart",str(OUT/"S02B_N16_N17_V004_QUALITY_TEST.mp4")
]
print("Rendering 658 frames from exact-source approved PNGs, single H.264 encode",flush=True)
process=subprocess.Popen(ffmpeg,stdin=subprocess.PIPE,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
frames_written=0; keyframes=[]; running_frame=0; previous=None
try:
 for spec in SHOTS:
  for i in range(spec["frames"]):
   frame=make_frame(spec,i)
   # An ultra-short N17->N16 audio-reaction dissolve, 5 frames within node 05.
   if spec["node"]==5 and i>=spec["frames"]-5:
    alpha=(i-(spec["frames"]-5)+1)/6
    frame=Image.blend(frame,make_frame(SHOTS[5],max(0,i-(spec["frames"]-5))),alpha)
   if i in (0,spec["frames"]//2,spec["frames"]-1):
    keyframes.append({"node":spec["node"],"frame":running_frame,"image":frame.copy()})
   process.stdin.write(frame.tobytes())
   frames_written+=1; running_frame+=1
except Exception:
 process.stdin.close()
 process.kill()
 raise
process.stdin.close()
errors=process.stderr.read().decode("utf-8",errors="replace")
code=process.wait()
if code!=0: raise RuntimeError("FFmpeg error "+str(code)+" "+errors[-5000:])
assert frames_written==658
outfile=OUT/"S02B_N16_N17_V004_QUALITY_TEST.mp4"
probe=json.loads(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration,size:stream=index,codec_type,codec_name,profile,width,height,r_frame_rate,nb_frames,sample_rate,channels","-of","json",str(outfile)],text=True))
vs=[v for v in probe["streams"] if v["codec_type"]=="video"]
aud=[a for a in probe["streams"] if a["codec_type"]=="audio"]
assert len(vs)==1 and len(aud)==1
assert vs[0]["nb_frames"]=="658" and (vs[0]["width"],vs[0]["height"])==SIZE
assert aud[0]["codec_name"]=="aac" and aud[0]["sample_rate"]=="44100" and aud[0]["channels"]==2
assert abs(float(probe["format"]["duration"])-21.950)<0.055,probe["format"]["duration"]
run(["ffmpeg","-hide_banner","-loglevel","error","-xerror","-i",outfile,"-f","null","-"],stdout=subprocess.DEVNULL)
v=subprocess.run(["ffmpeg","-hide_banner","-nostats","-i",outfile,"-vn","-af","volumedetect","-f","null","-"],capture_output=True,text=True,check=True)
mean=re.search(r"mean_volume:\s*([-\d.]+) dB",v.stderr)
maxv=re.search(r"max_volume:\s*([-\d.]+) dB",v.stderr)
assert mean and maxv and float(mean.group(1))>-55,"Audio absent/silent"
# Separate MP3 for independent audio review, copied from original canonical source.
run(["ffmpeg","-hide_banner","-loglevel","error","-y","-ss","78.750","-i",AUDIO,"-t","21.950","-vn","-c:a","libmp3lame","-q:a","3",OUT/"S02B_N16_N17_V004_AUDIO_ONLY.mp3"])
# Midpoint preview sheet: preview only; not a reference asset.
mid=[x for x in keyframes if x["frame"]==next(
  sum(k["frames"] for k in SHOTS[:x["node"]-1])+SHOTS[x["node"]-1]["frames"]//2 for _ in [0])]
thumb_w,thumb_h=216,384
sheet=Image.new("RGB",(thumb_w*6,thumb_h+32),(14,16,20))
d=ImageDraw.Draw(sheet)
for j,info in enumerate(mid):
 pic=info["image"].resize((thumb_w,thumb_h),Image.Resampling.LANCZOS)
 sheet.paste(pic,(j*thumb_w,32))
 d.text((j*thumb_w+5,7),f"{info['node']:02d} / {SHOTS[info['node']-1]['sid']}",fill="white")
sheet.save(OUT/"V004_QUALITY_SIX_BEATS.jpg",quality=93,subsampling=0)
pos=0;nodes=[]
for s in SHOTS:
 nodes.append({**{k:v for k,v in s.items() if k!="lead" and k!="trail"},"start_frame":pos,"end_frame_exclusive":pos+s["frames"],"source_crop_width_min":min(s["a"][2],s["b"][2]),"min_native_horizontal_px":min(s["a"][2],s["b"][2]),"digital_zoom_vs_full_image_max":round(940/min(s["a"][2],s["b"][2]),3)})
 pos+=s["frames"]
manifest={
 "status":"RENDER PASS / REVIEW ONLY / NOT CANONICAL",
 "version":"S02B N16-N17 V004 QUALITY FIRST",
 "V001_approved_video":"UNCHANGED",
 "input_approved_png":originals,
 "canonical_audio_sha256":AUDIO_SHA,"canonical_audio_window_seconds":[78.750,100.700],
 "output":{"name":outfile.name,"sha256":sha256(outfile),"byte_size":outfile.stat().st_size,"ffprobe":probe,"full_decode":"PASS","audio_mean_volume_db":float(mean.group(1)),"audio_max_volume_db":float(maxv.group(1))},
 "frames":658,"duration_seconds":21.950,"fps":FPS,"output_size":SIZE,
 "policy":"Original approved RGB PNG directly resampled per frame; single final H264 encode, minimum native source crop width 734px (>720px output), no intermediate video transcoding; retain V003 six-node timings, gentle camera moves, 5-frame reaction dissolve; retain original audio.",
 "nodes":nodes,
 "audio_fallback_mp3_sha256":sha256(OUT/"S02B_N16_N17_V004_AUDIO_ONLY.mp3")
}
(OUT/"RENDER_MANIFEST.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"PASS":True,"sha256":sha256(outfile),"bytes":outfile.stat().st_size,"frames":658,"audio_mean_dB":mean.group(1),"audio_peak_dB":maxv.group(1)},ensure_ascii=False),flush=True)
