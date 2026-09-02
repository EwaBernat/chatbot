# -*- coding: utf-8 -*-
"""Logo PCTP — to samo, którym firmowane są druki banku celów SMART.

Druki FBA miały do tej pory w nagłówku sam napis „PCTP" w kwadraciku. To był
znacznik zastępczy, nie logo: materiał firmowany jej nazwiskiem ma nosić ten
sam znak, co reszta ekosystemu EduPlaner.

Plik: `assets/logo_pctp.jpg` (kopia z `eduplaner_przedszkole/assets/`), wchodzi
do dokumentu jako `data:` URI w zmiennej `--logo`, więc dokument zostaje
samodzielnym plikiem i działa bez internetu.
"""

import base64
from pathlib import Path

PLIK = Path(__file__).resolve().parent.parent / "assets" / "logo_pctp.jpg"


def uri():
    return "data:image/jpeg;base64," + base64.b64encode(PLIK.read_bytes()).decode()


def zmienna():
    """Deklaracja `--logo` do wstawienia na początku arkusza stylów."""
    return f":root{{--logo:url({uri()})}}"


# Znak w nagłówku: okrągłe logo zamiast napisu w kwadraciku.
STYL = """
.mark{flex:0 0 auto; width:38px; height:38px; border-radius:50%;
  background:center/cover no-repeat var(--soft); background-image:var(--logo);
  box-shadow:0 0 0 1px var(--line-2)}
"""
