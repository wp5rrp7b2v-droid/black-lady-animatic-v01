#!/usr/bin/env python3
"""Review-only chronological contact sheet from exact V018. No approved file edits."""
import hashlib, io, json, subprocess
from pathlib import Path
from PIL import Image, ImageDraw
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"production/environment_dynamic/review_candidates/S02_B_M01_V018_FULL_LENGTH_C_VISIBLE_REVIEW/S02_B_M01_V018_FULL_LENGTH_MORE_VISIBLE_C_GROUP_PREVIEW_V001.mp4"
EDL=ROOT/"production/editorial_specs/S02_B_V006_CINEMATIC_ROUGH_EDL_V002_RENDERED_RECONSTRUCTED_REVIEW.json"
OUT=ROOT/"production/video_candidates/review/s02b_v019_directors_cut_preflight"
SHA="6897b1ac246e4c30d84aca3b80003a58d7bae86eb7631272fe28253b23a01427"
def extract(n):
    b=subprocess.run(["ffmpeg","-v","error","-i",str(SRC),"-vf",f"select=eq(n\\,{n}),scale=230:409","-frames:v","1","-f","image2pipe","-vcodec","mjpeg","pipe:1"],check=True,capture_output=True).stdout
    return Image.open(io.BytesIO(b)).convert("RGB")
def main():
    OUT.mkdir(parents=True,exist_ok=True)
    assert hashlib.file_digest(open(SRC,"rb"),"sha256").hexdigest()==SHA
    edl=json.loads(EDL.read_text())
    shots=edl["timeline"]
    frames=[]
    for shot in shots:
        a,b=shot["start_frame"],shot["end_frame_exclusive"]
        for location,n in [("EARLY",a+max(1,round((b-a)*.20))),("LATE",a+max(1,round((b-a)*.75)))]:
            if n>=b:n=b-1
            frames.append((shot["id"],location,n,extract(n)))
    col,row=6,6
    cw,ch=230,443
    board=Image.new("RGB",(col*cw,row*ch),(18,18,18))
    draw=ImageDraw.Draw(board)
    for index,(shot,position,n,im) in enumerate(frames):
        x=(index%col)*cw;y=(index//col)*ch
        draw.text((x+6,y+5),f"{shot} | {position}",fill="white")
        draw.text((x+6,y+20),f"#{n} {n/30:.2f}s",fill="white")
        board.paste(im,(x,y+34))
    board.save(OUT/"S02B_V019_DIRECTOR_CHRONOLOGY_CONTACT_V001.jpg",quality=86,optimize=True)
    data={"source_v018_sha256":SHA,"source_edl":"S02_B_V006_CINEMATIC_ROUGH_EDL_V002_RENDERED_RECONSTRUCTED_REVIEW.json","state":"READ_ONLY_EDITORIAL_DIAGNOSTIC","cells":[{"id":id,"time":n/30,"frame":n,"location":pos} for id,pos,n,_ in frames]}
    (OUT/"S02B_V019_DIRECTOR_CHRONOLOGY_CONTACT_V001.json").write_text(json.dumps(data,indent=2))
    print("PASS: EXACT_V018, 34 labeled frames, no canonical modifications",flush=True)
if __name__=="__main__":main()
