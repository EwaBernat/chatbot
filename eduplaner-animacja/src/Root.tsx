import React from 'react';
import {Composition, staticFile} from 'remotion';
import {getAudioDurationInSeconds} from '@remotion/media-utils';
import {EduPlanerPromo, type Props} from './EduPlanerPromo';
import film from '../public/film.json';
import type {Film} from './typy';

const FPS = 30;

/** Długość filmu bierze się z nagrania — poprawiona narracja sama zmienia długość. */
export const RemotionRoot: React.FC = () => (
  <Composition
    id="EduPlanerPromo"
    component={EduPlanerPromo}
    durationInFrames={60 * FPS}
    fps={FPS}
    width={1920}
    height={1080}
    defaultProps={{film: film as unknown as Film} satisfies Props}
    calculateMetadata={async ({props}) => {
      const dane = props.film;
      const koniecScen = Math.max(0, ...dane.sceny.map((s) => s.doSek));
      let sekundy = koniecScen;
      try {
        sekundy = Math.max(koniecScen, await getAudioDurationInSeconds(staticFile(dane.audio)));
      } catch {
        // brak nagrania nie wywraca renderu
      }
      return {durationInFrames: Math.max(1, Math.round(sekundy * FPS))};
    }}
  />
);
