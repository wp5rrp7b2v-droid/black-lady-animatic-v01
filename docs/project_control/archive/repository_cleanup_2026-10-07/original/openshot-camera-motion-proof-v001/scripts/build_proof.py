import json, math, os, shutil
from pathlib import Path
import openshot

PROJECT = Path(__file__).resolve().parents[1]
WORK = PROJECT / "work"
INPUTS = WORK / "inputs"
FRAMES = WORK / "frames"
FRAMES.mkdir(parents=True, exist_ok=True)
for p in FRAMES.glob("frame_*.png"):
    p.unlink()

FPS = 30
W, H = 1080, 1920
TOTAL_FRAMES = 228
KEEPALIVE = []  # libopenshot Timeline stores raw pointers; keep SWIG reader/clip objects alive through render

def kf(points):
    k = openshot.Keyframe()
    for frame, value, mode in points:
        interp = openshot.BEZIER if mode == "bezier" else openshot.LINEAR
        k.AddPoint(frame, value, interp)
    return k

def add_clip(timeline, sid, start_frame, duration, layer, curves, alpha_points):
    reader = openshot.QtImageReader(str(INPUTS / f"{sid}.png"))
    clip = openshot.Clip(reader)
    clip.Position(start_frame / FPS)
    clip.Start(0.0)
    clip.End(duration / FPS)
    clip.Layer(layer)
    clip.gravity = openshot.GRAVITY_CENTER
    clip.scale = openshot.SCALE_CROP

    clip.scale_x = kf(curves["scale"])
    clip.scale_y = kf(curves["scale"])
    clip.location_x = kf(curves["x"])
    clip.location_y = kf(curves["y"])
    clip.rotation = kf(curves.get("rotation", [(1,0.0,"bezier"),(duration,0.0,"bezier")]))
    clip.alpha = kf(alpha_points)

    timeline.AddClip(clip)
    KEEPALIVE.extend([reader, clip])
    return clip

timeline = openshot.Timeline(W, H, openshot.Fraction(FPS,1), 44100, 2, openshot.LAYOUT_STEREO)

spec = {
  "engine": "libopenshot Python bindings",
  "fps": FPS,
  "resolution": [W,H],
  "total_frames": TOTAL_FRAMES,
  "total_seconds": TOTAL_FRAMES / FPS,
  "audio": "NONE / MOTION-ONLY TECHNICAL SPIKE",
  "sequence": ["N08","N03","N05"],
  "clips": {}
}

# N08 — architecture attraction: brief hold -> accelerating push -> slight overshoot -> settle
n08 = {
  "scale":[(1,1.000,"bezier"),(7,1.000,"bezier"),(28,1.025,"bezier"),(64,1.075,"bezier"),(84,1.065,"bezier")],
  "x":[(1,0.000,"bezier"),(7,0.000,"bezier"),(28,-0.002,"bezier"),(64,-0.007,"bezier"),(84,-0.006,"bezier")],
  "y":[(1,0.000,"bezier"),(7,0.000,"bezier"),(28,-0.006,"bezier"),(64,-0.022,"bezier"),(84,-0.018,"bezier")],
}
add_clip(timeline,"N08",0,84,1,n08,[(1,1.0,"bezier"),(72,1.0,"bezier"),(84,0.0,"bezier")])
spec["clips"]["N08"]={"start_frame":0,"duration_frames":84,"motion":"hold -> architecture push -> overshoot -> settle","curves":n08}

# N03 — reaction observation: pull back + lateral drift + settle
n03 = {
  "scale":[(1,1.050,"bezier"),(12,1.042,"bezier"),(38,1.022,"bezier"),(68,1.000,"bezier"),(78,1.004,"bezier")],
  "x":[(1,-0.016,"bezier"),(12,-0.010,"bezier"),(38,0.002,"bezier"),(68,0.015,"bezier"),(78,0.011,"bezier")],
  "y":[(1,0.002,"bezier"),(38,0.000,"bezier"),(78,0.001,"bezier")],
}
add_clip(timeline,"N03",72,78,2,n03,[(1,0.0,"bezier"),(12,1.0,"bezier"),(66,1.0,"bezier"),(78,0.0,"bezier")])
spec["clips"]["N03"]={"start_frame":72,"duration_frames":78,"motion":"pull-back + lateral observation drift + settle","curves":n03}

# N05 — action peak: hold -> push/reframe -> directional settle-shake -> settle
n05 = {
  "scale":[(1,1.000,"bezier"),(6,1.000,"bezier"),(28,1.020,"bezier"),(50,1.050,"bezier"),(64,1.082,"bezier"),(76,1.072,"bezier"),(90,1.065,"bezier")],
  "x":[
    (1,0.000,"bezier"),(28,0.002,"bezier"),(50,0.006,"bezier"),
    (54,0.014,"linear"),(56,-0.002,"linear"),(58,0.012,"linear"),(60,0.000,"linear"),(62,0.009,"linear"),(64,0.004,"linear"),
    (76,0.003,"bezier"),(90,0.002,"bezier")
  ],
  "y":[
    (1,0.000,"bezier"),(28,-0.003,"bezier"),(50,-0.010,"bezier"),
    (54,-0.014,"linear"),(56,-0.007,"linear"),(58,-0.013,"linear"),(60,-0.008,"linear"),(62,-0.012,"linear"),(64,-0.010,"linear"),
    (76,-0.009,"bezier"),(90,-0.008,"bezier")
  ],
  "rotation":[
    (1,0.00,"bezier"),(28,0.06,"bezier"),(50,0.18,"bezier"),
    (54,0.42,"linear"),(56,-0.18,"linear"),(58,0.30,"linear"),(60,-0.10,"linear"),(62,0.16,"linear"),(64,0.08,"linear"),
    (76,0.04,"bezier"),(90,0.00,"bezier")
  ]
}
add_clip(timeline,"N05",138,90,3,n05,[(1,0.0,"bezier"),(12,1.0,"bezier"),(90,1.0,"bezier")])
spec["clips"]["N05"]={"start_frame":138,"duration_frames":90,"motion":"action push + directional reframe + settle-shake + micro rotation","curves":n05}

timeline.Open()
try:
    for n in range(1, TOTAL_FRAMES + 1):
        frame = timeline.GetFrame(n)
        frame.Save(str(FRAMES / f"frame_{n:04d}.png"), 1.0)
        if n % 30 == 0 or n == TOTAL_FRAMES:
            print(f"RENDERED_FRAME={n}/{TOTAL_FRAMES}")
finally:
    timeline.Close()

spec["rendered_frame_count"] = len(list(FRAMES.glob("frame_*.png")))
if spec["rendered_frame_count"] != TOTAL_FRAMES:
    raise RuntimeError(f"frame render count mismatch: {spec['rendered_frame_count']}")

(WORK/"motion_manifest.json").write_text(json.dumps(spec,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(spec,ensure_ascii=False,indent=2))
