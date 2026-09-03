import React from 'react';
import {Composition, staticFile} from 'remotion';
import {getAudioDurationInSeconds} from '@remotion/media-utils';
import {Film, type Props} from './Film';
import {parsujSrt, type Napis} from './srt';
import type {Film as FilmT} from './typy';

import M1 from '../public/M1.json';
import M2 from '../public/M2.json';
import M3 from '../public/M3.json';
import M4 from '../public/M4.json';
import M5 from '../public/M5.json';
import M6 from '../public/M6.json';

const FPS = 30;
const MODULY = [M1, M2, M3, M4, M5, M6] as unknown as FilmT[];

/**
 * Sześć kompozycji — po jednej na moduł. Długość każdej wynika z długości
 * nagrania; poprawiona narracja i nowy MP3 same zmieniają długość filmu.
 */
export const RemotionRoot: React.FC = () => (
  <>
    {MODULY.map((film) => (
      <Composition
        key={film.id}
        id={film.id}
        component={Film}
        durationInFrames={60 * FPS}
        fps={FPS}
        width={1920}
        height={1080}
        defaultProps={{film, napisy: [] as Napis[]} as Props}
        calculateMetadata={async ({props}) => {
          const dane = props.film;
          let napisy: Napis[] = [];
          if (dane.napisy) {
            try {
              napisy = parsujSrt(await (await fetch(staticFile(dane.napisy))).text());
            } catch {
              napisy = [];
            }
          }
          const koniecScen = Math.max(1, ...dane.sceny.map((s) => s.doSek));
          let sekundy = koniecScen;
          if (dane.audio) {
            try {
              sekundy = Math.max(koniecScen, await getAudioDurationInSeconds(staticFile(dane.audio)));
            } catch {
              // bez pliku audio zostaje długość wynikająca ze scen
            }
          }
          return {durationInFrames: Math.max(1, Math.round(sekundy * FPS)), props: {...props, napisy}};
        }}
      />
    ))}
  </>
);
