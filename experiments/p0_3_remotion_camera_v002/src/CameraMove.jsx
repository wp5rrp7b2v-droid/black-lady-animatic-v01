import React from 'react';
import {
  AbsoluteFill,
  Easing,
  Img,
  interpolate,
  staticFile,
  useCurrentFrame,
} from 'remotion';

const clamp = {
  extrapolateLeft: 'clamp',
  extrapolateRight: 'clamp',
};

const ease = Easing.bezier(0.22, 0.0, 0.28, 1.0);

const shotForFrame = (frame) => {
  if (frame < 24) {
    return {
      key: 'A01',
      src: staticFile('A01.png'),
      start: 0,
      end: 23,
      scale: [1.0, 1.42],
      x: [0, -6],
      y: [0, 18],
      origin: '65% 51%',
    };
  }

  if (frame < 47) {
    return {
      key: 'WIDE',
      src: staticFile('WIDE.png'),
      start: 24,
      end: 46,
      scale: [1.01, 1.18],
      x: [0, -8],
      y: [4, -2],
      origin: '60% 57%',
    };
  }

  if (frame < 68) {
    return {
      key: 'TIGHT',
      src: staticFile('TIGHT.png'),
      start: 47,
      end: 67,
      scale: [1.0, 1.17],
      x: [-2, -10],
      y: [2, -10],
      origin: '61% 47%',
    };
  }

  return {
    key: 'A02',
    src: staticFile('A02.png'),
    start: 68,
    end: 97,
    scale: [1.0, 1.065],
    x: [0, -5],
    y: [0, -7],
    origin: '53% 33%',
  };
};

const cutBlur = (frame) => {
  const cuts = [24, 47, 68];
  let blur = 0;

  for (const cut of cuts) {
    const d = Math.abs(frame - cut);
    if (d <= 1) blur = Math.max(blur, 2.8 - d * 1.4);
  }

  return blur;
};

export const CameraMove = () => {
  const frame = useCurrentFrame();
  const shot = shotForFrame(frame);

  const globalProgress = interpolate(frame, [0, 97], [0, 1], clamp);
  const cameraClock = ease(globalProgress);

  const shotStartClock = ease(shot.start / 97);
  const shotEndClock = ease(shot.end / 97);

  const scale = interpolate(
    cameraClock,
    [shotStartClock, shotEndClock],
    shot.scale,
    clamp,
  );
  const x = interpolate(
    cameraClock,
    [shotStartClock, shotEndClock],
    shot.x,
    clamp,
  );
  const y = interpolate(
    cameraClock,
    [shotStartClock, shotEndClock],
    shot.y,
    clamp,
  );

  const blur = cutBlur(frame);

  return (
    <AbsoluteFill style={{backgroundColor: 'black', overflow: 'hidden'}}>
      <Img
        src={shot.src}
        style={{
          width: '100%',
          height: '100%',
          objectFit: 'cover',
          transformOrigin: shot.origin,
          transform: `translate3d(${x}px, ${y}px, 0) scale(${scale})`,
          filter: blur > 0 ? `blur(${blur}px)` : 'none',
          willChange: 'transform, filter',
        }}
      />
    </AbsoluteFill>
  );
};
