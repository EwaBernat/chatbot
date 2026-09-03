import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate} from 'remotion';
import {MARKA, FONT} from '../marka';

/** Jedna wielka liczba z opisem — dla terminów: 14 dni, 30 dni, 2 razy w roku. */
export const Liczba: React.FC<{wartosc: string; opis: string; kontekst?: string}> = ({wartosc, opis, kontekst}) => {
  const klatka = useCurrentFrame();
  const {fps} = useVideoConfig();
  const w = spring({frame: klatka, fps, config: {damping: 14, stiffness: 110}});
  const o = spring({frame: klatka - 12, fps, config: {damping: 200}});
  return (
    <AbsoluteFill style={{justifyContent: 'center', alignItems: 'center', padding: '0 200px 200px', fontFamily: FONT}}>
      <div style={{fontSize: 260, fontWeight: 800, color: MARKA.tekst, lineHeight: 1, letterSpacing: -6, transform: `scale(${interpolate(w, [0, 1], [0.7, 1])})`, opacity: w}}>
        {wartosc}
      </div>
      <div style={{fontSize: 48, fontWeight: 700, color: MARKA.wyroznienie, marginTop: 26, opacity: o, textAlign: 'center'}}>{opis}</div>
      {kontekst ? <div style={{fontSize: 30, color: MARKA.tekstDrugi, marginTop: 16, opacity: o, textAlign: 'center', maxWidth: 1300, lineHeight: 1.4}}>{kontekst}</div> : null}
    </AbsoluteFill>
  );
};
