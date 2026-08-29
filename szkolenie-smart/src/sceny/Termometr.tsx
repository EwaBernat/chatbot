import React from 'react';
import {useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from '../marka';
import {wejscie, postep} from '../anim';
import {Ekran} from '../Ekran';
import type {Scena} from '../typy';

type S = Extract<Scena, {typ: 'termometr'}>;

const KOLORY: Record<string, {plama: string; tlo: string}> = {
  'Strefa czerwona': {plama: MARKA.czerwony, tlo: MARKA.czerwonyTlo},
  'Strefa żółta': {plama: MARKA.zolty, tlo: MARKA.zoltyTlo},
  'Strefa zielona': {plama: MARKA.zielony, tlo: MARKA.zielonyTlo},
};

/**
 * Termometr napięcia 1–6 z konspektu TUE-1, obok karty obserwacji „4 na 5".
 * Kolor stref jest tu treścią, nie ozdobą, dlatego każda strefa ma podpis —
 * plansza czyta się także w skali szarości i przy protanopii.
 */
export const Termometr: React.FC<{scena: S}> = ({scena}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  return (
    <Ekran rozdzial={scena.rozdzial} naglowek={scena.naglowek}>
      <div style={{fontFamily: FONT, height: '100%', display: 'flex', gap: 34}}>
        <div style={{display: 'flex', flexDirection: 'column', gap: 10, flex: 1}}>
          {scena.strefy.map((s, i) => {
            const kolor = KOLORY[s.nazwa] ?? {plama: MARKA.akcent, tlo: MARKA.tloDrugie};
            return (
              <div
                key={s.nazwa}
                style={{
                  flex: s.do - s.od + 1,
                  display: 'flex',
                  alignItems: 'center',
                  gap: 20,
                  background: kolor.tlo,
                  borderRadius: 16,
                  padding: '16px 22px',
                  borderLeft: `8px solid ${kolor.plama}`,
                  ...wejscie(frame, fps, 0.9 + i * 0.7, 20),
                }}
              >
                <div style={{display: 'flex', flexDirection: 'column-reverse', gap: 6}}>
                  {Array.from({length: s.do - s.od + 1}, (_, k) => (
                    <span
                      key={k}
                      style={{
                        width: 40,
                        height: 34,
                        borderRadius: 8,
                        background: kolor.plama,
                        color: MARKA.bialy,
                        fontSize: 21,
                        fontWeight: 800,
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                      }}
                    >
                      {s.od + k}
                    </span>
                  ))}
                </div>
                <div>
                  <div
                    style={{
                      color: kolor.plama,
                      fontSize: 24,
                      fontWeight: 800,
                      letterSpacing: 1.6,
                      textTransform: 'uppercase',
                    }}
                  >
                    {s.nazwa}
                  </div>
                  <div
                    style={{
                      color: MARKA.tekst,
                      fontSize: 26,
                      lineHeight: 1.34,
                      marginTop: 6,
                    }}
                  >
                    {s.opis}
                  </div>
                </div>
              </div>
            );
          })}
        </div>

        <div
          style={{
            width: 330,
            background: MARKA.bialy,
            border: `2px solid ${MARKA.siatka}`,
            borderRadius: 20,
            padding: '26px 24px',
            display: 'flex',
            flexDirection: 'column',
            ...wejscie(frame, fps, 3.0, 22),
          }}
        >
          <div
            style={{
              color: MARKA.akcent,
              fontSize: 18,
              fontWeight: 800,
              letterSpacing: 2,
              textTransform: 'uppercase',
              lineHeight: 1.4,
            }}
          >
            Karta obserwacji
          </div>
          <div style={{color: MARKA.tekstDrugi, fontSize: 22, marginTop: 10, lineHeight: 1.35}}>
            Pięć kolejnych sytuacji trudnych w tygodniu.
          </div>
          <div style={{display: 'flex', gap: 10, marginTop: 22}}>
            {scena.karta.map((ok, i) => {
              const widoczny = postep(frame, fps, 3.3 + i * 0.22, 0.25);
              return (
                <span
                  key={i}
                  style={{
                    width: 52,
                    height: 62,
                    borderRadius: 12,
                    border: `2px solid ${MARKA.siatka}`,
                    background: ok ? MARKA.zielonyTlo : MARKA.tloDrugie,
                    color: ok ? MARKA.zielony : MARKA.tekstCichy,
                    fontSize: 30,
                    fontWeight: 800,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    opacity: widoczny,
                  }}
                >
                  {ok ? '✓' : '–'}
                </span>
              );
            })}
          </div>
          <div
            style={{
              marginTop: 'auto',
              paddingTop: 22,
              color: MARKA.tekst,
              fontSize: 52,
              fontWeight: 800,
              letterSpacing: -1,
              opacity: postep(frame, fps, 4.6, 0.4),
            }}
          >
            4 / 5
          </div>
          <div
            style={{
              color: MARKA.zielony,
              fontSize: 22,
              fontWeight: 700,
              opacity: postep(frame, fps, 4.6, 0.4),
            }}
          >
            kryterium spełnione
          </div>
        </div>
      </div>
    </Ekran>
  );
};
