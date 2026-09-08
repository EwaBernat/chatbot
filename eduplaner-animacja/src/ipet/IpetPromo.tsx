import React from 'react';
import {AbsoluteFill, Audio, Sequence, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from '../marka';
import {Napisy} from '../Napisy';
import {Logo, Pojaw, useWejscie} from '../ui';
import {OryginalnyDruk, type Krok, type Ujecie} from '../kpof/OryginalnyDruk';
import krokiJson from '../../public/ipet-kroki.json';
import type {Napis} from '../typy';

export type FilmIpet = {audio: string | null; napisy: Napis[]; dlugosc: number};
export type Props = {film: FilmIpet};

type KrokIpet = {faza: string; typ: 'tekst' | 'klik'; k: string; tekst?: string};
const KROKI = krokiJson as KrokIpet[];

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

const IpetIntro: React.FC<{terminy: number}> = ({terminy}) => (
  <Tlo>
    <Pojaw od={0} style={{position: 'absolute', left: 0, right: 0, top: 110, textAlign: 'center'}}>
      <div style={{fontSize: 20, letterSpacing: 4, color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase'}}>EduPlaner 2026 · Ścieżka dziecka · przystanek piąty</div>
      <div style={{fontSize: 66, fontWeight: 800, color: '#fff', marginTop: 12, letterSpacing: -1, lineHeight: 1.1}}>Indywidualny Program<br />Edukacyjno-Terapeutyczny</div>
      <div style={{display: 'inline-block', marginTop: 22, background: MARKA.pomarancz, color: '#fff', fontSize: 22, fontWeight: 700, padding: '10px 26px', borderRadius: 999, letterSpacing: 2}}>IPET · OD OCENY DO ZOBOWIĄZANIA · DZIECKO Z ORZECZENIEM</div>
    </Pojaw>
    <div style={{position: 'absolute', left: 0, right: 0, top: 480, display: 'flex', justifyContent: 'center', gap: 50}}>
      <Karta od={terminy} akcent style={{width: 640, boxShadow: '0 24px 60px rgba(232,69,10,0.45)'}}>
        <div style={{fontSize: 18, letterSpacing: 3, fontWeight: 700, color: 'rgba(255,255,255,0.85)'}}>TERMIN 1</div>
        <div style={{fontSize: 56, fontWeight: 800, lineHeight: 1.05, marginTop: 10}}>do 30 września</div>
        <div style={{fontSize: 22, marginTop: 12, lineHeight: 1.4}}>dla dziecka, które rozpoczyna wychowanie przedszkolne z orzeczeniem o potrzebie kształcenia specjalnego</div>
      </Karta>
      <Karta od={terminy + 10} style={{width: 640}}>
        <div style={{fontSize: 18, letterSpacing: 3, fontWeight: 700, color: '#F6A57E'}}>TERMIN 2</div>
        <div style={{fontSize: 56, fontWeight: 800, lineHeight: 1.05, marginTop: 10}}>30 dni od złożenia orzeczenia</div>
        <div style={{fontSize: 22, marginTop: 12, lineHeight: 1.4, color: 'rgba(255,255,255,0.85)'}}>niezależnie od miesiąca · § 6 rozp. MEN z 9.08.2017 r. (t.j. Dz.U. 2020 poz. 1309)</div>
      </Karta>
    </div>
  </Tlo>
);

const WYMOGI: [string, string, string][] = [
  ['pkt 1', 'Zakres i sposób dostosowania programu wychowania przedszkolnego', 'metody i formy pracy · sekcja 5'],
  ['pkt 2', 'Zintegrowane działania nauczycieli i specjalistów', 'w tym AAC i działania rewalidacyjne · sekcje 4a–4b, sfery 1–6'],
  ['pkt 3', 'Formy, okres i wymiar godzin pomocy psychologiczno-pedagogicznej', 'ustala dyrektor · sekcja 6B'],
  ['pkt 4', 'Działania wspierające rodziców i współdziałanie z poradnią, PDN, NGO, instytucjami', 'sekcje 9–10'],
  ['pkt 5', 'Zajęcia rewalidacyjne i inne zajęcia odpowiednie do potrzeb dziecka', 'sekcja 6A · programy P1–P3'],
  ['pkt 6', 'Zakres współpracy nauczycieli i specjalistów z rodzicami', 'sekcja 9 · plan współpracy'],
  ['pkt 7', 'Dostosowanie warunków organizacji kształcenia i technologie wspomagające', 'sekcja 5b'],
  ['pkt 8', 'Wybrane zajęcia realizowane indywidualnie lub w grupie do 5 dzieci', 'sekcja 6A · WOPF sekcja XVI'],
];

const Straznik: React.FC<{wiersze: number[]; dodatek: number}> = ({wiersze, dodatek}) => {
  const frame = useCurrentFrame();
  const tarcza = useWejscie(0, {damping: 10, stiffness: 120});
  const puls = 1 + 0.03 * Math.sin(frame / 8);
  const wd = useWejscie(dodatek);
  return (
    <Tlo>
      <div style={{position: 'absolute', left: 0, right: 0, top: 40, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 26}}>
        <div style={{width: 96, height: 96, borderRadius: '50%', background: MARKA.pomarancz, display: 'grid', placeItems: 'center', fontSize: 52, transform: `scale(${tarcza * puls})`, boxShadow: '0 16px 40px rgba(232,69,10,0.5)'}}>⚖</div>
        <Pojaw od={2}>
          <div style={{fontSize: 52, fontWeight: 800, color: '#fff', lineHeight: 1}}>Strażnik prawa · co musi zawierać IPET</div>
          <div style={{fontSize: 20, color: 'rgba(255,255,255,0.75)', marginTop: 8, letterSpacing: 1.5}}>§ 6 ust. 1 rozp. MEN z 9.08.2017 r. w sprawie kształcenia specjalnego · t.j. Dz.U. 2020 poz. 1309 · wg skryptu szkolenia, wyd. 2 po audycie z 5.09.2026</div>
        </Pojaw>
      </div>
      <div style={{position: 'absolute', left: 90, right: 90, top: 180, background: 'rgba(255,255,255,0.07)', border: '1.5px solid rgba(255,255,255,0.25)', borderRadius: 20, overflow: 'hidden'}}>
        {WYMOGI.map(([pkt, co, gdzie], i) => {
          const w = Math.max(0, Math.min(1, (frame - wiersze[i]) / 10));
          return (
            <div key={pkt} style={{display: 'grid', gridTemplateColumns: '150px 1fr 520px', padding: '13px 24px', borderTop: i ? '1px solid rgba(255,255,255,0.12)' : 'none', opacity: w, transform: `translateX(${(1 - w) * -20}px)`, color: '#fff', fontSize: 23, lineHeight: 1.3, alignItems: 'center'}}>
              <div><span style={{display: 'inline-block', background: MARKA.pomarancz, color: '#fff', fontWeight: 800, fontSize: 18, padding: '5px 14px', borderRadius: 999, letterSpacing: 1}}>§ 6 ust. 1 {pkt}</span></div>
              <div style={{fontWeight: 700, paddingRight: 16}}>{co}</div>
              <div style={{color: 'rgba(255,255,255,0.75)', fontSize: 19}}>✓ w druku: {gdzie}</div>
            </div>
          );
        })}
      </div>
      <div style={{position: 'absolute', left: 90, right: 90, bottom: 112, textAlign: 'center', opacity: wd, transform: `translateY(${(1 - wd) * 20}px)`}}>
        <span style={{display: 'inline-block', border: '2px solid #F6A57E', color: '#fff', borderRadius: 999, padding: '12px 30px', fontSize: 21, fontWeight: 700, lineHeight: 1.35}}>
          Do tego: program po WOPF z zaleceniami z orzeczenia (ust. 4) · termin 30 IX / 30 dni (ust. 5) · ocena co najmniej 2× w roku · prawa rodziców · autyzm: AAC + TUS (ust. 2), nauczyciel współorganizujący (§ 7 ust. 2)
        </span>
      </div>
    </Tlo>
  );
};

const IpetFinal: React.FC<{haslo: number}> = ({haslo}) => (
  <Tlo>
    <div style={{position: 'absolute', left: 0, right: 0, top: 220, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
      <Logo rozmiar={130} />
      <div style={{fontSize: 92, fontWeight: 800, color: '#fff', letterSpacing: -2, marginTop: 22, lineHeight: 1}}>EduPlaner <span style={{color: '#F6A57E'}}>2026</span></div>
      <Pojaw od={haslo}>
        <div style={{fontSize: 40, color: '#fff', fontWeight: 700, marginTop: 22}}>Mniej dokumentów. Więcej edukacji.</div>
      </Pojaw>
      <Pojaw od={haslo + 20}>
        <div style={{marginTop: 40, fontSize: 20, color: 'rgba(255,255,255,0.7)', letterSpacing: 2}}>IPET NA ORYGINALNYM DRUKU · DANE Z KPOF, WOPF I OBSERWACJI POGŁĘBIONEJ · STRAŻNIK PRAWA</div>
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

/** Kroki z ipet-kroki.json ułożone w czasie: faza → (start, koniec, tempo znaków/s). */
const rozloz = (okna: Record<string, [number, number, number?]>): Krok[] => {
  const kroki: Krok[] = [];
  const grupy: Record<string, KrokIpet[]> = {};
  for (const k of KROKI) (grupy[k.faza] ??= []).push(k);
  for (const [faza, [od, do_, tempo]] of Object.entries(okna)) {
    const g = grupy[faza] ?? [];
    const dt = g.length > 1 ? (do_ - od) / g.length : 0;
    g.forEach((k, i) => {
      const selektor = `[data-k="${k.k}"]`;
      if (k.typ === 'klik') kroki.push({sek: od + i * dt, typ: 'klik', selektor});
      else kroki.push({sek: od + i * dt, typ: 'tekst', selektor, tekst: k.tekst ?? '', tempo: tempo ?? 30});
    });
  }
  return kroki;
};

export const IpetPromo: React.FC<Props> = ({film}) => {
  const {fps} = useVideoConfig();
  const n = film.napisy;
  const z = (i: number) => n[i]?.odSek ?? i * 5;
  const kz = (i: number) => n[i]?.doSek ?? i * 5 + 4;
  const granica = (i: number) => (i <= 0 ? 0 : (kz(i - 1) + z(i)) / 2);
  const fr = (sek: number) => Math.round(sek * fps);
  const lok = (od: number) => (s: number) => Math.max(0, fr(s - od));
  const koniec = film.dlugosc;

  const drukOd = granica(2);
  const kroki = rozloz({
    dane: [z(2) + 0.2, kz(2), 40],
    glos: [z(3) + 0.2, kz(3), 36],
    glos2: [z(4) + 0.2, z(4) + 0.3, 50],
    kpof: [z(5) + 0.2, kz(5) - 0.5, 200],
    poziom: [z(6) + 0.6, z(6) + 0.7],
    zorz: [z(7) + 0.3, kz(8), 55],
    zwopf: [z(9) + 0.2, kz(9), 90],
    sf2: [z(10) + 0.2, kz(10), 50],
    sf2cel: [z(11) + 0.2, z(11) + 4, 30],
    sf2b: [z(12) + 0.2, kz(12), 50],
    zint: [z(13) + 0.2, kz(13), 60],
    dost: [z(14) + 0.2, kz(14), 60],
    rew: [z(15) + 0.2, kz(15), 40],
    nw: [z(16) + 0.2, kz(16), 40],
    zespol: [z(17) + 0.2, kz(17), 60],
    ewal: [z(18) + 0.3, z(18) + 0.4, 40],
    kk: [z(19) + 0.2, z(19) + 3.5],
    kk2: [z(19) + 3.6, kz(19), 60],
  });
  const kamera: Ujecie[] = [
    {sek: 0, selektor: '@1 .tt-h1', skala: 1.35, przesun: 120},
    {sek: z(2), selektor: '@1 .fields', skala: 1.5, przesun: 120},
    {sek: z(3), selektor: '@2 .checks', skala: 1.5, przesun: 150},
    {sek: z(4), selektor: '@2 .ta', skala: 1.55, przesun: 110},
    {sek: z(5), selektor: '@6 table', skala: 1.45, przesun: 130},
    {sek: z(6), selektor: '@6 table', skala: 1.5, przesun: 330},
    {sek: z(7), selektor: '@9 table', skala: 1.4, przesun: 110},
    {sek: z(8) + 1.5, selektor: '@9 table', skala: 1.4, przesun: 330},
    {sek: z(9), selektor: '@12 table', skala: 1.35, przesun: 230},
    {sek: z(10), selektor: '@15 .sfera', skala: 1.5, przesun: 140},
    {sek: z(11), selektor: '@15 .smart', skala: 1.6, przesun: 80},
    {sek: z(12), selektor: '@15 .smart', skala: 1.45, przesun: 200},
    {sek: z(13), selektor: '@25 .checks', skala: 1.45, przesun: 150},
    {sek: z(14), selektor: '@27 .pair', skala: 1.45, przesun: 160},
    {sek: z(15), selektor: '@28 table', skala: 1.35, przesun: 230},
    {sek: z(16), selektor: '@30 .fields', skala: 1.5, przesun: 110},
    {sek: z(17), selektor: '@32 table', skala: 1.4, przesun: 130},
    {sek: z(18), selektor: '@32 .checks', skala: 1.5, przesun: 150},
    {sek: z(19), selektor: '@40 table', skala: 1.3, przesun: 260},
  ];
  const META: Krok[] = [];
  for (const pg of [1, 2, 6, 9, 12, 15, 25, 27, 28, 30, 32, 40]) {
    (['Zofia Lewandowska', 'Biedronki', '30.09.2026'] as const).forEach((t, i) => META.push({sek: 0, typ: 'tekst', selektor: `@${pg} [data-k="meta:${i}"]`, tekst: t, tempo: 10000}));
  }
  const wyr: Krok[] = [
    {sek: z(11) + 0.1, doSek: kz(12) + 0.3, typ: 'wyroznij', selektor: '@15 .smart'},
    {sek: z(6) + 0.6, doSek: kz(6) + 0.3, typ: 'wyroznij', selektor: '@6 [data-k="kpof_poziom:II"]'},
    {sek: z(16) + 0.1, doSek: kz(16) + 0.3, typ: 'wyroznij', selektor: '@30 .fields'},
  ];

  type Scena = {id: string; od: number; do: number; el: (od: number) => React.ReactNode};
  const sceny: Scena[] = [
    {id: 'intro', od: 0, do: drukOd, el: (od) => <IpetIntro terminy={lok(od)(z(1))} />},
    {id: 'druk', od: drukOd, do: granica(20), el: (od) => <OryginalnyDruk plik="ipet.html" kroki={[...META, ...kroki, ...wyr]} kamera={kamera} odSek={od} />},
    {id: 'straznik', od: granica(20), do: granica(31), el: (od) => <Straznik wiersze={[22, 23, 24, 25, 26, 27, 28, 29].map((i) => lok(od)(z(i)))} dodatek={lok(od)(z(30))} />},
    {id: 'final', od: granica(31), do: koniec, el: (od) => <IpetFinal haslo={lok(od)(z(32))} />},
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
