#!/usr/bin/env python3
"""S02-B V007 candle-aware entire editorial coverage. Review only.
Uses PO-accepted N23/NEW02 M01 temporal style, independently inspected frame
contact sheet for every other shot. Never changes source stills, base V006,
audio, Video Index, locked masters or main. No M02/M03/M04/M05.
"""
import hashlib,json,math,pathlib,subprocess
import numpy as np
from PIL import Image

ROOT=pathlib.Path(__file__).resolve().parents[1]
BASE=ROOT/"production/video_candidates/assets/S02_B_V006_CINEMATIC_ROUGH_RECONSTRUCTED_CANDIDATE_V001.mp4"
BASE_SHA="7af0982385c877b159f053233378b98c2c035ce19df257a6e65077dfbaa33402"
EDL=ROOT/"production/editorial_specs/S02_B_V006_CINEMATIC_ROUGH_EDL_V001.json"
OUT=ROOT/"_s02b_v007_full_m01"
VIDEO=OUT/"S02_B_V007_FULL_M01_CANDLELIGHT_REVIEW_V001.mp4"
AB=OUT/"S02_B_V007_AB_ORIGINAL_VS_FULL_M01_REVIEW_V001.mp4"
QC=OUT/"S02_B_V007_FULL_M01_AND_AB_QC_V001.json"
INTERMEDIATE=OUT/"v007_m01_video_only.mp4"
W,H,FPS,TOTAL=720,1280,30,1927
TINT=np.array([12,7,1.7],dtype=np.float32)
# Anchor positions are normalized image coordinates, manually aligned using
# actual V006 mid-frame contact sheet (not a blind universal flicker filter).
# For each: (x,y,normalized_x_sigma,normalized_y_sigma).
# Luminous practicals / architectural light only, never portrait or full frame.
ANCHORS={
 "N16_PART_1":[(.894,.105,.027,.042)],
 "N16_PART_2":[], # no visible candle; daylight dominates. Explicit honest exemption
 "N17":[], # daylight-lit close-up, no identified practical flame
 "N18":[(.810,.180,.035,.053),(.875,.195,.028,.046)],
 "N19":[(.058,.215,.030,.054)],
 "N20_FIRST":[(.116,.183,.041,.048),(.479,.217,.032,.046),(.835,.208,.043,.060)],
 "V006_NEW_01":[(.125,.188,.046,.051),(.494,.206,.035,.054),(.926,.168,.043,.057)],
 "JUN_APPROVED_REACTION":[(.077,.236,.043,.065),(.902,.240,.033,.054)],
 "N21":[(.608,.172,.038,.051),(.893,.182,.043,.063)],
 "N22_FIRST":[(.119,.162,.037,.054),(.647,.183,.041,.052)],
 "V006_NEW_02":"APPROVED_NEW02_PRECISE_ARCHITECTURE_ROI",
 "N23":"APPROVED_N23_PRECISE_ARCHITECTURE_ROI",
 "A06":[(.086,.355,.032,.053),(.894,.311,.037,.059)],
 "N24":[(.091,.179,.040,.053),(.888,.208,.045,.060)],
 "N25":[(.112,.215,.042,.052),(.899,.267,.043,.060)],
 "NING_REACTION_APPROVED":[(.110,.195,.039,.058),(.952,.402,.026,.050)],
 "N26":[(.115,.176,.043,.052),(.864,.191,.046,.059)],
}
EXEMPT_REASON={
 "N16_PART_2":"sunlight dominates; no identified candle in reviewed mid-frame",
 "N17":"daylit character close-up without identified in-frame flame",
}
NEW02_PROFILE=ROOT/"production/environment_dynamic/shot_profiles/NEW02_M01_M03_TEST_V001.json"

def digest(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for data in iter(lambda:f.read(1024*1024),b""):h.update(data)
    return h.hexdigest()

def probe(path):
    return json.loads(subprocess.check_output(["ffprobe","-v","error",
        "-show_entries","stream=codec_type,codec_name,nb_frames,width,height,r_frame_rate:format=duration",
        "-of","json",str(path)],text=True))

def audio_packets(path):
    dat=json.loads(subprocess.check_output(["ffprobe","-v","error",
        "-select_streams","a:0","-show_packets",
        "-show_entries","packet=pts_time,duration_time,data_hash",
        "-show_data_hash","sha256","-of","json",str(path)],text=True))
    return [(p.get("pts_time"),p.get("duration_time"),p.get("data_hash")) for p in dat["packets"]]

def new02_mask():
    p=json.loads(NEW02_PROFILE.read_text())
    assert p["source_identity"]["sha256"]=="d1866a667d7a24b8c5ae5b7670486b8b312e6f4a8fbce457763668e84d843bd4"
    m=np.zeros((H,W),dtype=np.float32)
    allowed=np.zeros((H,W),dtype=bool)
    for a in p["candlelight"]["anchors"]:
        x0,x1,y0,y1=a["roi"]
        xa,xb=int(x0*W),int(np.ceil(x1*W))
        ya,yb=int(y0*H),int(np.ceil(y1*H))
        assert 0<=xa<xb<=W and 0<=ya<yb<int(.4*H)
        yy,xx=np.ogrid[ya:yb,xa:xb]
        cx,cy=a["center"];sx,sy=a["radius"]
        local=np.exp(-.5*((((xx+.5)/W-cx)/sx)**2+(((yy+.5)/H-cy)/sy)**2)).astype("float32")
        local[local<.003]=0
        m[ya:yb,xa:xb]+=local
        allowed[ya:yb,xa:xb]|=local>0
    m=np.clip(m,0,1);m[m<.003]=0
    assert not np.any((m>0)&~allowed)
    return m

def n23_mask():
    y,x=np.ogrid[:H,:W]
    left=np.exp(-.5*(((x-231)/99)**2+((y-128)/111)**2))
    left*=np.clip((286-y)/48,0,1)
    upper=np.exp(-.5*(((x-711)/36)**2+((y-123)/55)**2))*np.clip((x-690)/17,0,1)
    lower=np.exp(-.5*(((x-712)/38)**2+((y-433)/60)**2))*np.clip((x-694)/17,0,1)
    m=(left+.64*upper+.60*lower).astype("float32")
    m[m<.003]=0
    return m

def manual_mask(anchors):
    y,x=np.ogrid[:H,:W]
    m=np.zeros((H,W),np.float32)
    for cx,cy,sx,sy in anchors:
        assert 0<cx<1 and 0<cy<.48
        assert 0<sx<.08 and 0<sy<.085
        dist=((x/W-cx)/sx)**2+((y/H-cy)/sy)**2
        local=np.exp(-.5*dist)
        local=np.where(dist<=4.0,local,0).astype("float32")
        m+=local
    m=np.clip(m,0,1)
    # An explicit mask goes no further than the intended wall and flame halo;
    # never globally modulate dark/bright regions.
    m[m<.003]=0
    return m

def frame_effect(raw,mask,i,frames):
    # N23 and NEW02 PO-accepted M01 signal; re-scale envelope to each shot's duration.
    t=i/FPS
    envelope=math.sin(math.pi*i/(frames-1))**1.2
    signal=(.50*math.sin(2*math.pi*.94*t)
           +.32*math.sin(2*math.pi*2.07*t+.64)
           +.18*math.sin(2*math.pi*3.06*t+1.4))
    original=np.frombuffer(raw,dtype=np.uint8).reshape(H,W,3)
    delta=envelope*signal*(mask[:,:,None]*TINT[None,None,:])
    mod=np.clip(original.astype(np.float32)+delta,0,255).astype(np.uint8)
    diff=np.any(mod!=original,axis=-1)
    maxdelta=int(np.abs(mod.astype("int16")-original.astype("int16")).max())
    outside=int(np.count_nonzero(diff & (mask==0)))
    return mod.tobytes(),maxdelta,outside,bool(np.array_equal(mod,original))

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    assert digest(BASE)==BASE_SHA,"LOCKED_BASE_SHA_CHANGED"
    edl=json.loads(EDL.read_text())["timeline"]
    assert len(edl)==17 and edl[0]["start_frame"]==0 and edl[-1]["end_frame_exclusive"]==TOTAL
    assert all(a["end_frame_exclusive"]==b["start_frame"] for a,b in zip(edl,edl[1:]))
    assert set(ANCHORS)=={s["id"] for s in edl}
    masks={}
    for s in edl:
        sid=s["id"]
        masks[sid]=(new02_mask() if sid=="V006_NEW_02" else
                    n23_mask() if sid=="N23" else manual_mask(ANCHORS[sid]))
        nonzero=int(np.count_nonzero(masks[sid]))
        if sid in EXEMPT_REASON: assert nonzero==0
        else:assert 0<nonzero<.20*W*H,f"BAD_LIGHT_MASK_{sid}"
    before=probe(BASE)
    vb=next(x for x in before["streams"] if x["codec_type"]=="video")
    assert (int(vb["nb_frames"]),vb["width"],vb["height"],vb["r_frame_rate"])==(TOTAL,W,H,"30/1")
    original_audio=audio_packets(BASE)
    assert len(original_audio)==3013
    dec=subprocess.Popen(["ffmpeg","-hide_banner","-loglevel","error","-xerror",
        "-i",str(BASE),"-map","0:v:0","-f","rawvideo","-pix_fmt","rgb24",
        "-vsync","0","pipe:1"],stdout=subprocess.PIPE)
    enc=subprocess.Popen(["ffmpeg","-hide_banner","-loglevel","error","-y",
        "-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-framerate",str(FPS),
        "-i","pipe:0","-an","-c:v","libx264","-preset","veryfast","-crf","18",
        "-pix_fmt","yuv420p","-r",str(FPS),"-movflags","+faststart",str(INTERMEDIATE)],
        stdin=subprocess.PIPE)
    stats={}
    for shot in edl:
        sid=shot["id"]
        stats[sid]={"start_frame":shot["start_frame"],"end_frame_exclusive":shot["end_frame_exclusive"],
                    "enabled":sid not in EXEMPT_REASON,"mask_pixels":int(np.count_nonzero(masks[sid])),
                    "frames":0,"max_raw_rgb_delta":0,"changed_pixels_outside_mask":0,
                    "first_raw_frame_matches_source":False,"last_raw_frame_matches_source":False,
                    "exemption_reason":EXEMPT_REASON.get(sid)}
    frame=0
    try:
        for shot in edl:
            sid=shot["id"];mask=masks[sid];stat=stats[sid]
            length=shot["end_frame_exclusive"]-shot["start_frame"]
            for j in range(length):
                raw=dec.stdout.read(W*H*3)
                assert len(raw)==W*H*3,f"SHORT_SOURCE_FRAME_{frame}"
                if sid not in EXEMPT_REASON:
                    edited,maxdelta,outside,identical=frame_effect(raw,mask,j,length)
                    assert maxdelta<=12 and outside==0,f"MASK_FAILURE_{sid}_{j}"
                    stat["max_raw_rgb_delta"]=max(stat["max_raw_rgb_delta"],maxdelta)
                    stat["changed_pixels_outside_mask"]=max(stat["changed_pixels_outside_mask"],outside)
                    if j==0:stat["first_raw_frame_matches_source"]=identical
                    if j==length-1:stat["last_raw_frame_matches_source"]=identical
                    raw=edited
                else:
                    if j==0:stat["first_raw_frame_matches_source"]=True
                    if j==length-1:stat["last_raw_frame_matches_source"]=True
                enc.stdin.write(raw)
                frame+=1;stat["frames"]+=1
        assert dec.stdout.read(1)==b""
    finally:
        dec.stdout.close()
        enc.stdin.close()
    assert dec.wait()==0 and enc.wait()==0 and frame==TOTAL
    assert all(x["first_raw_frame_matches_source"] and x["last_raw_frame_matches_source"] for x in stats.values())
    assert all(x["max_raw_rgb_delta"]>0 for x in stats.values() if x["enabled"]),"M01_INVISIBLE_SEGMENT"
    # Preserve video timebase and copy AAC packet payload/PTS/duration unchanged.
    subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-y",
      "-i",str(INTERMEDIATE),"-i",str(BASE),"-map","0:v:0","-map","1:a:0",
      "-c:v","copy","-c:a","copy","-copyts","-start_at_zero",
      "-movflags","+faststart",str(VIDEO)],check=True)
    pv=probe(VIDEO)
    videost=next(x for x in pv["streams"] if x["codec_type"]=="video")
    assert (int(videost["nb_frames"]),videost["width"],videost["height"],videost["r_frame_rate"])==(TOTAL,W,H,"30/1")
    assert abs(float(pv["format"]["duration"])-64.25)<.035
    assert audio_packets(VIDEO)==original_audio
    # Render full-duration synchronized A/B; one original audio track only.
    labels=(
        "[0:v]pad=iw:ih+72:0:72:black,drawtext=text='A V006 ORIGINAL':fontsize=29:fontcolor=white:x=24:y=18[va];"
        "[1:v]pad=iw:ih+72:0:72:black,drawtext=text='B V007 FULL M01':fontsize=29:fontcolor=white:x=24:y=18[vb];"
        "[va][vb]hstack=inputs=2[v]"
    )
    subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-y",
      "-i",str(BASE),"-i",str(VIDEO),"-filter_complex",labels,
      "-map","[v]","-map","0:a:0","-c:v","libx264",
      "-preset","veryfast","-crf","20","-pix_fmt","yuv420p","-r","30",
      "-c:a","copy","-copyts","-start_at_zero","-movflags","+faststart",str(AB)],check=True)
    p_ab=probe(AB); va=next(x for x in p_ab["streams"] if x["codec_type"]=="video")
    assert (int(va["nb_frames"]),va["width"],va["height"],va["r_frame_rate"])==(TOTAL,1440,1352,"30/1")
    assert abs(float(p_ab["format"]["duration"])-64.25)<.035
    assert audio_packets(AB)==original_audio
    for p in (VIDEO,AB):
        for stream in ("v:0","a:0"):
            subprocess.run(["ffmpeg","-hide_banner","-v","error","-xerror",
                "-i",str(p),"-map","0:"+stream,"-f","null","-"],check=True)
    assert digest(BASE)==BASE_SHA
    covered=sum(x["frames"] for x in stats.values() if x["enabled"])
    assert covered==1433
    report={
      "task":"S02_B_V007_FULL_M01_CANDLELIGHT_AND_AB_REVIEW_V001",
      "status":"TECHNICAL_PASS_PO_VISUAL_REVIEW_PENDING",
      "base_V006_exact_sha256":BASE_SHA,
      "baseline":"N23_AND_NEW02_V003_PO_ACCEPTED_M01_ONLY",
      "shot_review_evidence":"production/video_candidates/review_m01_v001/analysis/S02B_V007_SHOT_CONTACT_SHEET_V001.jpg.b64.txt",
      "total_nodes":len(edl),"m01_enabled_nodes":sum(x["enabled"] for x in stats.values()),
      "exempt_nodes":list(EXEMPT_REASON),"eligible_coverage_frames":covered,
      "eligible_coverage_seconds":covered/FPS,"overall_timeline_coverage_percent":round(covered/TOTAL*100,3),
      "source_shots_with_no_supported_practical":EXEMPT_REASON,
      "all_m01_masks_are_local_architecture_or_candle_regions":True,
      "globally_modulated_frame_count":0,"m02_m03_m04_m05_enabled":False,
      "frame_count":TOTAL,"fps":FPS,"duration_seconds":64.25,
      "audio_packet_count":len(original_audio),
      "v007_original_AAC_packet_contents_and_timestamps_identical":True,
      "AB_original_AAC_packet_contents_and_timestamps_identical":True,
      "v007":{"file":VIDEO.name,"bytes":VIDEO.stat().st_size,"sha256":digest(VIDEO),"dimensions":[W,H]},
      "ab":{"file":AB.name,"bytes":AB.stat().st_size,"sha256":digest(AB),"dimensions":[1440,1352]},
      "node_exact_raw_region_protection_and_boundaries":stats,
      "source_mp4_unchanged":True,"approved_PNGs_unchanged":True,
      "official_video_index_unchanged":True,"no_canonical_publication":True,
      "no_main_merge":True,"po_approved_final_video":False,
      "note":"All 17 shots individually evaluated; 15 with verified local practical candle masks and 2 daylight/no-candle exceptions. MP4 compression changes pixels globally but pre-encode RAW outside effect masks unchanged."
    }
    QC.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    INTERMEDIATE.unlink(missing_ok=True)
    print("S02_B_V007_FULL_M01_AND_AB_TECHNICAL_PASS",json.dumps({k:v for k,v in report.items() if k!="node_exact_raw_region_protection_and_boundaries"},ensure_ascii=False),flush=True)

if __name__=="__main__":
    main()
