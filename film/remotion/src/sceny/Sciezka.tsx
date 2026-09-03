import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate} from 'remotion';
import {MARKA, FONT} from '../marka';

/**
 * Obieg dokumentów: przystanki połączone linią rysowaną od lewej. Aktywny
 * przystanek jest większy i wypełniony — to jedyne miejsce, gdzie oko ma
 * się zatrzymać, reszta jest kontekstem.
 */
export const Sciezka: React.FC<{tytul?: string; przystanki: string[]; aktywny?: number}> = ({
  tytul,
  przystanki,
  aktywny,
}) => {
  const klatka = useCurrentFrame();
  const {fps} = useVideoConfig();
  const n = przystanki.length;
  const szer = 1680;
  const krok = szer / (n - 1);
  const linia = interpolate(klatka, [10, 10 + n * 10], [0, 1], {extrapolateRight: 'clamp'});

  return (
    <AbsoluteFill style={{padding: '90px 120px 220px', fontFamily: FONT, justifyContent: 'center'}}>
      {tytul ? (
        <div
          style={{
            fontSize: 50,
            fontWeight: 700,
            color: MARKA.tekst,
            marginBottom: 90,
            opacity: spring({frame: klatka, fps, config: {damping: 200}}),
          }}
        >
          {tytul}
        </div>
      ) : null}

      <div style={{position: 'relative', height: 300, width: szer, alignSelf: 'center'}}>
        {/* tor */}
        <div
          style={{
            position: 'absolute',
            top: 62,
            left: 0,
            width: szer,
            height: 8,
            borderRadius: 4,
            background: MARKA.siatka,
          }}
        />
        {/* linia rysowana */}
        <div
          style={{
            position: 'absolute',
            top: 62,
            left: 0,
            width: szer * linia,
            height: 8,
            borderRadius: 4,
            background: MARKA.slupek,
          }}
        />

        {przystanki.map((p, i) => {
          const w = spring({frame: klatka - 8 - i * 10, fps, config: {damping: 16, stiffness: 140}});
          const jestAktywny = aktywny !== undefined && aktywny === i;
          const pulsuj = jestAktywny
            ? 1 + 0.04 * Math.sin((klatka / fps) * 2 * Math.PI * 0.6)
            : 1;
          const r = jestAktywny ? 64 : 48;
          return (
            <div
              key={i}
              style={{
                position: 'absolute',
                left: i * krok - 120,
                top: 0,
                width: 240,
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                opacity: w,
                transform: `scale(${interpolate(w, [0, 1], [0.6, 1]) * pulsuj})`,
              }}
            >
              <div
                style={{
                  width: r * 2,
                  height: r * 2,
                  borderRadius: '50%',
                  marginTop: 66 - r,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  background: jestAktywny ? MARKA.slupek : '#FFFFFF',
                  border: `6px solid ${jestAktywny ? MARKA.slupek : MARKA.siatka}`,
                  boxShadow: jestAktywny ? '0 12px 34px rgba(91,63,168,0.35)' : 'none',
                  fontSize: jestAktywny ? 46 : 34,
                  fontWeight: 800,
                  color: jestAktywny ? '#FFFFFF' : MARKA.tekst,
                }}
              >
                {i + 1}
              </div>
              <div
                style={{
                  marginTop: 22,
                  fontSize: jestAktywny ? 30 : 26,
                  fontWeight: jestAktywny ? 700 : 600,
                  color: jestAktywny ? MARKA.tekst : MARKA.tekstDrugi,
                  textAlign: 'center',
                  lineHeight: 1.25,
                }}
              >
                {p}
              </div>
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
