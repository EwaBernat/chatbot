# SEO i podgląd linku

## Adres podstrony

```
/sklep/kolorowy-swiat-emocji
```

Krótko, po polsku, bez numeru części — część 2 dostanie własny adres.

## Tytuł strony (`<title>`, do 60 znaków)

```
Kolorowy Świat Emocji — zeszyt o emocjach dla nastolatka
```

## Opis (`meta description`, do 160 znaków)

```
Zeszyt do zajęć rozwijających kompetencje emocjonalne i społeczne dla młodzieży
ze spektrum autyzmu. 58 stron A4, gra planszowa, karty emocji. PDF do druku.
```

## Podgląd linku w mediach społecznościowych

```html
<meta property="og:type" content="product">
<meta property="og:title" content="Kolorowy Świat Emocji — zeszyt o emocjach dla nastolatka">
<meta property="og:description" content="Pięć emocji, pięć kolorów. Zeszyt do zajęć rozwijających kompetencje emocjonalne i społeczne dla młodzieży ze spektrum autyzmu.">
<meta property="og:image" content="https://www.eduplaner2026.pl/grafiki/og-social.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:url" content="https://www.eduplaner2026.pl/sklep/kolorowy-swiat-emocji">
<meta property="og:locale" content="pl_PL">
<meta name="twitter:card" content="summary_large_image">
```

Grafika: `grafiki/og-social.jpg` (1200×630).
Po wgraniu sprawdź podgląd w debugerach Facebooka i LinkedIna — obie
platformy trzymają link w pamięci podręcznej i po zmianie trzeba ją odświeżyć.

## Frazy, pod które warto pisać teksty na stronie

Główne: `emocje autyzm`, `zeszyt ćwiczeń emocje`, `karty emocji do druku`,
`materiały rewalidacja emocje`, `kompetencje społeczne nastolatek`

Uzupełniające: `pomoc psychologiczno-pedagogiczna materiały`,
`rozpoznawanie emocji spektrum autyzmu`, `gra o emocjach do wydruku`,
`ćwiczenia na emocje dla nastolatka`

Nie upychaj ich w opisie produktu — opis ma sprzedawać, nie zbierać frazy.
Lepiej działa osobny wpis na blogu linkujący do produktu.

## Dane strukturalne produktu

Warto dodać `schema.org/Product` z ceną i dostępnością — dzięki temu wynik
w Google pokaże cenę. Uzupełnij `price` po ustaleniu cennika.

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Kolorowy Świat Emocji — zeszyt ćwiczeń dla nastolatka",
  "image": "https://www.eduplaner2026.pl/grafiki/okladka.jpg",
  "description": "Zeszyt do zajęć rozwijających kompetencje emocjonalne i społeczne dla młodzieży ze spektrum autyzmu.",
  "brand": { "@type": "Brand", "name": "Świat Kolorów" },
  "author": { "@type": "Person", "name": "Mirosława Ewa Jurczyszyn" },
  "publisher": { "@type": "Organization", "name": "Pomorskie Centrum Terapii Pedagogicznej" },
  "inLanguage": "pl",
  "numberOfPages": 58,
  "offers": {
    "@type": "Offer",
    "priceCurrency": "PLN",
    "price": "[ cena ]",
    "availability": "https://schema.org/InStock",
    "url": "https://www.eduplaner2026.pl/sklep/kolorowy-swiat-emocji"
  }
}
```
