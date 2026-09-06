// Kształt scenariusza — jeden plik JSON opisuje cały moduł filmu.

export type Scena =
  | { typ: 'czolowka'; tytul: string; podtytul: string; czesci: string[] }
  | { typ: 'tytulModulu'; numer: string; tytul: string; podtytul: string; czas: string }
  | { typ: 'punkty'; naglowek: string; nadtytul?: string; punkty: string[] }
  | { typ: 'cytat'; naglowek: string; tresc: string; zrodlo: string }
  | { typ: 'tabela'; naglowek: string; nadtytul?: string; naglowki: string[]; wiersze: string[][]; szerokosci?: number[] }
  | { typ: 'druk'; naglowek: string; nadtytul?: string; plik: string; opis?: string; kadrowanie?: { x: number; y: number; skala: number } }
  | { typ: 'sciezki'; naglowek: string; lewa: { tytul: string; kroki: string[] }; prawa: { tytul: string; kroki: string[] } }
  | { typ: 'obieg'; naglowek: string; przystanki: { nazwa: string; opis: string }[] }
  | { typ: 'domkniecie'; naglowek: string; zdania: string[] };

export type Ujecie = {
  id: string;
  scena: Scena;
  /** Tekst czysty — napisy i transkrypcja. */
  narracja: string;
  /** Tekst ze wskazówkami aktorskimi — wyłącznie do ElevenLabs. */
  narracjaTts?: string;
  /** Zmierzona długość nagrania w sekundach; bez nagrania liczona z tempa 107 słów/min. */
  sekundy: number;
  /** Nazwa pliku MP3 w public/glos, jeśli nagranie już jest. */
  glos?: string;
};

export type Modul = {
  id: string;
  numer: string;
  tytul: string;
  podtytul: string;
  ujecia: Ujecie[];
};
