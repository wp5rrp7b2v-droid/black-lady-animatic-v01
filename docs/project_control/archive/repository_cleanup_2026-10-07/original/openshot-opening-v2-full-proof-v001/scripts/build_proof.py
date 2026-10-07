import json
from pathlib import Path
import openshot

PROJECT=Path(__file__).resolve().parents[1]
SPEC=json.loads((PROJECT/"shot_motion_spec.json").read_text())
WORK=PROJECT/"work"
INPUTS=WORK/"inputs"
FRAMES=WORK/"frames"
FRAMES.mkdir(parents=True,exist_ok=True)
for p in FRAMES.glob("frame_*.png"): p.unlink()

FPS=SPEC["fps"]; W=SPEC["width"]; H=SPEC["height"]; TOTAL=SPEC["total_frames"]
KEEPALIVE=[]

def make_kf(points):
    k=openshot.Keyframe()
    for frame,value,mode in points:
        k.AddPoint(frame,value,openshot.BEZIER if mode=="bezier" else openshot.LINEAR)
    return k

def shifted_curve(raw, pre, total_local):
    # raw tuples: [frame, value]; preserve first value during preroll and last value during postroll
    pts=[(1,float(raw[0][1]),"bezier")]
    if pre>0:
        pts.append((pre+1,float(raw[0][1]),"bezier"))
    for f,v in raw:
        pts.append((int(f)+pre,float(v),"bezier"))
    last=pts[-1][1]
    if pts[-1][0] < total_local:
        pts.append((total_local,last,"bezier"))
    # de-duplicate same frame keeping last declaration
    dedup={}
    for f,v,m in pts: dedup[int(f)]=(int(f),float(v),m)
    return [dedup[k] for k in sorted(dedup)]

def curve_from_keyframes(shot, idx):
    raw=shot["keyframes"]
    return {
      "scale":[(r[0],r[1]) for r in raw],
      "x":[(r[0],r[2]) for r in raw],
      "y":[(r[0],r[3]) for r in raw],
      "rotation":[(r[0],r[4]) for r in raw],
    }

timeline=openshot.Timeline(W,H,openshot.Fraction(FPS,1),44100,2,openshot.LAYOUT_STEREO)
motion_manifest={"engine":"libopenshot Python bindings","fps":FPS,"resolution":[W,H],"total_frames":TOTAL,"sequence":SPEC["sequence"],"shots":[]}

shots=SPEC["shots"]
for idx,shot in enumerate(shots):
    tin=shot["transition_in"]
    pre=0 if tin["type"] in ("hard","fade_black") else tin["frames"]//2
    next_t=shots[idx+1]["transition_in"] if idx+1<len(shots) else {"type":"hard","frames":0}
    post=0 if next_t["type"] in ("hard","fade_black") else (next_t["frames"]-next_t["frames"]//2)

    expanded_start=max(0,shot["start_frame"]-pre)
    actual_pre=shot["start_frame"]-expanded_start
    total_local=shot["duration_frames"]+actual_pre+post

    reader=openshot.QtImageReader(str(INPUTS/f"{shot['shot_id']}.png"))
    clip=openshot.Clip(reader)
    clip.Position(expanded_start/FPS)
    clip.Start(0.0)
    clip.End(total_local/FPS)
    clip.Layer(idx+1)
    clip.gravity=openshot.GRAVITY_CENTER
    clip.scale=openshot.SCALE_CROP

    curves=curve_from_keyframes(shot,idx)
    clip.scale_x=make_kf(shifted_curve(curves["scale"],actual_pre,total_local))
    clip.scale_y=make_kf(shifted_curve(curves["scale"],actual_pre,total_local))
    clip.location_x=make_kf(shifted_curve(curves["x"],actual_pre,total_local))
    clip.location_y=make_kf(shifted_curve(curves["y"],actual_pre,total_local))
    clip.rotation=make_kf(shifted_curve(curves["rotation"],actual_pre,total_local))

    alpha=[]
    if idx==0 and tin["type"]=="fade_black":
        alpha=[(1,0.0,"bezier"),(tin["frames"],1.0,"bezier")]
    elif tin["type"]=="hard":
        alpha=[(1,1.0,"bezier")]
    else:
        alpha=[(1,0.0,"bezier"),(max(2,actual_pre+(tin["frames"]-tin["frames"]//2)),1.0,"bezier")]
    if idx==len(shots)-1:
        fade=SPEC["final_fade_out_frames"]
        fade_start=max(1,total_local-fade)
        alpha.extend([(fade_start,1.0,"bezier"),(total_local,0.0,"bezier")])
    elif alpha[-1][0] < total_local:
        alpha.append((total_local,1.0,"bezier"))
    clip.alpha=make_kf(alpha)

    timeline.AddClip(clip)
    KEEPALIVE.extend([reader,clip])
    motion_manifest["shots"].append({
      "shot_id":shot["shot_id"],"start_frame":shot["start_frame"],"duration_frames":shot["duration_frames"],
      "expanded_start_frame":expanded_start,"expanded_duration_frames":total_local,
      "transition_in":tin,"motion":shot["motion"],"keyframes":shot["keyframes"]
    })

timeline.Open()
try:
    for n in range(1,TOTAL+1):
        frame=timeline.GetFrame(n)
        frame.Save(str(FRAMES/f"frame_{n:04d}.png"),1.0)
        if n%60==0 or n==TOTAL:
            print(f"RENDERED_FRAME={n}/{TOTAL}")
finally:
    timeline.Close()

count=len(list(FRAMES.glob("frame_*.png")))
if count!=TOTAL: raise RuntimeError(f"rendered frame count mismatch {count}")
motion_manifest["rendered_frame_count"]=count
(WORK/"motion_manifest.json").write_text(json.dumps(motion_manifest,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"RENDERED_FRAME_COUNT":count,"STATUS":"LIBOPENSHOT_FRAME_RENDER_PASS"},indent=2))
