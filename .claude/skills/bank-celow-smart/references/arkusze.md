# Arkusze do wydruku i biblioteka symboli

Każdy ze 178 konspektów ma materiał do wydruku — razem 226 arkuszy, wszystkie
na jednej stronie A4 pionowo. Arkusz to nie ilustracja do konspektu, tylko rzecz,
którą nauczyciel wytnie, powiesi albo wypełni.

## Siedem rodzajów

| rodzaj | do czego | potrzebuje symboli |
|---|---|---|
| `karty` | kafle do wycięcia | tak |
| `pasek` | sekwencja z numerami (plan, etapy) | tak |
| `tablica` | plansza bez rozcinania (AAC, zasady) | tak |
| `tabela` | tabela do wypełniania przez nauczyciela | nie |
| `pola` | puste pola z etykietami | nie |
| `etykiety` | karteczki z polem koloru | nie |
| `sciezki` | pasy do przecięcia albo szlaczki do obrysowania (SVG) | nie |

Cztery ostatnie nie potrzebują rysunków i są w konspektach większością — to
dobra wiadomość, bo arkusz bez symboli można dopisać od ręki.

## Gdzie dopisać

`src/karty_druk.py`, słownik `ARKUSZE`, klucz to numer konspektu:

```python
"B3-12": [dict(
    rodzaj="pasek", tytul="Plan dnia do opowiadania",
    wstep="Wydrukuj, wytnij paski i ułóż je na dywanie w kolejności. "
          "Dziecko opowiada, wskazując kolejne obrazki.",
    kolumny=3,
    symbole=["dzien_przyjscie", "dzien_sniadanie", "dzien_zajecia",
             "dzien_obiad", "dzien_powrot"],
)],
```

Wstęp pisz do nauczyciela i mów w nim, **co zrobić z kartką**: wydrukować, wyciąć,
nakleić na karton, powiesić. Bez tego arkusz bywa odkładany, bo nie wiadomo,
czy to materiał dla dziecka, czy pomoc dla dorosłego.

## Budżet strony

Szerokość druku **726 px**, na siatkę zostaje **745 px** po nagłówku arkusza.
Układ pilnują dwie funkcje w `karty_druk.py`:

* `_kolumny(ile, podane)` — dokłada kolumn, gdy kafle nie mieszczą się na stronie,
* `_rozciag(wysokosci, zapas)` — rozciąga pola, gdy zostaje pusta kartka.

Po zmianie układu **zmierz**, nie oglądaj:

```bash
node .claude/skills/bank-celow-smart/scripts/zmierz_a4.mjs
```

Arkusz `tabela` musi mieć `min-width:0` — tabela banku ma `min-width:1080px`
i bez tego wyjątku arkusz ucieka poza krawędź strony.

## Biblioteka symboli

`src/symbole.py`: kod → `(podpis na karcie, opis dla modelu rysującego)`. Podpis
widzi dziecko i nauczyciel; opis jest instrukcją dla modelu i nie trafia do
dokumentu.

**Zanim dodasz nowy symbol, przejrzyj bibliotekę.** Konspekty proszą o materiał
243 razy, ale to wciąż ten sam słownik: plan dnia, mycie rąk, emocje, prośby AAC
wracają w wersji A, B, C i U. Dziecko korzystające z komunikacji obrazkowej musi
widzieć ten sam symbol wszędzie — drugi „podobny” symbol pod jeden konspekt to
błąd merytoryczny, nie oszczędność czasu.

Symbol nienarysowany po prostu nie ma pliku, a arkusz go używający jest pomijany
przy budowaniu. Dokument składa się poprawnie i nie ma po tym śladu — dlatego
`sprawdz_bank.py` liczy arkusze „gotowe do złożenia” osobno od wszystkich.

## Rysowanie symboli

`creative_generate_image`, model `gemini-2.5-flash-image`, `generations_count=1`.
Sprawdzony wzór polecenia:

> Flat vector children's pictogram on a plain white background. No frame, no border,
> no coloured panel behind the object. Subject: `<opis z symbole.py>`. Bold dark
> outline, flat solid fill, uniform colours, no decorative spots or patches,
> no shading, no shadow, no text.

Model potrafi mimo to wstawić rysunek na kolorowym panelu albo posypać go
plamkami. Gdy tak się stanie, nie powtarzaj tego samego polecenia — **zamień
zakazy na opis pozytywny**, to działa:

> Nothing is behind the object: no arch, no square, no circle, no coloured panel,
> no frame, no border — only white.
> Each cloud is filled with one single uniform light grey, exactly the same grey
> across the whole cloud. There are no spots, dots, patches, streaks or any second
> colour anywhere.

Postaci ludzkie w symbolach rysuj jako **to samo dziecko**: krótkie jasne włosy,
brzoskwiniowa skóra, zielona koszulka. Skóra nigdy nie przyjmuje koloru emocji —
przy pierwszym podejściu wyszła czerwona twarz przy złości i zielona przy
zdziwieniu, a wtedy kolor twarzy staje się wskazówką zamiast miny i kart nie da
się ze sobą porównać.

Po pobraniu obrazków: `python3 src/kompresuj_media.py` (kadruje do rysunku,
domyka do kwadratu, zapisuje `k_<kod>.jpg`). Skrypt ma kontrolę `tlo_niebiale()`
i wypisuje ostrzeżenie, gdy któryś róg kadru nie jest biały — potraktuj to
poważnie, bo na wydrukowanej karcie widać wtedy obcy prostokąt, a po wycięciu
nożyczkami ciemną krawędź.

**Obejrzyj rysunki, zanim uznasz je za gotowe.** Najszybciej arkuszem stykowym:
zestaw kilkanaście `k_*.jpg` w jedną siatkę z podpisami i spójrz na całość — błędy
stylu widać dopiero w zestawieniu, nie na pojedynczym obrazku.
