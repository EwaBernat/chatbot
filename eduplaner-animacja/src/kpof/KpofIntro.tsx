import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {MARKA, FONT} from '../marka';
import {Kursor, Logo, Pojaw, useWejscie} from '../ui';

const MODULY = ['Metryczka', 'KPOF', 'WOPFU', 'IPET / PEWS', 'Realizacja', 'Ewaluacja'];
const WERSJE = [
  {litera: 'A', wiek: '3–4 lata', twierdzen: '42 twierdzenia', opis: 'wersja podstawowa — także dla dzieci starszych z głęboką niepełnosprawnością'},
  {litera: 'B', wiek: '5 lat', twierdzen: '44 twierdzenia', opis: 'oczekiwania rozwojowe pięciolatka'},
  {litera: 'C', wiek: '6 lat', twierdzen: '44 twierdzenia', opis: 'przed analizą gotowości szkolnej'},
];

/** Przełączenie w aplikacji: z Metryczki na KPOF i wybór wersji dla wieku dziecka. */
export const KpofIntro: React.FC<{klikModul: number; klikWersja: number}> = ({klikModul, klikWersja}) => {
  const frame = useCurrentFrame();
  const aktywnyKpof = frame >= klikModul;
  const wersje = useWejscie(klikModul + 6, {damping: 14, stiffness: 100});
  const wybor = interpolate(frame, [klikWersja, klikWersja + 8], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const zoom = interpolate(frame, [klikWersja + 10, klikWersja + 40], [1, 1.12], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const zakl = (i: number) => {
    const el = document.querySelector<HTMLElement>(`[data-zakladka="${i}"]`);
    if (!el) return {x: 400 + i * 200, y: 140};
    const r = el.getBoundingClientRect();
    return {x: r.left + r.width / 2, y: r.top + r.height / 2};
  };
  void zakl;
  return (
    <AbsoluteFill style={{background: `linear-gradient(135deg, #FBF3EA 0%, ${MARKA.tloCieple} 45%, #F4F1F7 100%)`, fontFamily: FONT}}>
      {/* pasek aplikacji */}
      <Pojaw od={0}>
        <div style={{position: 'absolute', left: 0, right: 0, top: 0, height: 118, background: '#fff', boxShadow: '0 6px 30px rgba(45,27,105,0.10)', display: 'flex', alignItems: 'center', padding: '0 80px', gap: 40}}>
          <div style={{display: 'flex', alignItems: 'center', gap: 16}}>
            <Logo rozmiar={64} />
            <div>
              <div style={{fontSize: 28, fontWeight: 800, color: MARKA.fiolet, lineHeight: 1}}>EduPlaner 2026</div>
              <div style={{fontSize: 12, letterSpacing: 2, color: MARKA.tekstCichy, marginTop: 4}}>ŚCIEŻKA DZIECKA · ZOFIA LEWANDOWSKA · GRUPA BIEDRONKI</div>
            </div>
          </div>
          <div style={{display: 'flex', gap: 10, marginLeft: 40}}>
            {MODULY.map((m, i) => {
              const aktywny = aktywnyKpof ? i === 1 : i === 0;
              return (
                <div
                  key={m}
                  data-zakladka={i}
                  style={{
                    padding: '14px 26px',
                    borderRadius: 999,
                    fontSize: 21,
                    fontWeight: 700,
                    color: aktywny ? '#fff' : MARKA.fiolet,
                    background: aktywny ? MARKA.pomarancz : MARKA.lawenda,
                    boxShadow: aktywny ? '0 10px 24px rgba(232,69,10,0.35)' : 'none',
                    transform: aktywny && i === 1 ? `scale(${1 + 0.06 * Math.max(0, 1 - (frame - klikModul) / 12)})` : 'none',
                  }}
                >
                  {i === 0 ? '✓ ' : ''}{m}
                </div>
              );
            })}
          </div>
        </div>
      </Pojaw>

      {/* wybór wersji */}
      <div style={{position: 'absolute', left: 0, right: 0, top: 190, opacity: wersje, transform: `translateY(${(1 - wersje) * 40}px) scale(${zoom})`, transformOrigin: '38% 60%'}}>
        <div style={{textAlign: 'center'}}>
          <div style={{fontSize: 16, letterSpacing: 3, color: MARKA.morski, fontWeight: 700}}>KWESTIONARIUSZ PRZEDSZKOLNEJ OCENY FUNKCJONALNEJ</div>
          <div style={{fontSize: 56, fontWeight: 800, color: '#2b2440', marginTop: 8, letterSpacing: -1}}>KPOF — wybierz wersję dla wieku dziecka</div>
          <div style={{fontSize: 22, color: MARKA.tekstDrugi, marginTop: 10}}>Ten sam arkusz wypełniają niezależnie nauczyciel, rodzic i specjalista.</div>
        </div>
        <div style={{display: 'flex', gap: 34, justifyContent: 'center', marginTop: 54}}>
          {WERSJE.map((w, i) => {
            const wybrana = i === 0 ? wybor : 0;
            return (
              <div
                key={w.litera}
                data-wersja={i}
                style={{
                  width: 460,
                  background: '#fff',
                  borderRadius: 24,
                  padding: '34px 36px',
                  borderTop: `10px solid ${i === 0 ? MARKA.pomarancz : MARKA.morski}`,
                  boxShadow: wybrana > 0 ? `0 26px 60px rgba(232,69,10,${0.18 + 0.2 * wybrana})` : '0 14px 40px rgba(45,27,105,0.10)',
                  outline: wybrana > 0 ? `${4 * wybrana}px solid ${MARKA.pomarancz}` : 'none',
                  transform: `scale(${1 + 0.04 * wybrana - (i !== 0 ? 0.03 * wybor : 0)})`,
                  opacity: i !== 0 ? 1 - 0.45 * wybor : 1,
                }}
              >
                <div style={{display: 'flex', alignItems: 'center', gap: 18}}>
                  <div style={{width: 74, height: 74, borderRadius: 20, background: i === 0 ? MARKA.pomaranczJasny : MARKA.morskiJasny, color: i === 0 ? MARKA.pomarancz : MARKA.morski, fontSize: 40, fontWeight: 800, display: 'grid', placeItems: 'center'}}>{w.litera}</div>
                  <div>
                    <div style={{fontSize: 34, fontWeight: 800, color: MARKA.fiolet, lineHeight: 1}}>{w.wiek}</div>
                    <div style={{fontSize: 18, color: MARKA.tekstDrugi, marginTop: 6}}>{w.twierdzen} · 9 obszarów ICF</div>
                  </div>
                </div>
                <div style={{fontSize: 18, color: MARKA.tekstDrugi, marginTop: 20, lineHeight: 1.4}}>{w.opis}</div>
                {i === 0 ? (
                  <div style={{marginTop: 18, display: 'inline-block', background: MARKA.pomaranczJasny, color: MARKA.pomarancz, fontWeight: 700, fontSize: 15, padding: '6px 14px', borderRadius: 999, opacity: wybor}}>✓ wybrano</div>
                ) : null}
              </div>
            );
          })}
        </div>
      </div>

      <Kursor
        punkty={[
          {klatka: Math.max(0, klikModul - 40), x: 1300, y: 760},
          {klatka: klikModul - 8, x: 690, y: 62},
          {klatka: klikModul + 14, x: 690, y: 62},
          {klatka: klikWersja - 10, x: 480, y: 560},
        ]}
        klik={klikModul}
        klik2={klikWersja}
      />
    </AbsoluteFill>
  );
};
