import React from 'react';
import {useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from '../marka';
import {wejscie, postep} from '../anim';
import type {Scena} from '../typy';

type S = Extract<Scena, {typ: 'tytul'}>;

export const Tytul: React.FC<{scena: S}> = ({scena}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const linia = postep(frame, fps, 0.5, 0.9);

  return (
    <div
      style={{
        flex: 1,
        height: '100%',
        background: MARKA.tlo,
        fontFamily: FONT,
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        padding: '54px 66px 190px 66px',
      }}
    >
      <div
        style={{
          display: 'inline-flex',
          alignSelf: 'flex-start',
          alignItems: 'center',
          gap: 12,
          padding: '10px 20px',
          borderRadius: 999,
          background: MARKA.tloTrzecie,
          color: MARKA.akcent,
          fontSize: 22,
          fontWeight: 700,
          letterSpacing: 2.2,
          textTransform: 'uppercase',
          ...wejscie(frame, fps, 0, 14),
        }}
      >
        EduPlaner 2026 · PCTP Koszalin
      </div>

      <h1
        style={{
          margin: '30px 0 0 0',
          color: MARKA.tekst,
          fontSize: 116,
          lineHeight: 0.98,
          letterSpacing: -3.6,
          fontWeight: 800,
          whiteSpace: 'pre-line',
          ...wejscie(frame, fps, 0.14, 26),
        }}
      >
        {scena.naglowek}
      </h1>

      <div
        style={{
          height: 6,
          width: `${linia * 100}%`,
          maxWidth: 380,
          background: MARKA.wyroznienie,
          borderRadius: 3,
          margin: '30px 0 26px 0',
        }}
      />

      <p
        style={{
          margin: 0,
          color: MARKA.tekstDrugi,
          fontSize: 36,
          lineHeight: 1.34,
          maxWidth: 900,
          ...wejscie(frame, fps, 0.3, 18),
        }}
      >
        {scena.podtytul}
      </p>

      <div style={{display: 'flex', gap: 14, marginTop: 44, flexWrap: 'wrap'}}>
        {scena.odznaki.map((o, i) => (
          <div
            key={o}
            style={{
              padding: '14px 26px',
              borderRadius: 14,
              background: MARKA.bialy,
              border: `2px solid ${MARKA.siatka}`,
              color: MARKA.tekst,
              fontSize: 27,
              fontWeight: 700,
              ...wejscie(frame, fps, 0.5 + i * 0.12, 16),
            }}
          >
            {o}
          </div>
        ))}
      </div>

      <div
        style={{
          marginTop: 46,
          color: MARKA.tekstCichy,
          fontSize: 24,
          letterSpacing: 0.4,
          ...wejscie(frame, fps, 0.95, 12),
        }}
      >
        {scena.autor}
      </div>
    </div>
  );
};
