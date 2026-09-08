import React from 'react';
import {AbsoluteFill, Audio, Sequence, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA} from '../marka';
import {Napisy} from '../Napisy';
import type {Napis} from '../typy';
import {KpofIntro} from './KpofIntro';
import {KpofFinal} from './KpofFinal';
import {OryginalnyDruk, type Krok, type Ujecie} from './OryginalnyDruk';

export type FilmKpof = {audio: string; plik: string; napisy: Napis[]; dlugosc: number};
export type Props = {film: FilmKpof};

/** Oceny dobrane tak, żeby profil pokazał WSZYSTKIE kolory: zasób, Poziom I, II i III (oraz jedno N). */
const OCENY: Record<string, string[]> = {
  I: ['4', '4', '3', '4', '3'], // 3,6 → Poziom I
  II: ['3', '3', '4', '3', '3'], // 3,2 → Poziom I
  III: ['3', '2', '3', '2', '3'], // 2,6 → Poziom II
  IV: ['5', '4', '5', '4', '4'], // 4,4 → zasób
  V: ['3', '3', '4', '2', '3'], // 3,0 → Poziom I
  VI: ['4', '3', 'N'], // opisowy, N nie obniża wyniku
  VII: ['2', '1', '2', '2', '1'], // 1,6 → Poziom III
  VIII: ['3', '4', '3', '3', '3'], // 3,2 → Poziom I
  IX: ['3', '2', '2', '3'], // 2,5 → Poziom II
};

const Przejscie: React.FC<{trwanie: number; children: React.ReactNode}> = ({trwanie, children}) => {
  const frame = useCurrentFrame();
  const wejscie = interpolate(frame, [0, 10], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const wyjscie = interpolate(frame, [trwanie - 9, trwanie - 1], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const o = Math.min(wejscie, wyjscie);
  return <AbsoluteFill style={{opacity: o}}>{children}</AbsoluteFill>;
};

const PasekPostepu: React.FC = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  return <div style={{position: 'absolute', left: 0, bottom: 0, height: 6, width: `${(100 * frame) / durationInFrames}%`, background: MARKA.pomarancz}} />;
};

/** Harmonogram kroków i kamery zbudowany z czasów zdań narracji (indeksy = kolejność zdań w scenariuszu). */
const zbudujHarmonogram = (n: Napis[]) => {
  const z = (i: number) => n[Math.min(i, n.length - 1)].odSek;
  const k = (i: number) => n[Math.min(i, n.length - 1)].doSek;
  const kroki: Krok[] = [];
  const kamera: Ujecie[] = [];

  // Metryczka (zdania 2–5)
  kamera.push({sek: 0, selektor: '.sheet:nth-of-type(1) .fgrid', skala: 1.42, przesun: -10});
  kroki.push({sek: z(3), doSek: k(3) + 0.4, typ: 'wyroznij', selektor: '.sheet:nth-of-type(1) .fgrid'});
  kroki.push({sek: z(3) + 0.6, typ: 'tekst', selektor: '.sheet:nth-of-type(1) .student .blank', tekst: '26.09.2026', tempo: 12});
  kroki.push({sek: z(4) + 1.0, typ: 'klik', selektor: '.sheet:nth-of-type(1) .optgrid .opt:nth-child(1)'});
  kroki.push({sek: z(5), typ: 'tekst', selektor: '.sheet:nth-of-type(1) .fgrid .fg:nth-child(5) .blankline', tekst: 'mgr Anna Nowak — nauczycielka grupy', tempo: 16});
  kroki.push({sek: z(5) + 1.4, typ: 'tekst', selektor: '.sheet:nth-of-type(1) .fgrid .fg:nth-child(6) .blankline', tekst: '01.09 – 26.09.2026', tempo: 16});

  // Skala (zdania 6–8)
  kamera.push({sek: z(6), selektor: '.sheet:nth-of-type(1) .scaleleg', skala: 1.9, przesun: 10});
  const chipy = 6;
  const krokChip = (k(7) - z(7)) / chipy;
  for (let i = 0; i < chipy; i++) {
    kroki.push({sek: z(7) + i * krokChip, doSek: z(7) + (i + 1) * krokChip + 0.15, typ: 'wyroznij', selektor: `.sheet:nth-of-type(1) .scaleleg .schip:nth-child(${i + 1})`});
  }
  kroki.push({sek: z(8), doSek: k(8) + 0.5, typ: 'wyroznij', selektor: '.sheet:nth-of-type(1) .scaleleg .schip:nth-child(6)'});

  // Oceny (zdania 9–11): 42 kliknięcia równo rozłożone, kamera podąża za obszarem
  const obszary = Object.keys(OCENY);
  const razem = obszary.reduce((s, o) => s + OCENY[o].length, 0);
  const start = z(9) + 0.4;
  const koniec = k(11) - 0.3;
  const krok = (koniec - start) / razem;
  let i = 0;
  for (const o of obszary) {
    kamera.push({sek: start + i * krok, selektor: `#area-${o}`, skala: 1.38, przesun: 150, czas: 0.8});
    OCENY[o].forEach((w, wiersz) => {
      kroki.push({sek: start + i * krok, typ: 'ocena', obszar: o, wiersz, wartosc: w});
      i++;
    });
  }

  // Prawa kolumna druku: monitoring podstawy programowej i kodów ICF (zdania 12–13)
  kamera.push({sek: z(12), selektor: '#area-VIII', skala: 1.62, przesun: 210});
  const wierszeIcf = [...Array(5)].map((_, r) => `#area-VIII tbody tr:nth-child(${r + 1}) td.code`).concat([...Array(4)].map((_, r) => `#area-IX tbody tr:nth-child(${r + 1}) td.code`));
  wierszeIcf.forEach((sel, r) => {
    kroki.push({sek: z(13) + 0.2 + r * 0.32, doSek: k(13) + 0.6, typ: 'wyroznij', selektor: sel});
  });
  kroki.push({sek: z(12) + 0.3, doSek: k(13) + 0.6, typ: 'wyroznij', selektor: '#area-VIII thead th:nth-child(4)'});

  // Podsumowanie i wykresy (zdania 14–16)
  kamera.push({sek: z(14), selektor: '.sheet:nth-of-type(5) .sec', skala: 1.4, przesun: 260});
  kamera.push({sek: z(15) + 0.2, selektor: '.kpchart', skala: 1.55, przesun: 120});
  kamera.push({sek: z(16), selektor: '.qrtbl', skala: 1.55, przesun: 70});

  return {kroki, kamera, wykresyOdSek: z(15) + 0.6};
};

export const KpofPromo: React.FC<Props> = ({film}) => {
  const {fps} = useVideoConfig();
  const n = film.napisy;
  const z = (i: number) => n[Math.min(i, n.length - 1)].odSek;
  const naKlatki = (s: number) => Math.max(0, Math.round(s * fps));
  const granica = (i: number) => (n[i].odSek + n[i - 1].doSek) / 2; // w środku pauzy

  const introOd = 0;
  const introDo = granica(2);
  const drukOd = introDo;
  const drukDo = granica(17);
  const finalOd = drukDo;
  const finalDo = film.dlugosc;
  const {kroki, kamera, wykresyOdSek} = zbudujHarmonogram(n);

  const lok = (s: number, od: number) => naKlatki(s - od);

  return (
    <AbsoluteFill style={{background: MARKA.tlo}}>
      <Audio src={staticFile(film.audio)} />
      <Sequence from={naKlatki(introOd)} durationInFrames={naKlatki(introDo) - naKlatki(introOd)} name="intro">
        <Przejscie trwanie={naKlatki(introDo) - naKlatki(introOd)}>
          <KpofIntro klikModul={lok(z(1) + 0.3, introOd)} klikWersja={lok(z(1) + 3.2, introOd)} />
        </Przejscie>
      </Sequence>
      <Sequence from={naKlatki(drukOd)} durationInFrames={naKlatki(drukDo) - naKlatki(drukOd)} name="druk">
        <Przejscie trwanie={naKlatki(drukDo) - naKlatki(drukOd)}>
          <OryginalnyDruk plik={film.plik} kroki={kroki} kamera={kamera} wykresyOdSek={wykresyOdSek} odSek={drukOd} />
        </Przejscie>
      </Sequence>
      <Sequence from={naKlatki(finalOd)} durationInFrames={naKlatki(finalDo) - naKlatki(finalOd)} name="final">
        <Przejscie trwanie={naKlatki(finalDo) - naKlatki(finalOd)}>
          <KpofFinal haslo={lok(z(18), finalOd)} prawo={[19, 20, 21, 22, 23].map((i) => lok(z(i), finalOd))} />
        </Przejscie>
      </Sequence>
      <Napisy napisy={n} />
      <PasekPostepu />
    </AbsoluteFill>
  );
};
