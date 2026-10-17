#!/usr/bin/env python3
"""Enlarge physically plausible candle fixture regions from SHA-pinned original images.

All crops sourced directly from approved PNGs; NO candle points are generated.
Coordinates use the 720x1280 exact-source review video canvas, X/Y absolute.
"""
import base64,json,pathlib,argparse
from PIL import Image,ImageDraw,ImageFont
import importlib.util
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("m01",ROOT/"scripts/m01_engine_v1.py")
m01=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m01)
MAP={
"N23":[("MAIN_CANDLE_CHANDELIER",170,20,285,165),("RIGHT_TOP_PARTIAL",695,50,720,170),("RIGHT_LOWER_PARTIAL",695,400,720,480)],
"NEW02":[("LEFT_CROPPED_CHANDELIER",0,0,85,145),("MID_CHANDELIER",258,160,348,263),("DEEPER_WALL_CHANDELIER",442,268,505,360),("RIGHT_ARCH_CHANDELIER",625,328,686,409),("FAR_RIGHT_PARTIAL",690,405,720,485)]
}
def run(name,profile,out):
 p=m01.read_profile(profile)
 src,_=m01.load_inputs(p)
 assert p["source"]["type"]=="still_png"
 with Image.open(src) as im:
  image=im.convert("RGB").resize((720,1280),Image.Resampling.LANCZOS)
 out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True)
 try:font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",15)
 except OSError:font=ImageFont.load_default()
 j={"source_sha256":p["source"]["sha256"],"source_verified":m01.sha(src)==p["source"]["sha256"],
    "shot":name,"status":"ZOOMED_SOURCE_ONLY_NO_FLAME_ASSIGNMENTS",
    "coordinate_space":"720x1280","crops":[]}
 for tag,x0,y0,x1,y1 in MAP[name]:
  crop=image.crop((x0,y0,x1,y1))
  zoom=4
  resized=crop.resize((crop.width*zoom,crop.height*zoom),Image.Resampling.LANCZOS)
  pic=Image.new("RGB",(resized.width+80,resized.height+60),(15,16,19))
  pic.paste(resized,(58,32))
  d=ImageDraw.Draw(pic)
  d.text((58,6),tag,font=font,fill=(255,255,255))
  for x in range((x0//10)*10,x1,10):
   dx=58+round((x-x0)*zoom)
   if dx<58:continue
   d.text((dx-9,19),str(x),font=font,fill=(252,226,164))
  for y in range((y0//10)*10,y1,10):
   dy=32+(y-y0)*zoom
   if dy<32:continue
   d.text((2,dy-8),str(y),font=font,fill=(252,226,164))
  dst=out/f"{tag}_SOURCE_ZOOM.jpg"
  pic.save(dst,quality=88,subsampling=0,optimize=True)
  b=base64.b64encode(dst.read_bytes()).decode("ascii")
  (out/f"{tag}_SOURCE_ZOOM.b64.txt").write_text("\n".join(b[i:i+4000] for i in range(0,len(b),4000))+"\n")
  j["crops"].append({"label":tag,"pixel_window":[x0,y0,x1,y1],
       "filename":dst.name,"sha256":m01.sha(dst),"dimensions":list(pic.size)})
 (out/"SOURCE_CANDLE_CLOSEUP_MANIFEST.json").write_text(json.dumps(j,indent=2)+"\n")
 print("EXACT_SOURCE_CANDLE_ZOOMS",name,len(j["crops"]))
if __name__=="__main__":
 a=argparse.ArgumentParser();a.add_argument("--shot",required=True);a.add_argument("--profile",required=True);a.add_argument("--out",required=True)
 s=a.parse_args();run(s.shot,s.profile,s.out)
