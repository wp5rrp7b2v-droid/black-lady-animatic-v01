import React from 'react';
import {Composition, registerRoot} from 'remotion';
import {CameraMove} from './CameraMove';

const Root = () => (
  <Composition
    id="P03A01A02CameraMoveV002"
    component={CameraMove}
    durationInFrames={98}
    fps={30}
    width={1080}
    height={1920}
  />
);

registerRoot(Root);
