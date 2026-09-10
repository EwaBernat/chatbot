import React from 'react';
import { AbsoluteFill, Audio, Sequence, staticFile, useVideoConfig } from 'remotion';
import { SCENARIUSZ } from './scenariusz';
import { EkranAplikacji } from './sceny/EkranAplikacji';
import { Kartkowanie } from './sceny/Kartkowanie';
import { Lista } from './sceny/Lista';
import { Plansza } from './sceny/Plansza';
import { Polaczenie } from './sceny/Polaczenie';
import { PasekPostepu } from './ui/Chrome';
import type { FilmProps, Scena } from './typy';

const Scenka: React.FC<{ scena: Scena; znakDanePrzykladowe: boolean }> = ({
  scena,
  znakDanePrzykladowe,
}) => {
  switch (scena.typ) {
    case 'plansza':
      return <Plansza dane={scena.plansza!} />;
    case 'final':
      return <Plansza dane={scena.plansza!} finalowa />;
    case 'kartkowanie':
      return <Kartkowanie scena={scena} znakDanePrzykladowe={znakDanePrzykladowe} />;
    case 'polaczenie':
      return <Polaczenie scena={scena} znakDanePrzykladowe={znakDanePrzykladowe} />;
    case 'lista':
      return <Lista scena={scena} />;
    case 'ekran':
    default:
      return <EkranAplikacji scena={scena} znakDanePrzykladowe={znakDanePrzykladowe} />;
  }
};

export const Film: React.FC<FilmProps> = ({ glos, znakDanePrzykladowe }) => {
  const { fps, durationInFrames } = useVideoConfig();

  return (
    <AbsoluteFill style={{ background: '#0d0724' }}>
      {glos ? <Audio src={staticFile(glos)} /> : null}

      {SCENARIUSZ.sceny.map((scena) => {
        const od = Math.round(scena.od * fps);
        return (
          <Sequence
            key={scena.id}
            from={od}
            durationInFrames={Math.round(scena.czas * fps)}
            name={`${scena.nr}. ${scena.tytul}`}
          >
            <Scenka scena={scena} znakDanePrzykladowe={znakDanePrzykladowe} />
            <PasekPostepu odKlatki={od} doKlatki={durationInFrames} />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};
