import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {MARKA, FONT} from '../marka';
import {Logo, Pojaw, useWejscie} from '../ui';
import type {Z} from '../typy';

const Slowo: React.FC<{tekst: string; od: number}> = ({tekst, od}) => {
  const w = useWejscie(od, {damping: 10, stiffness: 170});
  return (
    <span style={{display: 'inline-block', opacity: w, transform: `translateY(${(1 - w) * 30}px) scale(${0.7 + 0.3 * w})`, marginRight: 34}}>{tekst}</span>
  );
};

const Krok: React.FC<{tekst: string; od: number; ostatni?: boolean; akcent?: boolean}> = ({tekst, od, ostatni, akcent}) => {
  const w = useWejscie(od, {damping: 12, stiffness: 120});
  return (
    <div style={{display: 'flex', alignItems: 'center'}}>
      <div
        style={{
          opacity: w,
          transform: `scale(${0.6 + 0.4 * w})`,
          background: akcent ? MARKA.pomarancz : 'rgba(255,255,255,0.12)',
          border: `2px solid ${akcent ? MARKA.pomarancz : 'rgba(255,255,255,0.45)'}`,
          color: '#fff',
          fontWeight: 700,
          fontSize: 26,
          padding: '14px 28px',
          borderRadius: 999,
          fontFamily: FONT,
          whiteSpace: 'nowrap',
        }}
      >
        {tekst}
      </div>
      {!ostatni ? <div style={{width: 46, height: 3, background: 'rgba(255,255,255,0.45)', transform: `scaleX(${w})`, transformOrigin: 'left', margin: '0 4px'}} /> : null}
    </div>
  );
};

const PRAWO = [
  {tytul: 'Ustawa Prawo oświatowe', opis: 'z 14 grudnia 2016 r. — kształcenie specjalne i pomoc psychologiczno-pedagogiczna'},
  {tytul: 'Rozporządzenie MEN z 9 sierpnia 2017 r.', opis: 'w sprawie warunków organizowania kształcenia specjalnego — § 6 ust. 8 i 11, § 7 ust. 2'},
  {tytul: 'Rozporządzenie MEN z 9 sierpnia 2017 r.', opis: 'w sprawie zasad organizacji i udzielania pomocy psychologiczno-pedagogicznej'},
  {tytul: 'RODO', opis: 'rozporządzenie (UE) 2016/679 — zgody i ochrona danych dziecka'},
];

/** Finał: ścieżka dziecka → hasła → nazwa → podstawa prawna. Momenty z nagrania (znaczniki). */
export const Final: React.FC<{z: Z}> = ({z}) => {
  const frame = useCurrentFrame();
  const hasla = z.hasla ?? 80;
  const czas = z.czas ?? hasla + 60;
  const nazwa = z.nazwa ?? czas + 90;
  const prawo = z.prawo ?? nazwa + 120;
  const faza2 = interpolate(frame, [nazwa - 8, nazwa + 10], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const glow = 0.35 + 0.15 * Math.sin(frame / 12);
  return (
    <AbsoluteFill style={{background: `linear-gradient(160deg, ${MARKA.fioletCiemny} 0%, ${MARKA.fiolet} 55%, #3b2a86 100%)`, fontFamily: FONT}}>
      <div style={{position: 'absolute', left: 460, top: -100, width: 1000, height: 900, borderRadius: '50%', background: `radial-gradient(circle, rgba(232,69,10,${glow}) 0%, rgba(232,69,10,0) 60%)`}} />

      {/* Faza 1: ścieżka + hasła */}
      <div style={{position: 'absolute', left: 0, right: 0, top: 0, bottom: 0, opacity: 1 - faza2, transform: `translateY(${-faza2 * 60}px)`}}>
        <Pojaw od={0} style={{textAlign: 'center', marginTop: 190}}>
          <div style={{fontSize: 22, letterSpacing: 4, color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase'}}>Od zgłoszenia po podsumowanie</div>
        </Pojaw>
        <div style={{display: 'flex', justifyContent: 'center', marginTop: 34}}>
          <Krok tekst="Metryczka" od={6} akcent />
          <Krok tekst="WOPFU" od={14} />
          <Krok tekst="IPET / PEWS" od={22} />
          <Krok tekst="Realizacja" od={30} />
          <Krok tekst="Ewaluacja" od={38} ostatni />
        </div>
        <div style={{textAlign: 'center', marginTop: 120, fontSize: 96, fontWeight: 800, color: '#fff', letterSpacing: -1}}>
          <Slowo tekst="Szybciej." od={hasla} />
          <Slowo tekst="Spokojniej." od={hasla + 16} />
          <Slowo tekst="Pewniej." od={hasla + 32} />
        </div>
        <Pojaw od={czas} style={{textAlign: 'center', marginTop: 30}}>
          <div style={{fontSize: 34, color: '#F6A57E', fontWeight: 700}}>A w zamian dostajesz czas — dla dziecka i dla siebie.</div>
        </Pojaw>
      </div>

      {/* Faza 2: nazwa, hasło, CTA, kontakt */}
      <div style={{position: 'absolute', left: 0, right: 0, top: 0, bottom: 0, opacity: faza2, transform: `translateY(${(1 - faza2) * 60}px)`}}>
        <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', marginTop: 130}}>
          <Logo rozmiar={130} />
          <div style={{fontSize: 92, fontWeight: 800, color: '#fff', letterSpacing: -2, marginTop: 22, lineHeight: 1}}>
            EduPlaner <span style={{color: '#F6A57E'}}>2026</span>
          </div>
          <Pojaw od={nazwa + 40}>
            <div style={{fontSize: 40, color: '#fff', fontWeight: 700, marginTop: 22, letterSpacing: 1}}>Mniej dokumentów. Więcej edukacji.</div>
          </Pojaw>
          <Pojaw od={prawo} style={{marginTop: 40, width: 1240}}>
            <div style={{background: 'rgba(255,255,255,0.08)', border: '1.5px solid rgba(255,255,255,0.28)', borderRadius: 22, padding: '22px 34px'}}>
              <div style={{display: 'flex', alignItems: 'center', gap: 12, marginBottom: 14}}>
                <span style={{fontSize: 26}}>⚖</span>
                <span style={{fontSize: 16, letterSpacing: 3, color: '#F6A57E', fontWeight: 700}}>PODSTAWA PRAWNA METRYCZKI</span>
              </div>
              {PRAWO.map((p, i) => (
                <Pojaw key={p.tytul} od={prawo + 10 + i * 12} przesun={14}>
                  <div style={{display: 'flex', gap: 14, alignItems: 'baseline', padding: '7px 0', borderTop: i === 0 ? 'none' : '1px solid rgba(255,255,255,0.14)'}}>
                    <span style={{color: '#F6A57E', fontWeight: 900, fontSize: 20}}>✓</span>
                    <span style={{fontSize: 22, color: '#fff', fontWeight: 700}}>{p.tytul}</span>
                    <span style={{fontSize: 17, color: 'rgba(255,255,255,0.72)'}}>{p.opis}</span>
                  </div>
                </Pojaw>
              ))}
            </div>
          </Pojaw>
          <Pojaw od={prawo + 60}>
            <div style={{marginTop: 22, fontSize: 17, color: 'rgba(255,255,255,0.6)', textAlign: 'center', letterSpacing: 2}}>
              EDUPLANER 2026 · PCTP KOSZALIN · kontakt@eduplaner2026.pl · 662 888 403
            </div>
          </Pojaw>
        </div>
      </div>
    </AbsoluteFill>
  );
};
