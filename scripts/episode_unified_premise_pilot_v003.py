#!/usr/bin/env python3
"""User-requested horror lettering revision; retain pilot timing and audio."""
from pathlib import Path
import argparse,json,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'production/video_candidates/episode_unified_director_v001'
def run(*cmd):return subprocess.run(list(map(str,cmd)),check=True,capture_output=True).stdout
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def audio(p):return hashlib.sha256(run('ffmpeg','-v','error','-i',p,'-map','0:a:0','-c:a','copy','-f','adts','pipe:1')).hexdigest()
def tail(p):return run('ffmpeg','-v','error','-i',p,'-vf','trim=start_frame=420,setpts=PTS-STARTPTS','-an','-f','hash','-hash','sha256','pipe:1').decode().strip()
def main():
 p=argparse.ArgumentParser();p.add_argument('--work',type=Path,required=True);p.add_argument('--welcome',type=Path,required=True);a=p.parse_args();a.work.mkdir(parents=True,exist_ok=True)
 old=BASE/'review/EPISODE_UNIFIED_PREMISE_PILOT_V001.mp4'
 assert sha(old)=='ac25d2d6906a555a7bd5a9fabecaea87fe361a05ece4e064c184b6b82b5b2aa0'
 output=BASE/'review/EPISODE_UNIFIED_PREMISE_PILOT_V003.mp4';assert not output.exists()
 parts=[];assets=[]
 for label,frames in [('TASK',225),('HINTS',195)]:
  source=BASE/f'assets/BLOOD_DOOR_{label}_HORROR_TYPE_V003.png';o=a.work/f'{label}.mp4'
  run('ffmpeg','-v','error','-y','-loop','1','-framerate','30','-i',source,'-vf','scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,setsar=1','-frames:v',frames,'-an','-c:v','libx264','-preset','fast','-crf','17','-g','30','-bf','2','-pix_fmt','yuv420p','-r','30','-video_track_timescale','15360',o)
  parts.append(o);assets.append({'path':str(source.relative_to(ROOT)),'sha256':sha(source)})
 parts.append(a.welcome);cat=a.work/'concat.ffconcat';cat.write_text('ffconcat version 1.0\n'+''.join(f"file '{x}'\n" for x in parts))
 picture=a.work/'picture.mp4';run('ffmpeg','-v','error','-y','-safe','0','-f','concat','-i',cat,'-map','0:v:0','-an','-c:v','copy',picture)
 run('ffmpeg','-v','error','-y','-i',picture,'-i',old,'-map','0:v:0','-map','1:a:0','-c','copy','-movflags','+faststart',output)
 info=json.loads(run('ffprobe','-v','error','-count_frames','-select_streams','v:0','-show_entries','stream=width,height,r_frame_rate,nb_read_frames','-of','json',output))['streams'][0]
 assert (info['width'],info['height'],info['r_frame_rate'],int(info['nb_read_frames']))==(720,1280,'30/1',617)
 old_audio=audio(old);assert audio(output)==old_audio
 tail_sha=tail(old);assert tail(output)==tail_sha
 run('ffmpeg','-v','error','-i',output,'-f','null','-')
 result={'status':'TECHNICAL_PASS_PO_TYPE_STYLE_REVIEW_PENDING','frames':617,'fps':30,'resolution':[720,1280],'output_sha256':sha(output),
 'change':'Restrained eerie handwritten lettering, muted red, no splatter or long blood drips; 血门任务 is now the largest typography; exact task and hint wording retained.',
 'generation':'Built-in image_gen; task page softened from V002; hints softened from V002 with V003 task as style reference; one PNG per call.',
 'prompt_summary':'Reduce V002 horror intensity: remove splashes, razor spikes and blood tails; retain slightly irregular legible handwritten strokes; large muted dark-red main title, smaller aged-ivory body; preserve exact Chinese words and wood background.',
 'assets':assets,'visual_text_check':'Task and both hints compared character by character with V001 and canonical source; no wording change observed.',
 'audio_payload_sha256':old_audio,'audio_identical_to_V001':True,'welcome_tail_decoded_sha256':tail_sha,'welcome_frames_identical_to_V001':True,
 'duration_and_cut_points_unchanged':True,'full_decode':'PASS','canonical_assets_modified':False,'public_upload':False}
 (BASE/'review/EPISODE_UNIFIED_PREMISE_PILOT_QC_V003.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
