import React from 'react';
import { Composition } from 'remotion';
import { Modul, dlugoscModulu, wymiary } from './Modul';
import scenariusz from './scenariusz.json';
import type { Modul as ModulTyp } from './typy';

const moduly = scenariusz as unknown as ModulTyp[];

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
