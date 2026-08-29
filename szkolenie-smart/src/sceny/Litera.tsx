import React from 'react';
import {useCurrentFrame, useVideoConfig, spring} from 'remotion';
import {MARKA, FONT} from '../marka';
import {wejscie} from '../anim';
import {Ekran} from '../Ekran';
import type {Scena} from '../typy';

type S = Extract<Scena, {typ: 'litera'}>;

const Wiersz: React.FC<{
  etykieta: string;
  tekst: string;
  kolor: string;
  styl: React.CSSProperties;
}> = ({etykieta, tekst, kolor, styl}) => (
  <div
    style={{
      display: 'flex',
      gap: 22,
      alignItems: 'flex-start',
      padding: '20px 0',
      borderTop: `2px solid ${MARKA.siatka}`,
      ...styl,
    }}
  >
    <span
      style={{
        minWidth: 190,
        color: kolor,
        fontSize: 20,
        fontWeight: 800,
        letterSpacing: 2,
        textTransform: 'uppercase',
        paddingTop: 8,
      }}
    >
      {etykieta}
    </span>
    <span style={{color: MARKA.tekst, fontSize: 31, lineHeight: 1.36, flex: 1}}>
      {tekst}
    </span>
  </div>
);

export const Litera: React.FC<{scena: S}> = ({scena}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const skok = spring({
    frame,
    fps,
    config: {damping: 14, mass: 0.9, stiffness: 90},
    durationInFrames: Math.round(fps * 1.2),
  });

  return (
    <Ekran rozdzial={scena.rozdzial} naglowek={scena.naglowek}>
      <div
        style={{
          fontFamily: FONT,
          height: '100%',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
        }}
      >
        <div style={{display: 'flex', alignItems: 'center', gap: 30, marginBottom: 12}}>
          <div
            style={{
              width: 148,
              height: 148,
              borderRadius: 30,
              background: `linear-gradient(150deg, ${MARKA.akcentJasny} 0%, ${MARKA.tekst} 100%)`,
              color: MARKA.bialy,
              fontSize: 92,
              fontWeight: 800,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              transform: `scale(${0.6 + skok * 0.4}) rotate(${(1 - skok) * -8}deg)`,
              boxShadow: '0 20px 44px rgba(45,27,105,0.28)',
            }}
          >
            {scena.litera}
          </div>
          <div style={wejscie(frame, fps, 0.2, 18)}>
            <div
              style={{
                color: MARKA.tekst,
                fontSize: 52,
                fontWeight: 800,
                letterSpacing: -1,
                lineHeight: 1.05,
              }}
            >
              {scena.nazwa}
            </div>
            <div
              style={{
                color: MARKA.tekstCichy,
                fontSize: 23,
                fontWeight: 700,
                letterSpacing: 2.6,
                textTransform: 'uppercase',
                marginTop: 8,
              }}
            >
              {scena.angielskie}
            </div>
          </div>
        </div>

        <div style={{marginTop: 40}}>
          <Wiersz
            etykieta="Pytanie"
            tekst={scena.pytanie}
            kolor={MARKA.akcent}
            styl={wejscie(frame, fps, 0.45, 20)}
          />
          <Wiersz
            etykieta="W praktyce"
            tekst={scena.praktyka}
            kolor={MARKA.zielony}
            styl={wejscie(frame, fps, 0.85, 20)}
          />
          <Wiersz
            etykieta="Pułapka"
            tekst={scena.pulapka}
            kolor={MARKA.wyroznienie}
            styl={wejscie(frame, fps, 1.25, 20)}
          />
        </div>
      </div>
    </Ekran>
  );
};
