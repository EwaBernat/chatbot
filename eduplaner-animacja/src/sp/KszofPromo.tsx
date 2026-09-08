import React from 'react';
import {AbsoluteFill, Audio, Sequence, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from '../marka';
import {Napisy} from '../Napisy';
import {Logo, Pojaw, useWejscie} from '../ui';
import {OryginalnyDruk, type Krok, type Ujecie} from '../kpof/OryginalnyDruk';
import type {Napis} from '../typy';

export type FilmKszof = {audio: string | null; napisy: Napis[]; dlugosc: number};
export type Props = {film: FilmKszof};

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
    <div style={{fontSize: 56, fontWeight: 800, color: '#fff', marginTop: 10, letterSpacing: -1, lineHeight: 1.1}}>{tytul}</div>
  </Pojaw>
);

const Intro: React.FC<{sub: number}> = ({sub}) => (
  <Tlo>
    <Pojaw od={0} style={{position: 'absolute', left: 0, right: 0, top: 150, textAlign: 'center'}}>
      <div style={{fontSize: 20, letterSpacing: 4, color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase'}}>EduPlaner 2026 · Szkoła podstawowa · przystanek drugi</div>
      <div style={{fontSize: 96, fontWeight: 800, color: '#fff', marginTop: 12, letterSpacing: -2, lineHeight: 1.05}}>KSz<span style={{color: '#F6A57E'}}>OF</span></div>
      <div style={{fontSize: 40, fontWeight: 700, color: '#fff', marginTop: 10}}>Kwestionariusz Szkolnej Oceny Funkcjonalnej</div>
      <div style={{display: 'inline-block', marginTop: 26, background: MARKA.pomarancz, color: '#fff', fontSize: 21, fontWeight: 700, padding: '10px 26px', borderRadius: 999, letterSpacing: 2}}>52 TWIERDZENIA · 9 OBSZARÓW ICF · SKALA 1–5 · STEN 1–10</div>
    </Pojaw>
    <div style={{position: 'absolute', left: 0, right: 0, top: 640, display: 'flex', justifyContent: 'center'}}>
      <Karta od={sub} akcent style={{width: 1180, textAlign: 'center', fontSize: 30, fontWeight: 700, lineHeight: 1.4}}>Serce dokumentacji: funkcjonowanie ucznia w codziennych sytuacjach szkolnych i domowych</Karta>
    </div>
  </Tlo>
);

const OBSZARY: [string, string, string][] = [
  ['I', 'Uczenie się i stosowanie wiedzy', 'd110–d177'],
  ['II', 'Ogólne zadania i obowiązki', 'd210–d240'],
  ['III', 'Porozumiewanie się', 'd310–d350'],
  ['IV', 'Motoryka, poruszanie się', 'd440–d450'],
  ['V', 'Dbanie o siebie i samodzielność', 'd510–d570'],
  ['VI', 'Życie domowe', 'd640'],
  ['VII', 'Wzajemne kontakty i związki', 'd710–d760'],
  ['VIII', 'Edukacja szkolna', 'd820'],
  ['IX', 'Życie w społeczności lokalnej', 'd920'],
];
const Icf: React.FC<{icf: number; obszary: number; nie: number; wersje: number}> = ({icf, obszary, nie, wersje}) => (
  <Tlo>
    <Naglowek kicker="ICF · Międzynarodowa Klasyfikacja Funkcjonowania (WHO 2001)" tytul="Dziewięć obszarów aktywności i uczestniczenia" />
    <div style={{position: 'absolute', left: 90, right: 90, top: 215}}>
      <Karta od={icf} style={{textAlign: 'center', fontSize: 26, lineHeight: 1.4, padding: '14px 24px'}}>
        ICF nie opisuje choroby ani rozpoznania — opisuje, <b style={{color: '#F6A57E'}}>co uczeń robi</b>, <b style={{color: '#F6A57E'}}>w czym uczestniczy</b> i co w otoczeniu mu pomaga albo przeszkadza.
      </Karta>
      <div style={{display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 16, marginTop: 20}}>
        {OBSZARY.map(([r, n, k], i) => (
          <Karta key={r} od={obszary + i * 4} style={{display: 'flex', alignItems: 'center', gap: 16, padding: '14px 18px'}}>
            <div style={{width: 58, height: 58, borderRadius: 14, background: MARKA.pomarancz, display: 'grid', placeItems: 'center', fontSize: 22, fontWeight: 800, flex: '0 0 auto'}}>{r}</div>
            <div>
              <div style={{fontSize: 22, fontWeight: 800, lineHeight: 1.15}}>{n}</div>
              <div style={{fontSize: 16, color: '#F6A57E', fontWeight: 700, marginTop: 4, letterSpacing: 1}}>ICF {k}</div>
            </div>
          </Karta>
        ))}
      </div>
      <div style={{display: 'flex', gap: 20, marginTop: 20}}>
        <Karta od={nie} style={{flex: 1, textAlign: 'center', fontSize: 22, fontWeight: 700, padding: '14px 20px'}}>To nie diagnoza — uporządkowany zapis obserwacji i punkt wyjścia do decyzji zespołu</Karta>
        <Karta od={wersje} akcent style={{flex: 1, textAlign: 'center', fontSize: 22, fontWeight: 700, padding: '14px 20px'}}>Trzy wersje: I–III · IV–VI · VII–VIII — decyduje wiek rozwojowy, nie metrykalny</Karta>
      </div>
    </div>
  </Tlo>
);

const ZASADY: string[] = [
  'Wypełnij CAŁY arkusz — wszystkie obszary I–IX; nie dziel obszarów między oceniających.',
  'Oceniaj na podstawie 2–4 tygodni obserwacji w codziennych, typowych sytuacjach — nie jednego dnia.',
  'Wypełniaj samodzielnie i niezależnie — nie konsultuj ocen z pozostałymi oceniającymi przed spotkaniem zespołu.',
  'Oceniaj to, co uczeń ROBI, a nie co potrafiłby zrobić „gdyby chciał”. Liczy się rzeczywiste zachowanie.',
  'Odnoś się do oczekiwań rozwojowych dla WIEKU ucznia, a nie do dorosłego wzorca.',
  'Przy ocenach 1–2 i 5 dopisz przykłady konkretnych zachowań — zwłaszcza w obszarach problemowych i mocnych.',
  'W II etapie zbierz oceny od co najmniej trzech nauczycieli przedmiotów; arkusz zwróć koordynatorowi w terminie.',
];
const Zasady: React.FC<{od: number[]}> = ({od}) => (
  <Tlo>
    <Naglowek kicker="Zanim postawisz pierwszą ocenę" tytul="Siedem zasad rzetelnej obserwacji" />
    <div style={{position: 'absolute', left: 120, right: 120, top: 220, display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16}}>
      {ZASADY.map((z, i) => (
        <Karta key={i} od={od[i < 2 ? 0 : i < 4 ? 1 : 2] + (i % 2) * 6} style={{display: 'flex', gap: 18, alignItems: 'flex-start', padding: '16px 20px', gridColumn: i === 6 ? '1 / span 2' : undefined}}>
          <div style={{width: 46, height: 46, borderRadius: '50%', background: i === 6 ? MARKA.pomarancz : MARKA.morski, display: 'grid', placeItems: 'center', fontSize: 22, fontWeight: 800, flex: '0 0 auto'}}>{i + 1}</div>
          <div style={{fontSize: 23, lineHeight: 1.35}}>{z}</div>
        </Karta>
      ))}
    </div>
  </Tlo>
);

const PRAWO: [string, string, string][] = [
  ['Prawo oświatowe, art. 127', 'w druku było t.j. Dz.U. 2024 poz. 737 — obowiązuje t.j. Dz.U. 2026 poz. 820 (2 miejsca)', 'POPRAWIONO'],
  ['Rozp. MEN z 9.08.2017 r. — pomoc pp i kształcenie specjalne', 'pierwotne publikatory Dz.U. 2017 poz. 1591 i 1578 → t.j. Dz.U. 2023 poz. 1798 i t.j. Dz.U. 2020 poz. 1309 (30 miejsc, także w zaleceniach)', 'POPRAWIONO'],
  ['Orzeczenia i opinie poradni', 'rozp. ME z 2.03.2026 r., Dz.U. 2026 poz. 428 — informacja szkoły o funkcjonowaniu ucznia w 10 dni; od 1.09.2026', '✓ zgodne'],
  ['Dokumentacja przebiegu nauczania', 'arkusz obserwacji = dokumentacja badań i czynności uzupełniających — rozp. MEN z 25.08.2017 r., t.j. Dz.U. 2024 poz. 50', 'PODSTAWA'],
  ['Progi poziomów wsparcia', 'sten 8–10 / 5–7 / 1–4 i przeliczanie wyniku — decyzja rady pedagogicznej wpisana do procedury szkoły, nie przepis', 'PROCEDURA'],
];
const Straznik: React.FC<{od: number[]}> = ({od}) => {
  const frame = useCurrentFrame();
  const tarcza = useWejscie(0, {damping: 10, stiffness: 120});
  return (
    <Tlo>
      <div style={{position: 'absolute', left: 0, right: 0, top: 44, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 26}}>
        <div style={{width: 96, height: 96, borderRadius: '50%', background: MARKA.pomarancz, display: 'grid', placeItems: 'center', fontSize: 52, transform: `scale(${tarcza * (1 + 0.03 * Math.sin(frame / 8))})`, boxShadow: '0 16px 40px rgba(232,69,10,0.5)'}}>⚖</div>
        <Pojaw od={2}>
          <div style={{fontSize: 56, fontWeight: 800, color: '#fff', lineHeight: 1}}>Strażnik prawa · KSzOF</div>
          <div style={{fontSize: 20, color: 'rgba(255,255,255,0.75)', marginTop: 8, letterSpacing: 1.5}}>publikatory z druku sprawdzone ze skryptem szkolenia dla szkoły podstawowej (część 5)</div>
        </Pojaw>
      </div>
      <div style={{position: 'absolute', left: 90, right: 90, top: 200, background: 'rgba(255,255,255,0.07)', border: '1.5px solid rgba(255,255,255,0.25)', borderRadius: 20, overflow: 'hidden'}}>
        {PRAWO.map(([a, b, c], i) => {
          const w = Math.max(0, Math.min(1, (frame - od[i]) / 10));
          const kolor = c.startsWith('✓') ? '#2E9E52' : c === 'PODSTAWA' || c === 'PROCEDURA' ? '#2F8F8A' : MARKA.pomarancz;
          return (
            <div key={a} style={{display: 'grid', gridTemplateColumns: '1fr 2.2fr 190px', padding: '19px 26px', borderTop: i ? '1px solid rgba(255,255,255,0.12)' : 'none', opacity: w, transform: `translateX(${(1 - w) * -20}px)`, color: '#fff', fontSize: 23, lineHeight: 1.35, alignItems: 'center', gap: 20}}>
              <div style={{fontWeight: 800}}>{a}</div>
              <div style={{color: 'rgba(255,255,255,0.9)'}}>{b}</div>
              <div style={{textAlign: 'center'}}><span style={{display: 'inline-block', background: kolor, color: '#fff', fontWeight: 800, fontSize: 16, padding: '6px 14px', borderRadius: 999}}>{c}</span></div>
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
      <Pojaw od={0}><div style={{fontSize: 56, fontWeight: 800, color: '#fff', textAlign: 'center', lineHeight: 1.2}}>Profil zamiast wrażenia.<br />Liczba zamiast przymiotnika.</div></Pojaw>
      <Pojaw od={logo} style={{marginTop: 50, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
        <Logo rozmiar={120} />
        <div style={{fontSize: 84, fontWeight: 800, color: '#fff', letterSpacing: -2, marginTop: 18, lineHeight: 1}}>EduPlaner <span style={{color: '#F6A57E'}}>2026</span></div>
      </Pojaw>
      <Pojaw od={haslo}>
        <div style={{fontSize: 38, color: '#fff', fontWeight: 700, marginTop: 22}}>Mniej dokumentów. Więcej edukacji.</div>
        <div style={{marginTop: 30, fontSize: 19, color: 'rgba(255,255,255,0.7)', letterSpacing: 2, textAlign: 'center'}}>SZKOŁA PODSTAWOWA · KSzOF IV–VI · PROFIL · 270° · OPINIA DLA PORADNI · STRAŻNIK PRAWA<br />PCTP KOSZALIN · kontakt@eduplaner2026.pl · 662 888 403</div>
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

/** Oceny z arkusza autorki (wartości 1–5) w kolejności twierdzeń, pogrupowane: [arkusz, obszar, wartości]. */
const OCENY: [number, string, number[]][] = [
  [2, 'I', [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]],
  [2, 'II', [3, 3, 3, 3, 3, 3]],
  [3, 'III', [3, 3, 3, 3, 3, 3, 3, 3]],
  [3, 'IV', [3, 4]],
  [3, 'V', [4, 4, 4, 2]],
  [3, 'VI', [2, 2]],
  [3, 'VII', [2, 2, 2]],
  [4, 'VII', [2, 2, 2, 2, 2, 2, 2]],
  [4, 'VIII', [2, 2, 2, 2]],
  [4, 'IX', [2, 2]],
];
/** Selektor k-tego (od zera) twierdzenia obszaru na danym arkuszu — kółko z wartością v. */
const rc = (arkusz: number, obszar: string, k: number, v: number) => `@${arkusz} tr.arow[data-area="${obszar}"] .rc[data-v="${v}"] #${k}`;

export const KszofPromo: React.FC<Props> = ({film}) => {
  const {fps} = useVideoConfig();
  const n = film.napisy;
  const z = (i: number) => n[i]?.odSek ?? i * 5;
  const kz = (i: number) => n[i]?.doSek ?? i * 5 + 4;
  const granica = (i: number) => (i <= 0 ? 0 : (kz(i - 1) + z(i)) / 2);
  const fr = (sek: number) => Math.round(sek * fps);
  const lok = (od: number) => (s: number) => Math.max(0, fr(s - od));
  const koniec = film.dlugosc;

  // --- harmonogram ocen: obszar I opowiadany (twierdzenia 3 i 10), reszta w szybkim tempie
  const ocena = (arkusz: number, obszar: string, k: number, v: number, sek: number): Krok => ({sek, typ: 'klasa', selektor: rc(arkusz, obszar, k, v), klasa: 'on'});
  const kroki: Krok[] = [
    ...Array.from({length: 28}, (_, i): Krok => ({sek: 0, typ: 'tekst', selektor: `@${i + 1} .student .blank #0`, tekst: '22.09.2026', tempo: 999})),
    {sek: z(9) + 0.4, doSek: z(9) + 2.6, typ: 'wyroznij', selektor: '@1 .ktorow'},
    {sek: z(9) + 2.8, typ: 'tekst', selektor: '@1 .mvl #0', tekst: '01–22.09.2026 (3 tygodnie obserwacji)', tempo: 40},
    {sek: z(9) + 4.0, typ: 'tekst', selektor: '@1 .mvl #1', tekst: 'mgr Katarzyna Wiśniewska — wychowawczyni III A (N)', tempo: 40},
    {sek: z(10) + 0.3, doSek: kz(10) + 0.3, typ: 'wyroznij', selektor: '@2 .scalebar'},
    // obszar I: 1–2 szybko, 3 po narracji, 4–9 szybko, 10 po narracji, 11–14 przy badge
    ocena(2, 'I', 0, 3, z(11) + 0.3),
    ocena(2, 'I', 1, 3, z(11) + 0.9),
    {sek: z(11) + 1.5, doSek: z(11) + 6.2, typ: 'wyroznij', selektor: '@2 tr.arow #2'},
    ocena(2, 'I', 2, 3, Math.max(z(11) + 6.0, kz(11) - 0.9)),
    ...[3, 4, 5, 6, 7, 8].map((k, i) => ocena(2, 'I', k, 3, z(12) + 0.2 + i * 0.3)),
    {sek: z(12) + 2.2, doSek: kz(12) + 0.2, typ: 'wyroznij', selektor: '@2 tr.arow #9'},
    ocena(2, 'I', 9, 3, kz(12) - 0.8),
    ...[10, 11, 12, 13].map((k, i) => ocena(2, 'I', k, 3, z(13) + 0.2 + i * 0.3)),
    {sek: z(13) + 1.6, doSek: kz(13) + 0.3, typ: 'wyroznij', selektor: '@2 .arsum'},
  ];
  // pozostałe obszary — jedna ocena co 0,22 s (38 twierdzeń ≈ 8,4 s)
  let t = z(14) + 0.2;
  for (const [arkusz, obszar, wartosci] of OCENY) {
    if (arkusz === 2 && obszar === 'I') continue;
    wartosci.forEach((v, k) => {
      kroki.push(ocena(arkusz, obszar, k, v, t));
      t += 0.22;
    });
  }
  kroki.push({sek: z(15) + 0.4, doSek: kz(15) + 0.3, typ: 'wyroznij', selektor: '@3 .arsum[data-c="VI"]'});
  kroki.push({sek: z(16) + 0.3, doSek: z(16) + 4.5, typ: 'wyroznij', selektor: '@8 .k-ogol'});
  kroki.push({sek: z(19) + 0.5, doSek: kz(19) + 0.3, typ: 'wyroznij', selektor: '@3 tr.arow[data-area="V"] .rc[data-v="2"] #3'});

  const S = 2.0;
  const kamera: Ujecie[] = [
    {sek: 0, selektor: '@1 .eyebrow', skala: 1.7, przesun: 170},
    {sek: z(9) + 2.6, selektor: '@1 .sec', skala: S, przesun: 120},
    {sek: z(10), selektor: '@2 .scalebar', skala: 2.1, przesun: 150},
    {sek: z(11), selektor: '@2 tr.arow #2', skala: S, przesun: 90},
    {sek: z(12), selektor: '@2 tr.arow #9', skala: S, przesun: 60},
    {sek: z(13), selektor: '@2 .arsum', skala: 2.2, przesun: 90},
    {sek: z(14), selektor: '@2 tr.arow #14', skala: 1.9, przesun: 150},
    {sek: z(14) + 1.7, selektor: '@3 tr.arow #0', skala: 1.8, przesun: 280},
    {sek: z(14) + 4.5, selektor: '@3 tr.arow #8', skala: 1.8, przesun: 250},
    {sek: z(15), selektor: '@3 .arsum[data-c="VI"]', skala: 2.1, przesun: 80},
    {sek: z(15) + 3.2, selektor: '@4 tr.arow #0', skala: 1.8, przesun: 240},
    {sek: z(16), selektor: '@8 .ogolbar', skala: S, przesun: 130},
    {sek: z(16) + 4.6, selektor: '@8 table.tbl #1', skala: S, przesun: 70},
    {sek: z(17), selektor: '@7 svg #0', skala: 1.9, przesun: 150},
    {sek: z(17) + 4.2, selektor: '@7 svg #1', skala: 1.9, przesun: 140},
    {sek: z(18), selektor: '@7 table.tbl', skala: 1.9, przesun: 130},
    {sek: z(19), selektor: '@3 tr.arow #13', skala: 2.1, przesun: 30},
    {sek: z(20), selektor: '@9 table.tbl', skala: 1.9, przesun: 150},
    {sek: z(21), selektor: '@10 .sbody', skala: 1.75, przesun: 290},
    {sek: z(22), selektor: '@11 .sec #0', skala: 1.9, przesun: 210},
    {sek: z(23), selektor: '@12 .sbody', skala: 1.75, przesun: 300},
    {sek: z(23) + 4.5, selektor: '@12 .smartgrid #1', skala: 1.9, przesun: 70},
    {sek: z(24), selektor: '@22 .eyebrow', skala: 1.8, przesun: 190},
    {sek: z(25), selektor: '@21 .sec #0', skala: 1.9, przesun: 210},
  ];
  const cssFilmu = [
    '.addrow,.delrow,.delcell,.printcell{display:none!important}',
    '.druk-oryginalny .sheet{box-shadow:0 10px 40px rgba(45,27,105,0.18)}',
    '.druk-oryginalny .mbox,.druk-oryginalny .box,.druk-oryginalny .ktobox{border-width:1.3px}',
    '.druk-oryginalny .blank,.druk-oryginalny .mvl,.druk-oryginalny .dline{overflow-wrap:break-word;white-space:normal;height:auto;min-height:15px}',
    '.druk-oryginalny .mvl,.druk-oryginalny .blank{display:block;max-width:100%;box-sizing:border-box}',
  ].join('\n');

  type Scena = {id: string; od: number; do: number; el: (od: number) => React.ReactNode};
  const sceny: Scena[] = [
    {id: 'intro', od: 0, do: granica(2), el: (od) => <Intro sub={lok(od)(z(1))} />},
    {id: 'icf', od: granica(2), do: granica(6), el: (od) => <Icf icf={lok(od)(z(2))} obszary={lok(od)(z(3))} nie={lok(od)(z(4))} wersje={lok(od)(z(5))} />},
    {id: 'zasady', od: granica(6), do: granica(9), el: (od) => <Zasady od={[6, 7, 8].map((i) => lok(od)(z(i)))} />},
    {id: 'druk', od: granica(9), do: granica(26), el: (od) => <OryginalnyDruk plik="kszof.html" kroki={kroki} kamera={kamera} wykresyOdSek={z(17) + 0.3} odSek={od} css={cssFilmu} />},
    {id: 'straznik', od: granica(26), do: granica(31), el: (od) => <Straznik od={[27, 28, 29, 29, 30].map((i, j) => lok(od)(z(i) + (j === 3 ? 4.0 : 0)))} />},
    {id: 'final', od: granica(31), do: koniec, el: (od) => <Final logo={lok(od)(z(32))} haslo={lok(od)(z(33))} />},
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
