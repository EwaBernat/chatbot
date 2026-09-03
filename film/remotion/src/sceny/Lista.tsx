import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate} from 'remotion';
import {MARKA, FONT} from '../marka';

/** Punkty wjeżdżające po kolei — po jednym na myśl w narracji. */
export const Lista: React.FC<{tytul: string; punkty: string[]; numerowana?: boolean}> = ({tytul, punkty, numerowana}) => {
  const klatka = useCurrentFrame();
  const {fps} = useVideoConfig();
  const naglowek = spring({frame: klatka, fps, config: {damping: 200}});
  const duzo = punkty.length > 6;

  return (
    <AbsoluteFill style={{padding: '90px 150px 210px', fontFamily: FONT, justifyContent: 'center'}}>
      <div style={{fontSize: 50, fontWeight: 700, color: MARKA.tekst, marginBottom: duzo ? 28 : 44, opacity: naglowek}}>
        {tytul}
      </div>
      <div style={{display: 'flex', flexDirection: 'column', gap: duzo ? 14 : 24}}>
        {punkty.map((p, i) => {
          const w = spring({frame: klatka - 12 - i * 10, fps, config: {damping: 200}});
          return (
            <div
              key={i}
              style={{
                display: 'flex',
                gap: 24,
                alignItems: 'flex-start',
                opacity: w,
                transform: `translateX(${interpolate(w, [0, 1], [-22, 0])}px)`,
              }}
            >
              {numerowana ? (
                <div
                  style={{
                    width: 54,
                    height: 54,
                    borderRadius: 12,
                    background: MARKA.slupek,
                    color: '#FFFFFF',
                    fontSize: 28,
                    fontWeight: 800,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    flexShrink: 0,
                  }}
                >
                  {i + 1}
                </div>
              ) : (
                <div style={{width: 16, height: 16, marginTop: 16, borderRadius: 4, background: MARKA.wyroznienie, flexShrink: 0}} />
              )}
              <div style={{fontSize: duzo ? 30 : 36, lineHeight: 1.35, color: MARKA.tekst, fontWeight: 500}}>{p}</div>
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
