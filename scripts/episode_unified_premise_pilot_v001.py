#!/usr/bin/env python3
"""Small editorial premise proof; append-only, no canonical publishing."""
from pathlib import Path
import subprocess, json, hashlib, argparse

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'production/video_candidates/episode_unified_director_v001'
OUT=BASE/'review'

def run(*cmd):
    return subprocess.run(list(map(str,cmd)),check=True,capture_output=True).stdout

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--opening',type=Path,required=True)
    parser.add_argument('--font',type=Path,required=True)
    parser.add_argument('--work',type=Path,required=True)
    a=parser.parse_args(); a.work.mkdir(parents=True,exist_ok=True);OUT.mkdir(parents=True,exist_ok=True)
    assert sha(a.opening)=='70d7922244161dd216a26446fd75531db20eea0ac7fc25f567f6ff14e2746e3a'
    final=OUT/'EPISODE_UNIFIED_PREMISE_PILOT_V001.mp4'
    assert not final.exists(),'Version exists; do not overwrite.'
    bg=BASE/'assets/BLOOD_DOOR_TYPOGRAPHY_BACKPLATE_V001.png'
    # A task-text graphic, not a new canonical story shot or an invented scene.
    cards=[
      {'id':'TASK','frames':225,'lines':[
        ('血门任务',34,294,'B58B84'),
        ('在莫妮卡夫人的庄园中',33,430,'DAD3C8'),
        ('活过五日',66,503,'E7DCD3'),
        ('并找到离开庄园的',35,658,'DAD3C8'),
        ('大门钥匙',60,721,'E7DCD3')]},
      {'id':'HINTS','frames':195,'lines':[
        ('血门提示',34,294,'B58B84'),
        ('提示一',28,437,'A99C91'),
        ('不要淋雨',59,487,'E7DCD3'),
        ('提示二',28,658,'A99C91'),
        ('不要长时间',43,710,'E7DCD3'),
        ('和它对视',59,775,'D89084')]}
    ]
    parts=[]
    common=['-an','-c:v','libx264','-preset','fast','-crf','17','-g','30','-bf','2','-pix_fmt','yuv420p','-r','30','-video_track_timescale','15360']
    for card in cards:
        filters=['scale=720:1280:force_original_aspect_ratio=increase','crop=720:1280','setsar=1']
        for i,(text,size,y,color) in enumerate(card['lines']):
            f=a.work/f"{card['id']}_{i}.txt";f.write_text(text)
            filters.append(f"drawtext=fontfile='{a.font}':textfile='{f}':fontcolor=0x{color}:fontsize={size}:x=(w-text_w)/2:y={y}:shadowcolor=black@0.8:shadowx=1:shadowy=2")
        p=a.work/f"{card['id']}.mp4"
        run('ffmpeg','-v','error','-y','-loop','1','-framerate','30','-i',bg,'-vf',','.join(filters),'-frames:v',card['frames'],*common,p)
        parts.append(p)
    welcome=a.work/'WELCOME.mp4'
    run('ffmpeg','-v','error','-y','-i',a.opening,'-vf','trim=start_frame=0:end_frame=197,setpts=PTS-STARTPTS,scale=720:1280,setsar=1',*common,welcome)
    parts.append(welcome)
    cat=a.work/'concat.ffconcat';cat.write_text('ffconcat version 1.0\n'+''.join(f"file '{p}'\n" for p in parts))
    silent=a.work/'PICTURE.mp4'
    run('ffmpeg','-v','error','-y','-safe','0','-f','concat','-i',cat,'-c:v','copy','-an',silent)
    # New 14s prologue is intentionally silent. Existing first two welcome lines
    # retain their order and speed. Only this independent candidate audio is AAC encoded.
    run('ffmpeg','-v','error','-y','-i',silent,'-i',a.opening,
        '-filter_complex','[1:a]atrim=start=0:end=6.55,asetpts=PTS-STARTPTS,adelay=14000|14000,apad,atrim=end=20.566666667[a]',
        '-map','0:v:0','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',final)
    meta=json.loads(run('ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',final))
    v=next(x for x in meta['streams'] if x['codec_type']=='video')
    assert (v['width'],v['height'],v['r_frame_rate'],int(v['nb_read_frames']))==(720,1280,'30/1',617)
    run('ffmpeg','-v','error','-i',final,'-f','null','-')
    text=ROOT/'source_material/S2_black_lady/S2_SOURCE_BLACK_LADY_TEXT_V001.txt'
    s=text.read_text();task='在莫妮卡夫人的庄园中活过五日并找到离开庄园的大门钥匙'
    assert task in s and '不要淋雨' in s and '不要长时间和它对视' in s
    qc={'status':'TECHNICAL_PASS_CONTENT_SOURCE_PASS_PO_NARRATIVE_REVIEW_PENDING',
        'output':str(final.relative_to(ROOT)),'sha256':sha(final),'frames':617,'fps':30,'resolution':[720,1280],
        'timeline':[{'id':'TASK','start':0,'end':7.5},{'id':'HINTS','start':7.5,'end':14},{'id':'OPENING_FIRST_TWO_LINES','start':14,'end':617/30}],
        'source_opening_sha256':sha(a.opening),'source_opening_exact_identity':True,
        'source_text':str(text.relative_to(ROOT)),'source_task':task,'source_hints':['不要淋雨','不要长时间和它对视'],
        'backplate_sha256':sha(bg),'typography':'Noto Sans SC Medium; clean deterministic Chinese typesetting',
        'audio':'First 14s silent; source opening audio 0-6.55s starts at 14s; speed unchanged; candidate AAC re-encoded, no exact packet-copy claim.',
        'new_voice_music_or_foley':False,'character_animation':False,'transition_fx':False,'full_decode':'PASS',
        'old_canonical_assets_modified':False,'public_upload':False,'github_actions_run':False,
        'limits':'Premise wording/readability and welcome juxtaposition only. No claim of complete combined-film improvement.',
        'review_pass':['Task and both original hints understandable on one viewing','庄园大门 key is not confused with the castle entrance','Text-to-welcome transition creates curiosity without excessive explanation'],
        'review_fail':['Text requires pausing or is unreadable','Silent prologue feels stalled or destroys momentum','Task scope becomes misleading or suspense is weakened']}
    (OUT/'EPISODE_UNIFIED_PREMISE_PILOT_QC_V001.json').write_text(json.dumps(qc,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(qc,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
