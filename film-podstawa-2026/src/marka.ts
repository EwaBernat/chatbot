/**
 * Marka PCTP w wersji na ekran.
 *
 * Paleta pochodzi ze stałej BRAND w ipet_data.js (fiolet #2D1B69, pomarańcz
 * #E8450A) i z walidacji dostępności ze skilla dane-i-glos: ciemny fiolet
 * niesie TEKST, jaśniejszy krok tego samego odcienia niesie WYPEŁNIENIA,
 * a pomarańcz jest zarezerwowany dla rzeczy wymagającej uwagi. Na filmie
 * dochodzi warstwa ciemna — plansze na tle sali — więc obok każdego koloru
 * jest jego odpowiednik na ciemnym tle.
 */
export const MARKA = {
  fiolet: '#2D1B69',
  fioletCiemny: '#1F1148',
  fioletJasny: '#5B3FA8',
  pomarancz: '#E8450A',
  pomaranczJasny: '#FFB48C',

  zielen: '#0D7D5C',
  bursztyn: '#C47A10',
  czerwien: '#B8350D',
  turkus: '#2B6E6E',

  tekst: '#1A1A2E',
  tekstDrugi: '#5B5B72',
  linia: '#D9D5E8',
  papier: '#F4F2FA',
  biel: '#FFFFFF',

  // na ciemnym tle
  naCiemnym: '#F1EBFF',
  naCiemnymDrugi: '#B7A9DC',
} as const;

/** Kolory dziewięciu obszarów — tinty jednego odcienia, żeby nie kolidowały
 *  ze znaczeniem zieleni, bursztynu i czerwieni (poziomy realizacji celu). */
export const OBSZARY_KOLOR: Record<string, string> = {
  spoleczny: '#5B3FA8',
  osobisty: '#7A4FB5',
  jezykowy: '#4A46A8',
  matematyczny: '#3E5AA8',
  przyrodniczy: '#2F6F8C',
  techniczny: '#6B4A9E',
  cyfrowy: '#45409C',
  artystyczny: '#8B4AA0',
  ruchowy: '#5A3E92',
};

export const FONT_NAGLOWEK =
  '"Sofia Sans Condensed", "Arial Narrow", Arial, system-ui, sans-serif';
export const FONT_TEKST =
  'Lato, Arial, "Helvetica Neue", system-ui, sans-serif';
export const FONT_DANE =
  '"IBM Plex Mono", "Consolas", ui-monospace, monospace';
