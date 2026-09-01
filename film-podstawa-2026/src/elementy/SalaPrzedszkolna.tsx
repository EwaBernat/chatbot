import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate } from 'remotion';
import { MARKA } from '../marka';

/**
 * Ilustrowana sala przedszkolna jako tło całego filmu.
 *
 * Rysowana wektorowo, a nie ze zdjęcia: nie ma problemu z licencją, skaluje
 * się do każdej rozdzielczości i trzyma paletę marki. Kolory są celowo
 * przygaszone i przykryte woalem — tło ma budować nastrój, a nie walczyć
 * o uwagę z tekstem plansz.
 *
 * Delikatny paralaksowy dryf (kilka pikseli na minutę) sprawia, że kadr żyje,
 * ale nie odciąga wzroku od treści.
 */
export const SalaPrzedszkolna: React.FC<{ jasnosc?: number }> = ({ jasnosc = 1 }) => {
  const klatka = useCurrentFrame();
  const dryf = Math.sin(klatka / 420) * 14;
  const oddech = 1 + Math.sin(klatka / 520) * 0.012;

  return (
    <AbsoluteFill style={{ backgroundColor: '#EDE7F6', overflow: 'hidden' }}>
      <AbsoluteFill
        style={{ transform: `translateX(${dryf}px) scale(${oddech})`, opacity: jasnosc }}
      >
        <svg viewBox="0 0 1920 1080" style={{ width: '100%', height: '100%' }}>
          <defs>
            <linearGradient id="sciana" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#F6F1FC" />
              <stop offset="100%" stopColor="#E2D9F0" />
            </linearGradient>
            <linearGradient id="swiatlo" x1="0.2" y1="0" x2="0.8" y2="1">
              <stop offset="0%" stopColor="#FFF6E8" stopOpacity="0.85" />
              <stop offset="100%" stopColor="#FFF6E8" stopOpacity="0" />
            </linearGradient>
            <linearGradient id="podloga" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#D8C6AE" />
              <stop offset="100%" stopColor="#C3AC90" />
            </linearGradient>
          </defs>

          <rect width="1920" height="1080" fill="url(#sciana)" />
          <rect y="760" width="1920" height="320" fill="url(#podloga)" />

          {/* okno z wpadającym światłem */}
          <g>
            <rect x="1180" y="140" width="520" height="440" rx="18" fill="#FBFDFF" stroke="#C9BEE2" strokeWidth="8" />
            <path d="M1440 140v440M1180 360h520" stroke="#C9BEE2" strokeWidth="8" />
            <rect x="1180" y="140" width="520" height="440" rx="18" fill="#DCEEFB" opacity="0.55" />
            <circle cx="1330" cy="250" r="46" fill="#FFE9A8" opacity="0.85" />
          </g>
          <path d="M1180 160L1700 200L1520 900L820 860Z" fill="url(#swiatlo)" />

          {/* regał z pojemnikami */}
          <g>
            <rect x="140" y="380" width="440" height="380" rx="10" fill="#E9DCC6" stroke="#CDB894" strokeWidth="6" />
            <path d="M140 505h440M140 630h440M360 380v380" stroke="#CDB894" strokeWidth="6" />
            {[
              [175, 415, MARKA.pomarancz], [265, 415, MARKA.fioletJasny],
              [395, 540, MARKA.zielen],    [485, 540, MARKA.bursztyn],
              [175, 665, MARKA.turkus],    [265, 665, MARKA.pomaranczJasny],
            ].map(([x, y, kolor], i) => (
              <rect key={i} x={x as number} y={y as number} width="72" height="62" rx="8"
                    fill={kolor as string} opacity="0.55" />
            ))}
          </g>

          {/* klocki na podłodze */}
          <g opacity="0.7">
            <rect x="700" y="880" width="86" height="86" rx="10" fill={MARKA.pomarancz} opacity="0.7" />
            <rect x="800" y="905" width="62" height="62" rx="9" fill={MARKA.fioletJasny} opacity="0.7" />
            <path d="M905 967l44-76 44 76z" fill={MARKA.zielen} opacity="0.7" />
            <circle cx="1060" cy="930" r="36" fill={MARKA.bursztyn} opacity="0.7" />
          </g>

          {/* dywan */}
          <ellipse cx="1260" cy="960" rx="470" ry="105" fill={MARKA.fioletJasny} opacity="0.16" />

          {/* roślina */}
          <g opacity="0.8">
            <path d="M1810 760c0-90 30-150 30-150s30 60 30 150z" fill="#3E7D4E" opacity="0.55" />
            <path d="M1770 760c0-70 40-120 70-140" stroke="#3E7D4E" strokeWidth="10" fill="none" opacity="0.55" />
            <rect x="1780" y="758" width="120" height="80" rx="12" fill="#B9702F" opacity="0.6" />
          </g>
        </svg>
      </AbsoluteFill>

      {/* woal — trzyma kontrast tekstu plansz niezależnie od tego, co jest pod spodem */}
      <AbsoluteFill
        style={{
          background:
            'linear-gradient(100deg, rgba(31,17,72,0.90) 0%, rgba(31,17,72,0.74) 46%, rgba(45,27,105,0.30) 100%)',
        }}
      />
    </AbsoluteFill>
  );
};
