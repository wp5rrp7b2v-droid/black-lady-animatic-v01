#!/usr/bin/env python3
"""Visualize draft positions on true N23 and NEW02 source, without promoting to Atlas.

Manual points originate from direct original-image inspection, NOT V013 generic
warm-pixel maxima. They remain unapproved position candidates until PO review.
"""
import base64,hashlib,json,pathlib,argparse,importlib.util
from PIL import Image,ImageDraw,ImageFont
ROOT=pathlib.Path(__file__).resolve().parents[1]
mod=importlib.util.spec_from_file_location("m01",ROOT/"scripts/m01_engine_v1.py")
engine=importlib.util.module_from_spec(mod);mod.loader.exec_module(engine)
def load_font(s):
 try:return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",s)
 except OSError:return ImageFont.load_default()
ZOOMS={
"N23":[("MAIN_CANDLE_CHANDELIER",[170,20,285,165])],
"NEW02":[("LEFT_CROPPED_CHANDELIER",[0,0,85,145]),("MID_CHANDELIER",[258,160,348,263]),
("DEEPER_WALL_CHANDELIER",[442,268,505,360]),("RIGHT_ARCH_CHANDELIER",[625,328,686,409])]
}
def ring(draw,x,y,index,scale=1):
 x,y=int(round(x)),int(round(y))
 rr=9*scale
 draw.ellipse((x-rr,y-rr,x+rr,y+rr),outline=(223,35,212),width=max(2,2*scale))
 draw.ellipse((x-2*scale,y-2*scale,x+2*scale,y+2*scale),fill=(30,238,230))
 # source pixels inside circle are unchanged; cyan center is overlay, not a mask.
def save(pic,path,sidecar=False):
 pic.save(path,quality=88,subsampling=0,optimize=True)
 if sidecar:
  b=base64.b64encode(path.read_bytes()).decode("ascii")
  path.with_suffix(".b64.txt").write_text("\n".join(b[i:i+4000] for i in range(0,len(b),4000))+"\n")
 return {"file":path.name,"sha256":engine.sha(path),"bytes":path.stat().st_size,"dims":list(pic.size)}
def main(name,out):
 root=ROOT/"production/environment_dynamic/benchmarks/m01_stage_a_v002"
 draft=json.loads((root/"M01_V014_TRUE_FLAME_CENTERS_VISUAL_CORRECTION_CANDIDATE.json").read_text())
 assert draft["status"]=="CHAT_DIRECT_VISUAL_SOURCE_INSPECTION_PENDING_PO_APPROVAL"
 shot=draft["shots"][name]
 p=engine.read_profile(shot["source_profile"])
 src,_=engine.load_inputs(p)
 with Image.open(src) as im:
  source=im.convert("RGB").resize((720,1280),Image.Resampling.LANCZOS)
 out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True)
 full=source.copy();draw=ImageDraw.Draw(full)
 for i,f in enumerate(shot["flames"],1):
  x,y=f["center"]
  assert 0<=x<720 and 0<=y<1280
  ring(draw,x,y,i)
 title=ImageDraw.Draw(full)
 title.rectangle((0,1194,720,1280),fill=(9,11,15))
 title.text((13,1207),f"{name}: {len(shot['flames'])} SOURCE-VISUAL CANDLE POINTS",font=load_font(22),fill=(252,252,252))
 title.text((13,1241),"MAGENTA=unapproved flame candidate. Cropped/unclear lights excluded.",font=load_font(14),fill=(255,211,97))
 a=save(full,out/f"{name}_V014_DIRECT_SOURCE_FLAME_POINT_OVERLAY.jpg",True)
 tiles=[]
 for n,(tag,region) in enumerate(ZOOMS[name]):
  x0,y0,x1,y1=region
  im=source.crop(region)
  zoom=4;im=im.resize((im.width*zoom,im.height*zoom),Image.Resampling.LANCZOS)
  canvas=Image.new("RGB",(max(im.width+90,530),max(im.height+73,400)),(18,19,22))
  canvas.paste(im,(55,35))
  d=ImageDraw.Draw(canvas)
  d.text((12,9),tag,font=load_font(17),fill=(255,246,201))
  for i,f in enumerate(shot["flames"],1):
   x,y=f["center"]
   if x0<=x<x1 and y0<=y<y1:
    xx=55+(x-x0)*zoom;yy=35+(y-y0)*zoom
    ring(d,xx,yy,i,scale=2)
    d.text((max(57,xx-5),min(canvas.height-24,yy+18)),f["id"].split("_")[-1],
          font=load_font(15),fill=(255,255,255),stroke_width=1,stroke_fill=(20,20,20))
  d.text((10,canvas.height-25),f"Pixel-space crop x={x0}..{x1}, y={y0}..{y1}. REVIEW ONLY.",font=load_font(13),fill=(219,211,193))
  tiles.append(canvas)
 maxw=max(im.width for im in tiles)
 height=sum(im.height for im in tiles)
 sheet=Image.new("RGB",(maxw,height),(15,15,16))
 y=0
 for im in tiles:
  sheet.paste(im,(0,y));y+=im.height
 b=save(sheet,out/f"{name}_V014_DIRECT_SOURCE_ENLARGED_FLAME_REVIEW.jpg",True)
 report={"schema":"M01_V014_DIRECT_VISUAL_FLAME_LOCATOR_REVIEW","status":"PO_VISUAL_REVIEW_PENDING_NOT_APPROVED",
 "shot":name,"source_sha256":p["source"]["sha256"],"source_exact":engine.sha(src)==p["source"]["sha256"],
 "draft_sha256":engine.sha(root/"M01_V014_TRUE_FLAME_CENTERS_VISUAL_CORRECTION_CANDIDATE.json"),
 "flames":shot["flames"],"deferred":shot["deferred"],"registered_flame_core_masks_created":False,
 "scope":"visual source-position draft only, no actual flame segmentation GT, no person masks and no video render",
 "images":[a,b],"reference_V012_unchanged":True,"publication_allowed":False}
 (out/f"{name}_V014_DIRECT_SOURCE_FLAME_LOCATOR_REPORT.json").write_text(json.dumps(report,indent=2)+"\n")
 print("DIRECT_VISUAL_SOURCE_FLAME_LOCATOR_PENDING_PO_REVIEW",name,len(shot["flames"]))
if __name__=="__main__":
 ap=argparse.ArgumentParser();ap.add_argument("--shot",required=True);ap.add_argument("--out",required=True)
 args=ap.parse_args();main(args.shot,args.out)
