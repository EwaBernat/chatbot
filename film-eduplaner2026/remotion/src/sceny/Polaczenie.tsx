import React from 'react';
import { Img, interpolate, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';
import { FONT, MARKA } from '../marka';
import { Podpis, Tlo, ZnakDanePrzykladowe } from '../ui/Chrome';
import { WIZUAL } from '../wizual';
import type { Scena } from '../typy';

/** Proporcje strony A4 wyrenderowanej z PDF (1191 × 1684 px). */
const A4 = 1191 / 1684;

/**
 * Wiersze tabeli III druku IPET (współrzędne znormalizowane w obrazie strony,
 * zmierzone na druk_IPET_Plan_s03.png):
 * 1 — Uczenie się i stosowanie wiedzy, 3 — Porozumiewanie się, 7 — Edukacja szkolna.
 */
const WIERSZE = [
  { yc: 0.361, x0: 0.085, x1: 0.91, h: 0.052 },
  { yc: 0.4536, x0: 0.085, x1: 0.91, h: 0.052 },
  { yc: 0.638, x0: 0.085, x1: 0.91, h: 0.052 },
];

/** Krzywa Béziera 2. stopnia — łuk, po którym leci pigułka z celem. */
const bezier = (t: number, p0: number, p1: number, p2: number) =>
  (1 - t) * (1 - t) * p0 + 2 * (1 - t) * t * p1 + t * t * p2;

/**
 * Scena typu „połączenie" — serce filmu: cele wybrane w module
 * przelatują na żywo do sekcji III prawdziwego druku IPET.
 */
export const Polaczenie: React.FC<{ scena: Scena; znakDanePrzykladowe: boolean }> = ({
  scena,
  znakDanePrzykladowe,
}) => {
  const f = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const w = WIZUAL[scena.id] ?? {};
  const pigulki = w.pigulki ?? [];

  const [modul, strona] = scena.zrzuty;

  // faza 2: prawa strona rozjeżdża się na cały kadr i zbliża nagłówek sekcji III
  const start2 = Math.round(durationInFrames * 0.74);
  const b = interpolate(f, [start2, durationInFrames - 8], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  // geometria strony A4: od prawej połowy kadru do zbliżenia na nagłówek
  const wysStrony = interpolate(b, [0, 1], [928, 1500]);
  const szerStrony = wysStrony * A4;
  const lewaStrony = interpolate(b, [0, 1], [1112, 477]);
  const gornaStrony = interpolate(b, [0, 1], [76, 135]);

  const pkt = (nx: number, ny: number) => ({
    x: lewaStrony + nx * szerStrony,
    y: gornaStrony + ny * wysStrony,
  });

  return (
    <Tlo>
      {/* LEWA POŁOWA — moduł z celami SMART */}
      <div
        style={{
          position: 'absolute',
          left: 0,
          top: 0,
          width: 960,
          height: 1080,
          overflow: 'hidden',
          opacity: interpolate(b, [0, 0.55], [1, 0], { extrapolateRight: 'clamp' }),
        }}
      >
        <Img
          src={staticFile(`zrzuty/${modul}`)}
          style={{
            position: 'absolute',
            height: '100%',
            left: '50%',
            transform: 'translateX(-46%) scale(1.06)',
          }}
        />
        <div
          style={{
            position: 'absolute',
            inset: 0,
            background: 'linear-gradient(90deg, rgba(26,15,66,0.35) 0%, rgba(26,15,66,0.05) 60%, rgba(26,15,66,0.5) 100%)',
          }}
        />
        <div
          style={{
            position: 'absolute',
            left: 40,
            top: 190,
            fontFamily: FONT,
            fontSize: 24,
            letterSpacing: 2,
            fontWeight: 700,
            color: MARKA.bialy,
            textShadow: `0 4px 18px ${MARKA.fioletCiemny}`,
          }}
        >
          MODUŁ · CELE SMART
        </div>
      </div>

      {/* przygaszenie góry kadru, żeby znak marki był czytelny nad zrzutem */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background:
            'linear-gradient(180deg, rgba(26,15,66,0.85) 0%, rgba(26,15,66,0.4) 10%, rgba(26,15,66,0) 20%)',
          pointerEvents: 'none',
        }}
      />

      {/* PRAWA POŁOWA — prawdziwy druk IPET (strona z sekcją III) */}
      <div
        style={{
          position: 'absolute',
          left: lewaStrony,
          top: gornaStrony,
          height: wysStrony,
          width: szerStrony,
          background: MARKA.bialy,
          boxShadow: `0 30px 70px ${MARKA.cien}`,
          borderRadius: 3,
          overflow: 'hidden',
        }}
      >
        <Img src={staticFile(`zrzuty/${strona}`)} style={{ width: '100%', display: 'block' }} />
      </div>

      {/* podświetlenia wierszy tabeli III po wylądowaniu celu */}
      {WIERSZE.map((wiersz, i) => {
        const wejscie = Math.round((1.6 + i * 2.5) * fps);
        const wyladowanie = wejscie + Math.round(1.2 * fps);
        const blysk = interpolate(f, [wyladowanie, wyladowanie + 8, wyladowanie + 40], [0, 1, 0.28], {
          extrapolateLeft: 'clamp',
          extrapolateRight: 'clamp',
        });
        const a = pkt(wiersz.x0, wiersz.yc - wiersz.h / 2);
        const bp = pkt(wiersz.x1, wiersz.yc + wiersz.h / 2);
        return (
          <div
            key={`w${i}`}
            style={{
              position: 'absolute',
              left: a.x,
              top: a.y,
              width: bp.x - a.x,
              height: bp.y - a.y,
              background: MARKA.fioletJasny,
              opacity: blysk * 0.5,
              borderLeft: `6px solid ${MARKA.pomarancz}`,
              mixBlendMode: 'multiply',
            }}
          />
        );
      })}

      {/* pigułki z treścią celu lecące z modułu do druku */}
      {pigulki.map((tekst, i) => {
        const wejscie = Math.round((1.6 + i * 2.5) * fps);
        const lot = Math.round(1.2 * fps);
        const t = interpolate(f, [wejscie, wejscie + lot], [0, 1], {
          extrapolateLeft: 'clamp',
          extrapolateRight: 'clamp',
        });
        if (f < wejscie - 2) return null;

        const cel = pkt(0.4, WIERSZE[i]?.yc ?? 0.4);
        const startX = 300;
        const startY = 360 + i * 150;
        const x = bezier(t, startX, 820, cel.x);
        const y = bezier(t, startY, startY - 220, cel.y);
        const krycie = interpolate(t, [0, 0.08, 0.88, 1], [0, 1, 1, 0]);
        const skala = interpolate(t, [0, 1], [1, 0.66]);

        return (
          <div
            key={tekst}
            style={{
              position: 'absolute',
              left: x,
              top: y,
              transform: `translate(-50%, -50%) scale(${skala})`,
              opacity: krycie,
              maxWidth: 520,
              background: MARKA.bialy,
              color: MARKA.fiolet,
              fontFamily: FONT,
              fontSize: 22,
              fontWeight: 700,
              lineHeight: 1.35,
              padding: '14px 20px',
              borderRadius: 10,
              borderLeft: `5px solid ${MARKA.pomarancz}`,
              boxShadow: `0 18px 44px rgba(0,0,0,0.35)`,
            }}
          >
            ✓ {tekst}
          </div>
        );
      })}

      {/* strzałka „na żywo" między modułem a drukiem */}
      <div
        style={{
          position: 'absolute',
          left: 900,
          top: 520,
          fontFamily: FONT,
          fontSize: 34,
          fontWeight: 700,
          color: MARKA.pomarancz,
          opacity: interpolate(b, [0, 0.4], [1, 0], { extrapolateRight: 'clamp' }),
        }}
      >
        →
      </div>

      {/* jak wyżej: nagłówek marki jest już na zrzucie modułu */}
      {scena.podpis ? <Podpis tekst={scena.podpis} /> : null}
      {znakDanePrzykladowe ? <ZnakDanePrzykladowe /> : null}
    </Tlo>
  );
};
