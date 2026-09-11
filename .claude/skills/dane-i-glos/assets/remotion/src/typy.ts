export type Slupek = {
  etykieta: string;
  wartosc: number;
};

export type Scena =
  | {typ: 'tytul'; odSek: number; doSek: number; tytul: string; podtytul?: string}
  | {typ: 'liczba'; odSek: number; doSek: number; wartosc: string; opis: string;
     kontekst?: string}
  | {typ: 'wykres'; odSek: number; doSek: number; tytul: string; jednostka?: string;
     slupki: Slupek[]; wyroznij?: string; maks?: number}
  | {typ: 'wniosek'; odSek: number; doSek: number; tekst: string};

export type UkladAwatara = 'pelny' | 'rog' | 'lewa' | 'prawa';

/** Postać Ewa PCTP (skill awatar-ewa-pctp): klip WebM z alfą w public/. */
export type Awatar = {
  plik: string;            // np. "ewa.webm" — VP9 z kanałem alfa
  uklad?: UkladAwatara;    // domyślnie pelny
  odSek?: number;          // od kiedy widać Ewę (domyślnie 0)
  doSek?: number;          // do kiedy (domyślnie do końca klipu)
  skala?: number;          // wysokość Ewy jako ułamek wysokości kadru (domyślnie wg układu)
  margines?: number;       // odstęp od krawędzi w px (domyślnie 48)
  dzwiek?: boolean;        // false = wycisz klip (gdy głos idzie z film.audio)
};

export type Film = {
  tytul: string;
  audio?: string;      // nazwa pliku w public/, np. "narracja.mp3"
  napisy?: string;     // nazwa pliku w public/, np. "napisy.srt"
  stopka?: string;
  awatar?: Awatar | Awatar[];   // Ewa w jednym miejscu albo w kilku odcinkach filmu
  sceny: Scena[];
};
