# Avatar: Ewa

> **Awatar istnieje.** `Group ID` jest wypełnione — skille używają go automatycznie,
> nie tworzą nowego. Identyfikator pochodzi z aplikacji HeyGen i **nie został
> zweryfikowany wywołaniem API** (sesja, w której go zapisano, nie miała połączenia
> z HeyGenem). Pierwsze użycie lokalnie to potwierdzi.

## Appearance
- Age: <do uzupełnienia — albo nieistotne, jeśli awatar powstaje ze zdjęcia lub nagrania>
- Gender: Woman
- Ethnicity: <do uzupełnienia>
- Hair: <do uzupełnienia>
- Build: <do uzupełnienia>
- Features: <do uzupełnienia>
- Style: Realistic
- Reference: <ścieżka do zdjęcia lub nagrania, trzymanego poza repozytorium>

Te pola opisują wygląd słowami i mają znaczenie tylko przy awatarze
generowanym z opisu (`prompt`). Przy awatarze ze zdjęcia (`photo`) albo
z nagrania (`digital_twin`) wygląd bierze się z materiału — wtedy wystarczy
wypełnić `Reference` i zostawić resztę.

## Voice
- Tone: ciepły, spokojny, szkoleniowy
- Accent: polski, standardowy
- Energy: opanowana, przekonująca — bez sprzedażowego nacisku
- Think: doświadczona pedagożka prowadząca szkolenie dla dyrektorów

**Uwaga:** na Twojej drodze narrację robi klon z ElevenLabs, a HeyGen tylko animuje
usta do gotowego MP3. Głos z katalogu HeyGen poniżej jest zapasowy — użyje go
wyłącznie skill `heygen-video`, gdybyś kiedyś generowała film wprost z tekstu.

## HeyGen
- Group ID: 41d5e035154744828ca9b697f7c3690a   ← „ewa-szkolenia" (postać)
- Voice ID: <wklej — opcjonalnie, głos zapasowy z katalogu HeyGen>
- Voice Name: <nazwa tego głosu>
- Voice Designed: false
- Voice Seed:
- Look ID: 4fceb4c254a349eab302734b740edbdd   ← „Ewa - szkolenia-niebieska" (strój)
- Looks: `szkolenia-niebieska` — strój niebieski, obsługuje na razie wszystkie postacie
  (patrz `postacie.md`, sekcja „Co już istnieje na koncie")

**Które jest które — do potwierdzenia.** Oba identyfikatory mają ten sam kształt
(32 znaki szesnastkowe), więc z samego wyglądu nie da się ich odróżnić. Przypisałem je
po nazwach: „ewa-szkolenia" to nazwa **postaci** (grupa), „Ewa - szkolenia-niebieska"
nazywa **strój** (look). To wnioskowanie, nie sprawdzony fakt — pierwsze wywołanie
rozstrzygnie. Gdyby było odwrotnie, zamień je miejscami w tym pliku.
- Last Synced: 2026-09-01 (zapisane z aplikacji, niezweryfikowane API)

### Pierwsze sprawdzenie (lokalnie, po zalogowaniu do HeyGena)

```bash
heygen avatar looks list --group-id 41d5e035154744828ca9b697f7c3690a
```

- **Wypisze listę looków**, a wśród nich `4fceb4c2…` → przypisanie poprawne, gotowe.
- **404 albo „group not found"** → identyfikatory są zamienione. Spróbuj drugiego:
  `heygen avatar looks list --group-id 4fceb4c254a349eab302734b740edbdd`
  i popraw kolejność w tym pliku.
- **Oba dają 404** → sprawdź, co naprawdę jest na koncie:
  `heygen avatar list --ownership private`

⚠️ `look_id` są ulotne — nie przywiązuj się do nich. Stabilny jest `group_id`.

## ElevenLabs (poza konwencją skilla HeyGen — nasza droga)
- Voice ID: jq4ZUryuBeDqmtkKtBZ4
- Voice Name: Ewa-głos_do skils
- Model: eleven_v3 (znaczniki reżyserii w `reklama/narracja-v3.txt`)
- Ustawienia: `--stability 0.35 --style 0.45 --speed 0.95`
- **Rytm: jedno zdanie = jeden akapit; wyliczenia po kropce, nie po przecinku.**
  Pełny przepis, zatwierdzony odsłuchem:
  `.claude/skills/dane-i-glos/references/rytm_i_pauzy.md`

## Agent głosowy (rozmowa po polsku)

- **Nazwa:** Asystent Ewy — rozmowa po polsku
- **Agent ID:** `agent_9201m1ezxy5hfxyvn8zkkz2gxa87`
- **Głos:** ten sam klon, `jq4ZUryuBeDqmtkKtBZ4`
- **Model TTS:** `eleven_turbo_v2_5` — **wymagany**; agenci nieanglojęzyczni nie
  działają na `eleven_multilingual_v2` ani `eleven_v3`, API odrzuca konfigurację
- **Język:** `pl`
- **Rozmowa:** [elevenlabs.io/app/talk-to?agent_id=agent_9201m1ezxy5hfxyvn8zkkz2gxa87](https://elevenlabs.io/app/talk-to?agent_id=agent_9201m1ezxy5hfxyvn8zkkz2gxa87)

Agent jest prywatny — link działa po zalogowaniu na konto ElevenLabs. Udostępnienie
publiczne (żeby rozmawiali z nim inni, np. rodzice albo dyrektorzy) włącza się
w ustawieniach agenta; wtedy `agents_get_link` zwróci token do wklejenia na stronę.

Kandydaci alternatywni: `MxdHRlURUZPVY5h2NiXH` (Ewa2, podobne tempo),
`D0Yz6dyyxHOodq3Zqi45` (Ewa1, dużo wolniejszy — raczej na materiały szkoleniowe).
`1tw3WuUEU1Wt8m68hw81` („Głos bez tytułu") **nie działa** — patrz
`reklama/scenariusz-60s.md`.

## Skąd wziąć identyfikatory

Wszystkie linki i ścieżki w aplikacji — patrz [`HEYGEN-START.md`](HEYGEN-START.md),
sekcja „Gdzie co wkleić".
