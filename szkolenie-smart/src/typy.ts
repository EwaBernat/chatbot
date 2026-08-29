import type {Rozdzial} from './marka';

/** Jeden wiersz napisów: początek i koniec w sekundach od startu filmu. */
export type Napis = {
  od: number;
  do: number;
  tekst: string;
};

/** Wspólne pola każdej sceny. `sekundy` liczone są z długości narracji. */
type Baza = {
  id: string;
  rozdzial: Rozdzial;
  naglowek: string;
  sekundy: number;
};

export type Scena =
  | (Baza & {typ: 'tytul'; podtytul: string; autor: string; odznaki: string[]})
  | (Baza & {
      typ: 'porownanie';
      zle: {etykieta: string; tekst: string; komentarz: string};
      dobre: {etykieta: string; tekst: string; komentarz: string};
    })
  | (Baza & {
      typ: 'litera';
      litera: string;
      nazwa: string;
      angielskie: string;
      pytanie: string;
      praktyka: string;
      pulapka: string;
    })
  | (Baza & {typ: 'kroki'; kroki: {numer: number; tytul: string; opis: string}[]})
  | (Baza & {typ: 'formula'; pola: {numer: number; etykieta: string}[]; zdanie: {tekst: string; pole?: number}[]})
  | (Baza & {typ: 'czasowniki'; dobre: string[]; zle: string[]; naprawa: string})
  | (Baza & {typ: 'termometr'; strefy: {od: number; do: number; nazwa: string; opis: string}[]; karta: boolean[]})
  | (Baza & {typ: 'obszary'; obszary: {nazwa: string; opis: string}[]; stopka: string})
  | (Baza & {typ: 'swiatla'; swiatla: {kolor: 'zielony' | 'zolty' | 'czerwony'; wynik: string; decyzja: string; ruch: string}[]})
  | (Baza & {typ: 'lista'; punkty: {etykieta: string; tekst: string}[]; stopka?: string})
  | (Baza & {typ: 'zakonczenie'; haslo: string; kontakt: {etykieta: string; wartosc: string}[]});

export type Scenariusz = {
  tytul: string;
  fps: number;
  audio: string | null;
  awatar: string | null;
  sceny: Scena[];
  napisy: Napis[];
};
