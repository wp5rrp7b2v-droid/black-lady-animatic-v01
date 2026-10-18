#!/usr/bin/env python3
"""Render S02-B V019 Director-Cut review from 3 authored PNGs plus V018 exact video.

Hard stops:
 - NEVER create or overwrite approved assets or publish to main.
 - Exact source SHA256 and original AAC packet hashes must match.
 - Require exactly 3 new PNGs (PO authorization is for director-run candidate, not publication).
 - Preserve all 1927 video frames, original time line / complete AAC, no paid AI video.
 - Render ordinary motivated HARD CUTS, no fades, wipes, ambient Foley, dust.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import shutil
import tempfile
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
SPEC=ROOT/"production/editorial_specs/S02_B_V019_DIRECTORS_CUT_EDL_V001.json"
OUTPUT=ROOT/"production/video_candidates/v019_directors_cut/review"
OUTPUT_VIDEO=OUTPUT/"S02_B_V019_DIRECTORS_CUT_FULL_REVIEW_V001.mp4"
REPORT=OUTPUT/"S02_B_V019_DIRECTORS_CUT_QC_V001.json"
FPS=30
def run(*argv):
    return subprocess.run([str(x) for x in argv],check=True,capture_output=True).stdout
def sha(p):
    with open(p,"rb") as f:
        return hashlib.file_digest(f,"sha256").hexdigest()
def exact_audio(p):
    return hashlib.sha256(run("ffmpeg","-v","error","-i",p,"-map","0:a:0",
        "-c:a","copy","-f","adts","pipe:1")).hexdigest()
def num_frames(p):
    o=json.loads(run("ffprobe","-v","error","-count_frames",
        "-select_streams","v:0","-show_entries","stream=nb_read_frames,width,height,r_frame_rate",
        "-of","json",p))
    v=o["streams"][0]
    assert (int(v["width"]),int(v["height"]),v["r_frame_rate"])==(720,1280,"30/1"),v
    return int(v["nb_read_frames"])
def render_segment(source,shot,p):
    frames=shot["duration_frames"]
    if shot["type"]=="source_video":
        cmd=["ffmpeg","-v","error","-y","-i",source,
             "-vf",f"trim=start_frame={shot['source_frame_start']}:end_frame={shot['source_frame_end_exclusive']},setpts=PTS-STARTPTS",
             "-map","0:v:0","-an","-c:v","libx264","-preset","fast","-crf","17",
             "-g","30","-bf","2","-pix_fmt","yuv420p","-r","30",
             "-movflags","+faststart",p]
    else:
        png=ROOT/shot["asset"]
        assert png.is_file(),f"Missing authored still: {png}"
        im=Image.open(png)
        assert im.format=="PNG","Candidate must be PNG"
        assert im.size==(941,1672),f"Wrong still dimensions: {im.size} @ {png.name}"
        im.close()
        cmd=["ffmpeg","-v","error","-y","-loop","1","-framerate","30",
             "-i",png,"-vf","scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,setsar=1",
             "-frames:v",str(frames),"-an","-c:v","libx264",
             "-preset","fast","-crf","17","-g","30","-bf","2",
             "-pix_fmt","yuv420p","-r","30","-movflags","+faststart",p]
    run(*cmd)
    assert num_frames(p)==frames,(shot["id"],num_frames(p),frames)
def main():
    spec=json.loads(SPEC.read_text())
    source=ROOT/spec["source_video_path"]
    assert source.exists()
    assert sha(source)==spec["source_sha256"],"V018 source exact SHA256 mismatch"
    assert not OUTPUT_VIDEO.exists(), "Fail-closed: candidate already exists; do not overwrite"
    frames=spec["output"]["total_frames"]
    assert frames==1927
    shots=spec["segments"]
    assert sum(x["duration_frames"] for x in shots)==frames
    assert [x["id"] for x in shots if x["type"]=="still"] == [
        "D01_JUN_SISTER_QUESTION_LISTEN",
        "D02_NING_WARNING_SPACE",
        "D03_JUN_LISTENS_LOOKS_OUTSIDE"
    ]
    src_audio=exact_audio(source)
    OUTPUT.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="s02b_director_") as tmp:
        temp=Path(tmp)
        segments=[]
        for i,shot in enumerate(shots):
            part=temp/f"seg_{i:02d}.mp4"
            render_segment(source,shot,part)
            segments.append(part)
            print("SEGMENT PASS",i,shot["id"],shot["duration_frames"],flush=True)
        concat=temp/"concat.ffconcat"
        concat.write_text("ffconcat version 1.0\n"+"".join(f"file '{p}'\n" for p in segments))
        silent=temp/"video_silent.mp4"
        run("ffmpeg","-v","error","-y","-safe","0","-f","concat","-i",concat,
            "-map","0:v:0","-c:v","copy","-an","-movflags","+faststart",silent)
        assert num_frames(silent)==frames,"Joined video frame count mismatch"
        run("ffmpeg","-v","error","-y","-i",silent,"-i",source,
            "-map","0:v:0","-map","1:a:0","-c:v","copy","-c:a","copy",
            "-movflags","+faststart",OUTPUT_VIDEO)
    assert num_frames(OUTPUT_VIDEO)==frames
    assert exact_audio(OUTPUT_VIDEO)==src_audio,"Approved AAC packets changed"
    result={
      "schema":"S02_B_V019_DIRECTORS_CUT_QC_V001",
      "status":"MACHINE_PASS / FULL_PO_VISUAL_REVIEW_PENDING / NOT_CANONICAL",
      "input_v018_path":spec["source_video_path"],
      "input_v018_sha256":spec["source_sha256"],
      "output":str(OUTPUT_VIDEO.relative_to(ROOT)),
      "output_sha256":sha(OUTPUT_VIDEO),
      "frames":frames,"fps":FPS,"resolution":[720,1280],
      "audio_aac_adts_input_sha256":src_audio,
      "audio_aac_adts_output_sha256":exact_audio(OUTPUT_VIDEO),
      "audio_exact_packet_copy":True,
      "image_sources":[{"id":x["id"],"path":x["asset"],"sha256":sha(ROOT/x["asset"])}
                       for x in shots if x["type"]=="still"],
      "no_paid_ai_video":True,
      "no_character_animation":True,
      "no_transition_fx":True,
      "unchanged_canonical_assets":True,
      "mandatory_next_gate":"PO views full candidate and judges story/identity/continuity; machine PASS != artwork approval",
      "main_merge_authorized":False
    }
    REPORT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print("DIRECTOR_CUT_REVIEW_MACHINE_PASS",json.dumps(result),flush=True)
if __name__=="__main__":
    main()
