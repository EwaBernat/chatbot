import React from 'react';
import { Composition, staticFile, getStaticFiles } from 'remotion';
import { Film } from './Film';
import dane from '../public/film.json';
import type { Film as FilmDane } from './typy';

const d = dane as FilmDane;

/** public/ decyduje o tym, czego film użyje: gdy nagranie i awatar są na
 *  miejscu, wchodzą do montażu; gdy ich nie ma, film i tak się składa. */
const maPlik = (nazwa: string) =>
  getStaticFiles().some((p) => p.name === nazwa);

export const RemotionRoot: React.FC = () => {
  const jestAudio = maPlik(d.audio);
  const jestAwatar = maPlik('awatar.mp4');
  const [napisySrt, setNapisySrt] = React.useState<string | undefined>();

  React.useEffect(() => {
    if (!maPlik(d.napisy)) return;
    fetch(staticFile(d.napisy)).then((r) => r.text()).then(setNapisySrt).catch(() => undefined);
  }, []);

  return (
    <Composition
      id="Film"
      component={Film}
      durationInFrames={Math.round(d.lacznieSekund * d.fps)}
      fps={d.fps}
      width={d.szerokosc}
      height={d.wysokosc}
      defaultProps={{ dane: d, jestAudio, jestAwatar, napisySrt }}
    />
  );
};
