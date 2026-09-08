import React from 'react';
import {AbsoluteFill, Img, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from '../marka';

/**
 * Animacja NA ORYGINALNYM DRUKU PDF: strony wyrenderowane 1:1 z pliku PDF, ułożone jedna pod
 * drugą, a na nich podświetlenia w miejscach opisanych współrzędnymi z PDF (punkty typograficzne),
 * znalezionymi przez skrypt po tekście druku. Kamera jedzie po arkuszu do miejsc, o których mówi narracja.
 */

export type Prostokat = [number, number, number, number]; // x0, y0, x1, y1 w punktach PDF

export type Wyroznienie = {
  sek: number;
  doSek: number;
  strona: number; // indeks w tablicy `strony`
  rect: Prostokat;
  pad?: number;
  etykieta?: string;
  kolor?: string;
};

export type UjeciePdf = {sek: number; strona: number; y: number; skala: number; czas?: number};

type Props = {
  strony: string[]; // nazwy plików w public/pog
  szerokoscPt: number;
  wysokoscPt: number;
  wyroznienia: Wyroznienie[];
  kamera: UjeciePdf[];
  odSek: number;
};

const SZER = 794;
const ODSTEP = 26;
const easeInOut = (t: number) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);

export const DrukPdf: React.FC<Props> = ({strony, szerokoscPt, wysokoscPt, wyroznienia, kamera, odSek}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const sek = odSek + frame / fps;
  const k = SZER / szerokoscPt;
  const WYS = wysokoscPt * k;
  const offset = (i: number) => i * (WYS + ODSTEP);

  // kamera
  let y = WYS / 2;
  let skala = 1.3;
  if (kamera.length > 0) {
    let i = 0;
    while (i + 1 < kamera.length && sek >= kamera[i + 1].sek) i++;
    const a = kamera[i];
    const ya = offset(a.strona) + a.y * k;
    y = ya;
    skala = a.skala;
    if (i + 1 < kamera.length) {
      const b = kamera[i + 1];
      const czas = b.czas ?? 1.1;
      const t = Math.max(0, Math.min(1, (sek - (b.sek - czas)) / czas));
      const e = easeInOut(t);
      y = ya + (offset(b.strona) + b.y * k - ya) * e;
      skala = a.skala + (b.skala - a.skala) * e;
    }
  }
  const tx = 960 - (SZER / 2) * skala;
  const ty = 540 - y * skala;

  return (
    <AbsoluteFill style={{background: `linear-gradient(135deg, #EFEBF7 0%, ${MARKA.tloCieple} 100%)`, overflow: 'hidden'}}>
      <div style={{position: 'absolute', left: 0, top: 0, width: SZER, transform: `translate(${tx}px, ${ty}px) scale(${skala})`, transformOrigin: '0 0'}}>
        {strony.map((s, i) => (
          <div key={s} style={{position: 'absolute', left: 0, top: offset(i), width: SZER, height: WYS, background: '#fff', boxShadow: '0 10px 40px rgba(45,27,105,0.18)', borderRadius: 6, overflow: 'hidden'}}>
            <Img src={staticFile(`pog/${s}.png`)} style={{width: SZER, height: WYS, display: 'block'}} />
          </div>
        ))}
        {wyroznienia.map((w, i) => {
          if (sek < w.sek || sek >= w.doSek) return null;
          const p = Math.min(1, (sek - w.sek) / 0.35);
          const e = easeInOut(p);
          const pad = w.pad ?? 8;
          const [x0, y0, x1, y1] = w.rect;
          const left = x0 * k - pad;
          const top = offset(w.strona) + y0 * k - pad;
          const szer = (x1 - x0) * k + 2 * pad;
          const wys = (y1 - y0) * k + 2 * pad;
          const kolor = w.kolor ?? MARKA.pomarancz;
          return (
            <div key={i} style={{position: 'absolute', left, top, width: szer, height: wys, borderRadius: 10, border: `3px solid ${kolor}`, background: `${kolor}1A`, boxShadow: `0 0 ${22 * e}px ${kolor}66`, opacity: e, transform: `scale(${1.08 - 0.08 * e})`, pointerEvents: 'none'}}>
              {w.etykieta ? (
                <div style={{position: 'absolute', left: -3, top: -34, background: kolor, color: '#fff', fontFamily: FONT, fontSize: 15, fontWeight: 700, padding: '5px 12px', borderRadius: 8, whiteSpace: 'nowrap', letterSpacing: 0.5}}>
                  {w.etykieta}
                </div>
              ) : null}
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
