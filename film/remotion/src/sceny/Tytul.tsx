import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate} from 'remotion';
import {MARKA, FONT} from '../marka';

export const Tytul: React.FC<{tytul: string; podtytul?: string; nadtytul?: string}> = ({tytul, podtytul, nadtytul}) => {
  const klatka = useCurrentFrame();
  const {fps} = useVideoConfig();

  const wejscie = spring({frame: klatka, fps, config: {damping: 200}});
  const przesuniecie = interpolate(wejscie, [0, 1], [28, 0]);

  return (
    <AbsoluteFill
      style={{
        justifyContent: 'center',
        padding: '0 140px 210px',
        fontFamily: FONT,
        opacity: wejscie,
        transform: `translateY(${przesuniecie}px)`,
      }}
    >
      <div
        style={{
          width: 84,
          height: 6,
          borderRadius: 3,
          background: MARKA.wyroznienie,
          marginBottom: 36,
        }}
      />
      {nadtytul ? (
        <div style={{fontSize: 24, letterSpacing: 5, fontWeight: 700, color: MARKA.wyroznienie, marginBottom: 18}}>
          {nadtytul}
        </div>
      ) : null}
      <div style={{fontSize: 82, fontWeight: 700, color: MARKA.tekst, lineHeight: 1.1}}>
        {tytul}
      </div>
      {podtytul ? (
        <div style={{fontSize: 36, color: MARKA.tekstDrugi, marginTop: 24, lineHeight: 1.35}}>
          {podtytul}
        </div>
      ) : null}
    </AbsoluteFill>
  );
};
