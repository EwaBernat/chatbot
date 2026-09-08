import React from 'react';
import {AbsoluteFill, Audio, Sequence, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from '../marka';
import {Napisy} from '../Napisy';
import {Logo, Pojaw, useWejscie} from '../ui';
import {OryginalnyDruk, type Krok, type Ujecie} from '../kpof/OryginalnyDruk';
import {DrukPdf, type Wyroznienie, type UjeciePdf, type Prostokat} from './DrukPdf';
import kotwice from '../../public/pog/kotwice.json';
import type {Napis} from '../typy';

export type FilmPog = {audio: string; napisy: Napis[]; dlugosc: number};
export type Props = {film: FilmPog};

type Kot = Record<string, {szer: number; wys: number; kotwice: Record<string, Prostokat>}>;
const K = kotwice as unknown as Kot;
const r = (strona: string, nazwa: string): Prostokat => K[strona].kotwice[nazwa];
/** Prostokąt z kotwicy rozszerzony o marginesy (lewo, góra, prawo, dół) w punktach PDF. */
const roz = (p: Prostokat, l: number, g: number, pr: number, d: number): Prostokat => [p[0] - l, p[1] - g, p[2] + pr, p[3] + d];
/** Prostokąt od górnej krawędzi kotwicy a do górnej krawędzi kotwicy b (blok wierszy). */
const blok = (a: Prostokat, b: Prostokat, x0: number, x1: number, gora = 4, dol = 6): Prostokat => [x0, a[1] - gora, x1, b[1] - dol];

/* ---------- sceny planszowe ---------- */

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

/** Intro: kwestionariusz → GDZIE, obserwacja pogłębiona → DLACZEGO. */
const PogIntro: React.FC<{dlaczego: number; przeslanka: number}> = ({dlaczego, przeslanka}) => {
  const frame = useCurrentFrame();
  const w2 = useWejscie(dlaczego, {damping: 11, stiffness: 120});
  const w3 = useWejscie(przeslanka);
  const puls = 1 + 0.02 * Math.sin(frame / 9);
  return (
    <Tlo>
      <Pojaw od={0} style={{position: 'absolute', left: 0, right: 0, top: 96, textAlign: 'center'}}>
        <div style={{fontSize: 20, letterSpacing: 4, color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase'}}>EduPlaner 2026 · Ścieżka dziecka · przystanek trzeci</div>
        <div style={{fontSize: 74, fontWeight: 800, color: '#fff', marginTop: 12, letterSpacing: -1}}>Obserwacja pogłębiona</div>
      </Pojaw>
      <div style={{position: 'absolute', left: 0, right: 0, top: 360, display: 'flex', justifyContent: 'center', gap: 60, alignItems: 'stretch'}}>
        <Karta od={8} style={{width: 620}}>
          <div style={{fontSize: 18, letterSpacing: 3, color: '#F6A57E', fontWeight: 700}}>KWESTIONARIUSZ KPOF · WSZYSTKIE DZIECI</div>
          <div style={{fontSize: 92, fontWeight: 800, lineHeight: 1, marginTop: 14}}>GDZIE?</div>
          <div style={{fontSize: 24, color: 'rgba(255,255,255,0.85)', marginTop: 14, lineHeight: 1.4}}>Przesiew mówi, w którym obszarze dziecko potrzebuje wsparcia.</div>
        </Karta>
        <div style={{alignSelf: 'center', fontSize: 70, color: '#F6A57E', opacity: w2, transform: `translateX(${(1 - w2) * -30}px)`}}>→</div>
        <div style={{width: 620, opacity: w2, transform: `translateY(${(1 - w2) * 40}px) scale(${puls})`, background: MARKA.pomarancz, borderRadius: 18, padding: '22px 26px', color: '#fff', boxShadow: '0 24px 60px rgba(232,69,10,0.45)'}}>
          <div style={{fontSize: 18, letterSpacing: 3, color: 'rgba(255,255,255,0.85)', fontWeight: 700}}>OBSERWACJA POGŁĘBIONA · JEDNO DZIECKO</div>
          <div style={{fontSize: 92, fontWeight: 800, lineHeight: 1, marginTop: 14}}>DLACZEGO?</div>
          <div style={{fontSize: 24, marginTop: 14, lineHeight: 1.4}}>Cztery narzędzia, każde odpowiada na inne pytanie.</div>
        </div>
      </div>
      <div style={{position: 'absolute', left: 0, right: 0, top: 790, textAlign: 'center', opacity: w3, transform: `translateY(${(1 - w3) * 20}px)`}}>
        <span style={{display: 'inline-block', border: '2px solid rgba(255,255,255,0.5)', borderRadius: 999, padding: '14px 34px', fontSize: 28, color: '#fff', fontWeight: 700}}>
          Uruchamiamy ją z przesłanką — nie „na wszelki wypadek”
        </span>
      </div>
    </Tlo>
  );
};

const REGULY = [
  ['1', 'Średnia obszaru poniżej 2,0'],
  ['2', 'Dwa lub więcej twierdzeń na 1–2 w tym samym obszarze'],
  ['3', 'Rozbieżność między oceniającymi ≥ 1,5 pkt'],
  ['4', 'Sygnał zdrowotny z metryczki (np. nadwrażliwość)'],
  ['5', 'Zachowanie powtarzalne, które zagraża — natychmiast'],
  ['6', 'Brak poprawy mimo pomocy przez ok. 3 miesiące'],
];

/** Sześć reguł przekierowania (wg skryptu) + karta decyzyjna. */
const Reguly: React.FC<{start: number; koniec: number; karta: number}> = ({start, koniec, karta}) => {
  const krok = Math.max(8, (koniec - start) / REGULY.length);
  const wk = useWejscie(karta, {damping: 12, stiffness: 120});
  return (
    <Tlo>
      <Pojaw od={0} style={{position: 'absolute', left: 0, right: 0, top: 70, textAlign: 'center'}}>
        <div style={{fontSize: 20, letterSpacing: 4, color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase'}}>Kiedy uruchamiamy</div>
        <div style={{fontSize: 60, fontWeight: 800, color: '#fff', marginTop: 8}}>Sześć reguł przekierowania <span style={{color: '#F6A57E'}}>— wystarczy jedna</span></div>
      </Pojaw>
      <div style={{position: 'absolute', left: 160, right: 160, top: 250, display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: 22}}>
        {REGULY.map(([n, t], i) => (
          <Karta key={n} od={start + i * krok} style={{display: 'flex', gap: 18, alignItems: 'center', minHeight: 150}}>
            <div style={{width: 64, height: 64, borderRadius: '50%', background: MARKA.pomarancz, display: 'grid', placeItems: 'center', fontSize: 32, fontWeight: 800, flexShrink: 0}}>{n}</div>
            <div style={{fontSize: 25, fontWeight: 700, lineHeight: 1.3}}>{t}</div>
          </Karta>
        ))}
      </div>
      <div style={{position: 'absolute', left: 0, right: 0, top: 660, display: 'flex', justifyContent: 'center', opacity: wk, transform: `translateY(${(1 - wk) * 40}px)`}}>
        <div style={{background: '#fff', color: MARKA.fiolet, borderRadius: 22, padding: '26px 44px', display: 'flex', gap: 28, alignItems: 'center', boxShadow: '0 24px 60px rgba(0,0,0,0.35)', width: 1200}}>
          <div style={{fontSize: 64}}>🗂️</div>
          <div>
            <div style={{fontSize: 34, fontWeight: 800}}>Karta decyzyjna — jedna na jedno dziecko</div>
            <div style={{fontSize: 22, color: MARKA.tekstDrugi, marginTop: 8, lineHeight: 1.4}}>Która reguła zadziałała · jakie narzędzie · kto obserwuje i od kiedy · termin spotkania zespołu. Wpinamy do teczki także wtedy, gdy decyzja brzmi: <b>nie uruchamiamy</b>.</div>
          </div>
        </div>
      </div>
    </Tlo>
  );
};

/** Dlaczego obserwacja, a nie diagnoza — granica kompetencji. */
const Kompetencje: React.FC<{granica: number; nauczyciel: number; specjalista: number; zapis: number}> = ({granica, nauczyciel, specjalista, zapis}) => {
  const wl = useWejscie(granica);
  const wz = useWejscie(zapis, {damping: 10, stiffness: 140});
  return (
    <Tlo>
      <Pojaw od={0} style={{position: 'absolute', left: 0, right: 0, top: 80, textAlign: 'center'}}>
        <div style={{fontSize: 64, fontWeight: 800, color: '#fff'}}>Dlaczego obserwacja, <span style={{color: '#F6A57E'}}>a nie diagnoza?</span></div>
        <div style={{fontSize: 26, color: 'rgba(255,255,255,0.8)', marginTop: 10}}>Bo granica kompetencji jest jasna.</div>
      </Pojaw>
      <div style={{position: 'absolute', left: 140, right: 140, top: 300, display: 'flex', gap: 0, alignItems: 'stretch'}}>
        <Karta od={nauczyciel} style={{flex: 1, minHeight: 300}}>
          <div style={{fontSize: 18, letterSpacing: 3, color: '#F6A57E', fontWeight: 700}}>NAUCZYCIEL</div>
          <div style={{fontSize: 44, fontWeight: 800, marginTop: 10}}>opisuje</div>
          <div style={{fontSize: 24, marginTop: 14, lineHeight: 1.45, color: 'rgba(255,255,255,0.9)'}}>to, co widzi i słyszy w naturalnych sytuacjach: częstość, okoliczności, wzorzec. Bez etykiet, bez interpretacji.</div>
        </Karta>
        <div style={{width: 6, margin: '0 40px', background: `linear-gradient(180deg, transparent, ${MARKA.pomarancz} 30%, ${MARKA.pomarancz} 70%, transparent)`, transform: `scaleY(${wl})`, borderRadius: 3}} />
        <Karta od={specjalista} style={{flex: 1, minHeight: 300}}>
          <div style={{fontSize: 18, letterSpacing: 3, color: '#F6A57E', fontWeight: 700}}>SPECJALISTA · PORADNIA</div>
          <div style={{fontSize: 44, fontWeight: 800, marginTop: 10}}>rozpoznaje</div>
          <div style={{fontSize: 24, marginTop: 14, lineHeight: 1.45, color: 'rgba(255,255,255,0.9)'}}>terapeuta integracji sensorycznej, psycholog, logopeda, zespół orzekający. Diagnoza i kwalifikacja do terapii należą do nich.</div>
        </Karta>
      </div>
      <div style={{position: 'absolute', left: 0, right: 0, top: 730, display: 'flex', justifyContent: 'center', opacity: wz, transform: `scale(${0.8 + 0.2 * wz}) rotate(${-2 * (1 - wz)}deg)`}}>
        <div style={{border: `4px solid #F6A57E`, color: '#fff', borderRadius: 14, padding: '18px 36px', fontSize: 30, fontWeight: 700, letterSpacing: 0.5, background: 'rgba(0,0,0,0.18)'}}>
          W dokumentacji: „obserwowany wzorzec … — wskazana konsultacja specjalisty”
        </div>
      </div>
    </Tlo>
  );
};

/** Czego się dowiadujemy i dokąd trafiają wnioski. */
const Wnioski: React.FC<{pyt: number; co: number; dokad: number}> = ({pyt, co, dokad}) => {
  const CO = ['co obserwowaliśmy', 'jak często', 'w jakich sytuacjach', 'co z tego wynika dla wsparcia'];
  const DOKAD = ['Ocena wielospecjalistyczna (WOPF)', 'Program — cele SMART', 'Opinia dla poradni'];
  return (
    <Tlo>
      <Pojaw od={pyt} style={{position: 'absolute', left: 0, right: 0, top: 90, textAlign: 'center'}}>
        <div style={{fontSize: 70, fontWeight: 800, color: '#fff'}}>Czego się <span style={{color: '#F6A57E'}}>dowiadujemy?</span></div>
      </Pojaw>
      <div style={{position: 'absolute', left: 170, right: 170, top: 250, display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 20}}>
        {CO.map((t, i) => (
          <Karta key={t} od={co + i * 9} style={{textAlign: 'center', minHeight: 150, display: 'grid', placeItems: 'center'}}>
            <div style={{fontSize: 27, fontWeight: 700, lineHeight: 1.3}}>{t}</div>
          </Karta>
        ))}
      </div>
      <Pojaw od={dokad} style={{position: 'absolute', left: 0, right: 0, top: 470, textAlign: 'center'}}>
        <div style={{fontSize: 22, letterSpacing: 4, color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase'}}>Wnioski przechodzą dalej</div>
        <div style={{fontSize: 54, color: '#F6A57E', marginTop: 6}}>↓</div>
      </Pojaw>
      <div style={{position: 'absolute', left: 170, right: 170, top: 600, display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 22}}>
        {DOKAD.map((t, i) => (
          <Karta key={t} od={dokad + 10 + i * 9} akcent style={{textAlign: 'center', minHeight: 130, display: 'grid', placeItems: 'center', boxShadow: '0 20px 50px rgba(232,69,10,0.35)'}}>
            <div style={{fontSize: 30, fontWeight: 800, lineHeight: 1.25}}>{t}</div>
          </Karta>
        ))}
      </div>
    </Tlo>
  );
};

const PRAWO = [
  ['Rozpoznawanie indywidualnych potrzeb i możliwości psychofizycznych dziecka oraz ocena efektywności pomocy', 'rozporządzenie o pomocy psychologiczno-pedagogicznej — t.j. Dz.U. 2023 poz. 1798'],
  ['Wystąpienie do poradni, gdy mimo udzielanej pomocy nie ma poprawy', 'za zgodą rodziców, na wniosek dyrektora'],
  ['Reguły przekierowania i karta decyzyjna', 'nie wynikają wprost z przepisu — decyzja rady pedagogicznej wpisana do procedury placówki'],
];

const PogFinal: React.FC<{haslo: number; prawo: number[]}> = ({haslo, prawo}) => {
  const wp = useWejscie(prawo[0] - 10);
  return (
    <Tlo>
      <div style={{position: 'absolute', left: 0, right: 0, top: 70, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
        <Logo rozmiar={110} />
        <div style={{fontSize: 84, fontWeight: 800, color: '#fff', letterSpacing: -2, marginTop: 14, lineHeight: 1}}>EduPlaner <span style={{color: '#F6A57E'}}>2026</span></div>
        <Pojaw od={haslo}>
          <div style={{fontSize: 38, color: '#fff', fontWeight: 700, marginTop: 16}}>Mniej dokumentów. Więcej edukacji.</div>
        </Pojaw>
      </div>
      <div style={{position: 'absolute', left: 300, right: 300, top: 420, background: 'rgba(255,255,255,0.08)', border: '1.5px solid rgba(255,255,255,0.28)', borderRadius: 22, padding: '26px 40px', opacity: wp, transform: `translateY(${(1 - wp) * 30}px)`}}>
        <div style={{fontSize: 17, letterSpacing: 3, color: '#F6A57E', fontWeight: 700, marginBottom: 6}}>⚖ PODSTAWA PRAWNA OBSERWACJI POGŁĘBIONEJ · WG SKRYPTU SZKOLENIA (WYD. 2 PO AUDYCIE)</div>
        {PRAWO.map(([t, o], i) => (
          <Pojaw key={t} od={prawo[i]}>
            <div style={{display: 'flex', gap: 16, padding: '14px 0', borderBottom: i < PRAWO.length - 1 ? '1px solid rgba(255,255,255,0.15)' : 'none'}}>
              <div style={{color: MARKA.pomarancz, fontSize: 24, fontWeight: 800}}>✓</div>
              <div>
                <div style={{fontSize: 25, fontWeight: 700, color: '#fff', lineHeight: 1.3}}>{t}</div>
                <div style={{fontSize: 19, color: 'rgba(255,255,255,0.75)', marginTop: 4}}>{o}</div>
              </div>
            </div>
          </Pojaw>
        ))}
      </div>
      <div style={{position: 'absolute', left: 0, right: 0, bottom: 150, textAlign: 'center', fontSize: 19, color: 'rgba(255,255,255,0.65)', letterSpacing: 2}}>EDUPLANER 2026 · PCTP KOSZALIN · kontakt@eduplaner2026.pl · 662 888 403</div>
    </Tlo>
  );
};

/* ---------- składanie filmu ---------- */

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

/** Oceny w karcie mowy wg przykładu ze skryptu: rozumienie 8, mowa czynna 6, słuch fonematyczny 3. */
const MOWA: Record<string, string[]> = {'cmp-1': ['2', '2', '2', '1', '1'], 'cmp-2': ['2', '1', '1', '1', '1'], 'cmp-3': ['1', '1', '1', '0', '0']};

export const PogPromo: React.FC<Props> = ({film}) => {
  const {fps} = useVideoConfig();
  const n = film.napisy;
  const z = (i: number) => n[i]?.odSek ?? i * 4;
  const kz = (i: number) => n[i]?.doSek ?? i * 4 + 3;
  const granica = (i: number) => (i <= 0 ? 0 : (kz(i - 1) + z(i)) / 2);
  const fr = (sek: number) => Math.round(sek * fps);
  const koniec = film.dlugosc;

  type Scena = {id: string; od: number; do: number; el: (od: number, trwanie: number) => React.ReactNode};
  const lok = (od: number) => (s: number) => Math.max(0, fr(s - od)); // sekunda filmu → klatka lokalna sceny

  const sceny: Scena[] = [
    {id: 'intro', od: 0, do: granica(3), el: (od) => <PogIntro dlaczego={lok(od)(z(1))} przeslanka={lok(od)(z(2))} />},
    {id: 'reguly', od: granica(3), do: granica(5), el: (od) => <Reguly start={lok(od)(z(3) + 1.2)} koniec={lok(od)(kz(3) - 1)} karta={lok(od)(z(4))} />},
    {id: 'kompetencje', od: granica(5), do: granica(10), el: (od) => <Kompetencje granica={lok(od)(z(6))} nauczyciel={lok(od)(z(7))} specjalista={lok(od)(z(8))} zapis={lok(od)(z(9))} />},
    {
      id: 'abc', od: granica(10), do: granica(15),
      el: (od) => {
        // pola A/B/C i pierwszy wiersz rejestru — geometria odczytana z druku (punkty PDF)
        const A: Prostokat = [31, 204, 202, 269]; const B: Prostokat = [211, 204, 382, 269]; const C: Prostokat = [391, 204, 563, 269];
        const W: Prostokat = [31, 338, 566, 372];
        const wyr: Wyroznienie[] = [
          {sek: z(11), doSek: kz(13) + 0.4, strona: 0, rect: A, pad: 4, etykieta: 'A · poprzednik', kolor: '#2E9E52'},
          {sek: z(12), doSek: kz(13) + 0.4, strona: 0, rect: B, pad: 4, etykieta: 'B · zachowanie', kolor: MARKA.fiolet},
          {sek: z(13), doSek: kz(13) + 0.4, strona: 0, rect: C, pad: 4, etykieta: 'C · następstwo'},
          {sek: z(14), doSek: z(14) + 3.2, strona: 0, rect: W, pad: 4, etykieta: 'zapis obserwowalny — bez interpretacji'},
          {sek: z(14) + 3.4, doSek: kz(14) + 0.6, strona: 1, rect: roz(r('bhw_6', 'odczyt'), 12, 8, 500, 118), etykieta: 'funkcja dominująca'},
        ];
        const kam: UjeciePdf[] = [
          {sek: 0, strona: 0, y: 250, skala: 1.35},
          {sek: z(11), strona: 0, y: 235, skala: 1.55},
          {sek: z(14), strona: 0, y: 290, skala: 1.5},
          {sek: z(14) + 3.4, strona: 1, y: 330, skala: 1.35},
        ];
        return <DrukPdf strony={['bhw_3', 'bhw_6']} szerokoscPt={K.bhw_3.szer} wysokoscPt={K.bhw_3.wys} wyroznienia={wyr} kamera={kam} odSek={od} />;
      },
    },
    {
      id: 'sens', od: granica(15), do: granica(18),
      el: (od) => {
        const nad = r('sens_2', 'nad'); const pod = r('sens_2', 'pod'); const szum = r('sens_2', 'szum'); const sluch = r('sens_2', 'sluch');
        const t16 = z(16); const d16 = (kz(16) - z(16)) / 3;
        const wyr: Wyroznienie[] = [
          {sek: t16 + d16 * 1.05, doSek: kz(17) + 0.5, strona: 0, rect: blok(nad, pod, 36, 560), etykieta: 'nadreaktywność', kolor: '#D93B30'},
          {sek: t16 + d16 * 1.75, doSek: kz(17) + 0.5, strona: 0, rect: blok(pod, szum, 36, 560), etykieta: 'podreaktywność', kolor: '#2E9E52'},
          {sek: t16 + d16 * 2.45, doSek: kz(17) + 0.5, strona: 0, rect: blok(szum, sluch, 36, 560, 4, 14), etykieta: 'poszukiwanie bodźców · biały szum', kolor: '#B3891A'},
          {sek: z(17) + 1.2, doSek: kz(17) + 0.6, strona: 1, rect: roz(r('sens_7', 'slupki'), 12, 10, 300, 150), etykieta: 'wzorzec, nie rozpoznanie'},
        ];
        const kam: UjeciePdf[] = [
          {sek: 0, strona: 0, y: 260, skala: 1.35},
          {sek: t16 + d16 * 1.05, strona: 0, y: 225, skala: 1.6},
          {sek: z(17) + 1.2, strona: 1, y: 300, skala: 1.35},
        ];
        return <DrukPdf strony={['sens_2', 'sens_7']} szerokoscPt={K.sens_2.szer} wysokoscPt={K.sens_2.wys} wyroznienia={wyr} kamera={kam} odSek={od} />;
      },
    },
    {
      id: 'tom', od: granica(18), do: granica(22),
      el: (od) => {
        const prag = r('tom_2', 'pragnienia'); const nan = r('tom_2', 'naniby'); const w14 = r('tom_2', 'w14');
        const wyr: Wyroznienie[] = [
          {sek: z(19), doSek: kz(20) + 0.3, strona: 0, rect: [36, prag[1] - 8, 560, nan[1] - 26], etykieta: 'różne pragnienia i upodobania'},
          {sek: z(20), doSek: kz(20) + 0.3, strona: 0, rect: [36, nan[1] - 8, 560, w14[3] + 36], etykieta: 'zabawa „na niby” i udawanie', kolor: MARKA.fiolet},
          {sek: z(21) + 0.6, doSek: kz(21) + 0.6, strona: 1, rect: roz(r('tom_5', 'odczyt'), 12, 8, 220, 118), etykieta: 'opis, nie test'},
        ];
        const kam: UjeciePdf[] = [
          {sek: 0, strona: 0, y: 250, skala: 1.35},
          {sek: z(19), strona: 0, y: 300, skala: 1.45},
          {sek: z(21) + 0.6, strona: 1, y: 330, skala: 1.35},
        ];
        return <DrukPdf strony={['tom_2', 'tom_5']} szerokoscPt={K.tom_2.szer} wysokoscPt={K.tom_2.wys} wyroznienia={wyr} kamera={kam} odSek={od} />;
      },
    },
    {
      id: 'mowa', od: granica(22), do: granica(28),
      el: (od) => {
        const kroki: Krok[] = [];
        const tabele = ['cmp-1', 'cmp-2', 'cmp-3'];
        const czasy = [z(24), z(25), z(26)];
        const konce = [kz(24), kz(25), kz(26)];
        tabele.forEach((t, ti) => {
          const w = MOWA[t];
          const dt = (konce[ti] - czasy[ti]) / (w.length + 0.5);
          // pierwszy wiersz tbody to nagłówek obszaru, stąd i + 1
          w.forEach((v, i) => kroki.push({sek: czasy[ti] + 0.3 + i * dt, typ: 'ocena', obszar: t, tabela: `#${t}`, wiersz: i + 1, wartosc: v}));
        });
        kroki.push({sek: z(23), doSek: kz(23) + 0.3, typ: 'wyroznij', selektor: '.scaleleg, .sec-note'});
        const kam: Ujecie[] = [
          {sek: 0, selektor: '.sheet:nth-of-type(1) .eyebrow', skala: 1.3, przesun: 220},
          {sek: z(23), selektor: '#cmp-1', skala: 1.5, przesun: 120},
          {sek: z(25), selektor: '#cmp-2', skala: 1.5, przesun: 120},
          {sek: z(26), selektor: '#cmp-3', skala: 1.5, przesun: 120},
          {sek: z(27) - 0.4, selektor: '.sheet:nth-of-type(5) svg', skala: 1.5, przesun: 40, czas: 0.9},
        ];
        return <OryginalnyDruk plik="karta_mowy.html" kroki={kroki} kamera={kam} odSek={od} />;
      },
    },
    {
      id: 'bio', od: granica(28), do: granica(29),
      el: (od) => {
        const zas = r('bio_4', 'zasoby'); const bar = r('bio_4', 'bariery'); const ula = r('bio_4', 'ulatwiacze'); const spo = r('bio_4', 'sporzadzil');
        const d = (kz(28) - z(28)) / 4;
        const wyr: Wyroznienie[] = [
          {sek: z(28) + d * 1.4, doSek: kz(28) + 0.6, strona: 0, rect: [28, zas[1] - 4, 568, bar[1] - 8], etykieta: 'zasoby', kolor: '#2E9E52'},
          {sek: z(28) + d * 2.1, doSek: kz(28) + 0.6, strona: 0, rect: [28, bar[1] - 4, 568, ula[1] - 8], etykieta: 'bariery', kolor: '#D93B30'},
          {sek: z(28) + d * 2.8, doSek: kz(28) + 0.6, strona: 0, rect: [28, ula[1] - 4, 568, spo[1] - 30], etykieta: 'ułatwiacze', kolor: MARKA.fiolet},
        ];
        const kam: UjeciePdf[] = [{sek: 0, strona: 0, y: 300, skala: 1.3}, {sek: z(28) + d, strona: 0, y: 420, skala: 1.5}];
        return <DrukPdf strony={['bio_4']} szerokoscPt={K.bio_4.szer} wysokoscPt={K.bio_4.wys} wyroznienia={wyr} kamera={kam} odSek={od} />;
      },
    },
    {id: 'wnioski', od: granica(29), do: granica(32), el: (od) => <Wnioski pyt={lok(od)(z(29))} co={lok(od)(z(30))} dokad={lok(od)(z(31))} />},
    {id: 'final', od: granica(32), do: koniec, el: (od) => <PogFinal haslo={lok(od)(z(33))} prawo={[lok(od)(z(34)), lok(od)(z(35)), lok(od)(z(36))]} />},
  ];

  return (
    <AbsoluteFill style={{background: MARKA.tlo}}>
      <Audio src={staticFile(film.audio)} />
      {sceny.map((s) => {
        const od = fr(s.od);
        const trwanie = Math.max(1, fr(s.do) - od);
        return (
          <Sequence key={s.id} from={od} durationInFrames={trwanie} name={s.id}>
            <Przejscie trwanie={trwanie}>{s.el(s.od, trwanie)}</Przejscie>
          </Sequence>
        );
      })}
      <Napisy napisy={n} />
      <PasekPostepu />
    </AbsoluteFill>
  );
};
