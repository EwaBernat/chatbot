import React from 'react';
import { useCurrentFrame, useVideoConfig, interpolate, spring } from 'remotion';
import { MARKA, FONT_NAGLOWEK, FONT_TEKST } from '../marka';
import { AwatarPelny } from '../elementy/Awatar';

/**
 * Powitanie — jedyne miejsce, w którym awatar mówi własnym dźwiękiem.
 *
 * Dalsze sceny prowadzi lektor z narracja.mp3, więc ruch ust rozjechałby się
 * z tekstem; dlatego w reszcie filmu postać pojawia się już tylko nieruchomo.
 * Tu przezroczystość pracuje na pełnych obrotach: sylwetka stoi wprost na tle
 * sali, bez ramki i bez koła.
 */
export const Powitanie: React.FC<{ jestAwatar: boolean }> = ({ jestAwatar }) => {
  const klatka = useCurrentFrame();
  const { fps } = useVideoConfig();

  const wejscie = (opoznienie: number) => {
    const s = spring({ frame: klatka - opoznienie, fps, config: { damping: 200, stiffness: 85 } });
    return { opacity: s, transform: `translateY(${interpolate(s, [0, 1], [30, 0])}px)` };
  };

  return (
    <>
      <AwatarPelny jest={jestAwatar} srodekX={1430} skala={1.02} gora={34} opoznienie={4} />

      {/* przyciemnienie po lewej, żeby biały tekst usiadł na tle sali */}
      <div style={{
        position: 'absolute', inset: 0,
        background: 'linear-gradient(100deg, rgba(20,10,52,.92) 0%, rgba(20,10,52,.78) 42%, rgba(20,10,52,0) 66%)',
      }} />

      <div style={{ position: 'absolute', left: 120, top: 250, width: 1000 }}>
        <p style={{ ...wejscie(8), margin: 0,
                    fontFamily: FONT_NAGLOWEK, fontWeight: 700, fontSize: 27,
                    letterSpacing: '.24em', textTransform: 'uppercase',
                    color: MARKA.pomaranczJasny }}>
          Szkolenie · EduPlaner 2026
        </p>

        <h1 style={{ ...wejscie(16), margin: '22px 0 0',
                     fontFamily: FONT_NAGLOWEK, fontWeight: 900,
                     fontSize: 104, lineHeight: .98, letterSpacing: '-.02em',
                     color: '#FFFFFF' }}>
          Nowa podstawa<br />programowa<br />
          <span style={{ color: MARKA.pomaranczJasny }}>w przedszkolu</span>
        </h1>

        <div style={{ ...wejscie(30), marginTop: 34, display: 'flex',
                      alignItems: 'center', gap: 18 }}>
          <span style={{ width: 64, height: 4, background: MARKA.pomarancz }} />
          <p style={{ margin: 0, fontFamily: FONT_TEKST, fontSize: 34,
                      color: MARKA.naCiemnym }}>
            Dziewięć obszarów i podstawa prawna
          </p>
        </div>

        <p style={{ ...wejscie(40), margin: '46px 0 0',
                    fontFamily: FONT_TEKST, fontSize: 27, lineHeight: 1.45,
                    color: MARKA.naCiemnymDrugi }}>
          prowadzi <strong style={{ color: '#fff', fontWeight: 700 }}>
          mgr Mirosława Ewa Jurczyszyn</strong><br />
          pedagog specjalny · PCTP Koszalin
        </p>
      </div>
    </>
  );
};
