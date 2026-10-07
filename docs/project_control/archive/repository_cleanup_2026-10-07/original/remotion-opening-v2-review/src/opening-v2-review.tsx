import {AbsoluteFill, Audio, Img, Sequence, interpolate, staticFile, useCurrentFrame} from 'remotion';
import timeline from './timeline.json';

type Shot = (typeof timeline.shots)[number];

const Still = ({shot}: {shot: Shot}) => {
  const frame = useCurrentFrame();
  const end = Math.max(1, shot.duration_frames - 1);
  const scale = interpolate(frame, [0, end], shot.scale, {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  return (
    <AbsoluteFill style={{overflow: 'hidden', backgroundColor: 'black'}}>
      <Img
        src={staticFile(`inputs/${shot.shot_id}.png`)}
        style={{
          width: '100%',
          height: '100%',
          objectFit: 'cover',
          objectPosition: shot.anchor,
          transformOrigin: shot.anchor,
          transform: `scale(${scale})`,
        }}
      />
    </AbsoluteFill>
  );
};

export const OpeningV2Review = () => (
  <AbsoluteFill style={{backgroundColor: 'black'}}>
    <Audio src={staticFile('inputs/opening_audio.m4a')} />
    {timeline.shots.map((shot) => (
      <Sequence key={shot.shot_id} from={shot.start_frame} durationInFrames={shot.duration_frames}>
        <Still shot={shot} />
      </Sequence>
    ))}
  </AbsoluteFill>
);
