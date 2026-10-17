#!/usr/bin/env python3
"""M01 A1 N17 late-light frame source evidence diagnostic only."""
import base64,hashlib,io,json,pathlib,subprocess
import numpy as np
from PIL import Image,ImageDraw,ImageFont

ROOT=pathlib.Path(__file__).resolve().parents[1]
SRC=ROOT/"production/video_candidates/assets/S02_B_V006_CINEMATIC_ROUGH_RECONSTRUCTED_CANDIDATE_V001.mp4"
MANIFEST=ROOT/"production/environment_dynamic/benchmarks/m01_stage_a_v002/evidence/M01_STAGE_A_MACHINE_BENCHMARK_V002.json"
OUT=ROOT/"_m01_a1_n17_source_localization"
W,H=720,1280
INDICES=[337,469,520,550,580,601,630,645]
def sha(b):return hashlib.sha256(b).hexdigest()
def font(s):
 p="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
 return ImageFont.truetype(p,s) if pathlib.Path(p).exists() else ImageFont.load_default()
def decode(indices):
 expr="+".join(f"eq(n\\,{i})" for i in indices)
 p=subprocess.Popen(["ffmpeg","-hide_banner","-loglevel","error","-xerror","-i",str(SRC),
   "-vf","select="+expr,"-vsync","vfr","-pix_fmt","rgb24","-f","rawvideo","pipe:1"],
   stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 frames={}
 n=W*H*3
 try:
  for i in indices:
   blocks=[];remaining=n
   while remaining:
    part=p.stdout.read(remaining)
    if not part:raise RuntimeError("SHORT_FRAME_"+str(i))
    remaining-=len(part);blocks.append(part)
   raw=b"".join(blocks)
   frames[i]=(np.frombuffer(raw,dtype=np.uint8).reshape(H,W,3).copy(),sha(raw))
  assert p.stdout.read(1)==b""
 finally:p.stdout.close()
 err=p.stderr.read().decode(errors="replace");p.stderr.close()
 assert p.wait()==0,err[-800:]
 return frames
def main():
 manifest=json.loads(MANIFEST.read_text())
 assert sha(SRC.read_bytes())==manifest["source_video_sha256"]
 n17=next(s for s in manifest["samples"] if s["shot_id"]=="N17")
 frames=decode(INDICES)
 for entry in n17["frames"]:
  assert frames[entry["frame_index"]][1]==entry["decoded_rgb_sha256"],"SOURCE_EXACT_FRAME_DRIFT"
 OUT.mkdir(parents=True,exist_ok=True)
 tiles=Image.new("RGB",(4*540,2*720),(13,13,15))
 pen=ImageDraw.Draw(tiles)
 source_proof=[]
 for i,idx in enumerate(INDICES):
  img,rgbsha=frames[idx]
  left=540*(i%4);top=720*(i//4)
  part=Image.fromarray(img,"RGB").crop((470,0,720,430)).resize((500,640),Image.Resampling.NEAREST)
  tiles.paste(part,(left+15,top+50))
  pen.text((left+17,top+12),f"F{idx} @ {(idx+.5)/30:.2f}s",font=font(27),fill="white")
  source_proof.append({"index":idx,"raw_rgb_sha256":rgbsha,"crop":[470,0,720,430],"frame_hash_validated":idx in [337,469,601]})
 name="M01_A1_N17_RIGHT_SCONCE_TIMELINE_8_FRAMES_V001.jpg"
 path=OUT/name
 tiles.save(path,"JPEG",quality=89,optimize=True)
 (OUT/(name+".b64.txt")).write_text(base64.b64encode(path.read_bytes()).decode()+"\n")
 rgb,rgbsha=frames[601]
 mid=Image.fromarray(rgb,"RGB")
 human_file=ROOT/"production/environment_dynamic/benchmarks/m01_stage_a_v002/evidence/person_mask_proposals/PERSON_PROPOSAL_N17_F0601.png"
 assert sha(human_file.read_bytes())==n17["frames"][2]["person_mask_sha256"]
 protection=np.asarray(Image.open(human_file).convert("L"))>0
 marked=rgb.astype(np.float32).copy()
 marked[protection]=marked[protection]*.55+np.array([35,95,248])*.45
 full=Image.new("RGB",(1440,1315),(13,13,15))
 full.paste(mid,(0,35));full.paste(Image.fromarray(np.clip(marked,0,255).astype("uint8")),(720,35))
 d=ImageDraw.Draw(full);d.text((10,7),"F601 ORIGINAL exact decoded frame",font=font(24),fill="white")
 d.text((730,7),"F601 detected-person mask BLUE (unverified)",font=font(22),fill="white")
 file2="M01_A1_N17_FULLFRAME_PERSON_PROTECTION_F601_V001.jpg"
 f2=OUT/file2;full.save(f2,"JPEG",quality=84,optimize=True)
 (OUT/(file2+".b64.txt")).write_text(base64.b64encode(f2.read_bytes()).decode()+"\n")
 report={"schema":"M01_STAGE_A1_N17_SOURCE_DIAGNOSTIC_V001","status":"SOURCE_FRAMES_EXTRACTED_NOT_CANDLE_GROUND_TRUTH",
 "source_sha256":manifest["source_video_sha256"],"frames":source_proof,"original_N17_mid_light_markers":0,
 "protection_mask_source_sha256":n17["frames"][2]["person_mask_sha256"],
 "timeline_image":name,"timeline_image_sha256":sha(path.read_bytes()),
 "person_overlay_image":file2,"person_overlay_image_sha256":sha(f2.read_bytes()),
 "no_flame_position_approved":True,"no_video_rendered":True,"no_main_merge":True}
 (OUT/"M01_A1_N17_SOURCE_DIAGNOSTIC_V001.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
 print("N17_EXACT_SOURCE_TIMELINE_QC_PASS; FLAME_POSITION_PENDING_VISUAL_CALIBRATION; SOURCE_UNCHANGED")
if __name__=="__main__":main()
