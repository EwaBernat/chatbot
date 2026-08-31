# Avatar: Ewa

> **⚠️ Zanim uruchomisz skill `heygen-avatar` — uzupełnij sekcję `## HeyGen` poniżej.**
> Dopóki `Group ID` jest puste, skill uzna, że awatara jeszcze nie ma, i zaproponuje
> utworzenie nowego zamiast użycia Twojego. Jeśli awatara robisz sama w aplikacji
> HeyGen (tak ustaliliśmy), najpierw wklej tu identyfikatory, potem wołaj skille.

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
- Group ID: <wklej — „Avatar Group ID" z aplikacji HeyGen>
- Voice ID: <wklej — opcjonalnie, głos zapasowy z katalogu HeyGen>
- Voice Name: <nazwa tego głosu>
- Voice Designed: false
- Voice Seed:
- Looks: landscape=<look_id>, portrait=<look_id>
- Last Synced: <data, gdy ostatnio to sprawdzałaś>

⚠️ `look_id` są ulotne — nie przywiązuj się do nich. Stabilny jest `group_id`;
aktualne looki rozwiązuj świeżo:

```bash
heygen avatar looks list --group-id <group_id>
```

## ElevenLabs (poza konwencją skilla HeyGen — nasza droga)
- Voice ID: jq4ZUryuBeDqmtkKtBZ4
- Voice Name: Ewa-głos_do skils
- Model: eleven_v3 (znaczniki reżyserii w `reklama/narracja-v3.txt`)
- Ustawienia: `--stability 0.35 --style 0.45 --speed 0.95`
- **Rytm: jedno zdanie = jeden akapit; wyliczenia po kropce, nie po przecinku.**
  Pełny przepis, zatwierdzony odsłuchem:
  `.claude/skills/dane-i-glos/references/rytm_i_pauzy.md`

Kandydaci alternatywni: `MxdHRlURUZPVY5h2NiXH` (Ewa2, podobne tempo),
`D0Yz6dyyxHOodq3Zqi45` (Ewa1, dużo wolniejszy — raczej na materiały szkoleniowe).
`1tw3WuUEU1Wt8m68hw81` („Głos bez tytułu") **nie działa** — patrz
`reklama/scenariusz-60s.md`.

## Skąd wziąć identyfikatory

Wszystkie linki i ścieżki w aplikacji — patrz [`HEYGEN-START.md`](HEYGEN-START.md),
sekcja „Gdzie co wkleić".
