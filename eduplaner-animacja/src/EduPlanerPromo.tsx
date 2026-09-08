import React from 'react';
import {AbsoluteFill, Audio, Sequence, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA} from './marka';
import {Napisy} from './Napisy';
import {Intro} from './sceny/Intro';
import {EkranGlowny} from './sceny/EkranGlowny';
import {Druk1} from './sceny/Druk1';
import {Druk2} from './sceny/Druk2';
import {Druk3} from './sceny/Druk3';
import {Druk4} from './sceny/Druk4';
import {Final} from './sceny/Final';
import type {Film, Scena, Z} from './typy';

export type Props = {film: Film};

/** Miękkie wejście/wyjście sceny — bez nakładania sekwencji. */
const Przejscie: React.FC<{trwanie: number; children: React.ReactNode}> = ({trwanie, children}) => {
  const frame = useCurrentFrame();
  const wejscie = interpolate(frame, [0, 10], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const wyjscie = interpolate(frame, [trwanie - 9, trwanie - 1], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const o = Math.min(wejscie, wyjscie);
  return <AbsoluteFill style={{opacity: o, transform: `scale(${0.985 + 0.015 * o})`}}>{children}</AbsoluteFill>;
};

const PasekPostepu: React.FC = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  return (
    <div style={{position: 'absolute', left: 0, bottom: 0, height: 6, width: `${(100 * frame) / durationInFrames}%`, background: MARKA.pomarancz}} />
  );
};

const scenaKomponent = (s: Scena, trwanie: number, fps: number) => {
  const z: Z = Object.fromEntries(Object.entries(s.znaczniki).map(([k, v]) => [k, Math.max(0, Math.round((v - s.odSek) * fps))]));
  switch (s.id) {
    case 'intro':
      return <Intro z={z} />;
    case 'ekran':
      return <EkranGlowny z={z} />;
    case 'druk1':
      return <Druk1 trwanie={trwanie} z={z} />;
    case 'druk2':
      return <Druk2 trwanie={trwanie} z={z} />;
    case 'druk3':
      return <Druk3 trwanie={trwanie} z={z} />;
    case 'druk4':
      return <Druk4 trwanie={trwanie} z={z} />;
    case 'final':
      return <Final z={z} />;
    default:
      return null;
  }
};

export const EduPlanerPromo: React.FC<Props> = ({film}) => {
  const {fps} = useVideoConfig();
  const naKlatki = (sek: number) => Math.max(1, Math.round(sek * fps));
  return (
    <AbsoluteFill style={{background: MARKA.tlo}}>
      {film.audio ? <Audio src={staticFile(film.audio)} /> : null}
      {film.sceny.map((s) => {
        const od = naKlatki(s.odSek);
        const trwanie = Math.max(1, naKlatki(s.doSek) - od);
        return (
          <Sequence key={s.id} from={od} durationInFrames={trwanie} name={s.id}>
            <Przejscie trwanie={trwanie}>{scenaKomponent(s, trwanie, fps)}</Przejscie>
          </Sequence>
        );
      })}
      <Napisy napisy={film.napisy} />
      <PasekPostepu />
    </AbsoluteFill>
  );
};
