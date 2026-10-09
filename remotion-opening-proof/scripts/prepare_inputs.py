"""Fail-closed canonical input verification; copies bytes only after validation."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import struct
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
REPO = PROJECT.parent
AUDIO_PATH = 'staging/p0_3_a01_a02_transition_validation/AUDIO_MVP1_CANONICAL_V001.m4a'
AUDIO_SHA = '8d0d12d3af5e2c15032912605c0d1b3f3e892fe24918a7064864b136987737a0'
OUTPUT_NAME = 'P03_OPENING_AUDIO_COMIC_PROOF_V001'
OUT = PROJECT / 'out' / OUTPUT_NAME


def require(condition, message, category='INPUT_IDENTITY_FAILURE'):
    if not condition:
        raise RuntimeError(f'{category}: {message}')


def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args], text=True).strip()


def identity(relative, category='INPUT_IDENTITY_FAILURE'):
    path = REPO / relative
    require(path.is_file() and not path.is_symlink(), f'not a regular file: {relative}', category)
    require(not any(p.is_symlink() for p in path.parents if p != REPO.parent),
            f'redirected path: {relative}', category)
    data = path.read_bytes()
    blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    require(blob == git('rev-parse', f'HEAD:{relative}'), f'Git blob mismatch: {relative}', category)
    return data, hashlib.sha256(data).hexdigest(), blob


def probe(path):
    return json.loads(subprocess.check_output([
        os.environ.get('FFPROBE', 'ffprobe'), '-v', 'error', '-show_streams',
        '-show_format', '-of', 'json', str(path)], text=True))


def local_audio_probe(path):
    # The recovery boundary permits native, read-only metadata inspection on Mac.
    # Formal runner validation always uses FFprobe, without this fallback.
    info = subprocess.check_output(['afinfo', str(path)], text=True)
    tracks = re.search(r'Num Tracks:\s+(\d+)', info)
    fmt = re.search(r'Data format:\s+(\d+) ch,\s+(\d+) Hz,\s+(\w+)', info)
    duration = re.search(r'estimated duration:\s+([\d.]+) sec', info)
    require(tracks and tracks[1] == '1' and fmt and duration, 'invalid afinfo metadata', 'AUDIO_SHA_FAILURE')
    return {'streams': [{'codec_type': 'audio', 'channels': int(fmt[1]),
                         'sample_rate': fmt[2], 'codec_name': fmt[3]}],
            'format': {'duration': duration[1]}}


def prepare(validate_only=False):
    timeline = json.loads((PROJECT / 'src/timeline.json').read_text())
    sequence = ['A01', 'A02', 'N02', 'N03', 'N04', 'N05', 'N01']
    locked_frames = [(0, 98), (98, 99), (197, 127), (324, 120), (444, 147), (591, 168), (759, 142)]
    require([s['shot_id'] for s in timeline['shots']] == sequence, 'shot order mismatch')
    require([(s['start_frame'], s['duration_frames']) for s in timeline['shots']] == locked_frames,
            'locked frame map mismatch')
    require(git('merge-base', timeline['source_baseline'], 'HEAD') == timeline['source_baseline'],
            'HEAD does not descend from canonical baseline')
    state_path = 'docs/project_control/core/project_state.json'
    index_path = 'production/story_shots/story_shot_index.jsonl'
    # Input/control authority must be identical to the locked baseline.
    for path in [state_path, index_path, 'production/story_shots/README.md',
                 'docs/project_control/gates/P0_3_video_pipeline/README.md']:
        require(git('rev-parse', f'HEAD:{path}') == git('rev-parse', f"{timeline['source_baseline']}:{path}"),
                f'canonical authority changed: {path}')
        identity(path)
    state = json.loads((REPO / state_path).read_text())
    require(state['state_revision'] == 'R085', 'Project Control must be R085')
    require(state['current_task'] == 'P0.3｜OPENING AUDIO-COMIC PROOF ASSEMBLY', 'current_task mismatch')
    require(state['blocker'] in [None, 'NONE'], 'Project Control blocked')
    controls = [v for v in state.values() if isinstance(v, dict) and 'opening_sequence' in v]
    require(len(controls) == 1 and controls[0]['opening_sequence'] == sequence,
            'Project Control opening sequence mismatch')
    require(controls[0]['registered_story_shot_count'] == 12, 'registered count mismatch')
    records = [json.loads(line) for line in (REPO / index_path).read_text().splitlines() if line.strip()]
    require(len(records) == 12 and len({r['shot_id'] for r in records}) == 12, 'index count or duplicates')
    require(all(r['approval_status'] == 'APPROVED' and r['lifecycle'] == 'CURRENT' for r in records),
            'approved/current registry count must be 12')
    registry = {r['shot_id']: r for r in records}
    shots = []
    copies = []
    for shot in timeline['shots']:
        sid, relative = shot['shot_id'], shot['canonical_path']
        record = registry[sid]
        require(record['canonical_path'] == relative, f'{sid}: index path mismatch')
        data, sha, blob = identity(relative)
        require(data[:8] == b'\x89PNG\r\n\x1a\n' and data[12:16] == b'IHDR', f'{sid}: invalid PNG')
        width, height = struct.unpack('>II', data[16:24])
        require((width, height) == (941, 1672), f'{sid}: dimensions mismatch')
        require(len(data) == record['byte_size'], f'{sid}: byte size mismatch')
        require(blob == record['github_blob_sha'], f'{sid}: registry Git blob mismatch')
        if 'dimensions' in record:
            require(record['dimensions'] == {'width': width, 'height': height}, f'{sid}: index dimensions mismatch')
        for expected in [shot['locked_sha256'], record.get('sha256_locked_identity')]:
            if expected:
                require(sha == expected, f'{sid}: SHA256 mismatch')
        start, duration = shot['start_frame'], shot['duration_frames']
        shots.append({**shot, 'sha256': sha, 'byte_size': len(data), 'git_blob_identity': blob,
                      'dimensions': {'width': width, 'height': height}, 'png_signature': 'VALID',
                      'start_time': start / 30, 'end_time': (start + duration) / 30,
                      'approval_status': 'APPROVED', 'lifecycle': 'CURRENT'})
        copies.append((relative, f'{sid}.png', sha))
    data, sha, blob = identity(AUDIO_PATH, 'AUDIO_SHA_FAILURE')
    require(sha == AUDIO_SHA, 'canonical audio SHA mismatch', 'AUDIO_SHA_FAILURE')
    native_local = validate_only and sys.platform == 'darwin' and not shutil.which(os.environ.get('FFPROBE', 'ffprobe'))
    metadata = local_audio_probe(REPO / AUDIO_PATH) if native_local else probe(REPO / AUDIO_PATH)
    streams = metadata['streams']
    require(len(streams) == 1 and streams[0]['codec_type'] == 'audio', 'source audio stream mismatch', 'AUDIO_SHA_FAILURE')
    audio = streams[0]
    duration = float(metadata['format']['duration'])
    require(abs(duration - 359.141995) < 0.01, f'audio duration mismatch: {duration}', 'AUDIO_SHA_FAILURE')
    require(audio['codec_name'] == 'aac' and int(audio['sample_rate']) > 0 and audio['channels'] > 0,
            'invalid audio metadata', 'AUDIO_SHA_FAILURE')
    manifest = {
        'source_commit': git('rev-parse', 'HEAD'), 'canonical_baseline': timeline['source_baseline'],
        'branch': os.environ.get('GITHUB_REF_NAME') or git('branch', '--show-current'),
        'composition_id': timeline['composition_id'], 'width': 1080, 'height': 1920,
        'fps': 30, 'duration_frames': 901, 'shots': shots,
        'audio': {'canonical_path': AUDIO_PATH, 'sha256': sha, 'expected_sha256': AUDIO_SHA,
                  'sha_match': 'YES', 'byte_size': len(data), 'git_blob_identity': blob,
                  'duration': duration, 'codec': audio['codec_name'], 'sample_rate': audio['sample_rate'],
                  'channels': audio['channels'], 'source_start': 0, 'source_end': 901 / 30},
        'overall_input_validation': 'PASS',
    }
    if not validate_only:
        runtime = PROJECT / 'public/inputs'
        runtime.mkdir(parents=True, exist_ok=True)
        copies.append((AUDIO_PATH, 'opening_audio.m4a', sha))
        for relative, name, expected in copies:
            dest = runtime / name
            require(not dest.is_symlink(), f'redirected destination: {dest}')
            shutil.copyfile(REPO / relative, dest)
            require(hashlib.sha256(dest.read_bytes()).hexdigest() == expected, f'copy mismatch: {name}')
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / 'opening_proof_input_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps(manifest, indent=2))
    return manifest


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--validate-only', action='store_true')
    args = parser.parse_args()
    try:
        prepare(args.validate_only)
    except (RuntimeError, OSError, ValueError, KeyError, subprocess.CalledProcessError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
