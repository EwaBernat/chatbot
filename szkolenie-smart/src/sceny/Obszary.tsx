import React from 'react';
import {useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from '../marka';
import {wejscie} from '../anim';
import {Ekran} from '../Ekran';
import type {Scena} from '../typy';

type S = Extract<Scena, {typ: 'obszary'}>;

export const Obszary: React.FC<{scena: S}> = ({scena}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  return (
    <Ekran rozdzial={scena.rozdzial} naglowek={scena.naglowek}>
      <div style={{fontFamily: FONT, height: '100%', display: 'flex', flexDirection: 'column'}}>
        <div
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(3, 1fr)',
            gap: 14,
          }}
        >
          {scena.obszary.map((o, i) => (
            <div
              key={o.nazwa}
              style={{
                background: MARKA.tloDrugie,
                borderRadius: 16,
                padding: '20px 22px',
                borderTop: `5px solid ${i % 2 === 0 ? MARKA.akcent : MARKA.akcentJasny}`,
                ...wejscie(frame, fps, 0.6 + i * 0.2, 18),
              }}
            >
              <div style={{color: MARKA.tekst, fontSize: 31, fontWeight: 700, lineHeight: 1.15}}>
                {o.nazwa}
              </div>
              <div
                style={{
                  color: MARKA.tekstCichy,
                  fontSize: 18,
                  fontWeight: 700,
                  letterSpacing: 1.2,
                  textTransform: 'uppercase',
                  marginTop: 10,
                  lineHeight: 1.35,
                }}
              >
                {o.opis}
              </div>
            </div>
          ))}
        </div>

        <div
          style={{
            marginTop: 'auto',
            display: 'flex',
            alignItems: 'center',
            gap: 18,
            background: MARKA.bialy,
            border: `2px solid ${MARKA.siatka}`,
            borderRadius: 18,
            padding: '22px 28px',
            ...wejscie(frame, fps, 2.6, 20),
          }}
        >
          <span
            style={{
              padding: '8px 16px',
              borderRadius: 999,
              background: MARKA.wyroznienie,
              color: MARKA.bialy,
              fontSize: 19,
              fontWeight: 800,
              letterSpacing: 1.4,
              textTransform: 'uppercase',
              whiteSpace: 'nowrap',
            }}
          >
            od 1 IX 2026
          </span>
          <span style={{color: MARKA.tekst, fontSize: 27, lineHeight: 1.38}}>{scena.stopka}</span>
        </div>
      </div>
    </Ekran>
  );
};
