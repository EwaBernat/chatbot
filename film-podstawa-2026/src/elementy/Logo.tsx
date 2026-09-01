import React from 'react';

/**
 * Znak PCTP — okrągła odznaka z kwiatem, ta sama, która jest w broszurze.
 * Rekonstrukcja wektorowa; przy podmianie na plik źródłowy wystarczy
 * zastąpić zawartość <svg>.
 */
export const ZnakPCTP: React.FC<{ rozmiar?: number }> = ({ rozmiar = 96 }) => (
  <svg viewBox="0 0 600 600" width={rozmiar} height={rozmiar}>
    <defs>
      <radialGradient id="pctpDisc" cx="40%" cy="30%" r="78%">
        <stop offset="0%" stopColor="#6B4795" />
        <stop offset="55%" stopColor="#523277" />
        <stop offset="100%" stopColor="#3B2359" />
      </radialGradient>
    </defs>
    <circle cx="300" cy="300" r="298" fill="#3A2258" />
    <circle cx="300" cy="300" r="288" fill="#CFC5E3" />
    <circle cx="300" cy="300" r="272" fill="#452A6B" />
    <circle cx="300" cy="300" r="264" fill="url(#pctpDisc)" />
    <g stroke="#C79C27" strokeWidth="8.5" strokeLinecap="round" fill="none">
      <path d="M301 190 L301 272" />
      <path d="M247 198 Q262 242 301 272" />
      <path d="M355 198 Q340 242 301 272" />
    </g>
    <g>
      <ellipse cx="245" cy="172" rx="22" ry="43" fill="#9C8BC6" transform="rotate(-30 245 172)" />
      <ellipse cx="357" cy="172" rx="22" ry="43" fill="#9C8BC6" transform="rotate(30 357 172)" />
      <ellipse cx="272" cy="150" rx="24" ry="51" fill="#F0A472" transform="rotate(-14 272 150)" />
      <ellipse cx="330" cy="150" rx="24" ry="51" fill="#EE9660" transform="rotate(14 330 150)" />
      <ellipse cx="301" cy="142" rx="26" ry="56" fill="#E2712F" />
      <circle cx="301" cy="173" r="14" fill="#FFFFFF" />
    </g>
    <text x="300" y="412" textAnchor="middle" fill="#F8F2E7"
          fontFamily="Georgia, 'Times New Roman', serif"
          fontSize="122" fontWeight="700" letterSpacing="4">PCTP</text>
  </svg>
);
