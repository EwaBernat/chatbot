import React from 'react';
import {useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from '../marka';
import {wejscie} from '../anim';
import {Ekran} from '../Ekran';
import type {Scena} from '../typy';

type S = Extract<Scena, {typ: 'formula'}>;

/**
 * Siedem pól formuły, a pod nimi to samo zdanie złożone z tych pól.
 * Fragmenty zdania zapalają się po kolei w tej samej kolejności, w jakiej
 * lektorka je wymienia, więc słuchacz widzi, skąd bierze się każdy kawałek.
 */
export const Formula: React.FC<{scena: S}> = ({scena}) => {
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
          justifyContent: 'center',
          gap: 46,
        }}
      >
        <div style={{display: 'flex', flexWrap: 'wrap', gap: 12}}>
          {scena.pola.map((p, i) => (
            <div
              key={p.numer}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 10,
                padding: '12px 20px',
                borderRadius: 12,
                background: MARKA.tloTrzecie,
                color: MARKA.tekst,
                fontSize: 24,
                fontWeight: 700,
                ...wejscie(frame, fps, 0.25 + i * 0.14, 14),
              }}
            >
              <span style={{color: MARKA.wyroznienie, fontWeight: 800}}>{p.numer}</span>
              {p.etykieta}
            </div>
          ))}
        </div>

        <div
          style={{
            background: MARKA.bialy,
            border: `2px solid ${MARKA.siatka}`,
            borderRadius: 22,
            padding: '30px 34px',
            ...wejscie(frame, fps, 1.4, 24),
          }}
        >
          <div
            style={{
              color: MARKA.akcent,
              fontSize: 19,
              fontWeight: 800,
              letterSpacing: 2.2,
              textTransform: 'uppercase',
              marginBottom: 18,
            }}
          >
            Formuła wypełniona — cel „Termometr napięcia”
          </div>
          <p style={{margin: 0, fontSize: 31, lineHeight: 1.5, color: MARKA.tekstDrugi}}>
            {scena.zdanie.map((cz, i) => (
              <span
                key={i}
                style={{
                  color: cz.pole ? MARKA.tekst : MARKA.tekstDrugi,
                  fontWeight: cz.pole ? 700 : 400,
                  background: cz.pole ? MARKA.tloTrzecie : 'transparent',
                  borderRadius: 6,
                  padding: cz.pole ? '2px 6px' : 0,
                  ...(cz.pole
                    ? {opacity: wejscie(frame, fps, 1.8 + cz.pole * 0.28, 0).opacity}
                    : {}),
                }}
              >
                {cz.tekst}
              </span>
            ))}
          </p>
        </div>
      </div>
    </Ekran>
  );
};
