import React from 'react';
import { Composition } from 'remotion';
import { Film } from './Film';
import { SCENARIUSZ, dlugoscWKlatkach } from './scenariusz';
import type { FilmProps } from './typy';

export const RemotionRoot: React.FC = () => (
  <>
    <Composition
      id="Film"
      component={Film}
      durationInFrames={dlugoscWKlatkach()}
      fps={SCENARIUSZ.fps}
      width={SCENARIUSZ.szerokosc}
      height={SCENARIUSZ.wysokosc}
      defaultProps={
        {
          // wgraj narrację do public/ i wpisz tu nazwę pliku, np. „narracja.mp3"
          glos: '',
          znakDanePrzykladowe: true,
        } satisfies FilmProps
      }
    />
  </>
);
