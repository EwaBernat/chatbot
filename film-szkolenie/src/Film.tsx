import React from 'react';
import {
  AbsoluteFill, Audio, Img, Sequence, interpolate, staticFile,
  useCurrentFrame, useVideoConfig,
} from 'remotion';
import {FIGTREE, SANS, zaladujFonty} from './fonty';
import {AUTOR, INSTYTUCJA, MOTYW, PODPROGRAM, PROGRAM} from './motyw';

export type Slajd = {
  n: number;
  tytul: string;
  narracja: string;
  obraz: string;
  audio: string;
};

export type Odcinek = {klatki: number; maAudio: boolean};

type Props = {
  slajdy: Slajd[];
  odcinki: Odcinek[];
  czesc: string;
  podtytul: string;
  intro: number;
  outro: number;
};

const OBRAZ_SZER = 1620;
const OBRAZ_WYS = Math.round((OBRAZ_SZER * 9) / 16); // 911

/** Dzieli narrację na zdania, żeby napisy zmieniały się w rytmie mowy. */
const naZdania = (tekst: string): string[] => {
  const czesci = tekst.match(/[^.!?]+[.!?]*/g) ?? [tekst];
  const wynik: string[] = [];
  for (const c of czesci) {
    const z = c.trim();
    if (!z) continue;
    const ostatni = wynik[wynik.length - 1];
    // krótkie zdania sklejamy z poprzednim, żeby napis nie migał
    if (ostatni && (ostatni.length < 45 || z.length < 30)) {
      wynik[wynik.length - 1] = ostatni + ' ' + z;
    } else {
      wynik.push(z);
    }
  }
  return wynik;
};

const Tor: React.FC<{postep: number; szerokosc: number}> = ({postep, szerokosc}) => (
  <div style={{position: 'relative', width: szerokosc, height: 12}}>
    <div style={{position: 'absolute', top: 5, left: 0, right: 0, height: 2, background: 'rgba(156,196,166,.28)'}} />
    <div style={{position: 'absolute', top: 5, left: 0, width: szerokosc * postep, height: 2, background: MOTYW.zielenJasna}} />
    <div
      style={{
        position: 'absolute', top: 0, left: Math.max(0, szerokosc * postep - 9),
        width: 18, height: 12, borderRadius: 2, background: MOTYW.bursztyn,
      }}
    />
  </div>
);

const Plansza: React.FC<{
  slajd: Slajd; indeks: number; liczba: number; czesc: string; klatki: number; maAudio: boolean;
}> = ({slajd, indeks, liczba, czesc, klatki, maAudio}) => {
  const klatka = useCurrentFrame();
  const {fps} = useVideoConfig();

  const wejscie = interpolate(klatka, [0, 14], [0, 1], {extrapolateRight: 'clamp'});
  const przesuniecie = interpolate(klatka, [0, 18], [22, 0], {extrapolateRight: 'clamp'});
  const zblizenie = interpolate(klatka, [0, klatki], [1, 1.018], {extrapolateRight: 'clamp'});

  const zdania = naZdania(slajd.narracja);
  const dlugosci = zdania.map((z) => z.length);
  const suma = dlugosci.reduce((a, b) => a + b, 0) || 1;
  let granica = 0;
  let biezace = zdania[0] ?? '';
  for (let i = 0; i < zdania.length; i++) {
    const koniec = granica + (dlugosci[i] / suma) * klatki;
    if (klatka >= granica && klatka < koniec) {
      biezace = zdania[i];
      break;
    }
    granica = koniec;
    biezace = zdania[i];
  }

  const postep = (indeks + Math.min(1, klatka / Math.max(1, klatki))) / liczba;

  return (
    <AbsoluteFill style={{opacity: wejscie}}>
      {maAudio ? <Audio src={staticFile(slajd.audio)} /> : null}

      <div style={{position: 'absolute', top: 28, left: (1920 - OBRAZ_SZER) / 2, transform: `translateY(${przesuniecie}px)`}}>
        <div style={{width: OBRAZ_SZER, height: OBRAZ_WYS, overflow: 'hidden', borderRadius: 10, boxShadow: '0 30px 70px -20px rgba(0,0,0,.75)'}}>
          <Img
            src={staticFile(slajd.obraz)}
            style={{width: OBRAZ_SZER, height: OBRAZ_WYS, transform: `scale(${zblizenie})`, transformOrigin: 'center'}}
          />
        </div>
      </div>

      <div style={{position: 'absolute', top: 956, left: (1920 - OBRAZ_SZER) / 2}}>
        <Tor postep={postep} szerokosc={OBRAZ_SZER} />
      </div>

      <div
        style={{
          position: 'absolute', top: 984, left: (1920 - OBRAZ_SZER) / 2, width: OBRAZ_SZER,
          display: 'flex', alignItems: 'flex-start', gap: 40,
        }}
      >
        <div style={{flex: 1, fontFamily: SANS, fontSize: 27, lineHeight: 1.35, color: MOTYW.tekst, maxWidth: 1240}}>
          {biezace}
        </div>
        <div style={{textAlign: 'right', minWidth: 190}}>
          <div style={{fontFamily: FIGTREE, fontWeight: 800, fontSize: 26, color: MOTYW.zielenJasna, fontVariantNumeric: 'tabular-nums'}}>
            {String(slajd.n).padStart(2, '0')} / {liczba}
          </div>
          <div style={{fontFamily: SANS, fontWeight: 600, fontSize: 14, letterSpacing: 2.4, textTransform: 'uppercase', color: MOTYW.tekstPrzygaszony, marginTop: 6}}>
            {czesc}
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

const Karta: React.FC<{dzieci: React.ReactNode}> = ({dzieci}) => {
  const klatka = useCurrentFrame();
  const pojawienie = interpolate(klatka, [0, 20], [0, 1], {extrapolateRight: 'clamp'});
  return (
    <AbsoluteFill style={{justifyContent: 'center', alignItems: 'center', opacity: pojawienie}}>
      <div style={{textAlign: 'center', maxWidth: 1400}}>{dzieci}</div>
    </AbsoluteFill>
  );
};

const Intro: React.FC<{czesc: string; podtytul: string}> = ({czesc, podtytul}) => (
  <Karta
    dzieci={
      <>
        <div style={{fontFamily: SANS, fontWeight: 600, fontSize: 20, letterSpacing: 6, textTransform: 'uppercase', color: MOTYW.zielenJasna}}>
          {czesc}
        </div>
        <div style={{fontFamily: FIGTREE, fontWeight: 800, fontSize: 96, lineHeight: 1.02, color: '#fff', margin: '26px 0 18px', letterSpacing: -2}}>
          {PROGRAM}
        </div>
        <div style={{fontFamily: SANS, fontSize: 34, color: MOTYW.tekst}}>{podtytul}</div>
        <div style={{width: 220, height: 2, background: MOTYW.zielen, margin: '40px auto 26px'}} />
        <div style={{fontFamily: SANS, fontSize: 22, color: MOTYW.tekstPrzygaszony, lineHeight: 1.6}}>
          Opracowanie: <span style={{color: '#fff', fontWeight: 600}}>{AUTOR}</span>
          <br />
          {INSTYTUCJA}
        </div>
      </>
    }
  />
);

const Outro: React.FC = () => (
  <Karta
    dzieci={
      <>
        <div style={{fontFamily: FIGTREE, fontWeight: 800, fontSize: 64, color: '#fff', letterSpacing: -1.4}}>{PROGRAM}</div>
        <div style={{fontFamily: SANS, fontSize: 26, color: MOTYW.zielenJasna, marginTop: 14}}>{PODPROGRAM}</div>
        <div style={{width: 220, height: 2, background: MOTYW.zielen, margin: '44px auto 30px'}} />
        <div style={{fontFamily: SANS, fontSize: 24, color: MOTYW.tekst, lineHeight: 1.7}}>
          Opracowanie i prowadzenie
          <br />
          <span style={{fontFamily: FIGTREE, fontWeight: 800, fontSize: 40, color: '#fff', letterSpacing: -0.6}}>{AUTOR}</span>
          <br />
          <span style={{color: MOTYW.tekstPrzygaszony}}>{INSTYTUCJA}</span>
        </div>
        <div style={{fontFamily: SANS, fontSize: 18, color: MOTYW.tekstPrzygaszony, marginTop: 46, letterSpacing: 1.4}}>
          Materiał szkoleniowy dla rady pedagogicznej &nbsp;·&nbsp; 2026
        </div>
      </>
    }
  />
);

export const Film: React.FC<Props> = ({slajdy, odcinki, czesc, podtytul, intro, outro}) => {
  zaladujFonty();
  let pozycja = intro;

  return (
    <AbsoluteFill style={{background: `radial-gradient(120% 100% at 50% -20%, ${MOTYW.tloJasne} 0%, ${MOTYW.las} 45%, ${MOTYW.tlo} 100%)`}}>
      <Sequence durationInFrames={intro} name="Wstęp">
        <Intro czesc={czesc} podtytul={podtytul} />
      </Sequence>

      {slajdy.map((slajd, i) => {
        const odcinek = odcinki[i];
        const od = pozycja;
        pozycja += odcinek.klatki;
        return (
          <Sequence key={slajd.n} from={od} durationInFrames={odcinek.klatki} name={`${slajd.n}. ${slajd.tytul}`}>
            <Plansza
              slajd={slajd}
              indeks={i}
              liczba={slajdy.length}
              czesc={czesc}
              klatki={odcinek.klatki}
              maAudio={odcinek.maAudio}
            />
          </Sequence>
        );
      })}

      <Sequence from={pozycja} durationInFrames={outro} name="Napisy końcowe">
        <Outro />
      </Sequence>
    </AbsoluteFill>
  );
};
