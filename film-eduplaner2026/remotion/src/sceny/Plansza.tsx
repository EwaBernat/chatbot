import React from 'react';
import { interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { FONT, MARKA } from '../marka';
import { Tlo, Znak } from '../ui/Chrome';
import type { Plansza as DanePlanszy } from '../typy';

/** Tytuł ujawniany słowo po słowie (stagger 3 klatki). */
const TytulSlowami: React.FC<{ tytul: string; odKlatki: number }> = ({ tytul, odKlatki }) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  return (
    <div>
      {tytul.split('\n').map((linia, li) => (
        <div key={li} style={{ display: 'flex', flexWrap: 'wrap', gap: '0 18px' }}>
          {linia.split(' ').map((slowo, si) => {
            const start = odKlatki + (li * 6 + si) * 3;
            const s = spring({ frame: f - start, fps, config: { damping: 200 }, durationInFrames: 24 });
            return (
              <span
                key={si}
                style={{
                  display: 'inline-block',
                  opacity: s,
                  transform: `translateY(${(1 - s) * 26}px)`,
                }}
              >
                {slowo}
              </span>
            );
          })}
        </div>
      ))}
    </div>
  );
};

export const Plansza: React.FC<{ dane: DanePlanszy; finalowa?: boolean }> = ({ dane, finalowa }) => {
  const f = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  const kreska = spring({ frame: f - 18, fps, config: { damping: 200 }, durationInFrames: 30 });
  const hasloOd = finalowa ? 11 * fps : 12 * fps;
  const hasloKrycie = interpolate(f, [hasloOd, hasloOd + 18], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const hasloSkala = interpolate(f, [hasloOd, hasloOd + 24], [0.96, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const kontaktOd = 8 * fps;

  return (
    <Tlo>
      <Znak />
      <div
        style={{
          position: 'absolute',
          inset: 0,
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
          padding: '0 140px',
          color: MARKA.bialy,
          fontFamily: FONT,
        }}
      >
        <div
          style={{
            fontSize: 22,
            letterSpacing: 4,
            fontWeight: 700,
            color: MARKA.pomarancz,
            opacity: interpolate(f, [0, 14], [0, 1], { extrapolateRight: 'clamp' }),
            transform: `translateY(${interpolate(f, [0, 14], [-20, 0], { extrapolateRight: 'clamp' })}px)`,
            marginBottom: 26,
          }}
        >
          {dane.nadtytul}
        </div>

        <div style={{ fontSize: 84, fontWeight: 700, lineHeight: 1.12, letterSpacing: -1 }}>
          <TytulSlowami tytul={dane.tytul} odKlatki={10} />
        </div>

        <div
          style={{
            height: 6,
            width: kreska * 260,
            background: MARKA.pomarancz,
            marginTop: 40,
            borderRadius: 3,
          }}
        />

        {dane.kontakt ? (
          <div
            style={{
              marginTop: 46,
              display: 'flex',
              gap: 44,
              fontSize: 30,
              opacity: interpolate(f, [kontaktOd, kontaktOd + 18], [0, 1], {
                extrapolateLeft: 'clamp',
                extrapolateRight: 'clamp',
              }),
            }}
          >
            {dane.kontakt.map((k) => (
              <span key={k} style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                <span style={{ width: 8, height: 8, background: MARKA.pomarancz, borderRadius: 8 }} />
                {k}
              </span>
            ))}
          </div>
        ) : null}

        <div
          style={{
            marginTop: 54,
            fontSize: 40,
            fontWeight: 700,
            opacity: hasloKrycie,
            transform: `scale(${hasloSkala})`,
            transformOrigin: 'left center',
          }}
        >
          {dane.haslo}
        </div>
      </div>

      {finalowa ? (
        <div
          style={{
            position: 'absolute',
            right: 140,
            top: '50%',
            marginTop: -160,
            width: 320,
            height: 320,
            border: `3px dashed rgba(255,255,255,0.45)`,
            borderRadius: 8,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            textAlign: 'center',
            color: 'rgba(255,255,255,0.6)',
            fontFamily: FONT,
            fontSize: 20,
            lineHeight: 1.5,
            opacity: interpolate(f, [fps * 4, fps * 5], [0, 1], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            }),
          }}
        >
          miejsce na kod QR
          <br />
          do formularza
        </div>
      ) : null}

      {/* wygaszenie do czerni na samym końcu filmu */}
      {finalowa ? (
        <div
          style={{
            position: 'absolute',
            inset: 0,
            background: '#000',
            opacity: interpolate(f, [durationInFrames - 12, durationInFrames], [0, 1], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            }),
          }}
        />
      ) : null}
    </Tlo>
  );
};
