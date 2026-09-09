import React from 'react';
import {AbsoluteFill, Audio, Sequence, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from '../marka';
import {Napisy} from '../Napisy';
import {Logo, Pojaw, useWejscie} from '../ui';
import {OryginalnyDruk, type Krok, type Ujecie} from '../kpof/OryginalnyDruk';
import type {Napis} from '../typy';
import ocenyJson from '../../public/kszof-oceny.json';

/** Film „Jak policzyć KSzOF ręcznie” — wzór na średnią, skąd biorą się steny, co znaczy poziom wsparcia. */
export type FilmLiczenie = {audio: string | null; napisy: Napis[]; dlugosc: number};
export type Props = {film: FilmLiczenie};
type Ocena = {a: number; i: number; lp: number; ob: string; v: number};
const OCENY = ocenyJson as unknown as Ocena[];

const ZIELONY = '#2E7D46';
const ZOLTY = '#E0A32E';
const CZERWONY = '#C0392B';

/* ---------- elementy plansz ---------- */
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
  <Pojaw od={od} style={{position: 'absolute', left: 110, right: 110, top: 60, textAlign: 'center'}}>
    <div style={{fontSize: 19, letterSpacing: 4, color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase'}}>{kicker}</div>
    <div style={{fontSize: 52, fontWeight: 800, color: '#fff', marginTop: 10, letterSpacing: -1, lineHeight: 1.1}}>{tytul}</div>
  </Pojaw>
);
const Kolo: React.FC<{n: string | number; kolor?: string; rozmiar?: number}> = ({n, kolor = MARKA.morski, rozmiar = 54}) => (
  <div style={{width: rozmiar, height: rozmiar, borderRadius: '50%', background: kolor, display: 'grid', placeItems: 'center', fontSize: rozmiar * 0.42, fontWeight: 800, flex: '0 0 auto', color: '#fff'}}>{n}</div>
);

/** Wiersz rachunku — pojawia się w rytm narracji; wynik na pomarańczowo. */
type Wiersz = {od: number; t: React.ReactNode; wynik?: boolean; male?: boolean};
const Rachunek: React.FC<{wiersze: Wiersz[]; style?: React.CSSProperties}> = ({wiersze, style}) => (
  <div style={{position: 'absolute', left: 150, right: 150, top: 215, display: 'flex', flexDirection: 'column', gap: 14, ...style}}>
    {wiersze.map((w, i) => {
      const p = useWejscie(w.od, {damping: 14, stiffness: 120});
      return (
        <div
          key={i}
          style={{
            opacity: p,
            transform: `translateX(${(1 - p) * -26}px)`,
            background: w.wynik ? MARKA.pomarancz : 'rgba(255,255,255,0.08)',
            border: `1.5px solid ${w.wynik ? MARKA.pomarancz : 'rgba(255,255,255,0.24)'}`,
            borderRadius: 14,
            padding: w.male ? '13px 24px' : '17px 26px',
            color: '#fff',
            fontSize: w.male ? 26 : 33,
            fontWeight: w.wynik ? 800 : 600,
            lineHeight: 1.3,
          }}
        >
          {w.t}
        </div>
      );
    })}
  </div>
);

/** Skala 1–5 z zaznaczoną średnią i progami poziomów. */
const SkalaSrednich: React.FC<{od: number; srednia?: number; progi?: boolean; podpis?: string}> = ({od, srednia, progi, podpis}) => {
  const p = useWejscie(od, {damping: 16, stiffness: 90});
  const frame = useCurrentFrame();
  const wyp = interpolate(frame, [od + 8, od + 34], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const poz = (v: number) => ((v - 1) / 4) * 100;
  return (
    <div style={{opacity: p, position: 'absolute', left: 170, right: 170, top: 430}}>
      <div style={{position: 'relative', height: 62, borderRadius: 31, background: 'rgba(255,255,255,0.12)', border: '1.5px solid rgba(255,255,255,0.3)', overflow: 'hidden'}}>
        {progi ? (
          <>
            <div style={{position: 'absolute', left: 0, top: 0, bottom: 0, width: `${poz(2.2308)}%`, background: 'rgba(192,57,43,0.55)'}} />
            <div style={{position: 'absolute', left: `${poz(2.2308)}%`, top: 0, bottom: 0, width: `${poz(3.7308) - poz(2.2308)}%`, background: 'rgba(224,163,46,0.55)'}} />
            <div style={{position: 'absolute', left: `${poz(3.7308)}%`, top: 0, right: 0, background: 'rgba(46,125,70,0.55)'}} />
          </>
        ) : null}
        {srednia !== undefined ? <div style={{position: 'absolute', left: 0, top: 0, bottom: 0, width: `${poz(srednia) * wyp}%`, background: MARKA.pomarancz, opacity: progi ? 0.85 : 1}} /> : null}
      </div>
      <div style={{position: 'relative', height: 46, marginTop: 8}}>
        {[1, 2, 3, 4, 5].map((v) => (
          <div key={v} style={{position: 'absolute', left: `${poz(v)}%`, transform: 'translateX(-50%)', fontSize: 27, fontWeight: 800, color: 'rgba(255,255,255,0.85)'}}>{v}</div>
        ))}
      </div>
      {progi ? (
        <div style={{position: 'relative', height: 40}}>
          <div style={{position: 'absolute', left: `${poz(2.2308)}%`, transform: 'translateX(-50%)', fontSize: 24, fontWeight: 800, color: '#F6A57E'}}>2,23</div>
          <div style={{position: 'absolute', left: `${poz(3.7308)}%`, transform: 'translateX(-50%)', fontSize: 24, fontWeight: 800, color: '#F6A57E'}}>3,73</div>
        </div>
      ) : null}
      {podpis ? <div style={{textAlign: 'center', fontSize: 27, color: 'rgba(255,255,255,0.85)', marginTop: 10, lineHeight: 1.35}}>{podpis}</div> : null}
    </div>
  );
};

/* ---------- plansze ---------- */
const Intro: React.FC = () => (
  <Tlo>
    <Pojaw od={0} style={{position: 'absolute', left: 0, right: 0, top: 190, textAlign: 'center'}}>
      <div style={{fontSize: 20, letterSpacing: 4, color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase'}}>EduPlaner 2026 · Szkoła podstawowa · KSzOF</div>
      <div style={{fontSize: 104, fontWeight: 800, color: '#fff', marginTop: 16, letterSpacing: -3, lineHeight: 1}}>Jak to <span style={{color: '#F6A57E'}}>policzyć</span></div>
      <div style={{fontSize: 38, fontWeight: 700, color: '#fff', marginTop: 18, lineHeight: 1.25}}>Średnia, sten i poziom wsparcia — krok po kroku</div>
    </Pojaw>
    <Pojaw od={30} style={{position: 'absolute', left: 300, right: 300, top: 660}}>
      <Karta od={30} akcent style={{textAlign: 'center', fontSize: 29, fontWeight: 700}}>Na kartce, bez arkusza kalkulacyjnego</Karta>
    </Pojaw>
  </Tlo>
);

const Pytania: React.FC<{a: number; b: number; c: number}> = ({a, b, c}) => (
  <Tlo>
    <Naglowek kicker="Odpowiemy na trzy pytania" tytul="Plan modułu" />
    <div style={{position: 'absolute', left: 120, right: 120, top: 260, display: 'flex', gap: 24}}>
      {[
        {od: a, n: '1', t: <>Jaki jest <b style={{color: '#F6A57E'}}>wzór na średnią</b> i jak ją policzyć</>},
        {od: b, n: '2', t: <>Skąd biorą się <b style={{color: '#F6A57E'}}>steny</b> i z czego wynikają</>},
        {od: c, n: '3', t: <>Co oznacza <b style={{color: '#F6A57E'}}>kwalifikacja do poziomu wsparcia</b></>},
      ].map((k) => (
        <Karta key={k.n} od={k.od} style={{flex: 1, padding: '34px 28px', fontSize: 28, lineHeight: 1.35, textAlign: 'center'}}>
          <div style={{display: 'flex', justifyContent: 'center'}}><Kolo n={k.n} rozmiar={62} kolor={MARKA.pomarancz} /></div>
          <div style={{marginTop: 20}}>{k.t}</div>
        </Karta>
      ))}
    </div>
  </Tlo>
);

const CoLiczymy: React.FC<{a: number; b: number}> = ({a, b}) => (
  <Tlo>
    <Naglowek kicker="Zacznijmy od tego, co w ogóle liczymy" tytul="Arkusz KSzOF · klasy IV–VI" />
    <div style={{position: 'absolute', left: 130, right: 130, top: 275, display: 'flex', gap: 26}}>
      {[
        {v: '52', p: 'pozycje do oceny'},
        {v: '9', p: 'obszarów ICF'},
        {v: '1–5', p: 'punktów za pozycję'},
      ].map((k, i) => (
        <Karta key={k.v} od={a + i * 7} style={{flex: 1, textAlign: 'center', padding: '40px 20px'}}>
          <div style={{fontSize: 88, fontWeight: 800, lineHeight: 1, color: '#F6A57E'}}>{k.v}</div>
          <div style={{fontSize: 27, marginTop: 14}}>{k.p}</div>
        </Karta>
      ))}
    </div>
    <Karta od={b} akcent style={{position: 'absolute', left: 200, right: 200, top: 610, textAlign: 'center', padding: '30px 26px'}}>
      <div style={{fontSize: 25, letterSpacing: 3, fontWeight: 800, color: 'rgba(255,255,255,0.85)'}}>WYNIK MOŻLIWY DO UZYSKANIA</div>
      <div style={{fontSize: 72, fontWeight: 800, marginTop: 10, lineHeight: 1}}>52 – 260 pkt</div>
    </Karta>
  </Tlo>
);

const DwaWyniki: React.FC<{a: number; b: number; c: number}> = ({a, b, c}) => (
  <Tlo>
    <Naglowek kicker="Liczymy dwa wyniki" tytul="Obszarowy i ogólny" />
    <div style={{position: 'absolute', left: 140, right: 140, top: 250, display: 'flex', gap: 26}}>
      <Karta od={a} style={{flex: 1, padding: '30px 28px', textAlign: 'center'}}>
        <div style={{fontSize: 23, letterSpacing: 3, fontWeight: 800, color: '#F6A57E'}}>WYNIK OBSZAROWY</div>
        <div style={{fontSize: 32, fontWeight: 700, marginTop: 14, lineHeight: 1.3}}>dla każdego z 9 obszarów<br />osobno</div>
      </Karta>
      <Karta od={a + 8} style={{flex: 1, padding: '30px 28px', textAlign: 'center'}}>
        <div style={{fontSize: 23, letterSpacing: 3, fontWeight: 800, color: '#F6A57E'}}>WYNIK OGÓLNY</div>
        <div style={{fontSize: 32, fontWeight: 700, marginTop: 14, lineHeight: 1.3}}>dla całego<br />arkusza</div>
      </Karta>
    </div>
    <Karta od={b} style={{position: 'absolute', left: 200, right: 200, top: 520, textAlign: 'center', fontSize: 30, fontWeight: 700, padding: '24px 26px'}}>
      Oba wyrażamy w <b style={{color: '#F6A57E'}}>stenach</b>, w skali od 1 do 10
    </Karta>
    <Karta od={c} akcent style={{position: 'absolute', left: 150, right: 150, top: 650, textAlign: 'center', padding: '30px 26px'}}>
      <div style={{fontSize: 40, fontWeight: 800, lineHeight: 1.2}}>Wysoki sten to DOBRY wynik</div>
      <div style={{fontSize: 28, marginTop: 12}}>oznacza mniej wsparcia, a nie więcej</div>
    </Karta>
  </Tlo>
);

const Przedzialy: React.FC<{tyt: number; a: number; b: number; c: number}> = ({tyt, a, b, c}) => (
  <Tlo>
    <Naglowek kicker="Krok 4 · trzy przedziały, trzy wzory" tytul="Z pozycji na sten" od={tyt} />
    <div style={{position: 'absolute', left: 100, right: 100, top: 240, display: 'flex', flexDirection: 'column', gap: 20}}>
      {[
        {od: a, kol: CZERWONY, tag: 'WYNIK NISKI · POZIOM III', zakres: 'pozycja poniżej 0,31', wzor: 'sten = 1 + (pozycja ÷ 0,31) × 3', out: 'sten 1–4'},
        {od: b, kol: ZOLTY, tag: 'WYNIK PRZECIĘTNY · POZIOM II', zakres: 'pozycja od 0,31 do 0,68', wzor: 'sten = 5 + ((pozycja − 0,31) ÷ 0,37) × 2', out: 'sten 5–7'},
        {od: c, kol: ZIELONY, tag: 'WYNIK WYSOKI · POZIOM I', zakres: 'pozycja od 0,68 w górę', wzor: 'sten = 8 + ((pozycja − 0,68) ÷ 0,32) × 2', out: 'sten 8–10'},
      ].map((k) => (
        <Karta key={k.tag} od={k.od} style={{padding: '20px 26px', borderColor: k.kol, background: 'rgba(255,255,255,0.07)', display: 'flex', alignItems: 'center', gap: 24}}>
          <div style={{flex: '0 0 300px'}}>
            <div style={{fontSize: 18, letterSpacing: 2.5, fontWeight: 800, color: k.kol === CZERWONY ? '#F09B90' : k.kol === ZOLTY ? '#F3D08A' : '#8FD3A6'}}>{k.tag}</div>
            <div style={{fontSize: 24, marginTop: 6, color: 'rgba(255,255,255,0.9)'}}>{k.zakres}</div>
          </div>
          <div style={{flex: 1, fontSize: 30, fontWeight: 700}}>{k.wzor}</div>
          <div style={{flex: '0 0 150px', textAlign: 'right', fontSize: 30, fontWeight: 800, color: '#F6A57E'}}>{k.out}</div>
        </Karta>
      ))}
    </div>
  </Tlo>
);

const Dlaczego: React.FC<{a: number; b: number; c: number}> = ({a, b, c}) => {
  const STENY = [
    {r: 'I', s: 6}, {r: 'II', s: 6}, {r: 'III', s: 6}, {r: 'IV', s: 7}, {r: 'V', s: 7},
    {r: 'VI', s: 3}, {r: 'VII', s: 3}, {r: 'VIII', s: 3}, {r: 'IX', s: 3},
  ];
  const frame = useCurrentFrame();
  return (
    <Tlo>
      <Naglowek kicker="Po co w ogóle przeliczamy" tytul="Punktów nie da się porównać" />
      <div style={{position: 'absolute', left: 150, right: 150, top: 230, display: 'flex', gap: 26}}>
        <Karta od={a} style={{flex: 1, textAlign: 'center', padding: '24px 20px', borderColor: '#C0392B'}}>
          <div style={{fontSize: 21, letterSpacing: 2.5, fontWeight: 800, color: '#F09B90'}}>OBSZAR I · 14 TWIERDZEŃ</div>
          <div style={{fontSize: 52, fontWeight: 800, marginTop: 8}}>42 pkt</div>
        </Karta>
        <Karta od={a + 6} style={{flex: 1, textAlign: 'center', padding: '24px 20px', borderColor: '#C0392B'}}>
          <div style={{fontSize: 21, letterSpacing: 2.5, fontWeight: 800, color: '#F09B90'}}>OBSZAR IV · 2 TWIERDZENIA</div>
          <div style={{fontSize: 52, fontWeight: 800, marginTop: 8}}>7 pkt</div>
        </Karta>
      </div>
      <Pojaw od={b} style={{position: 'absolute', left: 0, right: 0, top: 420, textAlign: 'center', fontSize: 30, fontWeight: 700, color: '#fff'}}>
        Dopiero sten kładzie wszystkie 9 obszarów na jednej skali
      </Pojaw>
      <div style={{position: 'absolute', left: 170, right: 170, top: 500, height: 300, display: 'flex', alignItems: 'flex-end', gap: 18}}>
        {STENY.map((o, i) => {
          const h = interpolate(frame, [c + i * 3, c + i * 3 + 16], [0, o.s / 10], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
          const kol = o.s >= 8 ? ZIELONY : o.s >= 5 ? ZOLTY : CZERWONY;
          return (
            <div key={o.r} style={{flex: 1, textAlign: 'center'}}>
              <div style={{fontSize: 26, fontWeight: 800, color: kol === ZOLTY ? '#F3D08A' : kol === CZERWONY ? '#F09B90' : '#8FD3A6', opacity: h > 0.02 ? 1 : 0}}>{o.s}</div>
              <div style={{height: 210 * h, background: kol, borderRadius: '8px 8px 0 0', marginTop: 6}} />
              <div style={{fontSize: 22, fontWeight: 700, color: 'rgba(255,255,255,0.8)', marginTop: 8}}>{o.r}</div>
            </div>
          );
        })}
      </div>
    </Tlo>
  );
};

const Steny: React.FC<{tyt: number; krzywa: number; pasma: number; stala: number}> = ({tyt, krzywa, pasma, stala}) => {
  const frame = useCurrentFrame();
  const p = interpolate(frame, [krzywa, krzywa + 26], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const W = 1240, H = 300;
  const y = (x: number) => H - H * 0.92 * Math.exp(-0.5 * ((x - 5.5) / 2) ** 2) / Math.exp(0);
  const pts = Array.from({length: 121}, (_, i) => {
    const s = 0.5 + (i / 120) * 10;
    return `${((s - 0.5) / 10) * W},${y(s)}`;
  }).join(' ');
  return (
    <Tlo>
      <Naglowek kicker="Sten · standard ten · standardowa dziesiątka" tytul="Skąd biorą się steny" od={tyt} />
      <div style={{position: 'absolute', left: 160, right: 160, top: 235}}>
        <svg viewBox={`0 0 ${W} ${H + 4}`} style={{width: '100%', height: 300}}>
          <defs>
            <clipPath id="lclip"><rect x="0" y="0" width={W * p} height={H + 4} /></clipPath>
          </defs>
          <g clipPath="url(#lclip)">
            {Array.from({length: 10}, (_, i) => {
              const s = i + 1;
              const kol = s >= 8 ? ZIELONY : s >= 5 ? ZOLTY : CZERWONY;
              const op = interpolate(frame, [pasma + i * 2, pasma + i * 2 + 10], [0, 0.55], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
              return <rect key={s} x={((s - 0.5) / 10) * W} y={0} width={W / 10} height={H} fill={kol} opacity={op} />;
            })}
            <polyline points={pts} fill="none" stroke="#fff" strokeWidth={4} />
          </g>
          <line x1={0} y1={H} x2={W} y2={H} stroke="rgba(255,255,255,0.5)" strokeWidth={2} />
        </svg>
        <div style={{position: 'relative', height: 44, marginTop: 4}}>
          {Array.from({length: 10}, (_, i) => (
            <div key={i} style={{position: 'absolute', left: `${((i + 0.5) / 10) * 100}%`, transform: 'translateX(-50%)', fontSize: 26, fontWeight: 800, color: 'rgba(255,255,255,0.9)'}}>{i + 1}</div>
          ))}
        </div>
      </div>
      <div style={{position: 'absolute', left: 160, right: 160, top: 660, display: 'flex', gap: 22}}>
        <Karta od={pasma} style={{flex: 1, textAlign: 'center', padding: '20px 18px'}}>
          <div style={{fontSize: 46, fontWeight: 800, color: '#F6A57E'}}>5,5</div>
          <div style={{fontSize: 24, marginTop: 6}}>średnia skali</div>
        </Karta>
        <Karta od={pasma + 6} style={{flex: 1, textAlign: 'center', padding: '20px 18px'}}>
          <div style={{fontSize: 46, fontWeight: 800, color: '#F6A57E'}}>2</div>
          <div style={{fontSize: 24, marginTop: 6}}>odchylenie standardowe</div>
        </Karta>
        <Karta od={stala} akcent style={{flex: 2, textAlign: 'center', padding: '20px 18px'}}>
          <div style={{fontSize: 40, fontWeight: 800}}>0,68 = 68% populacji</div>
          <div style={{fontSize: 23, marginTop: 6}}>w granicach jednego odchylenia od średniej — granica wyniku przeciętnego</div>
        </Karta>
      </div>
    </Tlo>
  );
};

const SurowyVsSten: React.FC<{a: number; b: number}> = ({a, b}) => (
  <Tlo>
    <Naglowek kicker="Dwa różne pytania" tytul="Wynik surowy a sten" />
    <div style={{position: 'absolute', left: 140, right: 140, top: 260, display: 'flex', gap: 26}}>
      <Karta od={a} style={{flex: 1, padding: '34px 28px', textAlign: 'center'}}>
        <div style={{fontSize: 22, letterSpacing: 3, fontWeight: 800, color: '#F6A57E'}}>WYNIK SUROWY</div>
        <div style={{fontSize: 34, fontWeight: 700, marginTop: 16, lineHeight: 1.3}}>Ile punktów<br />uczeń zebrał</div>
      </Karta>
      <Karta od={a + 8} akcent style={{flex: 1, padding: '34px 28px', textAlign: 'center'}}>
        <div style={{fontSize: 22, letterSpacing: 3, fontWeight: 800, color: 'rgba(255,255,255,0.85)'}}>STEN</div>
        <div style={{fontSize: 34, fontWeight: 700, marginTop: 16, lineHeight: 1.3}}>Gdzie ten wynik leży<br />na skali funkcjonowania</div>
      </Karta>
    </div>
    <div style={{position: 'absolute', left: 140, right: 140, top: 600, display: 'flex', gap: 20}}>
      {[
        {kol: CZERWONY, s: '1 · 2 · 3 · 4', t: 'wynik niski'},
        {kol: ZOLTY, s: '5 · 6 · 7', t: 'przeciętny'},
        {kol: ZIELONY, s: '8 · 9 · 10', t: 'wysoki'},
      ].map((k, i) => (
        <Karta key={k.t} od={b + i * 7} style={{flex: 1, textAlign: 'center', padding: '24px 18px', borderColor: k.kol, background: 'rgba(255,255,255,0.07)'}}>
          <div style={{fontSize: 40, fontWeight: 800, color: k.kol === CZERWONY ? '#F09B90' : k.kol === ZOLTY ? '#F3D08A' : '#8FD3A6'}}>{k.s}</div>
          <div style={{fontSize: 27, marginTop: 8}}>{k.t}</div>
        </Karta>
      ))}
    </div>
  </Tlo>
);

const Poziomy: React.FC<{tyt: number; a: number; b: number; c: number}> = ({tyt, a, b, c}) => (
  <Tlo>
    <Naglowek kicker="Co oznacza kwalifikacja do poziomu wsparcia" tytul="Kto, kiedy i w jakiej formie" od={tyt} />
    <div style={{position: 'absolute', left: 100, right: 100, top: 245, display: 'flex', flexDirection: 'column', gap: 20}}>
      {[
        {od: a, kol: ZIELONY, jasny: '#8FD3A6', n: 'POZIOM I', st: 'sten 8–10', t: 'Wsparcie w bieżącej pracy nauczyciela: dostosowanie metod, form pracy i wymagań, indywidualizacja. Bez dodatkowych zajęć.'},
        {od: b, kol: ZOLTY, jasny: '#F3D08A', n: 'POZIOM II', st: 'sten 5–7', t: 'Wsparcie dodatkowe — formy pomocy psychologiczno-pedagogicznej: korekcyjno-kompensacyjne, logopedyczne, TUS, dydaktyczno-wyrównawcze.'},
        {od: c, kol: CZERWONY, jasny: '#F09B90', n: 'POZIOM III', st: 'sten 1–4', t: 'Wsparcie specjalistyczne: obserwacja pogłębiona, WOPFU i IPET dla ucznia z orzeczeniem, zajęcia rewalidacyjne, kontakt z poradnią PP.'},
      ].map((k) => (
        <Karta key={k.n} od={k.od} style={{padding: '22px 28px', borderColor: k.kol, background: 'rgba(255,255,255,0.07)', display: 'flex', alignItems: 'center', gap: 26}}>
          <div style={{flex: '0 0 250px'}}>
            <div style={{fontSize: 36, fontWeight: 800, color: k.jasny}}>{k.n}</div>
            <div style={{fontSize: 25, color: 'rgba(255,255,255,0.85)', marginTop: 4}}>{k.st}</div>
          </div>
          <div style={{flex: 1, fontSize: 26, lineHeight: 1.35}}>{k.t}</div>
        </Karta>
      ))}
    </div>
  </Tlo>
);

const Ostrzezenia: React.FC<{tyt: number; a: number; b: number; c: number}> = ({tyt, a, b, c}) => (
  <Tlo>
    <Naglowek kicker="Trzy ostrzeżenia na koniec" tytul="Czego liczby nie powiedzą" od={tyt} />
    <div style={{position: 'absolute', left: 110, right: 110, top: 245, display: 'flex', flexDirection: 'column', gap: 20}}>
      {[
        {od: a, n: '1', tt: 'Średnia maskuje pojedyncze oceny', t: <>Reguła nadrzędna: każde pojedyncze twierdzenie ocenione na <b style={{color: '#F6A57E'}}>1 lub 2</b> podlega analizie zespołu — niezależnie od średniej i od stena.</>},
        {od: b, n: '2', tt: 'Arkusz niepełny', t: <>Im więcej pozycji pustych, tym mniej pewny sten. Przy dużej liczbie braków odczytujemy <b style={{color: '#F6A57E'}}>sam profil obszarowy</b> i zaznaczamy to w druku.</>},
        {od: c, n: '3', tt: 'Każdy ocenia niezależnie', t: <>Nauczyciel, rodzic i specjalista wypełniają cały arkusz osobno. <b style={{color: '#F6A57E'}}>Wynik uzgodniony ustala zespół</b> — i to on trafia do dokumentacji.</>},
      ].map((k) => (
        <Karta key={k.n} od={k.od} style={{padding: '22px 28px', display: 'flex', alignItems: 'center', gap: 26}}>
          <Kolo n={k.n} rozmiar={62} kolor={MARKA.pomarancz} />
          <div style={{flex: 1}}>
            <div style={{fontSize: 31, fontWeight: 800}}>{k.tt}</div>
            <div style={{fontSize: 25, lineHeight: 1.35, marginTop: 8, color: 'rgba(255,255,255,0.92)'}}>{k.t}</div>
          </div>
        </Karta>
      ))}
    </div>
  </Tlo>
);

const Straznik: React.FC<{od: number[]}> = ({od}) => (
  <Tlo>
    <Pojaw od={od[0]} style={{position: 'absolute', left: 110, right: 110, top: 58, textAlign: 'center'}}>
      <div style={{fontSize: 19, letterSpacing: 4, color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase'}}>Weryfikacja źródeł i publikatorów</div>
      <div style={{fontSize: 56, fontWeight: 800, color: '#fff', marginTop: 8}}>Strażnik prawa</div>
    </Pojaw>
    <div style={{position: 'absolute', left: 110, right: 110, top: 205, display: 'flex', flexDirection: 'column', gap: 15}}>
      {[
        {i: 1, z: 'Narzędzie KSzOF', a: 'Z. Gajdzica, E. Widawska, S. Byra, E. Domagała-Zyśk, B. Jachimczak, R. Piotrowicz, E. Neroj', p: 'Katowice–Kraków 2024 · model oceny funkcjonalnej dla edukacji włączającej'},
        {i: 2, z: 'Skala stenowa', a: 'standardowe narzędzie psychometryczne', p: 'średnia 5,5 · odchylenie standardowe 2'},
        {i: 3, z: 'Rozpoznawanie potrzeb ucznia', a: 'rozp. MEN o pomocy psychologiczno-pedagogicznej', p: 't.j. Dz.U. 2023 poz. 1798'},
        {i: 4, z: 'WOPFU i IPET (uczeń z orzeczeniem)', a: 'rozp. MEN o kształceniu specjalnym, § 6', p: 't.j. Dz.U. 2020 poz. 1309'},
      ].map((r) => (
        <Karta key={r.i} od={od[r.i]} style={{padding: '17px 26px', display: 'flex', alignItems: 'center', gap: 22}}>
          <div style={{flex: '0 0 330px', fontSize: 25, fontWeight: 800, color: '#F6A57E'}}>{r.z}</div>
          <div style={{flex: 1, fontSize: 22, lineHeight: 1.3, color: 'rgba(255,255,255,0.92)'}}>{r.a}</div>
          <div style={{flex: '0 0 330px', textAlign: 'right', fontSize: 22, fontWeight: 700}}>{r.p}</div>
        </Karta>
      ))}
    </div>
    <Karta od={od[5]} akcent style={{position: 'absolute', left: 110, right: 110, top: 660, padding: '24px 30px', fontSize: 26, lineHeight: 1.4}}>
      <b>Uwaga ważna.</b> Wzór przeliczania punktów na steny i progi poziomów wsparcia <b>nie wynikają z przepisu</b> — pochodzą z narzędzia. Przepis wymaga rozpoznania potrzeb i udzielenia pomocy, a sposób liczenia wpisujemy do procedury szkoły, żeby wynik nie zależał od tego, kto danego dnia liczy.
    </Karta>
  </Tlo>
);

const Final: React.FC<{kroki: number; logo: number; haslo: number}> = ({kroki, logo, haslo}) => (
  <Tlo>
    <div style={{position: 'absolute', left: 90, right: 90, top: 200, display: 'flex', gap: 14}}>
      {['Suma', 'Średnia', 'Pozycja', 'Sten', 'Poziom'].map((t, i) => (
        <Karta key={t} od={kroki + i * 5} akcent={i === 4} style={{flex: 1, textAlign: 'center', padding: '28px 12px'}}>
          <div style={{fontSize: 22, fontWeight: 800, color: i === 4 ? 'rgba(255,255,255,0.85)' : '#F6A57E'}}>KROK {i + 1}</div>
          <div style={{fontSize: 32, fontWeight: 800, marginTop: 10}}>{t}</div>
        </Karta>
      ))}
    </div>
    <Pojaw od={kroki + 28} style={{position: 'absolute', left: 0, right: 0, top: 420, textAlign: 'center', fontSize: 40, fontWeight: 800, color: '#fff'}}>
      Pięć kroków, jedna kartka
    </Pojaw>
    <Pojaw od={logo} style={{position: 'absolute', left: 0, right: 0, top: 540, display: 'flex', justifyContent: 'center'}}>
      <Logo rozmiar={92} />
    </Pojaw>
    <Pojaw od={logo + 8} style={{position: 'absolute', left: 0, right: 0, top: 665, textAlign: 'center', fontSize: 46, fontWeight: 800, color: '#fff'}}>EduPlaner 2026</Pojaw>
    <Pojaw od={haslo} style={{position: 'absolute', left: 0, right: 0, top: 740, textAlign: 'center', fontSize: 34, color: '#F6A57E', fontWeight: 700}}>
      Mniej dokumentów. Więcej edukacji.
    </Pojaw>
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
  '.druk-oryginalny .rc{border:1.5px solid #b3a6dd!important;font-weight:700!important}',
  '.druk-oryginalny .rc.on{border-color:#E8450A!important}',
  '.druk-oryginalny .arsum{font-weight:800!important}',
  '.druk-oryginalny .ar-sum{font-size:12.5px!important}',
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

/** Zaznaczenia ocen z druku autorki — druk resetuje się co klatkę, więc każda scena klika je od nowa. */
const oceny = (filtr: (o: Ocena) => boolean, start: number, krok = 0): Krok[] =>
  OCENY.filter(filtr).map((o, i): Krok => ({sek: start + i * krok, typ: 'klik', selektor: `@${o.a} .rc #${o.i}`}));
const WSZYSTKIE = (start = 0): Krok[] => oceny(() => true, start, 0);

export const LiczeniePromo: React.FC<Props> = ({film}) => {
  const {fps} = useVideoConfig();
  const n = film.napisy;
  const z = (i: number) => n[i]?.odSek ?? i * 5;
  const kz = (i: number) => n[i]?.doSek ?? i * 5 + 4;
  const granica = (i: number) => (i <= 0 ? 0 : (kz(i - 1) + z(i)) / 2);
  const fr = (sek: number) => Math.round(sek * fps);
  const L = (od: number) => (s: number) => Math.max(0, fr(s - od));
  const koniec = film.dlugosc;

  /* --- legenda ocen 1–5 (strona 5), zdania 9–15 --- */
  const legKroki: Krok[] = [
    ...Array.from({length: 5}, (_, i): Krok => ({sek: z(10 + i) - 0.2, doSek: kz(10 + i) + 0.3, typ: 'wyroznij', selektor: `@5 tbody tr #${i}`})),
    {sek: z(15) - 0.2, doSek: kz(15) + 0.4, typ: 'wyroznij', selektor: '@5 .sec #0'},
  ];
  const legKamera: Ujecie[] = [
    U(0, '@5 .sec #0', 2.1, 22),
    U(z(10) - 0.6, '@5 table.tbl #0', 2.2, 22),
    Uc(z(12) - 0.4, '@5 table.tbl #0', 2.2, 300),
    Uc(z(14) - 0.4, '@5 table.tbl #0', 2.2, 470),
  ];

  /* --- krok 1: suma obszaru I (strona 2), zdania 21–28 --- */
  const OB1 = OCENY.filter((o) => o.ob === 'I');
  const tik = (z(26) + 1.2 - z(25)) / OB1.length;
  const sumaKroki: Krok[] = [
    ...OB1.map((o, i): Krok => ({sek: z(25) + 0.4 + i * tik, typ: 'klik', selektor: `@${o.a} .rc #${o.i}`})),
    ...OB1.map((o, i): Krok => ({sek: z(25) + 0.4 + i * tik - 0.1, doSek: z(25) + 0.4 + (i + 1) * tik, typ: 'wyroznij', selektor: `@2 tr.arow #${i}`})),
    {sek: z(23) - 0.2, doSek: kz(24) + 0.3, typ: 'wyroznij', selektor: '@2 tr.cmprow #0'},
    {sek: z(27) - 0.2, doSek: kz(28) + 0.5, typ: 'wyroznij', selektor: '@2 .arsum #0'},
  ];
  const sumaKamera: Ujecie[] = [
    U(0, '@2 .sec #0', 2.1, 22),
    U(z(23) - 0.5, '@2 table.tbl #0', 2.2, 22),
    Uc(z(25) + 0.2, '@2 table.tbl #0', 2.2, 245, 1.0),
    Uc(z(25) + 4.0, '@2 table.tbl #0', 2.2, 400, 3.4),
    U(z(27) - 0.4, '@2 tr.cmprow #0', 2.4, 40),
  ];

  /* --- krok 5: tabela poziomów (strona 8), zdania 70–75 --- */
  const poziomKroki: Krok[] = [
    ...WSZYSTKIE(),
    ...[0, 1, 2].map((i): Krok => ({sek: z(72 + i) - 0.2, doSek: kz(72 + i) + 0.3, typ: 'wyroznij', selektor: `@8 .band #${i}`})),
  ];
  const poziomKamera: Ujecie[] = [U(0, '@8 .sec #0', 2.15, 22), U(z(72) - 0.6, '@8 .band #0', 2.3, 90)];

  /* --- obszar VI (strona 3), zdania 82–85 --- */
  const OB6 = OCENY.filter((o) => o.ob === 'VI');
  const vi = OCENY.findIndex((o) => o.ob === 'VI');
  const viKroki: Krok[] = [
    ...OB6.map((o, i): Krok => ({sek: z(84) + 0.5 + i * 0.9, typ: 'klik', selektor: `@${o.a} .rc #${o.i}`})),
    {sek: z(83) - 0.2, doSek: kz(83) + 0.4, typ: 'wyroznij', selektor: '@3 tr.cmprow #3'},
    {sek: z(85) - 0.2, doSek: kz(85) + 0.5, typ: 'wyroznij', selektor: '@3 .arsum #3'},
  ];
  const viKamera: Ujecie[] = [U(0, '@3 tr.cmprow #3', 2.4, 60), U(z(85) - 0.4, '@3 tr.cmprow #3', 2.55, 40)];

  /* --- obszar IV (strona 3), zdania 91–93 --- */
  const OB4 = OCENY.filter((o) => o.ob === 'IV');
  const ivKroki: Krok[] = [
    ...OB4.map((o, i): Krok => ({sek: z(92) + 0.5 + i * 1.1, typ: 'klik', selektor: `@${o.a} .rc #${o.i}`})),
    {sek: z(91) - 0.2, doSek: kz(91) + 0.4, typ: 'wyroznij', selektor: '@3 tr.cmprow #1'},
    {sek: z(93) - 0.2, doSek: kz(93) + 0.5, typ: 'wyroznij', selektor: '@3 .arsum #1'},
  ];
  const ivKamera: Ujecie[] = [U(0, '@3 tr.cmprow #1', 2.4, 60), U(z(93) - 0.4, '@3 tr.cmprow #1', 2.55, 40)];

  /* --- wynik ogólny (strona 8), zdania 104–106 --- */
  const ogolKroki: Krok[] = [...WSZYSTKIE(), {sek: z(106) - 0.2, doSek: kz(106) + 0.5, typ: 'wyroznij', selektor: '@8 .k-ogol #0'}];
  const ogolKamera: Ujecie[] = [U(0, '@8 .sec #0', 2.15, 22), U(z(106) - 0.5, '@8 .k-ogol #0', 2.5, 60)];

  /* --- tabela norm (strona 8), zdania 113–119 --- */
  const tabKroki: Krok[] = [
    ...WSZYSTKIE(),
    ...[0, 1, 2].map((i): Krok => ({sek: z(114 + i) - 0.2, doSek: kz(114 + i) + 0.3, typ: 'wyroznij', selektor: `@8 .band #${i}`})),
    {sek: z(117) - 0.2, doSek: kz(118) + 0.4, typ: 'wyroznij', selektor: '@8 .band #1'},
  ];
  const tabKamera: Ujecie[] = [U(0, '@8 table.tbl #0', 2.2, 22), U(z(114) - 0.6, '@8 .band #0', 2.3, 90)];

  /* --- profil obszarowy (strona 7), zdania 139–142 --- */
  const profKroki: Krok[] = [...WSZYSTKIE(), {sek: z(140) - 0.2, doSek: kz(141) + 0.4, typ: 'wyroznij', selektor: '@7 table.tbl #0'}];
  const profKamera: Ujecie[] = [U(0, '@7 .sec #0', 2.0, 22), U(z(140) - 0.6, '@7 table.tbl #0', 2.15, 30)];

  type Scena = {id: string; od: number; do: number; el: (od: number) => React.ReactNode};
  const sceny: Scena[] = [
    {id: 'intro', od: 0, do: granica(2), el: () => <Intro />},
    {id: 'pytania', od: granica(2), do: granica(6), el: (o) => <Pytania a={L(o)(z(3))} b={L(o)(z(4))} c={L(o)(z(5))} />},
    {id: 'coliczymy', od: granica(6), do: granica(9), el: (o) => <CoLiczymy a={L(o)(z(7))} b={L(o)(z(8))} />},
    {id: 'legenda', od: granica(9), do: granica(16), el: (o) => <OryginalnyDruk plik="kszof.html" kroki={legKroki} kamera={legKamera} odSek={o} css={CSS_FILMU} />},
    {id: 'dwawyniki', od: granica(16), do: granica(21), el: (o) => <DwaWyniki a={L(o)(z(17))} b={L(o)(z(18))} c={L(o)(z(19))} />},
    {id: 'suma', od: granica(21), do: granica(29), el: (o) => <OryginalnyDruk plik="kszof.html" kroki={sumaKroki} kamera={sumaKamera} odSek={o} css={CSS_FILMU} />},
    {
      id: 'srednia',
      od: granica(29),
      do: granica(37),
      el: (o) => (
        <Tlo>
          <Naglowek kicker="Krok 2 · wzór na średnią" tytul="Suma ÷ liczba ocenionych twierdzeń" />
          <Rachunek
            wiersze={[
              {od: L(o)(z(31)), t: <>średnia = suma punktów ÷ liczba ocenionych twierdzeń</>},
              {od: L(o)(z(32)), t: <>42 ÷ 14 = <b style={{color: '#F6A57E'}}>3,00</b></>},
              {od: L(o)(z(33)), t: <>Średnia w obszarze I wynosi 3,00</>, wynik: true},
              {od: L(o)(z(34)), t: <>Średnią wyrażamy w tej samej skali 1–5, w której oceniamy</>, male: true},
              {od: L(o)(z(35)), t: <>Średnia 3 = ocena 3: umiarkowany stopień, z częściowym wsparciem</>, male: true},
            ]}
          />
          <SkalaSrednich od={L(o)(z(33))} srednia={3} podpis="czytelna informacja jeszcze zanim policzymy stena" />
        </Tlo>
      ),
    },
    {
      id: 'puste',
      od: granica(37),
      do: granica(42),
      el: (o) => (
        <Tlo>
          <Naglowek kicker="Uwaga na pozycje puste" tytul="Czego nie wliczamy" />
          <div style={{position: 'absolute', left: 150, right: 150, top: 250}}>
            <Karta od={L(o)(z(38))} style={{padding: '30px 30px', fontSize: 30, lineHeight: 1.4, textAlign: 'center'}}>
              Nie mieliśmy możliwości zaobserwować zachowania? <b style={{color: '#F6A57E'}}>Zostawiamy pozycję pustą</b> — to pełnoprawna, uczciwa odpowiedź.
            </Karta>
          </div>
          <div style={{position: 'absolute', left: 150, right: 150, top: 470, display: 'flex', gap: 24}}>
            <Karta od={L(o)(z(39))} style={{flex: 1, textAlign: 'center', padding: '30px 22px', fontSize: 27, lineHeight: 1.35}}>
              Nie wliczamy jej <b style={{color: '#F6A57E'}}>ani do sumy</b>
            </Karta>
            <Karta od={L(o)(z(39)) + 8} style={{flex: 1, textAlign: 'center', padding: '30px 22px', fontSize: 27, lineHeight: 1.35}}>
              ani do <b style={{color: '#F6A57E'}}>liczby twierdzeń</b>, przez którą dzielimy
            </Karta>
          </div>
          <Karta od={L(o)(z(41))} akcent style={{position: 'absolute', left: 180, right: 180, top: 660, textAlign: 'center', fontSize: 32, fontWeight: 700, padding: '28px 26px', lineHeight: 1.35}}>
            Dzielimy zawsze przez liczbę twierdzeń <b>faktycznie ocenionych</b>
          </Karta>
        </Tlo>
      ),
    },
    {
      id: 'pozycja',
      od: granica(42),
      do: granica(51),
      el: (o) => (
        <Tlo>
          <Naglowek kicker="Krok 3 · pozycja na skali" tytul="Najniższy wynik to nie zero" />
          <Rachunek
            wiersze={[
              {od: L(o)(z(45)), t: <>Uczeń z samymi jedynkami ma tyle punktów, ile jest twierdzeń</>, male: true},
              {od: L(o)(z(47)), t: <>Droga od średniej 1 do średniej 5 jest długa na 4 jednostki</>, male: true},
              {od: L(o)(z(48)), t: <>pozycja = (średnia − 1) ÷ 4</>, wynik: true},
              {od: L(o)(z(49)), t: <>(3 − 1) ÷ 4 = 2 ÷ 4 = 0,50</>},
            ]}
            style={{top: 235}}
          />
          <SkalaSrednich od={L(o)(z(49))} srednia={3} podpis="połowa drogi od minimum do maksimum" />
        </Tlo>
      ),
    },
    {id: 'przedzialy', od: granica(51), do: granica(62), el: (o) => <Przedzialy tyt={L(o)(z(51))} a={L(o)(z(53))} b={L(o)(z(56))} c={L(o)(z(59))} />},
    {
      id: 'podstawienie',
      od: granica(62),
      do: granica(70),
      el: (o) => (
        <Tlo>
          <Naglowek kicker="Obszar I · podstawiamy do wzoru" tytul="Pozycja 0,50 → przedział przeciętny" />
          <Rachunek
            wiersze={[
              {od: L(o)(z(64)), t: <>0,50 − 0,31 = 0,19</>},
              {od: L(o)(z(65)), t: <>0,19 ÷ 0,37 = 0,51</>},
              {od: L(o)(z(66)), t: <>0,51 × 2 = 1,02</>},
              {od: L(o)(z(67)), t: <>1,02 + 5 = 6,02</>},
              {od: L(o)(z(69)), t: <>Obszar I to sten 6</>, wynik: true},
            ]}
            style={{top: 250}}
          />
        </Tlo>
      ),
    },
    {id: 'poziomtab', od: granica(70), do: granica(76), el: (o) => <OryginalnyDruk plik="kszof.html" kroki={poziomKroki} kamera={poziomKamera} odSek={o} css={CSS_FILMU} />},
    {
      id: 'skrot',
      od: granica(76),
      do: granica(82),
      el: (o) => (
        <Tlo>
          <Naglowek kicker="Najkrótsza droga — dla liczących na zebraniu zespołu" tytul="Progi wprost w średniej" />
          <div style={{position: 'absolute', left: 130, right: 130, top: 230, display: 'flex', gap: 22}}>
            {[
              {od: L(o)(z(78)), kol: CZERWONY, jasny: '#F09B90', z: 'średnia < 2,23', p: 'Poziom III'},
              {od: L(o)(z(79)), kol: ZOLTY, jasny: '#F3D08A', z: '2,23 – 3,73', p: 'Poziom II'},
              {od: L(o)(z(80)), kol: ZIELONY, jasny: '#8FD3A6', z: 'średnia ≥ 3,73', p: 'Poziom I'},
            ].map((k) => (
              <Karta key={k.p} od={k.od} style={{flex: 1, textAlign: 'center', padding: '30px 18px', borderColor: k.kol, background: 'rgba(255,255,255,0.07)'}}>
                <div style={{fontSize: 38, fontWeight: 800, color: k.jasny}}>{k.z}</div>
                <div style={{fontSize: 32, fontWeight: 700, marginTop: 12}}>{k.p}</div>
              </Karta>
            ))}
          </div>
          <SkalaSrednich od={L(o)(z(78))} progi podpis="jedno spojrzenie na średnią — i poziom wsparcia gotowy" />
        </Tlo>
      ),
    },
    {id: 'druk-vi', od: granica(82), do: granica(86), el: (o) => <OryginalnyDruk plik="kszof.html" kroki={viKroki} kamera={viKamera} odSek={o} css={CSS_FILMU} />},
    {
      id: 'kalk-vi',
      od: granica(86),
      do: granica(91),
      el: (o) => (
        <Tlo>
          <Naglowek kicker="Obszar VI · życie domowe · 2 twierdzenia" tytul="Suma 4 z 10" />
          <Rachunek
            wiersze={[
              {od: L(o)(z(86)), t: <>średnia = 4 ÷ 2 = <b style={{color: '#F6A57E'}}>2,00</b></>},
              {od: L(o)(z(87)), t: <>2,00 &lt; 2,23 → przedział niski</>},
              {od: L(o)(z(88)), t: <>pozycja = (2 − 1) ÷ 4 = 0,25</>},
              {od: L(o)(z(89)), t: <>0,25 ÷ 0,31 = 0,80 · × 3 = 2,40 · + 1 = 3,40</>},
              {od: L(o)(z(90)), t: <>sten 3 · Poziom III — wsparcie specjalistyczne</>, wynik: true},
            ]}
            style={{top: 250}}
          />
        </Tlo>
      ),
    },
    {id: 'druk-iv', od: granica(91), do: granica(94), el: (o) => <OryginalnyDruk plik="kszof.html" kroki={ivKroki} kamera={ivKamera} odSek={o} css={CSS_FILMU} />},
    {
      id: 'kalk-iv',
      od: granica(94),
      do: granica(99),
      el: (o) => (
        <Tlo>
          <Naglowek kicker="Obszar IV · motoryka · 2 twierdzenia" tytul="Suma 7 z 10" />
          <Rachunek
            wiersze={[
              {od: L(o)(z(94)), t: <>średnia = 7 ÷ 2 = <b style={{color: '#F6A57E'}}>3,50</b></>},
              {od: L(o)(z(95)), t: <>2,23 ≤ 3,50 &lt; 3,73 → przedział przeciętny</>},
              {od: L(o)(z(96)), t: <>pozycja = (3,50 − 1) ÷ 4 = 0,63</>},
              {od: L(o)(z(97)), t: <>0,63 − 0,31 = 0,32 · ÷ 0,37 = 0,86 · × 2 = 1,73 · + 5 = 6,73</>, male: true},
              {od: L(o)(z(98)), t: <>sten 7 · Poziom II</>, wynik: true},
            ]}
            style={{top: 250}}
          />
        </Tlo>
      ),
    },
    {id: 'dlaczego', od: granica(99), do: granica(104), el: (o) => <Dlaczego a={L(o)(z(100))} b={L(o)(z(102))} c={L(o)(z(102)) + 14} />},
    {id: 'druk-ogol', od: granica(104), do: granica(107), el: (o) => <OryginalnyDruk plik="kszof.html" kroki={ogolKroki} kamera={ogolKamera} odSek={o} css={CSS_FILMU} />},
    {
      id: 'kalk-ogol',
      od: granica(107),
      do: granica(113),
      el: (o) => (
        <Tlo>
          <Naglowek kicker="Wynik ogólny · 52 twierdzenia" tytul="141 z 260 punktów" />
          <Rachunek
            wiersze={[
              {od: L(o)(z(108)), t: <>średnia = 141 ÷ 52 = <b style={{color: '#F6A57E'}}>2,71</b></>},
              {od: L(o)(z(109)), t: <>2,23 ≤ 2,71 &lt; 3,73 → przedział przeciętny</>},
              {od: L(o)(z(110)), t: <>pozycja = (2,71 − 1) ÷ 4 = 0,43</>},
              {od: L(o)(z(111)), t: <>0,43 − 0,31 = 0,12 · ÷ 0,37 = 0,32 · × 2 = 0,64 · + 5 = 5,64</>, male: true},
              {od: L(o)(z(112)), t: <>sten 6 · Poziom II</>, wynik: true},
            ]}
            style={{top: 250}}
          />
        </Tlo>
      ),
    },
    {id: 'druk-tabela', od: granica(113), do: granica(120), el: (o) => <OryginalnyDruk plik="kszof.html" kroki={tabKroki} kamera={tabKamera} odSek={o} css={CSS_FILMU} />},
    {id: 'steny', od: granica(120), do: granica(128), el: (o) => <Steny tyt={L(o)(z(120))} krzywa={L(o)(z(122))} pasma={L(o)(z(124))} stala={L(o)(z(125))} />},
    {id: 'surowy', od: granica(128), do: granica(133), el: (o) => <SurowyVsSten a={L(o)(z(128))} b={L(o)(z(130))} />},
    {id: 'poziomy', od: granica(133), do: granica(139), el: (o) => <Poziomy tyt={L(o)(z(133))} a={L(o)(z(135))} b={L(o)(z(137))} c={L(o)(z(138))} />},
    {id: 'druk-profil', od: granica(139), do: granica(143), el: (o) => <OryginalnyDruk plik="kszof.html" kroki={profKroki} kamera={profKamera} odSek={o} css={CSS_FILMU} wykresyOdSek={z(139)} />},
    {id: 'ostrzezenia', od: granica(143), do: granica(154), el: (o) => <Ostrzezenia tyt={L(o)(z(143))} a={L(o)(z(144))} b={L(o)(z(148))} c={L(o)(z(151))} />},
    {id: 'straznik', od: granica(154), do: granica(161), el: (o) => <Straznik od={[155, 155, 156, 157, 158, 159].map((i) => L(o)(z(i)))} />},
    {id: 'final', od: granica(161), do: koniec, el: (o) => <Final kroki={L(o)(z(161))} logo={L(o)(z(163))} haslo={L(o)(z(164))} />},
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
