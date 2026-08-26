import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate} from 'remotion';
import {MARKA, FONT} from '../marka';

export const Wniosek: React.FC<{tekst: string}> = ({tekst}) => {
  const klatka = useCurrentFrame();
  const {fps} = useVideoConfig();

  const wejscie = spring({frame: klatka, fps, config: {damping: 200}});
  const przesuniecie = interpolate(wejscie, [0, 1], [22, 0]);

  return (
    <AbsoluteFill
      style={{
        justifyContent: 'center',
        padding: '0 160px 210px',
        fontFamily: FONT,
        opacity: wejscie,
        transform: `translateY(${przesuniecie}px)`,
      }}
    >
      <div
        style={{
          borderLeft: `6px solid ${MARKA.wyroznienie}`,
          paddingLeft: 40,
          fontSize: 54,
          lineHeight: 1.32,
          fontWeight: 600,
          color: MARKA.tekst,
        }}
      >
        {tekst}
      </div>
    </AbsoluteFill>
  );
};
