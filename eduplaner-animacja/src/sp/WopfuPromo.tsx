import React from 'react';
import {AbsoluteFill, Audio, Sequence, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from '../marka';
import {Napisy} from '../Napisy';
import {Logo, Pojaw, useWejscie} from '../ui';
import {OryginalnyDruk, type Krok, type Ujecie} from '../kpof/OryginalnyDruk';
import type {Napis} from '../typy';
import krokiJson from '../../public/wopfu-kroki.json';

/** Film „Szkoła podstawowa · WOPF-SP” — narracja: dosłowne fragmenty skryptu (przystanek czwarty + „Jak przygotować ocenę”) i Strażnik prawa. */
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
];
const Straznik: React.FC<{od: number[]}> = ({od}) => {
  const frame = useCurrentFrame();
  const tarcza = useWejscie(0, {damping: 10, stiffness: 120});
  return (
    <Tlo>
      <div style={{position: 'absolute', left: 0, right: 0, top: 50, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 26}}>
        <div style={{width: 96, height: 96, borderRadius: '50%', background: MARKA.pomarancz, display: 'grid', placeItems: 'center', fontSize: 52, transform: `scale(${tarcza * (1 + 0.03 * Math.sin(frame / 8))})`, boxShadow: '0 16px 40px rgba(232,69,10,0.5)'}}>⚖</div>
        <Pojaw od={2}>
          <div style={{fontSize: 56, fontWeight: 800, color: '#fff', lineHeight: 1}}>Strażnik prawa · WOPF-SP</div>
          <div style={{fontSize: 20, color: 'rgba(255,255,255,0.75)', marginTop: 8, letterSpacing: 1.5}}>podstawa istnienia druku i publikatory — stan prawny na rok szkolny 2026/2027</div>
        </Pojaw>
      </div>
      <div style={{position: 'absolute', left: 90, right: 90, top: 205, background: 'rgba(255,255,255,0.07)', border: '1.5px solid rgba(255,255,255,0.25)', borderRadius: 20, overflow: 'hidden'}}>
        {PRAWO.map(([a, b, c], i) => {
          const w = Math.max(0, Math.min(1, (frame - od[i]) / 10));
          const kolor = c === 'POPRAWIONO' ? MARKA.pomarancz : c === 'PODSTAWA' ? '#4A3AA0' : '#2F8F8A';
          return (
            <div key={a} style={{display: 'grid', gridTemplateColumns: '1fr 2.3fr 180px', padding: '20px 28px', borderTop: i ? '1px solid rgba(255,255,255,0.12)' : 'none', opacity: w, transform: `translateX(${(1 - w) * -20}px)`, color: '#fff', fontSize: 23, lineHeight: 1.35, alignItems: 'center', gap: 20}}>
              <div style={{fontWeight: 800}}>{a}</div>
              <div style={{color: 'rgba(255,255,255,0.9)'}}>{b}</div>
              <div style={{textAlign: 'center'}}><span style={{display: 'inline-block', background: kolor, color: '#fff', fontWeight: 800, fontSize: 16, padding: '7px 15px', borderRadius: 999}}>{c}</span></div>
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
        <div style={{marginTop: 30, fontSize: 19, color: 'rgba(255,255,255,0.7)', letterSpacing: 2, textAlign: 'center'}}>SZKOŁA PODSTAWOWA · WOPF-SP · STRAŻNIK PRAWA<br />PCTP KOSZALIN · kontakt@eduplaner2026.pl · 662 888 403</div>
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

/** Film pokazuje druk w powiększeniu — linie, ramki i siatki tabel muszą być wyraźne także po kompresji wideo. */
const CSS_FILMU = [
  '.addrow,.delrow,.delcell,.printcell{display:none!important}',
  '.druk-oryginalny .sheet{box-shadow:0 14px 50px rgba(45,27,105,0.22)!important}',
  '.druk-oryginalny table.tbl{border:2.2px solid #2D1B69!important;border-radius:9px}',
  '.druk-oryginalny .tbl thead th{border-bottom:2.2px solid #2D1B69!important;font-size:10.5px!important;letter-spacing:.5px!important}',
  '.druk-oryginalny .tbl td{border-top:1.4px solid #9d90c8!important}',
  '.druk-oryginalny .tbl td + td,.druk-oryginalny .tbl th + th{border-left:1.4px solid #9d90c8!important}',
  '.druk-oryginalny .opt{border:1.6px solid #b3a6dd!important}',
  '.druk-oryginalny .opt.on{border-color:#E8450A!important;background:#fdece4!important}',
  '.druk-oryginalny .chk{border:2.2px solid #6f5fae!important}',
  '.druk-oryginalny .box{border:1.6px solid #b3a6dd!important}',
  '.druk-oryginalny .legal{border:1.4px solid #c3b8e4!important}',
  '.druk-oryginalny .sec{border-bottom:1.6px solid #d9d0f0;padding-bottom:3px}',
  '.druk-oryginalny .blankline,.druk-oryginalny .blank{border-bottom:1.8px dotted #8f81c2!important;height:auto!important;min-height:15px;overflow-wrap:anywhere;white-space:normal;display:block;max-width:100%;box-sizing:border-box}',
  '.druk-oryginalny .dline{border-bottom:1.6px dotted #8f81c2!important;display:block!important;width:100%!important;min-width:0!important;height:auto!important;min-height:15px;overflow-wrap:anywhere;white-space:normal}',
  '.druk-oryginalny .fg .v,.druk-oryginalny .field .val,.druk-oryginalny td.ex,.druk-oryginalny .box{overflow-wrap:anywhere;white-space:normal}',
  '.druk-oryginalny [data-anim-tekst]{color:#1b1730!important}',
].join('\n');

const arkusz = (sel: string) => Number(/^@(\d+)/.exec(sel)?.[1] ?? 0);
/** Ujęcie „element od góry kadru”: kamera centruje na (górna krawędź + przesunięcie). */
const U = (sek: number, selektor: string, skala: number, gora = 22, czas = 0.75): Ujecie => ({sek, selektor, skala, przesun: Math.round(1080 / skala / 2 - gora), czas});
/** Ujęcie z jawnym przesunięciem (do wyśrodkowania małych elementów). */
const Uc = (sek: number, selektor: string, skala: number, przesun: number, czas = 0.75): Ujecie => ({sek, selektor, skala, przesun, czas});

const TYTUL = '@1 .eyebrow + div';

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

  /* ---------- scena „przegląd druku” (zdania 18–27) ---------- */
  const P: [number, string, number, number][] = [
    // [sekunda, selektor, skala, „od góry”]
    [z(18), TYTUL, 2.5, 150],
    [z(19), '@2 #gNarzedzia', 2.4, 22],
    [z(20), '@1 .sec #0', 2.35, 22],
    [z(20) + 7.0, '@1 .sec #1', 2.45, 22],
    [z(21), '@1 #tblZespol', 2.45, 22],
    [z(21) + 3.0, '@2 #gKonteksty', 2.45, 22],
    [z(21) + 6.0, '@3 #gMedyczne', 2.4, 22],
    [z(22), '@4 table.tbl', 2.35, 22],
    [z(22) + 5.5, '@5 table.tbl', 2.35, 22],
    [z(23), '@10 table.tbl', 2.4, 22],
    [z(23) + 2.9, '@12 table.tbl', 2.4, 22],
    [z(23) + 5.7, '@13 table.tbl', 2.35, 22],
    [z(23) + 8.6, '@11 table.tbl', 2.35, 22],
    [z(24), '@6 .box #0', 2.4, 40],
    [z(24) + 5.0, '@7 table.tbl', 2.35, 22],
    [z(25), '@8 #gOsobyWsparcia', 2.4, 22],
    [z(26), '@16 .sec #0', 2.3, 22],
    [z(26) + 3.5, '@15 table.tbl', 2.35, 22],
    [z(27), '@18 .box #0', 2.3, 22],
    [z(27) + 4.0, '@19 .box #0', 2.3, 22],
  ];
  const przegladKamera: Ujecie[] = P.map(([s, sel, sk, g], i) => (i === 0 ? Uc(s, sel, sk, 30) : U(s, sel, sk, g)));
  const przegladKroki: Krok[] = [
    {sek: 0, typ: 'tekst', selektor: '@1 .fg .v #1', tekst: '14.03.2017', tempo: 999},
    // ramka wokół omawianego elementu — trwa do następnego ujęcia
    ...P.map(([s, sel], i): Krok => ({sek: s + 0.45, doSek: (P[i + 1]?.[0] ?? granica(28)) - 0.2, typ: 'wyroznij', selektor: sel})),
  ];

  /* ---------- scena „pełne wypełnianie” (zdania 34–50) ---------- */
  const T = {
    zespol: z(35) + 0.3,
    dane1: z(37) + 0.3,
    tryb1: z(37) + 7.0,
    s2narz: z(38) + 0.3,
    s2ctx: z(38) + 4.4,
    s2kont: z(40) + 0.2,
    s3: z(40) + 2.6,
    s4: z(41) + 0.4,
    s5: z(42) + 0.2,
    s6: z(42) + 2.4,
    s10: z(43) + 0.1,
    s12: z(43) + 3.2,
    s13: z(43) + 6.3,
    s11: z(43) + 9.4,
    s14: z(43) + 11.0,
    s7: z(44) + 0.2,
    s9opt: z(45) + 0.2,
    s9box: z(46) + 0.2,
    s8: z(47) + 0.2,
    s16: z(48) + 0.1,
    s15: z(48) + 1.6,
    s18: z(49) + 0.2,
    s19: z(49) + 3.2,
    s17: z(50) + 0.2,
    s21: z(50) + 2.5,
  };
  const start = (k: KrokJson): number => {
    const a = arkusz(k.sel);
    if (/\.student \.blank/.test(k.sel)) return 0;
    if (a === 1) return /\.dline/.test(k.sel) ? T.zespol : /\.opt|\.fg \.v #4|\.blankline #4/.test(k.sel) ? T.tryb1 : T.dane1;
    if (a === 2) return /\.dline/.test(k.sel) ? T.s2kont : /\.opt #(?:[6-9]|1[0-3])$/.test(k.sel) ? T.s2narz : T.s2ctx;
    if (a === 9) return /\.opt/.test(k.sel) ? T.s9opt : T.s9box;
    const m: Record<number, number> = {3: T.s3, 4: T.s4, 5: T.s5, 6: T.s6, 7: T.s7, 8: T.s8, 10: T.s10, 11: T.s11, 12: T.s12, 13: T.s13, 14: T.s14, 15: T.s15, 16: T.s16, 17: T.s17, 18: T.s18, 19: T.s19, 21: T.s21};
    return m[a] ?? 0;
  };
  const ODSTEP: Record<string, number> = {'1:zespol': 0.55, '1:dane': 0.9, '1:tryb': 1.2, '2:narz': 0.5, '2:ctx': 0.42, '2:kont': 0.28, '3': 0.18, '4': 0.8, '5': 0.12, '6': 0.4, '7': 0.6, '8': 0.2, '9:opt': 0.8, '9:box': 1.3, '10': 0.14, '11': 0.07, '12': 0.19, '13': 0.14, '14': 0.1, '15': 0.06, '16': 0.28, '17': 0.2, '18': 0.55, '19': 0.65, '21': 0.25};
  const TEMPO: Record<number, number> = {1: 42, 2: 320, 3: 400, 4: 22, 5: 600, 6: 900, 7: 300, 8: 350, 9: 300, 10: 500, 11: 700, 12: 300, 13: 500, 14: 700, 15: 900, 16: 900, 17: 800, 18: 700, 19: 700, 21: 60};
  const grupa = (k: KrokJson): string => {
    const a = arkusz(k.sel);
    if (a === 1) return /\.dline/.test(k.sel) ? '1:zespol' : /\.opt|\.fg \.v #4|\.blankline #4/.test(k.sel) ? '1:tryb' : '1:dane';
    if (a === 2) return /\.dline/.test(k.sel) ? '2:kont' : /\.opt #(?:[6-9]|1[0-3])$/.test(k.sel) ? '2:narz' : '2:ctx';
    if (a === 9) return /\.opt/.test(k.sel) ? '9:opt' : '9:box';
    return String(a);
  };
  const licznik: Record<string, number> = {};
  const wypKroki: Krok[] = KROKI.map((k): Krok => {
    const a = arkusz(k.sel);
    const s0 = start(k);
    const g = grupa(k);
    const i = licznik[g] ?? 0;
    licznik[g] = i + 1;
    const sek = s0 === 0 ? 0 : s0 + i * (ODSTEP[g] ?? 0.2);
    if (k.k) return {sek, typ: 'klik', selektor: k.sel};
    return {sek, typ: 'tekst', selektor: k.sel, tekst: k.t ?? '', tempo: s0 === 0 ? 999 : TEMPO[a] ?? 300};
  });
  const W: [number, string, number, number][] = [
    [0, '@1 #tblZespol', 2.45, 22],
    [T.dane1 - 0.4, '@1 .sec #0', 2.35, 22],
    [T.tryb1 - 0.4, '@1 .sec #1', 2.45, 22],
    [T.s2narz - 0.3, '@2 #gNarzedzia', 2.4, 22],
    [T.s2ctx - 0.3, '@2 #gKonteksty', 2.45, 22],
    [T.s2kont - 0.3, '@2 #tblKontekst', 2.3, 22],
    [T.s3 - 0.3, '@3 #gMedyczne', 2.4, 22],
    [T.s4 - 0.3, '@4 table.tbl', 2.35, 22],
    [T.s5 - 0.2, '@5 table.tbl', 2.35, 22],
    [T.s6 - 0.2, '@6 .box #0', 2.4, 40],
    [T.s10 - 0.1, '@10 table.tbl', 2.4, 22],
    [T.s12 - 0.2, '@12 table.tbl', 2.4, 22],
    [T.s13 - 0.2, '@13 table.tbl', 2.35, 22],
    [T.s11 - 0.2, '@11 table.tbl', 2.35, 22],
    [T.s7 - 0.2, '@7 table.tbl', 2.35, 22],
    [T.s9opt - 0.2, '@9 #gCzynniki', 2.35, 22],
    [T.s9box - 0.2, '@9 .box #0', 2.3, 40],
    [T.s8 - 0.2, '@8 #gOsobyWsparcia', 2.4, 22],
    [T.s16 - 0.1, '@16 .sec #0', 2.3, 22],
    [T.s18 - 0.2, '@18 .box #0', 2.3, 22],
    [T.s19 - 0.2, '@19 .box #0', 2.3, 22],
    [T.s17 - 0.2, '@17 .sec #0', 2.25, 22],
    [T.s21 - 0.2, '@21 .sec #1', 2.3, 22],
  ];
  const wypKamera: Ujecie[] = W.map(([s, sel, sk, g], i) => (i === 8 || i === 15 ? Uc(s, sel, sk, g) : U(s, sel, sk, g)));
  const wypRamki: Krok[] = W.map(([s, sel], i): Krok => ({sek: s + 0.5, doSek: (W[i + 1]?.[0] ?? granica(51)) - 0.2, typ: 'wyroznij', selektor: sel}));

  type Scena = {id: string; od: number; do: number; el: (od: number) => React.ReactNode};
  const sceny: Scena[] = [
    {id: 'intro', od: 0, do: granica(1), el: () => <Intro />},
    {id: 'scala', od: granica(1), do: granica(5), el: (od) => <Scala lista={L(od)(z(2))} jezyk={L(od)(z(3))} opis={L(od)(z(4))} />},
    {id: 'rozgalezienie', od: granica(5), do: granica(10), el: (od) => <Rozgalezienie sekcja={L(od)(z(6))} ipet={L(od)(z(7))} pwes={L(od)(z(8))} jeden={L(od)(z(9))} />},
    {id: 'podstawa', od: granica(10), do: granica(13), el: (od) => <Podstawa rozp={L(od)(z(11))} dwa={L(od)(z(12))} />},
    {id: 'dlaczego', od: granica(13), do: granica(18), el: (od) => <Dlaczego od={[14, 15, 16, 17].map((i) => L(od)(z(i)))} />},
    {id: 'przeglad', od: granica(18), do: granica(28), el: (od) => <OryginalnyDruk plik="wopfu.html" kroki={przegladKroki} kamera={przegladKamera} odSek={od} css={CSS_FILMU} />},
    {id: 'zrodla', od: granica(28), do: granica(34), el: (od) => <Zrodla od={[29, 30, 31, 32, 33].map((i) => L(od)(z(i)))} />},
    {id: 'wypelnianie', od: granica(34), do: granica(51), el: (od) => <OryginalnyDruk plik="wopfu.html" kroki={[...wypKroki, ...wypRamki]} kamera={wypKamera} odSek={od} css={CSS_FILMU} />},
    {id: 'straznik', od: granica(51), do: granica(57), el: (od) => <Straznik od={[52, 53, 54, 55, 56].map((i) => L(od)(z(i)))} />},
    {id: 'final', od: granica(57), do: koniec, el: (od) => <Final logo={L(od)(z(58))} haslo={L(od)(z(59))} />},
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
