import React from 'react';
import {useCurrentFrame, useVideoConfig, interpolate} from 'remotion';
import {MARKA, FONT} from './marka';
import type {Napis} from './srt';

/**
 * Napisy sterowane znacznikami czasu z ElevenLabs — nie szacowane z liczby słów,
 * więc trzymają się nagrania co do dziesiątej części sekundy.
 */
export const Napisy: React.FC<{napisy: Napis[]}> = ({napisy}) => {
  const klatka = useCurrentFrame();
  const {fps} = useVideoConfig();
  const sekunda = klatka / fps;

  const biezacy = napisy.find((n) => sekunda >= n.odSek && sekunda < n.doSek);
  if (!biezacy) return null;

  const wejscie = interpolate(sekunda - biezacy.odSek, [0, 0.12], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <div
      style={{
        position: 'absolute',
        left: 0,
        right: 0,
        bottom: 72,
        display: 'flex',
        justifyContent: 'center',
        padding: '0 140px',
        opacity: wejscie,
      }}
    >
      <div
        style={{
          fontFamily: FONT,
          fontSize: 34,
          lineHeight: 1.35,
          fontWeight: 600,
          color: MARKA.tekst,
          background: 'rgba(252, 252, 251, 0.94)',
          borderRadius: 12,
          padding: '14px 26px',
          textAlign: 'center',
          maxWidth: 1180,
          boxShadow: '0 2px 18px rgba(45, 27, 105, 0.10)',
        }}
      >
        {biezacy.tekst}
      </div>
    </div>
  );
};
