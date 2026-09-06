import React from 'react';
import { AbsoluteFill, Audio, OffthreadVideo, Sequence, staticFile } from 'remotion';
import { FPS, KADR, KOLOR } from './marka';
import { PasekNapisow, Stopka, Tlo } from './elementy';
import { RysujScene } from './sceny/Sceny';
import type { Modul as ModulTyp, Ujecie } from './typy';

/** Napisy: dzielimy zdanie na kawałki po ~11 słów i rozkładamy je proporcjonalnie do długości. */
export const podzielNaNapisy = (tekst: string, klatki: number) => {
  const slowa = tekst.split(/\s+/).filter(Boolean);
  if (!slowa.length) return [];
  const naKawalek = 11;
  const kawalki: string[] = [];
  for (let i = 0; i < slowa.length; i += naKawalek) kawalki.push(slowa.slice(i, i + naKawalek).join(' '));
  const znaki = kawalki.reduce((s, k) => s + k.length, 0) || 1;
  let kursor = 0;
  return kawalki.map((k, i) => {
    const dlugosc = i === kawalki.length - 1 ? klatki - kursor : Math.round((k.length / znaki) * klatki);
    const wynik = { tekst: k, od: kursor, dlugosc: Math.max(dlugosc, 12) };
    kursor += dlugosc;
    return wynik;
  });
};

export const klatkiUjecia = (u: Ujecie) => Math.max(Math.round(u.sekundy * FPS), FPS);

/**
 * Okienko z awatarem HeyGen w lewym dolnym rogu — równo z paskiem napisów.
 * Awatar niesie własny dźwięk, więc w takim ujęciu nie dokładamy ścieżki lektora.
 */
const OkienkoAwatara: React.FC<{ plik: string }> = ({ plik }) => (
  <div
    style={{
      position: 'absolute',
      left: KADR.margines,
      top: KADR.pasekNapisowGora,
      width: 300,
      height: 169,
      borderRadius: 14,
      overflow: 'hidden',
      border: `1px solid ${KOLOR.ramka}`,
      boxShadow: '0 12px 34px rgba(45,27,105,0.18)',
      background: KOLOR.kartka,
    }}
  >
    <OffthreadVideo src={staticFile(`awatar/${plik}`)} style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
  </div>
);

const Ujecie: React.FC<{ ujecie: Ujecie; etykieta: string }> = ({ ujecie, etykieta }) => {
  const klatki = klatkiUjecia(ujecie);
  const napisy = podzielNaNapisy(ujecie.narracja, klatki);
  return (
    <AbsoluteFill>
      <Tlo />
      <RysujScene scena={ujecie.scena} etykieta={etykieta} />
      {ujecie.awatar ? (
        <OkienkoAwatara plik={ujecie.awatar} />
      ) : ujecie.glos ? (
        <Audio src={staticFile(`glos/${ujecie.glos}`)} />
      ) : null}
      {napisy.map((n, i) => (
        <Sequence key={i} from={n.od} durationInFrames={n.dlugosc}>
          <PasekNapisow tekst={n.tekst} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};

export const Modul: React.FC<{ modul: ModulTyp }> = ({ modul }) => {
  let kursor = 0;
  return (
    <AbsoluteFill style={{ backgroundColor: KOLOR.tlo }}>
      {modul.ujecia.map((u) => {
        const klatki = klatkiUjecia(u);
        const od = kursor;
        kursor += klatki;
        return (
          <Sequence key={u.id} from={od} durationInFrames={klatki}>
            <Ujecie ujecie={u} etykieta={`CZĘŚĆ ${modul.numer} · ${modul.tytul.toUpperCase()}`} />
            <Stopka lewa="EduPlaner 2026 · PCTP Koszalin · szkoła podstawowa" prawa={`${u.id}`} />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};

export const dlugoscModulu = (modul: ModulTyp) =>
  modul.ujecia.reduce((s, u) => s + klatkiUjecia(u), 0) || FPS;

export const wymiary = { width: KADR.szerokosc, height: KADR.wysokosc, fps: FPS };
