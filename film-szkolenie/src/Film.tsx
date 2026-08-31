import React from 'react';
import {
  AbsoluteFill, Audio, Img, OffthreadVideo, Sequence, interpolate, staticFile,
  useCurrentFrame, useVideoConfig,
} from 'remotion';
import {FIGTREE, SANS, zaladujFonty} from './fonty';
import {AUTOR, INSTYTUCJA, MOTYW, PODPROGRAM, PROGRAM} from './motyw';

export type Napis = {t: string; od: number; do: number};

export type Slajd = {
  n: number;
  tytul: string;
  narracja: string;
  obraz: string;
  audio: string;
  /** Napisy z prawdziwym czasem, wyliczone z nagrania lektorskiego. */
  napisy?: Napis[];
  /** Zdjęcie z sali pokazywane na wejściu slajdu, zanim wjedzie treść. */
  foto?: string;
};

export type Odcinek = {klatki: number; maAudio: boolean};

type Props = {
  slajdy: Slajd[];
  odcinki: Odcinek[];
  czesc: string;
  podtytul: string;
  intro: number;
  outro: number;
  /** Zapowiedź czytana na planszy tytułowej, jeśli została nagrana. */
  audioIntro?: string;
  /** Znak PCTP na planszach otwierającej i końcowej. */
  logo?: string;
  /** Awatar prowadzącej w kółku przy prawej krawędzi slajdu (zdjęcie lub film). */
  awatar?: string;
  /** Zdjęcie w tle planszy tytułowej. */
  fotoTytulowe?: string;
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

const Monogram: React.FC<{mowi: boolean}> = ({mowi}) => {
  const klatka = useCurrentFrame();
  // pierścień pulsuje w rytm mowy — kółko żyje, choć nie ma jeszcze nagrania twarzy
  const puls = mowi ? 1 + 0.045 * Math.sin(klatka / 4.2) : 1;
  const inicjaly = AUTOR.split(' ').map((w) => w[0]).join('').slice(0, 3);
  return (
    <div
      style={{
        width: '100%', height: '100%', display: 'flex', flexDirection: 'column',
        alignItems: 'center', justifyContent: 'center', gap: 6,
        background: `radial-gradient(120% 120% at 30% 10%, ${MOTYW.zielenSrednia} 0%, ${MOTYW.zielen} 55%, ${MOTYW.las} 100%)`,
        transform: `scale(${puls})`,
      }}
    >
      <div style={{fontFamily: FIGTREE, fontWeight: 800, fontSize: 62, color: '#fff', letterSpacing: 1}}>{inicjaly}</div>
      <div style={{display: 'flex', alignItems: 'flex-end', gap: 4, height: 20}}>
        {[0, 1, 2, 3, 4].map((i) => (
          <div
            key={i}
            style={{
              width: 4, borderRadius: 2, background: MOTYW.bursztyn,
              height: mowi ? 5 + 13 * Math.abs(Math.sin(klatka / (5 + i * 1.6) + i)) : 5,
            }}
          />
        ))}
      </div>
    </div>
  );
};

const KolkoAwatara: React.FC<{plik?: string; rozmiar?: number}> = ({plik, rozmiar = 232}) => {
  const klatka = useCurrentFrame();
  const skala = interpolate(klatka, [0, 16], [0.9, 1], {extrapolateRight: 'clamp'});
  const film = plik ? /\.(mp4|webm|mov|m4v)$/i.test(plik) : false;
  return (
    <div
      style={{
        position: 'absolute', right: (1920 - OBRAZ_SZER) / 2 + 22, top: 28 + OBRAZ_WYS - rozmiar - 22,
        width: rozmiar, height: rozmiar, borderRadius: '50%', overflow: 'hidden',
        border: `5px solid ${MOTYW.zielenJasna}`, boxShadow: '0 22px 50px -16px rgba(0,0,0,.7)',
        transform: `scale(${skala})`,
      }}
    >
      {!plik ? (
        <Monogram mowi />
      ) : film ? (
        <OffthreadVideo src={staticFile(plik)} muted style={{width: '100%', height: '100%', objectFit: 'cover'}} />
      ) : (
        <Img src={staticFile(plik)} style={{width: '100%', height: '100%', objectFit: 'cover'}} />
      )}
    </div>
  );
};

const Plansza: React.FC<{
  slajd: Slajd; indeks: number; liczba: number; czesc: string; klatki: number; maAudio: boolean; awatar?: string;
}> = ({slajd, indeks, liczba, czesc, klatki, maAudio, awatar}) => {
  const klatka = useCurrentFrame();
  const {fps} = useVideoConfig();

  const wejscie = interpolate(klatka, [0, 14], [0, 1], {extrapolateRight: 'clamp'});
  const przesuniecie = interpolate(klatka, [0, 18], [22, 0], {extrapolateRight: 'clamp'});
  const zblizenie = interpolate(klatka, [0, klatki], [1, 1.018], {extrapolateRight: 'clamp'});
  // zdjęcie trzyma kadr przez pierwsze ~3,5 s slajdu i miękko ustępuje treści
  const trwanieFoto = Math.min(Math.round(klatki * 0.42), 108);
  const nakladka = slajd.foto
    ? interpolate(klatka, [0, 12, trwanieFoto - 18, trwanieFoto], [0, 1, 1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'})
    : 0;
  const fotoZblizenie = interpolate(klatka, [0, trwanieFoto], [1.06, 1], {extrapolateRight: 'clamp'});

  let biezace = '';
  if (slajd.napisy && slajd.napisy.length) {
    // czas wzięty wprost z nagrania — napis pojawia się dokładnie ze słowem
    const sekunda = klatka / fps;
    let ostatni = slajd.napisy[0].t;
    for (const n of slajd.napisy) {
      if (sekunda >= n.od - 0.15) ostatni = n.t;
      if (sekunda >= n.od - 0.15 && sekunda < n.do + 0.45) break;
    }
    biezace = ostatni;
  } else {
    // bez nagrania: zdania dzielone proporcjonalnie do długości
    const zdania = naZdania(slajd.narracja);
    const dlugosci = zdania.map((z) => z.length);
    const suma = dlugosci.reduce((a, b) => a + b, 0) || 1;
    let granica = 0;
    biezace = zdania[0] ?? '';
    for (let i = 0; i < zdania.length; i++) {
      const koniec = granica + (dlugosci[i] / suma) * klatki;
      if (klatka >= granica && klatka < koniec) {
        biezace = zdania[i];
        break;
      }
      granica = koniec;
      biezace = zdania[i];
    }
  }

  const postep = (indeks + Math.min(1, klatka / Math.max(1, klatki))) / liczba;

  return (
    <AbsoluteFill style={{opacity: wejscie}}>
      {maAudio ? <Audio src={staticFile(slajd.audio)} /> : null}

      <div style={{position: 'absolute', top: 28, left: (1920 - OBRAZ_SZER) / 2, transform: `translateY(${przesuniecie}px)`}}>
        <div style={{position: 'relative', width: OBRAZ_SZER, height: OBRAZ_WYS, overflow: 'hidden', borderRadius: 10, boxShadow: '0 30px 70px -20px rgba(0,0,0,.75)'}}>
          <Img
            src={staticFile(slajd.obraz)}
            style={{width: OBRAZ_SZER, height: OBRAZ_WYS, transform: `scale(${zblizenie})`, transformOrigin: 'center'}}
          />
          {slajd.foto ? (
            <div style={{position: 'absolute', inset: 0, opacity: nakladka}}>
              <Img
                src={staticFile(slajd.foto)}
                style={{width: OBRAZ_SZER, height: OBRAZ_WYS, objectFit: 'cover', transform: `scale(${fotoZblizenie})`, transformOrigin: 'center'}}
              />
              <div
                style={{
                  position: 'absolute', inset: 0,
                  background: `linear-gradient(180deg, rgba(46,35,82,.10) 0%, rgba(46,35,82,.18) 52%, rgba(46,35,82,.88) 100%)`,
                }}
              />
              <div style={{position: 'absolute', left: 58, right: 58, bottom: 46}}>
                <div style={{width: 74, height: 4, background: MOTYW.bursztyn, borderRadius: 2, marginBottom: 16}} />
                <div style={{fontFamily: FIGTREE, fontWeight: 800, fontSize: 54, lineHeight: 1.08, color: '#fff', letterSpacing: -1.1}}>
                  {slajd.tytul}
                </div>
              </div>
            </div>
          ) : null}
        </div>
      </div>

      <KolkoAwatara plik={awatar || undefined} />

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

const Intro: React.FC<{czesc: string; podtytul: string; audioIntro?: string; logo?: string; foto?: string}> = ({
  czesc, podtytul, audioIntro, logo, foto,
}) => {
  const klatka = useCurrentFrame();
  const wejscie = interpolate(klatka, [0, 22], [0, 1], {extrapolateRight: 'clamp'});
  const podnies = interpolate(klatka, [0, 30], [26, 0], {extrapolateRight: 'clamp'});
  const najazd = interpolate(klatka, [0, 200], [1.08, 1], {extrapolateRight: 'clamp'});
  const kreska = interpolate(klatka, [24, 54], [0, 260], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});

  return (
    <AbsoluteFill>
      {audioIntro ? <Audio src={staticFile(audioIntro)} /> : null}

      {foto ? (
        <AbsoluteFill>
          <Img src={staticFile(foto)} style={{width: '100%', height: '100%', objectFit: 'cover', transform: `scale(${najazd})`}} />
          <AbsoluteFill
            style={{
              background: `linear-gradient(105deg, rgba(36,28,63,.96) 0%, rgba(46,35,82,.92) 42%, rgba(93,74,138,.62) 78%, rgba(168,143,208,.34) 100%)`,
            }}
          />
        </AbsoluteFill>
      ) : null}

      <AbsoluteFill style={{padding: '0 128px', justifyContent: 'center', opacity: wejscie, transform: `translateY(${podnies}px)`}}>
        <div style={{display: 'flex', alignItems: 'center', gap: 26, marginBottom: 34}}>
          {logo ? (
            <div
              style={{
                width: 108, height: 108, borderRadius: '50%', background: 'rgba(255,255,255,.94)',
                display: 'flex', alignItems: 'center', justifyContent: 'center',
                boxShadow: '0 18px 46px -16px rgba(0,0,0,.6)',
              }}
            >
              <Img src={staticFile(logo)} style={{width: 82, height: 82}} />
            </div>
          ) : null}
          <div>
            <div style={{fontFamily: FIGTREE, fontWeight: 800, fontSize: 26, color: '#fff', letterSpacing: 3}}>PCTP</div>
            <div style={{fontFamily: SANS, fontSize: 17, color: MOTYW.tekstPrzygaszony, letterSpacing: 1.2, marginTop: 3}}>
              Pomorskie Centrum Terapii Pedagogicznej
            </div>
          </div>
        </div>

        <div style={{fontFamily: SANS, fontWeight: 600, fontSize: 19, letterSpacing: 6.4, textTransform: 'uppercase', color: MOTYW.zielenJasna}}>
          {czesc}
        </div>
        <div
          style={{
            fontFamily: FIGTREE, fontWeight: 800, fontSize: 108, lineHeight: 0.98, color: '#fff',
            margin: '22px 0 20px', letterSpacing: -3.2, maxWidth: 1280,
          }}
        >
          {PROGRAM}
        </div>
        <div style={{fontFamily: SANS, fontSize: 36, color: MOTYW.tekst, maxWidth: 1080, lineHeight: 1.35}}>{podtytul}</div>

        <div style={{width: kreska, height: 3, background: MOTYW.bursztyn, borderRadius: 2, margin: '44px 0 30px'}} />

        <div style={{display: 'flex', alignItems: 'flex-end', gap: 60}}>
          <div>
            <div style={{fontFamily: SANS, fontSize: 16, letterSpacing: 2.6, textTransform: 'uppercase', color: MOTYW.tekstPrzygaszony}}>
              Opracowanie i prowadzenie
            </div>
            <div style={{fontFamily: FIGTREE, fontWeight: 800, fontSize: 44, color: '#fff', letterSpacing: -0.8, marginTop: 8}}>
              {AUTOR}
            </div>
            <div style={{fontFamily: SANS, fontSize: 21, color: MOTYW.zielenJasna, marginTop: 6}}>
              pedagog specjalny &nbsp;·&nbsp; {INSTYTUCJA}
            </div>
          </div>
          <div style={{fontFamily: SANS, fontSize: 19, color: MOTYW.tekstPrzygaszony, lineHeight: 1.75, paddingBottom: 6}}>
            kontakt@eduplaner2026.pl
            <br />
            eduplaner2026.pl
          </div>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

const Outro: React.FC<{logo?: string}> = ({logo}) => (
  <Karta
    dzieci={
      <>
        {logo ? <Img src={staticFile(logo)} style={{width: 104, height: 104, marginBottom: 26}} /> : null}
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

export const Film: React.FC<Props> = ({slajdy, odcinki, czesc, podtytul, intro, outro, audioIntro, logo, awatar, fotoTytulowe}) => {
  zaladujFonty();
  let pozycja = intro;

  return (
    <AbsoluteFill style={{background: `radial-gradient(120% 100% at 50% -20%, ${MOTYW.tloJasne} 0%, ${MOTYW.las} 45%, ${MOTYW.tlo} 100%)`}}>
      <Sequence durationInFrames={intro} name="Wstęp">
        <Intro czesc={czesc} podtytul={podtytul} audioIntro={audioIntro} logo={logo} foto={fotoTytulowe} />
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
              awatar={awatar}
            />
          </Sequence>
        );
      })}

      <Sequence from={pozycja} durationInFrames={outro} name="Napisy końcowe">
        <Outro logo={logo} />
      </Sequence>
    </AbsoluteFill>
  );
};
