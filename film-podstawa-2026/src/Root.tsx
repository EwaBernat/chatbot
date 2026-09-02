import React from 'react';
import { Composition, staticFile, getStaticFiles } from 'remotion';
import { Film } from './Film';
import dane from '../public/film.json';
import type { Film as FilmDane } from './typy';

const d = dane as FilmDane;

/** Długość powitania — tyle trwa awatar.webm (13,04 s po wycięciu tła
 *  z nagrania HeyGen). O tyle przesuwa się cała narracja lektorska. */
const POWITANIE_SEKUND = 13.04;

/** public/ decyduje o tym, czego film użyje: gdy nagranie i awatar są na
 *  miejscu, wchodzą do montażu; gdy ich nie ma, film i tak się składa. */
const maPlik = (nazwa: string) =>
  getStaticFiles().some((p) => p.name === nazwa);

export const RemotionRoot: React.FC = () => {
  const jestAudio = maPlik(d.audio);
  const jestAwatar = maPlik('awatar.webm');
  /** Awatar zsynchronizowany z narracja.mp3 — usta idą wtedy za lektorem.
   *  Dwa źródła, dwa kształty kadru:
   *    awatar-lektor-kolo.mp4 — lipsync z ElevenLabs, gotowy kwadrat pod koło;
   *    awatar-lektor.mp4      — HeyGen, pełna klatka jak awatar.webm.
   *  Gdy nie ma żadnego, w kółeczku jest nieruchoma sylwetka. */
  const awatarKolo = maPlik('awatar-lektor-kolo.mp4');
  const awatarMowiacy = awatarKolo
    ? 'awatar-lektor-kolo.mp4'
    : ['awatar-lektor.webm', 'awatar-lektor.mp4'].find(maPlik);
  const awatarKadr: 'pelny' | 'kolo' = awatarKolo ? 'kolo' : 'pelny';
  const powitanieKlatek = jestAwatar ? Math.round(POWITANIE_SEKUND * d.fps) : 0;
  const [napisySrt, setNapisySrt] = React.useState<string | undefined>();

  React.useEffect(() => {
    if (!maPlik(d.napisy)) return;
    fetch(staticFile(d.napisy)).then((r) => r.text()).then(setNapisySrt).catch(() => undefined);
  }, []);

  return (
    <Composition
      id="Film"
      component={Film}
      durationInFrames={powitanieKlatek + Math.round(d.lacznieSekund * d.fps)}
      fps={d.fps}
      width={d.szerokosc}
      height={d.wysokosc}
      defaultProps={{ dane: d, jestAudio, jestAwatar, napisySrt, powitanieKlatek, awatarMowiacy, awatarKadr }}
    />
  );
};
