export type Scena = {
  id: 'intro' | 'ekran' | 'druk1' | 'druk2' | 'druk3' | 'druk4' | 'final';
  odSek: number;
  doSek: number;
  /** Sekundy nagrania (bezwzględne), w których pada fraza sterująca animacją. */
  znaczniki: Record<string, number>;
};

export type Napis = {odSek: number; doSek: number; tekst: string};

export type Film = {
  audio: string;
  napisy: Napis[];
  sceny: Scena[];
};

/** Znaczniki przeliczone na klatki lokalne sceny. */
export type Z = Record<string, number>;
