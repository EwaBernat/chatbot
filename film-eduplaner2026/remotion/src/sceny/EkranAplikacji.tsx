import React from 'react';
import { Img, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';
import { FONT, MARKA } from '../marka';
import { Licznik, Podpis, Tlo, ZnakDanePrzykladowe } from '../ui/Chrome';
import { KADR_DOMYSLNY, WIZUAL } from '../wizual';
import type { Scena } from '../typy';

const zrzut = (nazwa: string) => staticFile(`zrzuty/${nazwa}`);

/** Jeden zrzut z aplikacji w ruchu (ken burns) + zaokrąglona „ramka okna". */
const Kadr: React.FC<{
  plik: string;
  krycie: number;
  postep: number;
  kadr: typeof KADR_DOMYSLNY;
}> = ({ plik, krycie, postep, kadr }) => {
  const skala = interpolate(postep, [0, 1], [kadr.odSkali, kadr.doSkali]);
  const y = interpolate(postep, [0, 1], [kadr.odY ?? 0, kadr.doY ?? 0]);
  const x = interpolate(postep, [0, 1], [kadr.odX ?? 0, kadr.doX ?? 0]);
  return (
    <div
      style={{
        position: 'absolute',
        inset: 0,
        opacity: krycie,
        overflow: 'hidden',
      }}
    >
      <Img
        src={zrzut(plik)}
        style={{
          position: 'absolute',
          width: '100%',
          height: '100%',
          objectFit: 'cover',
          transform: `scale(${skala}) translate(${x}%, ${y}%)`,
          transformOrigin: 'center center',
        }}
      />
    </div>
  );
};

/** Dymek-podpis wskazujący element ekranu — po 4 s gaśnie, żeby nie wisiał nad kolejnym kadrem. */
const Dymek: React.FC<{ tekst: string; x: number; y: number; opoznienie: number }> = ({
  tekst,
  x,
  y,
  opoznienie,
}) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  const wejscie = spring({ frame: f - opoznienie, fps, config: { damping: 200 }, durationInFrames: 20 });
  const zniknij = interpolate(f, [opoznienie + fps * 4, opoznienie + fps * 4.5], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const s = wejscie * zniknij;
  if (f < opoznienie - 2 || s <= 0.01) return null;
  return (
    <div
      style={{
        position: 'absolute',
        left: `${x * 100}%`,
        top: `${y * 100}%`,
        transform: `translate(-6px, ${(1 - s) * 14}px) scale(${0.94 + s * 0.06})`,
        opacity: s,
        background: MARKA.bialy,
        color: MARKA.fiolet,
        fontFamily: FONT,
        fontSize: 24,
        fontWeight: 700,
        padding: '12px 20px',
        borderRadius: 6,
        borderBottom: `4px solid ${MARKA.pomarancz}`,
        boxShadow: `0 14px 34px ${MARKA.cien}`,
        whiteSpace: 'nowrap',
      }}
    >
      {tekst}
    </div>
  );
};

/** Nakładka „maszyny do pisania" — pokazuje dopisywanie własnego celu. */
const Maszyna: React.FC<{ tekst: string; opoznienie: number }> = ({ tekst, opoznienie }) => {
  const f = useCurrentFrame();
  const znakow = Math.max(0, Math.floor((f - opoznienie) / 1.4));
  if (f < opoznienie) return null;
  return (
    <div
      style={{
        position: 'absolute',
        left: '12%',
        bottom: '26%',
        width: '58%',
        background: MARKA.bialy,
        border: `2px solid ${MARKA.fioletJasny}`,
        borderRadius: 8,
        padding: '20px 24px',
        fontFamily: FONT,
        fontSize: 30,
        color: MARKA.fiolet,
        boxShadow: `0 18px 40px ${MARKA.cien}`,
      }}
    >
      {tekst.slice(0, znakow)}
      <span style={{ opacity: Math.floor(f / 8) % 2 === 0 ? 1 : 0, color: MARKA.pomarancz }}>|</span>
    </div>
  );
};

/** Trzy hasła wskakujące od dołu (scena o otwartym projekcie). */
const Hasla: React.FC<{ slowa: string[]; opoznienie: number }> = ({ slowa, opoznienie }) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  return (
    <div
      style={{
        position: 'absolute',
        left: 0,
        right: 0,
        bottom: 150,
        display: 'flex',
        justifyContent: 'center',
        gap: 28,
      }}
    >
      {slowa.map((slowo, i) => {
        const s = spring({
          frame: f - (opoznienie + i * 8),
          fps,
          config: { damping: 14, mass: 0.6 },
          durationInFrames: 26,
        });
        return (
          <div
            key={slowo}
            style={{
              opacity: s,
              transform: `translateY(${(1 - s) * 60}px)`,
              background: MARKA.pomarancz,
              color: MARKA.bialy,
              fontFamily: FONT,
              fontSize: 34,
              fontWeight: 700,
              padding: '16px 34px',
              borderRadius: 999,
              boxShadow: `0 16px 36px ${MARKA.cien}`,
            }}
          >
            {slowo}
          </div>
        );
      })}
    </div>
  );
};

/**
 * Scena typu „ekran": kolejne zrzuty aplikacji z ruchem kamery,
 * przejścia na przenikanie, plus nakładki opisowe.
 */
export const EkranAplikacji: React.FC<{ scena: Scena; znakDanePrzykladowe: boolean }> = ({
  scena,
  znakDanePrzykladowe,
}) => {
  const f = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const w = WIZUAL[scena.id] ?? {};
  const n = Math.max(1, scena.zrzuty.length);
  const dlugoscKadru = durationInFrames / n;
  const przenikanie = Math.min(14, dlugoscKadru / 4);

  return (
    <Tlo>
      {scena.zrzuty.map((plik, i) => {
        const start = i * dlugoscKadru;
        const koniec = start + dlugoscKadru;
        const postep = interpolate(f, [start, koniec], [0, 1], {
          extrapolateLeft: 'clamp',
          extrapolateRight: 'clamp',
        });
        const krycie =
          i === 0
            ? interpolate(f, [koniec - przenikanie, koniec], [1, n > 1 ? 0 : 1], {
                extrapolateLeft: 'clamp',
                extrapolateRight: 'clamp',
              })
            : interpolate(
                f,
                [start - przenikanie, start, koniec - przenikanie, koniec],
                [0, 1, 1, i === n - 1 ? 1 : 0],
                { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' },
              );
        return (
          <Kadr
            key={plik}
            plik={plik}
            krycie={krycie}
            postep={postep}
            kadr={w.kadry?.[i] ?? KADR_DOMYSLNY}
          />
        );
      })}

      {/* przygaszenie góry i dołu, żeby napisy marki były czytelne */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background:
            'linear-gradient(180deg, rgba(26,15,66,0.82) 0%, rgba(26,15,66,0.45) 9%, rgba(26,15,66,0) 20%, rgba(26,15,66,0) 60%, rgba(26,15,66,0.4) 88%, rgba(26,15,66,0.72) 100%)',
        }}
      />

      {/* Znaku marki nie dublujemy — zrzut aplikacji ma własny nagłówek EduPlaner 2026. */}
      {scena.licznik ? (
        <Licznik do={scena.licznik.do} opis={scena.licznik.opis} klatekNabijania={fps * 4} />
      ) : null}
      {scena.podpis ? <Podpis tekst={scena.podpis} /> : null}

      {(w.dymki ?? []).map((d) => (
        <Dymek key={d.tekst} tekst={d.tekst} x={d.x} y={d.y} opoznienie={Math.round(d.t * fps)} />
      ))}
      {w.maszyna ? (
        <Maszyna tekst={w.maszyna.tekst} opoznienie={Math.round(w.maszyna.t * fps)} />
      ) : null}
      {w.hasla ? <Hasla slowa={w.hasla.slowa} opoznienie={Math.round(w.hasla.t * fps)} /> : null}

      {w.kontra ? (
        <div
          style={{
            position: 'absolute',
            right: 56,
            top: '46%',
            fontFamily: FONT,
            fontSize: 44,
            fontWeight: 700,
            color: MARKA.bialy,
            textAlign: 'right',
            textShadow: `0 6px 24px ${MARKA.fioletCiemny}`,
            opacity: interpolate(f, [durationInFrames * 0.55, durationInFrames * 0.62], [0, 1], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            }),
          }}
        >
          {w.kontra}
        </div>
      ) : null}

      {znakDanePrzykladowe ? <ZnakDanePrzykladowe /> : null}
    </Tlo>
  );
};
