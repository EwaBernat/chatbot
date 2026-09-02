import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate, spring } from 'remotion';
import { MARKA, OBSZARY_KOLOR, FONT_NAGLOWEK, FONT_TEKST, FONT_DANE } from '../marka';
import { IkonaObszaru } from '../elementy/Ikony';
import { ZnakPCTP } from '../elementy/Logo';
import { AwatarStop } from '../elementy/Awatar';
import { Eyebrow, Naglowek, Punkty, Panel, useWejscie } from './wspolne';
import type { Scena } from '../typy';

/* ── 1. INTRO ─────────────────────────────────────────────────────────── */
export const Intro: React.FC = () => {
  const w = useWejscie(0);
  return (
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center',
                           paddingLeft: 110, paddingRight: 470 }}>
      <div style={{ ...w, textAlign: 'center' }}>
        <div style={{ display: 'flex', justifyContent: 'center', marginBottom: 30 }}>
          <ZnakPCTP rozmiar={132} />
        </div>
        <p style={{ margin: 0, fontFamily: FONT_NAGLOWEK, fontWeight: 700, fontSize: 30,
                    letterSpacing: '.24em', textTransform: 'uppercase',
                    color: MARKA.pomaranczJasny }}>
          EduPlaner 2026 · PCTP Koszalin
        </p>
        <h1 style={{ margin: '22px 0 0', fontFamily: FONT_NAGLOWEK, fontWeight: 900,
                     fontSize: 104, lineHeight: 1.02, color: '#fff', letterSpacing: '-.02em' }}>
          Nowa podstawa programowa
        </h1>
        <p style={{ margin: '20px 0 0', fontFamily: FONT_NAGLOWEK, fontWeight: 900,
                    fontSize: 74, color: MARKA.pomaranczJasny, letterSpacing: '-.01em' }}>
          wychowania przedszkolnego
        </p>
        <p style={{ margin: '38px 0 0', fontFamily: FONT_TEKST, fontSize: 40,
                    color: MARKA.naCiemnymDrugi }}>
          Szkolenie dla nauczycieli · obowiązuje od 1 września 2026 r.
        </p>
        <p style={{ margin: '14px 0 0', fontFamily: FONT_TEKST, fontSize: 30,
                    color: MARKA.naCiemnymDrugi }}>
          prowadzi pedagog specjalny mgr Mirosława Ewa Jurczyszyn
        </p>
      </div>
    </AbsoluteFill>
  );
};

/* ── 2. FAKT — jedna wielka data ──────────────────────────────────────── */
export const Fakt: React.FC<{ scena: Scena }> = ({ scena }) => {
  const klatka = useCurrentFrame();
  const { fps } = useVideoConfig();
  const puls = 1 + Math.sin(klatka / 26) * 0.012;
  const w = useWejscie(4);
  return (
    <Panel>
      <Eyebrow>Kiedy</Eyebrow>
      <div style={{ ...w, transform: `${w.transform} scale(${puls})`, transformOrigin: 'left center' }}>
        <p style={{ margin: '10px 0 0', fontFamily: FONT_NAGLOWEK, fontWeight: 900,
                    fontSize: 190, lineHeight: 1, color: '#fff', letterSpacing: '-.02em' }}>
          {scena.znak}
        </p>
      </div>
      <p style={{ ...useWejscie(18), margin: '6px 0 0', fontFamily: FONT_TEKST,
                  fontSize: 44, color: MARKA.pomaranczJasny }}>
        {scena.podpis}
      </p>
      <Punkty odKlatki={28} pozycje={[
        'Przedszkola publiczne i niepubliczne',
        'Oddziały przedszkolne w szkołach podstawowych',
        'Inne formy wychowania przedszkolnego',
      ]} />
    </Panel>
  );
};

/* ── 3. PODSTAWA PRAWNA — akty wjeżdżające po kolei ───────────────────── */
const AKTY = [
  { akt: 'Rozporządzenie Ministra Edukacji z 11 marca 2026 r.',
    sygn: 'Dz.U. 2026 poz. 378', rola: 'podstawa programowa — od 1 IX 2026', glowny: true },
  { akt: 'Rozporządzenie MEN z 9 sierpnia 2017 r. — pomoc psychologiczno-pedagogiczna',
    sygn: 't.j. Dz.U. 2023 poz. 1798', rola: 'obserwacja i ocena efektywności pomocy' },
  { akt: 'Rozporządzenie MEN z 9 sierpnia 2017 r. — kształcenie specjalne',
    sygn: 't.j. Dz.U. 2020 poz. 1309', rola: 'IPET i wielospecjalistyczna ocena' },
  { akt: 'Ustawa z 14 grudnia 2016 r. — Prawo oświatowe',
    sygn: 't.j. Dz.U. 2025 poz. 1043', rola: 'rama całego systemu' },
];

export const Prawo: React.FC = () => (
  <Panel>
    <Eyebrow>Podstawa prawna</Eyebrow>
    <Naglowek maly>Na co powołasz się w dokumentacji</Naglowek>
    <div style={{ marginTop: 32, display: 'flex', flexDirection: 'column', gap: 13 }}>
      {AKTY.map((a, i) => (
        <div key={i} style={{
          ...useWejscie(16 + i * 11),
          background: a.glowny ? 'rgba(232,69,10,.16)' : 'rgba(255,255,255,.07)',
          borderLeft: `6px solid ${a.glowny ? MARKA.pomarancz : MARKA.pomaranczJasny}`,
          borderRadius: '0 14px 14px 0', padding: '15px 24px',
        }}>
          <p style={{ margin: 0, fontFamily: FONT_TEKST, fontSize: 27, lineHeight: 1.28,
                      color: '#fff', fontWeight: a.glowny ? 700 : 400 }}>{a.akt}</p>
          <p style={{ margin: '6px 0 0', fontFamily: FONT_DANE, fontSize: 23,
                      color: MARKA.pomaranczJasny }}>{a.sygn}</p>
          <p style={{ margin: '3px 0 0', fontFamily: FONT_TEKST, fontSize: 21,
                      color: MARKA.naCiemnymDrugi }}>{a.rola}</p>
        </div>
      ))}
    </div>
  </Panel>
);

/* ── 4. KONSTRUKCJA — pięć pojęć nośnych ──────────────────────────────── */
const POJECIA = [
  ['Kompetencje fundamentalne', 'językowe · matematyczne · cyfrowe · ruchowe'],
  ['Kompetencje przekrojowe', 'przechodzą przez wszystkie obszary naraz'],
  ['Doświadczenia edukacyjne', 'dziecko uczy się przez działanie i zmysły'],
  ['Sprawczość dziecka', 'prawo do wyboru, decyzji i błędu'],
  ['Dobrostan', 'warunek, nie dodatek'],
];

export const Konstrukcja: React.FC = () => (
  <Panel>
    <Eyebrow>Jak zbudowany jest dokument</Eyebrow>
    <Naglowek maly>Pięć pojęć, które wracają w całej podstawie</Naglowek>
    <div style={{ marginTop: 40, display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 18 }}>
      {POJECIA.map(([tytul, opis], i) => (
        <div key={i} style={{
          ...useWejscie(14 + i * 10),
          background: 'rgba(255,255,255,.08)', borderRadius: 16, padding: '22px 26px',
          borderTop: `4px solid ${MARKA.pomaranczJasny}`,
          gridColumn: i === 4 ? 'span 2' : undefined,
        }}>
          <p style={{ margin: 0, fontFamily: FONT_NAGLOWEK, fontWeight: 800, fontSize: 40,
                      color: '#fff' }}>{tytul}</p>
          <p style={{ margin: '8px 0 0', fontFamily: FONT_TEKST, fontSize: 27,
                      color: MARKA.naCiemnymDrugi }}>{opis}</p>
        </div>
      ))}
    </div>
  </Panel>
);

/* ── 5. PRZEJŚCIE 4 → 9 ───────────────────────────────────────────────── */
const STARE = ['fizyczny', 'emocjonalny', 'społeczny', 'poznawczy'];
const NOWE = ['społeczny', 'osobisty', 'językowy', 'matematyczny', 'przyrodniczy',
              'techniczny', 'cyfrowy', 'artystyczny', 'ruchowy'];

export const Przejscie: React.FC = () => {
  const klatka = useCurrentFrame();
  const { fps } = useVideoConfig();
  const przejscie = spring({ frame: klatka - fps * 2.2, fps, config: { damping: 200 } });
  return (
    <Panel>
      <Eyebrow>Największa zmiana</Eyebrow>
      <Naglowek maly>Z czterech obszarów na dziewięć</Naglowek>
      <div style={{ marginTop: 46, display: 'flex', alignItems: 'center', gap: 46 }}>
        <div style={{ opacity: interpolate(przejscie, [0, 1], [1, 0.28]) }}>
          <p style={{ margin: '0 0 14px', fontFamily: FONT_NAGLOWEK, fontWeight: 800,
                      fontSize: 24, letterSpacing: '.16em', textTransform: 'uppercase',
                      color: MARKA.naCiemnymDrugi }}>Do 2026</p>
          {STARE.map((n, i) => (
            <div key={n} style={{
              ...useWejscie(6 + i * 6),
              background: 'rgba(255,255,255,.10)', borderRadius: 12,
              padding: '13px 22px', marginBottom: 10, width: 330,
              fontFamily: FONT_TEKST, fontSize: 30, color: '#fff',
            }}>{n}</div>
          ))}
        </div>

        <div style={{
          fontFamily: FONT_NAGLOWEK, fontWeight: 900, fontSize: 90,
          color: MARKA.pomarancz,
          transform: `translateX(${interpolate(przejscie, [0, 1], [-30, 0])}px)`,
          opacity: przejscie,
        }}>→</div>

        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 10,
                      opacity: przejscie }}>
          <p style={{ gridColumn: 'span 2', margin: '0 0 4px', fontFamily: FONT_NAGLOWEK,
                      fontWeight: 800, fontSize: 24, letterSpacing: '.16em',
                      textTransform: 'uppercase', color: MARKA.pomaranczJasny }}>
            Od 1 IX 2026
          </p>
          {NOWE.map((n, i) => {
            const s = spring({ frame: klatka - fps * 2.4 - i * 3, fps, config: { damping: 200 } });
            return (
              <div key={n} style={{
                background: OBSZARY_KOLOR[NOWE[i]] ?? MARKA.fioletJasny,
                borderRadius: 11, padding: '11px 18px', width: 268,
                fontFamily: FONT_TEKST, fontSize: 26, color: '#fff',
                opacity: s, transform: `scale(${interpolate(s, [0, 1], [0.9, 1])})`,
              }}>{n}</div>
            );
          })}
        </div>
      </div>
    </Panel>
  );
};

/* ── 6–14. OBSZAR ─────────────────────────────────────────────────────── */
const OPISY: Record<string, string[]> = {
  spoleczny: ['Relacje z rówieśnikami i współpraca w grupie', 'Tutoring rówieśniczy — starsze dziecko uczy młodsze', 'Poczucie przynależności do grupy i wspólnoty'],
  osobisty: ['Tożsamość, autonomia, poczucie własnej wartości', 'Rozpoznawanie i nazywanie emocji', 'Radzenie sobie z porażką · granice własne i cudze'],
  jezykowy: ['Rozwój mowy i komunikacja słowna oraz bezsłowna', 'Przygotowanie do nauki czytania i pisania', 'Zainteresowanie literami i książkami'],
  matematyczny: ['Orientacja w przestrzeni, rytmy, intuicja geometryczna', 'Logiczne myślenie w codziennych sytuacjach', 'Zdolności matematyczne u każdego dziecka'],
  przyrodniczy: ['Bezpośrednia obserwacja — regularne wychodzenie', 'Niezależnie od pogody, przez cały rok', 'Edukacja klimatyczna i ekologiczna z doświadczenia'],
  techniczny: ['Majsterkowanie i konstruowanie', 'Bezpieczne posługiwanie się prostymi narzędziami', 'Samodzielny dostęp dziecka do materiałów'],
  cyfrowy: ['Kompetencje cyfrowe przede wszystkim bez ekranu', 'Rozumienie, czym jest technologia i do czego służy', 'Higiena cyfrowa i ograniczanie czasu ekranowego'],
  artystyczny: ['Proces twórczy ważniejszy niż gotowy produkt', 'Ekspresja plastyczna, muzyczna, teatralna, ruchowa', 'Eksperymentowanie z formą, kolorem i dźwiękiem'],
  ruchowy: ['Sprawność motoryczna i koordynacja', 'Prawidłowa postawa i bezpieczeństwo', 'Profilaktyka zdrowotna jako osobny cel'],
};

export const Obszar: React.FC<{ scena: Scena }> = ({ scena }) => {
  const klucz = scena.klucz ?? 'spoleczny';
  const kolor = OBSZARY_KOLOR[klucz] ?? MARKA.fioletJasny;
  const naglowekWejscie = useWejscie(4);
  return (
    <>
      <Panel>
        <div style={{ ...naglowekWejscie, display: 'flex', alignItems: 'center', gap: 28 }}>
          <div style={{
            width: 118, height: 118, borderRadius: 26, background: kolor,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            boxShadow: '0 20px 50px -20px rgba(0,0,0,.7)',
          }}>
            <IkonaObszaru klucz={klucz} rozmiar={68} kolor="#FFD9C4" />
          </div>
          <div>
            <p style={{ margin: 0, fontFamily: FONT_NAGLOWEK, fontWeight: 700, fontSize: 26,
                        letterSpacing: '.2em', textTransform: 'uppercase',
                        color: MARKA.pomaranczJasny }}>
              Obszar {scena.nrObszaru} z 9
            </p>
            <h1 style={{ margin: '8px 0 0', fontFamily: FONT_NAGLOWEK, fontWeight: 900,
                         fontSize: 92, lineHeight: 1, color: '#fff' }}>
              {scena.tytul.replace('OBSZAR ', '').toLowerCase()}
            </h1>
          </div>
        </div>
        <Punkty odKlatki={22} pozycje={OPISY[klucz] ?? []} />
      </Panel>
      <PasekObszarow aktywny={scena.nrObszaru ?? 1} />
    </>
  );
};

/** Dziewięć kropek u dołu — widz cały czas wie, w którym miejscu jest film. */
const PasekObszarow: React.FC<{ aktywny: number }> = ({ aktywny }) => (
  <div style={{ position: 'absolute', left: 120, bottom: 122, display: 'flex', gap: 14 }}>
    {NOWE.map((n, i) => (
      <div key={n} style={{
        width: i + 1 === aktywny ? 54 : 16, height: 16, borderRadius: 8,
        background: i + 1 === aktywny ? MARKA.pomarancz : 'rgba(255,255,255,.28)',
        transition: 'all .3s',
      }} />
    ))}
  </div>
);

/* ── 15. FILARY ───────────────────────────────────────────────────────── */
const FILARY = [
  ['językowe', 'jezykowy'], ['matematyczne', 'matematyczny'],
  ['cyfrowe', 'cyfrowy'], ['ruchowe', 'ruchowy'],
];

export const Filary: React.FC = () => (
  <Panel>
    <Eyebrow>Kompetencje fundamentalne</Eyebrow>
    <Naglowek maly>Cztery filary, na których stoi reszta</Naglowek>
    <div style={{ marginTop: 48, display: 'flex', gap: 22 }}>
      {FILARY.map(([nazwa, klucz], i) => (
        <div key={nazwa} style={{
          ...useWejscie(14 + i * 12),
          flex: 1, background: 'rgba(255,255,255,.09)', borderRadius: 20,
          padding: '30px 24px', textAlign: 'center',
          borderBottom: `6px solid ${MARKA.pomarancz}`,
        }}>
          <div style={{ display: 'flex', justifyContent: 'center', marginBottom: 16 }}>
            <IkonaObszaru klucz={klucz} rozmiar={62} kolor={MARKA.pomaranczJasny} />
          </div>
          <p style={{ margin: 0, fontFamily: FONT_NAGLOWEK, fontWeight: 800,
                      fontSize: 40, color: '#fff' }}>{nazwa}</p>
        </div>
      ))}
    </div>
    <p style={{ ...useWejscie(64), margin: '40px 0 0', fontFamily: FONT_TEKST,
                fontSize: 36, color: MARKA.naCiemnym, maxWidth: 1020, lineHeight: 1.35 }}>
      Nie planuje się ich od święta. Wracają codziennie, w każdym obszarze.
    </p>
  </Panel>
);

/* ── 16. PRAKTYKA — cztery kroki ──────────────────────────────────────── */
const KROKI = [
  ['Sprawdź program', 'czy dopuszczony program jest zgodny z nową podstawą'],
  ['Przełóż arkusze', 'cztery stare kolumny na dziewięć nowych obszarów'],
  ['Wskaż obszar i osiągnięcie', 'w każdym celu dla dziecka'],
  ['Zrób cel mierzalnym', 'liczba, warunki, termin, narzędzie pomiaru'],
];

export const Praktyka: React.FC = () => (
  <Panel>
    <Eyebrow>Co z tego wynika dla Ciebie</Eyebrow>
    <Naglowek maly>Cztery kroki na wrzesień</Naglowek>
    <div style={{ marginTop: 42, display: 'flex', flexDirection: 'column', gap: 16 }}>
      {KROKI.map(([tytul, opis], i) => (
        <div key={i} style={{
          ...useWejscie(14 + i * 11),
          display: 'grid', gridTemplateColumns: '78px 1fr', gap: 26, alignItems: 'center',
          background: 'rgba(255,255,255,.07)', borderRadius: 16, padding: '18px 26px',
        }}>
          <div style={{
            width: 66, height: 66, borderRadius: '50%', background: MARKA.pomarancz,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            fontFamily: FONT_NAGLOWEK, fontWeight: 900, fontSize: 38, color: '#fff',
          }}>{i + 1}</div>
          <div>
            <p style={{ margin: 0, fontFamily: FONT_NAGLOWEK, fontWeight: 800,
                        fontSize: 42, color: '#fff' }}>{tytul}</p>
            <p style={{ margin: '4px 0 0', fontFamily: FONT_TEKST, fontSize: 28,
                        color: MARKA.naCiemnymDrugi }}>{opis}</p>
          </div>
        </div>
      ))}
    </div>
  </Panel>
);

/* ── 17. ARKUSZ — mapa starych obszarów na nowe ───────────────────────── */
const MAPA = [
  ['fizyczny', ['ruchowy', 'techniczny']],
  ['emocjonalny', ['osobisty']],
  ['społeczny', ['społeczny']],
  ['poznawczy', ['językowy', 'matematyczny', 'przyrodniczy', 'cyfrowy', 'artystyczny']],
] as const;

export const Arkusz: React.FC = () => (
  <Panel>
    <Eyebrow>Arkusz obserwacji</Eyebrow>
    <Naglowek maly>Nie przepisuj od zera — rozpisz</Naglowek>
    <div style={{ marginTop: 40, display: 'flex', flexDirection: 'column', gap: 14 }}>
      {MAPA.map(([stary, nowe], i) => (
        <div key={stary} style={{
          ...useWejscie(14 + i * 12),
          display: 'grid', gridTemplateColumns: '300px 60px 1fr', gap: 18, alignItems: 'center',
        }}>
          <div style={{ background: 'rgba(255,255,255,.10)', borderRadius: 12,
                        padding: '14px 22px', fontFamily: FONT_TEKST, fontSize: 30, color: '#fff' }}>
            {stary}
          </div>
          <div style={{ textAlign: 'center', fontFamily: FONT_NAGLOWEK, fontWeight: 900,
                        fontSize: 42, color: MARKA.pomarancz }}>→</div>
          <div style={{ display: 'flex', gap: 10, flexWrap: 'wrap' }}>
            {nowe.map((n) => (
              <span key={n} style={{
                background: OBSZARY_KOLOR[NOWE.find((x) => x === n) ?? 'spoleczny'] ?? MARKA.fioletJasny,
                borderRadius: 10, padding: '11px 18px',
                fontFamily: FONT_TEKST, fontSize: 26, color: '#fff',
              }}>{n}</span>
            ))}
          </div>
        </div>
      ))}
    </div>
  </Panel>
);

/* ── 18. KONIEC ───────────────────────────────────────────────────────── */
export const Koniec: React.FC<{ jestAwatar?: boolean }> = ({ jestAwatar = false }) => {
  const w = useWejscie(4);
  return (
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center',
                           paddingLeft: 110, paddingRight: 470 }}>
      {/* pożegnanie: sylwetka wraca, ale nieruchomo — mówi lektor, nie awatar */}
      <AwatarStop jest={jestAwatar} srodekX={1515} skala={0.80} gora={200} opoznienie={14} />
      <div style={{ ...w, textAlign: 'center' }}>
        <div style={{ display: 'flex', justifyContent: 'center', marginBottom: 26 }}>
          <ZnakPCTP rozmiar={112} />
        </div>
        <h1 style={{ margin: 0, fontFamily: FONT_NAGLOWEK, fontWeight: 900, fontSize: 82,
                     color: '#fff', lineHeight: 1.04 }}>
          Cel bez liczby i bez terminu<br />
          <span style={{ color: MARKA.pomaranczJasny }}>nie obroni się</span>
        </h1>
        <p style={{ ...useWejscie(26), margin: '34px 0 0', fontFamily: FONT_TEKST,
                    fontSize: 32, color: MARKA.naCiemnym, maxWidth: 980 }}>
          Gotowe cele do wszystkich dziewięciu obszarów znajdziesz w broszurze
          „Cele SMART w przedszkolu”.
        </p>
        <div style={{ ...useWejscie(40), marginTop: 34, display: 'flex',
                      justifyContent: 'center', gap: 34, flexWrap: 'wrap' }}>
          {/* Numer telefonu został usunięty z repozytorium — jeśli ma wrócić
              na planszę końcową, dopisz go tutaj jako trzecią pozycję. */}
          {[['www.eduplaner2026.pl', 'strona i baza celów'],
            ['kontakt@eduplaner2026.pl', 'pytania i zgłoszenia']].map(([a, b]) => (
            <div key={a}>
              <p style={{ margin: 0, fontFamily: FONT_NAGLOWEK, fontWeight: 800, fontSize: 30,
                          color: '#fff' }}>{a}</p>
              <p style={{ margin: '4px 0 0', fontFamily: FONT_TEKST, fontSize: 24,
                          color: MARKA.naCiemnymDrugi }}>{b}</p>
            </div>
          ))}
        </div>
        <p style={{ ...useWejscie(54), margin: '36px 0 0', fontFamily: FONT_TEKST,
                    fontSize: 21, color: MARKA.naCiemnymDrugi, maxWidth: 900 }}>
          EduPlaner 2026 · PCTP Koszalin — Pomorskie Centrum Terapii Pedagogicznej ·
          opracowanie: pedagog specjalny mgr Mirosława Ewa Jurczyszyn
        </p>
      </div>
    </AbsoluteFill>
  );
};
