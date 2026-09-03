import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate} from 'remotion';
import {MARKA, FONT} from '../marka';

/**
 * Dwie kolumny „było / jest”. Lewa odsłania się pierwsza i zostaje przygaszona,
 * prawa wjeżdża dopiero po niej i dostaje pomarańczową krawędź — oko ma
 * wylądować na stanie obecnym, nie na historii.
 */
export const Porownanie: React.FC<{
  tytul: string;
  naglowki?: [string, string];
  bylo: string[];
  jest: string[];
}> = ({tytul, naglowki = ['BYŁO · do 31.08.2026', 'JEST · od 1.09.2026'], bylo, jest}) => {
  const klatka = useCurrentFrame();
  const {fps} = useVideoConfig();
  const naglowek = spring({frame: klatka, fps, config: {damping: 200}});
  const startPrawej = 14 + bylo.length * 9 + 6;

  const kolumna = (
    punkty: string[],
    start: number,
    akcent: boolean,
  ) => (
    <div
      style={{
        flex: 1,
        background: akcent ? '#FFFFFF' : MARKA.tloDrugie,
        borderRadius: 16,
        padding: '34px 40px',
        borderLeft: akcent ? `10px solid ${MARKA.wyroznienie}` : `10px solid ${MARKA.siatka}`,
        boxShadow: akcent ? '0 14px 44px rgba(45,27,105,0.10)' : 'none',
        opacity: spring({frame: klatka - start + 6, fps, config: {damping: 200}}),
      }}
    >
      <div
        style={{
          fontSize: 22,
          letterSpacing: 3,
          fontWeight: 700,
          color: akcent ? MARKA.wyroznienie : MARKA.tekstCichy,
          marginBottom: 22,
        }}
      >
        {akcent ? naglowki[1] : naglowki[0]}
      </div>
      {punkty.map((p, i) => {
        const w = spring({frame: klatka - start - i * 9, fps, config: {damping: 200}});
        return (
          <div
            key={i}
            style={{
              display: 'flex',
              gap: 18,
              alignItems: 'flex-start',
              marginBottom: 18,
              opacity: w,
              transform: `translateX(${interpolate(w, [0, 1], [akcent ? 18 : -18, 0])}px)`,
            }}
          >
            <div
              style={{
                width: 12,
                height: 12,
                marginTop: 14,
                borderRadius: 3,
                flexShrink: 0,
                background: akcent ? MARKA.wyroznienie : MARKA.tekstCichy,
              }}
            />
            <div
              style={{
                fontSize: 30,
                lineHeight: 1.35,
                color: akcent ? MARKA.tekst : MARKA.tekstDrugi,
                fontWeight: akcent ? 600 : 400,
              }}
            >
              {p}
            </div>
          </div>
        );
      })}
    </div>
  );

  return (
    <AbsoluteFill style={{padding: '80px 120px 220px', fontFamily: FONT}}>
      <div
        style={{
          fontSize: 50,
          fontWeight: 700,
          color: MARKA.tekst,
          marginBottom: 40,
          opacity: naglowek,
        }}
      >
        {tytul}
      </div>
      <div style={{display: 'flex', gap: 40, alignItems: 'stretch'}}>
        {kolumna(bylo, 14, false)}
        {kolumna(jest, startPrawej, true)}
      </div>
    </AbsoluteFill>
  );
};
