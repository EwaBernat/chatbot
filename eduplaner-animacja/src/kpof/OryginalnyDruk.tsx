import React, {useEffect, useLayoutEffect, useRef, useState} from 'react';
import {AbsoluteFill, continueRender, delayRender, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA} from '../marka';
import {znajdz, zaznaczBx, type WopfKrok} from './wopfResolver';

/**
 * Animacja NA ORYGINALNYM DRUKU. Komponent wczytuje prawdziwy plik HTML kwestionariusza
 * (bez zmian w jego wyglądzie), uruchamia jego własny skrypt liczący wyniki i klatka po
 * klatce „obsługuje” go jak użytkownik: klika oceny, zaznacza pola, wpisuje tekst.
 * Kamera jedzie po arkuszu A4 do miejsc, o których mówi narracja.
 */

export type Krok =
  | {sek: number; typ: 'ocena'; obszar: string; wiersz: number; wartosc: string; tabela?: string}
  | {sek: number; typ: 'klik'; selektor: string}
  | {sek: number; typ: 'tekst'; selektor: string; tekst: string; tempo?: number}
  | {sek: number; typ: 'wyroznij'; selektor: string; doSek: number}
  | {sek: number; typ: 'dane'; krok: WopfKrok; tempo?: number};

/** Selektor z opcjonalnym przedrostkiem strony: "@3 .fields .fv" = trzecia .page w druku. */
const wybierz = (root: ParentNode, sel: string): Element | null => {
  const m = /^@(\d+)\s+(.*)$/.exec(sel);
  if (!m) return root.querySelector(sel);
  const pg = root.querySelectorAll('.page')[Number(m[1]) - 1];
  return pg ? pg.querySelector(m[2]) : null;
};

export type Ujecie = {sek: number; selektor: string; skala: number; przesun?: number; czas?: number};

type Props = {
  plik: string;
  kroki: Krok[];
  kamera: Ujecie[];
  wykresyOdSek?: number;
  odSek: number; // początek tej sceny w sekundach filmu
};

const SZEROKOSC_DOKUMENTU = 794; // 210 mm przy 96 dpi

declare global {
  interface Window {
    kpofRecompute?: () => void;
    tomRecompute?: () => void;
  }
}

const easeInOut = (t: number) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);

export const OryginalnyDruk: React.FC<Props> = ({plik, kroki, kamera, wykresyOdSek, odSek}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const sek = odSek + frame / fps;
  const [html, setHtml] = useState<{css: string; body: string; skrypt: string} | null>(null);
  const [uchwyt] = useState(() => delayRender('Wczytywanie oryginalnego druku'));
  const kontener = useRef<HTMLDivElement>(null);
  const kameraRef = useRef<HTMLDivElement>(null);
  const kursorRef = useRef<HTMLDivElement>(null);
  const skalaRef = useRef(1);
  const skryptUruchomiony = useRef(false);

  useEffect(() => {
    let aktywny = true;
    fetch(staticFile(plik))
      .then((r) => r.text())
      .then(async (zrodlo) => {
        const css = [...zrodlo.matchAll(/<style[^>]*>([\s\S]*?)<\/style>/g)].map((m) => m[1]).join('\n');
        const cialo = zrodlo.replace(/^[\s\S]*?<body[^>]*>/, '').replace(/<\/body>[\s\S]*$/, '');
        // skrypty z całego pliku (WOPF trzyma swój w <head>), bez zewnętrznych src
        const skrypt = [...zrodlo.matchAll(/<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/g)].map((m) => m[1]).join('\n');
        const body = cialo.replace(/<script[\s\S]*?<\/script>/g, '');
        if (!aktywny) return;
        setHtml({css, body, skrypt});
      });
    return () => {
      aktywny = false;
    };
  }, [plik]);

  // Po wstawieniu HTML: uruchom oryginalny skrypt druku (liczy sumy, średnie, rysuje wykresy) i poczekaj na fonty.
  useEffect(() => {
    if (!html) return;
    document.fonts.ready.then(() => continueRender(uchwyt));
  }, [html, uchwyt]);

  /** Skrypt druku uruchamiamy synchronicznie, ZANIM pierwszy raz nałożymy kroki — inaczej zdarzenia „input" trafiłyby w pustkę. */
  const uruchomSkrypt = () => {
    if (!html || skryptUruchomiony.current) return;
    skryptUruchomiony.current = true;
    try {
      // eslint-disable-next-line no-new-func
      new Function(html.skrypt)();
      // druki czekające na „load" (np. WOPF) dostają je teraz — DOM jest już wstawiony
      window.dispatchEvent(new Event('load'));
    } catch (e) {
      // skrypt druku nie jest niezbędny do wyświetlenia — wyniki policzymy bez niego
      console.warn('Skrypt druku nie uruchomił się', e);
    }
  };

  // Każda klatka: stan druku wynika wyłącznie z czasu (deterministycznie), więc najpierw zerujemy, potem nakładamy kroki.
  useLayoutEffect(() => {
    const root = kontener.current;
    if (!root || !html) return;
    uruchomSkrypt();

    // Zerujemy tylko tabele, których dotykają kroki — przykładowe wartości w pozostałych zostają jak w druku.
    const tabele = new Set<string>();
    for (const k of kroki) if (k.typ === 'ocena') tabele.add(k.tabela ?? `#area-${k.obszar}`);
    if (tabele.size === 0) root.querySelectorAll('.rc.on').forEach((el) => el.classList.remove('on'));
    tabele.forEach((t) => root.querySelectorAll(`${t} .rc.on`).forEach((el) => el.classList.remove('on')));
    root.querySelectorAll('.chk.on, .opt.on').forEach((el) => el.classList.remove('on'));
    root.querySelectorAll<HTMLElement>('[data-anim-tekst]').forEach((el) => {
      el.textContent = '';
      el.removeAttribute('data-anim-tekst');
    });
    // kroki 'dane': zerujemy dotykane pola oryginalnego druku (tekst i pola .bx)
    for (const k of kroki) {
      if (k.typ !== 'dane') continue;
      for (const el of znajdz(root, k.krok)) {
        if (k.krok.bx) zaznaczBx(el, false);
        else el.textContent = '';
      }
    }
    root.querySelectorAll<HTMLElement>('[data-anim-wyr]').forEach((el) => {
      el.style.boxShadow = '';
      el.style.borderRadius = '';
      el.style.background = '';
      el.style.transition = '';
      el.removeAttribute('data-anim-wyr');
    });

    let ostatniCel: Element | null = null;
    let ostatniCzas = -1;
    let nastepny: {el: Element; sek: number} | null = null;

    for (const k of kroki) {
      if (k.typ === 'dane') {
        const els = znajdz(root, k.krok);
        if (!els.length) continue;
        if (sek >= k.sek) {
          for (const el of els) {
            if (k.krok.bx) zaznaczBx(el, true);
            else {
              const tempo = k.tempo ?? 22;
              const tekst = k.krok.tekst ?? '';
              const n = Math.min(tekst.length, Math.floor((sek - k.sek) * tempo));
              el.textContent = tekst.slice(0, n);
              (el as HTMLElement).dataset.man = '1'; // pole wpisane ręcznie — automat arkusza go nie nadpisze
              if (k.krok.qtab !== undefined) el.dispatchEvent(new Event('input', {bubbles: true}));
            }
          }
          if (k.sek > ostatniCzas) {
            ostatniCzas = k.sek;
            ostatniCel = els[0];
          }
        } else if (!nastepny || k.sek < nastepny.sek) {
          nastepny = {el: els[0], sek: k.sek};
        }
        continue;
      }
      if (k.typ === 'wyroznij') {
        if (sek >= k.sek && sek < k.doSek) {
          const el = wybierz(root, k.selektor) as HTMLElement | null;
          if (el) {
            const p = Math.min(1, (sek - k.sek) / 0.35);
            el.style.boxShadow = `0 0 0 ${3 * p}px ${MARKA.pomarancz}, 0 0 ${24 * p}px rgba(232,69,10,0.35)`;
            el.style.borderRadius = '8px';
            el.setAttribute('data-anim-wyr', '1');
          }
        }
        continue;
      }
      let el: Element | null = null;
      if (k.typ === 'ocena') {
        const tabela = root.querySelector(`${k.tabela ?? `#area-${k.obszar}`} tbody`);
        const wiersz = tabela?.children[k.wiersz];
        el = wiersz?.querySelector(`.rc[data-v="${k.wartosc}"]`) ?? null;
      } else {
        el = wybierz(root, k.selektor);
      }
      if (!el) continue;
      if (sek >= k.sek) {
        if (k.typ === 'ocena') el.classList.add('on');
        else if (k.typ === 'klik') {
          const chk = el.querySelector('.chk');
          (chk ?? el).classList.add('on');
          if (el.classList.contains('opt')) el.classList.add('on');
        } else if (k.typ === 'tekst') {
          const tempo = k.tempo ?? 14; // znaki na sekundę
          const n = Math.min(k.tekst.length, Math.floor((sek - k.sek) * tempo));
          (el as HTMLElement).textContent = k.tekst.slice(0, n);
          el.setAttribute('data-anim-tekst', '1');
        }
        if (k.sek > ostatniCzas) {
          ostatniCzas = k.sek;
          ostatniCel = el;
        }
      } else if (!nastepny || k.sek < nastepny.sek) {
        nastepny = {el, sek: k.sek};
      }
    }

    (window.kpofRecompute ?? window.tomRecompute)?.();

    // Wykresy: rosną od momentu, w którym narracja o nich mówi.
    if (wykresyOdSek !== undefined) {
      const p = easeInOut(Math.max(0, Math.min(1, (sek - wykresyOdSek) / 1.1)));
      root.querySelectorAll<SVGElement>('.barchart rect').forEach((r) => {
        r.style.transformBox = 'fill-box';
        r.style.transformOrigin = 'bottom';
        r.style.transform = `scaleY(${p})`;
      });
      root.querySelectorAll<SVGElement>('.barchart text, .radarchart circle').forEach((t) => {
        t.style.opacity = String(p);
      });
      root.querySelectorAll<SVGElement>('.radarchart polygon:last-of-type').forEach((pg) => {
        pg.style.transformBox = 'fill-box';
        pg.style.transformOrigin = 'center';
        pg.style.transform = `scale(${0.05 + 0.95 * p})`;
        pg.style.opacity = String(p);
      });
      root.querySelectorAll<HTMLElement>('.qrtbl tbody tr').forEach((tr, i) => {
        const q = Math.max(0, Math.min(1, (sek - wykresyOdSek - 0.6 - i * 0.12) / 0.3));
        tr.style.opacity = String(q);
      });
    }

    // Kamera: interpolacja między ujęciami, cel mierzony na żywo z DOM.
    const skalaPoprzednia = skalaRef.current;
    const rootRect = root.getBoundingClientRect();
    const celY = (u: Ujecie) => {
      const el = wybierz(root, u.selektor);
      if (!el) return 0;
      const r = el.getBoundingClientRect();
      return (r.top - rootRect.top) / skalaPoprzednia + (u.przesun ?? 0);
    };
    let y = 0;
    let skala = 1.3;
    if (kamera.length > 0) {
      let i = 0;
      while (i + 1 < kamera.length && sek >= kamera[i + 1].sek) i++;
      const a = kamera[i];
      const ya = celY(a);
      if (i + 1 < kamera.length) {
        const b = kamera[i + 1];
        const czas = b.czas ?? 1.1;
        const t = Math.max(0, Math.min(1, (sek - (b.sek - czas)) / czas));
        const e = easeInOut(t);
        y = ya + (celY(b) - ya) * e;
        skala = a.skala + (b.skala - a.skala) * e;
      } else {
        y = ya;
        skala = a.skala;
      }
      // pierwsze ujęcie: kamera już stoi na miejscu, nie ma skąd dojeżdżać
      if (i === 0 && sek < a.sek) {
        y = ya;
        skala = a.skala;
      }
    }
    skalaRef.current = skala;
    const tx = 960 - (SZEROKOSC_DOKUMENTU / 2) * skala;
    const ty = 540 - y * skala;
    if (kameraRef.current) kameraRef.current.style.transform = `translate(${tx}px, ${ty}px) scale(${skala})`;

    // Kursor: dojeżdża do następnego celu w ciągu 0,5 s, na kliknięciu lekko „siada".
    const kursor = kursorRef.current;
    if (kursor) {
      const poz = (el: Element) => {
        const r = el.getBoundingClientRect();
        return {x: (r.left + r.width / 2 - rootRect.left) / skalaPoprzednia, y: (r.top + r.height / 2 - rootRect.top) / skalaPoprzednia};
      };
      let x = -100;
      let yk = -100;
      let widoczny = 0;
      let nacisk = 1;
      if (ostatniCel) {
        const p = poz(ostatniCel);
        x = p.x;
        yk = p.y;
        widoczny = 1;
        const od = sek - ostatniCzas;
        nacisk = od < 0.12 ? 0.85 : 1;
        if (nastepny && nastepny.sek - sek < 0.5) {
          const q = poz(nastepny.el);
          const t = easeInOut(1 - (nastepny.sek - sek) / 0.5);
          x = p.x + (q.x - p.x) * t;
          yk = p.y + (q.y - p.y) * t;
        }
        if (od > 2.5 && !(nastepny && nastepny.sek - sek < 0.5)) widoczny = Math.max(0, 1 - (od - 2.5) / 0.4);
      } else if (nastepny && nastepny.sek - sek < 0.5) {
        const q = poz(nastepny.el);
        x = q.x;
        yk = q.y + 40 * (nastepny.sek - sek) / 0.5;
        widoczny = 1 - (nastepny.sek - sek) / 0.5;
      }
      kursor.style.transform = `translate(${x}px, ${yk}px) scale(${nacisk / Math.max(skala, 0.5)})`;
      kursor.style.opacity = String(widoczny);
    }
  });

  return (
    <AbsoluteFill style={{background: `linear-gradient(135deg, #EFEBF7 0%, ${MARKA.tloCieple} 100%)`, overflow: 'hidden'}}>
      {html ? <style dangerouslySetInnerHTML={{__html: html.css}} /> : null}
      <div ref={kameraRef} style={{position: 'absolute', left: 0, top: 0, width: SZEROKOSC_DOKUMENTU, transformOrigin: '0 0', willChange: 'transform'}}>
        <div ref={kontener} className="druk-oryginalny" dangerouslySetInnerHTML={{__html: html?.body ?? ''}} />
        <div ref={kursorRef} style={{position: 'absolute', left: 0, top: 0, width: 26, height: 34, opacity: 0, pointerEvents: 'none', transformOrigin: '0 0'}}>
          <svg width="26" height="34" viewBox="0 0 26 34" style={{filter: 'drop-shadow(0 3px 4px rgba(0,0,0,0.35))'}}>
            <path d="M2 2 L2 26 L8.5 20 L13 31 L18 29 L13.5 18.5 L22 18 Z" fill="#1a1230" stroke="#fff" strokeWidth="2" strokeLinejoin="round" />
          </svg>
        </div>
      </div>
    </AbsoluteFill>
  );
};
