import React from 'react';
import {Composition} from 'remotion';
import {Film} from './Film';
import czesc1 from './dane/czesc1.json';
import czesc2 from './dane/czesc2.json';
import rada45 from './dane/rada45.json';
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
          audioIntro: 'audio/czesc1/intro.wav',
          logo: 'logo/pctp-logo.png',
          fotoTytulowe: 'media/07-zabawa.jpg',
          awatar: 'awatar/warsztaty.png',
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
          logo: 'logo/pctp-logo.png',
          awatar: 'awatar/warsztaty.png',
        }}
      />
      <Composition
        id="Rada45"
        component={Film}
        durationInFrames={czas.rada45.suma + INTRO + OUTRO}
        fps={FPS}
        width={1920}
        height={1080}
        defaultProps={{
          slajdy: rada45,
          odcinki: czas.rada45.odcinki,
          czesc: 'Rada pedagogiczna · 45 minut',
          podtytul: 'Teoria umysłu w 45 minut',
          intro: INTRO,
          outro: OUTRO,
          logo: 'logo/pctp-logo.png',
          awatar: 'awatar/warsztaty.png',
        }}
      />
    </>
  );
};
