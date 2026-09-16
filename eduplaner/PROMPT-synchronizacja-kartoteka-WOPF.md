# EduPlaner 2026 · PROMPT SYNCHRONIZACJI DRUKÓW
## Kartoteka → Metryczka → KPOF → Obserwacje pogłębione → WOPF

**Ekosystem:** EduPlaner2026-MJ-PCTP · PCTP Koszalin
**Zakres tego dokumentu:** od kartoteki ucznia do WOPF **włącznie**. IPET — następny etap (poza zakresem).
**Etap edukacyjny w tej wersji:** przedszkole (grupy 3–4-latki, 5-latki, 6-latki); logika działa też dla szkoły (klasa zamiast grupy).
**Marka:** fiolet `#2D1B69`, pomarańcz `#E8450A`; kolory funkcjonalne: zielony `#0D7D5C` (mocne strony), czerwony `#B8350D` (trudności), teal `#2B6E6E` (sensoryka), amber `#C47A10` (pozycje **sugerowane automatycznie** — do potwierdzenia).

---

## CZĘŚĆ 0 · JAK CZYTAĆ TEN PROMPT

Dokument ma cztery warstwy:

| Część | Co zawiera | Dla kogo |
|---|---|---|
| **I** | Zasada jednego źródła prawdy i łańcuch druków | architekt / generator |
| **II** | Prompt per druk: pola, skąd pobiera, co oddaje dalej, automaty | generator każdego druku |
| **III** | Transkrypcja uporządkowana specyfikacji WOPF (18 sekcji w kolejności druku) | generator WOPF + opisy narracyjne |
| **IV** | Tabela synchronizacji + **lista rzeczy jeszcze niepowiązanych** | do decyzji przed IPET |

Legenda statusów synchronizacji:
✅ powiązane (reguła jednoznaczna) · ⚠️ powiązane częściowo (brakuje reguły lub źródła) · ❌ niepowiązane (nie ma skąd pobrać)

---

## CZĘŚĆ I · ZASADA JEDNEGO ŹRÓDŁA PRAWDY

### I.1 Reguła nadrzędna

> **Każda dana jest wpisywana ręcznie dokładnie RAZ — w druku, który jest jej właścicielem. Każdy kolejny druk ją POBIERA, nigdy nie przepisuje.** Jeśli użytkownik poprawia daną w druku niebędącym właścicielem, aplikacja pyta: „Zaktualizować w źródle (kartoteka/metryczka)?” — i propaguje w dół łańcucha.

### I.2 Łańcuch druków i kierunek przepływu

```
KARTOTEKA  (rejestr placówki: kto, gdzie, jaki dokument, jaki tryb, jaki zespół)
    ↓ id ucznia, etap, grupa, tryb A/B, dokument, koordynator, zespół
METRYCZKA  (karta ucznia: dane osobowe, medyczne, wywiad, rodzaj dokumentacji, daty)
    ↓ + medyczne, wywiad z rodzicem, rodzaj i data dokumentacji, współpraca z poradnią
KPOF       (Karta Podstawowej Obserwacji Funkcjonalnej — OBOWIĄZKOWA u każdego dziecka)
    ↓ + oceny obszarów, średnie, poziomy wsparcia, relacje, konteksty, daty obserwacji
OBSERWACJE POGŁĘBIONE  (opcjonalne, wybierane przez nauczyciela/terapeutę)
    ↓ + profil sensoryczny, ToM / poznanie społeczne, ABC, profil biopsychospołeczny (ICF), inne tabelki
WOPF       (wielospecjalistyczna ocena — składa wszystko + opisy narracyjne + decyzja zespołu)
    ↓ karta zespołu + zestaw załączników
IPET       (następny etap — poza tym promptem)
```

### I.3 Jeden obiekt danych ucznia (rozszerzenie istniejącego `data`)

Istniejące klucze generatorów (`student, team, obs, areas, abc, sens, wopf`) **pozostają bez zmian** — to gwarantuje, że generatory Word/xlsx dalej działają. Nowe druki dopisują warstwy **przed** nimi i **zasilają** je:

```javascript
data = {
  kartoteka:  { /* CZĘŚĆ II.1 */ },
  metryczka:  { /* CZĘŚĆ II.2 */ },
  kpof:       { /* CZĘŚĆ II.3 */ },
  poglebione: { sens, tom, abc, bps, inne, wywiad },   // CZĘŚĆ II.4
  // ——— warstwa zgodności z generatorami (wyliczana, nie wpisywana ręcznie) ———
  student, team, obs, areas, abc, sens, wopf
}
```

**Klucz ucznia:** `kartoteka.id` (format `UCZ-001`, `UCZ-002` …) — ten sam identyfikator we wszystkich drukach, w nazwach plików eksportu JSON i w Bazie xlsx (arkusz Rejestr).

**Wersjonowanie:** każda dokumentacja (pierwsza / okresowa / roczna) to osobny **snapshot** `data` z polem `metryczka.dokumentacja.typ` i datą. Kartoteka trzyma listę snapshotów (`kartoteka.historia[]`), żeby ocena okresowa mogła pokazać zmianę względem poprzedniej.

---

## CZĘŚĆ II · PROMPT PER DRUK

### II.1 KARTOTEKA (rejestr placówki)

**Rola:** właściciel tożsamości ucznia, przypisania do grupy, statusu dokumentu z poradni, trybu i składu zespołu.
**Wpisuje ręcznie:** dyrektor / koordynator, raz na rok szkolny (i przy zmianie dokumentu).

```javascript
kartoteka: {
  id:            'UCZ-001',
  placowka:      'Przedszkole nr …',
  rok_szkolny:   '2026/2027',
  etap:          'przedszkole',            // 'przedszkole' | 'sp' | 'ponadpodstawowa'
  grupa:         'Motylki',                // nazwa grupy / klasa
  poziom:        '5',                      // '3-4' | '5' | '6'  (dla szkoły: numer klasy)
  wychowawca:    'mgr …',
  ksztalcenie:   'ogolnodostepne',         // 'ogolnodostepne' | 'integracyjne' | 'specjalne'

  dokument: {                              // dokument z poradni — jeśli jest
    rodzaj:      'orzeczenie',             // 'orzeczenie' | 'opinia' | 'brak'
    numer:       'PPP-…/2026',
    data_wydania:'dd.mm.rrrr',
    data_dostarczenia: 'dd.mm.rrrr',       // dzień wpływu do placówki — od niego liczy się „pierwsza” dokumentacja
    organ:       'Poradnia PP nr … w …',
    wazny_do:    'etap edukacyjny / dd.mm.rrrr',
    rozpoznanie: 'np. autyzm / afazja / niepełnosprawność ruchowa …',
    zalecenia: {                           // ZAZNACZANE Z TREŚCI ORZECZENIA — źródło dla WOPF §10
      nauczyciel_wspolorganizujacy: true,
      rewalidacja:                  true,
      pomoc_pp: ['logopedyczne','korekcyjno-kompensacyjne','rozwijające kompetencje emocjonalno-społeczne'],
      inne: 'tekst'
    }
  },

  tryb: 'B',                               // WYLICZANE: 'A' = bez orzeczenia (opinia lub brak), 'B' = z orzeczeniem
  koordynator: 'mgr Mirosława Jurczyszyn', // domyślnie
  zespol: [                                // ŹRÓDŁO PRAWDY składu zespołu dla wszystkich druków
    { rola:'Koordynator zespołu', imie_nazwisko:'mgr Mirosława Jurczyszyn', specjalnosc:'pedagog specjalny' },
    { rola:'Wychowawca',           imie_nazwisko:'', specjalnosc:'nauczyciel wychowania przedszkolnego' },
    { rola:'Psycholog',            imie_nazwisko:'', specjalnosc:'' },
    { rola:'Logopeda',             imie_nazwisko:'', specjalnosc:'' },
    { rola:'Terapeuta SI',         imie_nazwisko:'', specjalnosc:'' }
  ],
  historia: [ /* { typ:'pierwsza', data:'…', snapshot_id:'…' } */ ]
}
```

**Automaty kartoteki**
1. `tryb` = `dokument.rodzaj === 'orzeczenie' ? 'B' : 'A'` — nie edytowalne ręcznie, tylko przez zmianę dokumentu.
2. Jeśli `tryb === 'B'` i `ksztalcenie ∈ {ogolnodostepne, integracyjne}` → flaga `wymaga_nwk` (nauczyciel współorganizujący) dostępna do zaznaczenia w `zalecenia`.
3. Zmiana `zespol[]` → pytanie „Zaktualizować zespół w metryczce, KPOF, obserwacjach pogłębionych i WOPF tego ucznia?”.

**Oddaje dalej:** `id, etap, grupa, poziom, wychowawca, ksztalcenie, dokument.*, tryb, koordynator, zespol[]`.

---

### II.2 METRYCZKA (karta ucznia)

**Rola:** właściciel danych osobowych, medycznych, wywiadu z rodzicem, rodzaju i daty dokumentacji, współpracy z poradnią.
**Pobiera z kartoteki (tylko do odczytu, z ikoną 🔗):** id, grupa, poziom, wychowawca, dokument, tryb, koordynator, zespół.

```javascript
metryczka: {
  imie_nazwisko: '', data_urodzenia:'dd.mm.rrrr', wiek:'5 l. 3 m.',   // wiek WYLICZANY na dzień data_przygotowania
  pesel_lub_id:  '', adres:'', rodzice_opiekunowie:'', telefon:'', email:'',

  medyczne: {                              // ŹRÓDŁO dla WOPF §5 i §9.4 — nic tu nie przepisujemy ręcznie dalej
    choroby:  ['np. padaczka'],
    leki:     ['nazwa — dawka — pora'],
    alergie:  [],
    dieta:    '',
    zalecenia_lekarskie: '',
    uwagi:    ''
  },

  wywiad: {                                // ŹRÓDŁO dla WOPF §12 (jakość życia) i §9.6 (efekty)
    rodzic:       { data:'', tresc:'', zainteresowania:'', co_lubi:'', czego_unika:'', sen_jedzenie_rytm:'' },
    wychowawca:   { data:'', tresc:'' },
    nauczyciele:  [ { kto:'', data:'', tresc:'' } ],
    dotychczasowe_dzialania: [ { co:'', kto:'', od_kiedy:'', skutecznosc:'' } ]   // → WOPF §9.6
  },

  dokumentacja: {                          // RODZAJ i DATA — z kalendarza lub własna
    typ:              'pierwsza',          // 'pierwsza' | 'okresowa' | 'roczna'
    termin_domyslny:  '30.09.2026',        // WYLICZANY (patrz automat 1)
    data_przygotowania: '30.09.2026',      // = termin_domyslny, chyba że użytkownik nadpisze
    data_auto:        true,                // false po ręcznej edycji
    okres_obserwacji: { od:'', do:'' }     // WYLICZANY z KPOF (pierwsza i ostatnia data obserwacji)
  },

  wspolpraca_poradnia: { poradnia:'', osoba_kontakt:'', ustalenia:'', data_ostatniego_kontaktu:'' }
}
```

**Automaty metryczki**
1. **Data przygotowania z kalendarza** — na podstawie dzisiejszej daty i roku szkolnego:
   - `pierwsza` → **30 września** roku szkolnego **lub** `kartoteka.dokument.data_dostarczenia + 30 dni`, jeśli dokument wpłynął po 1 września (późniejsza z dat);
   - `okresowa` → **31 stycznia** (opcja 1) **lub** „inny termin” wpisany ręcznie (opcja 2);
   - `roczna` → **30 czerwca** (ostatni tydzień zajęć).
   Pole zawsze edytowalne; po edycji `data_auto=false` i etykieta „data własna”.
2. `wiek` liczony automatycznie na dzień `data_przygotowania`.
3. `poziom` w kartotece a `wiek` — jeśli niezgodne (np. 6-latek w grupie 3–4), ostrzeżenie, nie blokada.

**Oddaje dalej:** dane osobowe → `student.*`; `medyczne` → WOPF §5, §9.4; `wywiad` → WOPF §9.6, §12, §8 (zainteresowania); `dokumentacja` → nagłówek WOPF; `wspolpraca_poradnia` → WOPF §1.

---

### II.3 KPOF — Karta Podstawowej Obserwacji Funkcjonalnej

**Rola:** obserwacja ogólna, **wykonywana u każdego dziecka** (tryb A i B). Właściciel ocen obszarów, średnich, poziomów wsparcia, kontekstów i dat obserwacji.
**Pobiera:** nagłówek z kartoteki + metryczki (tylko odczyt).

```javascript
kpof: {
  obserwator:  [ 'mgr …' ],                // z kartoteka.zespol[] — wybór wielokrotny
  sesje:       [ { data:'', kontekst:'', czas_min:0 } ],   // każda obserwacja to sesja
  konteksty:   [ 'zajęcia dydaktyczne','zabawa swobodna','posiłki','plac zabaw','odpoczynek','zajęcia ruchowe','przyjście/odbiór' ],  // bank dla przedszkola; dla szkoły: lekcje, przerwy, świetlica, stołówka, WF
  metoda:      'naturalistyczna + strukturalna',

  obszary: {                               // 8 obszarów = AREAS_DEF (poznaw, spol, emo, kom, beh, tom, sen, samo)
    poznaw: {
      pozycje: [ { id:'A1', tresc:'Skupia uwagę na zadaniu …', ocena: 3 } ],   // skala 1–4 (patrz automat 1)
      srednia: 3.0,                        // WYLICZANA
      poziom_wsparcia: 'II',               // WYLICZANY (progi — automat 2)
      uwagi: ''
    },
    spol:  { /* jak wyżej; zawiera pozycje „relacje” → WOPF §9.5 */ },
    emo:   {}, kom: {}, beh: {}, tom: {}, sen: {}, samo: {}
  },
  srednia_ogolna: 0,                       // WYLICZANA
  podsumowanie:  '',                       // wolny tekst obserwatora (opcjonalny)
  pola_wypelnione: true                    // WYLICZANE — walidacja przed WOPF
}
```

**Automaty KPOF**
1. **Skala ocen** (propozycja domyślna — do potwierdzenia): `1` = nie wykonuje / wymaga pełnej pomocy, `2` = z dużą pomocą, `3` = z niewielką podpowiedzią, `4` = samodzielnie. Puste pozycje **nie wchodzą** do średniej.
2. **Średnia i poziom wsparcia** (w przedszkolu liczone automatycznie): `srednia = suma/liczba_ocenionych`; progi domyślne — do potwierdzenia:
   - `≥ 3,25` → **Poziom I** (wsparcie minimalne / monitorowanie)
   - `2,25 – 3,24` → **Poziom II** (wsparcie umiarkowane / dostosowania + zajęcia)
   - `< 2,25` → **Poziom III** (wsparcie intensywne / specjalistyczne)
   Poziom można nadpisać ręcznie — wtedy oznaczony jako „ocena zespołu” zamiast „wyliczony”.
3. `okres_obserwacji` w metryczce = min/max dat z `sesje[]`.
4. `pola_wypelnione` = wszystkie 8 obszarów mają ≥ 1 ocenę. Bez tego WOPF pokazuje ostrzeżenie „KPOF niekompletna”.
5. **Mapowanie na warstwę zgodności:** `areas[<id>].frequency/intensity` wyliczane z KPOF (odwrotność średniej: niska średnia → wysoka intensywność trudności), `areas[<id>].diff[]` — sugerowane z pozycji ocenionych na 1–2 (patrz luka L-9 w części IV).

**Oddaje dalej:** oceny, średnie, poziomy → WOPF §6; konteksty i metoda → WOPF §3; relacje (obszar `spol`) → WOPF §9.5; narzędzie „KPOF” → WOPF §4 (zawsze zaznaczone).

---

### II.4 OBSERWACJE POGŁĘBIONE (opcjonalne — wybiera nauczyciel / terapeuta)

**Rola:** narzędzia szczegółowe. Każde wypełnione narzędzie **samo zgłasza się** do WOPF §4 (zastosowane narzędzia) i **samo wypełnia** odpowiadającą mu tabelę w WOPF (§13–§15).
**Pobiera:** nagłówek + zespół (odczyt); obserwator z `kartoteka.zespol[]`.

```javascript
poglebione: {
  sens: {                                  // PROFIL SENSORYCZNY → WOPF §13
    wykonano: true, obserwator:'', data:'',
    kanaly: {                              // 8 kanałów = klucze istniejącego `sens`
      slu:{ pozycje:[{tresc:'',ocena:0}], rating:'high', note:'' },   // rating WYLICZANY z pozycji: high|norm|low|seek
      wzr:{}, dot:{}, pro:{}, prz:{}, sma:{}, wec:{}, ora:{}
    },
    opis_auto: '',                         // GENEROWANY (profesjonalny opis wyników)
    wskazania_auto: { dieta_sensoryczna:'', dostosowania:'' }   // GENEROWANE → WOPF §13b
  },

  tom: {                                   // TEORIA UMYSŁU / POZNANIE SPOŁECZNE → WOPF §14
    wykonano: true, obserwator:'', data:'',
    proby: {                               // 4 pola = AREAS_DEF.tom.fields
      rozpoznawanie_emocji:{ pozycje:[], wynik:'' },
      perspektywa:{}, intencje:{}, metafory:{}
    },
    opis_auto:'', wskazania_auto:''        // GENEROWANE
  },

  abc: {                                   // ANALIZA ZACHOWAŃ TRUDNYCH → istniejące `abc[]` + WOPF §15
    wykonano: false, obserwator:'', data:'',
    zdarzenia: [ { antecedent:'', behavior:'', consequence:'', func:'ucieczka', freq:'' } ]
  },

  bps: {                                   // PROFIL BIOPSYCHOSPOŁECZNY (ICF) → WOPF §9.1, §9.2, §11
    wykonano: false, obserwator:'', data:'',
    cialo:        [ { kod:'b…', opis:'', stopien:0 } ],          // funkcje ciała
    aktywnosc:    [ { kod:'d…', opis:'', wykonanie:0, zdolnosc:0 } ],   // aktywność i uczestnictwo
    srodowisko:   [ { kod:'e…', opis:'', wplyw:'bariera'|'ulatwienie', stopien:0 } ],   // → WOPF §11
    opis_auto:''
  },

  inne: [ { nazwa:'', obserwator:'', data:'', tabela:[], opis_auto:'' } ],   // pozostałe tabelki → WOPF §15

  wywiad: { /* jeśli wywiad prowadzi terapeuta, nie wychowawca — inaczej metryczka.wywiad jest źródłem */ }
}
```

**Automaty obserwacji pogłębionych**
1. `wykonano = true` **wyłącznie** gdy narzędzie ma ≥ 1 wypełnioną pozycję — wtedy trafia do WOPF §4 jako zaznaczone.
2. `sens.kanaly[x].rating` wyliczany z pozycji kanału (progi — luka L-11); zapis do istniejącego `sens[x]` (warstwa zgodności).
3. `abc.zdarzenia[]` kopiowane 1:1 do `abc[]` (warstwa zgodności).
4. `tom.proby.*` zasila `areas.tom.observations.*`.
5. `bps.srodowisko[]` → WOPF §11 (czynniki środowiskowe ICF) — bez ręcznego przepisywania.

---

### II.5 WOPF — Wielospecjalistyczna Ocena Poziomu Funkcjonowania

**Rola:** dokument końcowy etapu. **Nie wpisuje nic, co istnieje wyżej w łańcuchu.** Wpisuje ręcznie tylko: decyzje zespołu, korekty opisów generowanych, podpisy.
Pełna specyfikacja sekcji — **CZĘŚĆ III**. Reguła: każda sekcja WOPF ma trzy warstwy:
- 🔗 **pobrane** (tylko odczyt, z odnośnikiem do druku-źródła),
- ✨ **wygenerowane** (opis narracyjny — edytowalny, z przyciskiem „⟳ Wygeneruj ponownie z danych”),
- ✍️ **decyzja zespołu** (ręczne).

---

## CZĘŚĆ III · TRANSKRYPCJA UPORZĄDKOWANA — WOPF SEKCJA PO SEKCJI

Poniżej Pani dyktowana specyfikacja, uporządkowana w kolejności druku. Przy każdej pozycji: skąd dane, co automatycznie, co sugerowane (amber), co ręczne.

### §1 Nagłówek dokumentu

| Pole | Źródło | Reguła |
|---|---|---|
| Grupa / poziom (3–4, 5, 6-latki) | 🔗 kartoteka.grupa, kartoteka.poziom | odczyt |
| Podstawa wydania opinii/orzeczenia | 🔗 kartoteka.dokument.rodzaj + organ | odczyt; `brak` → „rozpoznanie w placówce” |
| Data i numer dokumentu | 🔗 kartoteka.dokument.numer, data_wydania | odczyt |
| Koordynator zespołu | 🔗 kartoteka.koordynator | odczyt |
| Data sporządzenia dokumentacji | 🔗 metryczka.dokumentacja.data_przygotowania | z kalendarza lub własna (II.2 automat 1) |
| **Rodzaj oceny i tryb** | 🔗 kartoteka.tryb | **A — bez orzeczenia** (opinia lub brak dokumentu; ocena funkcjonalna w ramach pomocy pp) · **B — z orzeczeniem** (WOPF obowiązkowa, Rozp. MEN z 9.08.2017) |
| **Rubryka: jaka to dokumentacja** | 🔗 metryczka.dokumentacja.typ | ☐ **pierwsza** — wrzesień lub moment dostarczenia dokumentu · ☐ **okresowa** — styczeń **lub** inny termin (dwie opcje) · ☐ **okresowa-roczna** — czerwiec |
| Współpraca z poradnią | 🔗 metryczka.wspolpraca_poradnia | odczyt + pole „ustalenia z tej dokumentacji” ✍️ |

### §2 Zespół specjalistów

Tabela: **rola / funkcja · imię i nazwisko · specjalność**.
Przycisk **„⇩ Pobierz skład z kartoteki”** (domyślnie wykonuje się sam, jeśli `kartoteka.zespol[]` niepusty). Jeśli skład był już wpisany w innym druku tego ucznia (KPOF, obserwacje pogłębione), pokazuje: „Skład zgodny z kartoteką ✓” albo „Różnice — scal?”. Ręczne dopisanie osoby → propozycja zapisu do kartoteki.

### §3 Kontekst i metoda obserwacji

- 🔗 `kpof.konteksty[]`, `kpof.metoda`, liczba sesji i łączny czas (wyliczone z `kpof.sesje[]`) — **wypełnia się z automatu**.
- Dla `tryb B` (orzeczenie) **z automatu zaznaczają się jako sugerowane** (kolor amber `#C47A10`, dymek: „Sugerowane na podstawie orzeczenia — dziecko może uczęszczać do grupy ogólnodostępnej; potwierdź lub odznacz”):
  - ☑ zajęcia rewalidacyjne,
  - ☑ zajęcia w małej grupie.
  Po kliknięciu użytkownika pozycja zmienia kolor na fioletowy (potwierdzona) lub znika (odrzucona). W druku: potwierdzone drukują się normalnie, sugerowane-niepotwierdzone drukują się z dopiskiem „(sugerowane)”.

### §4 Zastosowane narzędzia

- ☑ **KPOF** — zaznaczone **zawsze, u wszystkich** (nieodznaczalne, bo KPOF jest obowiązkowa).
- ☑ Profil sensoryczny / ☑ ToM / ☑ ABC / ☑ Profil biopsychospołeczny (ICF) / ☑ inne — **zaznaczają się same**, gdy `poglebione.<x>.wykonano === true` (bo są wypełnione). Nie da się zaznaczyć ręcznie narzędzia, które nie ma danych — zamiast tego link „Wypełnij narzędzie →”.
- ☑ Wywiad z rodzicem / wychowawcą / nauczycielami — zaznaczone, gdy `metryczka.wywiad.*` ma treść.

### §5 Informacje medyczne

🔗 `metryczka.medyczne` — choroby, leki, alergie, dieta, zalecenia lekarskie. **Wskakują bez dodatkowego zapisywania.** Brak danych → „Brak zgłoszonych informacji medycznych (wg metryczki z dn. …)”.

### §6 Tabela: od diagnozy do obserwacji funkcjonalnej

- Kolumna „Diagnoza / rozpoznanie” — 🔗 `kartoteka.dokument.rozpoznanie` (jeśli jest dokument; inaczej „—”).
- Kolumny obszarów **A–H** — 🔗 z KPOF: **wszystkie pola** (pozycje z ocenami), **podsumowanie**, **średnia obszaru** (w przedszkolu liczona automatycznie), **średnia ogólna**, **poziom wsparcia** — **wszystko zaznaczone z automatu**. Nic nie przepisujemy.
- Nagłówek tabeli: „Dane z KPOF z dn. … (obserwator: …)”.

### §7 Charakterystyka funkcjonowania — mocne strony · trudności

Tabela 8 wierszy (obszary A–H) × 2 kolumny (**mocne strony** zielone · **trudności** czerwone).
✨ **Generowane** — „piękny, merytoryczny opis” na podstawie wyników poszczególnych obszarów z KPOF:
- pozycje ocenione 3–4 → mocne strony (zdania pełne, język funkcjonalny, bez etykiet diagnostycznych),
- pozycje ocenione 1–2 → trudności (co, w jakich kontekstach, z jaką pomocą się udaje),
- jeśli dla obszaru istnieje obserwacja pogłębiona (sens → G, tom → F i B, abc → E, bps → wszystkie) — generator **dopisuje informacje tematycznie do właściwego obszaru** i **zaznacza w opisie źródło**: „*Na podstawie profilu sensorycznego (dn. …) …*”, „*Obserwacja ToM potwierdza …*”. Wstęp tabeli: „Opis oparty na KPOF; obserwacje pogłębione (…lista…) wykorzystano również do wzbogacenia obserwacji ogólnej.”
- Każda komórka edytowalna; przycisk ⟳ regeneruje tylko tę komórkę.

### §8 Indywidualne potrzeby, mocne strony, predyspozycje

✨ Generowane, **z ciągłością stylu i treści względem §7** (generator dostaje §7 jako kontekst i ma się do niego odwoływać: „jak wskazano w charakterystyce…”). Cztery pola:
1. **Indywidualne potrzeby rozwojowe i edukacyjne** — z trudności §7 przekute na potrzeby („potrzebuje…”, „wymaga…”), z uwzględnieniem poziomów wsparcia z KPOF.
2. **Mocne strony** — **przeniesione z §7** (kolumna zielona, skondensowana) + ewentualne uzupełnienie.
3. **Zainteresowania i uzdolnienia** — 🔗 `metryczka.wywiad.rodzic.zainteresowania / co_lubi` + obserwacje z KPOF (pozycje 4 w obszarach poznaw/sen/kom) — ⚠️ patrz luka L-3.
4. **Predyspozycje i kierunek rozwoju** — synteza 1–3: na czym budować, w którą stronę prowadzić (to później staje się osią celów IPET).

### §9 Przyczyny niepowodzeń, bariery i ograniczenia

Tabela **wypełniana automatycznie** (✨ z 🔗), każdy wiersz z podanym źródłem:

| Wiersz | Źródło | Reguła generowania |
|---|---|---|
| 9.1 Przyczyny niepowodzeń edukacyjnych | KPOF (obszary z poziomem II/III) + `bps.cialo/aktywnosc` + trudności z §7 + dokument z poradni | zdania przyczynowe: „trudności w … wynikają z …” |
| 9.2 Bariery i ograniczenia uczestnictwa | `bps.aktywnosc` (wykonanie < zdolność) + `bps.srodowisko` (bariery) + KPOF konteksty z najniższymi ocenami | ICF: aktywność vs uczestnictwo |
| 9.3 Ograniczenia sensoryczne | `poglebione.sens` (kanały high/low/seek) + inne obserwacje (KPOF obszar G) | jeśli sens niewykonany → „nie prowadzono profilu sensorycznego; wg KPOF …” |
| 9.4 Uwarunkowania medyczne — leki, choroby | 🔗 `metryczka.medyczne` — **przeniesione**, bez przepisywania | dosłownie z metryczki + wpływ na funkcjonowanie (jeśli podano) |
| 9.5 Trudności włączenia do zajęć | `poglebione.tom` (ocena ToM) + KPOF obszar `spol` (relacje) | „w relacjach z rówieśnikami … (KPOF) — co koresponduje z wynikami ToM …” |
| 9.6 Efekty dotychczasowych działań | 🔗 `metryczka.wywiad.dotychczasowe_dzialania[]` + poprzedni snapshot (jeśli dokumentacja okresowa/roczna) | „co robiono, kto, od kiedy, z jaką skutecznością”; przy pierwszej dokumentacji bez historii → „dotychczas nie prowadzono działań w placówce / działania przed przyjęciem: …” — ⚠️ luka L-2 |

### §10 Zakres i charakter wsparcia

**Przeniesione z tego, co już wyodrębniono w innych drukach** — reguły automatów:

| Pozycja | Reguła | Kolor |
|---|---|---|
| Nauczyciel współorganizujący kształcenie | ☑ gdy `kartoteka.dokument.zalecenia.nauczyciel_wspolorganizujacy === true` **i** `ksztalcenie ∈ {ogolnodostepne, integracyjne}` | fiolet (z orzeczenia) |
| Logopeda | ☑ sugerowane, gdy KPOF obszar `kom` poziom II/III **lub** orzeczenie wymienia zajęcia logopedyczne | amber jeśli tylko z obserwacji, fiolet jeśli z orzeczenia |
| **Zintegrowane działania nauczycieli** | ☑ **zawsze** — oznacza szeroką współpracę na rzecz ucznia (nieodznaczalne, z opisem generowanym: kto i w jakim zakresie, na podstawie `kartoteka.zespol[]`) | fiolet |
| Zalecane formy organizacyjne — **z orzeczenia** | ☑ zajęcia rewalidacyjne **zawsze z automatu przy trybie B**; ☑ pomoc pp (konkretne rodzaje) **tylko jeśli orzeczenie ma taki zapis** (`zalecenia.pomoc_pp[]`) | fiolet |
| Zalecane formy organizacyjne — **z obserwacji** | sugerowane na podstawie wyników KPOF i obserwacji pogłębionych (mapa: `emo`/`spol` II/III → zajęcia rozwijające kompetencje emocjonalno-społeczne; `sen` + profil sensoryczny → SI / dieta sensoryczna; `poznaw` → korekcyjno-kompensacyjne; `kom` → logopedyczne; `samo` → trening samodzielności) | amber, do potwierdzenia |

Pozycje z `FORMS_BANK` (19 form) zaznaczają się według tej samej mapy do `wopf.forms[]`.

### §11 Czynniki środowiskowe (ICF)

✨ z 🔗 `poglebione.bps.srodowisko[]` (kody e-, bariera/ułatwienie, stopień) + obserwacje KPOF (konteksty). Generator grupuje: **ułatwienia** (na czym się oprzeć) / **bariery** (co zmienić). Jeśli `bps` niewykonany → opis tylko z KPOF z adnotacją „profil biopsychospołeczny nie był prowadzony”.

### §12 Jakość życia i dobrostan

✨ z 🔗 obserwacja ogólna (KPOF `podsumowanie`, obszary `emo`, `spol`) + `metryczka.wywiad.rodzic` (sen, jedzenie, rytm dnia, co lubi, czego unika) + `wywiad.wychowawca` + `wywiad.nauczyciele[]`. Struktura: samopoczucie w placówce · relacje · poczucie bezpieczeństwa i sprawczości · sygnały przeciążenia · co podnosi dobrostan.

### §13 Profil sensoryczny

**§13a tabela** — 🔗 z `poglebione.sens.kanaly` — 8 kanałów, pozycje, **oceny zapisane**, rating (nadwrażliwy / w normie / podwrażliwy / poszukujący) z kolorem. ✨ **profesjonalny opis obserwacji** na podstawie zaznaczonych wyników (kanał po kanale; zachowania obserwowalne → interpretacja modulacji; bez diagnozowania „zaburzeń SI”, tylko profil).
**§13b wskazania sensoryczne** — ✨ **dieta sensoryczna** (aktywności, rytm, dawkowanie, kto prowadzi) i **dostosowania** (środowisko, materiały, przejścia, posiłki, ubranie) — **ściśle zgodne z oceną**: nadwrażliwość → redukcja bodźca + przewidywalność; poszukiwanie → dozowane dostarczanie; podwrażliwość → wzmocnienie sygnału.
Jeśli `sens.wykonano === false` → cała sekcja drukuje się jako „nie prowadzono” (jedna linia).

### §14 Teoria umysłu — poznanie społeczne

**§14a tabela** — 🔗 `poglebione.tom.proby` (rozpoznawanie emocji · perspektywa · intencje · metafory/ironia) z wynikami. ✨ opis merytoryczny wyników (co dziecko rozumie, gdzie potrzebuje wsparcia, jak to widać w grupie — odwołanie do KPOF `spol`).
**§14b wskazania** — ✨ strategie: modelowanie, historyjki społeczne, komentowanie stanów mentalnych, TUS w małej grupie — dobrane do wyników prób.

### §15 Pozostałe tabelki z obserwacji pogłębionej

Dla każdego `poglebione.abc`, `poglebione.bps`, `poglebione.inne[]` z `wykonano === true`: 🔗 tabela + ✨ opis. ABC — tabela A/B/C/funkcja/częstotliwość + opis hipotez funkcji zachowań; BPS — profil ciało/aktywność/środowisko + opis.

### §16 Sugerowana decyzja zespołu — opinia

✨ **Generowana opinia** na podstawie wszystkich zebranych danych (§1–§15): rodzaj i tryb, najważniejsze wyniki, poziomy wsparcia, rekomendowane formy, oraz **proponowana decyzja** (patrz luka L-14 — lista decyzji do zdefiniowania). ✍️ Zespół zatwierdza / modyfikuje. Pole „uzasadnienie zmian względem propozycji” (jeśli zespół zmienił).

### §17 Co przechodzi do IPET — karta zespołu

Wygenerowana **lista przeniesień** (tylko odczyt, jako karta zespołu):
- z §1: tryb, dokument, daty → podstawa prawna i metryka IPET
- z §2: zespół → zespół opracowujący IPET
- z §6: poziomy wsparcia → kwalifikacja poziomu wsparcia (I/II/III)
- z §7–§8: mocne strony, potrzeby, kierunek rozwoju → cele SMART (obszar po obszarze)
- z §9: bariery, uwarunkowania medyczne → dostosowania i ograniczenia
- z §10: zakres wsparcia, formy → organizacja zajęć specjalistycznych
- z §11–§12: czynniki środowiskowe, dobrostan → dostosowania projektowania uniwersalnego
- z §13b, §14b: wskazania sensoryczne i ToM → zalecenia specjalistyczne
- z §16: decyzja zespołu → zakres IPET
**Zestaw załączników** (checklist, generowany z `wykonano`): ☑ KPOF · ☑/☐ profil sensoryczny · ☑/☐ ToM · ☑/☐ ABC · ☑/☐ BPS/ICF · ☑/☐ wywiady · ☑ kopia dokumentu z poradni.

### §18 Podpisy i zatwierdzenie

Podpisy zespołu (z §2), koordynatora, dyrektora; data spotkania zespołu; zapoznanie rodzica (data, podpis) — ⚠️ luka L-15.

---

## CZĘŚĆ IV · SYNCHRONIZACJA — TABELA POWIĄZAŃ I LUKI

### IV.1 Tabela synchronizacji (kto jest właścicielem, kto pobiera)

| # | Dana | Właściciel (wpis ręczny) | Pobierają | Reguła | Status |
|---|---|---|---|---|---|
| 1 | id ucznia `UCZ-xxx` | kartoteka | wszystkie | nadawany raz | ✅ |
| 2 | grupa / poziom / etap | kartoteka | metryczka, KPOF, WOPF §1 | odczyt | ✅ |
| 3 | dokument z poradni (rodzaj, nr, data, organ, rozpoznanie) | kartoteka | WOPF §1, §6 | odczyt | ✅ |
| 4 | zalecenia z orzeczenia (NWK, rewalidacja, pp) | kartoteka | WOPF §3, §10 | automat §10 | ⚠️ L-1 |
| 5 | tryb A/B | kartoteka (wyliczany) | WOPF §1 | z rodzaju dokumentu | ⚠️ L-4 |
| 6 | koordynator | kartoteka | WOPF §1, §2 | odczyt | ✅ |
| 7 | zespół specjalistów (rola, nazwisko, specjalność) | kartoteka | metryczka, KPOF, pogłębione, WOPF §2 | „pobierz / scal” | ✅ |
| 8 | dane osobowe, wiek | metryczka | WOPF, Baza | wiek wyliczany | ✅ |
| 9 | informacje medyczne | metryczka | WOPF §5, §9.4 | odczyt | ✅ |
| 10 | rodzaj dokumentacji + data przygotowania | metryczka | WOPF §1 | kalendarz / własna | ✅ |
| 11 | okres obserwacji od–do | KPOF (sesje) → metryczka | WOPF §3 | min/max dat | ✅ |
| 12 | współpraca z poradnią | metryczka | WOPF §1 | odczyt | ⚠️ L-13 |
| 13 | konteksty, metoda, liczba sesji | KPOF | WOPF §3 | automat | ✅ |
| 14 | oceny obszarów, średnie, poziomy wsparcia | KPOF (wyliczane) | WOPF §6, §7, §8, §10 | progi | ⚠️ L-7, L-8 |
| 15 | relacje (obszar spol) | KPOF | WOPF §9.5 | + ToM | ✅ |
| 16 | narzędzia zastosowane | KPOF (zawsze) + pogłębione (`wykonano`) | WOPF §4 | automat | ✅ |
| 17 | profil sensoryczny (oceny, rating) | pogłębione.sens | WOPF §9.3, §13, `sens` | progi rating | ⚠️ L-11 |
| 18 | ToM (próby, wyniki) | pogłębione.tom | WOPF §9.5, §14, `areas.tom` | — | ⚠️ L-12 |
| 19 | ABC | pogłębione.abc | WOPF §15, `abc[]` | 1:1 | ✅ |
| 20 | profil biopsychospołeczny / ICF | pogłębione.bps | WOPF §9.1, §9.2, §11, §15 | — | ❌ L-5 |
| 21 | wywiad z rodzicem / wychowawcą / nauczycielami | metryczka.wywiad | WOPF §8.3, §9.6, §12 | — | ❌ L-2, L-3 |
| 22 | efekty dotychczasowych działań | metryczka.wywiad + poprzedni snapshot | WOPF §9.6 | — | ❌ L-2 |
| 23 | zainteresowania i uzdolnienia | metryczka.wywiad.rodzic | WOPF §8.3 | — | ❌ L-3 |
| 24 | mocne strony / trudności (opisy) | WOPF §7 (generowane) | WOPF §8, §9, §16, IPET | ciągłość stylu | ✅ |
| 25 | formy organizacyjne (`wopf.forms[]`) | WOPF §10 (automat + potwierdzenie) | IPET | mapa obszar→forma | ⚠️ L-10 |
| 26 | metody (`wopf.methods[]`) | — | IPET | — | ❌ L-10 |
| 27 | decyzja zespołu | WOPF §16 | IPET | lista decyzji | ❌ L-14 |
| 28 | podpisy, data spotkania, zapoznanie rodzica | WOPF §18 | IPET | — | ❌ L-15 |
| 29 | historia dokumentacji (pierwsza → okresowa → roczna) | kartoteka.historia | WOPF okresowa (porównanie) | snapshot | ⚠️ L-6 |
| 30 | banki trudności `areas.diff[]` z KPOF | KPOF → warstwa zgodności | WOPF (listy ▸), IPET | mapa pozycja KPOF → bank | ❌ L-9 |

### IV.2 CO W SYNCHRONIZACJI JEST JESZCZE NIEPOWIĄZANE (do decyzji przed IPET)

**L-1 · Zalecenia z orzeczenia nie mają dziś struktury.** Kartoteka trzyma tylko numer i datę. Żeby §10 (NWK, rewalidacja, pp) i §3 (małe grupy) zaznaczały się automatycznie, potrzebne są **checkboxy zaleceń** wpisywane przy rejestracji dokumentu (propozycja w II.1). *Decyzja: przyjąć strukturę `zalecenia{}` z II.1?*

**L-2 · „Efekty dotychczasowych działań” (§9.6) nie mają druku-źródła.** Przy pierwszej dokumentacji nie ma historii. Propozycja: w metryczce lista `dotychczasowe_dzialania[]` (co, kto, od kiedy, skuteczność) + przy okresowej/rocznej automatyczne porównanie z poprzednim snapshotem KPOF (zmiana średnich obszarów). *Decyzja: kto wypełnia — wychowawca w metryczce czy koordynator w WOPF?*

**L-3 · Zainteresowania i uzdolnienia (§8.3) — brak pola w KPOF i metryczce.** Propozycja: 2 pola w wywiadzie z rodzicem (`zainteresowania`, `co_lubi`) + 1 pozycja obserwacyjna w KPOF „przejawia szczególne zainteresowanie / uzdolnienie w …”.

**L-4 · Tryb A — doprecyzować.** „A — bez orzeczenia” obejmuje dziecko **z opinią** i dziecko **bez żadnego dokumentu** (rozpoznanie w placówce)? Wpływa na §1 (podstawa) i na to, czy WOPF jest obowiązkowa czy „ocena funkcjonalna” w ramach pomocy pp. Propozycja: A1 = opinia, A2 = bez dokumentu — w druku nadal jeden tryb A z podtypem.

**L-5 · Profil biopsychospołeczny (ICF) nie istnieje jako druk.** Jest wymieniany jako źródło dla §9.1, §9.2 i §11, ale nie ma go na liście druków (kartoteka, metryczka, KPOF, pogłębione). Trzeba go zdefiniować w obserwacjach pogłębionych: lista kodów ICF (b-, d-, e-) dla przedszkola, skala 0–4, bariera/ułatwienie. *Bez tego §11 i §9.2 generują się tylko z KPOF.*

**L-6 · Wersjonowanie dokumentacji.** Pierwsza / okresowa / roczna to osobne snapshoty; dziś model ma jedną `data.student.date`. Potrzebna `kartoteka.historia[]` i reguła: ocena okresowa **pobiera** poprzednią KPOF do porównania (Δ średnich), roczna — obie poprzednie.

**L-7 · Skala ocen KPOF i sposób liczenia średnich.** „W przedszkolu oblicz średnie” — ale skala (1–4? 0–3?), czy pozycje nieocenione pomija się, czy średnia ogólna to średnia z 8 obszarów czy ze wszystkich pozycji — **do potwierdzenia** (propozycja w II.3). *Dla szkoły: liczyć tak samo czy inaczej?*

**L-8 · Progi poziomów wsparcia (I / II / III).** Poziom ma się „zaznaczać automatycznie” — propozycja progów w II.3 automat 2 jest robocza. *Potwierdzić progi i czy poziom liczy się per obszar, ogólnie, czy oba.*

**L-9 · Mapowanie pozycji KPOF → banki trudności (`AREAS_DEF[x].difficulties[]`).** WOPF w Wordzie i IPET pracują na indeksach banków. Żeby KPOF automatycznie zaznaczała trudności (a potem cele), każda pozycja KPOF ocenioną na 1–2 musi mieć przypisany indeks w banku. **Tej mapy nie ma.** *To największa luka na styku z IPET — cele SMART w IPET biorą się z `goals[]`, a `goals[]` nie mają dziś żadnego źródła w KPOF.*

**L-10 · Metody pracy (`METHODS_BANK`, 24) — brak jakiegokolwiek źródła.** Formy (`FORMS_BANK`) mają roboczą mapę obszar→forma (§10), metody nie mają. *Decyzja: metody proponuje generator z wyników (np. profil sensoryczny → SI, ToM → TUS), czy wybiera terapeuta ręcznie w WOPF?*

**L-11 · Profil sensoryczny — progi ratingu.** Rating kanału (nadwrażliwy / norma / podwrażliwy / poszukujący) ma się wyliczać z pozycji kanału. Pozycje obserwacji sensorycznej muszą mieć przypisany kierunek (nadwrażliwość vs poszukiwanie), inaczej z punktów nie da się wyprowadzić ratingu. **Nie ma też banku „dieta sensoryczna” i „dostosowania”** — §13b generuje z reguł ogólnych (II.4), warto zbudować bank PCTP.

**L-12 · ToM — brak skali i banku wskazań.** Cztery próby są powiązane z `areas.tom.fields`, ale nie ma skali wyników (zaliczona / częściowo / niezaliczona? punkty?) ani banku strategii do §14b.

**L-13 · Współpraca z poradnią — zakres.** Wolny tekst czy struktura (poradnia, osoba, data kontaktu, ustalenia)? Wpływa na to, czy pole można zsynchronizować z Bazą xlsx.

**L-14 · Lista możliwych decyzji zespołu (§16).** Generator ma „zasugerować decyzję”, ale zbiór decyzji nie jest zdefiniowany. Propozycja: ☐ objęcie pomocą pp w placówce (formy: …) · ☐ opracowanie / kontynuacja IPET · ☐ modyfikacja IPET · ☐ wniosek do poradni o opinię / orzeczenie / zmianę orzeczenia · ☐ skierowanie na konsultację (logopeda, psycholog, SI, lekarz) · ☐ monitorowanie bez zmian.

**L-15 · Podpisy, data spotkania zespołu, zapoznanie rodzica.** Nie było w dyktowanej specyfikacji; wymagane prawnie (rodzic otrzymuje kopię WOPF). Dodać jako §18 i przenieść do IPET.

**L-16 · Kontekst obserwacji per etap.** Bank kontekstów dla przedszkola (zabawa swobodna, posiłki, plac zabaw…) różni się od szkoły (lekcje, przerwy, świetlica). Istniejący `obs.contexts` ma bank szkolny — potrzebny drugi bank i przełączanie po `kartoteka.etap`.

**L-17 · Jedna ocena vs wielu obserwatorów.** KPOF może wypełniać wychowawca **i** terapeuta. Model ma jedną ocenę per pozycja. *Decyzja: jedna wspólna ocena (uzgodniona) czy oceny per obserwator + uśrednienie?*

**L-18 · Warstwa zgodności `areas[x].frequency / intensity`.** Generatory Word/xlsx używają skal 0–4 „częstotliwość / intensywność”. KPOF daje średnią 1–4. Potrzebna jawna funkcja przeliczenia (propozycja: `intensity = round(4 − (srednia − 1))`, `frequency` z liczby kontekstów, w których obszar oceniono ≤ 2).

### IV.3 Co jest gotowe do IPET (kolejny etap)

Po domknięciu **L-1, L-8, L-9, L-10, L-14** do IPET przechodzą z WOPF bez ręcznego przepisywania: metryka i podstawa prawna, zespół, poziomy wsparcia, mocne strony i potrzeby, kierunek rozwoju → cele SMART (przez `goals[]`), bariery i uwarunkowania medyczne, zakres i formy wsparcia, wskazania sensoryczne i ToM, decyzja zespołu, zestaw załączników. Pozostałe luki (L-2, L-3, L-5, L-6, L-11, L-12, L-13, L-15–L-18) poprawiają jakość opisów, ale nie blokują IPET.

---

## ZAŁĄCZNIK · PROMPT GENERATORA OPISÓW (do wklejenia w aplikacji)

> Jesteś specjalistą PCTP Koszalin. Piszesz fragment WOPF dla dziecka w wieku przedszkolnym. Dostajesz: (1) dane z kartoteki i metryczki, (2) oceny KPOF obszar po obszarze ze średnimi i poziomami wsparcia, (3) wyniki wykonanych obserwacji pogłębionych (tylko tych z `wykonano: true`), (4) wcześniej wygenerowane sekcje WOPF (dla ciągłości).
> Zasady: język funkcjonalny (co dziecko robi, w jakim kontekście, z jaką pomocą), bez etykiet diagnostycznych i bez ocen osoby; każdy wniosek z obserwacji pogłębionej oznaczaj źródłem w nawiasie („wg profilu sensorycznego z dn. …”); mocne strony zawsze przed trudnościami; trudności formułuj jako potrzeby tam, gdzie sekcja tego wymaga; zachowuj ciągłość — odwołuj się do wcześniejszych sekcji („jak wskazano w charakterystyce funkcjonowania…”); nie wymyślaj danych — jeśli źródła brak, napisz jednym zdaniem, że narzędzia nie prowadzono. Długość: §7 — 2–4 zdania na komórkę; §8, §9, §12 — 1 akapit na pole; §13a/§14a — 1 akapit na kanał/próbę; §13b/§14b — lista punktowana; §16 — opinia 1 strona A4 z proponowaną decyzją na końcu.
