import React from 'react';
import {
  OffthreadVideo, Img, Loop, staticFile, useCurrentFrame, useVideoConfig,
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
 * Awatar w prawym dolnym rogu — prowadząca obecna przez cały film.
 *
 * Nagranie trwa 13 s, a film ponad jedenaście minut, więc klip chodzi w pętli
 * i **bez dźwięku**: mówi lektor z narracja.mp3. W tej skali ruch ust czyta się
 * jako „prowadząca mówi", a nie jako litery — dlatego pętla tu nie przeszkadza,
 * a nieruchome zdjęcie przez jedenaście minut wyglądałoby na zacięty obraz.
 *
 * Kadrujemy popiersie: pudełko o stałym rozmiarze przycina nagranie, a sylwetka
 * jest w nim ustawiona tak, żeby czubek głowy siedział tuż pod górną krawędzią.
 */
/** Długość nagrania z HeyGen — po tylu sekundach pętla wraca na początek.
 *  Pierwsza i ostatnia klatka mają praktycznie tę samą pozę, więc szew
 *  nie rzuca się w oczy. */
const DLUGOSC_KLIPU = 13.04;
const ROG_SZEROKOSC = 500;
const ROG_WYSOKOSC = 620;

export const AwatarRog: React.FC<{ jest: boolean; opoznienie?: number }> = ({
  jest, opoznienie = 10,
}) => {
  const klatka = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const wejscie = spring({
    frame: klatka - opoznienie, fps, config: { damping: 200, stiffness: 80 },
  });
  // znika razem z końcem sekwencji, żeby nie ucinało go twardo na cięciu
  const wyjscie = interpolate(
    klatka, [durationInFrames - 14, durationInFrames - 4], [1, 0],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' },
  );

  if (!jest) return null;

  // sylwetka ma trafić środkiem w środek pudełka, czubkiem głowy tuż pod górę
  const skala = 0.6;
  const lewo = ROG_SZEROKOSC / 2 - SRODEK_ZRODLA * skala;
  const gora = 8 - GORA_ZRODLA * skala;

  return (
    <div style={{
      position: 'absolute', right: 44, bottom: 0,
      width: ROG_SZEROKOSC, height: ROG_WYSOKOSC,
      opacity: Math.min(wejscie, wyjscie),
      transform: `translateY(${interpolate(wejscie, [0, 1], [40, 0])}px)`,
    }}>
      {/* poświata i cień — bez nich wycinanka odkleja się od tła */}
      <div style={{
        position: 'absolute', left: -40, top: 40, width: 580, height: 580,
        borderRadius: '50%',
        background: `radial-gradient(circle, ${MARKA.fioletJasny}4D 0%, transparent 66%)`,
        filter: 'blur(34px)',
      }} />
      <div style={{
        position: 'absolute', left: 60, bottom: -34, width: 380, height: 120,
        borderRadius: '50%', background: 'rgba(10,6,26,.5)', filter: 'blur(34px)',
      }} />

      <div style={{ position: 'absolute', inset: 0, overflow: 'hidden' }}>
        <Loop durationInFrames={Math.round(DLUGOSC_KLIPU * fps)}>
          <OffthreadVideo
            src={staticFile('awatar.webm')}
            transparent
            muted
            style={{
              position: 'absolute', left: lewo, top: gora,
              width: 1920 * skala, height: 1080 * skala,
            }}
          />
        </Loop>
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
