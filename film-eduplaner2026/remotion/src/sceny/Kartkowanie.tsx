import React from 'react';
import { Img, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';
import { FONT, MARKA } from '../marka';
import { Licznik, Podpis, Tlo, Znak, ZnakDanePrzykladowe } from '../ui/Chrome';
import { WIZUAL } from '../wizual';
import type { Scena } from '../typy';

const WYSOKOSC_STRONY = 760; // px w kadrze 1080p (A4 → szerokość ~537 px)

/**
 * Scena typu „kartkowanie": prawdziwe strony A4 druku wjeżdżają jedna po drugiej
 * (talia kart albo wachlarz), a na koniec scena zbliża wybraną stronę.
 */
export const Kartkowanie: React.FC<{ scena: Scena; znakDanePrzykladowe: boolean }> = ({
  scena,
  znakDanePrzykladowe,
}) => {
  const f = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const w = WIZUAL[scena.id] ?? {};
  const uklad = w.uklad ?? 'talia';
  const strony = scena.zrzuty;

  const koniecUkladania = Math.round(durationInFrames * 0.62);
  const naStrone = koniecUkladania / Math.max(1, strony.length);
  const wybrana = Math.min(strony.length, Math.max(1, w.stronaFinalowa ?? 1)) - 1;

  // b = 0 podczas układania, 1 na końcu (złożony stos + zbliżenie)
  const b = interpolate(f, [koniecUkladania, durationInFrames - 6], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <Tlo>
      <div style={{ position: 'absolute', inset: 0, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        {strony.map((plik, i) => {
          const start = Math.round(i * naStrone);
          const s = spring({
            frame: f - start,
            fps,
            config: { damping: 18, mass: 0.7 },
            durationInFrames: 26,
          });

          // pozycja docelowa w fazie układania
          const rozstaw =
            uklad === 'wachlarz'
              ? interpolate(i, [0, Math.max(1, strony.length - 1)], [-330, 330])
              : i * 26 - (strony.length - 1) * 13;
          const obrot =
            uklad === 'wachlarz'
              ? interpolate(i, [0, Math.max(1, strony.length - 1)], [-8, 8])
              : (i % 2 === 0 ? -1.6 : 1.6);

          const xUklad = interpolate(s, [0, 1], [920, rozstaw]);
          const yUklad = interpolate(s, [0, 1], [40, uklad === 'wachlarz' ? 0 : i * 4]);
          const rUklad = interpolate(s, [0, 1], [10, obrot]);

          // pozycja docelowa w fazie zbliżenia
          const wybor = i === wybrana;
          const xFinal = 0;
          const yFinal = wybor ? 0 : 120;
          const rFinal = 0;
          const skalaFinal = wybor ? 1.32 : 0.94;

          const x = interpolate(b, [0, 1], [xUklad, xFinal]);
          const y = interpolate(b, [0, 1], [yUklad, yFinal]);
          const r = interpolate(b, [0, 1], [rUklad, rFinal]);
          const skala = interpolate(b, [0, 1], [1, skalaFinal]);
          const krycie = wybor ? s : Math.min(s, interpolate(b, [0, 0.7], [1, 0], { extrapolateRight: 'clamp' }));

          return (
            <div
              key={plik}
              style={{
                position: 'absolute',
                height: WYSOKOSC_STRONY,
                opacity: krycie,
                transform: `translate(${x}px, ${y}px) rotate(${r}deg) scale(${skala})`,
                boxShadow: `0 26px 60px ${MARKA.cien}`,
                borderRadius: 3,
                overflow: 'hidden',
                background: MARKA.bialy,
                zIndex: wybor ? 50 : i,
              }}
            >
              <Img src={staticFile(`zrzuty/${plik}`)} style={{ height: '100%', display: 'block' }} />
            </div>
          );
        })}
      </div>

      <Znak />
      {scena.licznik ? (
        <Licznik do={scena.licznik.do} opis={scena.licznik.opis} klatekNabijania={koniecUkladania} />
      ) : null}
      {scena.podpis ? <Podpis tekst={scena.podpis} /> : null}

      {w.kontra ? (
        <div
          style={{
            position: 'absolute',
            left: 56,
            top: '30%',
            fontFamily: FONT,
            fontSize: 46,
            fontWeight: 700,
            color: MARKA.bialy,
            maxWidth: 420,
            lineHeight: 1.2,
            opacity: interpolate(f, [koniecUkladania, koniecUkladania + fps], [0, 1], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            }),
          }}
        >
          {w.kontra}
        </div>
      ) : null}

      {znakDanePrzykladowe ? <ZnakDanePrzykladowe /> : null}
    </Tlo>
  );
};
