/**
 * Awatar prowadzącej — trzy układy używane w filmach szkoleniowych i podkastach.
 *
 *   <Awatar plik="awatar/ewa.mp4" />                       kółko po prawej stronie
 *   <UkladPolowa plik="awatar/ewa.mp4">{ekran}</UkladPolowa>   pół ekranu na pół
 *   <UkladPelny plik="awatar/ewa.mp4" podpis="…" />         pełny kadr (wstęp, zakończenie)
 *
 * Plik może być filmem (mp4/webm/mov) albo zdjęciem (png/jpg) — rozpoznaje się
 * po rozszerzeniu. Wideo jest wyciszone domyślnie, bo ścieżkę lektorską film
 * dokłada osobno; ustaw `zDzwiekiem`, jeśli awatar ma mówić własnym dźwiękiem.
 */
import React from 'react';
import {AbsoluteFill, Img, OffthreadVideo, interpolate, staticFile, useCurrentFrame} from 'remotion';

type Zrodlo = {plik: string; zDzwiekiem?: boolean};

const jestFilmem = (plik: string) => /\.(mp4|webm|mov|m4v)$/i.test(plik);

const Media: React.FC<Zrodlo & {styl?: React.CSSProperties}> = ({plik, zDzwiekiem, styl}) => {
  const wspolne: React.CSSProperties = {width: '100%', height: '100%', objectFit: 'cover', ...styl};
  return jestFilmem(plik) ? (
    <OffthreadVideo src={staticFile(plik)} muted={!zDzwiekiem} style={wspolne} />
  ) : (
    <Img src={staticFile(plik)} style={wspolne} />
  );
};

/* ------------------------------------------------------------------ */
/*  1. KÓŁKO — awatar w kole, domyślnie przy prawej krawędzi           */
/* ------------------------------------------------------------------ */

export type Pozycja = 'prawy-dol' | 'prawy-srodek' | 'prawy-gora' | 'lewy-dol';

export const Awatar: React.FC<
  Zrodlo & {
    pozycja?: Pozycja;
    /** średnica koła w pikselach (kadr 1920×1080: 300–400 czyta się najlepiej) */
    rozmiar?: number;
    /** kolor obwódki — domyślnie zieleń marki */
    obwodka?: string;
    margines?: number;
    /** delikatne wejście na starcie ujęcia */
    wejscie?: boolean;
  }
> = ({plik, zDzwiekiem, pozycja = 'prawy-dol', rozmiar = 340, obwodka = '#9CC4A6', margines = 56, wejscie = true}) => {
  const klatka = useCurrentFrame();
  const skala = wejscie ? interpolate(klatka, [0, 18], [0.86, 1], {extrapolateRight: 'clamp'}) : 1;
  const widocznosc = wejscie ? interpolate(klatka, [0, 14], [0, 1], {extrapolateRight: 'clamp'}) : 1;

  const umiejscowienie: Record<Pozycja, React.CSSProperties> = {
    'prawy-dol': {right: margines, bottom: margines},
    'prawy-srodek': {right: margines, top: `calc(50% - ${rozmiar / 2}px)`},
    'prawy-gora': {right: margines, top: margines},
    'lewy-dol': {left: margines, bottom: margines},
  };

  return (
    <div
      style={{
        position: 'absolute',
        width: rozmiar,
        height: rozmiar,
        borderRadius: '50%',
        overflow: 'hidden',
        border: `6px solid ${obwodka}`,
        boxShadow: '0 24px 60px -18px rgba(0,0,0,.65)',
        transform: `scale(${skala})`,
        opacity: widocznosc,
        ...umiejscowienie[pozycja],
      }}
    >
      <Media plik={plik} zDzwiekiem={zDzwiekiem} />
    </div>
  );
};

/* ------------------------------------------------------------------ */
/*  2. PÓŁ EKRANU — ekran obok mówiącej                                */
/* ------------------------------------------------------------------ */

export const UkladPolowa: React.FC<
  Zrodlo & {
    children: React.ReactNode;
    /** po której stronie stoi prowadząca */
    strona?: 'prawa' | 'lewa';
    /** udział awatara w szerokości kadru (0.35–0.5) */
    udzial?: number;
    tlo?: string;
    odstep?: number;
    podpis?: string;
  }
> = ({plik, zDzwiekiem, children, strona = 'prawa', udzial = 0.42, tlo = '#14231A', odstep = 28, podpis}) => {
  const szerokoscAwatara = `calc(${udzial * 100}% - ${odstep * 1.5}px)`;
  const awatar = (
    <div style={{position: 'relative', width: szerokoscAwatara, height: '100%', borderRadius: 16, overflow: 'hidden'}}>
      <Media plik={plik} zDzwiekiem={zDzwiekiem} />
      {podpis ? (
        <div
          style={{
            position: 'absolute', left: 0, right: 0, bottom: 0,
            padding: '46px 26px 22px',
            background: 'linear-gradient(to top, rgba(10,20,13,.92), transparent)',
            color: '#fff', fontSize: 26, fontWeight: 600, letterSpacing: 0.2,
          }}
        >
          {podpis}
        </div>
      ) : null}
    </div>
  );

  return (
    <AbsoluteFill style={{background: tlo, padding: odstep, display: 'flex', gap: odstep, alignItems: 'stretch'}}>
      {strona === 'lewa' ? awatar : null}
      <div style={{flex: 1, position: 'relative', borderRadius: 16, overflow: 'hidden'}}>{children}</div>
      {strona === 'prawa' ? awatar : null}
    </AbsoluteFill>
  );
};

/* ------------------------------------------------------------------ */
/*  3. PEŁNY KADR — wstęp, zakończenie, wypowiedź do kamery            */
/* ------------------------------------------------------------------ */

export const UkladPelny: React.FC<Zrodlo & {podpis?: string; funkcja?: string}> = ({
  plik, zDzwiekiem, podpis, funkcja,
}) => (
  <AbsoluteFill style={{background: '#14231A'}}>
    <Media plik={plik} zDzwiekiem={zDzwiekiem} />
    {podpis ? (
      <div
        style={{
          position: 'absolute', left: 72, bottom: 72,
          padding: '18px 28px', borderRadius: 10,
          background: 'rgba(20,35,26,.86)', borderLeft: '5px solid #E08A2E', color: '#fff',
        }}
      >
        <div style={{fontSize: 34, fontWeight: 700, letterSpacing: -0.4}}>{podpis}</div>
        {funkcja ? <div style={{fontSize: 20, color: '#9CC4A6', marginTop: 4}}>{funkcja}</div> : null}
      </div>
    ) : null}
  </AbsoluteFill>
);
