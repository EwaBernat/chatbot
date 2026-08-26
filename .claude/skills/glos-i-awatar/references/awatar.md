# Awatar prowadzącej — układy kadru

Trzy układy pokrywają wszystko, co pojawia się w szkoleniach i podkastach.
Komponenty są w `assets/Awatar.tsx`; wystarczy skopiować plik do `src/`
projektu Remotion.

| Układ | Kiedy | Wywołanie |
|---|---|---|
| **Kółko po prawej** | slajd niesie treść, prowadząca komentuje | `<Awatar plik="awatar/ewa.mp4" />` |
| **Pół ekranu** | rozmowa, podkast, omawianie czegoś na ekranie | `<UkladPolowa plik="…">{ekran}</UkladPolowa>` |
| **Pełny kadr** | powitanie, pointa, zakończenie | `<UkladPelny plik="…" podpis="Mirosława Ewa Jurczyszyn" funkcja="PCTP Koszalin" />` |

## Kółko po prawej

```tsx
<Awatar plik="awatar/ewa.mp4" pozycja="prawy-dol" rozmiar={340} />
```

- `pozycja`: `prawy-dol` (domyślnie), `prawy-srodek`, `prawy-gora`, `lewy-dol`
- `rozmiar`: średnica koła. W kadrze 1920×1080 czyta się dobrze **300–400 px**;
  poniżej 260 twarz przestaje być rozpoznawalna na rzutniku.
- Kółko zasłania róg slajdu — projektując slajdy trzymaj prawy dolny narożnik
  wolny (albo ustaw `pozycja="prawy-gora"`, jeśli treść siedzi na dole).
- Domyślna obwódka to zieleń marki `#9CC4A6`; zmienia się parametrem `obwodka`.

## Pół ekranu

```tsx
<UkladPolowa plik="awatar/ewa.mp4" strona="prawa" udzial={0.42} podpis="Mirosława Ewa Jurczyszyn">
  <Img src={staticFile('slajdy/czesc1/07.png')} style={{width: '100%', height: '100%', objectFit: 'cover'}} />
</UkladPolowa>
```

- `udzial` 0.35–0.5 — ile szerokości zajmuje prowadząca. Przy 0.42 slajd
  zachowuje czytelność, a twarz jest duża.
- Nagranie awatara powinno być **pionowe albo kwadratowe** — kadr jest wąski
  i wysoki, więc materiał 16:9 przycina się do samej twarzy.
- `podpis` rysuje delikatną plakietkę z nazwiskiem u dołu kadru awatara.

## Pełny kadr

Plakietka z nazwiskiem i funkcją pojawia się w lewym dolnym rogu, z
pomarańczowym paskiem marki. Dobre na 5–8 sekund wstępu i na zakończenie.

## Jak nagrać materiał do awatara

- **Kamera na wysokości oczu**, twarz w górnej ⅓ kadru, trochę powietrza nad głową.
- **Światło z przodu** (okno, lampa) — nigdy za plecami, bo powstaje sylwetka.
- **Tło spokojne**: jednolita ściana, regał bez bałaganu. Zielone tło tylko wtedy,
  gdy naprawdę chcesz wycinać postać — inaczej szkoda pracy.
- **Rozdzielczość**: 1080p wystarcza do kółka i do połowy kadru; 4K przydaje się
  tylko, gdy chcesz przycinać kadr w montażu.
- **Długość**: do kółka wystarczy 30–60 sekund spokojnego mówienia lub słuchania —
  materiał zapętla się pod dowolnie długi slajd.
- Pliki trzymaj w `public/awatar/`, nazwane po roli: `ewa-mowi.mp4`,
  `ewa-slucha.mp4`, `ewa-portret.jpg`.

## Zapętlanie krótkiego materiału

Gdy nagranie awatara jest krótsze niż slajd, użyj `<Loop>` z Remotion:

```tsx
<Loop durationInFrames={sekundy(45)}>
  <Awatar plik="awatar/ewa-slucha.mp4" />
</Loop>
```

## Podkast: dwie osoby

`UkladPolowa` z `strona="lewa"` dla gościa i `strona="prawa"` dla prowadzącej
daje klasyczny podział. Gdy mówi jedna osoba, powiększ jej udział do 0.55 i
przygaś drugą (`opacity: 0.75`) — widz od razu wie, kto ma głos.
