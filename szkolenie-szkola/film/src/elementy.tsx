import React from 'react';
import { AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig } from 'remotion';
import { KADR, KOLOR, KROJ } from './marka';

/** Miękkie wejście: 0 → 1 w zadanej liczbie klatek, z lekkim podniesieniem. */
export const wejscie = (klatka: number, start = 0, dlugosc = 18) => {
  const t = interpolate(klatka - start, [0, dlugosc], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  // easing „ease-out cubic" — szybko rusza, miękko dochodzi
  return 1 - Math.pow(1 - t, 3);
};

/** Tło kadru: ciepła biel, delikatna poświata i pasek marki u góry. */
export const Tlo: React.FC<{ ziarno?: number }> = ({ ziarno = 0 }) => {
  const klatka = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  // powolny dryf poświaty — kadr nigdy nie stoi całkiem w miejscu
  const dryf = interpolate(klatka, [0, Math.max(durationInFrames, 1)], [0, 1]);
  return (
    <AbsoluteFill style={{ backgroundColor: KOLOR.tlo }}>
      <AbsoluteFill
        style={{
          background: `radial-gradient(1200px 760px at ${18 + dryf * 8 + ziarno}% ${12 + dryf * 6}%, rgba(45,27,105,0.07), transparent 62%),
                       radial-gradient(900px 620px at ${92 - dryf * 6}% ${88 - dryf * 4}%, rgba(232,69,12,0.06), transparent 60%)`,
        }}
      />
      <AbsoluteFill
        style={{
          backgroundImage:
            'linear-gradient(rgba(45,27,105,0.045) 1px, transparent 1px), linear-gradient(90deg, rgba(45,27,105,0.045) 1px, transparent 1px)',
          backgroundSize: '96px 96px',
          maskImage: 'radial-gradient(1400px 800px at 50% 45%, black, transparent 78%)',
        }}
      />
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          right: 0,
          height: KADR.gornyPasek,
          background: `linear-gradient(90deg, ${KOLOR.pomarancz}, ${KOLOR.pomaranczJasny} 55%, ${KOLOR.fiolet})`,
        }}
      />
    </AbsoluteFill>
  );
};

/** Nagłówek kadru: etykieta modułu, kreska, tytuł sceny. */
export const NaglowekSceny: React.FC<{
  etykieta: string;
  nadtytul?: string;
  tytul: string;
  start?: number;
}> = ({ etykieta, nadtytul, tytul, start = 0 }) => {
  const klatka = useCurrentFrame();
  const w = wejscie(klatka, start, 20);
  return (
    <div style={{ position: 'absolute', top: 76, left: KADR.margines, right: KADR.margines }}>
      <div
        style={{
          fontFamily: KROJ,
          fontSize: 21,
          letterSpacing: 4.2,
          color: KOLOR.szaryJasny,
          fontWeight: 700,
          opacity: w,
        }}
      >
        {etykieta}
      </div>
      <div
        style={{
          height: 4,
          width: interpolate(w, [0, 1], [0, 118]),
          background: KOLOR.pomarancz,
          margin: '18px 0 26px',
          borderRadius: 2,
        }}
      />
      {nadtytul ? (
        <div
          style={{
            fontFamily: KROJ,
            fontSize: 24,
            letterSpacing: 2.4,
            color: KOLOR.pomarancz,
            fontWeight: 700,
            marginBottom: 10,
            opacity: wejscie(klatka, start + 4, 18),
          }}
        >
          {nadtytul}
        </div>
      ) : null}
      <div
        style={{
          fontFamily: KROJ,
          fontSize: 60,
          lineHeight: 1.1,
          color: KOLOR.fiolet,
          fontWeight: 700,
          opacity: wejscie(klatka, start + 6, 22),
          transform: `translateY(${interpolate(wejscie(klatka, start + 6, 22), [0, 1], [16, 0])}px)`,
        }}
      >
        {tytul}
      </div>
    </div>
  );
};

/**
 * Tekst z kolorowaniem ważnych miejsc: fragmenty w **gwiazdkach** dostają
 * pomarańczowy zakreślacz, który wjeżdża od lewej jak pociągnięcie markerem.
 */
export const Zakreslany: React.FC<{
  tekst: string;
  start: number;
  kolor?: string;
  grubosc?: number;
}> = ({ tekst, start, kolor = KOLOR.atrament, grubosc }) => {
  const klatka = useCurrentFrame();
  const czesci = tekst.split(/\*\*(.*?)\*\*/g);
  return (
    <span style={{ color: kolor, fontWeight: grubosc as never }}>
      {czesci.map((czesc, i) => {
        if (i % 2 === 0) return <span key={i}>{czesc}</span>;
        const szerokosc = interpolate(klatka - start - 10, [0, 16], [0, 100], {
          extrapolateLeft: 'clamp',
          extrapolateRight: 'clamp',
        });
        return (
          <span key={i} style={{ position: 'relative', whiteSpace: 'nowrap', fontWeight: 700 }}>
            <span
              style={{
                position: 'absolute',
                left: -6,
                right: 0,
                bottom: -2,
                top: '18%',
                width: `calc(${szerokosc}% + 12px)`,
                background: KOLOR.zaznaczenie,
                borderRadius: 4,
                zIndex: 0,
              }}
            />
            <span style={{ position: 'relative', zIndex: 1, color: KOLOR.fiolet }}>{czesc}</span>
          </span>
        );
      })}
    </span>
  );
};

/** Pasek napisów u dołu kadru — ten sam co w modułach przedszkolnych. */
export const PasekNapisow: React.FC<{ tekst: string }> = ({ tekst }) => {
  const klatka = useCurrentFrame();
  const w = wejscie(klatka, 0, 10);
  if (!tekst) return null;
  return (
    <div
      style={{
        position: 'absolute',
        left: 388,
        width: 1147,
        top: KADR.pasekNapisowGora,
        minHeight: KADR.pasekNapisowWysokosc,
        background: 'rgba(255,255,255,0.94)',
        border: `1px solid ${KOLOR.ramka}`,
        borderRadius: 14,
        boxShadow: '0 10px 34px rgba(45,27,105,0.10)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '18px 40px',
        opacity: w,
      }}
    >
      <div
        style={{
          fontFamily: KROJ,
          fontSize: 30,
          lineHeight: 1.34,
          color: KOLOR.atrament,
          textAlign: 'center',
        }}
      >
        {tekst}
      </div>
    </div>
  );
};

/** Stopka: nazwa materiału po lewej, numer modułu po prawej. */
export const Stopka: React.FC<{ lewa: string; prawa: string }> = ({ lewa, prawa }) => (
  <div
    style={{
      position: 'absolute',
      bottom: 30,
      left: KADR.margines,
      right: KADR.margines,
      display: 'flex',
      justifyContent: 'space-between',
      fontFamily: KROJ,
      fontSize: 18,
      letterSpacing: 1.6,
      color: '#C4C9CE',
    }}
  >
    <span>{lewa}</span>
    <span>{prawa}</span>
  </div>
);

/** Znak PCTP — rysowany, żeby nie zależeć od pliku graficznego. */
export const ZnakPctp: React.FC<{ rozmiar?: number; opacity?: number }> = ({ rozmiar = 96, opacity = 1 }) => (
  <div
    style={{
      width: rozmiar,
      height: rozmiar,
      borderRadius: '50%',
      background: `radial-gradient(circle at 34% 28%, ${KOLOR.fioletJasny}, ${KOLOR.fiolet} 70%)`,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      color: '#fff',
      fontFamily: KROJ,
      fontWeight: 700,
      fontSize: rozmiar * 0.26,
      letterSpacing: 1.5,
      boxShadow: '0 8px 26px rgba(45,27,105,0.28)',
      opacity,
    }}
  >
    PCTP
  </div>
);
