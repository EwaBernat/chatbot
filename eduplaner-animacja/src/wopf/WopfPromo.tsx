import React from 'react';
import {AbsoluteFill, Audio, Sequence, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from '../marka';
import {Napisy} from '../Napisy';
import {Logo, Pojaw, useWejscie} from '../ui';
import {OryginalnyDruk, type Krok, type Ujecie} from '../kpof/OryginalnyDruk';
import type {WopfKrok} from '../kpof/wopfResolver';
import dane from '../../public/wopf-dane.json';
import type {Napis} from '../typy';

export type FilmWopf = {audio: string | null; napisy: Napis[]; dlugosc: number};
export type Props = {film: FilmWopf};

const KROKI = (dane as {kroki: WopfKrok[]}).kroki;

/* ---------- plansze ---------- */
const Tlo: React.FC<{children: React.ReactNode}> = ({children}) => (
  <AbsoluteFill style={{background: `linear-gradient(160deg, ${MARKA.fioletCiemny} 0%, ${MARKA.fiolet} 55%, #3b2a86 100%)`, fontFamily: FONT}}>
    <div style={{position: 'absolute', left: 460, top: -100, width: 1000, height: 900, borderRadius: '50%', background: 'radial-gradient(circle, rgba(232,69,10,0.35) 0%, rgba(232,69,10,0) 60%)'}} />
    {children}
  </AbsoluteFill>
);

const Karta: React.FC<{od: number; children: React.ReactNode; style?: React.CSSProperties; akcent?: boolean}> = ({od, children, style, akcent}) => {
  const w = useWejscie(od, {damping: 13, stiffness: 110});
  return (
    <div style={{opacity: w, transform: `translateY(${(1 - w) * 30}px) scale(${0.94 + 0.06 * w})`, background: akcent ? MARKA.pomarancz : 'rgba(255,255,255,0.08)', border: `1.5px solid ${akcent ? MARKA.pomarancz : 'rgba(255,255,255,0.28)'}`, borderRadius: 18, padding: '22px 26px', color: '#fff', ...style}}>
      {children}
    </div>
  );
};

const WopfIntro: React.FC<{sciezki: number}> = ({sciezki}) => (
  <Tlo>
    <Pojaw od={0} style={{position: 'absolute', left: 0, right: 0, top: 110, textAlign: 'center'}}>
      <div style={{fontSize: 20, letterSpacing: 4, color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase'}}>EduPlaner 2026 · Ścieżka dziecka · przystanek czwarty</div>
      <div style={{fontSize: 66, fontWeight: 800, color: '#fff', marginTop: 12, letterSpacing: -1, lineHeight: 1.1}}>Wielospecjalistyczna Ocena<br />Poziomu Funkcjonowania</div>
      <div style={{display: 'inline-block', marginTop: 22, background: MARKA.pomarancz, color: '#fff', fontSize: 22, fontWeight: 700, padding: '10px 26px', borderRadius: 999, letterSpacing: 2}}>WOPF · DOKUMENT SCALAJĄCY · JEDEN DRUK, DWIE ŚCIEŻKI</div>
    </Pojaw>
    <div style={{position: 'absolute', left: 0, right: 0, top: 480, display: 'flex', justifyContent: 'center', gap: 50}}>
      <Karta od={sciezki} akcent style={{width: 640, boxShadow: '0 24px 60px rgba(232,69,10,0.45)'}}>
        <div style={{fontSize: 18, letterSpacing: 3, fontWeight: 700, color: 'rgba(255,255,255,0.85)'}}>ŚCIEŻKA A · DZIECKO Z ORZECZENIEM</div>
        <div style={{fontSize: 56, fontWeight: 800, lineHeight: 1.05, marginTop: 10}}>WOPF → IPET</div>
        <div style={{fontSize: 22, marginTop: 12, lineHeight: 1.4}}>orzeczenie o potrzebie kształcenia specjalnego · program do 30 września · ocena co najmniej dwa razy w roku</div>
      </Karta>
      <Karta od={sciezki + 10} style={{width: 640}}>
        <div style={{fontSize: 18, letterSpacing: 3, fontWeight: 700, color: '#F6A57E'}}>ŚCIEŻKA B · DZIECKO BEZ ORZECZENIA</div>
        <div style={{fontSize: 56, fontWeight: 800, lineHeight: 1.05, marginTop: 10}}>WOPF → plan pomocy pp</div>
        <div style={{fontSize: 22, marginTop: 12, lineHeight: 1.4, color: 'rgba(255,255,255,0.85)'}}>rozpoznanie potrzeb przez nauczycieli · formy, okres i wymiar pomocy ustala dyrektor</div>
      </Karta>
    </div>
  </Tlo>
);

const STRAZNIK: [string, string, string, 'ok' | 'popraw' | 'poza'][] = [
  ['Kształcenie specjalne (WOPF, IPET) — rozp. MEN z 9.08.2017', 'Dz.U. 2017 poz. 1578 (miejscami t.j. 2020 poz. 1309)', 't.j. Dz.U. 2020 poz. 1309 — cytuj tekst jednolity', 'popraw'],
  ['Pomoc psychologiczno-pedagogiczna — rozp. MEN z 9.08.2017', 'Dz.U. 2017 poz. 1591', 't.j. Dz.U. 2023 poz. 1798', 'popraw'],
  ['Prawo oświatowe — ustawa z 14.12.2016', 't.j. Dz.U. 2024 poz. 737', 't.j. Dz.U. 2026 poz. 820', 'popraw'],
  ['Orzeczenia i opinie zespołów orzekających', 'rozp. MEN z 7.09.2017 (Dz.U. 2017 poz. 1743)', 'rozp. ME z 2.03.2026 (Dz.U. 2026 poz. 428) — uchyliło akt z 2017; opinia w 10 dni (§ 7 ust. 3)', 'popraw'],
  ['Podstawa programowa wychowania przedszkolnego', 'Dz.U. 2017 poz. 356', 'rozp. ME z 11.03.2026 (Dz.U. 2026 poz. 378), od 1.09.2026 — 9 obszarów', 'popraw'],
  ['Dokumentacja przebiegu nauczania — rozp. MEN z 25.08.2017', 'Dz.U. 2017 poz. 1646', 't.j. Dz.U. 2024 poz. 50', 'popraw'],
  ['RODO — rozp. (UE) 2016/679: art. 5 ust. 1 lit. c, art. 9', 'zgodnie', 'zgodnie ze skryptem', 'ok'],
  ['Karta Nauczyciela · ustawa o opiece zdrowotnej nad uczniami · „ustawa Kamilka”', 'cytowane w druku', 'poza zakresem audytu skryptu — do sprawdzenia osobno (opieka zdrowotna: dotyczy uczniów, nie przedszkola)', 'poza'],
];

const Straznik: React.FC<{start: number; wiersze: number[]; uwaga: number}> = ({start, wiersze, uwaga}) => {
  const frame = useCurrentFrame();
  const tarcza = useWejscie(0, {damping: 10, stiffness: 120});
  const puls = 1 + 0.03 * Math.sin(frame / 8);
  const wu = useWejscie(uwaga);
  return (
    <Tlo>
      <div style={{position: 'absolute', left: 0, right: 0, top: 44, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 26}}>
        <div style={{width: 96, height: 96, borderRadius: '50%', background: MARKA.pomarancz, display: 'grid', placeItems: 'center', fontSize: 52, transform: `scale(${tarcza * puls})`, boxShadow: '0 16px 40px rgba(232,69,10,0.5)'}}>⚖</div>
        <Pojaw od={2}>
          <div style={{fontSize: 56, fontWeight: 800, color: '#fff', lineHeight: 1}}>Strażnik prawa</div>
          <div style={{fontSize: 20, color: 'rgba(255,255,255,0.75)', marginTop: 8, letterSpacing: 1.5}}>każdy przepis z druku sprawdzony ze skryptem szkolenia · wydanie 2 po audycie podstaw prawnych z 5.09.2026</div>
        </Pojaw>
      </div>
      <div style={{position: 'absolute', left: 90, right: 90, top: 190, background: 'rgba(255,255,255,0.07)', border: '1.5px solid rgba(255,255,255,0.25)', borderRadius: 20, overflow: 'hidden'}}>
        <div style={{display: 'grid', gridTemplateColumns: '1.35fr 1fr 1.45fr 150px', gap: 0, background: 'rgba(255,255,255,0.12)', padding: '12px 22px', fontSize: 15, letterSpacing: 2, color: '#F6A57E', fontWeight: 700}}>
          <div>AKT PRAWNY</div><div>W DRUKU WOPF</div><div>WG SKRYPTU (WYD. 2 PO AUDYCIE)</div><div style={{textAlign: 'center'}}>STATUS</div>
        </div>
        {STRAZNIK.map(([akt, druk, skrypt, st], i) => {
          const od = i < wiersze.length ? wiersze[i] : start + i * 14;
          const w = Math.max(0, Math.min(1, (frame - od) / 10));
          const kolor = st === 'ok' ? '#2E9E52' : st === 'popraw' ? MARKA.pomarancz : '#8B8698';
          return (
            <div key={akt} style={{display: 'grid', gridTemplateColumns: '1.35fr 1fr 1.45fr 150px', padding: '11px 22px', borderTop: '1px solid rgba(255,255,255,0.12)', opacity: w, transform: `translateX(${(1 - w) * -20}px)`, color: '#fff', fontSize: 19, lineHeight: 1.3}}>
              <div style={{fontWeight: 700, paddingRight: 14}}>{akt}</div>
              <div style={{color: 'rgba(255,255,255,0.8)', paddingRight: 14, textDecoration: st === 'popraw' ? 'line-through' : 'none', textDecorationColor: 'rgba(255,255,255,0.5)'}}>{druk}</div>
              <div style={{paddingRight: 14}}>{skrypt}</div>
              <div style={{textAlign: 'center'}}><span style={{display: 'inline-block', background: kolor, color: '#fff', fontWeight: 800, fontSize: 15, padding: '5px 12px', borderRadius: 999, letterSpacing: 1}}>{st === 'ok' ? '✓ ZGODNE' : st === 'popraw' ? '⚠ POPRAW' : '? SPRAWDŹ'}</span></div>
            </div>
          );
        })}
      </div>
      <div style={{position: 'absolute', left: 0, right: 0, bottom: 118, textAlign: 'center', opacity: wu, transform: `translateY(${(1 - wu) * 20}px)`}}>
        <span style={{display: 'inline-block', border: '2px solid #F6A57E', color: '#fff', borderRadius: 999, padding: '12px 30px', fontSize: 22, fontWeight: 700}}>
          Reguła ze skryptu: w każdym druku cytuj obowiązujący tekst jednolity, nie pierwotny publikator
        </span>
      </div>
    </Tlo>
  );
};

const WopfFinal: React.FC<{haslo: number}> = ({haslo}) => (
  <Tlo>
    <div style={{position: 'absolute', left: 0, right: 0, top: 220, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
      <Logo rozmiar={130} />
      <div style={{fontSize: 92, fontWeight: 800, color: '#fff', letterSpacing: -2, marginTop: 22, lineHeight: 1}}>EduPlaner <span style={{color: '#F6A57E'}}>2026</span></div>
      <Pojaw od={haslo}>
        <div style={{fontSize: 40, color: '#fff', fontWeight: 700, marginTop: 22}}>Mniej dokumentów. Więcej edukacji.</div>
      </Pojaw>
      <Pojaw od={haslo + 20}>
        <div style={{marginTop: 40, fontSize: 20, color: 'rgba(255,255,255,0.7)', letterSpacing: 2}}>WOPF WYPEŁNIONY NA ORYGINALNYM DRUKU · ZALECENIA Z ORZECZENIA · STRAŻNIK PRAWA</div>
        <div style={{marginTop: 12, fontSize: 19, color: 'rgba(255,255,255,0.6)', letterSpacing: 2, textAlign: 'center'}}>PCTP KOSZALIN · kontakt@eduplaner2026.pl · 662 888 403</div>
      </Pojaw>
    </div>
  </Tlo>
);

/* ---------- składanie ---------- */
const Przejscie: React.FC<{trwanie: number; children: React.ReactNode}> = ({trwanie, children}) => {
  const frame = useCurrentFrame();
  const o = Math.min(interpolate(frame, [0, 10], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}), interpolate(frame, [trwanie - 9, trwanie - 1], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}));
  return <AbsoluteFill style={{opacity: o, transform: `scale(${0.985 + 0.015 * o})`}}>{children}</AbsoluteFill>;
};

const PasekPostepu: React.FC = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  return <div style={{position: 'absolute', left: 0, bottom: 0, height: 6, width: `${(100 * frame) / durationInFrames}%`, background: MARKA.pomarancz}} />;
};

/** Kroki z wopf-dane.json ułożone w czasie: faza → (start, koniec) w sekundach filmu. */
const rozloz = (okna: Record<string, [number, number, number?]>, natychmiast: string[]): Krok[] => {
  const kroki: Krok[] = [];
  const grupy: Record<string, WopfKrok[]> = {};
  for (const k of KROKI) (grupy[k.faza ?? ''] ??= []).push(k);
  for (const f of natychmiast) for (const k of grupy[f] ?? []) kroki.push({sek: 0, typ: 'dane', krok: k, tempo: 100000});
  for (const [faza, [od, do_, tempo]] of Object.entries(okna)) {
    const g = grupy[faza] ?? [];
    const dt = g.length > 1 ? (do_ - od) / g.length : 0;
    g.forEach((k, i) => kroki.push({sek: od + i * dt, typ: 'dane', krok: k, tempo: tempo ?? 22}));
  }
  return kroki;
};

export const WopfPromo: React.FC<Props> = ({film}) => {
  const {fps} = useVideoConfig();
  const n = film.napisy;
  const z = (i: number) => n[i]?.odSek ?? i * 5;
  const kz = (i: number) => n[i]?.doSek ?? i * 5 + 4;
  const granica = (i: number) => (i <= 0 ? 0 : (kz(i - 1) + z(i)) / 2);
  const fr = (sek: number) => Math.round(sek * fps);
  const lok = (od: number) => (s: number) => Math.max(0, fr(s - od));
  const koniec = film.dlugosc;

  const drukOd = granica(2);
  const kroki = rozloz(
    {
      metryczka: [z(2) + 0.2, kz(2), 26],
      orzeczenie: [z(3) + 0.2, z(3) + 2.5, 40],
      sciezka: [z(4) + 0.3, kz(4) - 1, 30],
      zespol: [z(5) + 0.3, kz(5), 40],
      mapa: [z(6) + 0.2, kz(6) + 0.5, 40],
      kpof: [z(7) + 0.3, kz(7), 30],
      zalecenia: [z(12) + 0.3, z(12) + 0.4, 62],
      zajecia: [z(13) + 0.3, z(13) + 2.4, 30],
      decyzja: [z(13) + 3.0, kz(13), 40],
      ipet: [z(14) + 0.2, kz(14) + 0.4, 60],
    },
    ['med', 'abc', 'tom', 'mowa', 'sens', 'potrzeby', 'przyczyny', 'synteza', 'efekty', 'opinia'],
  );
  const kamera: Ujecie[] = [
    {sek: 0, selektor: '@1 .tt-h1', skala: 1.35, przesun: 120},
    {sek: z(2), selektor: '@1 .fields', skala: 1.55, przesun: 130},
    {sek: z(4), selektor: '@2 .checks', skala: 1.5, przesun: 150},
    {sek: z(5), selektor: '@2 table', skala: 1.5, przesun: 90},
    {sek: z(6), selektor: '@3 table', skala: 1.45, przesun: 140},
    {sek: z(7), selektor: '@5 table.qtab', skala: 1.5, przesun: 140},
    {sek: z(8), selektor: '@5 #cgSVG', skala: 1.45, przesun: 120},
    {sek: z(9), selektor: '@7 table', skala: 1.3, przesun: 300},
    {sek: z(10), selektor: '@9 table', skala: 1.4, przesun: 110},
    {sek: z(10) + 2.8, selektor: '@10 table', skala: 1.4, przesun: 140},
    {sek: z(10) + 5.6, selektor: '@11 table', skala: 1.4, przesun: 140},
    {sek: z(11), selektor: '@13 table', skala: 1.3, przesun: 300},
    {sek: z(11) + 3.8, selektor: '@14 table', skala: 1.35, przesun: 180},
    {sek: z(12), selektor: '@14 .ta', skala: 1.55, przesun: 110},
    {sek: z(13), selektor: '@15 .checks', skala: 1.5, przesun: 150},
    {sek: z(13) + 3.2, selektor: '@15 .fields', skala: 1.55, przesun: 40},
    {sek: z(14), selektor: '@17 table', skala: 1.32, przesun: 250},
  ];
  const wyr: Krok[] = [
    {sek: z(12) + 0.1, doSek: kz(12) + 0.3, typ: 'wyroznij', selektor: '@14 .ta'},
    {sek: z(8), doSek: kz(8) + 0.3, typ: 'wyroznij', selektor: '@5 #autoOpis'},
  ];

  type Scena = {id: string; od: number; do: number; el: (od: number) => React.ReactNode};
  const sceny: Scena[] = [
    {id: 'intro', od: 0, do: drukOd, el: (od) => <WopfIntro sciezki={lok(od)(z(1))} />},
    {id: 'druk', od: drukOd, do: granica(15), el: (od) => <OryginalnyDruk plik="wopf.html" kroki={[...kroki, ...wyr]} kamera={kamera} odSek={od} />},
    {id: 'straznik', od: granica(15), do: granica(23), el: (od) => <Straznik start={lok(od)(z(17))} wiersze={[17, 18, 19, 20, 21, 21, 22, 22].map((i, j) => lok(od)(z(i) + (j === 5 || j === 7 ? 3 : 0)))} uwaga={lok(od)(z(22) + 2)} />},
    {id: 'final', od: granica(23), do: koniec, el: (od) => <WopfFinal haslo={lok(od)(z(24))} />},
  ];

  return (
    <AbsoluteFill style={{background: MARKA.tlo}}>
      {film.audio ? <Audio src={staticFile(film.audio)} /> : null}
      {sceny.map((s) => {
        const od = fr(s.od);
        const trwanie = Math.max(1, fr(s.do) - od);
        return (
          <Sequence key={s.id} from={od} durationInFrames={trwanie} name={s.id}>
            <Przejscie trwanie={trwanie}>{s.el(s.od)}</Przejscie>
          </Sequence>
        );
      })}
      <Napisy napisy={n} />
      <PasekPostepu />
    </AbsoluteFill>
  );
};
