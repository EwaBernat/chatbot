import React from 'react';
import {AbsoluteFill, useCurrentFrame} from 'remotion';
import {MARKA, FONT} from '../marka';
import {Logo, Pojaw, useWejscie} from '../ui';

/** Podstawa prawna części KPOF — dokładnie jak w skrypcie szkolenia (wydanie 2, po audycie). */
const PODSTAWA = [
  {tytul: 'Rozpoznawanie potrzeb dziecka przez nauczycieli', opis: 'rozporządzenie o pomocy psychologiczno-pedagogicznej — t.j. Dz.U. 2023 poz. 1798'},
  {tytul: 'Arkusz obserwacji jako dokumentacja badań i czynności uzupełniających', opis: 'rozporządzenie o dokumentacji — t.j. Dz.U. 2024 poz. 50'},
  {tytul: 'Podstawa programowa wychowania przedszkolnego', opis: 'Dz.U. 2026 poz. 378 — dziewięć obszarów osiągnięć dziecka; każde twierdzenie odsyła do punktu podstawy'},
  {tytul: 'ICF (WHO 2001) — model biopsychospołeczny', opis: 'rozporządzenie o orzekaniu (Dz.U. 2026 poz. 428) nakazuje opisywać funkcjonowanie w kategoriach aktywności i uczestniczenia'},
];

const Wiersz: React.FC<{w: (typeof PODSTAWA)[number]; od: number}> = ({w, od}) => {
  const p = useWejscie(od, {damping: 14, stiffness: 110});
  return (
    <div style={{display: 'flex', gap: 16, alignItems: 'flex-start', padding: '14px 0', borderBottom: '1px solid rgba(255,255,255,0.12)', opacity: p, transform: `translateX(${(1 - p) * 30}px)`}}>
      <span style={{color: MARKA.pomarancz, fontSize: 22, fontWeight: 900, lineHeight: 1.2}}>✓</span>
      <div>
        <div style={{color: '#fff', fontWeight: 700, fontSize: 24, lineHeight: 1.2}}>{w.tytul}</div>
        <div style={{color: 'rgba(255,255,255,0.72)', fontSize: 18, marginTop: 4, lineHeight: 1.35}}>{w.opis}</div>
      </div>
    </div>
  );
};

export const KpofFinal: React.FC<{haslo: number; prawo: number[]}> = ({haslo, prawo}) => {
  const frame = useCurrentFrame();
  const glow = 0.35 + 0.15 * Math.sin(frame / 12);
  const wPrawo = useWejscie(prawo[0], {damping: 16, stiffness: 90});
  return (
    <AbsoluteFill style={{background: `linear-gradient(160deg, ${MARKA.fioletCiemny} 0%, ${MARKA.fiolet} 55%, #3b2a86 100%)`, fontFamily: FONT}}>
      <div style={{position: 'absolute', left: 460, top: -100, width: 1000, height: 900, borderRadius: '50%', background: `radial-gradient(circle, rgba(232,69,10,${glow}) 0%, rgba(232,69,10,0) 60%)`}} />
      <div style={{position: 'absolute', left: 0, right: 0, top: 0, display: 'flex', flexDirection: 'column', alignItems: 'center', transform: `translateY(${110 - 60 * wPrawo}px)`}}>
        <div style={{transform: `scale(${1 - 0.25 * wPrawo})`, transformOrigin: 'top center', display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
          <Logo rozmiar={130} />
          <div style={{fontSize: 92, fontWeight: 800, color: '#fff', letterSpacing: -2, marginTop: 22, lineHeight: 1}}>
            EduPlaner <span style={{color: '#F6A57E'}}>2026</span>
          </div>
          <Pojaw od={haslo}>
            <div style={{fontSize: 40, color: '#fff', fontWeight: 700, marginTop: 22, letterSpacing: 1}}>Mniej dokumentów. Więcej edukacji.</div>
          </Pojaw>
        </div>
        <div style={{width: 1240, marginTop: 30, background: 'rgba(255,255,255,0.06)', border: '1px solid rgba(255,255,255,0.18)', borderRadius: 22, padding: '22px 34px', opacity: wPrawo}}>
          <div style={{color: MARKA.pomarancz, fontSize: 16, letterSpacing: 3, fontWeight: 700}}>⚖ PODSTAWA PRAWNA KWESTIONARIUSZA KPOF · WG SKRYPTU SZKOLENIA (WYD. 2 PO AUDYCIE)</div>
          {PODSTAWA.map((w, i) => (
            <Wiersz key={w.tytul} w={w} od={prawo[Math.min(i + 1, prawo.length - 1)]} />
          ))}
        </div>
        <Pojaw od={prawo[0] + 20}>
          <div style={{marginTop: 22, fontSize: 18, color: 'rgba(255,255,255,0.6)', letterSpacing: 2}}>EDUPLANER 2026 · PCTP KOSZALIN · kontakt@eduplaner2026.pl · 662 888 403</div>
        </Pojaw>
      </div>
    </AbsoluteFill>
  );
};
