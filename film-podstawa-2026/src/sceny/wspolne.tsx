import React from 'react';
import { useCurrentFrame, useVideoConfig, spring, interpolate } from 'remotion';
import { MARKA, FONT_NAGLOWEK, FONT_TEKST } from '../marka';

/** Wejście elementu z opóźnieniem — jedna sprężyna, żeby cały film miał
 *  ten sam charakter ruchu, a nie zbiór różnych animacji. */
export const useWejscie = (opoznienieKlatek = 0) => {
  const klatka = useCurrentFrame();
  const { fps } = useVideoConfig();
  const s = spring({
    frame: klatka - opoznienieKlatek, fps,
    config: { damping: 200, stiffness: 90 },
  });
  return {
    opacity: s,
    transform: `translateY(${interpolate(s, [0, 1], [26, 0])}px)`,
  };
};

export const Eyebrow: React.FC<{ children: React.ReactNode; opoznienie?: number }> = ({
  children, opoznienie = 0,
}) => (
  <p style={{
    ...useWejscie(opoznienie), margin: 0,
    fontFamily: FONT_NAGLOWEK, fontWeight: 700, fontSize: 26,
    letterSpacing: '.22em', textTransform: 'uppercase',
    color: MARKA.pomaranczJasny,
  }}>{children}</p>
);

export const Naglowek: React.FC<{ children: React.ReactNode; opoznienie?: number; maly?: boolean }> = ({
  children, opoznienie = 6, maly,
}) => (
  <h1 style={{
    ...useWejscie(opoznienie), margin: '18px 0 0',
    fontFamily: FONT_NAGLOWEK, fontWeight: 900,
    fontSize: maly ? 74 : 96, lineHeight: 1.03, letterSpacing: '-.015em',
    color: '#FFFFFF', maxWidth: 1180, textWrap: 'balance' as never,
  }}>{children}</h1>
);

export const Punkty: React.FC<{ pozycje: React.ReactNode[]; odKlatki?: number }> = ({
  pozycje, odKlatki = 20,
}) => (
  <ul style={{ margin: '38px 0 0', padding: 0, listStyle: 'none',
               display: 'flex', flexDirection: 'column', gap: 22 }}>
    {pozycje.map((p, i) => (
      <li key={i} style={{
        ...useWejscie(odKlatki + i * 9),
        display: 'grid', gridTemplateColumns: '18px 1fr', gap: 20,
        alignItems: 'start', fontFamily: FONT_TEKST, fontSize: 38,
        lineHeight: 1.35, color: MARKA.naCiemnym, maxWidth: 1080,
      }}>
        <span style={{ width: 14, height: 14, borderRadius: '50%',
                       background: MARKA.pomarancz, marginTop: 16 }} />
        <span>{p}</span>
      </li>
    ))}
  </ul>
);

/** Panel treści — lewa kolumna kadru, prawa zostaje na awatara. */
export const Panel: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <div style={{
    position: 'absolute', left: 120, top: 172, width: 1150,
    display: 'flex', flexDirection: 'column',
  }}>{children}</div>
);
