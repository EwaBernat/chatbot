import React from 'react';
import { Composition } from 'remotion';
import { Modul, dlugoscModulu, wymiary } from './Modul';
import scenariuszSzkola from './scenariusz.json';
import scenariuszPrzedszkole from './scenariusz-przedszkole.json';
import type { Modul as ModulTyp } from './typy';

// S1…S7 — szkoła podstawowa, P1…P6 — przedszkole. Oba szkolenia dzielą ten sam zestaw scen.
const moduly = [
  ...(scenariuszSzkola as unknown as ModulTyp[]),
  ...(scenariuszPrzedszkole as unknown as ModulTyp[]),
];

export const RemotionRoot: React.FC = () => (
  <>
    {moduly.map((m) => (
      <Composition
        key={m.id}
        id={m.id}
        component={Modul as never}
        durationInFrames={dlugoscModulu(m)}
        defaultProps={{ modul: m } as never}
        {...wymiary}
      />
    ))}
  </>
);
