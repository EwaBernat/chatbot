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
// Widz musi zdążyć przeczytać slajd, a nie tylko wysłuchać lektora. Slajdy tego cyklu
// mają po 140–240 słów; przy cichym czytaniu ok. 5 słów na sekundę daje to 28–48 s,
// co jest za dużo na film — zakładamy więc, że widz skanuje slajd, nie czyta go w całości:
// liczymy 7 słów na sekundę i doliczamy 1,8 s na złapanie układu strony.
const TEMPO_SKANOWANIA = 7.0;
const NA_UKLAD = 1.8;
const MAX_DODATKU = 9;       // ile najwyżej dokładamy ponad ścieżkę lektorską

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
  // liczba słów widocznych na każdym slajdzie prezentacji (jeśli policzona)
  const plikGestosci = join(KATALOG, 'src', 'dane', `gestosc-${nazwa}.json`);
  const gestosc = existsSync(plikGestosci) ? JSON.parse(readFileSync(plikGestosci, 'utf8')) : null;
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

    // przedłużenie ekspozycji: slajd zostaje na ekranie, aż da się go objąć wzrokiem
    const naEkranie = gestosc?.[odcinki.length];
    if (naEkranie) {
      const doPrzeczytania = naEkranie / TEMPO_SKANOWANIA + NA_UKLAD;
      sekundy = Math.min(Math.max(sekundy, doPrzeczytania), sekundy + MAX_DODATKU);
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
