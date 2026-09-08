import React from 'react';
import {AbsoluteFill, Audio, Sequence, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from '../marka';
import {Napisy} from '../Napisy';
import {Logo, Pojaw, useWejscie} from '../ui';
import {OryginalnyDruk, type Krok, type Ujecie} from '../kpof/OryginalnyDruk';
import type {Napis} from '../typy';
import krokiDruku from '../../public/metryczka-sp-kroki.json';

export type FilmSp = {audio: string | null; napisy: Napis[]; dlugosc: number};
export type Props = {film: FilmSp};

type KrokDruku = {f: string; sel: string; t?: string; k?: number};
const KROKI = (krokiDruku as {kroki: KrokDruku[]}).kroki;

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
const Pastylka: React.FC<{od: number; children: React.ReactNode}> = ({od, children}) => (
  <Pojaw od={od} style={{position: 'absolute', left: 0, right: 0, bottom: 150, textAlign: 'center'}}>
    <span style={{display: 'inline-block', border: '2px solid #F6A57E', color: '#fff', borderRadius: 999, padding: '12px 30px', fontSize: 22, fontWeight: 700}}>{children}</span>
  </Pojaw>
);

const Intro: React.FC<{sub: number}> = ({sub}) => (
  <Tlo>
    <Pojaw od={0} style={{position: 'absolute', left: 0, right: 0, top: 150, textAlign: 'center'}}>
      <div style={{fontSize: 20, letterSpacing: 4, color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase'}}>EduPlaner 2026 · Szkoła podstawowa · przystanek pierwszy</div>
      <div style={{fontSize: 92, fontWeight: 800, color: '#fff', marginTop: 12, letterSpacing: -2, lineHeight: 1.05}}>Metryczka <span style={{color: '#F6A57E'}}>ucznia</span></div>
      <div style={{fontSize: 40, fontWeight: 700, color: '#fff', marginTop: 14}}>teczka, zmiany w prawie i pierwszy druk</div>
      <div style={{display: 'inline-block', marginTop: 26, background: MARKA.pomarancz, color: '#fff', fontSize: 21, fontWeight: 700, padding: '10px 26px', borderRadius: 999, letterSpacing: 2}}>ZGŁOSZENIE · WOPFU · IPET · EWALUACJA</div>
    </Pojaw>
    <div style={{position: 'absolute', left: 0, right: 0, top: 640, display: 'flex', justifyContent: 'center'}}>
      <Karta od={sub} akcent style={{width: 1100, textAlign: 'center', fontSize: 30, fontWeight: 700, lineHeight: 1.4}}>Zanim otworzymy druk — jedno pytanie z każdej rady pedagogicznej</Karta>
    </div>
  </Tlo>
);

const Pytanie: React.FC<{pyt: number; odp: number; nie: number; jezyk: number}> = ({pyt, odp, nie, jezyk}) => (
  <Tlo>
    <Naglowek kicker="Pytanie nauczycieli szkoły specjalnej" tytul="Czy nasza dokumentacja może zostać jak w zeszłym roku?" />
    <div style={{position: 'absolute', left: 120, right: 120, top: 250}}>
      <Karta od={pyt} style={{fontSize: 30, lineHeight: 1.45, fontStyle: 'italic', borderLeft: `8px solid #F6A57E`}}>
        „Mamy teczki, oceny wielospecjalistyczne i programy. Czy naprawdę musimy to zmieniać?”
      </Karta>
      <div style={{display: 'flex', gap: 26, marginTop: 26}}>
        <Karta od={odp} akcent style={{flex: 1.1, boxShadow: '0 24px 60px rgba(232,69,10,0.45)'}}>
          <div style={{fontSize: 18, letterSpacing: 3, fontWeight: 800, color: 'rgba(255,255,255,0.85)'}}>ODPOWIEDŹ</div>
          <div style={{fontSize: 44, fontWeight: 800, marginTop: 8, lineHeight: 1.15}}>Nie zaczynamy od zera.<br />Aktualizujemy.</div>
        </Karta>
        <Karta od={nie} style={{flex: 1}}>
          <div style={{fontSize: 18, letterSpacing: 3, fontWeight: 800, color: '#F6A57E'}}>CZEGO NIE ROBIMY</div>
          <div style={{fontSize: 26, marginTop: 10, lineHeight: 1.4}}>✗ nie przepisujemy dokumentów już sporządzonych<br />✗ nie unieważniamy dotychczasowych ocen ani programów<br />✗ nie tworzymy druków ponad przepis i procedurę</div>
        </Karta>
      </div>
      <Karta od={jezyk} style={{marginTop: 26, textAlign: 'center', fontSize: 28, fontWeight: 700, lineHeight: 1.4, borderColor: '#F6A57E'}}>
        Od 1 września 2026 zmienia się <span style={{color: '#F6A57E'}}>nie objętość</span> dokumentacji, lecz jej <span style={{color: '#F6A57E'}}>język i funkcja</span> — dokument w starym języku przestaje działać w nowym obiegu.
      </Karta>
    </div>
  </Tlo>
);

const POWODY: [string, string, string, string][] = [
  ['Orzeczenie w języku ICF', 'poradnia opiera orzeczenie na ocenie funkcjonalnej — opis aktywności i uczestniczenia, nie samej diagnozy', '§ 7 ust. 7 rozp. ME z 2.03.2026 r. (Dz.U. 2026 poz. 428)', '#6C4CC4'],
  ['Opinia szkoły w 10 dni', 'termin liczy się od wpływu prośby do dyrektora; ucznia klasy VII uczy nawet 12 nauczycieli — dane muszą już istnieć', '§ 7 ust. 2–3 rozp. ME z 2.03.2026 r. (Dz.U. 2026 poz. 428)', '#E8450A'],
  ['Program po ocenie i na jej podstawie', 'każdy wniosek ma źródło, każde zalecenie — formę, osobę, wymiar godzin i datę realizacji', '§ 6 rozp. MEN z 9.08.2017 r. (t.j. Dz.U. 2020 poz. 1309)', '#C47A10'],
  ['Cel z kryterium = ocena efektywności', 'bez liczby w celu nie da się ocenić efektywności, a ocena efektywności jest obowiązkiem zespołu', '§ 6 ust. 9 rozp. MEN z 9.08.2017 r. (t.j. Dz.U. 2020 poz. 1309)', '#1f8a5b'],
  ['Dokumentacja jako dowód wydatkowania', 'środki naliczone na kształcenie specjalne wydatkuje się na jego organizację — teczka ucznia jest jedynym dowodem', 'art. 8 ust. 16–17 ustawy z 27.10.2017 r. o finansowaniu zadań oświatowych', '#2F8F8A'],
];
const Powody: React.FC<{od: number[]}> = ({od}) => (
  <Tlo>
    <Naglowek kicker="Dlaczego aktualizujemy — pięć powodów ze skryptu (z dziesięciu)" tytul="Każdy powód ma swoją podstawę prawną" />
    <div style={{position: 'absolute', left: 70, right: 70, top: 228, display: 'grid', gridTemplateColumns: 'repeat(5, 1fr)', gap: 18}}>
      {POWODY.map(([t, o, p, k], i) => (
        <Karta key={t} od={od[i]} style={{padding: '22px 18px', minHeight: 560, borderColor: 'rgba(255,255,255,0.35)', display: 'flex', flexDirection: 'column'}}>
          <div style={{width: 64, height: 64, borderRadius: '50%', background: k, display: 'grid', placeItems: 'center', fontSize: 32, fontWeight: 800, boxShadow: '0 12px 30px rgba(0,0,0,0.3)'}}>{i + 1}</div>
          <div style={{fontSize: 27, fontWeight: 800, marginTop: 16, lineHeight: 1.15}}>{t}</div>
          <div style={{fontSize: 20, marginTop: 12, lineHeight: 1.38, color: 'rgba(255,255,255,0.88)', flex: 1}}>{o}</div>
          <div style={{marginTop: 14, background: 'rgba(0,0,0,0.25)', borderRadius: 10, padding: '8px 10px', fontSize: 15.5, lineHeight: 1.35, color: '#F6A57E', fontWeight: 700}}>{p}</div>
        </Karta>
      ))}
    </div>
    <Pastylka od={od[4] + 20}>pełna tabela dziesięciu powodów dla dyrektora i rady pedagogicznej — skrypt szkolenia, część 1</Pastylka>
  </Tlo>
);

const PRZEPISY: [string, string, string, string, string][] = [
  ['Orzekanie i opinie', 'rozp. ME z 2.03.2026 r. — Dz.U. 2026 poz. 428', 'od 1.09.2026: ocena funkcjonalna przed orzeczeniem, opinia szkoły w 10 dni, opis w kategoriach aktywności i uczestniczenia (ICF)', 'NOWE', '#E8450A'],
  ['Kształcenie specjalne', 'rozp. MEN z 9.08.2017 r. — t.j. Dz.U. 2020 poz. 1309', 'cytujemy tekst jednolity, nie pierwotny publikator Dz.U. 2017 poz. 1578 — WOPFU, IPET, nauczyciel współorganizujący', 'TEKST JEDNOLITY', '#6C4CC4'],
  ['Pomoc psychologiczno-pedagogiczna', 'rozp. MEN z 9.08.2017 r. — t.j. Dz.U. 2023 poz. 1798', 'formy pomocy w szkole, zindywidualizowana ścieżka kształcenia (§ 12), ocena efektywności pomocy', 'TEKST JEDNOLITY', '#6C4CC4'],
  ['Dokumentacja przebiegu nauczania', 'rozp. MEN z 25.08.2017 r. — t.j. Dz.U. 2024 poz. 50', 'księga uczniów, dzienniki zajęć, arkusze ocen, dokumentacja badań i czynności uzupełniających — podstawa teczki ucznia', 'TEKST JEDNOLITY', '#6C4CC4'],
];
const Przepisy: React.FC<{tytul: number; od: number[]; nie: number}> = ({tytul, od, nie}) => {
  const frame = useCurrentFrame();
  return (
    <Tlo>
      <Naglowek od={tytul} kicker="Zmiany w prawie oświatowym i w orzecznictwie — rok szkolny 2026/2027" tytul="Co zmieniło się w przepisach?" />
      <div style={{position: 'absolute', left: 90, right: 90, top: 218, background: 'rgba(255,255,255,0.07)', border: '1.5px solid rgba(255,255,255,0.25)', borderRadius: 20, overflow: 'hidden'}}>
        {PRZEPISY.map(([a, b, c, d, k], i) => {
          const w = Math.max(0, Math.min(1, (frame - od[i]) / 10));
          return (
            <div key={a} style={{display: 'grid', gridTemplateColumns: '300px 1fr 200px', padding: '18px 26px', borderTop: i ? '1px solid rgba(255,255,255,0.12)' : 'none', opacity: w, transform: `translateX(${(1 - w) * -20}px)`, color: '#fff', alignItems: 'center', gap: 22}}>
              <div>
                <div style={{fontSize: 25, fontWeight: 800, lineHeight: 1.15}}>{a}</div>
                <div style={{fontSize: 17, color: '#F6A57E', fontWeight: 700, marginTop: 6, lineHeight: 1.3}}>{b}</div>
              </div>
              <div style={{fontSize: 21.5, lineHeight: 1.38, color: 'rgba(255,255,255,0.92)'}}>{c}</div>
              <div style={{textAlign: 'center'}}><span style={{display: 'inline-block', background: k, color: '#fff', fontWeight: 800, fontSize: 15, padding: '7px 14px', borderRadius: 999, letterSpacing: 1}}>{d}</span></div>
            </div>
          );
        })}
      </div>
      <div style={{position: 'absolute', left: 90, right: 90, bottom: 130}}>
        <Karta od={nie} akcent style={{textAlign: 'center', fontSize: 26, fontWeight: 700, lineHeight: 1.4}}>
          Czego nie zmieniamy: nie tworzymy druków ponad przepis i procedurę — dotychczasowe zapisy zostają w teczce jako historia wsparcia ucznia.
        </Karta>
      </div>
    </Tlo>
  );
};

const PRAWO: [string, string, string][] = [
  ['Prawo oświatowe', 'ustawa z 14.12.2016 r., art. 1 i art. 127 — w druku było t.j. Dz.U. 2024 poz. 737; obowiązuje t.j. Dz.U. 2026 poz. 820', 'POPRAWIONO'],
  ['Kształcenie specjalne · pomoc pp', 'rozp. MEN z 9.08.2017 r. — t.j. Dz.U. 2020 poz. 1309 oraz t.j. Dz.U. 2023 poz. 1798', '✓ zgodne'],
  ['Organizacja szkół · dostępność · RODO', 't.j. Dz.U. 2023 poz. 2736 · t.j. Dz.U. 2024 poz. 1411 · rozp. (UE) 2016/679, art. 6 i 9', '✓ zgodne'],
  ['Dokumentacja przebiegu nauczania', 'rozp. MEN z 25.08.2017 r. — t.j. Dz.U. 2024 poz. 50; podstawa teczki ucznia — dopisana do sekcji XIV', 'DOPISANO'],
  ['Zasada Strażnika', 'publikator sprawdzamy w ISAP (isap.sejm.gov.pl) bezpośrednio przed wpisaniem go do dokumentu ucznia', 'ISAP'],
];
const Straznik: React.FC<{od: number[]}> = ({od}) => {
  const frame = useCurrentFrame();
  const tarcza = useWejscie(0, {damping: 10, stiffness: 120});
  return (
    <Tlo>
      <div style={{position: 'absolute', left: 0, right: 0, top: 44, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 26}}>
        <div style={{width: 96, height: 96, borderRadius: '50%', background: MARKA.pomarancz, display: 'grid', placeItems: 'center', fontSize: 52, transform: `scale(${tarcza * (1 + 0.03 * Math.sin(frame / 8))})`, boxShadow: '0 16px 40px rgba(232,69,10,0.5)'}}>⚖</div>
        <Pojaw od={2}>
          <div style={{fontSize: 56, fontWeight: 800, color: '#fff', lineHeight: 1}}>Strażnik prawa · Metryczka ucznia</div>
          <div style={{fontSize: 20, color: 'rgba(255,255,255,0.75)', marginTop: 8, letterSpacing: 1.5}}>publikatory z sekcji XIV druku sprawdzone ze skryptem szkolenia dla szkoły podstawowej</div>
        </Pojaw>
      </div>
      <div style={{position: 'absolute', left: 90, right: 90, top: 200, background: 'rgba(255,255,255,0.07)', border: '1.5px solid rgba(255,255,255,0.25)', borderRadius: 20, overflow: 'hidden'}}>
        {PRAWO.map(([a, b, c], i) => {
          const w = Math.max(0, Math.min(1, (frame - od[i]) / 10));
          const kolor = c.startsWith('✓') ? '#2E9E52' : c === 'ISAP' ? '#2F8F8A' : MARKA.pomarancz;
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
      <Pojaw od={0}><div style={{fontSize: 56, fontWeight: 800, color: '#fff', textAlign: 'center', lineHeight: 1.2}}>Każdy druk ma swój przepis —<br />i my go znamy.</div></Pojaw>
      <Pojaw od={logo} style={{marginTop: 50, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
        <Logo rozmiar={120} />
        <div style={{fontSize: 84, fontWeight: 800, color: '#fff', letterSpacing: -2, marginTop: 18, lineHeight: 1}}>EduPlaner <span style={{color: '#F6A57E'}}>2026</span></div>
      </Pojaw>
      <Pojaw od={haslo}>
        <div style={{fontSize: 38, color: '#fff', fontWeight: 700, marginTop: 22}}>Mniej dokumentów. Więcej edukacji.</div>
        <div style={{marginTop: 30, fontSize: 19, color: 'rgba(255,255,255,0.7)', letterSpacing: 2, textAlign: 'center'}}>SZKOŁA PODSTAWOWA · METRYCZKA UCZNIA · TECZKA · STRAŻNIK PRAWA<br />PCTP KOSZALIN · kontakt@eduplaner2026.pl · 662 888 403</div>
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

/** Kroki wypełniania z public/metryczka-sp-kroki.json rozłożone w czasie narracji: faza → (start, odstęp, tempo znaków/s). */
const rozloz = (faza: string, start: number, odstep: number, tempo: number, filtr?: (k: KrokDruku, i: number) => boolean): Krok[] => {
  const lista = KROKI.filter((k) => k.f === faza).filter((k, i) => (filtr ? filtr(k, i) : true));
  return lista.map((k, i) =>
    k.k ? {sek: start + i * odstep, typ: 'klik' as const, selektor: k.sel} : {sek: start + i * odstep, typ: 'tekst' as const, selektor: k.sel, tekst: k.t ?? '', tempo},
  );
};

export const MetryczkaSpPromo: React.FC<Props> = ({film}) => {
  const {fps} = useVideoConfig();
  const n = film.napisy;
  const z = (i: number) => n[i]?.odSek ?? i * 5;
  const kz = (i: number) => n[i]?.doSek ?? i * 5 + 4;
  const granica = (i: number) => (i <= 0 ? 0 : (kz(i - 1) + z(i)) / 2);
  const fr = (sek: number) => Math.round(sek * fps);
  const lok = (od: number) => (s: number) => Math.max(0, fr(s - od));
  const koniec = film.dlugosc;

  // --- metryczka: oryginalny druk z aplikacji (6 arkuszy A4)
  const jestBlank = (k: KrokDruku) => k.sel.includes('.blankline');
  const kroki: Krok[] = [
    ...rozloz('meta', 0, 0, 999),
    ...rozloz('dane', z(17) + 0.4, 2.3, 30),
    ...rozloz('szkola', z(18) + 0.3, 1.5, 40),
    ...rozloz('orz', z(19) + 0.3, 2.2, 30),
    {sek: z(20) + 0.3, doSek: kz(20) + 0.4, typ: 'wyroznij', selektor: '@1 .blankline #2'},
    ...rozloz('zgl', z(21) + 0.4, 1.4, 60),
    ...rozloz('sciezka', z(21) + 7.6, 0, 60),
    ...rozloz('zespol', z(22) + 0.3, 0.85, 40, jestBlank),
    ...rozloz('zespol', z(22) + 2.8, 0.36, 80, (k) => !jestBlank(k)),
    ...rozloz('audyt', z(23) + 0.8, 1.3, 60),
    ...rozloz('med', z(24) + 0.3, 3.4, 60),
    ...rozloz('synteza', z(25) + 0.3, 0, 90),
    ...rozloz('dost', z(26) + 0.3, 0.5, 70),
    ...rozloz('wsp', z(26) + 4.6, 0.9, 60),
    ...rozloz('glos', z(27) + 0.3, 1.0, 90),
    ...rozloz('zgody', z(28) + 0.3, 0.7, 60),
    ...rozloz('teczka', z(28) + 2.2, 0.35, 60),
    ...rozloz('podpisy', z(28) + 5.4, 0.6, 60, jestBlank),
    ...rozloz('podpisy', z(28) + 7.0, 0.25, 100, (k) => !jestBlank(k)),
  ];
  // Powiększenie ~2× (jak w filmie przedszkolnym: jedna sekcja na ekran, czcionka ok. 24 px w kadrze 1080p)
  const S = 2.05;
  const kamera: Ujecie[] = [
    {sek: 0, selektor: '@1 .eyebrow', skala: 1.75, przesun: 150},
    {sek: z(17), selektor: '@1 .sec #0', skala: S, przesun: 205},
    {sek: z(18), selektor: '@1 .sec #1', skala: S, przesun: 215},
    {sek: z(19), selektor: '@2 .sec #0', skala: S, przesun: 175},
    {sek: z(20), selektor: '@1 .blankline #2', skala: 2.3, przesun: -30},
    {sek: z(21), selektor: '@2 .sec #1', skala: 1.9, przesun: 225},
    {sek: z(21) + 6.5, selektor: '@2 .sec #2', skala: S, przesun: 80},
    {sek: z(22), selektor: '@3 .sec #0', skala: 1.95, przesun: 225},
    {sek: z(23), selektor: '@3 .sec #1', skala: S, przesun: 150},
    {sek: z(24), selektor: '@3 .box #0', skala: S, przesun: 20},
    {sek: z(25), selektor: '@3 .sec #2', skala: S, przesun: 110},
    {sek: z(26), selektor: '@4 .sec #0', skala: 1.9, przesun: 220},
    {sek: z(26) + 4.4, selektor: '@4 .sec #1', skala: S, przesun: 130},
    {sek: z(27), selektor: '@4 .sec #2', skala: 1.9, przesun: 220},
    {sek: z(28), selektor: '@5 .sec #0', skala: S, przesun: 150},
    {sek: z(28) + 2.0, selektor: '@5 .sec #1', skala: 1.9, przesun: 200},
    {sek: z(28) + 5.2, selektor: '@6 .sec #1', skala: 1.9, przesun: 230},
    {sek: z(29), selektor: '@1 .eyebrow', skala: 1.75, przesun: 150},
  ];
  // Tylko na czas filmu: wyraźniejsze ramki i linie (plik druku pozostaje bez zmian)
  const cssFilmu = [
    '.addrow,.delrow,.delcell,.printcell{display:none!important}',
    '.druk-oryginalny .sheet{--hair:#b3a9d8;box-shadow:0 10px 40px rgba(45,27,105,0.18)}',
    '.druk-oryginalny .fg,.druk-oryginalny .box,.druk-oryginalny .opt{border-width:1.3px}',
    '.druk-oryginalny .fg .blankline,.druk-oryginalny .dline{border-bottom-color:#9a8ecb}',
    '.druk-oryginalny table.tbl td{border-top-color:#cfc8e6}',
    // Układ pól wypełnianych (jak po inicjalizacji skryptu druku) — niezależnie od momentu uruchomienia skryptu przy renderze
    '.druk-oryginalny .blankline,.druk-oryginalny .dline,.druk-oryginalny .blank,.druk-oryginalny .box{overflow-wrap:break-word;word-break:normal;white-space:normal}',
    '.druk-oryginalny .dline,.druk-oryginalny .blank{display:inline-block;max-width:100%;height:auto;min-height:15px;min-width:40px;box-sizing:border-box;vertical-align:top}',
    '.druk-oryginalny .fg .blankline,.druk-oryginalny .blankline{display:block;width:100%;max-width:100%;height:auto;min-height:15px;box-sizing:border-box}',
    '.druk-oryginalny table.tbl td .dline{display:block;width:100%;max-width:100%}',
  ].join('\n');

  type Scena = {id: string; od: number; do: number; el: (od: number) => React.ReactNode};
  const sceny: Scena[] = [
    {id: 'intro', od: 0, do: granica(2), el: (od) => <Intro sub={lok(od)(z(1))} />},
    {id: 'pytanie', od: granica(2), do: granica(6), el: (od) => <Pytanie pyt={lok(od)(z(2))} odp={lok(od)(z(3))} nie={lok(od)(z(4))} jezyk={lok(od)(z(5))} />},
    {id: 'powody', od: granica(6), do: granica(11), el: (od) => <Powody od={[6, 7, 8, 9, 10].map((i) => lok(od)(z(i)))} />},
    {id: 'przepisy', od: granica(11), do: granica(16), el: (od) => <Przepisy tytul={lok(od)(z(11))} od={[z(12), z(13), z(14), z(14) + 6.5].map(lok(od))} nie={lok(od)(z(15))} />},
    {id: 'druk', od: granica(16), do: granica(30), el: (od) => <OryginalnyDruk plik="metryczka-sp.html" kroki={kroki} kamera={kamera} odSek={od} css={cssFilmu} />},
    {id: 'straznik', od: granica(30), do: granica(35), el: (od) => <Straznik od={[31, 32, 32, 33, 34].map((i, j) => lok(od)(z(i) + (j === 2 ? 3.2 : 0)))} />},
    {id: 'final', od: granica(35), do: koniec, el: (od) => <Final logo={lok(od)(z(36))} haslo={lok(od)(z(37))} />},
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
