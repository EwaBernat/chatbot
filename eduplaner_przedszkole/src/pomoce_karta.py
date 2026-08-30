# -*- coding: utf-8 -*-
"""Renderowanie kart pomocy dydaktycznych — wspólne dla wszystkich wersji.

Każda wersja wiekowa (A, B, C) trzyma własny rejestr pomocy i własny katalog
mediów, ale karta wygląda tak samo: zdjęcie poglądowe, lista rzeczy do
przygotowania, trzy kroki użycia, nagrane polecenie i wskazówka. Ten moduł
zna układ karty; moduły `pomoce_a`, `pomoce_b`… znają tylko treść.

Media osadzamy raz — zdjęcia w klasach CSS `.pf-<kod>`, nagrania w jednym
`<audio id="pa-<kod>">` — bo karta może pojawić się w dokumencie wielokrotnie.
"""

import base64
from pathlib import Path

_KORZEN = Path(__file__).resolve().parent.parent

# Zestawy zarejestrowane przez moduły pomocy, w kolejności dodania.
ZESTAWY = []


class Zestaw:
    """Jeden rejestr pomocy: treść + katalogi mediów + etykieta wieku."""

    def __init__(self, pomoce, katalog_foto, katalog_audio, wiek):
        self.pomoce = pomoce
        self.foto = _KORZEN / "assets" / katalog_foto
        self.audio = _KORZEN / "assets" / katalog_audio
        self.wiek = wiek
        ZESTAWY.append(self)

    def _foto(self, kod):
        dane = base64.b64encode((self.foto / f"k_{kod}.jpg").read_bytes()).decode()
        return f"data:image/jpeg;base64,{dane}"

    def _dzwiek(self, kod):
        dane = base64.b64encode((self.audio / f"{kod}.mp3").read_bytes()).decode()
        return f"data:audio/mpeg;base64,{dane}"

    def style(self):
        return "\n".join(f'.pf-{k}{{background-image:url({self._foto(k)})}}'
                         for k in self.pomoce)

    def audio_tagi(self):
        return "".join(f'<audio id="pa-{k}" preload="none" src="{self._dzwiek(k)}"></audio>'
                       for k in self.pomoce)

    def karta(self, kod, esc):
        nr, tytul, przygotuj, kroki, tekst, wskaz = self.pomoce[kod]
        lista = "\n".join(f'      <li>{esc(x)}</li>' for x in przygotuj)
        krok = "\n".join(f'      <li><span class="pk-n">{i}</span>{esc(x)}</li>'
                         for i, x in enumerate(kroki, 1))
        return f'''<section class="zal pomoc" data-poziom="p1">
  <header class="zal-head">
    <span class="mark" role="img" aria-label="Logo PCTP"></span>
    <div>
      <div class="zal-w">EduPlaner 2026</div>
      <div class="zal-s">Pomoc dydaktyczna · konspekt {esc(nr)} · {self.wiek}</div>
    </div>
    <span class="zal-pill p1">druk KC-4</span>
  </header>
  <div class="zal-tytul">
    <span class="zal-kp">Tak ma wyglądać ta pomoc</span>
    <h3>{esc(tytul)}</h3>
  </div>
  <div class="pf pf-{kod}" role="img" aria-label="Zdjęcie poglądowe pomocy: {esc(tytul)}"></div>
  <div class="pomoc-dwie">
    <div><h4 class="pomoc-h">Co przygotować</h4>
    <ul class="klista pomoc-lista">
{lista}
    </ul></div>
    <div><h4 class="pomoc-h">Jak użyć — trzy kroki</h4>
    <ol class="pomoc-kroki">
{krok}
    </ol></div>
  </div>
  <div class="pomoc-glos">
    <button type="button" class="au-btn" data-au="pa-{kod}"
      aria-label="Posłuchaj polecenia"><span aria-hidden="true">▶</span> Posłuchaj polecenia</button>
    <p class="pomoc-tekst">„{esc(tekst)}"</p>
  </div>
  <div class="callout rule pomoc-wsk"><span class="cap">Wskazówka</span>{esc(wskaz)}</div>
  <div class="zal-stopka">
    <span><b>Konspekt {esc(nr)}</b> · pomoc dydaktyczna</span>
    <span class="mono">EduPlaner 2026 · PCTP · druk KC-4</span>
  </div>
</section>'''


def style_pomocy():
    """Zdjęcia wszystkich zestawów, osadzone raz, w klasach CSS."""
    regu = "\n".join(z.style() for z in ZESTAWY if z.pomoce)
    return f"<style>{regu}</style>"


def audio_pomocy():
    return "".join(z.audio_tagi() for z in ZESTAWY)


def pomoce_dla(nr, esc):
    """Karta pomocy dla konspektu o tym numerze albo pusty string."""
    for z in ZESTAWY:
        for kod, dane in z.pomoce.items():
            if dane[0] == nr:
                return z.karta(kod, esc)
    return ""
