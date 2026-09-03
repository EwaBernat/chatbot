import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate} from 'remotion';
import {MARKA, FONT} from '../marka';

const LITERY: [string, string][] = [
  ['S', 'konkretny'],
  ['M', 'mierzalny'],
  ['A', 'osiągalny'],
  ['R', 'istotny'],
  ['T', 'w czasie'],
];

/**
 * Cel życzeniowy zostaje przekreślony, w jego miejsce wjeżdża cel SMART,
 * a pod nim po kolei zapalają się litery. Przekreślenie rośnie od lewej —
 * widz ma zobaczyć, że stary zapis nie znika, tylko przestaje obowiązywać.
 */
export const CelSmart: React.FC<{przed: string; po: string}> = ({przed, po}) => {
  const klatka = useCurrentFrame();
  const {fps} = useVideoConfig();

  const przedW = spring({frame: klatka, fps, config: {damping: 200}});
  const kreska = interpolate(klatka, [30, 52], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const poW = spring({frame: klatka - 62, fps, config: {damping: 200}});
  const literyStart = 100;

  return (
    <AbsoluteFill style={{padding: '90px 150px 210px', fontFamily: FONT, justifyContent: 'center'}}>
      <div style={{fontSize: 22, letterSpacing: 4, fontWeight: 700, color: MARKA.tekstCichy, opacity: przedW}}>
        CEL ŻYCZENIOWY
      </div>
      <div style={{position: 'relative', display: 'inline-block', alignSelf: 'flex-start', marginTop: 12, opacity: przedW}}>
        <div style={{fontSize: 44, lineHeight: 1.3, color: MARKA.tekstDrugi, fontWeight: 500}}>{przed}</div>
        <div
          style={{
            position: 'absolute',
            left: 0,
            top: '52%',
            height: 6,
            width: `${kreska * 100}%`,
            background: MARKA.wyroznienie,
            borderRadius: 3,
          }}
        />
      </div>

      <div
        style={{
          marginTop: 56,
          opacity: poW,
          transform: `translateY(${interpolate(poW, [0, 1], [26, 0])}px)`,
        }}
      >
        <div style={{fontSize: 22, letterSpacing: 4, fontWeight: 700, color: MARKA.wyroznienie}}>CEL SMART</div>
        <div
          style={{
            marginTop: 14,
            fontSize: 40,
            lineHeight: 1.38,
            color: MARKA.tekst,
            fontWeight: 600,
            background: '#FFFFFF',
            padding: '30px 40px',
            borderRadius: 16,
            borderLeft: `12px solid ${MARKA.wyroznienie}`,
            boxShadow: '0 14px 44px rgba(45,27,105,0.10)',
          }}
        >
          {po}
        </div>
      </div>

      <div style={{display: 'flex', gap: 34, marginTop: 50}}>
        {LITERY.map(([l, opis], i) => {
          const w = spring({frame: klatka - literyStart - i * 9, fps, config: {damping: 14, stiffness: 160}});
          return (
            <div key={l} style={{display: 'flex', alignItems: 'center', gap: 14, opacity: w, transform: `scale(${interpolate(w, [0, 1], [0.7, 1])})`}}>
              <div
                style={{
                  width: 74,
                  height: 74,
                  borderRadius: 16,
                  background: MARKA.slupek,
                  color: '#FFFFFF',
                  fontSize: 44,
                  fontWeight: 800,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                }}
              >
                {l}
              </div>
              <div style={{fontSize: 26, fontWeight: 600, color: MARKA.tekstDrugi}}>{opis}</div>
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
