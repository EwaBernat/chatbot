import React from 'react';

/** Ikony dziewięciu obszarów — te same, które niesie broszura „Cele SMART". */
const RYSUNKI: Record<string, React.ReactNode> = {
  spoleczny: (<>
    <circle cx="9" cy="8.6" r="3" /><circle cx="16.4" cy="10.2" r="2.3" />
    <path d="M3.6 19.4c0-3 2.4-5.2 5.4-5.2s5.4 2.2 5.4 5.2" />
    <path d="M15.4 14.1c2.6.2 4.6 2.3 4.6 5" /></>),
  osobisty: <path d="M12 20.2s-6.8-4.3-6.8-8.8a3.7 3.7 0 0 1 6.8-2.1 3.7 3.7 0 0 1 6.8 2.1c0 4.5-6.8 8.8-6.8 8.8z" />,
  jezykowy: (<>
    <path d="M20.2 12.3c0 3.5-3.7 6.4-8.2 6.4-1 0-2-.15-2.9-.42L4.4 19.9l1.5-3.3c-1-1.2-1.6-2.7-1.6-4.3C4.3 8.8 8 5.9 12.4 5.9s7.8 2.9 7.8 6.4z" />
    <path d="M8.6 11.4h7.2M8.6 14.2h4.4" /></>),
  matematyczny: (<>
    <circle cx="5.6" cy="12" r="2.5" /><rect x="9.6" y="9.5" width="5" height="5" rx="1" />
    <path d="M19 9.2l2.7 5.6h-5.4z" /></>),
  przyrodniczy: (<>
    <path d="M19.4 4.8c.6 8.3-4.5 12-9.6 12-2.6 0-4.4-1.5-4.4-3.9 0-5 6.3-8.1 14-8.1z" />
    <path d="M15.6 8.4C11.8 11 9.2 14.8 7.6 19.6" /></>),
  techniczny: <path d="M17.8 4.4a4.6 4.6 0 0 0-6 5.8L5.1 16.9a1.9 1.9 0 0 0 2.6 2.6l6.7-6.7a4.6 4.6 0 0 0 5.8-6l-2.6 2.6-2.3-.6-.6-2.3 2.6-2.6z" />,
  cyfrowy: (<><rect x="7" y="3.4" width="10" height="17.2" rx="2.2" /><path d="M10.4 17.6h3.2" /></>),
  artystyczny: (<>
    <path d="M12 4.2c4.4 0 8 3.2 8 7.1 0 2.2-1.8 3.4-3.4 3.4h-1.3c-1.1 0-1.9.8-1.9 1.9 0 .5.2.9.5 1.2.3.3.4.6.4 1 0 1-.9 1.6-1.9 1.6-4.4 0-8-3.6-8-8s3.2-8.2 7.6-8.2z" />
    <circle cx="8.4" cy="10.2" r="1" /><circle cx="12" cy="7.9" r="1" /><circle cx="15.6" cy="9.8" r="1" /></>),
  ruchowy: (<>
    <circle cx="14.8" cy="5.4" r="1.9" /><path d="M7.6 20.4l3.2-4.8 3 1.6 1.6 3.2" />
    <path d="M10.8 15.6L9.2 10.8l3.6-2.1 2.6 2.6 2.6.7" /></>),
};

export const IkonaObszaru: React.FC<{ klucz: string; rozmiar?: number; kolor?: string }> = ({
  klucz, rozmiar = 64, kolor = '#FFB48C',
}) => (
  <svg viewBox="0 0 24 24" width={rozmiar} height={rozmiar}
       fill="none" stroke={kolor} strokeWidth={1.6}
       strokeLinecap="round" strokeLinejoin="round">
    {RYSUNKI[klucz] ?? null}
  </svg>
);

export const KLUCZE_OBSZAROW = Object.keys(RYSUNKI);
