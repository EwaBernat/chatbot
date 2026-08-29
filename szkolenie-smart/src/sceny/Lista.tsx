import React from 'react';
import {useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from '../marka';
import {wejscie} from '../anim';
import {Ekran} from '../Ekran';
import type {Scena} from '../typy';

type S = Extract<Scena, {typ: 'lista'}>;

/** Uniwersalna scena „etykieta + zdanie" — ewaluacja i podstawa prawna. */
export const Lista: React.FC<{scena: S}> = ({scena}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  return (
    <Ekran rozdzial={scena.rozdzial} naglowek={scena.naglowek}>
      <div
        style={{
          fontFamily: FONT,
          height: '100%',
          display: 'flex',
          flexDirection: 'column',
          gap: 16,
          justifyContent: 'center',
        }}
      >
        {scena.punkty.map((p, i) => (
          <div
            key={p.etykieta}
            style={{
              display: 'flex',
              gap: 26,
              alignItems: 'flex-start',
              background: MARKA.bialy,
              border: `2px solid ${MARKA.siatka}`,
              borderRadius: 18,
              padding: '22px 28px',
              ...wejscie(frame, fps, 0.4 + i * 0.75, 22),
            }}
          >
            <div
              style={{
                minWidth: 250,
                color: MARKA.akcent,
                fontSize: 24,
                fontWeight: 800,
                letterSpacing: 1.2,
                textTransform: 'uppercase',
                lineHeight: 1.3,
                paddingTop: 4,
                whiteSpace: 'pre-line',
              }}
            >
              {p.etykieta}
            </div>
            <div style={{color: MARKA.tekst, fontSize: 29, lineHeight: 1.4, flex: 1}}>
              {p.tekst}
            </div>
          </div>
        ))}

        {scena.stopka ? (
          <div
            style={{
              marginTop: 8,
              background: MARKA.tloDrugie,
              borderLeft: `6px solid ${MARKA.wyroznienie}`,
              borderRadius: 14,
              padding: '20px 26px',
              color: MARKA.tekst,
              fontSize: 28,
              fontWeight: 700,
              lineHeight: 1.36,
              ...wejscie(frame, fps, 0.4 + scena.punkty.length * 0.75, 18),
            }}
          >
            {scena.stopka}
          </div>
        ) : null}
      </div>
    </Ekran>
  );
};
