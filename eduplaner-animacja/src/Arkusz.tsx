import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {MARKA, FONT} from './marka';
import {Chip, NaglowekDruku, useWejscie} from './ui';

/** Kartka druku A4 na ekranie 16:9 — wspólna rama dla wszystkich stron metryczki. */
export const Arkusz: React.FC<{
  strona: string;
  children: React.ReactNode;
  data?: string;
  szerokosc?: number;
}> = ({strona, children, data = '23.07.2026 r.', szerokosc = 1520}) => {
  const frame = useCurrentFrame();
  const w = useWejscie(0, {damping: 16, stiffness: 90});
  const cien = interpolate(frame, [0, 20], [0, 1], {extrapolateRight: 'clamp'});
  return (
    <AbsoluteFill style={{background: `linear-gradient(135deg, #EFEBF7 0%, ${MARKA.tloCieple} 100%)`, fontFamily: FONT}}>
      <div
        style={{
          position: 'absolute',
          left: (1920 - szerokosc) / 2,
          top: 34,
          width: szerokosc,
          height: 1080,
          background: '#fff',
          borderRadius: '18px 18px 0 0',
          boxShadow: `0 ${20 * cien}px ${60 * cien}px rgba(45,27,105,0.18)`,
          transform: `translateY(${(1 - w) * 80}px)`,
          opacity: w,
          overflow: 'hidden',
        }}
      >
        <NaglowekDruku podtytul="METRYCZKA · DANE DZIECKA I PLACÓWKI" etykieta="Metryczka" />
        <div style={{display: 'flex', gap: 18, padding: '22px 44px 0'}}>
          <Chip etykieta="DOTYCZY DZIECKA" wartosc="Maja Dąbrowska" style={{flex: 1.3}} />
          <Chip etykieta="ROK SZKOLNY" wartosc="2025/2026" style={{flex: 0.9}} />
          <Chip etykieta="DATA" wartosc={data} style={{flex: 1}} />
        </div>
        <div style={{padding: '22px 44px 0', position: 'relative'}}>{children}</div>
        <div style={{position: 'absolute', left: 44, right: 44, bottom: 0, display: 'flex', justifyContent: 'space-between', fontSize: 13, color: MARKA.tekstCichy, padding: '10px 0', borderTop: `1px solid ${MARKA.linia}`}}>
          <span>EduPlaner 2026 · PCTP</span>
          <span>{strona}</span>
        </div>
      </div>
    </AbsoluteFill>
  );
};
