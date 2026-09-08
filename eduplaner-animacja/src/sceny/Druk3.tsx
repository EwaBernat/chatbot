import React from 'react';
import {interpolate, useCurrentFrame} from 'remotion';
import {Arkusz} from '../Arkusz';
import {MARKA, FONT} from '../marka';
import {Kratka, Pojaw, Pole, Sekcja, useWejscie} from '../ui';
import type {Z} from '../typy';

const ZESPOL = [
  ['Koordynator zespołu', 'mgr Joanna Krawczyk'],
  ['Wychowawca grupy', 'mgr Joanna Krawczyk'],
  ['Pedagog specjalny', 'imię i nazwisko'],
  ['Psycholog', 'imię i nazwisko'],
  ['Logopeda', 'imię i nazwisko'],
  ['Nauczyciel wspomagający', 'imię i nazwisko'],
];

const Wiersz: React.FC<{lp: number; funkcja: string; osoba: string; od: number; auto: boolean}> = ({lp, funkcja, osoba, od, auto}) => {
  const frame = useCurrentFrame();
  const w = useWejscie(od, {damping: 16, stiffness: 120});
  const blask = auto ? interpolate(frame - od, [8, 20, 60], [0, 0.35, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}) : 0;
  return (
    <div
      style={{
        display: 'grid',
        gridTemplateColumns: '60px 1fr 1.1fr 1fr',
        fontFamily: FONT,
        fontSize: 18,
        background: blask > 0 ? `rgba(232,69,10,${blask})` : lp % 2 === 0 ? '#FBF7F2' : '#fff',
        borderBottom: `1px solid ${MARKA.linia}`,
        opacity: w,
        transform: `translateX(${(1 - w) * -30}px)`,
      }}
    >
      <div style={{padding: '10px 14px', color: MARKA.pomarancz, fontWeight: 700, borderRight: `1px solid ${MARKA.linia}`}}>{lp}</div>
      <div style={{padding: '10px 14px', color: '#1f1a33', borderRight: `1px solid ${MARKA.linia}`}}>{funkcja}</div>
      <div style={{padding: '10px 14px', color: auto ? MARKA.fiolet : '#B3ADC4', fontWeight: auto ? 700 : 400, borderRight: `1px solid ${MARKA.linia}`}}>
        {osoba}
        {auto ? <span style={{marginLeft: 10, fontSize: 12, background: MARKA.morskiJasny, color: MARKA.morski, padding: '2px 8px', borderRadius: 999, fontWeight: 700}}>z metryczki</span> : null}
      </div>
      <div style={{padding: '10px 14px', color: '#B3ADC4'}}>funkcja w placówce</div>
    </div>
  );
};

/** Strona 3: VI Powołanie koordynatora i skład zespołu, VII Źródła informacji — audyt. */
export const Druk3: React.FC<{trwanie: number; z: Z}> = ({trwanie, z}) => {
  const tabela = z.tabela ?? Math.round(trwanie * 0.2);
  const zrodla = z.zrodla ?? Math.round(trwanie * 0.6);
  const t = (u: number) => (u < 0.17 ? Math.round(4 + (u / 0.17) * (tabela - 4)) : u < 0.52 ? Math.round(tabela + ((u - 0.17) / 0.35) * (zrodla - 10 - tabela)) : Math.round(zrodla + ((u - 0.52) / 0.3) * (trwanie - 30 - zrodla)));
  return (
    <Arkusz strona="Strona 3 z 4 · Zespół i źródła informacji" data="21.07.2026 r.">
      <Sekcja numer="VI" tytul="POWOŁANIE KOORDYNATORA I SKŁAD ZESPOŁU" od={t(0.02)} />
      <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px 20px', marginTop: 12}}>
        <Pole etykieta="DATA POWOŁANIA" wartosc="2025-09-22" od={t(0.05)} wysokosc={60} />
        <Pole etykieta="DECYZJA / ZARZĄDZENIE NR" wartosc="19/PP/2025" od={t(0.09)} wysokosc={60} />
      </div>
      <Pojaw od={t(0.14)} style={{marginTop: 14, borderRadius: 10, overflow: 'hidden', border: `1px solid ${MARKA.linia}`}}>
        <div style={{display: 'grid', gridTemplateColumns: '60px 1fr 1.1fr 1fr', background: MARKA.fiolet, color: '#fff', fontFamily: FONT, fontSize: 15, fontWeight: 700, letterSpacing: 1}}>
          <div style={{padding: '10px 14px'}}>LP.</div>
          <div style={{padding: '10px 14px'}}>FUNKCJA W ZESPOLE</div>
          <div style={{padding: '10px 14px'}}>IMIĘ I NAZWISKO</div>
          <div style={{padding: '10px 14px'}}>FUNKCJA W PLACÓWCE</div>
        </div>
        {ZESPOL.map(([f, o], i) => (
          <Wiersz key={f} lp={i + 1} funkcja={f} osoba={o} od={t(0.17) + i * 7} auto={i < 2} />
        ))}
      </Pojaw>
      <Sekcja numer="VII" tytul="ŹRÓDŁA INFORMACJI O DZIECKU — AUDYT" od={t(0.52)} style={{marginTop: 18}} />
      <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 10, marginTop: 10}}>
        <Kratka tekst="Orzeczenie o potrzebie kształcenia specjalnego" od={t(0.55)} />
        <Kratka tekst="Opinia poradni psychologiczno-pedagogicznej" od={t(0.57)} zaznacz />
        <Kratka tekst="Opinie nauczycieli / specjalisty" od={t(0.59)} />
        <Kratka tekst="Wywiad z rodzicem / opiekunem" od={t(0.61)} zaznacz />
      </div>
      <Pojaw od={t(0.7)}>
        <div style={{fontSize: 14, color: MARKA.tekstCichy, marginTop: 12, fontFamily: FONT}}>Uwarunkowania medyczne istotne dla funkcjonowania</div>
      </Pojaw>
      <div style={{display: 'grid', gridTemplateColumns: 'repeat(6, 1fr)', gap: 10, marginTop: 6}}>
        {['Padaczka', 'Cukrzyca', 'Alergie', 'Astma', 'Wady serca', 'Inne'].map((m, i) => (
          <Kratka key={m} tekst={m} od={t(0.72) + i * 3} zaznacz={m === 'Alergie'} />
        ))}
      </div>
    </Arkusz>
  );
};
