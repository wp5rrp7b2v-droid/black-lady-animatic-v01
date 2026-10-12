#!/usr/bin/env python3
"""Noncanonical 21.95-second transition refinement from exact approved N16/N17 PNGs."""
import hashlib,json,os,pathlib,subprocess
ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=pathlib.Path(os.environ.get("RUNNER_TEMP","/tmp"))/"S02B_N16_N17_V003_TRANSITION_TEST"
OUT.mkdir(parents=True,exist_ok=True)
IDX={d["shot_id"]:d for d in map(json.loads,(ROOT/"production/story_shots/story_shot_index.jsonl").read_text().splitlines())}
AUDIO=ROOT/"staging/p0_3_a01_a02_transition_validation/AUDIO_MVP1_CANONICAL_V001.m4a"
AUDIO_SHA="8d0d12d3af5e2c15032912605c0d1b3f3e892fe24918a7064864b136987737a0"
def sha(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(1048576),b""):h.update(b)
 return h.hexdigest()
def blob(p):
 a=p.read_bytes()
 return hashlib.sha1(f"blob {len(a)}\0".encode()+a).hexdigest()
def run(cmd):
 print("RUN "+" ".join(map(str,cmd))[:320],flush=True)
 subprocess.run(list(map(str,cmd)),check=True,stdout=subprocess.DEVNULL)
def probe(p):
 return json.loads(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration,size:stream=codec_name,nb_frames,width,height,r_frame_rate","-of","json",str(p)],text=True))
assert AUDIO.stat().st_size==4957338 and sha(AUDIO)==AUDIO_SHA
sources={}
for sid in ("N16","N17"):
 d=IDX[sid];p=ROOT/d["canonical_path"]
 assert d["approval_status"]=="APPROVED" and d["lifecycle"]=="CURRENT"
 assert p.stat().st_size==d["byte_size"] and sha(p)==d["sha256_locked_identity"] and blob(p)==d["github_blob_sha"],sid
 st=probe(p)["streams"][0];assert (st["width"],st["height"])==(941,1672)
 sources[sid]={"path":d["canonical_path"],"sha256":sha(p),"git_blob":blob(p),"bytes":p.stat().st_size}
# This is a deliberate mixture of camera-continuous reframings and dialogue-motivated straight cuts.
# Segments 1->2 and 4->5 join with *identical* framing at the boundary, without a jump cut.
# 2->3 is a clean dialogue reverse shot; 3->4 a clean change of scene composition.
# 5->6 has a restrained 5-frame crossfade for a reply/reaction transition.
def eased_filter(z0,z1,x0,x1,y0,y1,count,hold=0,finish_hold=0):
 den=max(1,count-1-hold-finish_hold)
 p=f"min(1,max(0,(on-{hold})/{den}))"
 q=f"({p})*({p})*(3-2*({p}))"
 z=f"({z0:.9f}+({z1-z0:.9f})*({q}))"
 x=f"max(0,min(iw-iw/zoom,({x0:.5f}+({x1-x0:.5f})*({q}))))"
 y=f"max(0,min(ih-ih/zoom,({y0:.5f}+({y1-y0:.5f})*({q}))))"
 return f"zoompan=z='{z}':x='{x}':y='{y}':d=1:s=720x1280:fps=30,setsar=1,format=yuv420p"
zj=941/616
zn=941/625
zl=941/511
specs=[
 ("N16","ESTABLISH_TO_JUN",69,(1,zj,0,325,0,120,69,15,0)),
 ("N16","JUN_QUESTION_GENTLE_DRIFT",95,(zj,1.552,325,330,120,125,95,13,20)),
 ("N16","NING_REPLY_CLEAN_REVERSE",117,(zn,1.53,0,1,110,125,117,12,20)),
 ("N17","RULE_TWO_SHOT_TO_PUSH",91,(1,1.30,0,0,0,60,91,22,0)),
 ("N17","NING_WARNING_CONTINUED_PUSH",175,(1.30,941/620,0,0,60,110,175,0,95)),
 ("N16","JUN_ACK_SOFT_CHANGE",116,(zl,1.864,430,435,110,115,116,8,30))
]
clips=[];boundaries=[];cursor=0
for i,(sid,kind,params) in enumerate(specs,1):
 frames=params[6]; vf=eased_filter(*params)
 dst=OUT/f"{i:02d}_{sid}_{kind}.mp4"
 run(["ffmpeg","-hide_banner","-loglevel","error","-y","-loop","1","-framerate","30","-i",ROOT/IDX[sid]["canonical_path"],"-vf",vf,"-frames:v",str(frames),"-an","-c:v","libx264","-preset","veryfast","-crf","19","-pix_fmt","yuv420p",dst])
 assert int(probe(dst)["streams"][0]["nb_frames"])==frames,(sid,kind)
 clips.append(dst)
 if i<=5:
  boundaries.append({"node":i,"shot_id":sid,"name":kind,"start_frame":cursor,"end_frame":cursor+frames,"frames":frames,"motion":list(params)})
  cursor+=frames
 else:
  boundaries.append({"node":i,"shot_id":sid,"name":kind,"first_fully_visible_frame":cursor,"rendered_frames":frames,"overlap_frames":5})
 # Archive representative frames to compare source visual continuity.
 run(["ffmpeg","-hide_banner","-loglevel","error","-y","-i",dst,"-frames:v","1",OUT/f"{i:02d}_START.png"])
 run(["ffmpeg","-hide_banner","-loglevel","error","-y","-sseof","-0.067","-i",dst,"-frames:v","1",OUT/f"{i:02d}_END.png"])
assert cursor==547
(OUT/"concat.txt").write_text("".join("file '"+str(p.resolve())+"'\n" for p in clips[:5]))
first=OUT/"first_five.mp4"
run(["ffmpeg","-hide_banner","-loglevel","error","-y","-f","concat","-safe","0","-i",OUT/"concat.txt","-c","copy",first])
assert int(probe(first)["streams"][0]["nb_frames"])==547
video=OUT/"merged_transitions.mp4"
run(["ffmpeg","-hide_banner","-loglevel","error","-y","-i",first,"-i",clips[-1],"-filter_complex",
     "[0:v]setpts=PTS-STARTPTS[a];[1:v]setpts=PTS-STARTPTS[b];[a][b]xfade=transition=fade:duration=0.166667:offset=18.066667,format=yuv420p[v]",
     "-map","[v]","-frames:v","658","-an","-c:v","libx264","-preset","veryfast","-crf","19","-pix_fmt","yuv420p",video])
assert int(probe(video)["streams"][0]["nb_frames"])==658
out=OUT/"S02B_N16_N17_V003_TRANSITION_TEST.mp4"
run(["ffmpeg","-hide_banner","-loglevel","error","-y","-i",video,"-i",AUDIO,"-filter_complex",
     "[1:a:0]atrim=start=78.750:duration=21.950,asetpts=PTS-STARTPTS[a]",
     "-map","0:v:0","-map","[a]","-t","21.950","-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2","-movflags","+faststart",out])
run(["ffmpeg","-hide_banner","-loglevel","error","-xerror","-i",out,"-f","null","-"])
meta=probe(out)
assert meta["streams"][0]["nb_frames"]=="658" and abs(float(meta["format"]["duration"])-21.95)<0.06
manifest={"result":"PASS / REVIEW ONLY / NOT APPROVED OR CANONICAL","source_originals":sources,"source_audio_sha256":AUDIO_SHA,"source_audio_window":[78.75,100.70],"approved_v001":"UNCHANGED","shots":boundaries,"transition_policy":"seamless camera continuation 01-02 and 04-05; clean dialogue cuts 02-03 and 03-04; 5-frame dissolve 05-06","frame_count":658,"video_sha256":sha(out),"video_bytes":out.stat().st_size,"ffprobe":meta}
(OUT/"RENDER_MANIFEST.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print(json.dumps({"RESULT":"PASS","file":str(out),"sha256":sha(out),"bytes":out.stat().st_size,"video_frames":658},ensure_ascii=False))
