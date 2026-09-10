import React from 'react';
import { interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { FONT, MARKA } from '../marka';
import { Tlo, Znak } from '../ui/Chrome';
import type { Scena } from '../typy';

/** Pomarańczowy „ptaszek" dorysowywany ścieżką SVG. */
const Ptaszek: React.FC<{ postep: number }> = ({ postep }) => (
  <svg width={40} height={40} viewBox="0 0 40 40" style={{ flexShrink: 0 }}>
    <path
      d="M7 21 L16 30 L33 11"
      fill="none"
      stroke={MARKA.pomarancz}
      strokeWidth={5}
      strokeLinecap="round"
      strokeLinejoin="round"
      strokeDasharray={48}
      strokeDashoffset={48 * (1 - postep)}
    />
  </svg>
);

/** Scena typu „lista" — co składa się na roczną subskrypcję. */
export const Lista: React.FC<{ scena: Scena }> = ({ scena }) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  const pozycje = scena.lista ?? [];
  const dopisekOd = 13 * fps;

  return (
    <Tlo>
      <Znak />
      <div
        style={{
          position: 'absolute',
          inset: 0,
          padding: '150px 140px 110px',
          fontFamily: FONT,
          color: MARKA.bialy,
        }}
      >
        <div
          style={{
            fontSize: 22,
            letterSpacing: 4,
            fontWeight: 700,
            color: MARKA.pomarancz,
            opacity: interpolate(f, [0, 14], [0, 1], { extrapolateRight: 'clamp' }),
          }}
        >
          {scena.tytul}
        </div>
        <div style={{ fontSize: 54, fontWeight: 700, marginTop: 14, marginBottom: 44 }}>
          Roczna subskrypcja to:
        </div>

        <div style={{ display: 'flex', flexDirection: 'column', gap: 18 }}>
          {pozycje.map((poz, i) => {
            const start = 18 + i * 8;
            const s = spring({ frame: f - start, fps, config: { damping: 200 }, durationInFrames: 22 });
            return (
              <div
                key={poz}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: 20,
                  opacity: s,
                  transform: `translateX(${(1 - s) * -50}px)`,
                  fontSize: 34,
                  lineHeight: 1.3,
                }}
              >
                <Ptaszek postep={s} />
                <span>{poz}</span>
              </div>
            );
          })}
        </div>

        <div
          style={{
            marginTop: 40,
            fontSize: 28,
            fontStyle: 'italic',
            color: 'rgba(255,255,255,0.86)',
            opacity: interpolate(f, [dopisekOd, dopisekOd + 18], [0, 1], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            }),
          }}
        >
          a ponad to — Państwa głos: rozwój według formularza analizy potrzeb
        </div>
      </div>
    </Tlo>
  );
};
