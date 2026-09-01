# Styl narracji szkoleniowej — wzorzec zatwierdzony

Ten dokument opisuje sposób mówienia, który autorka zaakceptowała
(„teraz jest super") dla filmów szkoleniowych PCTP. Trzymaj się go
we wszystkich częściach szkolenia, żeby materiały brzmiały jednolicie.

## Krótko: jak to brzmi

Ciepła trenerka, która wie, o czym mówi, i nie spieszy się. Nie prezenterka
radiowa, nie lektor reklamy, nie robot czytający listę. Intonacja **zmienia się
zależnie od treści** — inaczej brzmi definicja, inaczej ostrzeżenie, inaczej
zaproszenie do refleksji.

## Model i głos

| co | wartość |
|---|---|
| model | `eleven_v3` — **nigdy** `eleven_multilingual_v2` |
| głos | „Ewa-głos_do skils", `jq4ZUryuBeDqmtkKtBZ4` |
| `generations_count` | 1 (warianty tylko przy szukaniu nowego stylu) |
| format wyjściowy | MP3 z ElevenLabs → korekcja → WAV 48 kHz mono |

`eleven_multilingual_v2` daje płaską, robotyczną recytację — autorka odrzuciła
ją wprost („NAGRANIA SĄ ROBOTYCZNE"). Cała różnica bierze się z tego, że `v3`
czyta wtrącone **znaczniki reżyserskie** w nawiasach kwadratowych.

## Znaczniki reżyserskie

Pisz je po polsku, wewnątrz tekstu, tuż przed fragmentem, którego dotyczą.
Jeden blok narracji ma zwykle 3–5 znaczników — nie jeden na całość i nie
jeden na zdanie.

| rodzaj treści | znacznik |
|---|---|
| powitanie, zaproszenie | `[ciepło, z uśmiechem, jak trenerka witająca salę]` |
| plan, wyliczenie, wyposażenie | `[rzeczowo, porządkująco]` / `[rzeczowo, jak przy wyliczaniu wyposażenia]` |
| definicja, wyjaśnienie mechanizmu | `[spokojnie, z namysłem]` |
| zasada, sedno, puenta | `[z naciskiem]` |
| przestroga, czego nie robić | `[stanowczo]` |
| zastrzeżenie, „to nie diagnoza" | `[łagodnie]` |
| historyjka, przykład dziecka | `[ciepło, jak przy opowiadaniu bajki]` |
| rozmowa z rodzicami, temat trudny | `[spokojnie, z szacunkiem]` |
| podsumowanie, plan działania | `[ciepło, podsumowująco]` |
| pytanie retoryczne do słuchaczki | `[powoli, ciepło, z zaciekawieniem]` |

## Reguła wstępu — najważniejsze

Pierwszy blok każdej części ma **dwa różne tempa**:

1. **Sam tytuł — normalne, płynne tempo.** Autorka odrzuciła obie skrajności:
   przelecenie tytułu w biegu („zaczynasz, jakbyś pędziła") i celebrowanie
   każdego słowa („za wolno, wydłużone").
2. **Reszta wstępu — wolno, z namysłem.** Pytanie retoryczne, odpowiedź
   i metafora mają płynąć spokojnie, z pauzami.

Miara docelowa dla trzech słów tytułu „Budowanie mostów społecznych":

| wersja | czas | werdykt |
|---|---|---|
| szybka | 1,51 s | za szybko |
| wolna | 2,31 s | za wolno |
| **zatwierdzona** | **1,76 s** | „teraz jest super" |

Czyli ok. **0,58 s na słowo tytułu**, a po tytule pauza 0,6–0,7 s.

### Jak to uzyskać, gdy model nie trafi w tempo

Nie generuj całości od nowa — stracisz dobrą resztę. Wygeneruj wersję wolną
(ta częściej wychodzi dobrze w partii środkowej) i **przyspiesz sam początek**:

```bash
# 1. znajdź pauzę po tytule
ffmpeg -i wstep.mp3 -af silencedetect=n=-38dB:d=0.25 -f null - 2>&1 | grep silence

# 2. przyspiesz odcinek do tej pauzy (tu: cięcie 2,66 s, współczynnik 1,32)
ffmpeg -y -i wstep.mp3 -af "atrim=0:2.66,atempo=1.32,asetpts=N/SR/TB" -ar 48000 -ac 1 tytul.wav
ffmpeg -y -i wstep.mp3 -af "atrim=2.66,asetpts=N/SR/TB"              -ar 48000 -ac 1 reszta.wav

# 3. sklej
printf "file 'tytul.wav'\nfile 'reszta.wav'\n" > lista.txt
ffmpeg -y -f concat -safe 0 -i lista.txt -c copy wstep-sklejka.wav
```

`atempo` zmienia tempo bez zmiany wysokości głosu, więc szwu nie słychać.
Trzymaj współczynnik w przedziale **1,2–1,4** — powyżej 1,5 pojawiają się
artefakty i mowa brzmi nerwowo.

## Redakcja tekstu pod głos

- **Pauzy rób interpunkcją, nie wielokropkami.** `Budowanie… mostów…
  społecznych.` każe modelowi wlec każde słowo — to była właśnie odrzucona
  wersja „za wolno". Kropka i przecinek wystarczą.
- **Myślnik** (—) daje ładne zawieszenie głosu przed puentą.
- **Nazwiska i terminy obce** zapisuj tak, jak mają być przeczytane po polsku,
  albo sprawdź nagranie: `Baron-Cohen`, `Francesca Happé`, `Carol Gray`.
- **Jedno zdanie = jedna myśl.** Zdania wielokrotnie złożone model czyta
  monotonnie, bo nie wie, gdzie postawić akcent.
- Sformułowania, na których autorce zależy, wpisz dosłownie — np. „a nasza
  praca **terapeutyczna** to budowanie mostów między torami".

## Po syntezie — obowiązkowa korekcja

Materiał z ElevenLabs wychodzi cichy (ok. −20 LUFS) i ze szczytem przy 0 dB.
Przepuść **każdy blok** przez firmowy łańcuch ze skilla `dane-i-glos`:

```
highpass=f=80,
equalizer=f=300:t=q:w=1.0:g=-2.5,
equalizer=f=2600:t=q:w=1.0:g=3,
treble=g=2.5:f=9000:width_type=q:w=0.7,
deesser=i=0.3,
acompressor=threshold=-19dB:ratio=2.4:attack=15:release=250:makeup=1.5,
alimiter=limit=0.95,
loudnorm=I=-14:TP=-1.2:LRA=9
```

Wyjście: `-ar 48000 -ac 1 -c:a pcm_s16le`. To jest łańcuch **lżejszy** niż ten
dla nagrania z telefonu — synteza nie ma szumu pokoju ani zapadniętej góry,
więc mocna korekcja tylko by ją wysuszyła.

Na koniec `node scripts/oblicz-czas.mjs`, żeby ekspozycja slajdów poszła za
nową długością nagrań.

## Rytm całości

Dla filmu 25-slajdowego jeden blok narracji to **35–75 sekund**. Blok krótszy
niż 30 s zostawia slajd wiszący w ciszy; dłuższy niż 80 s męczy, bo obraz stoi.
Gdy tekst wychodzi dłuższy — podziel slajd, nie przyspieszaj lektora.
