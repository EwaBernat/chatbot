import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate} from 'remotion';
import {MARKA, FONT} from '../marka';

/**
 * Jedna liczba na ekranie. Gdy dane mają jeden nagłówkowy wynik, tabela ani
 * wykres nie są potrzebne — liczba czytana na głos i pokazana wielkim drukiem
 * niesie więcej niż słupek o jednym elemencie.
 */
export const Liczba: React.FC<{wartosc: string; opis: string; kontekst?: string}> = ({
  wartosc,
  opis,
  kontekst,
}) => {
  const klatka = useCurrentFrame();
  const {fps} = useVideoConfig();

  const wejscie = spring({frame: klatka, fps, config: {damping: 200}});
  const skala = interpolate(wejscie, [0, 1], [0.94, 1]);

  return (
    <AbsoluteFill
      style={{
        justifyContent: 'center',
        alignItems: 'center',
        paddingBottom: 210,
        fontFamily: FONT,
        opacity: wejscie,
      }}
    >
      <div
        style={{
          fontSize: 240,
          fontWeight: 700,
          color: MARKA.tekst,
          lineHeight: 1,
          transform: `scale(${skala})`,
          letterSpacing: '-0.02em',
        }}
      >
        {wartosc}
      </div>
      <div style={{fontSize: 44, color: MARKA.tekstDrugi, marginTop: 28}}>{opis}</div>
      {kontekst ? (
        <div style={{fontSize: 30, color: MARKA.tekstCichy, marginTop: 16}}>{kontekst}</div>
      ) : null}
    </AbsoluteFill>
  );
};
