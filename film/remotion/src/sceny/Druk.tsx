import React from 'react';
import {AbsoluteFill, Img, staticFile, useCurrentFrame, useVideoConfig, interpolate, spring} from 'remotion';
import {MARKA, FONT} from '../marka';
import type {Kadr, PoleDruku} from '../typy';

/**
 * Animacja wypełniania prawdziwego druku.
 *
 * Tłem jest strona druku (PNG z pdftoppm). Kadr wskazuje fragment strony
 * w pikselach obrazu; komponent skaluje go tak, by mieścił się w klatce,
 * i nakłada pola: ramkę podświetlenia i tekst dopisujący się znak po znaku.
 * Współrzędne pól są w tym samym układzie co kadr, więc obraz i pola
 * przesuwają się razem.
 */
export const Druk: React.FC<{
  obraz: string;
  szerObrazu: number;
  wysObrazu: number;
  kadr: Kadr;
  pola: PoleDruku[];
  etykieta?: string;
}> = ({obraz, szerObrazu, wysObrazu, kadr, pola, etykieta}) => {
  const klatka = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();
  const sek = klatka / fps;

  const wolne = {szer: width - 160, wys: height - 200};
  const skala = Math.min(wolne.szer / kadr.szer, wolne.wys / kadr.wys);
  const wejscie = spring({frame: klatka, fps, config: {damping: 200}});
  // delikatny najazd — kadr „osiada” zamiast stać jak zrzut ekranu
  const najazd = interpolate(wejscie, [0, 1], [0.97, 1]);
  const s = skala * najazd;

  const srodekX = kadr.x + kadr.szer / 2;
  const srodekY = kadr.y + kadr.wys / 2;
  const tx = width / 2 - srodekX * s;
  const ty = (height - 120) / 2 - srodekY * s + 20;

  return (
    <AbsoluteFill style={{background: MARKA.tloDrugie, overflow: 'hidden', fontFamily: FONT}}>
      <div
        style={{
          position: 'absolute',
          left: 0,
          top: 0,
          width: szerObrazu,
          height: wysObrazu,
          transform: `translate(${tx}px, ${ty}px) scale(${s})`,
          transformOrigin: '0 0',
          opacity: wejscie,
          boxShadow: '0 30px 90px rgba(45,27,105,0.18)',
          background: '#FFFFFF',
        }}
      >
        <Img src={staticFile(obraz)} style={{width: szerObrazu, height: wysObrazu, display: 'block'}} />

        {pola.map((p, i) => {
          const start = p.odSek;
          if (sek < start) return null;
          const lokalna = sek - start;
          const rodzaj = p.rodzaj ?? 'tekst';
          const ramka = interpolate(lokalna, [0, 0.25], [0, 1], {extrapolateRight: 'clamp'});
          const znakow = p.tekst ? Math.min(p.tekst.length, Math.floor(lokalna * 18)) : 0;
          const rozmiar = p.rozmiar ?? Math.max(14, Math.round(p.wys * 0.62));
          const gotowe = p.tekst ? znakow >= p.tekst.length : lokalna > 0.5;
          const zanik = p.doSek !== undefined
            ? interpolate(sek, [p.doSek - 0.3, p.doSek], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'})
            : 1;

          return (
            <div key={i} style={{position: 'absolute', left: p.x, top: p.y, width: p.szer, height: p.wys, opacity: zanik}}>
              {/* podświetlenie pola */}
              <div
                style={{
                  position: 'absolute',
                  inset: -6,
                  borderRadius: 6,
                  border: `3px solid ${MARKA.wyroznienie}`,
                  background: p.tlo ? '#FFFCF9' : `rgba(232, 69, 10, ${gotowe ? 0.04 : 0.10})`,
                  opacity: ramka,
                  boxShadow: gotowe ? 'none' : '0 0 0 6px rgba(232,69,10,0.12)',
                }}
              />

              {rodzaj === 'tekst' && p.tekst ? (
                <div
                  style={{
                    position: 'absolute',
                    left: 8,
                    top: 0,
                    height: p.wys,
                    display: 'flex',
                    alignItems: 'center',
                    fontSize: rozmiar,
                    fontWeight: 600,
                    color: MARKA.tekst,
                    whiteSpace: 'nowrap',
                    letterSpacing: 0.3,
                  }}
                >
                  {p.tekst.slice(0, znakow)}
                  {!gotowe ? (
                    <span
                      style={{
                        display: 'inline-block',
                        width: 3,
                        height: rozmiar * 1.1,
                        marginLeft: 2,
                        background: MARKA.wyroznienie,
                        opacity: Math.floor(lokalna * 3) % 2 === 0 ? 1 : 0,
                      }}
                    />
                  ) : null}
                </div>
              ) : null}

              {rodzaj === 'kolko' ? (
                <svg width={p.szer} height={p.wys} viewBox={`0 0 ${p.szer} ${p.wys}`} style={{position: 'absolute', inset: 0, overflow: 'visible'}}>
                  <circle
                    cx={p.szer / 2}
                    cy={p.wys / 2}
                    r={Math.min(p.szer, p.wys) / 2 + 2}
                    fill="none"
                    stroke={MARKA.wyroznienie}
                    strokeWidth={4}
                    strokeDasharray={Math.PI * (Math.min(p.szer, p.wys) + 4)}
                    strokeDashoffset={Math.PI * (Math.min(p.szer, p.wys) + 4) * (1 - interpolate(lokalna, [0.1, 0.7], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}))}
                    transform={`rotate(-90 ${p.szer / 2} ${p.wys / 2})`}
                  />
                </svg>
              ) : null}

              {rodzaj === 'ptaszek' ? (
                <svg width={p.szer} height={p.wys} viewBox="0 0 100 100" style={{position: 'absolute', inset: 0}}>
                  <path
                    d="M 18 52 L 42 76 L 84 26"
                    fill="none"
                    stroke={MARKA.wyroznienie}
                    strokeWidth={14}
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeDasharray={140}
                    strokeDashoffset={140 * (1 - interpolate(lokalna, [0.1, 0.5], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}))}
                  />
                </svg>
              ) : null}
            </div>
          );
        })}
      </div>

      {etykieta ? (
        <div
          style={{
            position: 'absolute',
            top: 36,
            left: 80,
            fontSize: 22,
            letterSpacing: 3,
            fontWeight: 700,
            color: MARKA.wyroznienie,
            background: 'rgba(252,252,251,0.92)',
            padding: '8px 16px',
            borderRadius: 8,
            opacity: wejscie,
          }}
        >
          {etykieta}
        </div>
      ) : null}
    </AbsoluteFill>
  );
};
