import React from 'react';
import {AbsoluteFill, Audio, Sequence, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from '../marka';
import {Napisy} from '../Napisy';
import {Logo, Pojaw, useWejscie} from '../ui';
import {OryginalnyDruk, type Krok, type Ujecie} from '../kpof/OryginalnyDruk';
import type {Napis} from '../typy';

export type FilmCele = {audio: string | null; napisy: Napis[]; dlugosc: number};
export type Props = {film: FilmCele};

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
  <Pojaw od={od} style={{position: 'absolute', left: 0, right: 0, top: 70, textAlign: 'center'}}>
    <div style={{fontSize: 19, letterSpacing: 4, color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase'}}>{kicker}</div>
    <div style={{fontSize: 58, fontWeight: 800, color: '#fff', marginTop: 10, letterSpacing: -1, lineHeight: 1.1}}>{tytul}</div>
  </Pojaw>
);

const Intro: React.FC<{sub: number}> = ({sub}) => (
  <Tlo>
    <Pojaw od={0} style={{position: 'absolute', left: 0, right: 0, top: 150, textAlign: 'center'}}>
      <div style={{fontSize: 20, letterSpacing: 4, color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase'}}>EduPlaner 2026 · Ścieżka dziecka · przystanek szósty</div>
      <div style={{fontSize: 96, fontWeight: 800, color: '#fff', marginTop: 12, letterSpacing: -2, lineHeight: 1.05}}>Cele <span style={{color: '#F6A57E'}}>SMART</span></div>
      <div style={{fontSize: 40, fontWeight: 700, color: '#fff', marginTop: 14}}>od obserwacji do celu, który ma liczbę</div>
      <div style={{display: 'inline-block', marginTop: 26, background: MARKA.pomarancz, color: '#fff', fontSize: 21, fontWeight: 700, padding: '10px 26px', borderRadius: 999, letterSpacing: 2}}>KPOF · WOPF · IPET · EWALUACJA</div>
    </Pojaw>
    <div style={{position: 'absolute', left: 0, right: 0, top: 640, display: 'flex', justifyContent: 'center'}}>
      <Karta od={sub} akcent style={{width: 1100, textAlign: 'center', fontSize: 30, fontWeight: 700, lineHeight: 1.4}}>Każdy cel musi mieć kryterium, do którego da się porównać wynik</Karta>
    </div>
  </Tlo>
);

const LITERY: [string, string, string, string][] = [
  ['S', 'konkretny', 'jakie zachowanie i w jakiej sytuacji', '#2D1B69'],
  ['M', 'mierzalny', 'ile razy z ilu prób i przy jakim wsparciu', '#E8450A'],
  ['A', 'osiągalny', 'jeden krok od tego, co dziecko robi dziś', '#C47A10'],
  ['R', 'istotny', 'wynika z oceny i zwiększa uczestnictwo dziecka', '#1f8a5b'],
  ['T', 'określony w czasie', 'do kiedy i kiedy sprawdzamy', '#2F8F8A'],
];
const Smart: React.FC<{od: number[]; sub: number}> = ({od, sub}) => (
  <Tlo>
    <Naglowek kicker="Czym są cele SMART?" tytul="Pięć liter, jedna zasada" />
    <Pojaw od={sub} style={{position: 'absolute', left: 0, right: 0, top: 232, textAlign: 'center', fontSize: 26, color: 'rgba(255,255,255,0.85)'}}>konkretny · mierzalny · osiągalny · istotny · określony w czasie</Pojaw>
    <div style={{position: 'absolute', left: 90, right: 90, top: 320, display: 'grid', gridTemplateColumns: 'repeat(5, 1fr)', gap: 22}}>
      {LITERY.map(([l, n, o, k], i) => (
        <Karta key={l} od={od[i]} style={{padding: '26px 20px', textAlign: 'center', minHeight: 330, borderColor: 'rgba(255,255,255,0.35)'}}>
          <div style={{width: 96, height: 96, borderRadius: '50%', background: k === '#2D1B69' ? '#6C4CC4' : k, margin: '0 auto', display: 'grid', placeItems: 'center', fontSize: 58, fontWeight: 800, boxShadow: '0 12px 30px rgba(0,0,0,0.3)'}}>{l}</div>
          <div style={{fontSize: 28, fontWeight: 800, marginTop: 18}}>{n}</div>
          <div style={{fontSize: 21, marginTop: 10, lineHeight: 1.35, color: 'rgba(255,255,255,0.85)'}}>{o}</div>
        </Karta>
      ))}
    </div>
    <Pojaw od={od[4] + 20} style={{position: 'absolute', left: 0, right: 0, bottom: 150, textAlign: 'center'}}>
      <span style={{display: 'inline-block', border: '2px solid #F6A57E', color: '#fff', borderRadius: 999, padding: '12px 30px', fontSize: 22, fontWeight: 700}}>skrypt szkolenia, część 6 · nazwa jest dowolna, mierzalność jest konieczna</span>
    </Pojaw>
  </Tlo>
);

const KLOCKI: [string, string][] = [['Dziecko, w konkretnej sytuacji', '#6C4CC4'], ['wykona obserwowalne zachowanie', '#6C4CC4'], ['w N z M prób', '#E8450A'], ['przy określonym wsparciu', '#C47A10'], ['do określonej daty', '#2F8F8A'], ['z określonym sposobem pomiaru', '#1f8a5b']];
const Formula: React.FC<{start: number; zle: number; dobrze: number; pytanie: number; odp: number}> = ({start, zle, dobrze, pytanie, odp}) => {
  const frame = useCurrentFrame();
  return (
    <Tlo>
      <Naglowek kicker="Formuła celu jest jedna" tytul="Sześć klocków, jedno zdanie" />
      <div style={{position: 'absolute', left: 100, right: 100, top: 250, display: 'flex', flexWrap: 'wrap', gap: 14, justifyContent: 'center'}}>
        {KLOCKI.map(([t, k], i) => {
          const w = Math.max(0, Math.min(1, (frame - start - i * 9) / 10));
          return <div key={t} style={{opacity: w, transform: `translateY(${(1 - w) * 16}px)`, background: k, color: '#fff', borderRadius: 999, padding: '12px 26px', fontSize: 25, fontWeight: 700, boxShadow: '0 10px 24px rgba(0,0,0,0.25)'}}>{t}</div>;
        })}
      </div>
      <div style={{position: 'absolute', left: 100, right: 100, top: 420, display: 'flex', gap: 30}}>
        <Karta od={zle} style={{flex: 1, borderColor: 'rgba(255,120,120,0.6)'}}>
          <div style={{fontSize: 18, letterSpacing: 3, color: '#ff9b9b', fontWeight: 800}}>✗ ZAPIS WYJŚCIOWY — INTENCJA</div>
          <div style={{fontSize: 34, fontWeight: 800, marginTop: 10, textDecoration: 'line-through', textDecorationColor: '#ff9b9b'}}>„rozwijanie samodzielności w czynnościach samoobsługowych”</div>
          <div style={{fontSize: 21, marginTop: 12, color: 'rgba(255,255,255,0.8)', lineHeight: 1.4}}>nie mówi, co ma się wydarzyć ani po czym poznamy, że się wydarzyło</div>
        </Karta>
        <Karta od={dobrze} akcent style={{flex: 1.35, boxShadow: '0 24px 60px rgba(232,69,10,0.45)'}}>
          <div style={{fontSize: 18, letterSpacing: 3, color: 'rgba(255,255,255,0.85)', fontWeight: 800}}>✓ CEL SMART — PRZYKŁAD ZE SKRYPTU</div>
          <div style={{fontSize: 27, fontWeight: 700, marginTop: 10, lineHeight: 1.45}}>
            <b style={{background: 'rgba(255,255,255,0.22)', borderRadius: 8, padding: '0 6px'}}>Zosia</b> podczas przygotowania do wyjścia na dwór <b style={{background: 'rgba(255,255,255,0.22)', borderRadius: 8, padding: '0 6px'}}>założy samodzielnie buty na rzepy</b> w <b style={{background: '#2D1B69', borderRadius: 8, padding: '0 8px'}}>4 z 5 kolejnych dni</b>, przy najwyżej jednej podpowiedzi słownej, do <b style={{background: '#2D1B69', borderRadius: 8, padding: '0 8px'}}>19 grudnia</b>. Pomiar: karta obserwacji szatni.
          </div>
        </Karta>
      </div>
      <div style={{position: 'absolute', left: 0, right: 0, bottom: 135, display: 'flex', justifyContent: 'center', gap: 24}}>
        <Karta od={pytanie} style={{padding: '14px 26px', fontSize: 26, fontWeight: 700}}>Czy przepis wymaga celów SMART?</Karta>
        <Karta od={odp} akcent style={{padding: '14px 26px', fontSize: 26, fontWeight: 800}}>Nie. Nazwa dowolna — mierzalność konieczna (ocena efektywności)</Karta>
      </div>
    </Tlo>
  );
};

const DECYZJE: [string, string, string][] = [['Cel osiągnięty', 'zamykamy i stawiamy kolejny', '#1f8a5b'], ['Osiągnięty częściowo', 'kontynuujemy i przesuwamy termin, nie obniżając kryterium', '#C47A10'], ['Brak postępu', 'modyfikujemy metodę i sprawdzamy bariery środowiskowe', '#E8450A'], ['Regres', 'spotkanie z rodzicami i rozważenie wystąpienia do poradni', '#c0392b']];
const Ewaluacja: React.FC<{sub: number; od: number[]}> = ({sub, od}) => (
  <Tlo>
    <Naglowek kicker="Ewaluacja nie wymaga nowych narzędzi" tytul="Wskaźnik jest już w celu" />
    <Pojaw od={sub} style={{position: 'absolute', left: 0, right: 0, top: 232, textAlign: 'center', fontSize: 26, color: 'rgba(255,255,255,0.85)'}}>po każdym pomiarze zespół podejmuje jedną z czterech decyzji</Pojaw>
    <div style={{position: 'absolute', left: 90, right: 90, top: 320, display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 22}}>
      {DECYZJE.map(([t, o, k], i) => (
        <Karta key={t} od={od[i]} style={{padding: '26px 22px', minHeight: 300, borderColor: k}}>
          <div style={{width: 60, height: 60, borderRadius: '50%', background: k, display: 'grid', placeItems: 'center', fontSize: 30, fontWeight: 800}}>{i + 1}</div>
          <div style={{fontSize: 30, fontWeight: 800, marginTop: 16, lineHeight: 1.2}}>{t}</div>
          <div style={{fontSize: 22, marginTop: 12, lineHeight: 1.4, color: 'rgba(255,255,255,0.88)'}}>{o}</div>
        </Karta>
      ))}
    </div>
    <Pojaw od={od[3] + 20} style={{position: 'absolute', left: 0, right: 0, bottom: 150, textAlign: 'center'}}>
      <span style={{display: 'inline-block', border: '2px solid #F6A57E', color: '#fff', borderRadius: 999, padding: '12px 30px', fontSize: 22, fontWeight: 700}}>trzy oceny w roku i dwa krótkie przeglądy wskaźników — w listopadzie i w marcu</span>
    </Pojaw>
  </Tlo>
);

const PRAWO: [string, string, string][] = [
  ['SMART w rozporządzeniu', 'nazwa nie pada ani razu — nie ma obowiązku używania skrótu w dokumencie', 'skrypt, część 6'],
  ['Ocena efektywności — kształcenie specjalne', '§ 6 rozp. MEN z 9.08.2017 r. (t.j. Dz.U. 2020 poz. 1309): wielospecjalistyczna ocena co najmniej 2× w roku, ocena efektywności programu', '✓ zgodne'],
  ['Ocena efektywności — pomoc pp', '§ 20 rozp. MEN z 9.08.2017 r. (t.j. Dz.U. 2023 poz. 1798): nauczyciele i specjaliści oceniają efektywność udzielanej pomocy', '✓ zgodne'],
  ['Twierdzenia KPOF', 'odsyłają do podstawy programowej — rozp. ME z 11.03.2026 r. (Dz.U. 2026 poz. 378) i kodów ICF (WHO 2001)', '✓ zgodne'],
];
const Straznik: React.FC<{od: number[]}> = ({od}) => {
  const frame = useCurrentFrame();
  const tarcza = useWejscie(0, {damping: 10, stiffness: 120});
  return (
    <Tlo>
      <div style={{position: 'absolute', left: 0, right: 0, top: 44, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 26}}>
        <div style={{width: 96, height: 96, borderRadius: '50%', background: MARKA.pomarancz, display: 'grid', placeItems: 'center', fontSize: 52, transform: `scale(${tarcza * (1 + 0.03 * Math.sin(frame / 8))})`, boxShadow: '0 16px 40px rgba(232,69,10,0.5)'}}>⚖</div>
        <Pojaw od={2}>
          <div style={{fontSize: 56, fontWeight: 800, color: '#fff', lineHeight: 1}}>Strażnik prawa · cele i ewaluacja</div>
          <div style={{fontSize: 20, color: 'rgba(255,255,255,0.75)', marginTop: 8, letterSpacing: 1.5}}>wg skryptu szkolenia, wyd. 2 po audycie podstaw prawnych z 5.09.2026</div>
        </Pojaw>
      </div>
      <div style={{position: 'absolute', left: 90, right: 90, top: 200, background: 'rgba(255,255,255,0.07)', border: '1.5px solid rgba(255,255,255,0.25)', borderRadius: 20, overflow: 'hidden'}}>
        {PRAWO.map(([a, b, c], i) => {
          const w = Math.max(0, Math.min(1, (frame - od[i]) / 10));
          return (
            <div key={a} style={{display: 'grid', gridTemplateColumns: '1fr 2.1fr 190px', padding: '18px 26px', borderTop: i ? '1px solid rgba(255,255,255,0.12)' : 'none', opacity: w, transform: `translateX(${(1 - w) * -20}px)`, color: '#fff', fontSize: 23, lineHeight: 1.35, alignItems: 'center', gap: 20}}>
              <div style={{fontWeight: 800}}>{a}</div>
              <div style={{color: 'rgba(255,255,255,0.9)'}}>{b}</div>
              <div style={{textAlign: 'center'}}><span style={{display: 'inline-block', background: c.startsWith('✓') ? '#2E9E52' : MARKA.pomarancz, color: '#fff', fontWeight: 800, fontSize: 16, padding: '6px 14px', borderRadius: 999}}>{c}</span></div>
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
      <Pojaw od={0}><div style={{fontSize: 56, fontWeight: 800, color: '#fff', textAlign: 'center', lineHeight: 1.2}}>Cel ma liczbę,<br />a ewaluacja ma konsekwencję.</div></Pojaw>
      <Pojaw od={logo} style={{marginTop: 50, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
        <Logo rozmiar={120} />
        <div style={{fontSize: 84, fontWeight: 800, color: '#fff', letterSpacing: -2, marginTop: 18, lineHeight: 1}}>EduPlaner <span style={{color: '#F6A57E'}}>2026</span></div>
      </Pojaw>
      <Pojaw od={haslo}>
        <div style={{fontSize: 38, color: '#fff', fontWeight: 700, marginTop: 22}}>Mniej dokumentów. Więcej edukacji.</div>
        <div style={{marginTop: 30, fontSize: 19, color: 'rgba(255,255,255,0.7)', letterSpacing: 2, textAlign: 'center'}}>TABELA CELÓW ToM · TABELA CELÓW KPOF · KREATOR CELU · STRAŻNIK PRAWA<br />PCTP KOSZALIN · kontakt@eduplaner2026.pl · 662 888 403</div>
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

export const CelePromo: React.FC<Props> = ({film}) => {
  const {fps} = useVideoConfig();
  const n = film.napisy;
  const z = (i: number) => n[i]?.odSek ?? i * 5;
  const kz = (i: number) => n[i]?.doSek ?? i * 5 + 4;
  const granica = (i: number) => (i <= 0 ? 0 : (kz(i - 1) + z(i)) / 2);
  const fr = (sek: number) => Math.round(sek * fps);
  const lok = (od: number) => (s: number) => Math.max(0, fr(s - od));
  const koniec = film.dlugosc;

  // --- tabela ToM (oryginalny plik autorki)
  const tomKroki: Krok[] = [
    {sek: z(17), doSek: kz(17) + 0.4, typ: 'wyroznij', selektor: '.legenda'},
    {sek: z(18) + 0.3, typ: 'zdarzenie', selektor: '#w-A tr[data-wsk="I.1"] td.g[data-lvl="p2"]'},
  ];
  const tomKamera: Ujecie[] = [
    {sek: 0, selektor: '.tyt', skala: 1.2, przesun: 60},
    {sek: z(15) + 1.5, selektor: '.zakladki', skala: 1.25, przesun: 80},
    {sek: z(16), selektor: '#w-A tr[data-wsk="I.1"]', skala: 1.28, przesun: 30},
    {sek: z(17), selektor: '.legenda', skala: 1.3, przesun: 10},
    {sek: z(18) + 0.6, selektor: '.kmodal.open .kcard', skala: 1.0, przesun: 330},
    {sek: z(18) + 4.0, selektor: '.kmodal.open .kcard', skala: 1.0, przesun: 560},
  ];
  // --- tabela KPOF-T (nowa) + kreator
  const K = (p: string) => `#kreator [data-p="${p}"]`;
  const kpofKroki: Krok[] = [
    {sek: z(21), typ: 'klasa', selektor: '#w-A tr[data-nr="30"] td.g[data-lvl="p3"]', klasa: 'on', doSek: kz(22) + 0.5},
    {sek: z(22), doSek: kz(22) + 0.5, typ: 'wyroznij', selektor: '#w-A tr[data-nr="30"] td.g[data-lvl="p3"]'},
    {sek: z(23) + 0.3, typ: 'zdarzenie', selektor: '[data-kreator]'},
    {sek: z(23) + 0.6, typ: 'zdarzenie', selektor: '#kreator .lvlsel button[data-l="p3"]'},
    {sek: z(24) + 0.2, typ: 'tekst', selektor: K('dziecko'), tekst: 'Zofia', tempo: 14},
    {sek: z(24) + 0.9, typ: 'tekst', selektor: K('syt'), tekst: 'po zapowiedzi sprzątania klocków (minutnik i symbol „koniec”)', tempo: 40},
    {sek: z(24) + 2.6, typ: 'tekst', selektor: K('zach'), tekst: 'zakończy zabawę bez krzyku i rzucania klockami', tempo: 40},
    {sek: z(24) + 4.0, typ: 'tekst', selektor: K('kryt'), tekst: '7 z 10 sytuacji', tempo: 30},
    {sek: z(24) + 4.7, typ: 'tekst', selektor: K('wsp'), tekst: 'przy jednym przypomnieniu dorosłego', tempo: 40},
    {sek: z(24) + 5.8, typ: 'tekst', selektor: K('data'), tekst: '29.01.2027', tempo: 20},
    {sek: z(24) + 6.5, typ: 'tekst', selektor: K('pomiar'), tekst: 'rejestr ABC w dzienniku grupy', tempo: 40},
    {sek: z(24) + 7.4, typ: 'tekst', selektor: K('zrodlo'), tekst: 'karta ABC·FBA (funkcja: uwaga + komunikat) · zalecenie z orzeczenia: pozytywne wsparcie zachowania', tempo: 60},
    {sek: z(25) + 0.2, doSek: kz(25) + 0.6, typ: 'wyroznij', selektor: '#kreator [data-zapisz]'},
  ];
  const kpofKamera: Ujecie[] = [
    {sek: 0, selektor: '.tyt', skala: 1.2, przesun: 60},
    {sek: z(19) + 3.5, selektor: '.sciezka', skala: 1.25, przesun: 40},
    {sek: z(20), selektor: '.sciezka .krok', skala: 1.45, przesun: 10},
    {sek: z(21), selektor: '#w-A tr[data-nr="30"]', skala: 1.3, przesun: 40},
    {sek: z(22), selektor: '#w-A tr[data-nr="30"] td.g[data-lvl="p3"]', skala: 1.55, przesun: 20},
    {sek: z(23) + 0.8, selektor: '.kmodal.open .kcard', skala: 1.0, przesun: 330},
    {sek: z(24) + 3.5, selektor: '#kreator .kgrid', skala: 1.1, przesun: 120},
    {sek: z(25), selektor: '#kreator .podglad', skala: 1.25, przesun: 60},
  ];

  type Scena = {id: string; od: number; do: number; el: (od: number) => React.ReactNode};
  const sceny: Scena[] = [
    {id: 'intro', od: 0, do: granica(2), el: (od) => <Intro sub={lok(od)(z(1))} />},
    {id: 'smart', od: granica(2), do: granica(9), el: (od) => <Smart sub={lok(od)(z(3))} od={[4, 5, 6, 7, 8].map((i) => lok(od)(z(i)))} />},
    {id: 'formula', od: granica(9), do: granica(14), el: (od) => <Formula start={lok(od)(z(9))} zle={lok(od)(z(10))} dobrze={lok(od)(z(11))} pytanie={lok(od)(z(12))} odp={lok(od)(z(13))} />},
    {id: 'tom', od: granica(14), do: granica(19), el: (od) => <OryginalnyDruk plik="tom-cele.html" kroki={tomKroki} kamera={tomKamera} odSek={od} szerokosc={1200} />},
    {id: 'kpof', od: granica(19), do: granica(26), el: (od) => <OryginalnyDruk plik="kpof-cele.html" kroki={kpofKroki} kamera={kpofKamera} odSek={od} szerokosc={1200} />},
    {id: 'ewaluacja', od: granica(26), do: granica(32), el: (od) => <Ewaluacja sub={lok(od)(z(27))} od={[28, 29, 30, 31].map((i) => lok(od)(z(i)))} />},
    {id: 'straznik', od: granica(32), do: granica(37), el: (od) => <Straznik od={[33, 34, 35, 36].map((i) => lok(od)(z(i)))} />},
    {id: 'final', od: granica(37), do: koniec, el: (od) => <Final logo={lok(od)(z(38))} haslo={lok(od)(z(39))} />},
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
