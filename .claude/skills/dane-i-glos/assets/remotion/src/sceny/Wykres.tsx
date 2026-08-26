import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate} from 'remotion';
import {MARKA, FONT} from '../marka';
import type {Slupek} from '../typy';

/**
 * Słupki poziome, JEDNA seria — więc jeden odcień fioletu na wszystkie słupki.
 * Pomarańcz pojawia się wyłącznie tam, gdzie `wyroznij` wskazuje wartość
 * wymagającą uwagi, i nigdy sam: towarzyszy mu podpis, żeby informacja nie
 * zależała od samego koloru (widzenie barw, druk czarno-biały).
 *
 * Legendy nie ma celowo: przy jednej serii tytuł nazywa to, co widać, a każdy
 * słupek ma etykietę wprost przy końcu.
 */
export const Wykres: React.FC<{
  tytul: string;
  slupki: Slupek[];
  jednostka?: string;
  wyroznij?: string;
  maks?: number;
}> = ({tytul, slupki, jednostka = '', wyroznij, maks}) => {
  const klatka = useCurrentFrame();
  const {fps} = useVideoConfig();

  const gora = maks ?? Math.max(...slupki.map((s) => s.wartosc)) * 1.08;
  const naglowek = spring({frame: klatka, fps, config: {damping: 200}});

  const sformatuj = (n: number) =>
    (Number.isInteger(n) ? String(n) : n.toFixed(1).replace('.', ',')) + jednostka;

  return (
    <AbsoluteFill style={{padding: '96px 140px 250px', fontFamily: FONT, justifyContent: 'center'}}>
      <div
        style={{
          fontSize: 52,
          fontWeight: 700,
          color: MARKA.tekst,
          marginBottom: 56,
          opacity: naglowek,
        }}
      >
        {tytul}
      </div>

      <div style={{display: 'flex', flexDirection: 'column', gap: 30}}>
        {slupki.map((s, i) => {
          // Każdy słupek wjeżdża z opóźnieniem — oko nadąża za kolejnością,
          // zamiast dostać cztery ruchy naraz.
          const wzrost = spring({
            frame: klatka - 6 - i * 5,
            fps,
            config: {damping: 200, mass: 0.7},
          });
          const udzial = interpolate(wzrost, [0, 1], [0, s.wartosc / gora], {
            extrapolateRight: 'clamp',
          });
          const podswietlony = wyroznij !== undefined && s.etykieta === wyroznij;

          return (
            <div key={s.etykieta} style={{display: 'flex', alignItems: 'center', gap: 28}}>
              <div
                style={{
                  width: 132,
                  textAlign: 'right',
                  fontSize: 34,
                  fontWeight: 600,
                  color: MARKA.tekst,
                  flexShrink: 0,
                }}
              >
                {s.etykieta}
              </div>

              <div
                style={{
                  flex: 1,
                  height: 56,
                  background: MARKA.tloDrugie,
                  borderRadius: 4,
                  position: 'relative',
                }}
              >
                <div
                  style={{
                    position: 'absolute',
                    left: 0,
                    top: 0,
                    bottom: 0,
                    width: `${udzial * 100}%`,
                    background: podswietlony ? MARKA.wyroznienie : MARKA.slupek,
                    // zaokrąglony tylko koniec danych; podstawa zostaje ostra
                    borderRadius: '0 4px 4px 0',
                  }}
                />
              </div>

              {/* Etykieta wprost przy słupku, w kolorze tekstu — nie w kolorze serii. */}
              <div
                style={{
                  width: 156,
                  fontSize: 34,
                  fontWeight: 700,
                  color: MARKA.tekst,
                  opacity: wzrost,
                  flexShrink: 0,
                }}
              >
                {sformatuj(s.wartosc)}
                {podswietlony ? (
                  <span
                    style={{
                      display: 'block',
                      fontSize: 21,
                      fontWeight: 600,
                      color: MARKA.wyroznienie,
                      marginTop: 2,
                    }}
                  >
                    wymaga uwagi
                  </span>
                ) : null}
              </div>
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
