import {Composition} from 'remotion';
import {OpeningV2Review} from './opening-v2-review';
import timeline from './timeline.json';

export const Root = () => (
  <Composition
    id={timeline.composition_id}
    component={OpeningV2Review}
    width={1080}
    height={1920}
    fps={timeline.fps}
    durationInFrames={timeline.duration_frames}
  />
);
