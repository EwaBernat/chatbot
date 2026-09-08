import React from 'react';
import {interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';
import {Arkusz} from '../Arkusz';
import {MARKA, FONT} from '../marka';
import {Kratka, Pojaw, Pole, Sekcja} from '../ui';
import type {Z} from '../typy';

const Stempel: React.FC<{od: number}> = ({od}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const s = spring({frame: frame - od, fps, config: {damping: 9, stiffness: 160}});
  const kat = interpolate(s, [0, 1], [-18, -8]);
  return (
    <div
      style={{
        position: 'absolute',
        right: 40,
        top: 640,
        transform: `rotate(${kat}deg) scale(${0.6 + 0.4 * s})`,
        opacity: s,
        border: `5px solid ${MARKA.morski}`,
        color: MARKA.morski,
        borderRadius: 16,
        padding: '14px 26px',
        fontFamily: FONT,
        fontWeight: 900,
        fontSize: 30,
        letterSpacing: 2,
        background: 'rgba(255,255,255,0.9)',
        boxShadow: '0 14px 40px rgba(47,143,138,0.25)',
        textAlign: 'center',
      }}
    >
      ✓ TECZKA DZIECKA
      <div style={{fontSize: 18, letterSpacing: 3, marginTop: 4}}>PIERWSZA STRONA GOTOWA</div>
    </div>
  );
};

/** Strona 4: VIII Synteza zaleceń, IX Dostępność placówki, X Plan współpracy międzysektorowej. */
export const Druk4: React.FC<{trwanie: number; z: Z}> = ({trwanie, z}) => {
  const dost = z.dostepnosc ?? Math.round(trwanie * 0.4);
  const gotowe = z.gotowe ?? Math.round(trwanie * 0.8);
  const t = (u: number) => (u < 0.4 ? Math.round(4 + (u / 0.4) * (dost - 4)) : u < 0.8 ? Math.round(dost + ((u - 0.4) / 0.4) * (gotowe - 6 - dost)) : gotowe + 4);
  return (
    <Arkusz strona="Strona 4 z 4 · Synteza i współpraca" data="21.07.2026 r.">
      <Sekcja numer="VIII" tytul="SYNTEZA ZALECEŃ I WSKAZAŃ" od={t(0.02)} />
      <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px 20px', marginTop: 12}}>
        <Pole etykieta="★ MOCNE STRONY DZIECKA" wartosc="Spostrzegawcza, uważna na szczegóły, zdolności plastyczne" od={t(0.05)} tempo={0.35} wysokosc={64} />
        <Pole etykieta="⚠ TRUDNOŚCI DZIECKA" wartosc="Reaguje lękiem na hałas i tłok, trudność w dołączaniu do zabaw grupowych" od={t(0.1)} tempo={0.3} wysokosc={64} />
      </div>
      <div style={{marginTop: 12}}>
        <Pole etykieta="➜ NADRZĘDNY KIERUNEK WSPARCIA" wartosc="Stopniowe oswajanie z bodźcami sensorycznymi · wsparcie w budowaniu relacji rówieśniczych · strefa wyciszenia w sali" od={t(0.17)} tempo={0.22} wysokosc={64} />
      </div>
      <Sekcja numer="IX" tytul="DOSTĘPNOŚĆ PLACÓWKI — ANALIZA GOTOWOŚCI" od={t(0.4)} style={{marginTop: 16}} />
      <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8, marginTop: 10}}>
        {[
          ['Dostępność fizyczna (podjazdy, winda, toaleta)', true],
          ['Regulowane stanowisko pracy / ławka', false],
          ['Strefa wyciszenia', true],
          ['Oświetlenie i akustyka pomieszczeń', true],
          ['Komunikacja AAC / pętla indukcyjna · FM', false],
          ['Dostosowanie materiałów i przygotowanie kadry', true],
        ].map(([tekst, z], i) => (
          <Kratka key={String(tekst)} tekst={String(tekst)} od={t(0.43) + i * 3} zaznacz={Boolean(z)} style={{padding: '7px 14px', fontSize: 16}} />
        ))}
      </div>
      <Sekcja numer="X" tytul="PLAN WSPÓŁPRACY MIĘDZYSEKTOROWEJ" od={t(0.6)} style={{marginTop: 16}} />
      <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px 20px', marginTop: 10}}>
        <Pole etykieta="OŚWIATA (PPP, SCWEW, INNE PLACÓWKI)" wartosc="konsultacje w PPP, wsparcie SCWEW" od={t(0.63)} tempo={0.5} wysokosc={58} />
        <Pole etykieta="ZDROWIE (LEKARZ, TERAPEUCI, PORADNIE)" wartosc="terapeuta SI, zalecenia lekarza" od={t(0.66)} tempo={0.5} wysokosc={58} />
        <Pole etykieta="POMOC SPOŁECZNA (OPS, ASYSTENT RODZINY)" wartosc="—" od={t(0.69)} wysokosc={58} />
        <Pole etykieta="WSPÓŁPRACA ZE SCWEW" wartosc="konsultacje eksperckie, superwizja" od={t(0.71)} tempo={0.5} wysokosc={58} />
      </div>
      <Stempel od={gotowe + 4} />
    </Arkusz>
  );
};
