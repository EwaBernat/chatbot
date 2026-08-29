import React from 'react';
import {useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT, ROZDZIALY} from './marka';
import type {Rozdzial} from './marka';
import {wejscie} from './anim';

/**
 * Prawa kolumna kadru — „ekran" z omawianą treścią.
 *
 * Nagłówek trzyma słuchacza w orientacji: nazwa rozdziału broszury po lewej,
 * kropki postępu po prawej. Ciało sceny dostaje resztę wysokości.
 */
export const Ekran: React.FC<{
  rozdzial: Rozdzial;
  naglowek: string;
  children: React.ReactNode;
}> = ({rozdzial, naglowek, children}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const aktywny = ROZDZIALY.indexOf(rozdzial);

  return (
    <div
      style={{
        flex: 1,
        height: '100%',
        background: MARKA.tlo,
        display: 'flex',
        flexDirection: 'column',
        padding: '54px 66px 190px 66px',
        fontFamily: FONT,
        position: 'relative',
      }}
    >
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          marginBottom: 12,
          ...wejscie(frame, fps, 0, 12),
        }}
      >
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 14,
            color: MARKA.akcent,
            fontSize: 22,
            fontWeight: 700,
            letterSpacing: 2.4,
            textTransform: 'uppercase',
          }}
        >
          <span
            style={{
              width: 34,
              height: 4,
              borderRadius: 2,
              background: MARKA.wyroznienie,
            }}
          />
          {rozdzial}
        </div>
        <div style={{display: 'flex', gap: 8, alignItems: 'center'}}>
          {ROZDZIALY.map((r, i) => (
            <span
              key={r}
              style={{
                width: i === aktywny ? 26 : 8,
                height: 8,
                borderRadius: 4,
                background: i === aktywny ? MARKA.wyroznienie : MARKA.siatka,
              }}
            />
          ))}
        </div>
      </div>

      <h1
        style={{
          margin: 0,
          color: MARKA.tekst,
          fontSize: 62,
          lineHeight: 1.08,
          letterSpacing: -1.4,
          fontWeight: 800,
          whiteSpace: 'pre-line',
          ...wejscie(frame, fps, 0.1, 18),
        }}
      >
        {naglowek}
      </h1>

      <div style={{flex: 1, marginTop: 34, minHeight: 0}}>{children}</div>
    </div>
  );
};
