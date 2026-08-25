import React from 'react';
import {Composition} from 'remotion';
import {Film} from './Film';
import czesc1 from './dane/czesc1.json';
import czesc2 from './dane/czesc2.json';
import czas from './czas.json';

const FPS = 30;
const INTRO = 4 * FPS;
const OUTRO = 5 * FPS;

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="CzescI"
        component={Film}
        durationInFrames={czas.czesc1.suma + INTRO + OUTRO}
        fps={FPS}
        width={1920}
        height={1080}
        defaultProps={{
          slajdy: czesc1,
          odcinki: czas.czesc1.odcinki,
          czesc: 'Część I · przedszkole',
          podtytul: 'Teoria umysłu w przedszkolu',
          intro: INTRO,
          outro: OUTRO,
        }}
      />
      <Composition
        id="CzescII"
        component={Film}
        durationInFrames={czas.czesc2.suma + INTRO + OUTRO}
        fps={FPS}
        width={1920}
        height={1080}
        defaultProps={{
          slajdy: czesc2,
          odcinki: czas.czesc2.odcinki,
          czesc: 'Część II · klasy 1–3',
          podtytul: 'Mosty społeczne w klasach 1–3',
          intro: INTRO,
          outro: OUTRO,
        }}
      />
    </>
  );
};
