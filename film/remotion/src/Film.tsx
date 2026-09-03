import React from 'react';
import {AbsoluteFill, Audio, Sequence, staticFile, useVideoConfig} from 'remotion';
import {MARKA, FONT} from './marka';
import {Tytul} from './sceny/Tytul';
import {Liczba} from './sceny/Liczba';
import {Wykres} from './sceny/Wykres';
import {Wniosek} from './sceny/Wniosek';
import {Ilustracja} from './sceny/Ilustracja';
import {Przepis} from './sceny/Przepis';
import {Porownanie} from './sceny/Porownanie';
import {Sciezka} from './sceny/Sciezka';
import {Druk} from './sceny/Druk';
import {Profil} from './sceny/Profil';
import {CelSmart} from './sceny/CelSmart';
import {Lista} from './sceny/Lista';
import {Napisy} from './Napisy';
import type {Film as FilmT, Scena} from './typy';
import type {Napis} from './srt';

export type Props = {film: FilmT; napisy: Napis[]};

const Scena: React.FC<{s: Scena}> = ({s}) => {
  switch (s.typ) {
    case 'tytul':
      return <Tytul tytul={s.tytul} podtytul={s.podtytul} nadtytul={s.nadtytul} />;
    case 'liczba':
      return <Liczba wartosc={s.wartosc} opis={s.opis} kontekst={s.kontekst} />;
    case 'wykres':
      return <Wykres tytul={s.tytul} slupki={s.slupki} jednostka={s.jednostka} wyroznij={s.wyroznij} maks={s.maks} />;
    case 'wniosek':
      return <Wniosek tekst={s.tekst} />;
    case 'ilustracja':
      return <Ilustracja obraz={s.obraz} tytul={s.tytul} podpis={s.podpis} />;
    case 'przepis':
      return <Przepis etykieta={s.etykieta} tytul={s.tytul} sygnatura={s.sygnatura} status={s.status} data={s.data} uwaga={s.uwaga} />;
    case 'porownanie':
      return <Porownanie tytul={s.tytul} naglowki={s.naglowki} bylo={s.bylo} jest={s.jest} />;
    case 'sciezka':
      return <Sciezka tytul={s.tytul} przystanki={s.przystanki} aktywny={s.aktywny} />;
    case 'druk':
      return <Druk obraz={s.obraz} szerObrazu={s.szerObrazu} wysObrazu={s.wysObrazu} kadr={s.kadr} pola={s.pola} etykieta={s.etykieta} />;
    case 'profil':
      return <Profil tytul={s.tytul} obszary={s.obszary} wynik={s.wynik} />;
    case 'celSmart':
      return <CelSmart przed={s.przed} po={s.po} />;
    case 'lista':
      return <Lista tytul={s.tytul} punkty={s.punkty} numerowana={s.numerowana} />;
  }
};

export const Film: React.FC<Props> = ({film, napisy}) => {
  const {fps} = useVideoConfig();
  const naKlatki = (sek: number) => Math.max(0, Math.round(sek * fps));

  return (
    <AbsoluteFill style={{background: MARKA.tlo, fontFamily: FONT}}>
      {film.audio ? <Audio src={staticFile(film.audio)} /> : null}

      {film.sceny.map((scena, i) => {
        const od = naKlatki(scena.odSek);
        const trwanie = Math.max(1, naKlatki(scena.doSek) - od);
        return (
          <Sequence key={i} from={od} durationInFrames={trwanie}>
            <Scena s={scena} />
          </Sequence>
        );
      })}

      {/* pasek modułu — stały punkt odniesienia dla widza */}
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          right: 0,
          height: 8,
          background: MARKA.wyroznienie,
        }}
      />
      <div
        style={{
          position: 'absolute',
          top: 30,
          right: 80,
          fontSize: 22,
          letterSpacing: 3,
          fontWeight: 700,
          color: MARKA.tekstCichy,
        }}
      >
        {film.modul}
      </div>

      {napisy.length > 0 ? <Napisy napisy={napisy} /> : null}

      {film.stopka ? (
        <div style={{position: 'absolute', left: 80, bottom: 30, fontSize: 20, color: MARKA.tekstCichy}}>
          {film.stopka}
        </div>
      ) : null}
    </AbsoluteFill>
  );
};
