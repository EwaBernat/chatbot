import React from 'react';
import {
  AbsoluteFill,
  OffthreadVideo,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
  interpolate,
} from 'remotion';
import {MARKA, FONT} from './marka';

/**
 * Lewa kolumna kadru — panel prowadzącej.
 *
 * Gdy w `public/` leży plik awatara, panel odtwarza go w pętli obrazu na całą
 * wysokość kolumny. Gdy pliku nie ma, panel pokazuje spójną z marką planszę
 * zastępczą: nikt nie renderuje wtedy pustego czarnego prostokąta, a plakietka
 * z nazwiskiem i tak zostaje na swoim miejscu.
 */
const Puls: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const t = frame / fps;

  return (
    <AbsoluteFill style={{alignItems: 'center', justifyContent: 'center'}}>
      {[0, 1, 2].map((i) => {
        const faza = (t * 0.35 + i / 3) % 1;
        return (
          <div
            key={i}
            style={{
              position: 'absolute',
              width: 320 + faza * 300,
              height: 320 + faza * 300,
              borderRadius: '50%',
              border: `2px solid rgba(255, 255, 255, ${0.3 * (1 - faza)})`,
            }}
          />
        );
      })}
      <div
        style={{
          width: 300,
          height: 300,
          borderRadius: '50%',
          background: 'linear-gradient(150deg, #7C5FD3 0%, #2D1B69 100%)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          color: MARKA.bialy,
          fontFamily: FONT,
          fontSize: 104,
          fontWeight: 700,
          letterSpacing: 2,
          boxShadow: '0 24px 60px rgba(0, 0, 0, 0.35)',
        }}
      >
        MJ
      </div>
    </AbsoluteFill>
  );
};

export const Awatar: React.FC<{plik: string | null; szerokosc: number}> = ({
  plik,
  szerokosc,
}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const wejscie = interpolate(frame, [0, fps * 0.8], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <div
      style={{
        position: 'relative',
        width: szerokosc,
        height: '100%',
        overflow: 'hidden',
        background: 'linear-gradient(165deg, #3A2483 0%, #241456 55%, #1A0F3E 100%)',
      }}
    >
      {plik ? (
        <OffthreadVideo
          src={staticFile(plik)}
          muted
          style={{width: '100%', height: '100%', objectFit: 'cover'}}
        />
      ) : (
        <Puls />
      )}

      {/* Winieta — zmiękcza krawędź między panelem a ekranem treści. */}
      <AbsoluteFill
        style={{
          background:
            'linear-gradient(to bottom, rgba(26,15,62,0.45) 0%, rgba(26,15,62,0) 26%, rgba(26,15,62,0) 58%, rgba(26,15,62,0.86) 100%)',
        }}
      />

      <div
        style={{
          position: 'absolute',
          left: 40,
          right: 40,
          bottom: 44,
          opacity: wejscie,
          transform: `translateY(${(1 - wejscie) * 16}px)`,
          fontFamily: FONT,
        }}
      >
        <div
          style={{
            display: 'inline-block',
            padding: '7px 16px',
            borderRadius: 999,
            background: MARKA.wyroznienie,
            color: MARKA.bialy,
            fontSize: 20,
            fontWeight: 700,
            letterSpacing: 1.6,
            textTransform: 'uppercase',
            marginBottom: 16,
          }}
        >
          Prowadzi
        </div>
        <div
          style={{
            color: MARKA.bialy,
            fontSize: 42,
            fontWeight: 700,
            lineHeight: 1.16,
            letterSpacing: -0.6,
          }}
        >
          mgr Mirosława Ewa
          <br />
          Jurczyszyn
        </div>
        <div
          style={{
            color: 'rgba(255,255,255,0.74)',
            fontSize: 24,
            marginTop: 10,
            lineHeight: 1.35,
          }}
        >
          pedagog specjalny
          <br />
          PCTP Koszalin
        </div>
      </div>
    </div>
  );
};
