import React from 'react';
import {useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from '../marka';
import {wejscie} from '../anim';
import {Ekran} from '../Ekran';
import type {Scena} from '../typy';

type S = Extract<Scena, {typ: 'kroki'}>;

export const Kroki: React.FC<{scena: S}> = ({scena}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  return (
    <Ekran rozdzial={scena.rozdzial} naglowek={scena.naglowek}>
      <div
        style={{
          fontFamily: FONT,
          display: 'flex',
          flexDirection: 'column',
          gap: 18,
          height: '100%',
          justifyContent: 'center',
        }}
      >
        {scena.kroki.map((k, i) => (
          <div
            key={k.numer}
            style={{
              display: 'flex',
              gap: 24,
              alignItems: 'flex-start',
              background: MARKA.tloDrugie,
              borderRadius: 18,
              padding: '22px 28px',
              borderLeft: `6px solid ${MARKA.akcent}`,
              ...wejscie(frame, fps, 0.3 + i * 0.45, 22),
            }}
          >
            <span
              style={{
                minWidth: 58,
                height: 58,
                borderRadius: 16,
                background: MARKA.tekst,
                color: MARKA.bialy,
                fontSize: 32,
                fontWeight: 800,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
              }}
            >
              {k.numer}
            </span>
            <div>
              <div style={{color: MARKA.tekst, fontSize: 34, fontWeight: 700, lineHeight: 1.2}}>
                {k.tytul}
              </div>
              <div
                style={{
                  color: MARKA.tekstDrugi,
                  fontSize: 26,
                  lineHeight: 1.38,
                  marginTop: 8,
                }}
              >
                {k.opis}
              </div>
            </div>
          </div>
        ))}
      </div>
    </Ekran>
  );
};
