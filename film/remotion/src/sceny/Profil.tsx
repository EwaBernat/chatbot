import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate} from 'remotion';
import {MARKA, FONT} from '../marka';

/**
 * Profil KPOF: dziewięć słupków d1–d9 w skali 1–5, linie progów 2,0 i 3,0.
 * Słupek poniżej 3,0 dostaje kolor uwagi i podpis z poziomem wsparcia —
 * informacja nie może zależeć od samego koloru. Obszar bez wartości (N,
 * albo d6 jako opisowy) rysuje się jako pusty tor z kreską.
 */
export const Profil: React.FC<{
  tytul: string;
  obszary: {kod: string; nazwa: string; wartosc: number | null}[];
  wynik?: number;
}> = ({tytul, obszary, wynik}) => {
  const klatka = useCurrentFrame();
  const {fps} = useVideoConfig();
  const naglowek = spring({frame: klatka, fps, config: {damping: 200}});

  const wysWykresu = 520;
  const doPx = (v: number) => ((v - 1) / 4) * wysWykresu;
  const kwalifikacja = (v: number) => (v >= 4 ? 'zasób' : v >= 3 ? 'poziom I' : v >= 2 ? 'poziom II' : 'poziom III');
  const kolorSlupka = (v: number) => (v >= 3 ? MARKA.profilZielony : v >= 2 ? MARKA.profilZolty : MARKA.profilCzerwony);
  const kolorTekstu = (v: number) => (v >= 3 ? MARKA.profilZielony : v >= 2 ? MARKA.profilZoltyTekst : MARKA.profilCzerwony);

  return (
    <AbsoluteFill style={{padding: '80px 140px 200px', fontFamily: FONT}}>
      <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', opacity: naglowek}}>
        <div style={{fontSize: 48, fontWeight: 700, color: MARKA.tekst}}>{tytul}</div>
        {wynik !== undefined ? (
          <div style={{fontSize: 30, color: MARKA.tekstDrugi}}>
            wynik ogólny <span style={{fontSize: 44, fontWeight: 800, color: MARKA.tekst}}>{wynik.toFixed(1).replace('.', ',')}</span> / 5
          </div>
        ) : null}
      </div>

      <div style={{position: 'relative', marginTop: 56, height: wysWykresu + 90}}>
        {/* siatka i progi */}
        {[1, 2, 3, 4, 5].map((v) => (
          <div
            key={v}
            style={{
              position: 'absolute',
              left: 70,
              right: 0,
              bottom: 90 + doPx(v),
              height: v === 2 || v === 3 ? 3 : 1,
              background: v === 2 ? MARKA.profilCzerwony : v === 3 ? MARKA.profilZielony : MARKA.siatka,
              opacity: v === 2 || v === 3 ? 0.7 : 1,
            }}
          >
            <div
              style={{
                position: 'absolute',
                left: -64,
                top: -18,
                fontSize: 26,
                fontWeight: 700,
                color: MARKA.tekstCichy,
              }}
            >
              {v},0
            </div>
          </div>
        ))}

        <div
          style={{
            position: 'absolute',
            left: 70,
            right: 0,
            bottom: 90,
            height: wysWykresu,
            display: 'flex',
            alignItems: 'flex-end',
            justifyContent: 'space-between',
            padding: '0 40px',
          }}
        >
          {obszary.map((o, i) => {
            const w = spring({frame: klatka - 8 - i * 4, fps, config: {damping: 200, mass: 0.8}});
            const brak = o.wartosc === null;
            const v = o.wartosc ?? 1;
            const h = doPx(v) * w;
            return (
              <div key={o.kod} style={{width: 120, display: 'flex', flexDirection: 'column', alignItems: 'center', position: 'relative'}}>
                {!brak ? (
                  <div
                    style={{
                      position: 'absolute',
                      bottom: h + 12,
                      fontSize: 30,
                      fontWeight: 800,
                      color: kolorTekstu(v),
                      opacity: w,
                      whiteSpace: 'nowrap',
                      textAlign: 'center',
                      lineHeight: 1.1,
                    }}
                  >
                    {v.toFixed(1).replace('.', ',')}
                    <div style={{fontSize: 18, fontWeight: 700, letterSpacing: 1}}>{kwalifikacja(v)}</div>
                  </div>
                ) : (
                  <div style={{position: 'absolute', bottom: 12, fontSize: 24, fontWeight: 700, color: MARKA.tekstCichy, opacity: w}}>
                    opisowy
                  </div>
                )}
                <div
                  style={{
                    width: 78,
                    height: Math.max(0, h),
                    background: brak ? 'transparent' : kolorSlupka(v),
                    borderRadius: '6px 6px 0 0',
                    border: brak ? `3px dashed ${MARKA.siatka}` : 'none',
                    minHeight: brak ? 40 : 0,
                  }}
                />
              </div>
            );
          })}
        </div>

        {/* podpisy osi */}
        <div style={{position: 'absolute', left: 70, right: 0, bottom: 0, display: 'flex', justifyContent: 'space-between', padding: '0 40px'}}>
          {obszary.map((o) => (
            <div key={o.kod} style={{width: 120, textAlign: 'center'}}>
              <div style={{fontSize: 28, fontWeight: 800, color: MARKA.tekst}}>{o.kod}</div>
              <div style={{fontSize: 17, color: MARKA.tekstDrugi, lineHeight: 1.2, marginTop: 4}}>{o.nazwa}</div>
            </div>
          ))}
        </div>
      </div>
    </AbsoluteFill>
  );
};
