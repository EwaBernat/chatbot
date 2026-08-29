import {interpolate, spring} from 'remotion';

/**
 * Jedno wejście elementu: przesunięcie w górę plus rozjaśnienie.
 * `opoznienie` podajemy w sekundach, żeby kolejność wejść dało się czytać
 * wprost ze sceny, bez przeliczania na klatki.
 */
export const wejscie = (
  frame: number,
  fps: number,
  opoznienie = 0,
  dystans = 24
) => {
  const s = spring({
    frame: frame - opoznienie * fps,
    fps,
    config: {damping: 200, mass: 0.6},
    durationInFrames: Math.round(fps * 0.7),
  });
  return {
    opacity: s,
    transform: `translateY(${(1 - s) * dystans}px)`,
  };
};

/** Wartość rosnąca od 0 do 1 w zadanym oknie sekund — do pasków i skal. */
export const postep = (
  frame: number,
  fps: number,
  odSekundy: number,
  trwanie: number
) =>
  interpolate(frame / fps, [odSekundy, odSekundy + trwanie], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
