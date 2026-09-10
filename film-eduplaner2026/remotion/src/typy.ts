export type TypScene =
  | 'plansza'
  | 'ekran'
  | 'kartkowanie'
  | 'polaczenie'
  | 'lista'
  | 'final';

export type Licznik = { do: number; opis: string };

export type Plansza = {
  nadtytul: string;
  tytul: string;
  haslo: string;
  kontakt?: string[];
};

export type Scena = {
  nr: number;
  id: string;
  tytul: string;
  od: number;
  czas: number;
  typ: TypScene;
  podpis?: string;
  plansza?: Plansza;
  lista?: string[];
  licznik?: Licznik;
  zrzuty: string[];
  animacja: string[];
  narracja: string;
  heygen: string;
};

export type Scenariusz = {
  tytul: string;
  podtytul: string;
  fps: number;
  szerokosc: number;
  wysokosc: number;
  uwaga_o_danych: string;
  sceny: Scena[];
};

/** Props kompozycji — pozwalają podłożyć narrację bez zmiany kodu. */
export type FilmProps = {
  /** Nazwa pliku audio w public/ (np. „narracja.mp3"). Pusty = film bez głosu. */
  glos: string;
  /** Znak wodny „DANE PRZYKŁADOWE" na zrzutach druków. */
  znakDanePrzykladowe: boolean;
};
