import React from 'react';
import {AbsoluteFill, Sequence, interpolate, staticFile} from 'remotion';
import {Audio, Video} from '@remotion/media';
const fullFrame = {width: '100%', height: '100%'};
export const Sh05AutoEdit: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: '#000'}}>
    {/* Remove B's startup; hold through its final reaction. */}
    <Sequence name="SH05B picture" durationInFrames={171}>
      <Video src={staticFile('SH05B_MICRO_MOTION_V002.mp4')} trimBefore={6} muted style={fullFrame} objectFit="cover"/>
    </Sequence>
    {/* Natural straight cut; no decorative visual transition. */}
    <Sequence name="SH05C picture" from={171} durationInFrames={130}>
      <Video src={staticFile('SH05C_VIDU_BASE_V001.mp4')} trimBefore={2} muted style={fullFrame} objectFit="cover"/>
    </Sequence>
    {/* Dialogue match plus a six-frame L-cut fade. */}
    <Sequence name="SH05B dialogue" durationInFrames={173}>
      <Audio src={staticFile('SH05B_MICRO_MOTION_V002.mp4')} trimBefore={6} volume={(frame) => 0.55 * interpolate(frame, [167, 173], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'})}/>
    </Sequence>
    {/* Response begins four frames early, with a restrained crossfade. */}
    <Sequence name="SH05C dialogue" from={167} durationInFrames={134}>
      <Audio src={staticFile('SH05C_VIDU_BASE_V001.mp4')} trimBefore={2} volume={(frame) => 0.75 * interpolate(frame, [0, 5], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'})}/>
    </Sequence>
    {/* Deterministic filtered room tone, kept subliminal. */}
    <Audio src={staticFile('castle-room-tone.wav')} volume={(frame) => interpolate(frame, [0, 18, 283, 300], [0, 0.13, 0.13, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'})}/>
  </AbsoluteFill>
);
