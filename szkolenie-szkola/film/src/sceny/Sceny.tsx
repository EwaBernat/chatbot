import React from 'react';
import { AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';
import { KADR, KOLOR, KROJ } from '../marka';
import { NaglowekSceny, wejscie, Zakreslany, ZnakPctp } from '../elementy';
import type { Scena } from '../typy';

const OBSZAR = { left: KADR.margines, right: KADR.margines, top: 300 };

/** Delikatny najazd kamery na całą scenę — kadr żyje, ale nie kręci się w kółko. */
const Najazd: React.FC<{ children: React.ReactNode; sila?: number }> = ({ children, sila = 0.018 }) => {
  const klatka = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const p = interpolate(klatka, [0, Math.max(durationInFrames, 1)], [0, 1]);
  return (
    <AbsoluteFill style={{ transform: `scale(${1 + sila * p})`, transformOrigin: '50% 46%' }}>
      {children}
    </AbsoluteFill>
  );
};

// ───────────────────────────────────────────── czołówka całego szkolenia

const Czolowka: React.FC<{ s: Extract<Scena, { typ: 'czolowka' }> }> = ({ s }) => {
  const k = useCurrentFrame();
  return (
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center' }}>
      <div style={{ opacity: wejscie(k, 0, 26), transform: `translateY(${interpolate(wejscie(k, 0, 26), [0, 1], [22, 0])}px)` }}>
        <ZnakPctp rozmiar={122} />
      </div>
      <div
        style={{
          fontFamily: KROJ,
          fontSize: 22,
          letterSpacing: 6,
          color: KOLOR.szaryJasny,
          fontWeight: 700,
          marginTop: 34,
          opacity: wejscie(k, 14, 20),
        }}
      >
        EDUPLANER 2026 · PCTP · SZKOLENIE RADY PEDAGOGICZNEJ
      </div>
      <div
        style={{
          fontFamily: KROJ,
          fontSize: 86,
          fontWeight: 700,
          color: KOLOR.fiolet,
          marginTop: 22,
          textAlign: 'center',
          lineHeight: 1.08,
          opacity: wejscie(k, 22, 24),
          transform: `translateY(${interpolate(wejscie(k, 22, 24), [0, 1], [18, 0])}px)`,
        }}
      >
        {s.tytul}
      </div>
      <div
        style={{
          width: interpolate(wejscie(k, 34, 22), [0, 1], [0, 300]),
          height: 5,
          background: KOLOR.pomarancz,
          borderRadius: 3,
          margin: '30px 0 26px',
        }}
      />
      <div
        style={{
          fontFamily: KROJ,
          fontSize: 34,
          color: KOLOR.szary,
          opacity: wejscie(k, 40, 22),
          textAlign: 'center',
          maxWidth: 1260,
          lineHeight: 1.36,
        }}
      >
        {s.podtytul}
      </div>
      <div style={{ display: 'flex', gap: 14, marginTop: 52, flexWrap: 'wrap', justifyContent: 'center', maxWidth: 1500 }}>
        {s.czesci.map((c, i) => (
          <div
            key={c}
            style={{
              fontFamily: KROJ,
              fontSize: 21,
              color: KOLOR.fiolet,
              background: KOLOR.wypelnienie,
              border: `1px solid ${KOLOR.ramka}`,
              borderRadius: 999,
              padding: '11px 22px',
              opacity: wejscie(k, 54 + i * 6, 16),
              transform: `translateY(${interpolate(wejscie(k, 54 + i * 6, 16), [0, 1], [12, 0])}px)`,
            }}
          >
            {c}
          </div>
        ))}
      </div>
    </AbsoluteFill>
  );
};

// ───────────────────────────────────────────── karta tytułowa modułu

const TytulModulu: React.FC<{ s: Extract<Scena, { typ: 'tytulModulu' }> }> = ({ s }) => {
  const k = useCurrentFrame();
  return (
    <AbsoluteFill style={{ justifyContent: 'center', paddingLeft: KADR.margines, paddingRight: KADR.margines }}>
      <div style={{ display: 'flex', alignItems: 'baseline', gap: 26, opacity: wejscie(k, 0, 20) }}>
        <div style={{ fontFamily: KROJ, fontSize: 150, fontWeight: 700, color: KOLOR.wypelnienie, lineHeight: 0.9 }}>
          {s.numer}
        </div>
        <div style={{ fontFamily: KROJ, fontSize: 24, letterSpacing: 4, color: KOLOR.pomarancz, fontWeight: 700 }}>
          CZĘŚĆ {s.numer} · {s.czas}
        </div>
      </div>
      <div
        style={{
          fontFamily: KROJ,
          fontSize: 74,
          fontWeight: 700,
          color: KOLOR.fiolet,
          marginTop: 6,
          maxWidth: 1400,
          lineHeight: 1.1,
          opacity: wejscie(k, 12, 24),
          transform: `translateY(${interpolate(wejscie(k, 12, 24), [0, 1], [20, 0])}px)`,
        }}
      >
        {s.tytul}
      </div>
      <div style={{ width: interpolate(wejscie(k, 26, 20), [0, 1], [0, 220]), height: 5, background: KOLOR.pomarancz, margin: '28px 0 24px', borderRadius: 3 }} />
      <div style={{ fontFamily: KROJ, fontSize: 32, color: KOLOR.szary, maxWidth: 1300, lineHeight: 1.36, opacity: wejscie(k, 34, 22) }}>
        {s.podtytul}
      </div>
    </AbsoluteFill>
  );
};

// ───────────────────────────────────────────── punkty

const Punkty: React.FC<{ s: Extract<Scena, { typ: 'punkty' }>; etykieta: string }> = ({ s, etykieta }) => {
  const k = useCurrentFrame();
  const duzo = s.punkty.length >= 5;
  return (
    <AbsoluteFill>
      <NaglowekSceny etykieta={etykieta} nadtytul={s.nadtytul} tytul={s.naglowek} />
      <div style={{ position: 'absolute', top: OBSZAR.top + 60, left: OBSZAR.left, right: OBSZAR.right }}>
        {s.punkty.map((p, i) => {
          const start = 26 + i * 15;
          const w = wejscie(k, start, 20);
          return (
            <div
              key={i}
              style={{
                display: 'flex',
                gap: 24,
                alignItems: 'flex-start',
                marginBottom: duzo ? 24 : 34,
                opacity: w,
                transform: `translateX(${interpolate(w, [0, 1], [-26, 0])}px)`,
              }}
            >
              <div
                style={{
                  minWidth: 46,
                  height: 46,
                  borderRadius: 12,
                  background: KOLOR.fiolet,
                  color: '#fff',
                  fontFamily: KROJ,
                  fontWeight: 700,
                  fontSize: 22,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  marginTop: 6,
                }}
              >
                {i + 1}
              </div>
              <div style={{ fontFamily: KROJ, fontSize: duzo ? 34 : 39, lineHeight: 1.36, maxWidth: 1440 }}>
                <Zakreslany tekst={p} start={start} />
              </div>
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

// ───────────────────────────────────────────── cytat z przepisu

const Cytat: React.FC<{ s: Extract<Scena, { typ: 'cytat' }>; etykieta: string }> = ({ s, etykieta }) => {
  const k = useCurrentFrame();
  const w = wejscie(k, 16, 26);
  return (
    <AbsoluteFill>
      <NaglowekSceny etykieta={etykieta} tytul={s.naglowek} />
      <div
        style={{
          position: 'absolute',
          top: OBSZAR.top + 40,
          left: OBSZAR.left,
          right: OBSZAR.right,
          background: KOLOR.kartka,
          border: `1px solid ${KOLOR.ramka}`,
          borderLeft: `10px solid ${KOLOR.pomarancz}`,
          borderRadius: 18,
          padding: '46px 56px 42px',
          boxShadow: '0 22px 60px rgba(45,27,105,0.10)',
          opacity: w,
          transform: `scale(${interpolate(w, [0, 1], [0.972, 1])})`,
        }}
      >
        <div
          style={{
            position: 'absolute',
            top: -34,
            right: 44,
            fontFamily: KROJ,
            fontSize: 150,
            color: KOLOR.wypelnienie,
            fontWeight: 700,
            lineHeight: 1,
          }}
        >
          §
        </div>
        <div style={{ fontFamily: KROJ, fontSize: 40, lineHeight: 1.44, color: KOLOR.atrament, position: 'relative' }}>
          <Zakreslany tekst={s.tresc} start={26} />
        </div>
        <div style={{ marginTop: 34, fontFamily: KROJ, fontSize: 25, color: KOLOR.szary, letterSpacing: 0.6 }}>
          {s.zrodlo}
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ───────────────────────────────────────────── tabela

const Tabela: React.FC<{ s: Extract<Scena, { typ: 'tabela' }>; etykieta: string }> = ({ s, etykieta }) => {
  const k = useCurrentFrame();
  const kolumny = s.naglowki.length;
  const szer = s.szerokosci ?? Array(kolumny).fill(100 / kolumny);
  const wysoko = s.wiersze.length > 5;
  return (
    <AbsoluteFill>
      <NaglowekSceny etykieta={etykieta} nadtytul={s.nadtytul} tytul={s.naglowek} />
      <div style={{ position: 'absolute', top: OBSZAR.top + 46, left: OBSZAR.left, right: OBSZAR.right }}>
        <div
          style={{
            display: 'flex',
            background: KOLOR.fiolet,
            borderRadius: '12px 12px 0 0',
            overflow: 'hidden',
            opacity: wejscie(k, 18, 16),
          }}
        >
          {s.naglowki.map((n, i) => (
            <div
              key={i}
              style={{
                width: `${szer[i]}%`,
                padding: '18px 24px',
                fontFamily: KROJ,
                fontSize: 23,
                letterSpacing: 1.4,
                color: '#fff',
                fontWeight: 700,
              }}
            >
              {n}
            </div>
          ))}
        </div>
        {s.wiersze.map((wiersz, r) => {
          const start = 30 + r * 13;
          const w = wejscie(k, start, 18);
          return (
            <div
              key={r}
              style={{
                display: 'flex',
                background: r % 2 ? KOLOR.wypelnienie2 : KOLOR.kartka,
                borderLeft: `1px solid ${KOLOR.ramka}`,
                borderRight: `1px solid ${KOLOR.ramka}`,
                borderBottom: `1px solid ${KOLOR.ramka}`,
                opacity: w,
                transform: `translateY(${interpolate(w, [0, 1], [10, 0])}px)`,
              }}
            >
              {wiersz.map((komorka, c) => (
                <div
                  key={c}
                  style={{
                    width: `${szer[c]}%`,
                    padding: wysoko ? '14px 24px' : '20px 24px',
                    fontFamily: KROJ,
                    fontSize: wysoko ? 25 : 29,
                    lineHeight: 1.32,
                    color: c === 0 ? KOLOR.fiolet : KOLOR.atrament,
                    fontWeight: c === 0 ? 700 : 400,
                  }}
                >
                  <Zakreslany tekst={komorka} start={start} kolor={c === 0 ? KOLOR.fiolet : KOLOR.atrament} />
                </div>
              ))}
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

// ───────────────────────────────────────────── druk / zrzut z aplikacji

const Druk: React.FC<{ s: Extract<Scena, { typ: 'druk' }>; etykieta: string }> = ({ s, etykieta }) => {
  const k = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const p = interpolate(k, [0, Math.max(durationInFrames, 1)], [0, 1]);
  const kad = s.kadrowanie;
  // Ken Burns: kartka wjeżdża w całości, potem powolny najazd na wskazany fragment
  const skala = interpolate(p, [0, 1], [1.0, kad ? kad.skala : 1.09]);
  const x = kad ? interpolate(p, [0, 1], [0, kad.x]) : 0;
  const y = kad ? interpolate(p, [0, 1], [0, kad.y]) : interpolate(p, [0, 1], [0, -34]);
  const w = wejscie(k, 8, 24);
  return (
    <AbsoluteFill>
      <NaglowekSceny etykieta={etykieta} nadtytul={s.nadtytul} tytul={s.naglowek} />
      <div
        style={{
          position: 'absolute',
          top: 292,
          left: OBSZAR.left,
          right: OBSZAR.right,
          height: 540,
          borderRadius: 16,
          overflow: 'hidden',
          border: `1px solid ${KOLOR.ramka}`,
          boxShadow: '0 26px 70px rgba(45,27,105,0.16)',
          background: KOLOR.kartka,
          opacity: w,
        }}
      >
        <Img
          src={staticFile(s.plik)}
          style={{
            width: '100%',
            transform: `scale(${skala}) translate(${x}px, ${y}px)`,
            transformOrigin: '50% 0%',
          }}
        />
        {s.opis ? (
          <div
            style={{
              position: 'absolute',
              left: 0,
              right: 0,
              bottom: 0,
              padding: '46px 30px 16px',
              background: 'linear-gradient(transparent, rgba(255,255,255,0.94) 58%)',
              fontFamily: KROJ,
              fontSize: 23,
              color: KOLOR.szary,
              opacity: wejscie(k, 30, 20),
            }}
          >
            {s.opis}
          </div>
        ) : null}
      </div>
    </AbsoluteFill>
  );
};

// ───────────────────────────────────────────── dwie ścieżki

const Sciezki: React.FC<{ s: Extract<Scena, { typ: 'sciezki' }>; etykieta: string }> = ({ s, etykieta }) => {
  const k = useCurrentFrame();
  const kolumna = (
    dane: { tytul: string; kroki: string[] },
    kolor: string,
    opoznienie: number,
  ) => (
    <div
      style={{
        flex: 1,
        background: KOLOR.kartka,
        border: `1px solid ${KOLOR.ramka}`,
        borderTop: `6px solid ${kolor}`,
        borderRadius: 16,
        padding: '30px 34px 34px',
        boxShadow: '0 18px 48px rgba(45,27,105,0.08)',
        opacity: wejscie(k, opoznienie, 22),
        transform: `translateY(${interpolate(wejscie(k, opoznienie, 22), [0, 1], [22, 0])}px)`,
      }}
    >
      <div style={{ fontFamily: KROJ, fontSize: 34, fontWeight: 700, color: kolor, marginBottom: 22 }}>
        {dane.tytul}
      </div>
      {dane.kroki.map((krok, i) => (
        <div
          key={i}
          style={{
            fontFamily: KROJ,
            fontSize: 27,
            color: KOLOR.atrament,
            lineHeight: 1.34,
            padding: '13px 0',
            borderBottom: i < dane.kroki.length - 1 ? `1px solid ${KOLOR.wypelnienie}` : 'none',
            opacity: wejscie(k, opoznienie + 14 + i * 10, 16),
          }}
        >
          <span style={{ color: kolor, fontWeight: 700, marginRight: 12 }}>{i + 1}</span>
          {krok}
        </div>
      ))}
    </div>
  );
  return (
    <AbsoluteFill>
      <NaglowekSceny etykieta={etykieta} tytul={s.naglowek} />
      <div style={{ position: 'absolute', top: OBSZAR.top + 46, left: OBSZAR.left, right: OBSZAR.right, display: 'flex', gap: 40 }}>
        {kolumna(s.lewa, KOLOR.fiolet, 22)}
        {kolumna(s.prawa, KOLOR.pomarancz, 34)}
      </div>
    </AbsoluteFill>
  );
};

// ───────────────────────────────────────────── obieg dokumentów

const Obieg: React.FC<{ s: Extract<Scena, { typ: 'obieg' }>; etykieta: string }> = ({ s, etykieta }) => {
  const k = useCurrentFrame();
  const n = s.przystanki.length;
  return (
    <AbsoluteFill>
      <NaglowekSceny etykieta={etykieta} tytul={s.naglowek} />
      <div style={{ position: 'absolute', top: OBSZAR.top + 96, left: OBSZAR.left, right: OBSZAR.right }}>
        <div style={{ position: 'relative', height: 6, background: KOLOR.wypelnienie, borderRadius: 3, marginBottom: 44 }}>
          <div
            style={{
              position: 'absolute',
              left: 0,
              top: 0,
              bottom: 0,
              width: `${interpolate(wejscie(k, 18, n * 14), [0, 1], [0, 100])}%`,
              background: `linear-gradient(90deg, ${KOLOR.fiolet}, ${KOLOR.pomarancz})`,
              borderRadius: 3,
            }}
          />
        </div>
        <div style={{ display: 'flex', gap: 20 }}>
          {s.przystanki.map((p, i) => {
            const start = 22 + i * 13;
            const w = wejscie(k, start, 18);
            return (
              <div
                key={i}
                style={{
                  flex: 1,
                  background: KOLOR.kartka,
                  border: `1px solid ${KOLOR.ramka}`,
                  borderRadius: 14,
                  padding: '22px 20px 24px',
                  opacity: w,
                  transform: `translateY(${interpolate(w, [0, 1], [24, 0])}px)`,
                  boxShadow: '0 14px 36px rgba(45,27,105,0.07)',
                }}
              >
                <div
                  style={{
                    width: 40,
                    height: 40,
                    borderRadius: 10,
                    background: KOLOR.pomarancz,
                    color: '#fff',
                    fontFamily: KROJ,
                    fontWeight: 700,
                    fontSize: 20,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    marginBottom: 16,
                  }}
                >
                  {i + 1}
                </div>
                <div style={{ fontFamily: KROJ, fontSize: 25, fontWeight: 700, color: KOLOR.fiolet, lineHeight: 1.24, marginBottom: 10 }}>
                  {p.nazwa}
                </div>
                <div style={{ fontFamily: KROJ, fontSize: 20, color: KOLOR.szary, lineHeight: 1.34 }}>{p.opis}</div>
              </div>
            );
          })}
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ───────────────────────────────────────────── domknięcie modułu

const Domkniecie: React.FC<{ s: Extract<Scena, { typ: 'domkniecie' }>; etykieta: string }> = ({ s, etykieta }) => {
  const k = useCurrentFrame();
  return (
    <AbsoluteFill>
      <NaglowekSceny etykieta={etykieta} tytul={s.naglowek} />
      <div style={{ position: 'absolute', top: OBSZAR.top + 70, left: OBSZAR.left, right: OBSZAR.right }}>
        {s.zdania.map((z, i) => {
          const start = 24 + i * 20;
          const w = wejscie(k, start, 22);
          return (
            <div
              key={i}
              style={{
                background: i === 1 ? KOLOR.wypelnienie : 'transparent',
                border: `1px solid ${i === 1 ? KOLOR.ramka : 'transparent'}`,
                borderRadius: 14,
                padding: i === 1 ? '26px 30px' : '26px 0',
                marginBottom: 18,
                fontFamily: KROJ,
                fontSize: 40,
                lineHeight: 1.34,
                opacity: w,
                transform: `translateY(${interpolate(w, [0, 1], [18, 0])}px)`,
              }}
            >
              <Zakreslany tekst={z} start={start} />
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

// ───────────────────────────────────────────── rozdzielacz

export const RysujScene: React.FC<{ scena: Scena; etykieta: string }> = ({ scena, etykieta }) => {
  const tresc = (() => {
    switch (scena.typ) {
      case 'czolowka':
        return <Czolowka s={scena} />;
      case 'tytulModulu':
        return <TytulModulu s={scena} />;
      case 'punkty':
        return <Punkty s={scena} etykieta={etykieta} />;
      case 'cytat':
        return <Cytat s={scena} etykieta={etykieta} />;
      case 'tabela':
        return <Tabela s={scena} etykieta={etykieta} />;
      case 'druk':
        return <Druk s={scena} etykieta={etykieta} />;
      case 'sciezki':
        return <Sciezki s={scena} etykieta={etykieta} />;
      case 'obieg':
        return <Obieg s={scena} etykieta={etykieta} />;
      case 'domkniecie':
        return <Domkniecie s={scena} etykieta={etykieta} />;
    }
  })();
  // druk ma własny najazd na obrazek — drugi najazd na całości robiłby przesuw tekstu
  return scena.typ === 'druk' ? <>{tresc}</> : <Najazd>{tresc}</Najazd>;
};
