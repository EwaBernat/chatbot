import React from 'react';
import {AbsoluteFill, Img, staticFile, useCurrentFrame, useVideoConfig, interpolate, spring} from 'remotion';
import {FONT} from '../marka';

/**
 * Zdjęcie pełnoekranowe z powolnym najazdem i tytułem na płaszczyźnie
 * przyciemnienia. Tekst nigdy nie leży wprost na fotografii — kontrast
 * musi być niezależny od tego, co akurat jest pod nim.
 */
export const Ilustracja: React.FC<{obraz: string; tytul?: string; podpis?: string}> = ({obraz, tytul, podpis}) => {
  const klatka = useCurrentFrame();
  const {fps, durationInFrames} = useVideoConfig();
  const wejscie = spring({frame: klatka, fps, config: {damping: 200}});
  const zoom = interpolate(klatka, [0, durationInFrames], [1.0, 1.07], {extrapolateRight: 'clamp'});
  const tytulW = spring({frame: klatka - 14, fps, config: {damping: 200}});

  return (
    <AbsoluteFill style={{background: '#000', overflow: 'hidden', fontFamily: FONT}}>
      <Img
        src={staticFile(obraz)}
        style={{
          width: '100%',
          height: '100%',
          objectFit: 'cover',
          transform: `scale(${zoom})`,
          opacity: wejscie,
        }}
      />
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          bottom: 0,
          height: 520,
          background: 'linear-gradient(180deg, rgba(20,10,50,0) 0%, rgba(20,10,50,0.72) 60%, rgba(20,10,50,0.86) 100%)',
        }}
      />
      {tytul ? (
        <div
          style={{
            position: 'absolute',
            left: 140,
            bottom: 200,
            maxWidth: 1400,
            opacity: tytulW,
            transform: `translateY(${interpolate(tytulW, [0, 1], [24, 0])}px)`,
          }}
        >
          <div style={{width: 84, height: 6, background: '#E8450A', borderRadius: 3, marginBottom: 26}} />
          <div style={{fontSize: 76, fontWeight: 800, color: '#FFFFFF', lineHeight: 1.08, letterSpacing: -0.5}}>
            {tytul}
          </div>
          {podpis ? (
            <div style={{fontSize: 34, color: 'rgba(255,255,255,0.86)', marginTop: 18, lineHeight: 1.3}}>{podpis}</div>
          ) : null}
        </div>
      ) : null}
    </AbsoluteFill>
  );
};
