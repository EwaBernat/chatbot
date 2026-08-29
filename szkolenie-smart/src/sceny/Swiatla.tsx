import React from 'react';
import {useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from '../marka';
import {wejscie} from '../anim';
import {Ekran} from '../Ekran';
import type {Scena} from '../typy';

type S = Extract<Scena, {typ: 'swiatla'}>;

const PALETA = {
  zielony: {plama: MARKA.zielony, tlo: MARKA.zielonyTlo, nazwa: 'Zielony'},
  zolty: {plama: MARKA.zolty, tlo: MARKA.zoltyTlo, nazwa: 'Żółty'},
  czerwony: {plama: MARKA.czerwony, tlo: MARKA.czerwonyTlo, nazwa: 'Czerwony'},
} as const;

export const Swiatla: React.FC<{scena: S}> = ({scena}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  return (
    <Ekran rozdzial={scena.rozdzial} naglowek={scena.naglowek}>
      <div style={{fontFamily: FONT, height: '100%', display: 'flex', gap: 20}}>
        {scena.swiatla.map((s, i) => {
          const p = PALETA[s.kolor];
          return (
            <div
              key={s.kolor}
              style={{
                flex: 1,
                background: p.tlo,
                borderRadius: 22,
                padding: '28px 26px',
                display: 'flex',
                flexDirection: 'column',
                ...wejscie(frame, fps, 0.6 + i * 0.9, 26),
              }}
            >
              <div style={{display: 'flex', alignItems: 'center', gap: 14}}>
                <span
                  style={{
                    width: 36,
                    height: 36,
                    borderRadius: 18,
                    background: p.plama,
                    flexShrink: 0,
                  }}
                />
                <span style={{color: p.plama, fontSize: 34, fontWeight: 800, letterSpacing: -0.5}}>
                  {p.nazwa}
                </span>
              </div>
              <div
                style={{
                  color: MARKA.tekst,
                  fontSize: 40,
                  fontWeight: 800,
                  letterSpacing: -1,
                  marginTop: 18,
                }}
              >
                {s.wynik}
              </div>
              <div
                style={{
                  color: MARKA.tekst,
                  fontSize: 27,
                  fontWeight: 700,
                  lineHeight: 1.32,
                  marginTop: 14,
                }}
              >
                {s.decyzja}
              </div>
              <div
                style={{
                  marginTop: 'auto',
                  paddingTop: 18,
                  color: MARKA.tekstDrugi,
                  fontSize: 24,
                  lineHeight: 1.4,
                }}
              >
                {s.ruch}
              </div>
            </div>
          );
        })}
      </div>
    </Ekran>
  );
};
