import React from 'react';
import {useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from '../marka';
import {wejscie} from '../anim';
import {Ekran} from '../Ekran';
import type {Scena} from '../typy';

type S = Extract<Scena, {typ: 'porownanie'}>;

const Karta: React.FC<{
  znak: string;
  etykieta: string;
  tekst: string;
  komentarz: string;
  kolor: string;
  tloKarty: string;
  styl: React.CSSProperties;
}> = ({znak, etykieta, tekst, komentarz, kolor, tloKarty, styl}) => (
  <div
    style={{
      flex: 1,
      background: tloKarty,
      border: `2px solid ${kolor}33`,
      borderRadius: 22,
      padding: '30px 32px',
      display: 'flex',
      flexDirection: 'column',
      ...styl,
    }}
  >
    <div style={{display: 'flex', alignItems: 'center', gap: 12}}>
      <span
        style={{
          width: 40,
          height: 40,
          borderRadius: 20,
          background: kolor,
          color: MARKA.bialy,
          fontSize: 26,
          fontWeight: 800,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        {znak}
      </span>
      <span
        style={{
          color: kolor,
          fontSize: 21,
          fontWeight: 800,
          letterSpacing: 2,
          textTransform: 'uppercase',
        }}
      >
        {etykieta}
      </span>
    </div>
    <p
      style={{
        margin: '20px 0 0 0',
        color: MARKA.tekst,
        fontSize: 33,
        lineHeight: 1.32,
        fontWeight: 600,
      }}
    >
      „{tekst}”
    </p>
    <p
      style={{
        margin: 'auto 0 0 0',
        paddingTop: 20,
        color: MARKA.tekstDrugi,
        fontSize: 25,
        lineHeight: 1.42,
      }}
    >
      {komentarz}
    </p>
  </div>
);

export const Porownanie: React.FC<{scena: S}> = ({scena}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  return (
    <Ekran rozdzial={scena.rozdzial} naglowek={scena.naglowek}>
      <div style={{display: 'flex', gap: 24, height: '100%', fontFamily: FONT}}>
        <Karta
          znak="✕"
          etykieta={scena.zle.etykieta}
          tekst={scena.zle.tekst}
          komentarz={scena.zle.komentarz}
          kolor={MARKA.wyroznienie}
          tloKarty={MARKA.czerwonyTlo}
          styl={wejscie(frame, fps, 0.25, 26)}
        />
        <Karta
          znak="✓"
          etykieta={scena.dobre.etykieta}
          tekst={scena.dobre.tekst}
          komentarz={scena.dobre.komentarz}
          kolor={MARKA.zielony}
          tloKarty={MARKA.zielonyTlo}
          styl={wejscie(frame, fps, 0.75, 26)}
        />
      </div>
    </Ekran>
  );
};
