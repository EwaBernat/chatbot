import React from 'react';
import {
  AbsoluteFill, Sequence, Audio, staticFile, useVideoConfig,
  useCurrentFrame, interpolate,
} from 'remotion';
import { SalaPrzedszkolna } from './elementy/SalaPrzedszkolna';
import { ZnakPCTP } from './elementy/Logo';
import { Powitanie } from './sceny/Powitanie';
import { Napisy, parsujSrt, type Napis } from './elementy/Napisy';
import {
  Intro, Fakt, Prawo, Konstrukcja, Przejscie, Obszar, Filary, Praktyka, Arkusz, Koniec,
} from './sceny/Sceny';
import { MARKA, FONT_NAGLOWEK } from './marka';
import type { Film as FilmDane, Scena } from './typy';

export type WlasciwosciFilmu = {
  dane: FilmDane;
  napisySrt?: string;
  jestAudio: boolean;
  jestAwatar: boolean;
  /** Długość powitania awatara — o tyle przesuwa się reszta filmu. */
  powitanieKlatek: number;
};

const trescSceny = (s: Scena, jestAwatar: boolean) => {
  switch (s.typ) {
    case 'intro':       return <Intro />;
    case 'fakt':        return <Fakt scena={s} />;
    case 'prawo':       return <Prawo />;
    case 'konstrukcja': return <Konstrukcja />;
    case 'przejscie':   return <Przejscie />;
    case 'obszar':      return <Obszar scena={s} />;
    case 'filary':      return <Filary />;
    case 'praktyka':    return <Praktyka />;
    case 'arkusz':      return <Arkusz />;
    case 'koniec':      return <Koniec jestAwatar={jestAwatar} />;
    default:            return null;
  }
};

/** Krótkie ściemnienie na styku scen — bez niego cięcia kłują w oczy. */
const Przenikanie: React.FC<{ dlugoscKlatek: number; children: React.ReactNode }> = ({
  dlugoscKlatek, children,
}) => {
  const klatka = useCurrentFrame();
  const k = 9;
  const krycie = Math.min(
    interpolate(klatka, [0, k], [0, 1], { extrapolateRight: 'clamp' }),
    interpolate(klatka, [dlugoscKlatek - k, dlugoscKlatek], [1, 0], { extrapolateLeft: 'clamp' }),
  );
  return <AbsoluteFill style={{ opacity: krycie }}>{children}</AbsoluteFill>;
};

export const Film: React.FC<WlasciwosciFilmu> = ({
  dane, napisySrt, jestAudio, jestAwatar, powitanieKlatek,
}) => {
  const { fps } = useVideoConfig();
  const napisy: Napis[] = React.useMemo(
    () => (napisySrt ? parsujSrt(napisySrt) : []), [napisySrt],
  );

  let kursor = 0;
  return (
    <AbsoluteFill>
      <SalaPrzedszkolna />

      {/* Powitanie awatara — mówi własnym dźwiękiem z awatar.webm,
          dlatego narracja lektorska startuje dopiero za nim. */}
      <Sequence durationInFrames={powitanieKlatek} name="0. Powitanie">
        <Przenikanie dlugoscKlatek={powitanieKlatek}>
          <Powitanie jestAwatar={jestAwatar} />
        </Przenikanie>
      </Sequence>

      <Sequence from={powitanieKlatek} name="Narracja">
        <AbsoluteFill>
          {jestAudio ? <Audio src={staticFile(dane.audio)} /> : null}

          {dane.sceny.map((s) => {
            const od = Math.round(kursor * fps);
            const dlugosc = Math.max(1, Math.round(s.sekundy * fps));
            kursor += s.sekundy;
            return (
              <Sequence key={s.nr} from={od} durationInFrames={dlugosc} name={`${s.nr}. ${s.tytul}`}>
                <Przenikanie dlugoscKlatek={dlugosc}>{trescSceny(s, jestAwatar)}</Przenikanie>
              </Sequence>
            );
          })}

          <Napisy napisy={napisy} />
        </AbsoluteFill>
      </Sequence>

      {/* warstwa stała nad wszystkim: znak i podpis materiału */}
      <div style={{ position: 'absolute', left: 64, top: 54, display: 'flex',
                    alignItems: 'center', gap: 18 }}>
        <ZnakPCTP rozmiar={74} />
        <div>
          <p style={{ margin: 0, fontFamily: FONT_NAGLOWEK, fontWeight: 900, fontSize: 30,
                      color: '#fff', lineHeight: 1 }}>
            EduPlaner <span style={{ color: MARKA.pomaranczJasny }}>2026</span>
          </p>
          <p style={{ margin: '3px 0 0', fontFamily: FONT_NAGLOWEK, fontWeight: 700,
                      fontSize: 15, letterSpacing: '.16em', textTransform: 'uppercase',
                      color: MARKA.naCiemnymDrugi }}>
            PCTP Koszalin
          </p>
        </div>
      </div>

    </AbsoluteFill>
  );
};
