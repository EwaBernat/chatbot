import React from 'react';
import {useCurrentFrame} from 'remotion';
import {Arkusz} from '../Arkusz';
import {MARKA, FONT} from '../marka';
import {Kratka, Kursor, Pojaw, Pole, Sekcja} from '../ui';
import type {Z} from '../typy';

/** Strona 2: III Podstawa objęcia, IV Karta potrzeby wsparcia, V Wybór ścieżki. */
export const Druk2: React.FC<{trwanie: number; z: Z}> = ({trwanie, z}) => {
  const frame = useCurrentFrame();
  const karta = z.karta ?? Math.round(trwanie * 0.4);
  const klikZn = z.klik ?? Math.round(trwanie * 0.8);
  // sekcja III do „karty", sekcja IV od „karty" do „kliknięcia", sekcja V wokół kliknięcia
  const t = (u: number) => (u < 0.4 ? Math.round(4 + (u / 0.4) * (karta - 4)) : u < 0.76 ? Math.round(karta + ((u - 0.4) / 0.36) * (klikZn - 10 - karta)) : Math.round(klikZn - 10 + (u - 0.76) * 100));
  const klik = klikZn + 34;
  return (
    <Arkusz strona="Strona 2 z 4 · Podstawa i zgłoszenie">
      <Sekcja numer="III" tytul="PODSTAWA OBJĘCIA KSZTAŁCENIEM SPECJALNYM / POMOCĄ PP" od={t(0.02)} />
      <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px 20px', marginTop: 12}}>
        <Pole etykieta="NUMER ORZECZENIA / OPINII" wartosc="PPP.4223.142.2025" od={t(0.05)} wysokosc={64} />
        <Pole etykieta="DATA WYDANIA" wartosc="2025-05-20" od={t(0.1)} wysokosc={64} />
        <Pole etykieta="ORGAN WYDAJĄCY (PORADNIA)" wartosc="Poradnia Psychologiczno-Pedagogiczna w Koszalinie" od={t(0.14)} tempo={0.5} wysokosc={64} />
        <Pole etykieta="OKRES OBOWIĄZYWANIA" wartosc="do rozpoczęcia nauki w szkole" od={t(0.22)} tempo={0.7} wysokosc={64} />
      </div>
      <Sekcja numer="IV" tytul="KARTA POTRZEBY WSPARCIA — ZGŁOSZENIE" od={t(0.4)} style={{marginTop: 18}} />
      <Pojaw od={t(0.42)}>
        <div style={{fontSize: 14, color: MARKA.tekstCichy, marginTop: 8, fontFamily: FONT}}>Zaznacz, kto zgłosił potrzebę wsparcia.</div>
      </Pojaw>
      <div style={{display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 12, marginTop: 8}}>
        <Kratka tekst="Dziecko" od={t(0.44)} />
        <Kratka tekst="Nauczyciel / wychowawca" od={t(0.46)} />
        <Kratka tekst="Rodzic / opiekun" od={t(0.48)} />
        <Kratka tekst="Inna osoba" od={t(0.5)} zaznacz />
      </div>
      <div style={{marginTop: 12}}>
        <Pole etykieta="ZGŁASZAJĄCY — IMIĘ I NAZWISKO / FUNKCJA" wartosc="Karolina Dąbrowska (matka)" od={t(0.56)} wysokosc={60} />
      </div>
      <Pojaw od={t(0.62)}>
        <div style={{fontSize: 14, color: MARKA.tekstCichy, marginTop: 10, fontFamily: FONT}}>Przyczyna zgłoszenia</div>
      </Pojaw>
      <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 10, marginTop: 6}}>
        <Kratka tekst="Trudności w nauce" od={t(0.64)} />
        <Kratka tekst="Trudności w radzeniu sobie z emocjami" od={t(0.66)} zaznacz />
        <Kratka tekst="Trudności w relacjach z rówieśnikami" od={t(0.68)} zaznacz />
        <Kratka tekst="Trudności w samoobsłudze" od={t(0.7)} />
      </div>
      <Sekcja numer="V" tytul="WYBÓR ŚCIEŻKI WSPARCIA" od={t(0.76)} style={{marginTop: 18}} />
      <div style={{display: 'grid', gap: 10, marginTop: 10}}>
        <Kratka tekst="Ścieżka A — dziecko z wcześniejszą diagnozą (orzeczenie / opinia PPP)" od={t(0.78)} zaznacz={frame >= klik - 14} />
        <Kratka tekst="Ścieżka B — dziecko nowo zgłoszone (pierwsza obserwacja w przedszkolu)" od={t(0.8)} />
      </div>
      <Kursor punkty={[{klatka: t(0.72), x: 1500, y: 1040}, {klatka: t(0.84), x: 340, y: 905}]} klik={klik} />
    </Arkusz>
  );
};
