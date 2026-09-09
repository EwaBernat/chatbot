import React from 'react';
import {AbsoluteFill, Audio, Sequence, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from '../marka';
import {Napisy} from '../Napisy';
import {Logo, Pojaw, useWejscie} from '../ui';
import {OryginalnyDruk, type Krok, type Ujecie} from '../kpof/OryginalnyDruk';
import type {Napis} from '../typy';

/** Film „Szkoła podstawowa · KSzOF” — narracja to dosłowna transkrypcja części 5 skryptu (27 akapitów) + Strażnik prawa. */
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
    <div style={{fontSize: 54, fontWeight: 800, color: '#fff', marginTop: 10, letterSpacing: -1, lineHeight: 1.1}}>{tytul}</div>
  </Pojaw>
);
const Podswietl: React.FC<{od: number; children: React.ReactNode}> = ({od, children}) => {
  const frame = useCurrentFrame();
  const w = Math.max(0, Math.min(1, (frame - od) / 8));
  return <span style={{background: `rgba(232,69,10,${0.85 * w})`, borderRadius: 8, padding: '0 8px', transition: 'none'}}>{children}</span>;
};

const Intro: React.FC<{sub: number; cel: number}> = ({sub, cel}) => (
  <Tlo>
    <Pojaw od={0} style={{position: 'absolute', left: 0, right: 0, top: 130, textAlign: 'center'}}>
      <div style={{fontSize: 20, letterSpacing: 4, color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase'}}>EduPlaner 2026 · Szkoła podstawowa · moduł piąty</div>
      <div style={{fontSize: 96, fontWeight: 800, color: '#fff', marginTop: 12, letterSpacing: -2, lineHeight: 1.05}}>KSz<span style={{color: '#F6A57E'}}>OF</span></div>
      <div style={{fontSize: 38, fontWeight: 700, color: '#fff', marginTop: 10}}>Kwestionariusz Szkolnej Oceny Funkcjonalnej</div>
    </Pojaw>
    <div style={{position: 'absolute', left: 0, right: 0, top: 520, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 22}}>
      <Karta od={sub} akcent style={{width: 1180, textAlign: 'center', fontSize: 30, fontWeight: 700, lineHeight: 1.4}}>Najdłuższy moduł szkolenia — kwestionariusz jest sercem całej dokumentacji</Karta>
      <Karta od={cel} style={{width: 1180, textAlign: 'center', fontSize: 25, lineHeight: 1.45}}>Po tym module: budowa arkusza · zasady rzetelnej obserwacji · obliczanie wyniku · odczyt stenów · odczyt profilu ucznia</Karta>
    </div>
  </Tlo>
);

const IcfPlansza: React.FC<{kryt: number; kod: number; icf: number; model: number; dwoje: number}> = ({kryt, kod, icf, model, dwoje}) => (
  <Tlo>
    <Pojaw od={0} style={{position: 'absolute', left: 120, right: 120, top: 62, textAlign: 'center'}}>
      <div style={{fontSize: 19, letterSpacing: 4, color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase'}}>Narzędzie kryterialne · ten sam język, co dokumentacja poradni</div>
      <div style={{fontSize: 60, fontWeight: 800, color: '#fff', marginTop: 8, letterSpacing: -1, lineHeight: 1.05}}>ICF</div>
      <div style={{fontSize: 34, fontWeight: 700, color: '#fff', marginTop: 4, lineHeight: 1.2}}>Międzynarodowa Klasyfikacja Funkcjonowania, Niepełnosprawności i Zdrowia</div>
    </Pojaw>
    <div style={{position: 'absolute', left: 110, right: 110, top: 215}}>
      <div style={{display: 'flex', gap: 22}}>
        <Karta od={kryt} style={{flex: 1, fontSize: 25, lineHeight: 1.4}}>Kwestionariusz opisuje funkcjonowanie ucznia w <b style={{color: '#F6A57E'}}>dziewięciu obszarach</b> ICF — w codziennych sytuacjach szkolnych i domowych.</Karta>
        <Karta od={kod} style={{flex: 1, fontSize: 25, lineHeight: 1.4}}>Przy każdym twierdzeniu stoi <b style={{color: '#F6A57E'}}>kod klasyfikacji</b> (np. d110, d710) — nasz opis mówi tym samym językiem, co poradnia.</Karta>
      </div>
      <Karta od={icf} akcent style={{marginTop: 22, textAlign: 'center', fontSize: 27, fontWeight: 700, lineHeight: 1.4}}>
        WHO 2001 · ICF nie opisuje choroby ani rozpoznania — opisuje, jak człowiek funkcjonuje: co robi, w czym uczestniczy, co w otoczeniu pomaga albo przeszkadza.
      </Karta>
      <Pojaw od={model} style={{marginTop: 26}}>
        <div style={{fontSize: 19, letterSpacing: 3, color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase', textAlign: 'center', marginBottom: 14}}>Model biopsychospołeczny — funkcjonowanie to wypadkowa trzech rzeczy</div>
        <div style={{display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 18}}>
          {[['1', 'Stan zdrowia i funkcje ciała'], ['2', 'Aktywność i uczestniczenie'], ['3', 'Czynniki środowiskowe i osobowe']].map(([n, t], i) => (
            <Karta key={n} od={model + i * 5} style={{display: 'flex', alignItems: 'center', gap: 16, padding: '16px 20px'}}>
              <div style={{width: 54, height: 54, borderRadius: '50%', background: MARKA.morski, display: 'grid', placeItems: 'center', fontSize: 24, fontWeight: 800, flex: '0 0 auto'}}>{n}</div>
              <div style={{fontSize: 23, fontWeight: 700, lineHeight: 1.2}}>{t}</div>
            </Karta>
          ))}
        </div>
      </Pojaw>
      <Karta od={dwoje} style={{marginTop: 22, textAlign: 'center', fontSize: 23, lineHeight: 1.4, borderColor: '#F6A57E'}}>
        Dwoje uczniów z tym samym rozpoznaniem może funkcjonować zupełnie inaczej — inna klasa, inny nauczyciel, inny hałas, inne wsparcie w domu. Bez opisu barier nie da się zaplanować dostosowań.
      </Karta>
    </div>
  </Tlo>
);

const OBSZARY: [string, string, string][] = [
  ['I', 'Uczenie się i stosowanie wiedzy', 'd110 i dalsze'],
  ['II', 'Ogólne zadania i obowiązki', 'd210'],
  ['III', 'Porozumiewanie się', 'd310'],
  ['IV', 'Motoryka i poruszanie się', 'd440'],
  ['V', 'Dbanie o siebie i samoobsługa', 'd510'],
  ['VI', 'Życie domowe', 'd640'],
  ['VII', 'Wzajemne kontakty i związki', 'd710'],
  ['VIII', 'Edukacja szkolna', 'd820'],
  ['IX', 'Życie w społeczności lokalnej', 'd920'],
];
const Obszary: React.FC<{od: number[]}> = ({od}) => (
  <Tlo>
    <Naglowek kicker="Dziewięć rozdziałów aktywności i uczestniczenia z klasyfikacji ICF" tytul="Dziewięć obszarów kwestionariusza" />
    <div style={{position: 'absolute', left: 90, right: 90, top: 230, display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 20}}>
      {OBSZARY.map(([r, n, k], i) => (
        <Karta key={r} od={od[i]} style={{display: 'flex', alignItems: 'center', gap: 18, padding: '22px 22px', minHeight: 150}}>
          <div style={{width: 70, height: 70, borderRadius: 16, background: MARKA.pomarancz, display: 'grid', placeItems: 'center', fontSize: 26, fontWeight: 800, flex: '0 0 auto'}}>{r}</div>
          <div>
            <div style={{fontSize: 26, fontWeight: 800, lineHeight: 1.15}}>{n}</div>
            <div style={{fontSize: 19, color: '#F6A57E', fontWeight: 700, marginTop: 6, letterSpacing: 1}}>kod {k}</div>
          </div>
        </Karta>
      ))}
    </div>
  </Tlo>
);

const NieJest: React.FC<{nie: number; zapis: number; wersje: number; wiek: number; przyklad: number}> = ({nie, zapis, wersje, wiek, przyklad}) => (
  <Tlo>
    <Naglowek kicker="Czym kwestionariusz nie jest · trzy wersje arkusza" tytul="Zapis obserwacji, nie diagnoza" />
    <div style={{position: 'absolute', left: 110, right: 110, top: 220}}>
      <div style={{display: 'flex', gap: 22}}>
        <Karta od={nie} style={{flex: 1, fontSize: 26, lineHeight: 1.4}}>✗ Nie jest diagnozą.<br />✗ Nie zastępuje badania psychologicznego, logopedycznego ani lekarskiego.</Karta>
        <Karta od={zapis} akcent style={{flex: 1, fontSize: 26, lineHeight: 1.4, fontWeight: 700}}>✓ Uporządkowany zapis naszej obserwacji<br />✓ Punkt wyjścia do decyzji zespołu</Karta>
      </div>
      <Pojaw od={wersje} style={{marginTop: 30}}>
        <div style={{fontSize: 19, letterSpacing: 3, color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase', textAlign: 'center', marginBottom: 14}}>Trzy wersje arkusza — ten sam układ dziewięciu obszarów</div>
        <div style={{display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 18}}>
          {[['I–III', '52 twierdzenia · pierwszy etap'], ['IV–VI', 'twierdzenia dla wieku i wymagań II etapu'], ['VII–VIII', 'twierdzenia dla wieku i wymagań II etapu']].map(([n, t], i) => (
            <Karta key={n} od={wersje + i * 5} style={{textAlign: 'center', padding: '18px 20px'}}>
              <div style={{fontSize: 44, fontWeight: 800, color: '#F6A57E', lineHeight: 1}}>{n}</div>
              <div style={{fontSize: 20, marginTop: 8, lineHeight: 1.3}}>{t}</div>
            </Karta>
          ))}
        </div>
      </Pojaw>
      <Karta od={wiek} style={{marginTop: 22, textAlign: 'center', fontSize: 27, fontWeight: 700, lineHeight: 1.4, borderColor: '#F6A57E'}}>O wyborze wersji decyduje <span style={{color: '#F6A57E'}}>wiek rozwojowy</span> ucznia, a nie metrykalny.</Karta>
      <Karta od={przyklad} style={{marginTop: 18, textAlign: 'center', fontSize: 22, lineHeight: 1.4}}>Uczeń klasy VII z niepełnosprawnością intelektualną w stopniu umiarkowanym → wersja I–III, bo tylko ona da użyteczną informację.</Karta>
    </div>
  </Tlo>
);

const SKALA: [string, string, string][] = [['1', 'niewielki', '#c0392b'], ['2', 'mały', '#e0693a'], ['3', 'umiarkowany', '#d9a623'], ['4', 'duży', '#7cb342'], ['5', 'bardzo duży', '#2e7d46']];
const Skala: React.FC<{skala: number; piec: number; n: number; nieZgadujemy: number; ogr: number; piecN: number}> = ({skala, piec, n, nieZgadujemy, ogr, piecN}) => (
  <Tlo>
    <Naglowek kicker="Skala oceny · zaznaczamy zawsze jedną wartość" tytul="Pięć wartości i litera N" />
    <div style={{position: 'absolute', left: 110, right: 110, top: 220}}>
      <div style={{display: 'grid', gridTemplateColumns: 'repeat(5, 1fr)', gap: 18}}>
        {SKALA.map(([v, t, k], i) => (
          <Karta key={v} od={skala + i * 4} style={{textAlign: 'center', padding: '18px 12px'}}>
            <div style={{width: 84, height: 84, borderRadius: '50%', background: k, margin: '0 auto', display: 'grid', placeItems: 'center', fontSize: 40, fontWeight: 800}}>{v}</div>
            <div style={{fontSize: 22, fontWeight: 700, marginTop: 12}}>{t}</div>
          </Karta>
        ))}
      </div>
      <Karta od={piec} akcent style={{marginTop: 20, textAlign: 'center', fontSize: 25, fontWeight: 700}}>Pięć to mocna strona ucznia — i tak ją zapisujemy w ocenie.</Karta>
      <div style={{display: 'flex', gap: 22, marginTop: 22}}>
        <Karta od={n} style={{flex: 1.1, display: 'flex', gap: 20, alignItems: 'center'}}>
          <div style={{width: 84, height: 84, borderRadius: 18, border: '3px dashed #F6A57E', display: 'grid', placeItems: 'center', fontSize: 40, fontWeight: 800, color: '#F6A57E', flex: '0 0 auto'}}>N</div>
          <div style={{fontSize: 23, lineHeight: 1.35}}>Szósta możliwość: <b>brak możliwości obserwacji</b>. Pozycję zostawiamy pustą — to pełnoprawna, uczciwa odpowiedź. N nie obniża wyniku obszaru.</div>
        </Karta>
        <Karta od={nieZgadujemy} style={{flex: 0.9, fontSize: 23, lineHeight: 1.35}}>Rodzic nie widzi ucznia na lekcji, wychowawca nie widzi prac domowych. <b style={{color: '#F6A57E'}}>Nie zgadujemy.</b></Karta>
      </div>
      <Karta od={ogr} style={{marginTop: 22, fontSize: 23, lineHeight: 1.4, borderColor: '#F6A57E'}}>
        Ograniczenie: normy stenowe zbudowano dla arkusza wypełnionego w całości. <Podswietl od={piecN}><b>Więcej niż 5 pozycji N → wyniku ogólnego nie przeliczamy na steny</b></Podswietl> — odczytujemy sam profil obszarowy i zaznaczamy „arkusz niepełny”.
      </Karta>
    </div>
  </Tlo>
);

const ZASADY: string[] = [
  'Wypełniamy cały arkusz — wszystkie dziewięć obszarów, nie dzieląc ich między oceniających.',
  'Oceniamy na podstawie dwóch do czterech tygodni obserwacji, a nie jednego dnia.',
  'Wypełniamy samodzielnie, bez konsultowania ocen przed spotkaniem zespołu.',
  'Oceniamy to, co uczeń robi, a nie to, co potrafiłby zrobić.',
  'Odnosimy się do oczekiwań rozwojowych dla wieku ucznia.',
  'Zapisujemy obserwacje jakościowe — konkretne przykłady zachowań, zwłaszcza przy ocenach skrajnych.',
  'W drugim etapie zbieramy oceny od co najmniej trzech nauczycieli przedmiotów — nikt nie widzi ucznia przez cały dzień.',
  'Zwracamy arkusz koordynatorowi w umówionym terminie, żeby omówić wyniki wspólnie z rodzicami.',
];
const Zasady: React.FC<{od: number[]}> = ({od}) => (
  <Tlo>
    <Naglowek kicker="Zanim postawisz pierwszą ocenę" tytul="Osiem zasad rzetelnej obserwacji" />
    <div style={{position: 'absolute', left: 110, right: 110, top: 215, display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16}}>
      {ZASADY.map((z, i) => (
        <Karta key={i} od={od[i]} style={{display: 'flex', gap: 18, alignItems: 'center', padding: '16px 20px', minHeight: 120}}>
          <div style={{width: 50, height: 50, borderRadius: '50%', background: i === 7 ? MARKA.pomarancz : MARKA.morski, display: 'grid', placeItems: 'center', fontSize: 24, fontWeight: 800, flex: '0 0 auto'}}>{i + 1}</div>
          <div style={{fontSize: 23, lineHeight: 1.35}}>{z}</div>
        </Karta>
      ))}
    </div>
  </Tlo>
);

const NORMY: [string, string, string, string][] = [
  ['10', '238–260', '233–260', 'wysoki'], ['9', '218–237', '214–232', 'wysoki'], ['8', '197–217', '194–213', 'wysoki'],
  ['7', '175–196', '172–193', 'przeciętny'], ['6', '154–174', '151–171', 'przeciętny'], ['5', '135–153', '132–150', 'przeciętny'],
  ['4', '113–134', '110–131', 'niski'], ['3', '91–112', '90–109', 'niski'], ['2', '72–90', '70–89', 'niski'], ['1', '52–71', '52–69', 'niski'],
];
const Kroki: React.FC<{k1: number; maks: number; suma: number; k2: number; kolumny: number; sten4: number; k3: number; wzor: number}> = ({k1, maks, suma, k2, kolumny, sten4, k3, wzor}) => {
  const frame = useCurrentFrame();
  return (
    <Tlo>
      <Naglowek kicker="Obliczamy wynik w trzech krokach" tytul="Suma → sten z tabeli norm → profil obszarowy" />
      <div style={{position: 'absolute', left: 70, right: 70, top: 215, display: 'grid', gridTemplateColumns: '1fr 1.25fr 1fr', gap: 20}}>
        <Karta od={k1} style={{display: 'flex', flexDirection: 'column', gap: 14}}>
          <div style={{fontSize: 18, letterSpacing: 3, color: '#F6A57E', fontWeight: 800}}>KROK 1 · WYNIK OGÓLNY</div>
          <div style={{fontSize: 25, lineHeight: 1.35}}>Sumujemy wszystkie punkty.</div>
          <Pojaw od={maks}><div style={{fontSize: 22, lineHeight: 1.35, color: 'rgba(255,255,255,0.85)'}}>Maksimum <b style={{color: '#fff'}}>260</b> = 52 twierdzenia × 5 pkt</div></Pojaw>
          <Pojaw od={suma}><div style={{marginTop: 6, background: MARKA.pomarancz, borderRadius: 14, padding: '14px 18px', fontSize: 30, fontWeight: 800, textAlign: 'center'}}>Przykład: 114 pkt</div></Pojaw>
        </Karta>
        <Karta od={k2} style={{padding: '18px 20px'}}>
          <div style={{fontSize: 18, letterSpacing: 3, color: '#F6A57E', fontWeight: 800}}>KROK 2 · STEN Z TABELI NORM</div>
          <Pojaw od={kolumny}><div style={{fontSize: 19, lineHeight: 1.3, marginTop: 6, color: 'rgba(255,255,255,0.85)'}}>Dwie kolumny — osobne przedziały dla nauczyciela i rodzica. To nie pomyłka: nauczyciele i rodzice systematycznie różnią się w ocenach.</div></Pojaw>
          <div style={{marginTop: 12, borderRadius: 12, overflow: 'hidden', border: '1px solid rgba(255,255,255,0.25)'}}>
            <div style={{display: 'grid', gridTemplateColumns: '70px 1fr 1fr', background: 'rgba(0,0,0,0.3)', fontSize: 15, fontWeight: 800, letterSpacing: 1, padding: '8px 12px'}}><div>STEN</div><div>NAUCZYCIEL</div><div>RODZIC</div></div>
            {NORMY.map(([s, n, r, o], i) => {
              const wyr = s === '4' ? Math.max(0, Math.min(1, (frame - sten4) / 8)) : 0;
              const kol = o === 'wysoki' ? '#2e7d46' : o === 'przeciętny' ? '#d9a623' : '#c0392b';
              return (
                <div key={s} style={{display: 'grid', gridTemplateColumns: '70px 1fr 1fr', padding: '5px 12px', fontSize: 18, borderTop: '1px solid rgba(255,255,255,0.1)', background: `rgba(232,69,10,${0.85 * wyr})`, fontWeight: wyr ? 800 : 500}}>
                  <div style={{color: kol, fontWeight: 800}}>{s}</div><div>{n}</div><div>{r}</div>
                </div>
              );
            })}
          </div>
          <Pojaw od={sten4}><div style={{marginTop: 10, fontSize: 21, fontWeight: 800, textAlign: 'center'}}>114 pkt (nauczyciel) → sten 4 · wynik niski — sygnał trudności</div></Pojaw>
        </Karta>
        <Karta od={k3} style={{display: 'flex', flexDirection: 'column', gap: 14}}>
          <div style={{fontSize: 18, letterSpacing: 3, color: '#F6A57E', fontWeight: 800}}>KROK 3 · PROFIL OBSZAROWY</div>
          <div style={{fontSize: 22, lineHeight: 1.35}}>Obszary mają różną liczbę twierdzeń: I ma 15, IX tylko 2. Porównanie surowych sum nie ma sensu — potrzebna wspólna skala.</div>
          <Pojaw od={wzor}>
            <div style={{background: 'rgba(0,0,0,0.3)', borderRadius: 14, padding: '16px 18px', textAlign: 'center'}}>
              <div style={{fontSize: 16, letterSpacing: 2, color: '#F6A57E', fontWeight: 800}}>WZÓR · SKALA 0–20</div>
              <div style={{fontSize: 26, fontWeight: 800, marginTop: 8, lineHeight: 1.3}}>(suma obszaru ÷ maksimum obszaru) × 20</div>
              <div style={{fontSize: 18, color: 'rgba(255,255,255,0.8)', marginTop: 6}}>zaokrąglone do pełnego punktu</div>
            </div>
          </Pojaw>
        </Karta>
      </div>
    </Tlo>
  );
};

const PRZYKLAD: [string, string, string, string][] = [
  ['I. Uczenie się i stosowanie wiedzy', '23 / 75', '6', 'III'], ['II. Ogólne zadania i obowiązki', '10 / 30', '7', 'III'], ['III. Porozumiewanie się', '22 / 40', '11', 'II'],
  ['IV. Motoryka i poruszanie się', '12 / 20', '12', 'II'], ['V. Dbanie o siebie i samoobsługa', '10 / 20', '10', 'II'], ['VI. Życie domowe (arkusz rodzica)', '4 / 10', '8', 'III'],
  ['VII. Wzajemne kontakty i związki', '22 / 40', '11', 'II'], ['VIII. Edukacja szkolna', '5 / 15', '7', 'III'], ['IX. Życie w społeczności lokalnej', '6 / 10', '12', 'II'],
];
const PROGI: [string, string, string, string][] = [['18–20', 'zasób — mocna strona', '#2e7d46', 'Z'], ['14–17', 'Poziom I — wsparcie minimalne', '#7cb342', 'I'], ['9–13', 'Poziom II — wsparcie umiarkowane', '#d9a623', 'II'], ['0–8', 'Poziom III — wsparcie znaczne, WOPF i poradnia', '#c0392b', 'III']];
const Przyklad: React.FC<{ob1: number; dziel1: number; razy1: number; zapis1: number; ob3: number; wynik3: number; progi: number[]; tabela: number; pozIII: number; pozII: number; rekom: number; ipet: number}> = (p) => {
  const frame = useCurrentFrame();
  const kol = (poz: string) => (poz === 'III' ? '#c0392b' : '#d9a623');
  return (
    <Tlo>
      <Naglowek kicker="Policzmy razem · Zofia Lewandowska, klasa III A, arkusz wychowawcy" tytul="Skala 0–20, progi i poziomy wsparcia" />
      <div style={{position: 'absolute', left: 70, right: 70, top: 210, display: 'grid', gridTemplateColumns: '1fr 1.3fr', gap: 20}}>
        <div style={{display: 'flex', flexDirection: 'column', gap: 16}}>
          <Karta od={p.ob1} style={{padding: '16px 20px'}}>
            <div style={{fontSize: 17, letterSpacing: 2, color: '#F6A57E', fontWeight: 800}}>OBSZAR I · UCZENIE SIĘ</div>
            <div style={{fontSize: 30, fontWeight: 800, marginTop: 6}}>23 / 75 <Pojaw od={p.dziel1} style={{display: 'inline'}}>→ 0,30</Pojaw> <Pojaw od={p.razy1} style={{display: 'inline'}}>× 20 = 6</Pojaw></div>
            <Pojaw od={p.zapis1}><div style={{fontSize: 21, marginTop: 4, color: 'rgba(255,255,255,0.85)'}}>zapisujemy: <b style={{color: '#fff'}}>6 na 20</b></div></Pojaw>
          </Karta>
          <Karta od={p.ob3} style={{padding: '16px 20px'}}>
            <div style={{fontSize: 17, letterSpacing: 2, color: '#F6A57E', fontWeight: 800}}>OBSZAR III · POROZUMIEWANIE SIĘ</div>
            <div style={{fontSize: 30, fontWeight: 800, marginTop: 6}}>22 / 40 <Pojaw od={p.wynik3} style={{display: 'inline'}}>→ 0,55 × 20 = 11</Pojaw></div>
          </Karta>
          <Pojaw od={p.progi[0] - 8}>
            <div style={{fontSize: 17, letterSpacing: 3, color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase', marginBottom: 8}}>Progi poziomów wsparcia (skala 0–20)</div>
          </Pojaw>
          {PROGI.map(([z, t, k, s], i) => (
            <Karta key={z} od={p.progi[i]} style={{display: 'flex', alignItems: 'center', gap: 16, padding: '10px 16px'}}>
              <div style={{minWidth: 96, textAlign: 'center', background: k, borderRadius: 10, padding: '6px 10px', fontSize: 24, fontWeight: 800}}>{z}</div>
              <div style={{fontSize: 21, lineHeight: 1.25}}>{t}</div>
              <div style={{marginLeft: 'auto', fontSize: 18, fontWeight: 800, color: k === '#d9a623' || k === '#7cb342' ? '#fff' : '#fff', opacity: 0.8}}>{s}</div>
            </Karta>
          ))}
        </div>
        <Karta od={p.tabela} style={{padding: '14px 18px'}}>
          <div style={{display: 'grid', gridTemplateColumns: '1fr 110px 90px 90px', fontSize: 15, fontWeight: 800, letterSpacing: 1, padding: '6px 10px', background: 'rgba(0,0,0,0.3)', borderRadius: 10}}><div>OBSZAR</div><div>SUMA / MAKS.</div><div>0–20</div><div>POZIOM</div></div>
          {PRZYKLAD.map(([o, s, w, poz], i) => {
            const wyr = poz === 'III' ? Math.max(0, Math.min(1, (frame - p.pozIII) / 8)) : Math.max(0, Math.min(1, (frame - p.pozII) / 8));
            return (
              <div key={o} style={{display: 'grid', gridTemplateColumns: '1fr 110px 90px 90px', padding: '7px 10px', fontSize: 19, borderBottom: '1px solid rgba(255,255,255,0.12)', alignItems: 'center'}}>
                <div>{o}</div><div style={{fontWeight: 700}}>{s}</div><div style={{fontWeight: 800}}>{w}</div>
                <div><span style={{display: 'inline-block', background: kol(poz), borderRadius: 999, padding: '3px 12px', fontWeight: 800, fontSize: 16, opacity: 0.25 + 0.75 * wyr}}>{poz}</span></div>
              </div>
            );
          })}
          <div style={{display: 'grid', gridTemplateColumns: '1fr 110px 90px 90px', padding: '9px 10px', fontSize: 20, fontWeight: 800, background: 'rgba(255,255,255,0.08)', borderRadius: 10, marginTop: 6}}><div>WYNIK OGÓLNY</div><div>114 / 260</div><div>—</div><div>sten 4</div></div>
          <Pojaw od={p.rekom}><div style={{marginTop: 12, background: MARKA.pomarancz, borderRadius: 12, padding: '12px 16px', fontSize: 21, fontWeight: 800, lineHeight: 1.3}}>Rekomendowany ogólny poziom wsparcia: II — ale w 4 obszarach wsparcie znaczne (III)</div></Pojaw>
          <Pojaw od={p.ipet}><div style={{marginTop: 10, fontSize: 19, textAlign: 'center', color: 'rgba(255,255,255,0.85)'}}>Ten zapis wędruje wprost do programu → IPET/2026-2027/III A/07</div></Pojaw>
        </Karta>
      </div>
    </Tlo>
  );
};

const PRAWO: [string, string, string][] = [
  ['Prawo oświatowe, art. 127', 'w druku było t.j. Dz.U. 2024 poz. 737 — obowiązuje t.j. Dz.U. 2026 poz. 820 (2 miejsca)', 'POPRAWIONO'],
  ['Rozp. MEN z 9.08.2017 r. — pomoc pp i kształcenie specjalne', 'pierwotne publikatory Dz.U. 2017 poz. 1591 i 1578 → t.j. Dz.U. 2023 poz. 1798 i t.j. Dz.U. 2020 poz. 1309 (32 miejsca, także w zaleceniach)', 'POPRAWIONO'],
  ['Orzeczenia i opinie poradni', 'rozp. ME z 2.03.2026 r., Dz.U. 2026 poz. 428 — informacja szkoły o funkcjonowaniu ucznia w 10 dni; od 1.09.2026', '✓ zgodne'],
  ['Dokumentacja przebiegu nauczania', 'arkusz obserwacji = dokumentacja badań i czynności uzupełniających — rozp. MEN z 25.08.2017 r., t.j. Dz.U. 2024 poz. 50', 'PODSTAWA'],
  ['Progi poziomów wsparcia i skala 0–20', 'decyzja rady pedagogicznej wpisana do procedury szkoły — nie wynikają wprost z przepisu', 'PROCEDURA'],
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
        <div style={{marginTop: 30, fontSize: 19, color: 'rgba(255,255,255,0.7)', letterSpacing: 2, textAlign: 'center'}}>SZKOŁA PODSTAWOWA · KSzOF · SKRYPT CZĘŚĆ 5 · STRAŻNIK PRAWA<br />PCTP KOSZALIN · kontakt@eduplaner2026.pl · 662 888 403</div>
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

/** Oceny w filmie odtwarzają przykład ze skryptu (twierdzenie „słucha” = 2, „pisze” = 1, obszar VI = N, profil: I, II, VI, VIII w poziomie III). [arkusz, obszar, wartości]. */
const OCENY: [number, string, number[]][] = [
  [2, 'I', [2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 2, 1, 2]],
  [2, 'II', [2, 2, 2, 1, 2, 1]],
  [3, 'III', [3, 3, 3, 2, 3, 3, 2, 3]],
  [3, 'IV', [3, 3]],
  [3, 'V', [3, 2, 3, 2]],
  [3, 'VII', [2, 2, 2]],
  [4, 'VII', [3, 2, 2, 2, 3, 3, 2]],
  [4, 'VIII', [1, 1, 2, 1]],
  [4, 'IX', [3, 3]],
];
const rc = (arkusz: number, obszar: string, k: number, v: number) => `@${arkusz} tr.arow[data-area="${obszar}"] .rc[data-v="${v}"] #${k}`;
const ocena = (arkusz: number, obszar: string, k: number, v: number, sek: number): Krok => ({sek, typ: 'klasa', selektor: rc(arkusz, obszar, k, v), klasa: 'on'});
const daty = (): Krok[] => Array.from({length: 28}, (_, i): Krok => ({sek: 0, typ: 'tekst', selektor: `@${i + 1} .student .blank #0`, tekst: '22.09.2026', tempo: 999}));

export const KszofPromo: React.FC<Props> = ({film}) => {
  const {fps} = useVideoConfig();
  const n = film.napisy;
  const z = (i: number) => n[i]?.odSek ?? i * 5;
  const kz = (i: number) => n[i]?.doSek ?? i * 5 + 4;
  const granica = (i: number) => (i <= 0 ? 0 : (kz(i - 1) + z(i)) / 2);
  const fr = (sek: number) => Math.round(sek * fps);
  const lok = (od: number) => (s: number) => Math.max(0, fr(s - od));
  const koniec = film.dlugosc;

  // --- druk 1 (zdania 56–66): metryczka, obszar I opowiadany, obszar VI = N, reszta szybko przy „obliczamy wynik”
  const kroki1: Krok[] = [
    ...daty(),
    {sek: z(56) + 0.3, typ: 'tekst', selektor: '@1 .mvl #0', tekst: '01–22.09.2026 (3 tygodnie obserwacji)', tempo: 45},
    {sek: z(56) + 1.6, typ: 'tekst', selektor: '@1 .mvl #1', tekst: 'mgr Katarzyna Wiśniewska — wychowawczyni III A (N)', tempo: 45},
    {sek: z(58) + 0.2, doSek: kz(60) + 0.3, typ: 'wyroznij', selektor: '@2 tr.arow #2'},
    ocena(2, 'I', 2, 2, z(60) + 0.9),
    {sek: z(61) + 0.2, doSek: kz(63) + 0.3, typ: 'wyroznij', selektor: '@2 tr.arow #10'},
    ocena(2, 'I', 10, 1, z(63) + 0.6),
    {sek: z(64) + 0.3, doSek: kz(66) + 0.3, typ: 'wyroznij', selektor: '@3 tr.arow[data-area="VI"] #0'},
    {sek: z(65) + 0.3, doSek: kz(66) + 0.3, typ: 'wyroznij', selektor: '@3 tr.arow[data-area="VI"] #1'},
  ];
  // pozostałe twierdzenia obszaru I (poza 3 i 11) — po narracji o twierdzeniu 12, oraz obszary II–IX w tempie 0,15 s
  let t = z(63) + 1.6;
  OCENY[0][2].forEach((v, k) => {
    if (k === 2 || k === 10) return;
    kroki1.push(ocena(2, 'I', k, v, t));
    t += 0.12;
  });
  t = Math.max(t, z(66) + 0.3);
  for (const [arkusz, obszar, wartosci] of OCENY.slice(1)) {
    wartosci.forEach((v, k) => {
      kroki1.push(ocena(arkusz, obszar, k, v, t));
      t += 0.15;
    });
  }
  const kamera1: Ujecie[] = [
    {sek: 0, selektor: '@1 .eyebrow', skala: 1.7, przesun: 170},
    {sek: z(56) + 0.2, selektor: '@1 .sec', skala: 2.0, przesun: 120},
    {sek: z(57), selektor: '@2 tr.arow #0', skala: 2.0, przesun: 150},
    {sek: z(58), selektor: '@2 tr.arow #2', skala: 2.05, przesun: 70},
    {sek: z(61), selektor: '@2 tr.arow #10', skala: 2.05, przesun: 60},
    {sek: z(64) + 0.9, selektor: '@3 .arsum[data-c="VI"]', skala: 2.1, przesun: 70},
    {sek: z(66) + 0.6, selektor: '@2 tr.arow #14', skala: 1.8, przesun: 200},
    {sek: z(66) + 3.0, selektor: '@3 tr.arow #4', skala: 1.8, przesun: 250},
  ];

  // --- druk 2 (zdania 99–123): wszystkie oceny od razu; reguła nadrzędna, profil, 270°, ewaluacja
  const kroki2: Krok[] = [...daty(), {sek: 0, typ: 'tekst', selektor: '@1 .mvl #0', tekst: '01–22.09.2026 (3 tygodnie obserwacji)', tempo: 999}, {sek: 0, typ: 'tekst', selektor: '@1 .mvl #1', tekst: 'mgr Katarzyna Wiśniewska — wychowawczyni III A (N)', tempo: 999}];
  for (const [arkusz, obszar, wartosci] of OCENY) wartosci.forEach((v, k) => kroki2.push(ocena(arkusz, obszar, k, v, 0)));
  kroki2.push({sek: z(100) + 0.3, doSek: kz(103) + 0.3, typ: 'wyroznij', selektor: '@2 tr.arow[data-area="I"] .rc[data-v="1"] #10'});
  kroki2.push({sek: z(109) + 0.3, doSek: kz(109) + 0.3, typ: 'wyroznij', selektor: '@4 tr.arow[data-area="VIII"] .rc[data-v="1"] #0'});
  const kamera2: Ujecie[] = [
    {sek: 0, selektor: '@2 tr.arow #10', skala: 2.1, przesun: 40},
    {sek: z(104), selektor: '@7 svg #0', skala: 1.9, przesun: 150},
    {sek: z(106), selektor: '@7 svg #1', skala: 1.9, przesun: 140},
    {sek: z(109), selektor: '@4 tr.arow #7', skala: 2.0, przesun: 60},
    {sek: z(110), selektor: '@9 table.tbl', skala: 1.9, przesun: 150},
    {sek: z(113), selektor: '@10 .sbody', skala: 1.75, przesun: 290},
    {sek: z(117), selektor: '@21 .sec #0', skala: 1.9, przesun: 210},
    {sek: z(121), selektor: '@21 .sec #1', skala: 1.9, przesun: 160},
  ];
  const cssFilmu = [
    '.addrow,.delrow,.delcell,.printcell{display:none!important}',
    '.druk-oryginalny .sheet{box-shadow:0 10px 40px rgba(45,27,105,0.18)}',
    '.druk-oryginalny .mbox,.druk-oryginalny .box,.druk-oryginalny .ktobox{border-width:1.3px}',
    '.druk-oryginalny .blank,.druk-oryginalny .mvl,.druk-oryginalny .dline{overflow-wrap:break-word;white-space:normal;height:auto;min-height:15px}',
    '.druk-oryginalny .mvl,.druk-oryginalny .blank{display:block;max-width:100%;box-sizing:border-box}',
  ].join('\n');

  type Scena = {id: string; od: number; do: number; el: (od: number) => React.ReactNode};
  const L = (od: number) => lok(od);
  const sceny: Scena[] = [
    {id: 'intro', od: 0, do: granica(3), el: (od) => <Intro sub={L(od)(z(1))} cel={L(od)(z(2))} />},
    {id: 'icf', od: granica(3), do: granica(15), el: (od) => <IcfPlansza kryt={L(od)(z(4))} kod={L(od)(z(5))} icf={L(od)(z(8))} model={L(od)(z(12))} dwoje={L(od)(z(13))} />},
    {id: 'obszary', od: granica(15), do: granica(25), el: (od) => <Obszary od={[16, 17, 18, 19, 20, 21, 22, 23, 24].map((i) => L(od)(z(i)))} />},
    {id: 'niejest', od: granica(25), do: granica(33), el: (od) => <NieJest nie={L(od)(z(26))} zapis={L(od)(z(27))} wersje={L(od)(z(28))} wiek={L(od)(z(31))} przyklad={L(od)(z(32))} />},
    {id: 'skala', od: granica(33), do: granica(47), el: (od) => <Skala skala={L(od)(z(34))} piec={L(od)(z(35))} n={L(od)(z(36))} nieZgadujemy={L(od)(z(39))} ogr={L(od)(z(42))} piecN={L(od)(z(44))} />},
    {id: 'zasady', od: granica(47), do: granica(56), el: (od) => <Zasady od={[48, 49, 50, 51, 52, 53, 54, 55].map((i) => L(od)(z(i)))} />},
    {id: 'druk1', od: granica(56), do: granica(67), el: (od) => <OryginalnyDruk plik="kszof.html" kroki={kroki1} kamera={kamera1} odSek={od} css={cssFilmu} />},
    {id: 'kroki', od: granica(67), do: granica(83), el: (od) => <Kroki k1={L(od)(z(69))} maks={L(od)(z(71))} suma={L(od)(z(72))} k2={L(od)(z(73))} kolumny={L(od)(z(74))} sten4={L(od)(z(77))} k3={L(od)(z(78))} wzor={L(od)(z(82))} />},
    {id: 'przyklad', od: granica(83), do: granica(99), el: (od) => <Przyklad ob1={L(od)(z(84))} dziel1={L(od)(z(85))} razy1={L(od)(z(86))} zapis1={L(od)(z(87))} ob3={L(od)(z(88))} wynik3={L(od)(z(89))} progi={[91, 92, 93, 94].map((i) => L(od)(z(i)))} tabela={L(od)(z(95) - 0.6)} pozIII={L(od)(z(95) + 0.6)} pozII={L(od)(z(96))} rekom={L(od)(z(97))} ipet={L(od)(z(98))} />},
    {id: 'druk2', od: granica(99), do: granica(124), el: (od) => <OryginalnyDruk plik="kszof.html" kroki={kroki2} kamera={kamera2} wykresyOdSek={z(105) + 0.2} odSek={od} css={cssFilmu} />},
    {id: 'straznik', od: granica(124), do: granica(128), el: (od) => <Straznik od={[124, 125, 126, 126, 127].map((i, j) => L(od)(z(i) + (j === 3 ? 4.5 : 0)))} />},
    {id: 'final', od: granica(128), do: koniec, el: (od) => <Final logo={L(od)(z(129))} haslo={L(od)(z(130))} />},
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
