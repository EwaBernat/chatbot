// Marka PCTP / EduPlaner 2026 — jedno miejsce z kolorami, krojem i miarami kadru.

export const KOLOR = {
  fiolet: '#2D1B69',
  fioletJasny: '#5B4A9E',
  pomarancz: '#E8450C',
  pomaranczJasny: '#F98A5B',
  atrament: '#2B2733',
  szary: '#6E6880',
  szaryJasny: '#968B9F',
  tlo: '#FCFCFA',
  tloCieple: '#F7F3EE',
  kartka: '#FFFFFF',
  wypelnienie: '#F2F0F7',
  wypelnienie2: '#F7F6FA',
  ramka: '#D6D1E4',
  zaznaczenie: 'rgba(232, 69, 12, 0.20)',
  zielony: '#2E7D5B',
} as const;

export const KROJ = "'Liberation Sans', Arial, Helvetica, sans-serif";

// Kadr 1920x1080 — te same marginesy w każdej scenie, żeby tytuły nie skakały.
export const KADR = {
  szerokosc: 1920,
  wysokosc: 1080,
  margines: 150,
  gornyPasek: 8,
  pasekNapisowGora: 858,
  pasekNapisowWysokosc: 120,
} as const;

export const FPS = 30;
