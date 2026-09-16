const S = require("../styl.js");
const W = require("../wspolne.js");
const C = S.CONTENT_W;

module.exports = {
  kod: "NP-04",
  plik: "NP-04_Arkusz_obserwacji_zajec_rewalidacyjnych_i_specjalistycznych.docx",
  tytul: "Arkusz obserwacji zajęć rewalidacyjnych i specjalistycznych",
  build() {
    const d = [];

    d.push(...S.blokTytulowy({
      kicker: "Obserwacja · kształcenie specjalne",
      tytul: "Arkusz obserwacji zajęć rewalidacyjnych i specjalistycznych",
      podtytul: "zajęcia indywidualne i grupowe prowadzone na podstawie orzeczenia oraz pomocy psychologiczno-pedagogicznej",
    }));

    d.push(W.metryczka2([
      ["Prowadzący zajęcia", "Data i godzina"],
      ["Uczeń / grupa (inicjały lub kod)", "Liczba uczestników"],
      ["Wymiar zajęć w tygodniu", "Obserwujący"],
    ]));

    d.push(S.etykieta("Rodzaj zajęć"));
    d.push(...S.kratki([
      "rewalidacyjne", "logopedyczne / neurologopedyczne", "korekcyjno-kompensacyjne",
      "rozwijające kompetencje emocjonalno-społeczne", "trening umiejętności społecznych (TUS)",
      "terapia integracji sensorycznej", "terapia ręki", "zajęcia rozwijające uzdolnienia",
      "wczesne wspomaganie rozwoju (WWR)", "inne: ...................................................",
    ], { after: 55 }));

    d.push(S.poleLinia("Temat / zakres zajęć"));
    d.push(S.poleLinia("Cel zajęć wynikający z IPET lub programu zajęć"));

    /* I */
    d.push(S.sekcja("I", "Zgodność z dokumentacją ucznia"));
    d.push(W.tabelaKryteriow("Kryterium", [
      "Cele zajęć wynikają wprost z IPET / programu zajęć i z zaleceń orzeczenia lub opinii.",
      "Zadania odpowiadają aktualnym ustaleniom wielospecjalistycznej oceny (WOPF).",
      "Prowadzący zna mocne strony ucznia i wykorzystuje je jako punkt wyjścia.",
      "Zajęcia są dokumentowane (dziennik zajęć, karta obserwacji postępów).",
      "Wymiar i regularność zajęć są zgodne z arkuszem organizacji placówki.",
    ]));
    d.push(W.legendaSkali());

    /* II */
    d.push(S.sekcja("II", "Warsztat terapeutyczny"));
    d.push(W.tabelaKryteriow("Kryterium", [
      "Struktura zajęć jest przewidywalna dla ucznia (rytuał otwarcia, praca, zamknięcie).",
      "Ćwiczenia są dobrane do strefy najbliższego rozwoju — nie za łatwe, nie za trudne.",
      "Stopniowanie trudności i liczba powtórzeń umożliwiają utrwalenie umiejętności.",
      "Prowadzący planuje generalizację umiejętności poza gabinet (klasa, dom).",
      "Pomoce i materiały są przygotowane przed zajęciami i adekwatne do celu.",
      "Prowadzący modyfikuje plan zajęć w reakcji na aktualny stan ucznia.",
    ]));
    d.push(W.legendaSkali());

    /* III */
    d.push(S.nowaStrona());
    d.push(S.sekcja("III", "Relacja, komunikacja i regulacja"));
    d.push(W.tabelaKryteriow("Kryterium", [
      "Prowadzący buduje kontakt i uważnie odczytuje sygnały ucznia.",
      "Stosowana jest komunikacja dostosowana do ucznia, w tym AAC, jeśli jest zalecona.",
      "Uczeń otrzymuje czas na odpowiedź i reakcję (bez ponaglania i wyręczania).",
      "Prowadzący rozpoznaje sygnały przeciążenia i stosuje przerwy regulacyjne.",
      "Reakcje na zachowania trudne są spójne z planem interwencji (model ABC).",
      "Wzmocnienia są adekwatne, natychmiastowe i zaplanowane.",
    ]));
    d.push(W.legendaSkali());

    /* IV */
    d.push(S.sekcja("IV", "Postępy ucznia w trakcie zajęć"));
    d.push(W.pustaTabela(
      ["Umiejętność ćwiczona", "Poziom wykonania (samodzielnie / z podpowiedzią / z pomocą)", "Obserwacje"],
      [3000, 3300, C - 6300], 5
    ));

    /* V */
    d.push(S.sekcja("V", "Współpraca"));
    d.push(S.etykieta("Współpraca z zespołem i rodzicami — zaznacz potwierdzone formy"));
    d.push(...S.kratki([
      "przekazywanie wskazówek nauczycielom prowadzącym zajęcia edukacyjne",
      "udział w pracach zespołu opracowującego IPET i WOPF",
      "instruktaż dla rodziców / opiekunów, materiały do pracy w domu",
      "wymiana informacji z poradnią psychologiczno-pedagogiczną lub placówką medyczną",
    ]));

    /* VI */
    d.push(S.nowaStrona());
    d.push(S.sekcja("VI", "Podsumowanie obserwacji"));
    d.push(...S.poleOpisowe("Mocne strony pracy prowadzącego", 4));
    d.push(...S.poleOpisowe("Obszary do rozwoju", 4));
    d.push(S.etykieta("Zalecenia dyrektora"));
    d.push(W.pustaTabelaLp(["Lp.", "Zalecenie", "Termin realizacji", "Sposób sprawdzenia"], [520, 4700, 1900, C - 7120], 4));
    d.push(...S.pudelko(
      "Jeżeli obserwacja wskazuje, że cele IPET wymagają korekty, przekaż wniosek zespołowi opracowującemu program — modyfikacja IPET następuje po ocenie efektywności udzielanej pomocy.",
      { bg: S.BRAND.orangeMist, accent: S.BRAND.orange, color: S.BRAND.ink, size: 15 }
    ));

    d.push(...W.podstawy([W.P.prawoOswiatowe, W.P.nadzor, W.P.ksztalcenieSpecjalne, W.P.pomocPP]));
    d.push(...W.klauzula());
    d.push(...S.blokPodpisow(["Obserwujący", "Prowadzący zajęcia — zapoznałam/em się"]));
    return d;
  },
};
