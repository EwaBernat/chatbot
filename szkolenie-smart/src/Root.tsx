import React from 'react';
import {Composition} from 'remotion';
import {Szkolenie} from './Szkolenie';
import scenariusz from './scenariusz.json';
import type {Scenariusz} from './typy';

const DANE = scenariusz as Scenariusz;

/**
 * Długość filmu bierze się z sumy scen, a te z długości narracji.
 * Poprawiona narracja sama zmienia długość filmu — nic nie trzeba przestawiać ręcznie.
 */
const KLATKI = Math.max(
  1,
  DANE.sceny.reduce((suma, s) => suma + Math.round(s.sekundy * DANE.fps), 0)
);

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="Szkolenie"
      component={Szkolenie}
      durationInFrames={KLATKI}
      fps={DANE.fps}
      width={1920}
      height={1080}
      defaultProps={{scenariusz: DANE}}
    />
  );
};
