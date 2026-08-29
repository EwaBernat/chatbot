import React from 'react';
import {useCurrentFrame, useVideoConfig, interpolate} from 'remotion';
import {MARKA, FONT} from './marka';
import {SZEROKOSC_AWATARA} from './Szkolenie';
import type {Napis} from './typy';

/**
 * Pasek napisów u dołu kadru. Wiersze przychodzą z pliku SRT wygenerowanego
 * razem z narracją, więc znaczniki czasu są rzeczywiste, a nie szacowane.
 */
export const Napisy: React.FC<{napisy: Napis[]}> = ({napisy}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const sekunda = frame / fps;

  const biezacy = napisy.find((n) => sekunda >= n.od && sekunda < n.do);
  if (!biezacy) {
    return null;
  }

  const wejscie = interpolate(sekunda - biezacy.od, [0, 0.16], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <div
      style={{
        position: 'absolute',
        left: SZEROKOSC_AWATARA + 40,
        right: 40,
        bottom: 34,
        display: 'flex',
        justifyContent: 'center',
        pointerEvents: 'none',
      }}
    >
      <div
        style={{
          maxWidth: 1160,
          padding: '18px 40px',
          borderRadius: 18,
          background: 'rgba(45, 27, 105, 0.92)',
          color: MARKA.bialy,
          fontFamily: FONT,
          fontSize: 38,
          lineHeight: 1.32,
          textAlign: 'center',
          fontWeight: 600,
          letterSpacing: -0.2,
          opacity: wejscie,
          transform: `translateY(${(1 - wejscie) * 10}px)`,
          boxShadow: '0 18px 44px rgba(45, 27, 105, 0.28)',
        }}
      >
        {biezacy.tekst}
      </div>
    </div>
  );
};
