import React from 'react';
import {interpolate, useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from './marka';
import type {Napis} from './typy';

/** Napisy sterowane znacznikami czasu dopasowanymi do nagrania. */
export const Napisy: React.FC<{napisy: Napis[]}> = ({napisy}) => {
  const klatka = useCurrentFrame();
  const {fps} = useVideoConfig();
  const sekunda = klatka / fps;
  const biezacy = napisy.find((n) => sekunda >= n.odSek && sekunda < n.doSek);
  if (!biezacy) return null;
  const wejscie = interpolate(sekunda - biezacy.odSek, [0, 0.14], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return (
    <div style={{position: 'absolute', left: 0, right: 0, bottom: 34, display: 'flex', justifyContent: 'center', padding: '0 140px', opacity: wejscie, transform: `translateY(${(1 - wejscie) * 10}px)`}}>
      <div
        style={{
          fontFamily: FONT,
          fontSize: 30,
          lineHeight: 1.3,
          fontWeight: 600,
          color: MARKA.fiolet,
          background: 'rgba(255,255,255,0.95)',
          borderLeft: `6px solid ${MARKA.pomarancz}`,
          borderRadius: 12,
          padding: '12px 26px',
          textAlign: 'center',
          maxWidth: 1300,
          boxShadow: '0 6px 24px rgba(45,27,105,0.18)',
        }}
      >
        {biezacy.tekst}
      </div>
    </div>
  );
};
