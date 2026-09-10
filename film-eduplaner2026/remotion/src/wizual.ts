/**
 * Parametry wizualne scen — „notatki reżyserskie" przełożone na liczby.
 * Treść i czasy scen mieszkają w ../../scenariusz.json (jedno źródło prawdy),
 * a tutaj jest tylko to, co musi być precyzyjne dla animacji.
 */

export type Dymek = {
  /** sekunda od początku SCENY, w której pojawia się dymek */
  t: number;
  tekst: string;
  /** pozycja w kadrze, 0–1 */
  x: number;
  y: number;
};

export type KenBurns = {
  odSkali: number;
  doSkali: number;
  /** przesunięcie kadru w procentach wysokości/szerokości obrazu */
  odY?: number;
  doY?: number;
  odX?: number;
  doX?: number;
};

export type WizualScena = {
  /** ken burns dla kolejnych zrzutów sceny */
  kadry?: KenBurns[];
  /** układ scen typu „kartkowanie": talia kart albo wachlarz */
  uklad?: 'talia' | 'wachlarz';
  /** numer strony (1-based), na której scena kończy zbliżeniem */
  stronaFinalowa?: number;
  dymki?: Dymek[];
  /** tekst wpisywany „na maszynie" (efekt pisania) */
  maszyna?: { t: number; tekst: string };
  /** hasła wskakujące od dołu */
  hasla?: { t: number; slowa: string[] };
  /** treść pigułek przelatujących z modułu do druku (scena IPET) */
  pigulki?: string[];
  kontra?: string;
};

export const WIZUAL: Record<string, WizualScena> = {
  'wopf-karta': {
    // pierwszy zrzut prawie bez ruchu, żeby dymki trafiały w realne rzędy wyboru
    kadry: [
      { odSkali: 1.02, doSkali: 1.06 },
      // drugi zrzut: mocniejsze zbliżenie, bo treść aplikacji siedzi w wąskiej kolumnie
      { odSkali: 1.3, doSkali: 1.45, odY: 2, doY: 8 },
    ],
    dymki: [
      { t: 2, tekst: '1 — osoba obserwująca', x: 0.6, y: 0.66 },
      { t: 4.2, tekst: '2 — miejsce obserwacji', x: 0.66, y: 0.775 },
      { t: 6.4, tekst: '3 — narzędzie: KSzOF · ABC · ToM · Sensoryka', x: 0.45, y: 0.865 },
    ],
  },
  'cele-smart': {
    kadry: [
      { odSkali: 1.02, doSkali: 1.12, odY: 0, doY: 6 },
      { odSkali: 1.1, doSkali: 1.0, odX: 6, doX: -2 },
      { odSkali: 1.0, doSkali: 1.08, odY: 2, doY: 8 },
    ],
    kontra: 'program ucznia składa się sam',
  },
  'ipet-zywy': {
    pigulki: [
      'Uczeń samodzielnie rozwiąże 2 zadania na lekcji — w 8 na 10 prób',
      'Uczeń zakomunikuje przebodźcowanie „Kartą Przerwy" — w 8 na 10 sytuacji',
      'Uczeń zgłosi chęć odpowiedzi przez podniesienie ręki — w 4 na 5 prób',
    ],
  },
  baza: {
    // pierwszy kadr startuje na jednym wierszu rejestru i odjeżdża do całej tabeli
    kadry: [
      { odSkali: 2.0, doSkali: 1.0, odX: 15, doX: 0, odY: 17, doY: 0 },
      { odSkali: 1.0, doSkali: 1.08 },
      { odSkali: 1.0, doSkali: 1.06 },
    ],
    kontra: 'pomoce i materiały pod ręką',
  },
  'ewaluacja-otwartosc': {
    kadry: [
      { odSkali: 1.04, doSkali: 1.04, odY: -6, doY: 10 },
      { odSkali: 1.06, doSkali: 1.0 },
      { odSkali: 1.0, doSkali: 1.08 },
    ],
    maszyna: { t: 9.5, tekst: 'Uczeń poprosi o przerwę sensoryczną, gdy…' },
    hasla: { t: 15, slowa: ['Dodawaj', 'Modyfikuj', 'Proponuj'] },
  },
  raport: { uklad: 'wachlarz', stronaFinalowa: 2, kontra: '5 stron zamiast 30' },
  'wopf-druk': { uklad: 'talia', stronaFinalowa: 5, kontra: 'gotowe, bez przepisywania' },
};

/** Domyślny, spokojny ken burns dla zrzutu bez własnych parametrów. */
export const KADR_DOMYSLNY: KenBurns = { odSkali: 1.0, doSkali: 1.06, odY: 0, doY: 3 };
