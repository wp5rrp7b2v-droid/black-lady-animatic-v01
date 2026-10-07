import {AbsoluteFill, Audio, Easing, Img, interpolate, staticFile, useCurrentFrame} from 'remotion';
import timeline from './timeline.json';

type Shot = (typeof timeline.shots)[number];

const clamp01 = (v: number) => Math.min(1, Math.max(0, v));
const ease = (v: number) => Easing.inOut(Easing.ease)(clamp01(v));

const transitionProgress = (frame: number, cut: number, frames: number) => {
  if (frames <= 0) return frame >= cut ? 1 : 0;
  const left = Math.floor(frames / 2);
  const right = Math.ceil(frames / 2);
  const start = cut - left;
  const end = cut + right;
  return ease((frame - start) / Math.max(1, end - start));
};

const shakePattern = [0, 1, -0.92, 0.78, -0.62, 0.48, -0.34, 0.22, -0.12, 0];

const ShotLayer = ({shot, index}: {shot: Shot; index: number}) => {
  const frame = useCurrentFrame();
  const next = index < timeline.shots.length - 1 ? timeline.shots[index + 1] : null;

  const progress = ease((frame - shot.start_frame) / Math.max(1, shot.duration_frames - 1));
  const scale = interpolate(progress, [0, 1], shot.scale, {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });
  const driftX = interpolate(progress, [0, 1], shot.drift_x_px, {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });
  const driftY = interpolate(progress, [0, 1], shot.drift_y_px, {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });

  let inOpacity = 1;
  let inBlur = 0;
  if (shot.transition_in.type === 'fade_black') {
    inOpacity = ease((frame - shot.start_frame) / Math.max(1, shot.transition_in.frames));
  } else if (shot.transition_in.type === 'hard') {
    inOpacity = frame >= shot.start_frame ? 1 : 0;
  } else {
    const p = transitionProgress(frame, shot.start_frame, shot.transition_in.frames);
    inOpacity = p;
    if (shot.transition_in.type === 'blur_dissolve') inBlur = (1 - p) * 5.5;
  }

  let outOpacity = 1;
  let outBlur = 0;
  if (next) {
    if (next.transition_in.type === 'hard') {
      outOpacity = frame < next.start_frame ? 1 : 0;
    } else {
      const p = transitionProgress(frame, next.start_frame, next.transition_in.frames);
      outOpacity = 1 - p;
      if (next.transition_in.type === 'blur_dissolve') outBlur = p * 5.5;
    }
  } else {
    const fadeStart = shot.start_frame + shot.duration_frames - timeline.final_fade_out_frames;
    outOpacity = 1 - ease((frame - fadeStart) / Math.max(1, timeline.final_fade_out_frames));
  }

  let shakeX = 0;
  let shakeY = 0;
  let shakeBlur = 0;
  if ('shake' in shot && shot.shake) {
    const local = frame - shot.start_frame - shot.shake.start_offset_frame;
    if (local >= 0 && local < shot.shake.duration_frames) {
      const idx = Math.min(shakePattern.length - 1, local);
      const value = shakePattern[idx] ?? 0;
      shakeX = value * shot.shake.amplitude_px;
      shakeY = -value * shot.shake.amplitude_px * 0.42;
      shakeBlur = Math.abs(value) * 1.5;
    }
  }

  const opacity = clamp01(Math.min(inOpacity, outOpacity));
  const blur = Math.max(inBlur, outBlur, shakeBlur);

  return (
    <AbsoluteFill style={{opacity, overflow: 'hidden'}}>
      <Img
        src={staticFile(`inputs/${shot.shot_id}.png`)}
        style={{
          width: '100%',
          height: '100%',
          objectFit: 'cover',
          objectPosition: shot.anchor,
          transformOrigin: shot.anchor,
          transform: `translate3d(${driftX + shakeX}px, ${driftY + shakeY}px, 0) scale(${scale})`,
          filter: `blur(${blur}px)`,
          willChange: 'transform, opacity, filter',
        }}
      />
      {shot.vignette > 0 ? (
        <AbsoluteFill
          style={{
            background: `radial-gradient(circle at 50% 46%, rgba(0,0,0,0) 42%, rgba(0,0,0,${shot.vignette * 0.45}) 72%, rgba(0,0,0,${shot.vignette}) 100%)`,
            pointerEvents: 'none',
          }}
        />
      ) : null}
    </AbsoluteFill>
  );
};

export const OpeningV2ReviewV003 = () => (
  <AbsoluteFill style={{backgroundColor: 'black'}}>
    <Audio src={staticFile('inputs/opening_audio.m4a')} />
    {timeline.shots.map((shot, index) => (
      <ShotLayer key={shot.shot_id} shot={shot} index={index} />
    ))}
  </AbsoluteFill>
);
