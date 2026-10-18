#!/usr/bin/env python3
"""Smaller, quieter handwritten typography after PO layout correction."""
import argparse,json
from pathlib import Path
from episode_unified_premise_pilot_v002 import ROOT,BASE,run,sha,audio,tail

def main():
 p=argparse.ArgumentParser();p.add_argument('--work',type=Path,required=True);p.add_argument('--welcome',type=Path,required=True);a=p.parse_args();a.work.mkdir(parents=True,exist_ok=True)
 old=BASE/'review/EPISODE_UNIFIED_PREMISE_PILOT_V001.mp4';assert sha(old)=='ac25d2d6906a555a7bd5a9fabecaea87fe361a05ece4e064c184b6b82b5b2aa0'
 final=BASE/'review/EPISODE_UNIFIED_PREMISE_PILOT_V004.mp4';assert not final.exists()
 bg=BASE/'assets/BLOOD_DOOR_TYPOGRAPHY_BACKPLATE_V001.png';font=BASE/'assets/fonts/LongCang-Regular.ttf'
 cards=[('TASK',225,[('血门任务',96,403,'9D5C58'),('在莫妮卡夫人的庄园中',38,565,'C8C2B8'),('活过五日',46,628,'D6CFC4'),('并找到离开庄园的',38,704,'C8C2B8'),('大门钥匙',46,767,'D6CFC4')]),
        ('HINTS',195,[('血门提示',96,403,'9D5C58'),('提示一',28,554,'9B9388'),('不要淋雨',46,594,'D6CFC4'),('提示二',28,700,'9B9388'),('不要长时间和它对视',40,740,'D6CFC4')])]
 parts=[]
 for label,frames,lines in cards:
  filters=['scale=720:1280:force_original_aspect_ratio=increase','crop=720:1280','setsar=1']
  for i,(t,size,y,color) in enumerate(lines):
   f=a.work/f'{label}_{i}.txt';f.write_text(t)
   filters.append(f"drawtext=fontfile='{font}':textfile='{f}':fontcolor=0x{color}:fontsize={size}:x=(w-text_w)/2:y={y}")
  vf=','.join(filters);part=a.work/f'{label}.mp4'
  run('ffmpeg','-v','error','-y','-loop','1','-framerate','30','-i',bg,'-vf',vf,'-frames:v',frames,'-an','-c:v','libx264','-preset','fast','-crf','17','-g','30','-bf','2','-pix_fmt','yuv420p','-r','30','-video_track_timescale','15360',part)
  parts.append(part)
  run('ffmpeg','-v','error','-y','-i',bg,'-vf',vf,'-frames:v','1',a.work/f'{label}.png')
 parts.append(a.welcome);cat=a.work/'concat.ffconcat';cat.write_text('ffconcat version 1.0\n'+''.join(f"file '{x}'\n" for x in parts))
 picture=a.work/'picture.mp4';run('ffmpeg','-v','error','-y','-safe','0','-f','concat','-i',cat,'-map','0:v:0','-an','-c:v','copy',picture)
 run('ffmpeg','-v','error','-y','-i',picture,'-i',old,'-map','0:v:0','-map','1:a:0','-c','copy','-movflags','+faststart',final)
 info=json.loads(run('ffprobe','-v','error','-count_frames','-select_streams','v:0','-show_entries','stream=width,height,r_frame_rate,nb_read_frames','-of','json',final))['streams'][0]
 assert (info['width'],info['height'],info['r_frame_rate'],int(info['nb_read_frames']))==(720,1280,'30/1',617)
 ah=audio(old);assert audio(final)==ah;th=tail(old);assert tail(final)==th
 run('ffmpeg','-v','error','-i',final,'-f','null','-')
 qc={'status':'TECHNICAL_PASS_PO_TYPOGRAPHY_REVIEW_PENDING','output_sha256':sha(final),'frames':617,'fps':30,'resolution':[720,1280],
 'typography':'Long Cang handwritten font; 96px main titles, 38-46px body; muted red titles and aged-ivory body; no blood effects.',
 'layout':'Text block approx 403-813px vertically (32% of 1280px); content centered, substantial negative space.',
 'text':{label:[x[0] for x in lines] for label,frames,lines in cards},'font_sha256':sha(font),
 'audio_identical_to_V001':True,'audio_payload_sha256':ah,'welcome_frames_identical_to_V001':True,'welcome_tail_decoded_sha256':th,
 'full_decode':'PASS','canonical_assets_modified':False,'public_upload':False,'github_actions_run':False}
 (BASE/'review/EPISODE_UNIFIED_PREMISE_PILOT_QC_V004.json').write_text(json.dumps(qc,ensure_ascii=False,indent=2)+'\n');print(json.dumps(qc,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
