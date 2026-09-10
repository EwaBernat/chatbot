import React from 'react';
import { interpolate, useCurrentFrame, useVideoConfig } from 'remotion';
import { FONT, MARKA, gradient } from '../marka';

/** Tło marki — gradient z wolnym dryfem kąta. */
export const Tlo: React.FC<{ children?: React.ReactNode }> = ({ children }) => {
  const f = useCurrentFrame();
  return (
    <div
      style={{
        position: 'absolute',
        inset: 0,
        background: gradient(interpolate(f, [0, 600], [0, 14], { extrapolateRight: 'clamp' })),
        fontFamily: FONT,
      }}
    >
      {children}
    </div>
  );
};

/** Znak marki w lewym górnym rogu (obecny na każdej scenie). */
export const Znak: React.FC<{ ciemnyTekst?: boolean }> = ({ ciemnyTekst }) => {
  const kolor = ciemnyTekst ? MARKA.fiolet : 'rgba(255,255,255,0.86)';
  return (
    <div
      style={{
        position: 'absolute',
        top: 44,
        left: 56,
        display: 'flex',
        alignItems: 'center',
        gap: 12,
        fontFamily: FONT,
        letterSpacing: 2.4,
        fontSize: 20,
        fontWeight: 700,
        color: kolor,
      }}
    >
      <span style={{ width: 12, height: 12, borderRadius: 12, background: MARKA.pomarancz }} />
      EDUPLANER 2026 · PCTP KOSZALIN
    </div>
  );
};

/** Podpis scen (dolny lewy róg) — wjeżdża z lewej i zostaje. */
export const Podpis: React.FC<{ tekst: string }> = ({ tekst }) => {
  const f = useCurrentFrame();
  const wejscie = interpolate(f, [8, 24], [-40, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const krycie = interpolate(f, [8, 24], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  return (
    <div
      style={{
        position: 'absolute',
        left: 56,
        bottom: 64,
        transform: `translateX(${wejscie}px)`,
        opacity: krycie,
        background: MARKA.fiolet,
        color: MARKA.bialy,
        fontFamily: FONT,
        fontSize: 26,
        fontWeight: 700,
        padding: '16px 26px',
        borderLeft: `6px solid ${MARKA.pomarancz}`,
        borderRadius: 4,
        boxShadow: `0 18px 44px ${MARKA.cien}`,
        maxWidth: 1100,
      }}
    >
      {tekst}
    </div>
  );
};

/** Licznik (prawy górny róg) — nabija wartość razem z animacją sceny. */
export const Licznik: React.FC<{ do: number; opis: string; klatekNabijania?: number }> = ({
  do: cel,
  opis,
  klatekNabijania = 90,
}) => {
  const f = useCurrentFrame();
  const wartosc = Math.round(
    interpolate(f, [12, 12 + klatekNabijania], [0, cel], {
      extrapolateLeft: 'clamp',
      extrapolateRight: 'clamp',
    }),
  );
  const krycie = interpolate(f, [6, 20], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  return (
    <div
      style={{
        position: 'absolute',
        top: 40,
        right: 56,
        opacity: krycie,
        textAlign: 'right',
        fontFamily: FONT,
        color: MARKA.bialy,
        background: 'rgba(26,15,66,0.88)',
        padding: '14px 22px',
        borderRadius: 6,
        borderTop: `4px solid ${MARKA.pomarancz}`,
      }}
    >
      <div style={{ fontSize: 62, fontWeight: 700, lineHeight: 1 }}>{wartosc}</div>
      <div style={{ fontSize: 18, letterSpacing: 1.4, opacity: 0.85, marginTop: 6 }}>
        {opis.toUpperCase()}
      </div>
    </div>
  );
};

/** Cienki pasek postępu całego filmu (na samym dole kadru). */
export const PasekPostepu: React.FC<{ odKlatki: number; doKlatki: number }> = ({
  odKlatki,
  doKlatki,
}) => {
  const f = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const globalna = odKlatki + f;
  const postep = Math.min(1, globalna / Math.max(1, doKlatki || durationInFrames));
  return (
    <div style={{ position: 'absolute', left: 0, right: 0, bottom: 0, height: 6, background: 'rgba(255,255,255,0.14)' }}>
      <div style={{ width: `${postep * 100}%`, height: '100%', background: MARKA.pomarancz }} />
    </div>
  );
};

/** Znak wodny informujący, że dane ucznia są przykładowe. */
export const ZnakDanePrzykladowe: React.FC = () => (
  <div
    style={{
      position: 'absolute',
      right: 56,
      bottom: 66,
      fontFamily: FONT,
      fontSize: 17,
      letterSpacing: 2,
      fontWeight: 700,
      color: 'rgba(45,27,105,0.55)',
      background: 'rgba(255,255,255,0.82)',
      border: `1px solid rgba(45,27,105,0.2)`,
      padding: '8px 14px',
      borderRadius: 4,
    }}
  >
    DANE PRZYKŁADOWE
  </div>
);
