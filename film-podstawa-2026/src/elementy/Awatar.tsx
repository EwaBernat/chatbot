import React from 'react';
import { OffthreadVideo, staticFile, useCurrentFrame, interpolate, spring, useVideoConfig } from 'remotion';
import { MARKA, FONT_NAGLOWEK } from '../marka';

/**
 * Okno awatara w prawym dolnym rogu.
 *
 * Gdy w public/ leży awatar.mp4 (nagranie z HeyGen), odtwarza je w kole.
 * Gdy pliku nie ma — pokazuje ramkę z informacją zamiast psuć kadr pustką,
 * więc film da się złożyć i obejrzeć zanim awatar powstanie.
 */
export const Awatar: React.FC<{ jest: boolean }> = ({ jest }) => {
  const klatka = useCurrentFrame();
  const { fps } = useVideoConfig();
  const wejscie = spring({ frame: klatka - 12, fps, config: { damping: 200 } });
  const srednica = 320;

  return (
    <div
      style={{
        position: 'absolute', right: 76, bottom: 168,
        width: srednica, height: srednica, borderRadius: '50%',
        overflow: 'hidden',
        border: `6px solid ${MARKA.pomaranczJasny}`,
        boxShadow: '0 30px 80px -30px rgba(0,0,0,.75)',
        transform: `scale(${interpolate(wejscie, [0, 1], [0.82, 1])})`,
        opacity: wejscie,
        background: MARKA.fioletCiemny,
        display: 'flex', alignItems: 'center', justifyContent: 'center',
      }}
    >
      {jest ? (
        <OffthreadVideo src={staticFile('awatar.mp4')}
                        style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
      ) : (
        <div style={{
          textAlign: 'center', color: MARKA.naCiemnymDrugi,
          fontFamily: FONT_NAGLOWEK, letterSpacing: '.14em', fontSize: 22,
          textTransform: 'uppercase', lineHeight: 1.5, padding: 30,
        }}>
          miejsce<br />na awatar<br />
          <span style={{ fontSize: 15, opacity: .75 }}>public/awatar.mp4</span>
        </div>
      )}
    </div>
  );
};
