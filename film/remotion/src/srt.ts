export type Napis = {odSek: number; doSek: number; tekst: string};

const CZAS = /(\d{2}):(\d{2}):(\d{2})[,.](\d{3})/g;

/** Parsuje SRT wygenerowany przez elevenlabs_tts.py --srt. */
export const parsujSrt = (surowe: string): Napis[] => {
  const napisy: Napis[] = [];
  for (const blok of surowe.replace(/\r\n/g, '\n').trim().split(/\n\s*\n/)) {
    const linie = blok.split('\n').filter((l) => l.trim() !== '');
    if (linie.length < 2) continue;
    const linijkaCzasu = linie.find((l) => l.includes('-->'));
    if (!linijkaCzasu) continue;
    const znaczniki = [...linijkaCzasu.matchAll(CZAS)];
    if (znaczniki.length < 2) continue;
    const naSekundy = (m: RegExpMatchArray) =>
      Number(m[1]) * 3600 + Number(m[2]) * 60 + Number(m[3]) + Number(m[4]) / 1000;
    const tekst = linie
      .slice(linie.indexOf(linijkaCzasu) + 1)
      .join(' ')
      .trim();
    if (tekst) {
      napisy.push({odSek: naSekundy(znaczniki[0]), doSek: naSekundy(znaczniki[1]), tekst});
    }
  }
  return napisy;
};
