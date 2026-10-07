import {Composition} from 'remotion';
import {OpeningV2ReviewV003} from './opening-v2-review-v003';
import timeline from './timeline.json';

export const Root = () => (
  <Composition
    id={timeline.composition_id}
    component={OpeningV2ReviewV003}
    width={timeline.width}
    height={timeline.height}
    fps={timeline.fps}
    durationInFrames={timeline.duration_frames}
  />
);
