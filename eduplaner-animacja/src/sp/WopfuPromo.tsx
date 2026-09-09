import React from 'react';
import {AbsoluteFill, Audio, Sequence, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from '../marka';
import {Napisy} from '../Napisy';
import {Logo, Pojaw, useWejscie} from '../ui';
import {OryginalnyDruk, type Krok, type Ujecie} from '../kpof/OryginalnyDruk';
import type {Napis} from '../typy';
import krokiJson from '../../public/wopfu-kroki.json';

/** Film „Szkoła podstawowa · WOPF-SP” — narracja: dosłowne fragmenty skryptu (część 3: przystanek czwarty; część 7: pkt 03–08 i „Jak przygotować WOPF-SP”) + Strażnik prawa. */
export type FilmWopfu = {audio: string | null; napisy: Napis[]; dlugosc: number};
export type Props = {film: FilmWopfu};
type KrokJson = {sel: string; t?: string; k?: number};
const KROKI = krokiJson as unknown as KrokJson[];

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
    <div style={{opacity: w, transform: `translateY(${(1 - w) * 30}px) scale(${0.94 + 0.06 * w})`, background: akcent ? MARKA.pomarancz : 'rgba(255,255,255,0.08)', border: `1.5px solid ${akcent ? MARKA.pomarancz : 'rgba(255,255,255,0.28)'}`, borderRadius: 18, padding: '20px 24px', color: '#fff', ...style}}>
      {children}
    </div>
  );
};
const Naglowek: React.FC<{kicker: string; tytul: string; od?: number}> = ({kicker, tytul, od = 0}) => (
  <Pojaw od={od} style={{position: 'absolute', left: 0, right: 0, top: 64, textAlign: 'center'}}>
    <div style={{fontSize: 19, letterSpacing: 4, color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase'}}>{kicker}</div>
    <div style={{fontSize: 54, fontWeight: 800, color: '#fff', marginTop: 10, letterSpacing: -1, lineHeight: 1.1}}>{tytul}</div>
  </Pojaw>
);
const Kolo: React.FC<{n: string | number; kolor?: string; rozmiar?: number}> = ({n, kolor = MARKA.morski, rozmiar = 54}) => (
  <div style={{width: rozmiar, height: rozmiar, borderRadius: '50%', background: kolor, display: 'grid', placeItems: 'center', fontSize: rozmiar * 0.45, fontWeight: 800, flex: '0 0 auto', color: '#fff'}}>{n}</div>
);

const Intro: React.FC = () => (
  <Tlo>
    <Pojaw od={0} style={{position: 'absolute', left: 0, right: 0, top: 150, textAlign: 'center'}}>
      <div style={{fontSize: 20, letterSpacing: 4, color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase'}}>EduPlaner 2026 · Szkoła podstawowa · przystanek czwarty</div>
      <div style={{fontSize: 110, fontWeight: 800, color: '#fff', marginTop: 12, letterSpacing: -3, lineHeight: 1}}>WOPF<span style={{color: '#F6A57E'}}>-SP</span></div>
      <div style={{fontSize: 40, fontWeight: 700, color: '#fff', marginTop: 16, lineHeight: 1.2}}>Wielospecjalistyczna Ocena Poziomu Funkcjonowania Ucznia</div>
    </Pojaw>
    <Pojaw od={40} style={{position: 'absolute', left: 260, right: 260, top: 560}}>
      <Karta od={40} akcent style={{textAlign: 'center', fontSize: 30, fontWeight: 700, lineHeight: 1.4}}>Ocena scalająca — jeden druk, który zbiera wyniki z druków wcześniejszych</Karta>
      <Karta od={70} style={{marginTop: 22, textAlign: 'center', fontSize: 24, lineHeight: 1.45}}>metryczka → kwestionariusz KSzOF → obserwacja pogłębiona → <b>WOPF-SP</b> → IPET albo plan wsparcia</Karta>
    </Pojaw>
  </Tlo>
);

const ZRODLA_SCALA = ['profil z kwestionariusza', 'wnioski z obserwacji pogłębionej', 'treść orzeczenia lub opinii poradni', 'informacje od rodziców', 'głos ucznia', 'efekty dotychczasowego wsparcia'];
const Scala: React.FC<{lista: number; jezyk: number; opis: number}> = ({lista, jezyk, opis}) => (
  <Tlo>
    <Naglowek kicker="Przystanek czwarty · ocena scalająca" tytul="Ocena scala wszystko, co zebraliśmy wcześniej" />
    <div style={{position: 'absolute', left: 120, right: 120, top: 225, display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 18}}>
      {ZRODLA_SCALA.map((t, i) => (
        <Karta key={t} od={lista + i * 6} style={{display: 'flex', alignItems: 'center', gap: 16, padding: '16px 20px'}}>
          <Kolo n={i + 1} rozmiar={48} />
          <div style={{fontSize: 24, fontWeight: 700, lineHeight: 1.2}}>{t}</div>
        </Karta>
      ))}
    </div>
    <div style={{position: 'absolute', left: 120, right: 120, top: 560}}>
      <Karta od={jezyk} akcent style={{textAlign: 'center', fontSize: 27, fontWeight: 700, lineHeight: 1.4}}>Język funkcjonalny: <b>co uczeń robi</b> · <b>w jakich warunkach</b> · <b>przy jakim wsparciu</b></Karta>
      <Karta od={opis} style={{marginTop: 22, textAlign: 'center', fontSize: 25, lineHeight: 1.4, borderColor: '#F6A57E'}}>mocne strony · trudności · bariery i ułatwienia w środowisku</Karta>
    </div>
  </Tlo>
);

const Rozgalezienie: React.FC<{sekcja: number; ipet: number; pwes: number; jeden: number}> = ({sekcja, ipet, pwes, jeden}) => (
  <Tlo>
    <Naglowek kicker="Rozgałęzienie z modułu pierwszego" tytul="Sekcja I a — wybór ścieżki" />
    <Karta od={sekcja} style={{position: 'absolute', left: 260, right: 260, top: 215, textAlign: 'center', fontSize: 26, lineHeight: 1.4}}>Sekcja pierwsza a druku oceny każe wybrać ścieżkę dokumentacyjną.</Karta>
    <div style={{position: 'absolute', left: 140, right: 140, top: 360, display: 'flex', gap: 26}}>
      <Karta od={ipet} akcent style={{flex: 1, textAlign: 'center', padding: '34px 24px'}}>
        <div style={{fontSize: 20, letterSpacing: 3, fontWeight: 800, color: 'rgba(255,255,255,0.85)'}}>UCZEŃ Z ORZECZENIEM</div>
        <div style={{fontSize: 44, fontWeight: 800, marginTop: 10}}>IPET</div>
        <div style={{fontSize: 23, marginTop: 8, lineHeight: 1.3}}>indywidualny program edukacyjno-terapeutyczny</div>
      </Karta>
      <Karta od={pwes} style={{flex: 1, textAlign: 'center', padding: '34px 24px'}}>
        <div style={{fontSize: 20, letterSpacing: 3, color: '#F6A57E', fontWeight: 800}}>UCZEŃ BEZ ORZECZENIA</div>
        <div style={{fontSize: 44, fontWeight: 800, marginTop: 10}}>PWES</div>
        <div style={{fontSize: 23, marginTop: 8, lineHeight: 1.3, color: 'rgba(255,255,255,0.85)'}}>plan wsparcia edukacyjnego w ramach pomocy psychologiczno-pedagogicznej</div>
      </Karta>
    </div>
    <Karta od={jeden} style={{position: 'absolute', left: 360, right: 360, top: 720, textAlign: 'center', fontSize: 34, fontWeight: 800}}>Jeden druk, dwie ścieżki.</Karta>
  </Tlo>
);

const Podstawa: React.FC<{rozp: number; dwa: number}> = ({rozp, dwa}) => (
  <Tlo>
    <Naglowek kicker="Zaczynamy od wielospecjalistycznej oceny" tytul="Podstawa prawna oceny" />
    <Karta od={rozp} akcent style={{position: 'absolute', left: 200, right: 200, top: 230, textAlign: 'center', fontSize: 28, fontWeight: 700, lineHeight: 1.4}}>
      Rozporządzenie MEN z 9 sierpnia 2017 r. w sprawie kształcenia specjalnego — § 6
      <div style={{fontSize: 21, fontWeight: 400, marginTop: 8, color: 'rgba(255,255,255,0.9)'}}>tekst jednolity Dz.U. 2020 poz. 1309 · Prawo oświatowe, art. 127 (t.j. Dz.U. 2026 poz. 820)</div>
    </Karta>
    <div style={{position: 'absolute', left: 200, right: 200, top: 470, display: 'flex', gap: 26}}>
      <Karta od={dwa} style={{flex: 1, textAlign: 'center', padding: '30px 24px'}}>
        <div style={{fontSize: 64, fontWeight: 800, color: '#F6A57E', lineHeight: 1}}>2×</div>
        <div style={{fontSize: 25, marginTop: 10, lineHeight: 1.3}}>zespół dokonuje oceny <b>co najmniej dwa razy</b> w roku szkolnym (§ 6 ust. 9)</div>
      </Karta>
      <Karta od={dwa + 8} style={{flex: 1, textAlign: 'center', padding: '30px 24px'}}>
        <div style={{fontSize: 64, fontWeight: 800, color: '#F6A57E', lineHeight: 1}}>§ 6 ust. 4</div>
        <div style={{fontSize: 25, marginTop: 10, lineHeight: 1.3}}>ocena jest <b>podstawą opracowania i modyfikacji</b> programu</div>
      </Karta>
    </div>
  </Tlo>
);

const POWODY: [string, string][] = [
  ['Wyznacza punkt startu', 'bez niego cele byłyby zgadywaniem'],
  ['Scala perspektywy', 'wychowawcy, nauczycieli przedmiotów, logopedy, psychologa i rodziców — w jeden obraz ucznia'],
  ['Chroni ucznia przed etykietą', 'dwoje uczniów z tym samym orzeczeniem otrzymuje dwie różne oceny'],
  ['Dokumentuje pracę szkoły', 'ocena jest zapisem tego, co zespół zobaczył i zaplanował'],
];
const Dlaczego: React.FC<{od: number[]}> = ({od}) => (
  <Tlo>
    <Naglowek kicker="Cztery powody" tytul="Dlaczego ocena jest tak ważna?" />
    <div style={{position: 'absolute', left: 120, right: 120, top: 225, display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 22}}>
      {POWODY.map(([t, o], i) => (
        <Karta key={t} od={od[i]} style={{display: 'flex', gap: 20, alignItems: 'center', padding: '24px 26px', minHeight: 170}}>
          <Kolo n={i + 1} kolor={i % 2 ? MARKA.pomarancz : MARKA.morski} rozmiar={62} />
          <div>
            <div style={{fontSize: 30, fontWeight: 800, lineHeight: 1.15}}>{t}</div>
            <div style={{fontSize: 22, marginTop: 8, color: 'rgba(255,255,255,0.85)', lineHeight: 1.35}}>{o}</div>
          </div>
        </Karta>
      ))}
    </div>
  </Tlo>
);

const ZRODLA: [string, string][] = [
  ['Mocne strony', 'oceny najwyższe w kwestionariuszu KSzOF'],
  ['Trudności', 'oceny najniższe + obserwacja pogłębiona'],
  ['Bariery i ułatwienia', 'analiza ABC + profil sensoryczny'],
  ['Efekty wsparcia', 'poprzednia karta ewaluacji'],
  ['Głos ucznia', 'ankieta „Mój głos”'],
];
const Zrodla: React.FC<{od: number[]}> = ({od}) => (
  <Tlo>
    <Naglowek kicker="Każdy blok ma swoje źródło" tytul="Skąd biorą się zapisy w ocenie" />
    <div style={{position: 'absolute', left: 150, right: 150, top: 220, display: 'flex', flexDirection: 'column', gap: 16}}>
      {ZRODLA.map(([co, skad], i) => (
        <Karta key={co} od={od[i]} style={{display: 'grid', gridTemplateColumns: '360px 60px 1fr', alignItems: 'center', padding: '16px 26px', gap: 10}}>
          <div style={{fontSize: 28, fontWeight: 800, color: '#F6A57E'}}>{co}</div>
          <div style={{fontSize: 34, textAlign: 'center', color: 'rgba(255,255,255,0.7)'}}>←</div>
          <div style={{fontSize: 26, lineHeight: 1.3}}>{skad}</div>
        </Karta>
      ))}
    </div>
  </Tlo>
);

const PRAWO: [string, string, string][] = [
  ['§ 6 rozp. MEN z 9.08.2017 r. — kształcenie specjalne', 'podstawa istnienia druku: ocena poprzedza IPET i jest jego podstawą (ust. 4), co najmniej 2× w roku (ust. 9), prawa rodziców do udziału i kopii (ust. 11–12) — t.j. Dz.U. 2020 poz. 1309', 'PODSTAWA'],
  ['Prawo oświatowe, art. 127', 'w druku było t.j. Dz.U. 2024 poz. 737 — obowiązuje t.j. Dz.U. 2026 poz. 820', 'POPRAWIONO'],
  ['Rozp. o kształceniu specjalnym — publikator', 'pierwotny Dz.U. 2017 poz. 1578 (5 miejsc) → wyłącznie t.j. Dz.U. 2020 poz. 1309', 'POPRAWIONO'],
  ['Rozp. o pomocy psychologiczno-pedagogicznej', 'Dz.U. 2017 poz. 1591 i t.j. 2020 poz. 1280 (3 miejsca) → t.j. Dz.U. 2023 poz. 1798', 'POPRAWIONO'],
  ['Rozp. ME z 2.03.2026 r. o orzeczeniach i opiniach', 'opis funkcjonowania wg ICF, opinia dla poradni w 10 dni — Dz.U. 2026 poz. 428', 'ZGODNE'],
  ['Skrypt (23 sekcje) a druk autorki (I–XIX, 21 stron)', 'numeracja sekcji obserwacji pogłębionej według druku: X ABC · XI sensoryka · XII ToM · XII b mowa', 'UWAGA'],
];
const Straznik: React.FC<{od: number[]}> = ({od}) => {
  const frame = useCurrentFrame();
  const tarcza = useWejscie(0, {damping: 10, stiffness: 120});
  return (
    <Tlo>
      <div style={{position: 'absolute', left: 0, right: 0, top: 40, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 26}}>
        <div style={{width: 96, height: 96, borderRadius: '50%', background: MARKA.pomarancz, display: 'grid', placeItems: 'center', fontSize: 52, transform: `scale(${tarcza * (1 + 0.03 * Math.sin(frame / 8))})`, boxShadow: '0 16px 40px rgba(232,69,10,0.5)'}}>⚖</div>
        <Pojaw od={2}>
          <div style={{fontSize: 56, fontWeight: 800, color: '#fff', lineHeight: 1}}>Strażnik prawa · WOPF-SP</div>
          <div style={{fontSize: 20, color: 'rgba(255,255,255,0.75)', marginTop: 8, letterSpacing: 1.5}}>podstawa istnienia druku i publikatory — sprawdzone ze skryptem szkolenia dla szkoły podstawowej (części 3 i 7)</div>
        </Pojaw>
      </div>
      <div style={{position: 'absolute', left: 90, right: 90, top: 180, background: 'rgba(255,255,255,0.07)', border: '1.5px solid rgba(255,255,255,0.25)', borderRadius: 20, overflow: 'hidden'}}>
        {PRAWO.map(([a, b, c], i) => {
          const w = Math.max(0, Math.min(1, (frame - od[i]) / 10));
          const kolor = c === 'POPRAWIONO' ? MARKA.pomarancz : c === 'UWAGA' ? '#b8860b' : '#2F8F8A';
          return (
            <div key={a} style={{display: 'grid', gridTemplateColumns: '1fr 2.3fr 170px', padding: '15px 26px', borderTop: i ? '1px solid rgba(255,255,255,0.12)' : 'none', opacity: w, transform: `translateX(${(1 - w) * -20}px)`, color: '#fff', fontSize: 21.5, lineHeight: 1.32, alignItems: 'center', gap: 20}}>
              <div style={{fontWeight: 800}}>{a}</div>
              <div style={{color: 'rgba(255,255,255,0.9)'}}>{b}</div>
              <div style={{textAlign: 'center'}}><span style={{display: 'inline-block', background: kolor, color: '#fff', fontWeight: 800, fontSize: 15, padding: '6px 14px', borderRadius: 999}}>{c}</span></div>
            </div>
          );
        })}
      </div>
    </Tlo>
  );
};

const Final: React.FC<{haslo: number; logo: number}> = ({haslo, logo}) => (
  <Tlo>
    <div style={{position: 'absolute', left: 0, right: 0, top: 150, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
      <Pojaw od={0}><div style={{fontSize: 56, fontWeight: 800, color: '#fff', textAlign: 'center', lineHeight: 1.2}}>Ocena scala wszystko,<br />co zebraliśmy wcześniej.</div></Pojaw>
      <Pojaw od={logo} style={{marginTop: 50, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
        <Logo rozmiar={120} />
        <div style={{fontSize: 84, fontWeight: 800, color: '#fff', letterSpacing: -2, marginTop: 18, lineHeight: 1}}>EduPlaner <span style={{color: '#F6A57E'}}>2026</span></div>
      </Pojaw>
      <Pojaw od={haslo}>
        <div style={{fontSize: 38, color: '#fff', fontWeight: 700, marginTop: 22}}>Mniej dokumentów. Więcej edukacji.</div>
        <div style={{marginTop: 30, fontSize: 19, color: 'rgba(255,255,255,0.7)', letterSpacing: 2, textAlign: 'center'}}>SZKOŁA PODSTAWOWA · WOPF-SP · SKRYPT CZĘŚĆ 3 I 7 · STRAŻNIK PRAWA<br />PCTP KOSZALIN · kontakt@eduplaner2026.pl · 662 888 403</div>
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

const CSS_FILMU = [
  '.addrow,.delrow,.delcell,.printcell{display:none!important}',
  '.druk-oryginalny .sheet{box-shadow:0 10px 40px rgba(45,27,105,0.18)}',
  '.druk-oryginalny .blankline,.druk-oryginalny .blank{height:auto!important;min-height:15px;overflow-wrap:anywhere;white-space:normal;display:block;max-width:100%;box-sizing:border-box}',
  '.druk-oryginalny .dline{display:block!important;width:100%!important;min-width:0!important;height:auto!important;min-height:15px;overflow-wrap:anywhere;white-space:normal}',
  '.druk-oryginalny .fg .v,.druk-oryginalny .field .val,.druk-oryginalny td.ex,.druk-oryginalny .box{overflow-wrap:anywhere;white-space:normal}',
  '.druk-oryginalny [data-anim-tekst]{color:#2b2733!important}',
].join('\n');

const arkusz = (sel: string) => Number(/^@(\d+)/.exec(sel)?.[1] ?? 0);

export const WopfuPromo: React.FC<Props> = ({film}) => {
  const {fps} = useVideoConfig();
  const n = film.napisy;
  const z = (i: number) => n[i]?.odSek ?? i * 5;
  const kz = (i: number) => n[i]?.doSek ?? i * 5 + 4;
  const granica = (i: number) => (i <= 0 ? 0 : (kz(i - 1) + z(i)) / 2);
  const fr = (sek: number) => Math.round(sek * fps);
  const lok = (od: number) => (s: number) => Math.max(0, fr(s - od));
  const koniec = film.dlugosc;
  const L = (od: number) => lok(od);

  // --- przegląd druku (zdania 18–27): pusty druk, kamera prowadzi po sekcjach
  const przegladKamera: Ujecie[] = [
    {sek: 0, selektor: '@1 .sec #0', skala: 1.45, przesun: -60},
    {sek: z(19), selektor: '@7 table.tbl', skala: 1.75, przesun: 150},
    {sek: z(20), selektor: '@1 .sec #0', skala: 1.8, przesun: 140},
    {sek: z(20) + 6.5, selektor: '@1 .sec #1', skala: 1.9, przesun: 70},
    {sek: z(21), selektor: '@1 #tblZespol', skala: 1.9, przesun: 60},
    {sek: z(21) + 3, selektor: '@2 #gNarzedzia', skala: 1.8, przesun: 90},
    {sek: z(21) + 6, selektor: '@3 #gMedyczne', skala: 1.8, przesun: 100},
    {sek: z(22), selektor: '@4 table.tbl', skala: 1.8, przesun: 210},
    {sek: z(22) + 5, selektor: '@5 table.tbl', skala: 1.75, przesun: 230},
    {sek: z(23), selektor: '@10 table.tbl', skala: 1.8, przesun: 150},
    {sek: z(23) + 3, selektor: '@12 table.tbl', skala: 1.8, przesun: 140},
    {sek: z(23) + 6, selektor: '@13 table.tbl', skala: 1.75, przesun: 200},
    {sek: z(23) + 8.7, selektor: '@11 table.tbl', skala: 1.75, przesun: 200},
    {sek: z(24), selektor: '@6 .box #0', skala: 1.75, przesun: 170},
    {sek: z(24) + 5, selektor: '@7 table.tbl', skala: 1.75, przesun: 240},
    {sek: z(25), selektor: '@8 #gOsobyWsparcia', skala: 1.8, przesun: 170},
    {sek: z(26), selektor: '@16 .sec #0', skala: 1.75, przesun: 250},
    {sek: z(26) + 3.5, selektor: '@15 table.tbl', skala: 1.75, przesun: 220},
    {sek: z(27), selektor: '@18 .box #0', skala: 1.7, przesun: 200},
    {sek: z(27) + 4, selektor: '@19 .box #0', skala: 1.7, przesun: 190},
  ];

  // --- pełne wypełnianie (zdania 34–50): jedna scena, harmonogram arkuszy w sekundach filmu
  const T = {
    zespol: z(35) + 0.3, dane1: z(37) + 0.4, tryb1: z(37) + 7.2,
    s2opt: z(38) + 0.4, s2tbl: z(38) + 5.2, s3: z(40) + 0.3,
    s4: z(41) + 0.5, s5: z(42) + 0.3,
    s10: z(43) + 0.1, s12: z(43) + 2.6, s13: z(43) + 5.1, s11: z(43) + 7.6, s14: z(43) + 10.1,
    s6: z(44) + 0.1, s7: z(44) + 2.7,
    s9opt: z(45) + 0.1, s9box: z(46) + 0.1, s8: z(47) + 0.4,
    s16: z(48) + 0.1, s18: z(49) + 0.1, s19: z(49) + 3.3,
    s17: z(50) + 0.1, s15: z(50) + 1.9, s21: z(50) + 3.4,
  };

  const start = (k: KrokJson): number => {
    const a = arkusz(k.sel);
    if (/\.student \.blank/.test(k.sel)) return 0;
    if (a === 1) return /\.dline/.test(k.sel) ? T.zespol : /\.opt|\.fg \.v #4|\.blankline #4/.test(k.sel) ? T.tryb1 : T.dane1;
    if (a === 2) return /\.opt|\.blankline/.test(k.sel) ? T.s2opt : T.s2tbl;
    if (a === 9) return /\.opt/.test(k.sel) ? T.s9opt : T.s9box;
    const m: Record<number, number> = {3: T.s3, 4: T.s4, 5: T.s5, 6: T.s6, 7: T.s7, 8: T.s8, 10: T.s10, 11: T.s11, 12: T.s12, 13: T.s13, 14: T.s14, 15: T.s15, 16: T.s16, 17: T.s17, 18: T.s18, 19: T.s19, 21: T.s21};
    return m[a] ?? 0;
  };
  const ODSTEP: Record<number, number> = {1: 0.42, 2: 0.16, 3: 0.22, 4: 0.5, 5: 0.19, 6: 0.55, 7: 0.3, 8: 0.11, 9: 0.5, 10: 0.11, 11: 0.1, 12: 0.18, 13: 0.09, 14: 0.12, 15: 0.08, 16: 0.35, 17: 0.16, 18: 0.55, 19: 0.4, 21: 0.22};
  const TEMPO: Record<number, number> = {1: 45, 2: 110, 3: 120, 4: 30, 5: 150, 6: 230, 7: 230, 8: 260, 9: 220, 10: 220, 11: 260, 12: 200, 13: 260, 14: 260, 15: 300, 16: 260, 17: 320, 18: 320, 19: 320, 21: 60};
  const licznik: Record<string, number> = {};
  const wypKroki: Krok[] = KROKI.map((k): Krok => {
    const a = arkusz(k.sel);
    const s0 = start(k);
    const klucz = `${a}:${s0}`;
    const i = licznik[klucz] ?? 0;
    licznik[klucz] = i + 1;
    const sek = s0 === 0 ? 0 : s0 + i * (ODSTEP[a] ?? 0.2);
    if (k.k) return {sek, typ: 'klik', selektor: k.sel};
    return {sek, typ: 'tekst', selektor: k.sel, tekst: k.t ?? '', tempo: s0 === 0 ? 999 : TEMPO[a] ?? 120};
  });
  const wypKamera: Ujecie[] = [
    {sek: 0, selektor: '@1 #tblZespol', skala: 1.9, przesun: 60},
    {sek: z(37), selektor: '@1 .sec #0', skala: 1.8, przesun: 150, czas: 0.7},
    {sek: T.tryb1 - 0.3, selektor: '@1 .sec #1', skala: 1.9, przesun: 70, czas: 0.7},
    {sek: z(38), selektor: '@2 #gKonteksty', skala: 1.8, przesun: 120, czas: 0.7},
    {sek: T.s2tbl - 0.3, selektor: '@2 #tblKontekst', skala: 1.8, przesun: 100, czas: 0.7},
    {sek: z(40), selektor: '@3 #gMedyczne', skala: 1.8, przesun: 180, czas: 0.7},
    {sek: z(41), selektor: '@4 table.tbl', skala: 1.8, przesun: 210, czas: 0.7},
    {sek: z(42), selektor: '@5 table.tbl', skala: 1.75, przesun: 240, czas: 0.7},
    {sek: T.s10 - 0.2, selektor: '@10 table.tbl', skala: 1.8, przesun: 150, czas: 0.7},
    {sek: T.s12 - 0.2, selektor: '@12 table.tbl', skala: 1.8, przesun: 150, czas: 0.7},
    {sek: T.s13 - 0.2, selektor: '@13 table.tbl', skala: 1.75, przesun: 210, czas: 0.7},
    {sek: T.s11 - 0.2, selektor: '@11 table.tbl', skala: 1.75, przesun: 200, czas: 0.7},
    {sek: T.s14 - 0.2, selektor: '@14 #gLogo', skala: 1.8, przesun: 160, czas: 0.7},
    {sek: z(44), selektor: '@6 .box #0', skala: 1.75, przesun: 190, czas: 0.7},
    {sek: T.s7 - 0.2, selektor: '@7 table.tbl', skala: 1.75, przesun: 250, czas: 0.7},
    {sek: z(45), selektor: '@9 #gCzynniki', skala: 1.8, przesun: 130, czas: 0.7},
    {sek: z(46), selektor: '@9 .box #0', skala: 1.9, przesun: 110, czas: 0.7},
    {sek: T.s8 - 0.2, selektor: '@8 #gOsobyWsparcia', skala: 1.75, przesun: 200, czas: 0.7},
    {sek: z(48), selektor: '@16 .sec #0', skala: 1.75, przesun: 250, czas: 0.7},
    {sek: z(49), selektor: '@18 .box #0', skala: 1.7, przesun: 200, czas: 0.7},
    {sek: T.s19 - 0.2, selektor: '@19 .box #0', skala: 1.7, przesun: 190, czas: 0.7},
    {sek: T.s17 - 0.2, selektor: '@17 .box #0', skala: 1.65, przesun: 190, czas: 0.7},
    {sek: T.s15 - 0.2, selektor: '@15 table.tbl', skala: 1.7, przesun: 220, czas: 0.7},
    {sek: T.s21 - 0.2, selektor: '@21 .sec #0', skala: 1.7, przesun: 250, czas: 0.7},
  ];

  type Scena = {id: string; od: number; do: number; el: (od: number) => React.ReactNode};
  const sceny: Scena[] = [
    {id: 'intro', od: 0, do: granica(1), el: () => <Intro />},
    {id: 'scala', od: granica(1), do: granica(5), el: (od) => <Scala lista={L(od)(z(2))} jezyk={L(od)(z(3))} opis={L(od)(z(4))} />},
    {id: 'rozgalezienie', od: granica(5), do: granica(10), el: (od) => <Rozgalezienie sekcja={L(od)(z(6))} ipet={L(od)(z(7))} pwes={L(od)(z(8))} jeden={L(od)(z(9))} />},
    {id: 'podstawa', od: granica(10), do: granica(13), el: (od) => <Podstawa rozp={L(od)(z(11))} dwa={L(od)(z(12))} />},
    {id: 'dlaczego', od: granica(13), do: granica(18), el: (od) => <Dlaczego od={[14, 15, 16, 17].map((i) => L(od)(z(i)))} />},
    {id: 'przeglad', od: granica(18), do: granica(28), el: (od) => <OryginalnyDruk plik="wopfu.html" kroki={[{sek: 0, typ: 'tekst', selektor: '@1 .fg .v #1', tekst: '14.03.2017', tempo: 999}]} kamera={przegladKamera} odSek={od} css={CSS_FILMU} />},
    {id: 'zrodla', od: granica(28), do: granica(34), el: (od) => <Zrodla od={[29, 30, 31, 32, 33].map((i) => L(od)(z(i)))} />},
    {id: 'wypelnianie', od: granica(34), do: granica(52), el: (od) => <OryginalnyDruk plik="wopfu.html" kroki={wypKroki} kamera={wypKamera} odSek={od} css={CSS_FILMU} />},
    {id: 'straznik', od: granica(52), do: granica(58), el: (od) => <Straznik od={[52, 53, 54, 55, 56, 57].map((i) => L(od)(z(i)))} />},
    {id: 'final', od: granica(58), do: koniec, el: (od) => <Final logo={L(od)(z(59))} haslo={L(od)(z(60))} />},
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
