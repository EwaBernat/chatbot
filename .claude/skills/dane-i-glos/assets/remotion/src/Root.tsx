import React from 'react';
import {Composition, staticFile} from 'remotion';
import {getAudioDurationInSeconds, getVideoMetadata} from '@remotion/media-utils';
import {RaportWideo, type Props} from './RaportWideo';
import {parsujSrt, type Napis} from './srt';
import film from '../public/film.json';
import type {Film} from './typy';

const FPS = 30;

/**
 * Czas trwania filmu bierze się z długości nagrania, a nie z ręcznie wpisanej
 * liczby — dzięki temu poprawienie narracji i przegenerowanie MP3 samo zmienia
 * długość filmu, bez dotykania kodu.
 */
export const RemotionRoot: React.FC = () => (
  <Composition
    id="RaportWideo"
    component={RaportWideo}
    durationInFrames={30 * FPS}
    fps={FPS}
    width={1920}
    height={1080}
    defaultProps={{film: film as Film, napisy: [] as Napis[]}}
    calculateMetadata={async ({props}) => {
      const dane = props.film;

      let napisy: Napis[] = [];
      if (dane.napisy) {
        try {
          napisy = parsujSrt(await (await fetch(staticFile(dane.napisy))).text());
        } catch {
          // Brak pliku z napisami nie może wywrócić renderu — film powstaje bez nich.
          napisy = [];
        }
      }

      const koniecScen = Math.max(0, ...dane.sceny.map((s) => s.doSek));
      let sekundy = koniecScen;
      if (dane.audio) {
        try {
          sekundy = Math.max(koniecScen, await getAudioDurationInSeconds(staticFile(dane.audio)));
        } catch {
          // zostaje długość wynikająca ze scen
        }
      }

      // Ewa (awatar) też wydłuża film: do końca swojego klipu albo do doSek.
      const awatary = Array.isArray(dane.awatar) ? dane.awatar : dane.awatar ? [dane.awatar] : [];
      for (const a of awatary) {
        let koniec = a.doSek;
        if (koniec == null) {
          try {
            koniec = (a.odSek ?? 0) + (await getVideoMetadata(staticFile(a.plik))).durationInSeconds;
          } catch {
            koniec = a.odSek ?? 0;
          }
        }
        sekundy = Math.max(sekundy, koniec);
      }

      return {
        durationInFrames: Math.max(1, Math.round(sekundy * FPS)),
        props: {...props, napisy},
      };
    }}
  />
);
