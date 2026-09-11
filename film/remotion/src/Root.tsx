import React from 'react';
import {Composition, staticFile} from 'remotion';
import {getAudioDurationInSeconds} from '@remotion/media-utils';
import {Film, type Props} from './Film';

const FPS = 30;

async function istnieje(nazwa: string): Promise<boolean> {
  try {
    const r = await fetch(staticFile(nazwa), {method: 'HEAD'});
    return r.ok;
  } catch {
    return false;
  }
}

/** Suma czasów scen wpisanych w film HTML (gdy nie ma nagrania). */
async function czasScenZHtml(): Promise<number> {
  const html = await (await fetch(staticFile('ocena_funkcjonalna_film.html'))).text();
  const m = html.match(/window\.__SCENY__ = (\[.*?\]);\n/s);
  if (!m) return 285;
  const sceny = JSON.parse(m[1]) as {dur: number}[];
  return sceny.reduce((a, s) => a + s.dur, 0);
}

/**
 * Długość filmu = długość MP3 z ElevenLabs (Twój głos). Bez MP3 render trwa tyle, ile sceny
 * w HTML, ale zgodnie z zasadą skilla film bez Twojego głosu nie jest materiałem do oddania —
 * służy tylko do podglądu układu.
 */
export const RemotionRoot: React.FC = () => (
  <Composition
    id="OcenaFunkcjonalna"
    component={Film}
    durationInFrames={285 * FPS}
    fps={FPS}
    width={1920}
    height={1080}
    defaultProps={{audio: null, awatar: null, srt: null, sekundy: 285} as Props}
    calculateMetadata={async () => {
      const [maAudio, maAwatar, maSrt] = await Promise.all([
        istnieje('narracja.mp3'),
        istnieje('awatar.mp4'),
        istnieje('napisy.srt'),
      ]);
      let sekundy = await czasScenZHtml();
      if (maAudio) {
        try {
          sekundy = await getAudioDurationInSeconds(staticFile('narracja.mp3'));
        } catch {
          // zostaje długość scen
        }
      }
      return {
        durationInFrames: Math.max(1, Math.round(sekundy * FPS)),
        props: {
          audio: maAudio ? 'narracja.mp3' : null,
          awatar: maAwatar ? 'awatar.mp4' : null,
          srt: maSrt ? 'napisy.srt' : null,
          sekundy,
        },
      };
    }}
  />
);
