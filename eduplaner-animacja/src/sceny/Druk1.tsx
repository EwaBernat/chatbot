import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {Arkusz} from '../Arkusz';
import {MARKA, FONT} from '../marka';
import {Pojaw, Pole, Sekcja, useWejscie} from '../ui';
import type {Z} from '../typy';

const Zasilanie: React.FC<{od: number}> = ({od}) => {
  const frame = useCurrentFrame();
  const w = useWejscie(od, {damping: 12, stiffness: 100});
  const cele = ['WOPFU', 'IPET', 'Ewaluacja'];
  return (
    <div style={{position: 'absolute', left: 1590, top: 330, width: 300, opacity: w, transform: `translateX(${(1 - w) * 60}px)`, fontFamily: FONT}}>
      <div style={{display: 'inline-block', background: MARKA.morskiJasny, color: MARKA.morski, fontWeight: 700, fontSize: 18, padding: '8px 18px', borderRadius: 999, marginBottom: 18}}>
        zasila cały system
      </div>
      {cele.map((c, i) => {
        const wi = useWejscie(od + 10 + i * 10, {damping: 12, stiffness: 110});
        const puls = 0.5 + 0.5 * Math.sin((frame - od) / 6 + i);
        return (
          <div key={c} style={{display: 'flex', alignItems: 'center', gap: 14, marginBottom: 16, opacity: wi, transform: `translateX(${(1 - wi) * 40}px)`}}>
            <div style={{width: 60, height: 3, background: `linear-gradient(90deg, ${MARKA.morski}, rgba(47,143,138,${0.2 + 0.8 * puls}))`, borderRadius: 2}} />
            <div style={{flex: 1, background: '#fff', border: `2px solid ${MARKA.morski}`, borderRadius: 14, padding: '12px 16px', boxShadow: `0 8px 24px rgba(47,143,138,${0.12 + 0.12 * puls})`}}>
              <div style={{fontSize: 20, fontWeight: 700, color: MARKA.fiolet}}>{c}</div>
              <div style={{fontSize: 14, color: MARKA.tekstDrugi, marginTop: 4}}>Maja Dąbrowska · 4-latki · mgr J. Krawczyk</div>
            </div>
          </div>
        );
      })}
    </div>
  );
};

/** Strona 1 metryczki: I Dane dziecka, II Dane przedszkola — pola wypełniają się same. */
export const Druk1: React.FC<{trwanie: number; z: Z}> = ({trwanie, z}) => {
  const frame = useCurrentFrame();
  const zas = z.zasila ?? Math.round(trwanie * 0.7);
  const pl = z.placowka ?? Math.round(trwanie * 0.4);
  // pola sekcji I rozkładają się między początkiem a „placówką", sekcji II — między „placówką" a „zasila"
  const t = (u: number) => (u < 0.36 ? Math.round(10 + (u / 0.36) * (pl - 10)) : Math.round(pl + ((u - 0.36) / 0.3) * (zas - 20 - pl)));
  const przesun = interpolate(frame, [zas - 6, zas + 14], [0, -150], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const tempo = 0.9;
  return (
    <AbsoluteFill>
      <AbsoluteFill style={{transform: `translateX(${przesun}px)`}}>
      <Arkusz strona="Strona 1 z 4 · Karta identyfikacyjna">
        <Pojaw od={4} style={{textAlign: 'center'}}>
          <div style={{display: 'inline-block', background: MARKA.pomarancz, color: '#fff', fontSize: 13, letterSpacing: 1.5, fontWeight: 700, padding: '6px 18px', borderRadius: 999}}>
            KARTA IDENTYFIKACYJNA · TECZKA DZIECKA
          </div>
          <div style={{fontSize: 40, fontWeight: 800, color: MARKA.fiolet, marginTop: 8}}>Metryczka dziecka</div>
          <div style={{fontSize: 14, letterSpacing: 3, color: MARKA.pomarancz, fontWeight: 700, marginTop: 4}}>ZGŁOSZENIE · WOPFU · IPET · EWALUACJA</div>
        </Pojaw>
        <Sekcja numer="I" tytul="DANE DZIECKA" od={t(0.05)} style={{marginTop: 18}} />
        <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '14px 20px', marginTop: 14}}>
          <Pole etykieta="IMIĘ I NAZWISKO" wartosc="Maja Dąbrowska" od={t(0.08)} tempo={tempo} />
          <Pole etykieta="DATA URODZENIA" wartosc="2021-11-03" od={t(0.14)} tempo={tempo} />
          <Pole etykieta="RODZICE / OPIEKUNOWIE PRAWNI" wartosc="Karolina i Rafał Dąbrowscy" od={t(0.2)} tempo={tempo} />
          <Pole etykieta="TELEFON I E-MAIL DO KONTAKTU" wartosc="505 447 900 · karolina.dabrowska@example.com" od={t(0.27)} tempo={0.6} />
        </div>
        <Sekcja numer="II" tytul="DANE PRZEDSZKOLA / PLACÓWKI" od={t(0.36)} style={{marginTop: 22}} />
        <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '14px 20px', marginTop: 14}}>
          <Pole etykieta="NAZWA PRZEDSZKOLA / PLACÓWKI" wartosc="Przedszkole nr 14 im. Kubusia Puchatka w Koszalinie" od={t(0.39)} tempo={0.55} />
          <Pole etykieta="ADRES PLACÓWKI" wartosc="ul. Miła 7, 75-400 Koszalin" od={t(0.42)} tempo={tempo} />
          <Pole etykieta="GRUPA / ODDZIAŁ" wartosc="4-latki" od={t(0.47)} tempo={tempo} />
          <Pole etykieta="ETAP EDUKACYJNY" wartosc="wychowanie przedszkolne" od={t(0.49)} tempo={tempo} />
          <Pole etykieta="WYCHOWAWCA" wartosc="mgr Joanna Krawczyk" od={t(0.53)} tempo={tempo} />
          <Pole etykieta="NR W KSIĘDZE DZIECI" wartosc="19/2025" od={t(0.56)} tempo={tempo} />
        </div>
      </Arkusz>
      </AbsoluteFill>
      <Zasilanie od={zas} />
    </AbsoluteFill>
  );
};
