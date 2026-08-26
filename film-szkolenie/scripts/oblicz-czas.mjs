/**
 * Wylicza długość każdego slajdu w filmie i zapisuje src/czas.json.
 *
 * Jeśli w public/audio/<czesc>/NN.mp3 (albo .m4a/.wav) leży nagranie, slajd trwa
 * dokładnie tyle, ile nagranie plus krótki oddech. Jeśli nagrania nie ma, długość
 * wynika z liczby słów narracji — dzięki temu film daje się zrenderować także
 * w wersji niemej, a po dograniu głosu wystarczy uruchomić skrypt ponownie.
 */
import {readFileSync, writeFileSync, existsSync} from 'node:fs';
import {dirname, join} from 'node:path';
import {fileURLToPath} from 'node:url';

const KATALOG = join(dirname(fileURLToPath(import.meta.url)), '..');
const FPS = 30;
const ODDECH = 0.9;          // sekundy ciszy po zdaniu lektora
const TEMPO_SLOW = 2.35;     // słów na sekundę przy spokojnym czytaniu
const MIN_SEK = 5;

const rozszerzenia = ['.mp3', '.m4a', '.wav', '.aac', '.ogg'];

const dlugoscAudio = async (sciezka) => {
  try {
    const {parseFile} = await import('music-metadata');
    const dane = await parseFile(sciezka);
    return dane.format.duration ?? null;
  } catch {
    return null;
  }
};

const policz = async (nazwa) => {
  const slajdy = JSON.parse(readFileSync(join(KATALOG, 'src', 'dane', `${nazwa}.json`), 'utf8'));
  const odcinki = [];
  let zAudio = 0;

  for (const slajd of slajdy) {
    let sekundy = null;
    let maAudio = false;

    for (const ext of rozszerzenia) {
      const plik = join(KATALOG, 'public', slajd.audio.replace(/\.mp3$/, ext));
      if (existsSync(plik)) {
        const d = await dlugoscAudio(plik);
        if (d) {
          sekundy = d + ODDECH;
          maAudio = true;
          zAudio++;
          break;
        }
      }
    }

    if (sekundy === null) {
      const slowa = slajd.narracja.trim().split(/\s+/).length;
      sekundy = Math.max(MIN_SEK, slowa / TEMPO_SLOW + ODDECH);
    }

    odcinki.push({klatki: Math.round(sekundy * FPS), maAudio});
  }

  const suma = odcinki.reduce((a, o) => a + o.klatki, 0);
  const minuty = (suma / FPS / 60).toFixed(1);
  console.log(`${nazwa}: ${slajdy.length} slajdów, ${zAudio} z nagraniem, ${minuty} min materiału`);
  return {odcinki, suma};
};

const czas = {
  czesc1: await policz('czesc1'),
  czesc2: await policz('czesc2'),
  rada45: await policz('rada45'),
};

writeFileSync(join(KATALOG, 'src', 'czas.json'), JSON.stringify(czas, null, 1), 'utf8');
console.log('Zapisano src/czas.json');
