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

export type Film = {
  tytul: string;
  audio?: string;      // nazwa pliku w public/, np. "narracja.mp3"
  napisy?: string;     // nazwa pliku w public/, np. "napisy.srt"
  stopka?: string;
  sceny: Scena[];
};
