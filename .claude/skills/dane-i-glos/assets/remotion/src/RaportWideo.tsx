import React from 'react';
import {AbsoluteFill, Audio, Sequence, staticFile, useVideoConfig} from 'remotion';
import {MARKA, FONT} from './marka';
import {Tytul} from './sceny/Tytul';
import {Liczba} from './sceny/Liczba';
import {Wykres} from './sceny/Wykres';
import {Wniosek} from './sceny/Wniosek';
import {Napisy} from './Napisy';
import type {Film} from './typy';
import type {Napis} from './srt';

export type Props = {film: Film; napisy: Napis[]};

export const RaportWideo: React.FC<Props> = ({film, napisy}) => {
  const {fps} = useVideoConfig();
  const naKlatki = (sek: number) => Math.max(1, Math.round(sek * fps));

  return (
    <AbsoluteFill style={{background: MARKA.tlo}}>
      {film.audio ? <Audio src={staticFile(film.audio)} /> : null}

      {film.sceny.map((scena, i) => {
        const od = naKlatki(scena.odSek);
        const trwanie = Math.max(1, naKlatki(scena.doSek) - od);
        return (
          <Sequence key={i} from={od} durationInFrames={trwanie}>
            {scena.typ === 'tytul' ? (
              <Tytul tytul={scena.tytul} podtytul={scena.podtytul} />
            ) : scena.typ === 'liczba' ? (
              <Liczba wartosc={scena.wartosc} opis={scena.opis} kontekst={scena.kontekst} />
            ) : scena.typ === 'wykres' ? (
              <Wykres
                tytul={scena.tytul}
                slupki={scena.slupki}
                jednostka={scena.jednostka}
                wyroznij={scena.wyroznij}
                maks={scena.maks}
              />
            ) : (
              <Wniosek tekst={scena.tekst} />
            )}
          </Sequence>
        );
      })}

      {napisy.length > 0 ? <Napisy napisy={napisy} /> : null}

      {film.stopka ? (
        <div
          style={{
            position: 'absolute',
            left: 140,
            bottom: 36,
            fontFamily: FONT,
            fontSize: 22,
            color: MARKA.tekstCichy,
          }}
        >
          {film.stopka}
        </div>
      ) : null}
    </AbsoluteFill>
  );
};
