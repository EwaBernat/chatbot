import React from 'react';
import { useCurrentFrame, useVideoConfig } from 'remotion';
import { FONT_TEKST } from '../marka';

export type Napis = { odS: number; doS: number; tekst: string };

/** Napisy z pliku SRT — czytelne na ciemnym woalu, bez tła-prostokąta. */
export const Napisy: React.FC<{ napisy: Napis[] }> = ({ napisy }) => {
  const klatka = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = klatka / fps;
  const biezacy = napisy.find((n) => t >= n.odS && t <= n.doS);
  if (!biezacy) return null;

  return (
    <div style={{
      position: 'absolute', left: 0, right: 0, bottom: 46,
      display: 'flex', justifyContent: 'center', padding: '0 220px',
    }}>
      <p style={{
        margin: 0, fontFamily: FONT_TEKST, fontSize: 34, lineHeight: 1.35,
        color: '#FFFFFF', textAlign: 'center', maxWidth: 1240,
        textShadow: '0 2px 12px rgba(0,0,0,.85), 0 0 3px rgba(0,0,0,.9)',
      }}>{biezacy.tekst}</p>
    </div>
  );
};

/** Minimalny parser SRT — tylko to, czego potrzebuje film. */
export const parsujSrt = (tekst: string): Napis[] => {
  const naSekundy = (s: string) => {
    const [g, m, r] = s.trim().replace(',', '.').split(':');
    return Number(g) * 3600 + Number(m) * 60 + Number(r);
  };
  return tekst.split(/\r?\n\r?\n/).flatMap((blok) => {
    const linie = blok.split(/\r?\n/).filter(Boolean);
    const czas = linie.find((l) => l.includes('-->'));
    if (!czas) return [];
    const [od, do_] = czas.split('-->');
    const tresc = linie.slice(linie.indexOf(czas) + 1).join(' ').trim();
    return tresc ? [{ odS: naSekundy(od), doS: naSekundy(do_), tekst: tresc }] : [];
  });
};
