import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate} from 'remotion';
import {MARKA, FONT} from '../marka';

/**
 * Karta aktu prawnego. Kolejność wejścia jest znacząca: najpierw etykieta
 * i tytuł, na końcu sygnatura — „pieczęć” wjeżdża z góry i osiada,
 * bo to ona jest tym, co rada ma zapamiętać.
 */
export const Przepis: React.FC<{
  etykieta?: string;
  tytul: string;
  sygnatura: string;
  status?: string;
  data?: string;
  uwaga?: string;
}> = ({etykieta = 'STRAŻNIK PRAWA', tytul, sygnatura, status, data, uwaga}) => {
  const klatka = useCurrentFrame();
  const {fps} = useVideoConfig();

  const karta = spring({frame: klatka, fps, config: {damping: 200}});
  const tytulW = spring({frame: klatka - 8, fps, config: {damping: 200}});
  const pieczec = spring({frame: klatka - 26, fps, config: {damping: 14, stiffness: 120, mass: 0.9}});
  const stopka = spring({frame: klatka - 46, fps, config: {damping: 200}});
  const uwagaW = spring({frame: klatka - 70, fps, config: {damping: 200}});

  const skala = interpolate(pieczec, [0, 1], [1.35, 1]);

  return (
    <AbsoluteFill style={{justifyContent: 'center', alignItems: 'center', fontFamily: FONT}}>
      <div
        style={{
          width: 1440,
          background: '#FFFFFF',
          borderRadius: 18,
          boxShadow: '0 18px 60px rgba(45, 27, 105, 0.12)',
          borderLeft: `14px solid ${MARKA.wyroznienie}`,
          padding: '60px 72px 56px 66px',
          opacity: karta,
          transform: `translateY(${interpolate(karta, [0, 1], [30, 0])}px)`,
        }}
      >
        <div
          style={{
            fontSize: 22,
            letterSpacing: 4,
            fontWeight: 700,
            color: MARKA.wyroznienie,
            marginBottom: 22,
          }}
        >
          {etykieta}
        </div>

        <div
          style={{
            fontSize: 40,
            lineHeight: 1.28,
            fontWeight: 600,
            color: MARKA.tekst,
            opacity: tytulW,
            transform: `translateY(${interpolate(tytulW, [0, 1], [14, 0])}px)`,
            maxWidth: 1280,
          }}
        >
          {tytul}
        </div>

        <div
          style={{
            marginTop: 40,
            display: 'flex',
            alignItems: 'baseline',
            gap: 28,
            opacity: pieczec,
            transform: `scale(${skala})`,
            transformOrigin: 'left center',
          }}
        >
          <div style={{fontSize: 74, fontWeight: 800, color: MARKA.tekst, letterSpacing: -1}}>
            {sygnatura}
          </div>
        </div>

        {(status || data) && (
          <div
            style={{
              marginTop: 28,
              display: 'flex',
              gap: 18,
              alignItems: 'center',
              opacity: stopka,
            }}
          >
            {status ? (
              <span
                style={{
                  fontSize: 24,
                  fontWeight: 700,
                  color: '#FFFFFF',
                  background: MARKA.slupek,
                  padding: '8px 18px',
                  borderRadius: 999,
                }}
              >
                {status}
              </span>
            ) : null}
            {data ? (
              <span style={{fontSize: 28, color: MARKA.tekstDrugi}}>{data}</span>
            ) : null}
          </div>
        )}

        {uwaga ? (
          <div
            style={{
              marginTop: 30,
              paddingTop: 22,
              borderTop: `2px solid ${MARKA.siatka}`,
              fontSize: 27,
              lineHeight: 1.4,
              color: MARKA.tekstDrugi,
              opacity: uwagaW,
            }}
          >
            {uwaga}
          </div>
        ) : null}
      </div>
    </AbsoluteFill>
  );
};
