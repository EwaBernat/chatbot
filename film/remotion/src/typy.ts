export type Slupek = {
  etykieta: string;
  wartosc: number;
};

/** Pole wypełniane na obrazie druku. Współrzędne w pikselach obrazu źródłowego. */
export type PoleDruku = {
  x: number;
  y: number;
  szer: number;
  wys: number;
  /** tekst wpisywany znak po znaku; dla 'kolko' i 'ptaszek' może być pusty */
  tekst?: string;
  /** 'tekst' (domyślnie) · 'kolko' — zakreślenie oceny · 'ptaszek' — zaznaczenie pola */
  rodzaj?: 'tekst' | 'kolko' | 'ptaszek';
  /** sekundy od początku sceny */
  odSek: number;
  doSek?: number;
  rozmiar?: number;
};

export type Kadr = {x: number; y: number; szer: number; wys: number};

export type Scena =
  | {typ: 'tytul'; odSek: number; doSek: number; tytul: string; podtytul?: string; nadtytul?: string}
  | {typ: 'liczba'; odSek: number; doSek: number; wartosc: string; opis: string; kontekst?: string}
  | {typ: 'wykres'; odSek: number; doSek: number; tytul: string; jednostka?: string;
     slupki: Slupek[]; wyroznij?: string; maks?: number}
  | {typ: 'wniosek'; odSek: number; doSek: number; tekst: string}
  | {typ: 'ilustracja'; odSek: number; doSek: number; obraz: string; tytul?: string; podpis?: string}
  | {typ: 'przepis'; odSek: number; doSek: number; etykieta?: string; tytul: string;
     sygnatura: string; status?: string; data?: string; uwaga?: string}
  | {typ: 'porownanie'; odSek: number; doSek: number; tytul: string;
     naglowki?: [string, string]; bylo: string[]; jest: string[]}
  | {typ: 'sciezka'; odSek: number; doSek: number; tytul?: string; przystanki: string[]; aktywny?: number}
  | {typ: 'druk'; odSek: number; doSek: number; obraz: string; szerObrazu: number; wysObrazu: number;
     kadr: Kadr; pola: PoleDruku[]; etykieta?: string}
  | {typ: 'profil'; odSek: number; doSek: number; tytul: string;
     obszary: {kod: string; nazwa: string; wartosc: number | null}[]; wynik?: number}
  | {typ: 'celSmart'; odSek: number; doSek: number; przed: string; po: string}
  | {typ: 'lista'; odSek: number; doSek: number; tytul: string; punkty: string[]; numerowana?: boolean};

export type Film = {
  id: string;
  tytul: string;
  modul: string;
  audio?: string;
  napisy?: string;
  stopka?: string;
  sceny: Scena[];
};
