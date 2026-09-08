import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {MARKA, FONT} from '../marka';
import {Ikona, Kursor, Pojaw, useWejscie} from '../ui';
import type {Z} from '../typy';

const KARTY = [
  {ikona: 'skrzynka', tytul: 'Zgłoszenie - placówka', opis: 'Wewnętrzne zgłoszenie dziecka do objęcia wsparciem.', odznaka: 'wejście ścieżki'},
  {ikona: 'osoby', tytul: 'Zgłoszenie - rodzica', opis: 'Zgłoszenie / wniosek od rodzica lub opiekuna.'},
  {ikona: 'dziecko', tytul: 'Druk metryczki dziecka', opis: 'Dane dziecka — zasilają wszystkie dalsze druki.', odznaka: 'zasila cały system', klik: true},
  {ikona: 'dymek', tytul: 'Wywiad z rodzicem', opis: 'Historia rozwoju, potrzeby, oczekiwania.'},
  {ikona: 'dostepnosc', tytul: 'Arkusz dostępności placówki', opis: 'Dostępność architektoniczna, komunikacyjna, organizacyjna.'},
  {ikona: 'budynek', tytul: 'Warianty organizacyjne', opis: 'Możliwe formy organizacji wsparcia.'},
  {ikona: 'tarcza', tytul: 'Zgoda rodzica / opiekuna prawnego', opis: 'Zgoda na przetwarzanie danych.'},
  {ikona: 'waga', tytul: 'Podstawa prawna', opis: 'Aktualne akty prawne 2026 — stały punkt odniesienia.'},
];

const WYLICZANKA = [0, 1, 3, 4, 6, 7]; // Zgłoszenie placówki, rodzica, wywiad, dostępność, zgody, podstawa prawna

const Karta: React.FC<{k: (typeof KARTY)[number]; od: number; KLIK: number; i: number; wyl: number; wylKoniec: number}> = ({k, od, KLIK, i, wyl, wylKoniec}) => {
  const frame = useCurrentFrame();
  const poz = WYLICZANKA.indexOf(i);
  const krok = (wylKoniec - wyl) / WYLICZANKA.length;
  const start = wyl + poz * krok;
  const wyr = poz >= 0 ? interpolate(frame, [start, start + 6, start + krok - 4, start + krok + 4], [0, 1, 1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}) : 0;
  const w = useWejscie(od, {damping: 15, stiffness: 110});
  const nacisk = k.klik ? interpolate(frame, [KLIK - 8, KLIK, KLIK + 6, KLIK + 14], [1, 1.03, 0.97, 1.02], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}) : 1;
  const podswietl = k.klik ? interpolate(frame, [KLIK - 14, KLIK], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}) : 0;
  return (
    <div
      style={{
        borderRadius: 18,
        borderLeft: `7px solid ${MARKA.morski}`,
        boxShadow: podswietl > 0 || wyr > 0 ? `0 18px 50px rgba(47,143,138,${0.15 + 0.3 * Math.max(podswietl, wyr)})` : '0 10px 30px rgba(45,27,105,0.08)',
        padding: '26px 30px',
        display: 'flex',
        gap: 22,
        alignItems: 'flex-start',
        fontFamily: FONT,
        opacity: w,
        transform: `translateY(${(1 - w) * 40}px) scale(${nacisk + 0.025 * wyr})`,
        background: wyr > 0 ? `rgb(${255 - 28 * wyr}, ${255 - 12 * wyr}, ${255 - 13 * wyr})` : '#fff',
        minHeight: 138,
        boxSizing: 'border-box',
        outline: podswietl > 0 || wyr > 0 ? `${3 * Math.max(podswietl, wyr)}px solid ${MARKA.morski}` : 'none',
      }}
    >
      <div style={{width: 58, height: 58, borderRadius: 14, background: MARKA.morskiJasny, display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0}}>
        <Ikona typ={k.ikona} rozmiar={32} />
      </div>
      <div>
        <div style={{fontSize: 26, fontWeight: 700, color: '#2b2440'}}>{k.tytul}</div>
        <div style={{fontSize: 19, color: '#5f5a70', marginTop: 8, lineHeight: 1.35}}>{k.opis}</div>
        {k.odznaka ? (
          <div style={{display: 'inline-block', marginTop: 12, background: MARKA.morskiJasny, color: MARKA.morski, fontSize: 15, fontWeight: 700, padding: '5px 14px', borderRadius: 999}}>
            {k.odznaka}
          </div>
        ) : null}
      </div>
    </div>
  );
};

export const EkranGlowny: React.FC<{z: Z}> = ({z}) => {
  const frame = useCurrentFrame();
  const KLIK = Math.max(70, (z.klik ?? 200) + 12);
  const wyl = z.wyliczanka ?? 60;
  const wylKoniec = KLIK - 40;
  const blysk = interpolate(frame, [KLIK + 8, KLIK + 22], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return (
    <AbsoluteFill style={{background: `linear-gradient(135deg, #FBF3EA 0%, ${MARKA.tloCieple} 45%, #F4F1F7 100%)`, fontFamily: FONT}}>
      <div style={{position: 'absolute', left: 120, top: 70, right: 120}}>
        <div style={{display: 'flex', gap: 26, alignItems: 'center'}}>
          <Pojaw od={0}>
            <div style={{width: 92, height: 92, borderRadius: 22, background: MARKA.morski, display: 'flex', alignItems: 'center', justifyContent: 'center', boxShadow: '0 12px 30px rgba(47,143,138,0.35)'}}>
              <Ikona typ="karta" kolor="#fff" rozmiar={52} />
            </div>
          </Pojaw>
          <div>
            <Pojaw od={2}>
              <div style={{fontSize: 17, letterSpacing: 2.5, fontWeight: 700, color: MARKA.morski}}>PRZYJĘCIE · DANE WEJŚCIOWE</div>
            </Pojaw>
            <Pojaw od={5}>
              <div style={{fontSize: 62, fontWeight: 800, color: '#2b2440', letterSpacing: -1, lineHeight: 1.05}}>Metryczka</div>
            </Pojaw>
          </div>
        </div>
        <Pojaw od={9}>
          <div style={{fontSize: 22, color: '#5f5a70', marginTop: 14}}>
            Zgłoszenie i dane wejściowe dziecka — druki wstępne, wywiad z rodzicem, dostępność placówki i zgody.
          </div>
        </Pojaw>
        <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '22px 26px', marginTop: 32}}>
          {KARTY.map((k, i) => (
            <Karta key={k.tytul} k={k} od={10 + i * 4} KLIK={KLIK} i={i} wyl={wyl} wylKoniec={wylKoniec} />
          ))}
        </div>
      </div>
      <Kursor
        punkty={[
          {klatka: KLIK - 60, x: 1500, y: 980},
          {klatka: KLIK - 30, x: 900, y: 620},
          {klatka: KLIK - 8, x: 560, y: 545},
        ]}
        klik={KLIK}
      />
      <AbsoluteFill style={{background: MARKA.lawendaTlo, opacity: blysk}} />
    </AbsoluteFill>
  );
};
