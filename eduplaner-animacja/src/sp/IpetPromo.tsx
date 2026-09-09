import React from 'react';
import {AbsoluteFill, Audio, Sequence, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from '../marka';
import {Napisy} from '../Napisy';
import {Logo, Pojaw, useWejscie} from '../ui';
import {OryginalnyDruk, type Krok, type Ujecie} from '../kpof/OryginalnyDruk';
import type {Napis} from '../typy';
import onJson from '../../public/ipet-sp-on.json';

/** Film „Szkoła podstawowa · IPET” — narracja: dosłowny tekst skryptu (część 7, pkt 09–18 i „Jak przygotować IPET”) + Strażnik prawa. */
export type FilmIpet = {audio: string | null; napisy: Napis[]; dlugosc: number};
export type Props = {film: FilmIpet};
type Zazn = {sel: string; a: number};
const ON = onJson as unknown as Zazn[];

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
  <Pojaw od={od} style={{position: 'absolute', left: 110, right: 110, top: 64, textAlign: 'center'}}>
    <div style={{fontSize: 19, letterSpacing: 4, color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase'}}>{kicker}</div>
    <div style={{fontSize: 54, fontWeight: 800, color: '#fff', marginTop: 10, letterSpacing: -1, lineHeight: 1.1}}>{tytul}</div>
  </Pojaw>
);
const Kolo: React.FC<{n: string | number; kolor?: string; rozmiar?: number}> = ({n, kolor = MARKA.morski, rozmiar = 54}) => (
  <div style={{width: rozmiar, height: rozmiar, borderRadius: '50%', background: kolor, display: 'grid', placeItems: 'center', fontSize: rozmiar * 0.42, fontWeight: 800, flex: '0 0 auto', color: '#fff'}}>{n}</div>
);

const Intro: React.FC = () => (
  <Tlo>
    <Pojaw od={0} style={{position: 'absolute', left: 0, right: 0, top: 170, textAlign: 'center'}}>
      <div style={{fontSize: 20, letterSpacing: 4, color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase'}}>EduPlaner 2026 · Szkoła podstawowa · przystanek piąty</div>
      <div style={{fontSize: 120, fontWeight: 800, color: '#fff', marginTop: 14, letterSpacing: -4, lineHeight: 1}}>IP<span style={{color: '#F6A57E'}}>ET</span></div>
      <div style={{fontSize: 40, fontWeight: 700, color: '#fff', marginTop: 16, lineHeight: 1.2}}>Indywidualny Program Edukacyjno-Terapeutyczny</div>
    </Pojaw>
    <Pojaw od={30} style={{position: 'absolute', left: 300, right: 300, top: 620}}>
      <Karta od={30} akcent style={{textAlign: 'center', fontSize: 29, fontWeight: 700, lineHeight: 1.4}}>Program wynika z oceny zdanie po zdaniu</Karta>
    </Pojaw>
  </Tlo>
);

const Terminy: React.FC<{dla: number; dwa: number; t1: number; t2: number}> = ({dla, dwa, t1, t2}) => (
  <Tlo>
    <Naglowek kicker="Dla kogo i do kiedy" tytul="Terminy opracowania programu" />
    <Karta od={dla} style={{position: 'absolute', left: 200, right: 200, top: 225, textAlign: 'center', fontSize: 27, lineHeight: 1.4}}>
      Program opracowujemy dla ucznia posiadającego <b style={{color: '#F6A57E'}}>orzeczenie o potrzebie kształcenia specjalnego</b>.
    </Karta>
    <Pojaw od={dwa} style={{position: 'absolute', left: 0, right: 0, top: 380, textAlign: 'center', fontSize: 26, letterSpacing: 3, color: 'rgba(255,255,255,0.75)', textTransform: 'uppercase'}}>Terminy są dwa</Pojaw>
    <div style={{position: 'absolute', left: 170, right: 170, top: 450, display: 'flex', gap: 26}}>
      <Karta od={t1} akcent style={{flex: 1, textAlign: 'center', padding: '36px 26px'}}>
        <div style={{fontSize: 62, fontWeight: 800, lineHeight: 1}}>30 IX</div>
        <div style={{fontSize: 25, marginTop: 12, lineHeight: 1.35}}>dla ucznia, który <b>rozpoczyna kształcenie</b> z orzeczeniem</div>
      </Karta>
      <Karta od={t2} style={{flex: 1, textAlign: 'center', padding: '36px 26px'}}>
        <div style={{fontSize: 62, fontWeight: 800, lineHeight: 1, color: '#F6A57E'}}>30 dni</div>
        <div style={{fontSize: 25, marginTop: 12, lineHeight: 1.35}}>od dnia <b>złożenia orzeczenia w szkole</b> — niezależnie od miesiąca</div>
      </Karta>
    </div>
  </Tlo>
);

const Rodzice: React.FC<{tyt: number; a: number; b: number}> = ({tyt, a, b}) => (
  <Tlo>
    <Naglowek kicker="§ 6 ust. 11–13" tytul="Prawa rodziców" od={tyt} />
    <div style={{position: 'absolute', left: 140, right: 140, top: 240, display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 24}}>
      <Karta od={a} style={{padding: '26px 28px', fontSize: 26, lineHeight: 1.35}}>
        <Kolo n="1" rozmiar={52} />
        <div style={{marginTop: 14}}>Prawo <b style={{color: '#F6A57E'}}>uczestniczyć w spotkaniach zespołu</b></div>
      </Karta>
      <Karta od={a + 8} style={{padding: '26px 28px', fontSize: 26, lineHeight: 1.35}}>
        <Kolo n="2" rozmiar={52} kolor={MARKA.pomarancz} />
        <div style={{marginTop: 14}}>Prawo otrzymać <b style={{color: '#F6A57E'}}>kopię programu i kopię oceny</b></div>
      </Karta>
    </div>
    <div style={{position: 'absolute', left: 140, right: 140, top: 560}}>
      <Karta od={b} akcent style={{textAlign: 'center', fontSize: 26, lineHeight: 1.4, padding: '24px 28px'}}>
        Dyrektor zawiadamia o terminie spotkania w sposób przyjęty w szkole, a przekazanie kopii <b>odnotowujemy w rejestrze kontaktów</b>.
      </Karta>
    </div>
  </Tlo>
);

const Czym: React.FC<{jak: number; podstawa: number; wyjatek: number}> = ({jak, podstawa, wyjatek}) => (
  <Tlo>
    <Naglowek kicker="W szkole wygląda inaczej niż w przedszkolu" tytul="Czym jest dostosowanie" />
    <div style={{position: 'absolute', left: 150, right: 150, top: 235, display: 'flex', gap: 26}}>
      <Karta od={jak} akcent style={{flex: 1, textAlign: 'center', padding: '32px 24px'}}>
        <div style={{fontSize: 22, letterSpacing: 3, fontWeight: 800, color: 'rgba(255,255,255,0.85)'}}>ZMIENIAMY</div>
        <div style={{fontSize: 40, fontWeight: 800, marginTop: 10}}>jak uczymy<br />i jak sprawdzamy</div>
      </Karta>
      <Karta od={jak + 8} style={{flex: 1, textAlign: 'center', padding: '32px 24px'}}>
        <div style={{fontSize: 22, letterSpacing: 3, fontWeight: 800, color: '#F6A57E'}}>NIE ZMIENIAMY</div>
        <div style={{fontSize: 40, fontWeight: 800, marginTop: 10}}>czego<br />uczymy</div>
      </Karta>
    </div>
    <Karta od={podstawa} style={{position: 'absolute', left: 150, right: 150, top: 560, textAlign: 'center', fontSize: 30, fontWeight: 700}}>Podstawa programowa pozostaje ta sama.</Karta>
    <Karta od={wyjatek} style={{position: 'absolute', left: 150, right: 150, top: 690, textAlign: 'center', fontSize: 24, lineHeight: 1.4, borderColor: '#F6A57E'}}>
      Wyjątek: uczeń z <b>niepełnosprawnością intelektualną w stopniu umiarkowanym lub znacznym</b> — obowiązuje odrębna podstawa programowa.
    </Karta>
  </Tlo>
);

const Przedmiotowo: React.FC<{zle: number; dobrze: number}> = ({zle, dobrze}) => (
  <Tlo>
    <Naglowek kicker="Dostosowania zapisujemy przedmiotowo, a nie ogólnie" tytul="Jeden zapis, dwie jakości" />
    <div style={{position: 'absolute', left: 120, right: 120, top: 245, display: 'flex', flexDirection: 'column', gap: 26}}>
      <Karta od={zle} style={{padding: '26px 30px', borderColor: '#C0392B', background: 'rgba(192,57,43,0.16)'}}>
        <div style={{fontSize: 20, letterSpacing: 3, fontWeight: 800, color: '#F09B90'}}>NIE MÓWI NIC NAUCZYCIELOWI GEOGRAFII</div>
        <div style={{fontSize: 34, fontWeight: 700, marginTop: 12, fontStyle: 'italic'}}>„wydłużenie czasu pracy”</div>
      </Karta>
      <Karta od={dobrze} style={{padding: '26px 30px', borderColor: '#2F8F8A', background: 'rgba(47,143,138,0.18)'}}>
        <div style={{fontSize: 20, letterSpacing: 3, fontWeight: 800, color: '#8FD8D2'}}>MÓWI WSZYSTKO</div>
        <div style={{fontSize: 26, lineHeight: 1.45, marginTop: 12, fontStyle: 'italic'}}>
          „na sprawdzianach z geografii: polecenia czytane na głos, mapa konturowa z pogrubionymi granicami, czas wydłużony o połowę, ocena za treść bez uwzględniania błędów zapisu”
        </div>
      </Karta>
    </div>
  </Tlo>
);

const PRAWO: [string, string, string][] = [
  ['§ 6 ust. 1 pkt 1–8', 'obowiązkowa zawartość programu — osiem elementów, karta kontrolna każdej kontroli', 'PODSTAWA'],
  ['§ 6 ust. 4', 'program opracowuje się po dokonaniu oceny, z uwzględnieniem zaleceń z orzeczenia', 'PODSTAWA'],
  ['§ 6 ust. 5 · ust. 9 · ust. 11–13', 'termin: do 30 IX albo 30 dni od złożenia orzeczenia · ocena co najmniej 2× w roku · prawa rodziców do udziału i kopii', 'PODSTAWA'],
  ['Rozp. o kształceniu specjalnym — publikator', 'w druku był pierwotny Dz.U. 2017 poz. 1578 (7 miejsc) → t.j. Dz.U. 2020 poz. 1309', 'POPRAWIONO'],
  ['Rozp. o pomocy psychologiczno-pedagogicznej', 'Dz.U. 2017 poz. 1591 → t.j. Dz.U. 2023 poz. 1798 · Prawo oświatowe, art. 127 — t.j. Dz.U. 2026 poz. 820', 'POPRAWIONO'],
  ['Cele mierzalne (SMART)', 'nazwa nie pada w rozporządzeniu — wymagana jest ocena efektywności, a cel z kryterium jest najprostszym sposobem, żeby ją przeprowadzić', 'UWAGA'],
];
const Straznik: React.FC<{od: number[]}> = ({od}) => {
  const frame = useCurrentFrame();
  const tarcza = useWejscie(0, {damping: 10, stiffness: 120});
  return (
    <Tlo>
      <div style={{position: 'absolute', left: 0, right: 0, top: 44, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 26}}>
        <div style={{width: 92, height: 92, borderRadius: '50%', background: MARKA.pomarancz, display: 'grid', placeItems: 'center', fontSize: 50, transform: `scale(${tarcza * (1 + 0.03 * Math.sin(frame / 8))})`, boxShadow: '0 16px 40px rgba(232,69,10,0.5)'}}>⚖</div>
        <Pojaw od={2}>
          <div style={{fontSize: 54, fontWeight: 800, color: '#fff', lineHeight: 1}}>Strażnik prawa · IPET</div>
          <div style={{fontSize: 20, color: 'rgba(255,255,255,0.75)', marginTop: 8, letterSpacing: 1.5}}>§ 6 rozporządzenia MEN z 9 sierpnia 2017 r. — t.j. Dz.U. 2020 poz. 1309 · stan na rok szkolny 2026/2027</div>
        </Pojaw>
      </div>
      <div style={{position: 'absolute', left: 80, right: 80, top: 185, background: 'rgba(255,255,255,0.07)', border: '1.5px solid rgba(255,255,255,0.25)', borderRadius: 20, overflow: 'hidden'}}>
        {PRAWO.map(([a, b, c], i) => {
          const w = Math.max(0, Math.min(1, (frame - od[i]) / 10));
          const kolor = c === 'POPRAWIONO' ? MARKA.pomarancz : c === 'UWAGA' ? '#b8860b' : '#4A3AA0';
          return (
            <div key={a} style={{display: 'grid', gridTemplateColumns: '1fr 2.2fr 170px', padding: '17px 26px', borderTop: i ? '1px solid rgba(255,255,255,0.12)' : 'none', opacity: w, transform: `translateX(${(1 - w) * -20}px)`, color: '#fff', fontSize: 22, lineHeight: 1.32, alignItems: 'center', gap: 18}}>
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
    <div style={{position: 'absolute', left: 0, right: 0, top: 160, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
      <Pojaw od={0}><div style={{fontSize: 56, fontWeight: 800, color: '#fff', textAlign: 'center', lineHeight: 1.2}}>Program wynika z oceny<br />zdanie po zdaniu.</div></Pojaw>
      <Pojaw od={logo} style={{marginTop: 50, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
        <Logo rozmiar={120} />
        <div style={{fontSize: 84, fontWeight: 800, color: '#fff', letterSpacing: -2, marginTop: 18, lineHeight: 1}}>EduPlaner <span style={{color: '#F6A57E'}}>2026</span></div>
      </Pojaw>
      <Pojaw od={haslo}>
        <div style={{fontSize: 38, color: '#fff', fontWeight: 700, marginTop: 22}}>Mniej dokumentów. Więcej edukacji.</div>
        <div style={{marginTop: 30, fontSize: 19, color: 'rgba(255,255,255,0.7)', letterSpacing: 2, textAlign: 'center'}}>SZKOŁA PODSTAWOWA · IPET · STRAŻNIK PRAWA<br />PCTP KOSZALIN · kontakt@eduplaner2026.pl · 662 888 403</div>
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
  '.druk-oryginalny .sheet{box-shadow:0 14px 50px rgba(45,27,105,0.22)!important}',
  '.druk-oryginalny table.tbl{border:2.2px solid #2D1B69!important;border-radius:9px}',
  '.druk-oryginalny .tbl thead th,.druk-oryginalny .tbl th{border-bottom:2.2px solid #2D1B69!important}',
  '.druk-oryginalny .tbl td{border-top:1.4px solid #9d90c8!important}',
  '.druk-oryginalny .tbl td + td,.druk-oryginalny .tbl th + th{border-left:1.4px solid #9d90c8!important}',
  '.druk-oryginalny .opt{border:1.6px solid #b3a6dd!important}',
  '.druk-oryginalny .opt.on{border-color:#E8450A!important;background:#fdece4!important}',
  '.druk-oryginalny .chk{border:2.2px solid #6f5fae!important}',
  '.druk-oryginalny .box{border:1.6px solid #b3a6dd!important}',
  '.druk-oryginalny .sec{border-bottom:1.6px solid #d9d0f0;padding-bottom:3px}',
  '.druk-oryginalny .dline,.druk-oryginalny .blank{border-bottom:1.6px dotted #8f81c2!important}',
  '.druk-oryginalny [data-anim-tekst]{color:#1b1730!important}',
].join('\n');

const U = (sek: number, selektor: string, skala: number, gora = 22, czas = 0.75): Ujecie => ({sek, selektor, skala, przesun: Math.round(1080 / skala / 2 - gora), czas});
const Uc = (sek: number, selektor: string, skala: number, przesun: number, czas = 0.75): Ujecie => ({sek, selektor, skala, przesun, czas});
/** Zaznaczenia z druku autorki — klikane w rytm narracji (druk resetuje się co klatkę, więc stan wynika z czasu). */
const kliki = (a: number, start: number, krok: number, pomin: string[] = []): Krok[] =>
  ON.filter((x) => x.a === a && !pomin.includes(x.sel)).map((x, i): Krok => ({sek: start + i * krok, typ: 'klik', selektor: x.sel}));
const OSIEM = Array.from({length: 8}, (_, i) => `@21 .chk #${i}`);

export const IpetPromo: React.FC<Props> = ({film}) => {
  const {fps} = useVideoConfig();
  const n = film.napisy;
  const z = (i: number) => n[i]?.odSek ?? i * 5;
  const kz = (i: number) => n[i]?.doSek ?? i * 5 + 4;
  const granica = (i: number) => (i <= 0 ? 0 : (kz(i - 1) + z(i)) / 2);
  const fr = (sek: number) => Math.round(sek * fps);
  const lok = (od: number) => (s: number) => Math.max(0, fr(s - od));
  const koniec = film.dlugosc;
  const L = (od: number) => lok(od);

  /* --- scena „osiem elementów” (zdania 8–17): karta kontrolna § 6, punkt odhaczany dokładnie wtedy, gdy pada --- */
  const osiemKroki: Krok[] = [
    ...Array.from({length: 8}, (_, i): Krok => ({sek: z(10 + i) + 0.9, typ: 'klik', selektor: `@21 .chk #${i}`})),
    ...Array.from({length: 8}, (_, i): Krok => ({sek: z(10 + i) + 0.6, doSek: kz(10 + i) + 0.4, typ: 'wyroznij', selektor: `@21 tbody tr #${i}`})),
  ];
  const osiemKamera: Ujecie[] = [
    U(0, '@21 .sec #0', 2.3, 22),
    U(z(10) - 0.4, '@21 table.tbl #0', 2.3, 22),
    Uc(z(14) - 0.4, '@21 table.tbl #0', 2.3, 330),
  ];

  /* --- scena „zalecenia z orzeczenia i z oceny” (18–22) --- */
  const zalKamera: Ujecie[] = [
    U(0, '@6 .sec #0', 2.3, 22),
    U(z(19) - 0.4, '@6 .sec #1', 2.3, 22),
    U(z(21) - 0.3, '@6 table.tbl #1', 2.3, 22),
  ];
  const zalKroki: Krok[] = [
    {sek: z(18) + 0.6, doSek: kz(18) + 0.3, typ: 'wyroznij', selektor: '@6 table.tbl #0'},
    {sek: z(19) + 0.4, doSek: kz(20) + 0.3, typ: 'wyroznij', selektor: '@6 table.tbl #1'},
    {sek: z(21) + 0.3, doSek: kz(22), typ: 'wyroznij', selektor: '@6 table.tbl #1'},
  ];

  /* --- scena „dostosowania, zintegrowane działania, UDL” (30–44) --- */
  const D13: [number, string[]][] = [
    [z(31) + 0.5, ['@13 .chk #1', '@13 .chk #8', '@13 .opt #3']],
    [z(32) + 0.5, ['@13 .chk #0', '@13 .chk #4']],
    [z(33) + 0.5, ['@13 .opt #0', '@13 .chk #9', '@13 .chk #10']],
    [z(34) + 0.5, ['@13 .chk #3']],
    [z(35) + 0.5, ['@13 .opt #2', '@13 .opt #6', '@13 .opt #8']],
  ];
  const dostKroki: Krok[] = [
    ...D13.flatMap(([s, sels]) => sels.map((sel, i): Krok => ({sek: s + i * 0.75, typ: 'klik', selektor: sel}))),
    ...kliki(16, z(37) + 0.6, 0.5),
    ...kliki(17, z(39) + 0.4, 0.55),
    {sek: z(36) + 0.4, doSek: kz(36) + 0.3, typ: 'wyroznij', selektor: '@13 .sec #0'},
    {sek: z(38) + 0.4, doSek: kz(38) + 0.3, typ: 'wyroznij', selektor: '@16 .sec #2'},
    {sek: z(43) + 0.4, doSek: kz(44), typ: 'wyroznij', selektor: '@13 .sec #1'},
  ];
  const dostKamera: Ujecie[] = [
    U(0, '@13 .sec #0', 2.3, 22),
    U(z(31) - 0.3, '@13 .sec #0', 2.35, 60),
    Uc(z(33) - 0.3, '@13 .sec #0', 2.3, 300),
    U(z(35) - 0.3, '@13 .sec #1', 2.35, 22),
    U(z(37) - 0.3, '@16 .sec #0', 2.35, 22),
    U(z(38) + 1.5, '@16 .sec #2', 2.35, 22),
    U(z(39) - 0.2, '@17 .sec #0', 2.3, 22),
    U(z(42) - 0.3, '@13 .sec #1', 2.35, 22),
  ];

  /* --- scena „krok po kroku” (45–58): przez cały program --- */
  const K = {
    metryczka: z(46) + 0.3,
    glos: z(47) + 0.2,
    orzecz: z(48) + 0.3,
    ocena: z(49) + 0.3,
    mocne: z(49) + 2.2,
    trud: z(50) + 0.3,
    kszof: z(50) + 3.4,
    sfery: z(51) + 0.4,
    dost: z(52) + 0.4,
    formyA: z(54) + 0.4,
    formyB: z(54) + 4.2,
    zintegr: z(55) + 0.4,
    karta: z(56) + 0.3,
    ewal: z(57) + 0.3,
  };
  const krokiKroki: Krok[] = [
    ...kliki(2, K.glos, 0.32),
    ...kliki(3, K.mocne, 0.3),
    ...kliki(4, K.trud, 0.28),
    ...kliki(5, K.kszof, 0.3),
    ...[7, 8, 9, 10, 11, 12].flatMap((a, j) => kliki(a, K.sfery + j * 2.6, 0.22)),
    ...kliki(13, K.dost, 0.35),
    ...kliki(14, K.formyA, 0.5),
    ...kliki(15, K.formyB, 0.5),
    ...kliki(16, K.zintegr, 0.4),
    ...kliki(21, K.karta, 0.22),
    {sek: K.metryczka + 0.4, doSek: K.glos - 0.3, typ: 'wyroznij', selektor: '@1 .box #0'},
    {sek: K.orzecz + 0.4, doSek: K.ocena - 0.3, typ: 'wyroznij', selektor: '@6 table.tbl #0'},
    ...[7, 8, 9, 10, 11, 12].map((a, j): Krok => ({sek: K.sfery + j * 2.6 + 0.3, doSek: K.sfery + (j + 1) * 2.6 - 0.3, typ: 'wyroznij', selektor: `@${a} .box #0`})),
    {sek: K.karta + 0.4, doSek: z(57) - 0.2, typ: 'wyroznij', selektor: '@21 table.tbl #0'},
    {sek: K.ewal + 0.4, doSek: kz(58), typ: 'wyroznij', selektor: '@18 .box #0'},
  ];
  const krokiKamera: Ujecie[] = [
    U(0, '@1 .box #0', 2.3, 40),
    U(K.glos - 0.3, '@2 .opt #0', 2.35, 60),
    U(K.orzecz - 0.3, '@6 table.tbl #0', 2.3, 22),
    U(K.ocena - 0.3, '@3 .sec #0', 2.35, 22),
    U(K.trud - 0.3, '@4 .sec #0', 2.35, 22),
    U(K.kszof - 0.3, '@5 table.tbl', 2.3, 22),
    ...[7, 8, 9, 10, 11, 12].map((a, j) => Uc(K.sfery + j * 2.6 - 0.25, `@${a} .chk #0`, 2.3, 95, 0.6)),
    U(K.dost - 0.3, '@13 .sec #0', 2.3, 22),
    U(K.formyA - 0.3, '@14 table.tbl', 2.3, 22),
    U(K.formyB - 0.3, '@15 table.tbl', 2.3, 22),
    U(K.zintegr - 0.3, '@16 .sec #0', 2.35, 22),
    U(K.karta - 0.3, '@21 table.tbl #0', 2.3, 22),
    U(K.ewal - 0.3, '@18 .box #0', 2.3, 60),
  ];

  type Scena = {id: string; od: number; do: number; el: (od: number) => React.ReactNode};
  const sceny: Scena[] = [
    {id: 'intro', od: 0, do: granica(1), el: () => <Intro />},
    {id: 'terminy', od: granica(1), do: granica(5), el: (od) => <Terminy dla={L(od)(z(1))} dwa={L(od)(z(2))} t1={L(od)(z(3))} t2={L(od)(z(4))} />},
    {id: 'rodzice', od: granica(5), do: granica(8), el: (od) => <Rodzice tyt={L(od)(z(5))} a={L(od)(z(6))} b={L(od)(z(7))} />},
    {id: 'osiem', od: granica(8), do: granica(18), el: (od) => <OryginalnyDruk plik="ipet-sp.html" kroki={osiemKroki} kamera={osiemKamera} odSek={od} css={CSS_FILMU} />},
    {id: 'zalecenia', od: granica(18), do: granica(23), el: (od) => <OryginalnyDruk plik="ipet-sp.html" kroki={zalKroki} kamera={zalKamera} odSek={od} css={CSS_FILMU} />},
    {id: 'czym', od: granica(23), do: granica(27), el: (od) => <Czym jak={L(od)(z(24))} podstawa={L(od)(z(25))} wyjatek={L(od)(z(26))} />},
    {id: 'przedmiotowo', od: granica(27), do: granica(30), el: (od) => <Przedmiotowo zle={L(od)(z(28))} dobrze={L(od)(z(29))} />},
    {id: 'dostosowania', od: granica(30), do: granica(45), el: (od) => <OryginalnyDruk plik="ipet-sp.html" kroki={dostKroki} kamera={dostKamera} odSek={od} css={CSS_FILMU} />},
    {id: 'kroki', od: granica(45), do: granica(59), el: (od) => <OryginalnyDruk plik="ipet-sp.html" kroki={krokiKroki} kamera={krokiKamera} odSek={od} css={CSS_FILMU} />},
    {id: 'straznik', od: granica(59), do: granica(68), el: (od) => <Straznik od={[60, 62, 63, 64, 65, 67].map((i) => L(od)(z(i)))} />},
    {id: 'final', od: granica(68), do: koniec, el: (od) => <Final logo={L(od)(z(69))} haslo={L(od)(z(70))} />},
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
