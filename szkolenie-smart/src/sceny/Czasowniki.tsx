import React from 'react';
import {useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from '../marka';
import {wejscie} from '../anim';
import {Ekran} from '../Ekran';
import type {Scena} from '../typy';

type S = Extract<Scena, {typ: 'czasowniki'}>;

const Kolumna: React.FC<{
  znak: string;
  tytul: string;
  slowa: string[];
  kolor: string;
  tlo: string;
  przekreslone: boolean;
  opoznienie: number;
}> = ({znak, tytul, slowa, kolor, tlo, przekreslone, opoznienie}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  return (
    <div style={{flex: 1, ...wejscie(frame, fps, opoznienie, 22)}}>
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          gap: 12,
          color: kolor,
          fontSize: 21,
          fontWeight: 800,
          letterSpacing: 2,
          textTransform: 'uppercase',
          marginBottom: 18,
        }}
      >
        <span
          style={{
            width: 34,
            height: 34,
            borderRadius: 17,
            background: kolor,
            color: MARKA.bialy,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: 22,
          }}
        >
          {znak}
        </span>
        {tytul}
      </div>
      <div style={{display: 'flex', flexWrap: 'wrap', gap: 10}}>
        {slowa.map((s, i) => (
          <span
            key={s}
            style={{
              padding: '11px 20px',
              borderRadius: 999,
              background: tlo,
              color: przekreslone ? MARKA.tekstDrugi : MARKA.tekst,
              fontSize: 27,
              fontWeight: 600,
              textDecoration: przekreslone ? 'line-through' : 'none',
              ...wejscie(frame, fps, opoznienie + 0.2 + i * 0.07, 12),
            }}
          >
            {s}
          </span>
        ))}
      </div>
    </div>
  );
};

export const Czasowniki: React.FC<{scena: S}> = ({scena}) => {
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
        <div style={{display: 'flex', gap: 30}}>
          <Kolumna
            znak="✓"
            tytul="Które widać"
            slowa={scena.dobre}
            kolor={MARKA.zielony}
            tlo={MARKA.zielonyTlo}
            przekreslone={false}
            opoznienie={0.25}
          />
          <Kolumna
            znak="✕"
            tytul="Do wymiany"
            slowa={scena.zle}
            kolor={MARKA.wyroznienie}
            tlo={MARKA.czerwonyTlo}
            przekreslone
            opoznienie={1.5}
          />
        </div>

        <div
          style={{
            background: MARKA.tloDrugie,
            borderRadius: 18,
            padding: '24px 30px',
            borderLeft: `6px solid ${MARKA.wyroznienie}`,
            color: MARKA.tekst,
            fontSize: 29,
            lineHeight: 1.4,
            ...wejscie(frame, fps, 2.6, 20),
          }}
        >
          {scena.naprawa}
        </div>
      </div>
    </Ekran>
  );
};
