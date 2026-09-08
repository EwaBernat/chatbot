import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {MARKA, FONT} from '../marka';
import {Logo, Pojaw, useWejscie} from '../ui';
import type {Z} from '../typy';

const DRUKI = ['Metryczka', 'WOPF', 'IPET / PEWS', 'Realizacja', 'Ewaluacja'];

const Teczka: React.FC<{i: number; od: number}> = ({i, od}) => {
  const w = useWejscie(od, {damping: 13, stiffness: 90});
  const kat = (i - 2) * 9;
  const startX = [-520, -300, 0, 300, 520][i];
  const startY = [-260, 340, -420, 360, -240][i];
  const slotX = 250 + i * 190;
  return (
    <div
      style={{
        position: 'absolute',
        left: slotX,
        top: 120,
        width: 150,
        height: 190,
        borderRadius: 12,
        background: '#fff',
        boxShadow: '0 14px 40px rgba(0,0,0,0.28)',
        transform: `translate(${(1 - w) * startX}px, ${(1 - w) * startY}px) rotate(${(1 - w) * kat}deg) scale(${0.7 + 0.3 * w})`,
        opacity: Math.min(1, w * 1.6),
        fontFamily: FONT,
        overflow: 'hidden',
      }}
    >
      <div style={{height: 6, display: 'flex'}}>
        <div style={{flex: 1.2, background: MARKA.fiolet}} />
        <div style={{flex: 1, background: MARKA.pomarancz}} />
      </div>
      <div style={{padding: 14}}>
        <div style={{fontSize: 15, fontWeight: 700, color: MARKA.fiolet}}>{DRUKI[i]}</div>
        {[0, 1, 2, 3, 4].map((k) => (
          <div key={k} style={{height: 6, borderRadius: 3, background: k === 0 ? MARKA.lawenda : '#ECEAF3', marginTop: 10, width: `${[100, 85, 92, 60, 75][k]}%`}} />
        ))}
        <div style={{marginTop: 14, height: 18, borderRadius: 9, background: MARKA.pomaranczJasny, border: `1px solid ${MARKA.pomarancz}`, width: 70}} />
      </div>
    </div>
  );
};

export const Intro: React.FC<{z: Z}> = ({z}) => {
  const frame = useCurrentFrame();
  const SZAFA = z.szafa ?? 92;
  const NAZWA = z.nazwa ?? SZAFA + 120;
  const logoW = useWejscie(0, {damping: 12, stiffness: 100});
  const szafa = useWejscie(SZAFA);
  const akcent = interpolate(frame, [NAZWA, NAZWA + 8, NAZWA + 24], [0, 1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const glow = interpolate(frame, [0, 60], [0.2, 0.6], {extrapolateRight: 'clamp'});
  // Faza 1 (0–90): logo + tytuł na środku. Faza 2 (92+): tytuł jedzie w górę, wjeżdża „szafa".
  const przesunTytul = interpolate(szafa, [0, 1], [0, -230]);
  const skalaTytul = interpolate(szafa, [0, 1], [1, 0.72]) * (1 + 0.06 * akcent);

  return (
    <AbsoluteFill style={{background: `linear-gradient(160deg, ${MARKA.fioletCiemny} 0%, ${MARKA.fiolet} 55%, #3b2a86 100%)`, fontFamily: FONT}}>
      <div
        style={{
          position: 'absolute',
          left: 560,
          top: 100,
          width: 800,
          height: 800,
          borderRadius: '50%',
          background: `radial-gradient(circle, rgba(232,69,10,${glow * 0.45}) 0%, rgba(232,69,10,0) 60%)`,
        }}
      />
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 300,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          transform: `translateY(${przesunTytul}px) scale(${skalaTytul})`,
        }}
      >
        <div style={{transform: `scale(${logoW}) rotate(${(1 - logoW) * -40}deg)`, opacity: logoW}}>
          <Logo rozmiar={170} />
        </div>
        <Pojaw od={10} style={{marginTop: 30}}>
          <div style={{fontSize: 104, fontWeight: 800, color: '#fff', letterSpacing: -2, lineHeight: 1}}>
            EduPlaner <span style={{color: '#F6A57E'}}>2026</span>
          </div>
        </Pojaw>
        <Pojaw od={26}>
          <div style={{marginTop: 18, fontSize: 30, color: 'rgba(255,255,255,0.82)', letterSpacing: 3, textTransform: 'uppercase'}}>
            Mniej dokumentów. Więcej edukacji.
          </div>
        </Pojaw>
      </div>

      {/* Cyfrowa szafa */}
      <div style={{position: 'absolute', left: 0, right: 0, top: 480, opacity: szafa}}>
        <div style={{position: 'relative', margin: '0 auto', width: 1260, height: 400}}>
          <div
            style={{
              position: 'absolute',
              left: 110,
              top: 60,
              width: 1040,
              height: 330,
              borderRadius: 22,
              border: '2px solid rgba(255,255,255,0.28)',
              background: 'rgba(255,255,255,0.06)',
              boxShadow: 'inset 0 0 60px rgba(0,0,0,0.25)',
              transform: `scaleX(${szafa})`,
            }}
          />
          {DRUKI.map((_, i) => (
            <Teczka key={i} i={i} od={SZAFA + 12 + i * 9} />
          ))}
          <Pojaw od={SZAFA + 58} style={{position: 'absolute', left: 0, right: 0, top: 342, textAlign: 'center'}}>
            <div style={{fontSize: 34, fontWeight: 700, color: '#fff'}}>Cyfrowa szafa dla Twojej placówki</div>
            <div style={{fontSize: 21, color: 'rgba(255,255,255,0.75)', marginTop: 8}}>cała dokumentacja w jednym, uporządkowanym miejscu</div>
          </Pojaw>
        </div>
      </div>
    </AbsoluteFill>
  );
};
