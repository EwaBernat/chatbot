import React from 'react';
import {useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from '../marka';
import {wejscie, postep} from '../anim';
import type {Scena} from '../typy';

type S = Extract<Scena, {typ: 'zakonczenie'}>;

export const Zakonczenie: React.FC<{scena: S}> = ({scena}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const linia = postep(frame, fps, 0.6, 0.9);

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
      <h1
        style={{
          margin: 0,
          color: MARKA.tekst,
          fontSize: 78,
          lineHeight: 1.04,
          letterSpacing: -2.2,
          fontWeight: 800,
          whiteSpace: 'pre-line',
          ...wejscie(frame, fps, 0, 24),
        }}
      >
        {scena.naglowek}
      </h1>

      <div
        style={{
          height: 6,
          width: `${linia * 100}%`,
          maxWidth: 300,
          background: MARKA.wyroznienie,
          borderRadius: 3,
          margin: '28px 0 32px 0',
        }}
      />

      <div style={{display: 'flex', flexDirection: 'column', gap: 14}}>
        {scena.kontakt.map((k, i) => (
          <div
            key={k.etykieta}
            style={{
              display: 'flex',
              gap: 24,
              alignItems: 'baseline',
              ...wejscie(frame, fps, 0.6 + i * 0.3, 16),
            }}
          >
            <span
              style={{
                minWidth: 190,
                color: MARKA.tekstCichy,
                fontSize: 21,
                fontWeight: 800,
                letterSpacing: 2,
                textTransform: 'uppercase',
              }}
            >
              {k.etykieta}
            </span>
            <span style={{color: MARKA.tekst, fontSize: 36, fontWeight: 700}}>{k.wartosc}</span>
          </div>
        ))}
      </div>

      <div
        style={{
          marginTop: 48,
          color: MARKA.akcent,
          fontSize: 46,
          fontWeight: 800,
          letterSpacing: -1.2,
          ...wejscie(frame, fps, 1.7, 20),
        }}
      >
        {scena.haslo}
      </div>
    </div>
  );
};
