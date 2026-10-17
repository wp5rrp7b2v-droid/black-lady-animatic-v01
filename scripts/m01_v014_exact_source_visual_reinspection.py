#!/usr/bin/env python3
"""Extract exact SHA-pinned source frames for human visual flame registration.

Not a detector. Never asserts a warm bright pixel is a fire source.
Writes full 720x1280 source and ROI contact sheets, each with a UTF-8
base64 inspection sidecar for reviewers who cannot fetch private binaries.
"""
import base64,io,json,pathlib
from PIL import Image,ImageDraw,ImageFont
import importlib.util, numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[1]
S=importlib.util.spec_from_file_location("engine",ROOT/"scripts/m01_engine_v1.py")
engine=importlib.util.module_from_spec(S);S.loader.exec_module(engine)
FONT="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
def font(n):
 try:return ImageFont.truetype(FONT,n)
 except OSError:return ImageFont.load_default()

def store(image,dest,stem,quality=74):
 jpg=dest/f"{stem}.jpg"
 image.save(jpg,quality=quality,optimize=True,subsampling=0)
 with jpg.open("rb") as f:
  b=f.read()
 (dest/f"{stem}.b64.txt").write_text("\n".join(base64.b64encode(b).decode("ascii")[i:i+4000] for i in range(0,len(base64.b64encode(b)),4000))+"\n",encoding="ascii")
 return {"image":jpg.name,"bytes":len(b),"sha256":engine.sha(jpg),
         "base64_sidecar":f"{stem}.b64.txt","dims":list(image.size)}

def run(name,out):
 p=engine.read_profile(name)
 assert p["source"]["type"]=="still_png"
 src,_=engine.load_inputs(p)
 with Image.open(src) as f:
  assert list(f.size)==p["source"]["input_dimensions"]
  image=f.convert("RGB").resize((720,1280),Image.Resampling.LANCZOS)
 out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True)
 manifest={"task":"M01_PO_REJECTED_V013_CORES_SOURCE_VISUAL_REALIGNMENT",
           "status":"SOURCE_VISUAL_INSPECTION_ONLY_NO_FLAME_POINTS_ASSIGNED",
           "profile":name,"source":p["source"]["path"],
           "source_sha256":p["source"]["sha256"],
           "source_exact":engine.sha(src)==p["source"]["sha256"],
           "screen_dims":[720,1280],"padded_or_synthetic_flames":False,
           "lighting_mode_separation":False,"images":[]}
 manifest["images"].append(store(image,out,"EXACT_SOURCE_NO_MARKERS",quality=76))
 # Larger crops of the stored historic receiving-light regions. These are
 # only viewing windows; their centers are not presumed to be flame centers.
 allc=[]
 for idx,fixture in enumerate(p["fixtures"]):
  x0,y0,x1,y1=fixture["region"]["roi_px"]
  x0=max(0,int(x0)-40);y0=max(0,int(y0)-40)
  x1=min(720,int(x1)+40);y1=min(1280,int(y1)+40)
  view=image.crop((x0,y0,x1,y1))
  tw,th=660,330
  view.thumbnail((tw,th),Image.Resampling.LANCZOS)
  canvas=Image.new("RGB",(700,385),(19,18,21))
  canvas.paste(view,((700-view.width)//2,40))
  drawer=ImageDraw.Draw(canvas)
  drawer.text((10,10),f"{idx+1} {fixture['individual_source_id']}  SOURCE ROI: {x0},{y0} to {x1},{y1}",
              font=font(15),fill=(246,234,205))
  drawer.text((12,365),"Historic light ROI, NOT a verified flame core",font=font(13),fill=(196,194,193))
  allc.append(canvas)
 rows=(len(allc)+1)//2
 contact=Image.new("RGB",(1400,rows*385),(18,18,21))
 for idx,pic in enumerate(allc):contact.paste(pic,((idx%2)*700,(idx//2)*385))
 manifest["images"].append(store(contact,out,"EXPANDED_REAL_SOURCE_ROI_CONTACT",quality=79))
 (out/"EXACT_SOURCE_VISUAL_REVIEW_MANIFEST.json").write_text(json.dumps(manifest,indent=2)+"\n")
 print("SOURCE_INSPECTION_ONLY",name,[x["bytes"] for x in manifest["images"]])
if __name__=="__main__":
 import argparse
 a=argparse.ArgumentParser()
 a.add_argument("--profile",required=True);a.add_argument("--out",required=True)
 z=a.parse_args();run(z.profile,z.out)
