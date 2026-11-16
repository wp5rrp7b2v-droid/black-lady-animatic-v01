import {Composition} from 'remotion';
import {OpeningProof} from './opening-proof';
import timeline from './timeline.json';

export const Root = () => (
  <Composition
    id={timeline.composition_id}
    component={OpeningProof}
    width={1080}
    height={1920}
    fps={30}
    durationInFrames={901}
  />
);
