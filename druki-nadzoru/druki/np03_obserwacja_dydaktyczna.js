const S = require("../styl.js");
const W = require("../wspolne.js");
const C = S.CONTENT_W;

module.exports = {
  kod: "NP-03",
  plik: "NP-03_Arkusz_obserwacji_zajec_dydaktycznych.docx",
  tytul: "Arkusz obserwacji zajęć dydaktycznych",
  build() {
    const d = [];

    d.push(...S.blokTytulowy({
      kicker: "Obserwacja · forma nadzoru",
      tytul: "Arkusz obserwacji zajęć dydaktycznych",
      podtytul: "zajęcia edukacyjne w oddziale szkoły specjalnej  ·  wypełnia dyrektor lub osoba upoważniona",
    }));

    d.push(W.metryczka2([
      ["Nauczyciel prowadzący", "Data i godzina"],
      ["Zajęcia edukacyjne / przedmiot", "Oddział / grupa"],
      ["Liczba uczniów obecnych / wpisanych", "Obserwujący"],
      ["Nauczyciel współorganizujący / pomoc nauczyciela", "Czas trwania obserwacji"],
    ]));

    d.push(S.etykieta("Rodzaj obserwacji"));
    d.push(S.kratkiWiersz(["planowa (ujęta w planie nadzoru)", "doraźna", "kontrolna (po zaleceniach)"]));

    d.push(S.poleLinia("Temat zajęć"));
    d.push(S.poleLinia("Cel obserwacji ustalony przez dyrektora"));

    /* I */
    d.push(S.sekcja("I", "Organizacja i przebieg zajęć"));
    d.push(W.tabelaKryteriow("Kryterium", [
      "Cele zajęć są sformułowane operacyjnie i przekazane uczniom w zrozumiałej formie.",
      "Struktura zajęć jest czytelna: wprowadzenie, część główna, podsumowanie.",
      "Czas zajęć jest wykorzystany efektywnie, tempo dostosowane do możliwości uczniów.",
      "Zadania wynikają z podstawy programowej i realizowanego programu / IPET.",
      "Zajęcia kończy podsumowanie i sprawdzenie stopnia osiągnięcia celu.",
    ]));
    d.push(W.legendaSkali());

    /* II */
    d.push(S.sekcja("II", "Dostosowanie do specjalnych potrzeb edukacyjnych"));
    d.push(W.tabelaKryteriow("Kryterium", [
      "Działania nauczyciela są zgodne z IPET i zaleceniami orzeczenia o potrzebie kształcenia specjalnego.",
      "Nauczyciel wykorzystuje ustalenia wielospecjalistycznej oceny poziomu funkcjonowania (WOPF).",
      "Treści, tempo i forma zadań są zindywidualizowane (zadania o zróżnicowanym stopniu trudności).",
      "Stosowane są dostosowania warunków: miejsce, czas, pomoce, przerwy regulacyjne.",
      "Praca nauczyciela współorganizującego / pomocy nauczyciela jest zaplanowana i celowa.",
      "Uczeń o największych potrzebach ma zapewnione wsparcie bez wyręczania go w zadaniu.",
    ]));
    d.push(W.legendaSkali());

    /* III */
    d.push(S.nowaStrona());
    d.push(S.sekcja("III", "Metody, środki i komunikacja"));
    d.push(W.tabelaKryteriow("Kryterium", [
      "Metody są aktywizujące i adekwatne do możliwości psychofizycznych uczniów.",
      "Nauczyciel stosuje komunikację wspomagającą i alternatywną (AAC), gdy uczeń jej potrzebuje.",
      "Wykorzystane są pomoce dydaktyczne, materiały sensoryczne i technologie wspomagające.",
      "Polecenia są krótkie, jednoznaczne, wsparte wzorem lub demonstracją.",
      "Nauczyciel stosuje wzmocnienia pozytywne i buduje poczucie bezpieczeństwa.",
      "Reakcje na zachowania trudne są spójne z ustaleniami zespołu (model ABC / plan interwencji).",
    ]));
    d.push(W.legendaSkali());

    /* IV */
    d.push(S.sekcja("IV", "Ocenianie, informacja zwrotna i bezpieczeństwo"));
    d.push(W.tabelaKryteriow("Kryterium", [
      "Uczniowie otrzymują informację zwrotną o tym, co zrobili dobrze i nad czym pracować dalej.",
      "Ocenianie uwzględnia wysiłek, postęp i możliwości ucznia, zgodnie ze statutem placówki.",
      "Nauczyciel monitoruje postępy i odnotowuje je w dokumentacji zajęć.",
      "Zapewnione są warunki bezpieczeństwa i higieny pracy, w tym bezpieczeństwo sensoryczne.",
    ]));
    d.push(W.legendaSkali());

    /* V */
    d.push(S.sekcja("V", "Obserwacja funkcjonowania uczniów"));
    d.push(...S.poleOpisowe("Zaangażowanie i aktywność uczniów, reakcje na zadania", 3));
    d.push(...S.poleOpisowe("Zaobserwowane trudności uczniów i sposób reagowania nauczyciela", 3));

    /* VI */
    d.push(S.nowaStrona());
    d.push(S.sekcja("VI", "Podsumowanie obserwacji"));
    d.push(...S.poleOpisowe("Mocne strony zajęć", 4));
    d.push(...S.poleOpisowe("Obszary do rozwoju", 4));
    d.push(S.etykieta("Zalecenia dyrektora"));
    d.push(W.pustaTabelaLp(["Lp.", "Zalecenie", "Termin realizacji", "Sposób sprawdzenia"], [520, 4700, 1900, C - 7120], 4));
    d.push(S.etykieta("Potrzeby wspomagania wynikające z obserwacji"));
    d.push(...S.kratki([
      "szkolenie / warsztat — temat: .................................................................",
      "obserwacja koleżeńska lub lekcja otwarta",
      "wsparcie specjalisty (psycholog, logopeda, terapeuta SI)",
      "konsultacja indywidualna z dyrektorem",
      "materiały i pomoce dydaktyczne — jakie: ...............................................",
    ]));
    d.push(S.poleLinia("Termin obserwacji sprawdzającej (jeżeli dotyczy)"));

    d.push(...W.podstawy([W.P.prawoOswiatowe, W.P.nadzor, W.P.ksztalcenieSpecjalne, W.P.kartaNauczyciela]));
    d.push(...W.klauzula());
    d.push(...S.blokPodpisow(["Obserwujący", "Nauczyciel — zapoznałam/em się"]));
    return d;
  },
};
