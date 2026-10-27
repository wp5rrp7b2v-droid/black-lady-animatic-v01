import {AbsoluteFill, Audio, Img, Sequence, interpolate, staticFile, useCurrentFrame} from 'remotion';
import timeline from './timeline.json';

type Shot = (typeof timeline.shots)[number];

const Still = ({shot}: {shot: Shot}) => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{overflow: 'hidden'}}>
      <Img
        src={staticFile(`inputs/${shot.shot_id}.png`)}
        style={{
          width: '100%', height: '100%', objectFit: 'cover',
          objectPosition: shot.anchor,
          transformOrigin: shot.anchor,
          scale: interpolate(frame, [0, shot.duration_frames - 1], shot.scale, {
            extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
          }),
        }}
      />
    </AbsoluteFill>
  );
};

export const OpeningProof = () => (
  <AbsoluteFill style={{backgroundColor: 'black'}}>
    <Audio src={staticFile('inputs/opening_audio.m4a')} />
    {timeline.shots.map((shot) => (
      <Sequence key={shot.shot_id} from={shot.start_frame} durationInFrames={shot.duration_frames}>
        <Still shot={shot} />
      </Sequence>
    ))}
  </AbsoluteFill>
);
