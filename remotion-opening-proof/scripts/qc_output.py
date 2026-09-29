"""Validate decoded output and write technical evidence only after all checks pass."""
from fractions import Fraction
import hashlib
import json
import os
import subprocess
import sys
from prepare_inputs import OUT, OUTPUT_NAME, probe, require


def qc():
    manifest = json.loads((OUT / 'opening_proof_input_manifest.json').read_text())
    output = OUT / f'{OUTPUT_NAME}.mp4'
    require(output.is_file() and output.stat().st_size > 0, 'missing output', 'OUTPUT_QC_FAILURE')
    metadata = probe(output)
    videos = [s for s in metadata['streams'] if s['codec_type'] == 'video']
    audios = [s for s in metadata['streams'] if s['codec_type'] == 'audio']
    require(len(videos) == 1 and len(audios) == 1, 'expected one video and one audio stream', 'OUTPUT_QC_FAILURE')
    v, a = videos[0], audios[0]
    for key, expected in [('codec_name', 'h264'), ('pix_fmt', 'yuv420p'), ('width', 1080), ('height', 1920)]:
        require(v[key] == expected, f'{key}: {v[key]} != {expected}', 'OUTPUT_QC_FAILURE')
    require(Fraction(v['avg_frame_rate']) == 30 and Fraction(v['r_frame_rate']) == 30, 'FPS mismatch', 'OUTPUT_QC_FAILURE')
    counted = json.loads(subprocess.check_output([
        os.environ.get('FFPROBE', 'ffprobe'), '-v', 'error', '-select_streams', 'v:0', '-count_frames',
        '-show_entries', 'stream=nb_read_frames', '-of', 'json', str(output)], text=True))
    frames = int(counted['streams'][0]['nb_read_frames'])
    require(frames == 901, f'decoded frames: {frames}', 'OUTPUT_QC_FAILURE')
    duration = float(metadata['format']['duration'])
    require(abs(float(v['duration']) - 901 / 30) < 0.002 and abs(duration - 901 / 30) < 0.06,
            f'duration mismatch: {duration}', 'OUTPUT_QC_FAILURE')
    require(a['codec_name'] == 'aac' and int(a['sample_rate']) > 0 and a['channels'] > 0,
            'audio metadata mismatch', 'OUTPUT_QC_FAILURE')
    require(abs(float(a.get('start_time', 0))) < 0.05 and abs(float(a['duration']) - 901 / 30) < 0.06,
            'audio coverage mismatch', 'OUTPUT_QC_FAILURE')
    decoded = subprocess.run(['ffmpeg', '-v', 'error', '-xerror', '-i', str(output),
                              '-map', '0:v:0', '-map', '0:a:0', '-f', 'null', '-'],
                             capture_output=True, text=True)
    require(decoded.returncode == 0 and not decoded.stderr.strip(),
            f'full decode failed: {decoded.stderr}', 'OUTPUT_QC_FAILURE')
    # Verify faststart without rewriting the rendered file.
    boxes = []
    with output.open('rb') as stream:
        while stream.tell() < output.stat().st_size:
            header = stream.read(8)
            require(len(header) == 8, 'truncated MP4 box', 'OUTPUT_QC_FAILURE')
            size, kind = int.from_bytes(header[:4], 'big'), header[4:].decode('ascii')
            header_size = 8
            if size == 1:
                size = int.from_bytes(stream.read(8), 'big')
                header_size = 16
            if size == 0:
                size = output.stat().st_size - stream.tell() + header_size
            require(size >= header_size, 'invalid MP4 box', 'OUTPUT_QC_FAILURE')
            boxes.append(kind)
            stream.seek(size - header_size, 1)
    require('moov' in boxes and 'mdat' in boxes and boxes.index('moov') < boxes.index('mdat'),
            'faststart missing', 'OUTPUT_QC_FAILURE')
    sha = hashlib.sha256(output.read_bytes()).hexdigest()
    values = {
        'SOURCE_COMMIT': manifest['source_commit'], 'CANONICAL_BASELINE': manifest['canonical_baseline'],
        'BRANCH': manifest['branch'], 'COMPOSITION_ID': manifest['composition_id'],
        'CANONICAL_AUDIO_SHA_EXPECTED': manifest['audio']['expected_sha256'],
        'CANONICAL_AUDIO_SHA_ACTUAL': manifest['audio']['sha256'], 'CANONICAL_AUDIO_SHA_MATCH': 'YES',
        'STORY_SHOT_COUNT': len(manifest['shots']), 'OUTPUT_FILENAME': output.name,
        'OUTPUT_BYTE_SIZE': output.stat().st_size, 'OUTPUT_SHA256': sha,
        'VIDEO_CODEC': v['codec_name'], 'PIX_FMT': v['pix_fmt'], 'WIDTH': v['width'], 'HEIGHT': v['height'],
        'FPS': 30, 'FRAME_COUNT': frames, 'DURATION': duration, 'VIDEO_DURATION': v['duration'],
        'AUDIO_CODEC': a['codec_name'], 'AUDIO_SAMPLE_RATE': a['sample_rate'], 'AUDIO_CHANNELS': a['channels'],
        'DECODE_TEST': 'PASS', 'FASTSTART': 'YES', 'STATUS': 'TECHNICAL_RENDER_PASS',
        'READY_FOR_PRODUCT_OWNER_ARTISTIC_REVIEW': 'YES',
    }
    lines = [f'{k} = {val}' for k, val in values.items()]
    for s in manifest['shots']:
        lines.append(f"SHOT {s['shot_id']} SHA256={s['sha256']} byte_size={s['byte_size']} "
                     f"dimensions={s['dimensions']['width']}x{s['dimensions']['height']} "
                     f"frames={s['start_frame']}–{s['start_frame'] + s['duration_frames'] - 1}")
    report = '\n'.join(lines) + '\n'
    (OUT / 'technical_qc.txt').write_text(report)
    print(report)
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as summary:
            summary.write('```text\n' + report + '```\n')


if __name__ == '__main__':
    try:
        qc()
    except (RuntimeError, OSError, ValueError, KeyError, subprocess.CalledProcessError) as exc:
        print(f'OUTPUT_QC_FAILURE: {exc}', file=sys.stderr)
        sys.exit(1)
