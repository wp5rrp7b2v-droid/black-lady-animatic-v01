#!/usr/bin/env python3
"""V019-B3 experimental 0.40-sec shadow-bridge cut transitions.
This is a review-only continuation of PO-approved B clip ORDER, not an approved
new visual/video. Never touches source video, full V018, audio, or main.
"""
from pathlib import Path
import hashlib, json, math, subprocess
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
OUTDIR = ROOT / "production/video_candidates/review/v019_b_transition_preflight_v001"
SOURCE = OUTDIR / "B_VISUAL_RELATION_REORDER_CONTEXT_REVIEW.mp4"
EXPECTED_SOURCE_SHA = "14a41d0985f12e3de489467b2fb643660f1e4dac073813a66c35d5beb9bcd5b9"
TARGET = OUTDIR / "B3_12_FRAME_SHADOW_BRIDGES_NO_OVERLAY_REVIEW.mp4"
AB = OUTDIR / "AB_B_APPROVED_ORDER_VS_B3_SHADOW_BRIDGES.mp4"
SHEET = OUTDIR / "B3_SHADOW_BRIDGE_CONTACT_SHEET.jpg"
REPORT = OUTDIR / "B3_SHADOW_BRIDGE_QC.json"

FPS, WIDTH, HEIGHT, FRAME_COUNT = 30,720,1280,334
CUTS = [108,175,252]
HALF_WINDOW = 6   # 6 previous + 6 following, 12 frames total per cut (0.4s)
LOW_POINT = 0.32   # gentle dimming, NOT fade-to-black
RAW_FRAME_BYTES = WIDTH * HEIGHT * 3

def run(*arguments):
    return subprocess.run([str(x) for x in arguments],check=True,capture_output=True).stdout

def packet_hash(path):
    return hashlib.sha256(run("ffmpeg","-v","error","-i",path,"-map","0:a:0",
                            "-c:a","copy","-f","adts","pipe:1")).hexdigest()

def frame_count(path):
    info=json.loads(run("ffprobe","-v","error","-count_frames",
                        "-select_streams","v:0","-show_entries","stream=nb_read_frames",
                        "-of","json",path))
    return int(info["streams"][0]["nb_read_frames"])

def strength(idx):
    for cut in CUTS:
        if cut-HALF_WINDOW <= idx < cut:
            step=(idx-(cut-HALF_WINDOW)+1)/HALF_WINDOW
            easing=(1-math.cos(math.pi*step))/2
            return (1-(1-LOW_POINT)*easing,cut)
        if cut <= idx < cut+HALF_WINDOW:
            step=(idx-cut+1)/HALF_WINDOW
            easing=(1-math.cos(math.pi*step))/2
            return (LOW_POINT+(1-LOW_POINT)*easing,cut)
    return (1.0,None)

def readexact(reader,count):
    buf=bytearray()
    while len(buf)<count:
        chunk=reader.stdout.read(count-len(buf))
        if not chunk: raise RuntimeError(f"Short video frame: {len(buf)}")
        buf.extend(chunk)
    return bytes(buf)

def main():
    assert SOURCE.exists(), "Missing prior approved-order B candidate"
    srcsha=hashlib.file_digest(open(SOURCE,"rb"),"sha256").hexdigest()
    assert srcsha==EXPECTED_SOURCE_SHA,(srcsha,EXPECTED_SOURCE_SHA)
    assert frame_count(SOURCE)==FRAME_COUNT
    parent_audio=packet_hash(SOURCE)
    reader=subprocess.Popen(["ffmpeg","-v","error","-i",str(SOURCE),
             "-map","0:v:0","-f","rawvideo","-pix_fmt","rgb24","pipe:1"],
             stdout=subprocess.PIPE)
    writer=subprocess.Popen(["ffmpeg","-v","error","-y",
             "-f","rawvideo","-pix_fmt","rgb24","-s",f"{WIDTH}x{HEIGHT}",
             "-r",str(FPS),"-i","pipe:0","-i",str(SOURCE),
             "-map","0:v:0","-map","1:a:0","-c:v","libx264","-preset","veryfast",
             "-crf","19","-pix_fmt","yuv420p","-c:a","copy",
             "-movflags","+faststart",str(TARGET)],stdin=subprocess.PIPE)
    evidence=[]
    try:
        for i in range(FRAME_COUNT):
            original=readexact(reader,RAW_FRAME_BYTES)
            gain,cut=strength(i)
            if cut is None:
                final=original
            else:
                origimage=Image.frombytes("RGB",(WIDTH,HEIGHT),original)
                lut=[min(255,int(round(x*gain))) for x in range(256)]
                edited=origimage.point(lut*3)
                final=edited.tobytes()
                evidence.append((i,cut,gain,origimage.resize((180,320)),edited.resize((180,320))))
            writer.stdin.write(final)
        writer.stdin.close()
        assert reader.wait()==0
        assert writer.wait()==0
    finally:
        if reader.poll() is None:reader.kill()
        if writer.poll() is None:writer.kill()
    assert frame_count(TARGET)==FRAME_COUNT
    assert packet_hash(TARGET)==parent_audio, "Do not advance: AAC stream differs"
    run("ffmpeg","-v","error","-y","-i",SOURCE,"-i",TARGET,
        "-filter_complex","[0:v]scale=540:960[a];[1:v]scale=540:960[b];"
                          "[a][b]hstack=inputs=2[v]",
        "-map","[v]","-map","0:a:0","-c:v","libx264",
        "-preset","veryfast","-crf","23","-pix_fmt","yuv420p",
        "-c:a","copy","-movflags","+faststart",AB)
    assert frame_count(AB)==FRAME_COUNT
    assert packet_hash(AB)==parent_audio
    # Exactly six representative frames on each side of each edit.
    selected=[]
    for cut in CUTS:
        for i in [cut-6,cut-4,cut-2,cut-1,cut,cut+1,cut+3,cut+5]:
            selected.append(next(x for x in evidence if x[0]==i))
    sheet=Image.new("RGB",(8*180,6*345),(18,18,18))
    d=ImageDraw.Draw(sheet)
    for row in range(6):
        for column in range(8):
            fr,cut,gain,orig,edited=selected[(row//2)*8+column]
            is_b3=bool(row%2)
            x,y=column*180,row*345
            sheet.paste(edited if is_b3 else orig,(x,y+20))
            d.text((x+5,y+4),f"{'B3' if is_b3 else 'B'}  #{fr} / {gain:.2f}",fill="#FFFFFF")
    sheet.save(SHEET,quality=87)
    report={
       "status":"TECHNICAL_PASS_PO_VISUAL_REVIEW_PENDING",
       "approval_scope":"NO_NEW_APPROVAL; B ORDER APPROVED BY PO ONLY",
       "version":"B3","order":["N21","NEW02","N22","N23"],
       "source_B_sha256":srcsha,
       "B3_sha256":hashlib.file_digest(open(TARGET,"rb"),"sha256").hexdigest(),
       "frame_count_B":frame_count(SOURCE),"frame_count_B3":frame_count(TARGET),
       "transition_cuts_relative_frames":CUTS,
       "edited_ranges_inclusive":[[c-6,c+5] for c in CUTS],
       "duration_each_seconds":2*HALF_WINDOW/FPS,
       "transition_method":"One-source-at-a-time frame dimming; zero double-exposure.",
       "min_brightness_multiplier":LOW_POINT,
       "audio_packet_sha256_B_B3_AB":parent_audio,
       "audio_packet_identical":True,
       "image_generated":False,"paid_AI_generation":False,
       "V018_and_approved_B_source_unchanged":True,
       "visual_limit":"Repeated dark dips might appear as flashes or slideshow fades; technical PASS is not an artistic PASS."
    }
    REPORT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(report,ensure_ascii=False),flush=True)
if __name__=="__main__":main()
