import React from 'react';
import {
  OffthreadVideo, Img, staticFile, useCurrentFrame, useVideoConfig,
  interpolate, spring,
} from 'remotion';
import { MARKA, FONT_NAGLOWEK } from '../marka';

/**
 * Awatar wycięty z tła — stoi w sali, nie siedzi w ramce.
 *
 * public/awatar.webm to nagranie z HeyGen po zdjęciu szachownicy
 * (narzedzia/wytnij_tlo.py): VP9 z kanałem alfa, który Chromium — a więc
 * i Remotion — odtwarza z przezroczystością. Dzięki temu postać kładzie się
 * wprost na tle sali przedszkolnej, razem z miękkim cieniem pod stopami.
 *
 * Kadr źródłowy ma 1920×1080, a sylwetka zajmuje w nim x 596–1361
 * (środek 978) i sięga od y≈59 do dolnej krawędzi. Stąd biorą się
 * przesunięcia poniżej: przenoszą ten środek tam, gdzie ma stanąć w kadrze.
 */

const SRODEK_ZRODLA = 978;
const GORA_ZRODLA = 59;

/** Poświata i cień pod postacią — bez nich wycinanka wisi w powietrzu. */
const Osadzenie: React.FC<{ srodekX: number }> = ({ srodekX }) => (
  <>
    <div style={{
      position: 'absolute', left: srodekX - 460, top: 40,
      width: 920, height: 920, borderRadius: '50%',
      background: `radial-gradient(circle, ${MARKA.fioletJasny}55 0%, transparent 68%)`,
      filter: 'blur(40px)',
    }} />
    <div style={{
      position: 'absolute', left: srodekX - 300, bottom: -60,
      width: 600, height: 180, borderRadius: '50%',
      background: 'rgba(10,6,26,.55)', filter: 'blur(46px)',
    }} />
  </>
);

/** Postać w pełnej sylwetce — powitanie i pożegnanie. */
export const AwatarPelny: React.FC<{
  jest: boolean;
  srodekX?: number;
  skala?: number;
  gora?: number;
  opoznienie?: number;
}> = ({ jest, srodekX = 1420, skala = 1.02, gora = 40, opoznienie = 0 }) => {
  const klatka = useCurrentFrame();
  const { fps } = useVideoConfig();
  const wejscie = spring({
    frame: klatka - opoznienie, fps, config: { damping: 200, stiffness: 70 },
  });

  if (!jest) return <BrakAwatara srodekX={srodekX} />;

  const przesuniecieX = srodekX - (960 + (SRODEK_ZRODLA - 960) * skala);
  const przesuniecieY = gora - (540 + (GORA_ZRODLA - 540) * skala);

  return (
    <div style={{
      position: 'absolute', inset: 0,
      opacity: wejscie,
      transform: `translateY(${interpolate(wejscie, [0, 1], [34, 0])}px)`,
    }}>
      <Osadzenie srodekX={srodekX} />
      <OffthreadVideo
        src={staticFile('awatar.webm')}
        transparent
        style={{
          position: 'absolute', inset: 0, width: 1920, height: 1080,
          transform: `translate(${przesuniecieX}px, ${przesuniecieY}px) scale(${skala})`,
          transformOrigin: 'center center',
        }}
      />
    </div>
  );
};

/** Nieruchoma sylwetka — tam, gdzie ruch ust rozjechałby się z lektorem. */
export const AwatarStop: React.FC<{
  jest: boolean;
  srodekX?: number;
  skala?: number;
  gora?: number;
  opoznienie?: number;
}> = ({ jest, srodekX = 1500, skala = 0.9, gora = 120, opoznienie = 0 }) => {
  const klatka = useCurrentFrame();
  const { fps } = useVideoConfig();
  const wejscie = spring({
    frame: klatka - opoznienie, fps, config: { damping: 200, stiffness: 70 },
  });

  if (!jest) return null;

  const przesuniecieX = srodekX - (960 + (SRODEK_ZRODLA - 960) * skala);
  const przesuniecieY = gora - (540 + (GORA_ZRODLA - 540) * skala);

  return (
    <div style={{
      position: 'absolute', inset: 0,
      opacity: wejscie,
      transform: `translateY(${interpolate(wejscie, [0, 1], [26, 0])}px)`,
    }}>
      <Osadzenie srodekX={srodekX} />
      <Img
        src={staticFile('portret-alfa.png')}
        style={{
          position: 'absolute', inset: 0, width: 1920, height: 1080,
          transform: `translate(${przesuniecieX}px, ${przesuniecieY}px) scale(${skala})`,
          transformOrigin: 'center center',
        }}
      />
    </div>
  );
};

/**
 * Awatar w kółeczku w prawym dolnym rogu — prowadząca obecna przez cały film.
 *
 * Kółeczko ma dwa tryby i sam wybiera właściwy:
 *
 * 1. Gdy w public/ leży `awatar-lektor.mp4` — awatar z HeyGen wygenerowany
 *    z gotowego `narracja.mp3` — postać **mówi**, a usta idą za lektorem,
 *    bo to jedno i to samo nagranie.
 * 2. Gdy tego pliku nie ma, w kółeczku jest **nieruchoma sylwetka**.
 *
 * Powitalnego klipu (`awatar.webm`) tu nie puszczamy. Trwa 13 s, powstał do
 * innego tekstu i w pętli pod 11-minutową narracją poruszałby ustami do słów,
 * których nie ma — widz wychwytuje to natychmiast. Lepsza nieruchoma postać
 * niż postać kłamiąca ustami.
 *
 * Żeby włączyć tryb pierwszy, wystarczy wygenerować nagranie i wrzucić je
 * do public/ — kod nie wymaga żadnej zmiany (patrz README, sekcja o awatarze).
 *
 * Nieruchoma sylwetka dostaje bardzo wolny najazd — ruch ledwo zauważalny
 * w skali kółeczka, ale kadr nie wygląda przez to na zacięty.
 *
 * Kadr portretowy liczymy z rzeczywistych wymiarów sylwetki, a nie na oko:
 * czubek głowy jest w źródle na y=62, broda ok. y=400, a głowa ma środek
 * w x=963 (pomiar z kanału alfa). Stąd skala i przesunięcia poniżej —
 * głowa zajmuje ok. 58% wysokości koła i siedzi 10% od jego górnej krawędzi.
 */
const GLOWA_GORA = 62;
const GLOWA_DOL = 400;
const GLOWA_SRODEK_X = 963;

const SREDNICA = 400;
const OBRAMOWANIE = 7;

export const AwatarRog: React.FC<{
  jest: boolean;
  /** nazwa nagrania awatara zsynchronizowanego z lektorem, gdy istnieje */
  mowiace?: string;
  opoznienie?: number;
}> = ({ jest, mowiace, opoznienie = 10 }) => {
  const klatka = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const wejscie = spring({
    frame: klatka - opoznienie, fps, config: { damping: 200, stiffness: 80 },
  });
  // znika przed końcem sekwencji, żeby nie ucinało go twardo na cięciu
  const wyjscie = interpolate(
    klatka, [durationInFrames - 14, durationInFrames - 4], [1, 0],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' },
  );

  if (!jest) return null;

  // najazd o 4% przez cały film — ruch na granicy dostrzegalności
  const najazd = interpolate(klatka, [0, durationInFrames], [1, 1.04]);
  const wnetrze = SREDNICA - OBRAMOWANIE * 2;
  const skala = (wnetrze * 0.58) / (GLOWA_DOL - GLOWA_GORA);
  const lewo = wnetrze / 2 - GLOWA_SRODEK_X * skala;
  const gora = wnetrze * 0.10 - GLOWA_GORA * skala;

  return (
    <div style={{
      position: 'absolute', right: 72, bottom: 96,
      width: SREDNICA, height: SREDNICA,
      opacity: Math.min(wejscie, wyjscie),
      transform: `scale(${interpolate(wejscie, [0, 1], [0.84, 1])})`,
      transformOrigin: 'center center',
    }}>
      <div style={{
        position: 'absolute', inset: 0, borderRadius: '50%',
        overflow: 'hidden',
        border: `${OBRAMOWANIE}px solid ${MARKA.pomaranczJasny}`,
        boxShadow: '0 34px 90px -30px rgba(0,0,0,.8)',
        // wypełnienie pod postacią: przezroczysty awatar musi mieć na czym stanąć
        background: `linear-gradient(160deg, ${MARKA.fioletJasny} 0%, ${MARKA.fioletCiemny} 72%)`,
      }}>
        {mowiace ? (
          <OffthreadVideo
            src={staticFile(mowiace)}
            transparent
            muted
            style={{
              position: 'absolute', left: lewo, top: gora,
              width: 1920 * skala, height: 1080 * skala,
            }}
          />
        ) : (
          <Img
            src={staticFile('portret-alfa.png')}
            style={{
              position: 'absolute', left: lewo, top: gora,
              width: 1920 * skala, height: 1080 * skala,
              transform: `scale(${najazd})`, transformOrigin: '50% 18%',
            }}
          />
        )}
      </div>
    </div>
  );
};

/** Gdy pliku awatara nie ma, film ma się złożyć — z widoczną luką, nie po cichu. */
const BrakAwatara: React.FC<{ srodekX: number }> = ({ srodekX }) => (
  <div style={{
    position: 'absolute', left: srodekX - 210, top: 300,
    width: 420, height: 420, borderRadius: '50%',
    border: `4px dashed ${MARKA.fioletJasny}`,
    display: 'flex', alignItems: 'center', justifyContent: 'center',
    textAlign: 'center', color: MARKA.naCiemnymDrugi,
    fontFamily: FONT_NAGLOWEK, letterSpacing: '.14em', fontSize: 24,
    textTransform: 'uppercase', lineHeight: 1.6,
  }}>
    miejsce<br />na awatar<br />
    <span style={{ fontSize: 15, opacity: .75 }}>public/awatar.webm</span>
  </div>
);
