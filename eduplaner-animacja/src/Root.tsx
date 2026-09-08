import React from 'react';
import {Composition, staticFile} from 'remotion';
import {getAudioDurationInSeconds} from '@remotion/media-utils';
import {EduPlanerPromo, type Props} from './EduPlanerPromo';
import film from '../public/film.json';
import kpof from '../public/kpof.json';
import {KpofPromo, type FilmKpof} from './kpof/KpofPromo';
import type {Film} from './typy';
import {PogPromo, type FilmPog} from './pog/PogPromo';
import pog from '../public/pog.json';
import {WopfPromo, type FilmWopf} from './wopf/WopfPromo';
import wopf from '../public/wopf.json';

const FPS = 30;

/** Długość filmu bierze się z nagrania — poprawiona narracja sama zmienia długość. */
export const RemotionRoot: React.FC = () => (
  <>
  <Composition
    id="KpofPromo"
    component={KpofPromo}
    durationInFrames={60 * FPS}
    fps={FPS}
    width={1920}
    height={1080}
    defaultProps={{film: kpof as unknown as FilmKpof}}
    calculateMetadata={async ({props}) => {
      let sekundy = props.film.dlugosc;
      try {
        sekundy = Math.max(sekundy, await getAudioDurationInSeconds(staticFile(props.film.audio)));
      } catch {
        // zostaje długość z pliku
      }
      return {durationInFrames: Math.max(1, Math.round(sekundy * FPS)), props: {film: {...props.film, dlugosc: sekundy}}};
    }}
  />
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
    <Composition
      id="PogPromo"
      component={PogPromo}
      durationInFrames={60 * FPS}
      fps={FPS}
      width={1920}
      height={1080}
      defaultProps={{film: pog as unknown as FilmPog}}
      calculateMetadata={async ({props}) => {
        let sekundy = props.film.dlugosc;
        try {
          sekundy = Math.max(sekundy, await getAudioDurationInSeconds(staticFile(props.film.audio)));
        } catch {
          // brak nagrania nie wywraca renderu
        }
        return {durationInFrames: Math.max(1, Math.round(sekundy * FPS))};
      }}
    />
    <Composition
      id="WopfPromo"
      component={WopfPromo}
      durationInFrames={60 * FPS}
      fps={FPS}
      width={1920}
      height={1080}
      defaultProps={{film: wopf as unknown as FilmWopf}}
      calculateMetadata={async ({props}) => {
        let sekundy = props.film.dlugosc;
        if (props.film.audio) {
          try {
            sekundy = Math.max(sekundy, await getAudioDurationInSeconds(staticFile(props.film.audio)));
          } catch {
            // bez nagrania długość bierze się z napisów
          }
        }
        return {durationInFrames: Math.max(1, Math.round(sekundy * FPS))};
      }}
    />
  </>
);
