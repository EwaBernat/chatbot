/**
 * Paleta PCTP / EduPlaner 2026 dla szkolenia „Cele SMART w przedszkolu".
 *
 * Role kolorów przeniesione z palety skilla `dane-i-glos` (przeszła sześć testów
 * dostępności) i rozszerzone o barwy potrzebne w szkoleniu:
 *   - ciemny fiolet #2D1B69 niesie TEKST i tło panelu awatara, nigdy dużych
 *     wypełnień pod drobnym tekstem,
 *   - jaśniejszy krok tego samego odcienia #5B3FA8 niesie wypełnienia i akcenty,
 *   - pomarańcz #E8450A jest zarezerwowany dla tego, co wymaga uwagi:
 *     pułapki, błędnego zapisu, strefy czerwonej. Nie używamy go jako ozdoby.
 * Zielony i żółty pojawiają się wyłącznie w scenie sygnalizacji i termometru,
 * gdzie kolor jest treścią, a nie dekoracją — i zawsze mają podpis słowny.
 */
export const MARKA = {
  tekst: '#2D1B69',
  tekstDrugi: '#5C5470',
  tekstCichy: '#8A83A0',
  akcent: '#5B3FA8',
  akcentJasny: '#7C5FD3',
  wyroznienie: '#E8450A',
  tlo: '#FCFCFB',
  tloDrugie: '#F3F1F8',
  tloTrzecie: '#EBE7F5',
  siatka: '#E4E0EE',
  bialy: '#FFFFFF',
  zielony: '#1E7A4A',
  zielonyTlo: '#E4F4EB',
  zolty: '#A9720B',
  zoltyTlo: '#FBF0DA',
  czerwony: '#C0361B',
  czerwonyTlo: '#FBE7E1',
} as const;

export const FONT =
  'Arial, "Helvetica Neue", Helvetica, "Segoe UI", system-ui, sans-serif';

/** Kolejność sekcji broszury — steruje paskiem postępu u góry ekranu. */
export const ROZDZIALY = [
  'Wstęp',
  'Po co',
  'Anatomia',
  'Skrypt',
  'Formuła',
  'Słownik',
  'Wzorzec',
  'Bank celów',
  'Ewaluacja',
  'Prawo',
] as const;

export type Rozdzial = (typeof ROZDZIALY)[number];
