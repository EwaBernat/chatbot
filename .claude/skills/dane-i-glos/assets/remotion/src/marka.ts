/**
 * Paleta marki PCTP, sprawdzona walidatorem dostępności kolorów.
 *
 * Wynik walidacji (tryb jasny, powierzchnia #FCFCFB):
 *   #2D1B69 jako wypełnienie — FAIL (jasność 0.30, poza pasmem 0.43–0.77),
 *   #5B3FA8 jako wypełnienie — PASS wszystkich sześciu testów,
 *   para #5B3FA8 / #E8450A — separacja dla protanopii ΔE 26,4; dla widzenia
 *   normalnego ΔE 33,7; kontrast wobec tła powyżej 3:1.
 *
 * Stąd podział ról: ciemny fiolet marki niesie TEKST, jaśniejszy krok tego
 * samego odcienia niesie SŁUPKI, a pomarańcz jest zarezerwowany wyłącznie dla
 * wartości wymagającej uwagi. Pomarańcza nie używamy jako „kolejnej serii".
 */
export const MARKA = {
  tekst: '#2D1B69',        // nagłówki i liczby — ciemny fiolet PCTP
  tekstDrugi: '#5C5470',   // podpisy, kontekst
  tekstCichy: '#8A83A0',   // osie, jednostki
  slupek: '#5B3FA8',       // wypełnienie słupków (jeden odcień, jedna seria)
  wyroznienie: '#E8450A',  // pomarańcz PCTP — tylko wartość wymagająca uwagi
  tlo: '#FCFCFB',
  tloDrugie: '#F3F1F8',    // tło toru słupka
  siatka: '#E4E0EE',
} as const;

export const FONT =
  'Arial, "Helvetica Neue", Helvetica, "Segoe UI", system-ui, sans-serif';
