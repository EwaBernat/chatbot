/** Identyfikacja wizualna EduPlaner 2026 / PCTP Koszalin. */
export const MARKA = {
  fiolet: '#2D1B69',
  fioletCiemny: '#1a0f42',
  fioletJasny: '#5B3FA8',
  pomarancz: '#E8450A',
  bialy: '#FFFFFF',
  kosc: '#FCFCFB',
  lawenda: '#F3EEFF',
  tekstDrugi: '#5C5470',
  cien: 'rgba(26, 15, 66, 0.28)',
} as const;

export const FONT =
  'Arial, "Helvetica Neue", Helvetica, "Segoe UI", system-ui, sans-serif';

/** Tło-gradient marki, delikatnie przesuwane w czasie. */
export const gradient = (przesuniecie: number) =>
  `linear-gradient(${125 + przesuniecie}deg, ${MARKA.fiolet} 0%, ${MARKA.fioletCiemny} 55%, #150c36 100%)`;
