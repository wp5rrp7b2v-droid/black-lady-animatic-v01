from fractions import Fraction
import hashlib, json, subprocess, sys
from pathlib import Path

PROJECT=Path(__file__).resolve().parents[1]
OUT=PROJECT/"out"/"P03_LIBOPENSHOT_CAMERA_MOTION_PROOF_V001"
MP4=OUT/"P03_LIBOPENSHOT_CAMERA_MOTION_PROOF_V001.mp4"

def require(ok,msg):
    if not ok: raise RuntimeError(msg)

def probe(path):
    return json.loads(subprocess.check_output(["ffprobe","-v","error","-show_streams","-show_format","-of","json",str(path)],text=True))

try:
    require(MP4.is_file() and MP4.stat().st_size>0,"missing MP4")
    m=probe(MP4)
    v=[s for s in m["streams"] if s["codec_type"]=="video"]
    a=[s for s in m["streams"] if s["codec_type"]=="audio"]
    require(len(v)==1,"video stream count mismatch")
    require(len(a)==0,"motion-only spike unexpectedly has audio")
    v=v[0]
    require(v["codec_name"]=="h264" and v["pix_fmt"]=="yuv420p","video codec/pixel format mismatch")
    require(int(v["width"])==1080 and int(v["height"])==1920,"dimensions mismatch")
    require(Fraction(v["avg_frame_rate"])==30 and Fraction(v["r_frame_rate"])==30,"fps mismatch")
    counted=json.loads(subprocess.check_output(["ffprobe","-v","error","-select_streams","v:0","-count_frames","-show_entries","stream=nb_read_frames","-of","json",str(MP4)],text=True))
    frames=int(counted["streams"][0]["nb_read_frames"])
    require(frames==228,f"frame count {frames}")
    require(abs(float(v["duration"])-7.6)<0.01,f"video duration {v['duration']}")
    dec=subprocess.run(["ffmpeg","-v","error","-xerror","-i",str(MP4),"-map","0:v:0","-f","null","-"],capture_output=True,text=True)
    require(dec.returncode==0 and not dec.stderr.strip(),f"decode failure: {dec.stderr}")
    sha=hashlib.sha256(MP4.read_bytes()).hexdigest()
    report={
      "STATUS":"TECHNICAL_RENDER_PASS",
      "ENGINE":"libopenshot",
      "READY_FOR_PRODUCT_OWNER_MOTION_REVIEW":"YES",
      "OUTPUT_SHA256":sha,
      "OUTPUT_BYTE_SIZE":MP4.stat().st_size,
      "FRAME_COUNT":frames,
      "VIDEO_DURATION":v["duration"],
      "FPS":30,"WIDTH":1080,"HEIGHT":1920,
      "VIDEO_CODEC":v["codec_name"],"PIX_FMT":v["pix_fmt"],
      "AUDIO":"NONE / MOTION-ONLY SPIKE",
      "FULL_DECODE":"PASS",
      "NOTE":"This is a 3-shot camera-motion technology spike only (N08→N03→N05), not an Opening V2 edit or P0.3 approval candidate."
    }
    (OUT/"technical_qc.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
except Exception as e:
    print(f"OUTPUT_QC_FAILURE: {e}",file=sys.stderr)
    sys.exit(1)
