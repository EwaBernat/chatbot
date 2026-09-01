export type Scena = {
  nr: number;
  tytul: string;
  typ: 'intro' | 'fakt' | 'prawo' | 'konstrukcja' | 'przejscie' | 'obszar'
     | 'filary' | 'praktyka' | 'arkusz' | 'koniec';
  sekundy: number;
  slowa: number;
  zdania: string[];
  klucz?: string;
  nrObszaru?: number;
  znak?: string;
  podpis?: string;
};

export type Film = {
  fps: number;
  szerokosc: number;
  wysokosc: number;
  audio: string;
  napisy: string;
  lacznieSekund: number;
  sceny: Scena[];
};
