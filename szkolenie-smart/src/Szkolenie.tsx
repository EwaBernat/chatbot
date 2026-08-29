import React from 'react';
import {
  AbsoluteFill,
  Audio,
  Series,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
  interpolate,
} from 'remotion';
import {MARKA} from './marka';
import {Awatar} from './Awatar';
import {Napisy} from './Napisy';
import {Tytul} from './sceny/Tytul';
import {Porownanie} from './sceny/Porownanie';
import {Litera} from './sceny/Litera';
import {Kroki} from './sceny/Kroki';
import {Formula} from './sceny/Formula';
import {Czasowniki} from './sceny/Czasowniki';
import {Termometr} from './sceny/Termometr';
import {Obszary} from './sceny/Obszary';
import {Swiatla} from './sceny/Swiatla';
import {Lista} from './sceny/Lista';
import {Zakonczenie} from './sceny/Zakonczenie';
import type {Scena, Scenariusz} from './typy';

export const SZEROKOSC_AWATARA = 660;

const Tresc: React.FC<{scena: Scena}> = ({scena}) => {
  switch (scena.typ) {
    case 'tytul':
      return <Tytul scena={scena} />;
    case 'porownanie':
      return <Porownanie scena={scena} />;
    case 'litera':
      return <Litera scena={scena} />;
    case 'kroki':
      return <Kroki scena={scena} />;
    case 'formula':
      return <Formula scena={scena} />;
    case 'czasowniki':
      return <Czasowniki scena={scena} />;
    case 'termometr':
      return <Termometr scena={scena} />;
    case 'obszary':
      return <Obszary scena={scena} />;
    case 'swiatla':
      return <Swiatla scena={scena} />;
    case 'lista':
      return <Lista scena={scena} />;
    case 'zakonczenie':
      return <Zakonczenie scena={scena} />;
  }
};

/** Miękkie wejście każdej planszy — ekran nie przeskakuje, tylko się przesuwa. */
const Przejscie: React.FC<{children: React.ReactNode}> = ({children}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const t = interpolate(frame, [0, fps * 0.4], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill
      style={{
        display: 'flex',
        opacity: t,
        transform: `translateX(${(1 - t) * 34}px)`,
      }}
    >
      {children}
    </AbsoluteFill>
  );
};

/** Cienka kreska postępu całego szkolenia, u samego dołu kolumny treści. */
const Postep: React.FC = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();

  return (
    <div
      style={{
        position: 'absolute',
        left: SZEROKOSC_AWATARA,
        right: 0,
        bottom: 0,
        height: 6,
        background: MARKA.siatka,
      }}
    >
      <div
        style={{
          height: '100%',
          width: `${(frame / Math.max(1, durationInFrames - 1)) * 100}%`,
          background: MARKA.wyroznienie,
        }}
      />
    </div>
  );
};

export const Szkolenie: React.FC<{scenariusz: Scenariusz}> = ({scenariusz}) => {
  const {fps} = useVideoConfig();

  return (
    <AbsoluteFill style={{background: MARKA.tlo}}>
      {scenariusz.audio ? <Audio src={staticFile(scenariusz.audio)} /> : null}

      <AbsoluteFill style={{flexDirection: 'row'}}>
        <Awatar plik={scenariusz.awatar} szerokosc={SZEROKOSC_AWATARA} />

        <div style={{flex: 1, position: 'relative', overflow: 'hidden'}}>
          <Series>
            {scenariusz.sceny.map((scena) => (
              <Series.Sequence
                key={scena.id}
                durationInFrames={Math.max(1, Math.round(scena.sekundy * fps))}
                layout="none"
              >
                <Przejscie>
                  <Tresc scena={scena} />
                </Przejscie>
              </Series.Sequence>
            ))}
          </Series>
        </div>
      </AbsoluteFill>

      <Postep />
      <Napisy napisy={scenariusz.napisy} />
    </AbsoluteFill>
  );
};
