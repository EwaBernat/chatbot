/* Dane kontaktowe PCTP — wspólne dla wszystkich generatorów.
 *
 * UWAGA: numer telefonu jest automatycznie usuwany z plików tekstowych
 * przy wypychaniu do repozytorium (ochrona danych osobowych po stronie
 * platformy). Dlatego NIE zapisujemy go w kodzie — podaje się go przy
 * budowaniu, zmienną środowiskową:
 *
 *     PCTP_TELEFON="000 000 000" node generuj.js
 *
 * Bez zmiennej w dokumencie pojawia się widoczny znacznik [ telefon ],
 * tak samo jak [ cena ] — od razu widać, że coś zostało do uzupełnienia.
 * Pliki PDF, DOCX i XLSX nie są czyszczone, więc raz zbudowany dokument
 * zachowuje numer.
 */

const TELEFON = process.env.PCTP_TELEFON || "[ telefon ]";

module.exports = {
  TELEFON,
  AUTORKA: "Mirosława Ewa Jurczyszyn",
  ROLA: "pedagog specjalny",
  WYDAWCA: "Pomorskie Centrum Terapii Pedagogicznej, Koszalin",
  EMAIL: "kontakt@eduplaner2026.pl",
  WWW: "www.eduplaner2026.pl",
  /* jedna linijka stopki: e-mail · telefon · strona */
  linia: () => `kontakt@eduplaner2026.pl · ${TELEFON} · www.eduplaner2026.pl`,
};
