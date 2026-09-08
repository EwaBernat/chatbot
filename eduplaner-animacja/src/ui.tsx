import React from 'react';
import {Img, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from './marka';

/** Sprężyste wejście 0→1, start w klatce `od` (względem bieżącej sekwencji). */
export const useWejscie = (od: number, opcje?: {damping?: number; stiffness?: number}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  return spring({
    frame: frame - od,
    fps,
    config: {damping: opcje?.damping ?? 14, stiffness: opcje?.stiffness ?? 120, mass: 0.8},
  });
};

/** Liniowy postęp 0→1 między klatkami `od` i `do` (obcięty). */
export const usePostep = (od: number, doK: number) => {
  const frame = useCurrentFrame();
  return interpolate(frame, [od, doK], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
};

export const Pojaw: React.FC<{
  od: number;
  children: React.ReactNode;
  przesun?: number;
  style?: React.CSSProperties;
}> = ({od, children, przesun = 28, style}) => {
  const w = useWejscie(od);
  return (
    <div
      style={{
        opacity: w,
        transform: `translateY(${(1 - w) * przesun}px)`,
        ...style,
      }}
    >
      {children}
    </div>
  );
};

export const Logo: React.FC<{rozmiar?: number}> = ({rozmiar = 80}) => (
  <Img
    src={staticFile('logo-lawenda.webp')}
    style={{width: rozmiar, height: rozmiar, borderRadius: '50%', display: 'block'}}
  />
);

/** Nagłówek druku EduPlaner (jak na wydrukach A4). */
export const NaglowekDruku: React.FC<{podtytul: string; etykieta: string; kolor?: string}> = ({
  podtytul,
  etykieta,
  kolor = MARKA.pomarancz,
}) => (
  <div style={{fontFamily: FONT}}>
    <div style={{display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '26px 44px 18px'}}>
      <div style={{display: 'flex', alignItems: 'center', gap: 18}}>
        <Logo rozmiar={64} />
        <div>
          <div style={{fontSize: 30, fontWeight: 700, color: MARKA.fiolet, letterSpacing: -0.5}}>EduPlaner 2026</div>
          <div style={{fontSize: 14, color: MARKA.tekstCichy, letterSpacing: 2, marginTop: 4}}>{podtytul}</div>
        </div>
      </div>
      <div style={{textAlign: 'right'}}>
        <div
          style={{
            display: 'inline-block',
            background: kolor,
            color: '#fff',
            fontWeight: 700,
            fontSize: 18,
            padding: '8px 22px',
            borderRadius: 999,
          }}
        >
          {etykieta}
        </div>
        <div style={{fontSize: 13, color: MARKA.tekstCichy, marginTop: 8}}>Teczka dziecka · WOPFU + IPET · 2026/27</div>
      </div>
    </div>
    <div style={{display: 'flex', height: 5}}>
      <div style={{flex: 1.2, background: MARKA.fiolet}} />
      <div style={{flex: 1, background: MARKA.pomarancz}} />
    </div>
  </div>
);

export const Chip: React.FC<{etykieta: string; wartosc: string; style?: React.CSSProperties}> = ({etykieta, wartosc, style}) => (
  <div
    style={{
      background: MARKA.lawenda,
      borderRadius: 10,
      padding: '12px 18px',
      fontFamily: FONT,
      display: 'flex',
      gap: 12,
      alignItems: 'baseline',
      ...style,
    }}
  >
    <span style={{fontSize: 13, letterSpacing: 1.5, fontWeight: 700, color: MARKA.fioletJasny}}>{etykieta}</span>
    <span style={{fontSize: 18, fontWeight: 700, color: MARKA.fiolet}}>{wartosc}</span>
  </div>
);

const RZYMSKIE_KOLOR = MARKA.pomarancz;

export const Sekcja: React.FC<{numer: string; tytul: string; od: number; style?: React.CSSProperties}> = ({numer, tytul, od, style}) => {
  const w = useWejscie(od);
  return (
    <div style={{display: 'flex', alignItems: 'center', gap: 14, fontFamily: FONT, opacity: w, ...style}}>
      <div
        style={{
          background: RZYMSKIE_KOLOR,
          color: '#fff',
          fontWeight: 700,
          fontSize: 16,
          width: 34,
          height: 30,
          borderRadius: 7,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          transform: `scale(${0.6 + 0.4 * w})`,
        }}
      >
        {numer}
      </div>
      <div style={{fontSize: 19, fontWeight: 700, color: MARKA.fiolet, letterSpacing: 1}}>{tytul}</div>
      <div style={{flex: 1, height: 1.5, background: MARKA.linia, transform: `scaleX(${w})`, transformOrigin: 'left'}} />
    </div>
  );
};

/** Pole druku: etykieta + wartość wpisująca się „na maszynie". */
export const Pole: React.FC<{
  etykieta: string;
  wartosc: string;
  od: number;
  tempo?: number; // klatek na znak
  style?: React.CSSProperties;
  wysokosc?: number;
}> = ({etykieta, wartosc, od, tempo = 1.2, style, wysokosc = 74}) => {
  const frame = useCurrentFrame();
  const w = useWejscie(od - 6);
  const znaki = Math.max(0, Math.floor((frame - od) / tempo));
  const gotowe = znaki >= wartosc.length;
  const tekst = wartosc.slice(0, znaki);
  const kursor = !gotowe && frame >= od && Math.floor(frame / 8) % 2 === 0;
  const blask = gotowe ? interpolate(frame - (od + wartosc.length * tempo), [0, 10, 30], [0.55, 0.35, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}) : 0;
  return (
    <div
      style={{
        border: `1.5px solid ${gotowe ? MARKA.fioletJasny : MARKA.linia}`,
        borderRadius: 12,
        background: MARKA.lawendaTlo,
        padding: '12px 16px',
        minHeight: wysokosc,
        fontFamily: FONT,
        opacity: w,
        transform: `translateY(${(1 - w) * 14}px)`,
        boxShadow: `0 0 0 ${blask * 8}px rgba(91,63,168,${blask * 0.35})`,
        boxSizing: 'border-box',
        ...style,
      }}
    >
      <div style={{fontSize: 11.5, letterSpacing: 1.3, fontWeight: 700, color: MARKA.fioletJasny}}>{etykieta}</div>
      <div style={{fontSize: 19, color: '#1f1a33', marginTop: 8, minHeight: 24}}>
        {tekst}
        {kursor ? <span style={{color: MARKA.pomarancz}}>|</span> : null}
      </div>
    </div>
  );
};

export const Kratka: React.FC<{tekst: string; zaznacz?: boolean; od: number; style?: React.CSSProperties}> = ({tekst, zaznacz, od, style}) => {
  const w = useWejscie(od);
  const frame = useCurrentFrame();
  const tick = zaznacz ? spring({frame: frame - od - 14, fps: 30, config: {damping: 10, stiffness: 200}}) : 0;
  const on = zaznacz && tick > 0.05;
  return (
    <div
      style={{
        display: 'flex',
        alignItems: 'center',
        gap: 12,
        border: `1.5px solid ${on ? MARKA.pomarancz : MARKA.linia}`,
        background: on ? MARKA.pomaranczJasny : '#fff',
        borderRadius: 10,
        padding: '10px 14px',
        fontFamily: FONT,
        fontSize: 17,
        fontWeight: 600,
        color: MARKA.fiolet,
        opacity: w,
        transform: `translateY(${(1 - w) * 12}px)`,
        ...style,
      }}
    >
      <div
        style={{
          width: 20,
          height: 20,
          borderRadius: 5,
          border: `2px solid ${on ? MARKA.pomarancz : '#B9B3CC'}`,
          background: on ? MARKA.pomarancz : '#fff',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          color: '#fff',
          fontSize: 14,
          fontWeight: 900,
          transform: `scale(${on ? 0.8 + 0.2 * Math.min(1, tick) : 1})`,
        }}
      >
        {on ? '✓' : ''}
      </div>
      {tekst}
    </div>
  );
};

/** Kursor myszy poruszający się między punktami [x,y] w zadanych klatkach. */
export const Kursor: React.FC<{punkty: {klatka: number; x: number; y: number}[]; klik?: number}> = ({punkty, klik}) => {
  const frame = useCurrentFrame();
  const xs = punkty.map((p) => p.x);
  const ys = punkty.map((p) => p.y);
  const ks = punkty.map((p) => p.klatka);
  const x = interpolate(frame, ks, xs, {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const y = interpolate(frame, ks, ys, {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const s = klik !== undefined ? interpolate(frame, [klik, klik + 5, klik + 12], [1, 0.8, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}) : 1;
  const fala = klik !== undefined ? interpolate(frame, [klik, klik + 18], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}) : 0;
  return (
    <div style={{position: 'absolute', left: x, top: y, transform: `scale(${s})`, transformOrigin: 'top left'}}>
      {fala > 0 && fala < 1 ? (
        <div
          style={{
            position: 'absolute',
            left: -30 + 30 * (1 - fala),
            top: -30 + 30 * (1 - fala),
            width: 60 * fala,
            height: 60 * fala,
            borderRadius: '50%',
            border: `3px solid ${MARKA.pomarancz}`,
            opacity: 1 - fala,
          }}
        />
      ) : null}
      <svg width="34" height="40" viewBox="0 0 34 40">
        <path d="M2 2 L2 30 L9.5 23 L15 36 L21 33.5 L15.5 21 L26 21 Z" fill="#1f1a33" stroke="#fff" strokeWidth="2.5" strokeLinejoin="round" />
      </svg>
    </div>
  );
};

/** Ikona modułu — proste, spójne kształty SVG w kolorze morskim (jak na ekranie głównym). */
export const Ikona: React.FC<{typ: string; kolor?: string; rozmiar?: number}> = ({typ, kolor = MARKA.morski, rozmiar = 30}) => {
  const p = {fill: 'none', stroke: kolor, strokeWidth: 2.2, strokeLinecap: 'round' as const, strokeLinejoin: 'round' as const};
  let body: React.ReactNode;
  switch (typ) {
    case 'skrzynka':
      body = <><path d="M3 12l3-7h12l3 7v7H3z" {...p} /><path d="M3 12h5l2 3h4l2-3h5" {...p} /></>;
      break;
    case 'osoby':
      body = <><circle cx="9" cy="8" r="3.2" {...p} /><path d="M3 20c0-3.5 2.7-6 6-6s6 2.5 6 6" {...p} /><circle cx="17" cy="9" r="2.6" {...p} /><path d="M17 14c2.6 0 4.5 2 4.5 5" {...p} /></>;
      break;
    case 'dziecko':
      body = <><circle cx="12" cy="12" r="8.5" {...p} /><circle cx="9" cy="10.5" r="0.8" fill={kolor} /><circle cx="15" cy="10.5" r="0.8" fill={kolor} /><path d="M8.5 14.5c1 1.5 2.2 2.2 3.5 2.2s2.5-.7 3.5-2.2" {...p} /></>;
      break;
    case 'dymek':
      body = <path d="M4 6a3 3 0 013-3h10a3 3 0 013 3v8a3 3 0 01-3 3H9l-5 4z" {...p} />;
      break;
    case 'dostepnosc':
      body = <><circle cx="15" cy="4.5" r="1.8" fill={kolor} /><path d="M9 21a5 5 0 110-10" {...p} /><path d="M14 8l-1 6h5l2 6" {...p} /><path d="M13 14h-2" {...p} /></>;
      break;
    case 'budynek':
      body = <><path d="M4 21V9l8-6 8 6v12z" {...p} /><path d="M10 21v-6h4v6" {...p} /><path d="M8 11h2M14 11h2" {...p} /></>;
      break;
    case 'tarcza':
      body = <><path d="M12 3l8 3v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6z" {...p} /><path d="M8.5 12l2.5 2.5 4.5-5" {...p} /></>;
      break;
    case 'waga':
      body = <><path d="M12 3v18M5 21h14M12 6l7 2M12 6L5 8" {...p} /><path d="M2 14l3-6 3 6a3 3 0 01-6 0zM16 14l3-6 3 6a3 3 0 01-6 0z" {...p} /></>;
      break;
    case 'karta':
      body = <><rect x="4" y="3" width="16" height="18" rx="2.5" {...p} /><circle cx="12" cy="10" r="2.5" {...p} /><path d="M8 17c.8-2 2.2-3 4-3s3.2 1 4 3" {...p} /></>;
      break;
    case 'lista':
      body = <><rect x="4" y="3" width="16" height="18" rx="2.5" {...p} /><path d="M8 8h8M8 12h8M8 16h5" {...p} /></>;
      break;
    case 'wykres':
      body = <><path d="M4 20V4M4 20h16" {...p} /><path d="M7 15l4-5 3 3 5-7" {...p} /></>;
      break;
    case 'zespol':
      body = <><circle cx="12" cy="7" r="3" {...p} /><circle cx="5" cy="10" r="2.4" {...p} /><circle cx="19" cy="10" r="2.4" {...p} /><path d="M7 20c0-3 2.2-5.5 5-5.5s5 2.5 5 5.5M1.5 17c0-2 1.5-3.5 3.5-3.5M22.5 17c0-2-1.5-3.5-3.5-3.5" {...p} /></>;
      break;
    case 'kalendarz':
      body = <><rect x="3" y="5" width="18" height="16" rx="2.5" {...p} /><path d="M3 10h18M8 3v4M16 3v4" {...p} /><path d="M8 15l2.5 2.5 5-5" {...p} /></>;
      break;
    default:
      body = <circle cx="12" cy="12" r="8" {...p} />;
  }
  return (
    <svg width={rozmiar} height={rozmiar} viewBox="0 0 24 24">
      {body}
    </svg>
  );
};
