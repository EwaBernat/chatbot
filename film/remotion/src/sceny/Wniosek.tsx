import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate} from 'remotion';
import {MARKA, FONT} from '../marka';

/** Jedno zdanie na zamknięcie — duże, wyśrodkowane, z pomarańczowym akcentem. */
export const Wniosek: React.FC<{tekst: string}> = ({tekst}) => {
  const klatka = useCurrentFrame();
  const {fps} = useVideoConfig();
  const w = spring({frame: klatka, fps, config: {damping: 200}});
  return (
    <AbsoluteFill style={{justifyContent: 'center', alignItems: 'center', padding: '0 220px 200px', fontFamily: FONT}}>
      <div style={{width: 110, height: 8, borderRadius: 4, background: MARKA.wyroznienie, marginBottom: 44, opacity: w}} />
      <div
        style={{
          fontSize: 60,
          lineHeight: 1.25,
          fontWeight: 700,
          color: MARKA.tekst,
          textAlign: 'center',
          opacity: w,
          transform: `translateY(${interpolate(w, [0, 1], [24, 0])}px)`,
        }}
      >
        {tekst}
      </div>
    </AbsoluteFill>
  );
};
