import dane from '../../scenariusz.json';
import type { Scenariusz } from './typy';

export const SCENARIUSZ = dane as unknown as Scenariusz;

/** Długość filmu w klatkach — wyliczona z ostatniej sceny scenariusza. */
export const dlugoscWKlatkach = () => {
  const ostatnia = SCENARIUSZ.sceny[SCENARIUSZ.sceny.length - 1];
  return Math.round((ostatnia.od + ostatnia.czas) * SCENARIUSZ.fps);
};
