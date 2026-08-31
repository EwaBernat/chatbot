# -*- coding: utf-8 -*-
"""Kanoniczna kolejność i podział na kafelki dla obu kącików."""
import json

# ——— paleta: dwie nowe pozycje modułów, poza rodziną sześciu istniejących i poza pomarańczem CTA
PALETA = {
 'kacik-dyrektora':   {'akcent':'#3D2566','pastel':'#EAE6F3','ikona':'🏛'},
 'kacik-nauczyciela': {'akcent':'#1F6F8B','pastel':'#E4EFF4','ikona':'🎓'},
}

DYR = {
 'klucz':'kacik-dyrektora','nazwa':'Kącik dyrektora','etap':'przedszkole',
 'wykaz':{'plik':'INDEKS_Kacik_Dyrektora','tytul':'Wykaz obowiązków dyrektora — czego pilnować',
          'opis':'Osiem bloków obowiązków, matryca sytuacji i pełna lista druków z odesłaniami.'},
 'terminy':{'plik':'Kacik_Dyrektora_Kalendarz_PCTP','sygn':['DK-1'],
            'tytul':'Kalendarz roku dyrektora — miesiąc po miesiącu',
            'opis':'Podział wszystkich czynności według terminów: wrzesień → sierpień, z terminami twardymi.'},
 'kafelki':[
  {'klucz':'planowanie','nazwa':'Planowanie pracy przedszkola','ikona':'🗺',
   'opis':'Plan pracy na rok szkolny i dokument wychowawczo-profilaktyczny.',
   'druki':[('DW-1','Kacik_Dyrektora_Plan_Pracy_PCTP','Plan pracy przedszkola — cztery typy placówki'),
            ('PW-1','Kacik_Dyrektora_Program_Wychowawczy_PCTP','Program wychowawczo-profilaktyczny — dokument fakultatywny')]},
  {'klucz':'nadzor','nazwa':'Nadzór pedagogiczny','ikona':'🔍',
   'opis':'Plan nadzoru, obserwacje, kontrole, dwa sprawozdania i ewaluacja wewnętrzna.',
   'druki':[('DN-1','Kacik_Dyrektora_Nadzor_PCTP','Plan nadzoru pedagogicznego — podstawa prawna każdego elementu'),
            ('DN-2','Kacik_Dyrektora_Nadzor_PCTP','Arkusz obserwacji zajęć'),
            ('DN-3','Kacik_Dyrektora_Nadzor_PCTP','Protokół kontroli'),
            ('DN-4','Kacik_Dyrektora_Nadzor_PCTP','Sprawozdanie semestralne z nadzoru'),
            ('DN-5','Kacik_Dyrektora_Nadzor_PCTP','Sprawozdanie roczne z nadzoru — do 31 sierpnia'),
            ('EW-1','Kacik_Dyrektora_Rekrutacja_Ewaluacja_PCTP','Raport z ewaluacji wewnętrznej')]},
  {'klucz':'rada','nazwa':'Rada pedagogiczna','ikona':'👥',
   'opis':'Protokoły, harmonogram zebrań, uchwały i regulamin rady.',
   'druki':[('RP-1','Kacik_Dyrektora_Rada_Pedagogiczna_PCTP','Protokół zebrania rady z listą obecności'),
            ('RP-2','Kacik_Dyrektora_Rada_Pedagogiczna_PCTP','Harmonogram zebrań rady pedagogicznej'),
            ('RP-3','Kacik_Dyrektora_Rada_Pedagogiczna_PCTP','Uchwała rady — wzór i rejestr'),
            ('RP-4','Kacik_Dyrektora_Rada_Pedagogiczna_PCTP','Regulamin rady pedagogicznej — wzór')]},
  {'klucz':'organizacja','nazwa':'Organizacja pracy','ikona':'⚙',
   'opis':'Godziny zajęć specjalistycznych, kontrola dokumentacji, zalecenia orzeczeń i zarządzenia.',
   'druki':[('DO-1','Kacik_Dyrektora_Organizacja_PCTP','Organizacja zajęć specjalistycznych'),
            ('DO-2','Kacik_Dyrektora_Organizacja_PCTP','Kontrola dokumentacji'),
            ('DO-3','Kacik_Dyrektora_Organizacja_PCTP','Realizacja zaleceń orzeczenia'),
            ('ZD-1','Kacik_Dyrektora_Rekrutacja_Ewaluacja_PCTP','Zarządzenie dyrektora — wzór i rejestr')]},
  {'klucz':'pomoc-pp','nazwa':'Pomoc psychologiczno-pedagogiczna','ikona':'🤝',
   'opis':'Ustalenie pomocy, rejestr, zespół i WOPFU, ocena efektywności oraz sprawozdanie nauczyciela.',
   'druki':[('DP-1','Kacik_Dyrektora_Pomoc_PP_PCTP','Ustalenie pomocy p-p dla dziecka'),
            ('DP-2','Kacik_Dyrektora_Pomoc_PP_PCTP','Rejestr pomocy p-p w przedszkolu'),
            ('DP-3','Kacik_Dyrektora_Pomoc_PP_PCTP','Zespół i harmonogram WOPFU'),
            ('DP-4','Kacik_Dyrektora_Pomoc_PP_PCTP','Zbiorcza ocena efektywności pomocy'),
            ('D-1','Kacik_Dyrektora_Sprawozdanie_Nauczyciela_PPP','Sprawozdanie nauczyciela z pomocy p-p')]},
  {'klucz':'poradnia-rodzice','nazwa':'Poradnia i rodzice','ikona':'✉',
   'opis':'Prośba poradni o opinię, obowiązkowe informacje dla rodziców, skargi i wnioski.',
   'druki':[('DR-1','Kacik_Dyrektora_Poradnia_Rodzice_PCTP','Prośba poradni o opinię — termin 10 dni'),
            ('DR-2','Kacik_Dyrektora_Poradnia_Rodzice_PCTP','Informacje dla rodziców'),
            ('DR-3','Kacik_Dyrektora_Poradnia_Rodzice_PCTP','Skargi, wnioski i sprawy')]},
  {'klucz':'bezpieczenstwo','nazwa':'Bezpieczeństwo','ikona':'🛡',
   'opis':'Kontrola obiektu, wypadek dziecka i przegląd procedur.',
   'druki':[('DB-1','Kacik_Dyrektora_Bezpieczenstwo_PCTP','Protokół kontroli obiektu'),
            ('DB-2','Kacik_Dyrektora_Bezpieczenstwo_PCTP','Wypadek dziecka'),
            ('DB-3','Kacik_Dyrektora_Bezpieczenstwo_PCTP','Procedury bezpieczeństwa')]},
  {'klucz':'rekrutacja','nazwa':'Rekrutacja','ikona':'📋',
   'opis':'Komisja, kryteria, listy i odwołania.',
   'druki':[('RE-1','Kacik_Dyrektora_Rekrutacja_Ewaluacja_PCTP','Rekrutacja do przedszkola')]},
  {'klucz':'zmiany','nazwa':'Zmiany 2026/2027','ikona':'📌',
   'opis':'Statut, nowa podstawa programowa i osiem kierunków polityki oświatowej.',
   'druki':[('DZ-1','Kacik_Dyrektora_Zmiany_2026_PCTP','Zmiany w statucie 2026/2027'),
            ('DZ-2','Kacik_Dyrektora_Zmiany_2026_PCTP','Wdrożenie nowej podstawy programowej'),
            ('DZ-3','Kacik_Dyrektora_Zmiany_2026_PCTP','Kierunki polityki oświatowej 2026/2027')]},
 ]}

NAU = {
 'klucz':'kacik-nauczyciela','nazwa':'Kącik nauczyciela','etap':'przedszkole',
 'wykaz':{'plik':'Kacik_Nauczyciela_Checklista_Wychowawcy_PCTP','sygn':['K-1'],
          'tytul':'Wykaz obowiązków nauczyciela wychowawcy',
          'opis':'Lista czynności w podziale na obszary pracy, z podstawą prawną i terminem przy każdej pozycji.',
          'indeks':'INDEKS_Kacik_Nauczyciela'},
 'terminy':{'plik':'Kacik_Nauczyciela_Checklista_Wychowawcy_PCTP','sygn':['K-1'],
            'tytul':'Terminarz roku nauczyciela',
            'opis':'Część K-1 z podziałem czynności według terminów — wrzesień, semestr, koniec roku.'},
 'kafelki':[
  {'klucz':'obserwacja-diagnoza','nazwa':'Obserwacja i diagnoza','ikona':'👁',
   'opis':'Arkusz obserwacji dziecka oraz analiza gotowości szkolnej.',
   'druki':[('O-1','Kacik_Nauczyciela_Wzory_Opinii_PCTP','Arkusz obserwacji dziecka'),
            ('O-5','Kacik_Nauczyciela_Wzory_Opinii_PCTP','Analiza gotowości szkolnej')]},
  {'klucz':'opinie','nazwa':'Opinie o dziecku','ikona':'📝',
   'opis':'Trzy wzory opinii — dla poradni, dla zespołu orzekającego i dla instytucji zewnętrznej.',
   'druki':[('O-2','Kacik_Nauczyciela_Wzory_Opinii_PCTP','Opinia o funkcjonowaniu dziecka dla poradni — 10 dni od prośby'),
            ('O-3','Kacik_Nauczyciela_Wzory_Opinii_PCTP','Opinia dla zespołu orzekającego'),
            ('O-4','Kacik_Nauczyciela_Wzory_Opinii_PCTP','Opinia dla instytucji zewnętrznej')]},
  {'klucz':'pomoc-pp','nazwa':'Pomoc psychologiczno-pedagogiczna','ikona':'🤝',
   'opis':'Wniosek o objęcie pomocą, plan działań wspierających i protokół zespołu.',
   'druki':[('P-1','Kacik_Nauczyciela_Pomoc_PP_PCTP','Wniosek o objęcie pomocą p-p'),
            ('P-2','Kacik_Nauczyciela_Pomoc_PP_PCTP','Plan działań wspierających — wzór wewnętrzny'),
            ('P-3','Kacik_Nauczyciela_Pomoc_PP_PCTP','Protokół spotkania zespołu')]},
  {'klucz':'dostosowania','nazwa':'Dostosowania','ikona':'🧩',
   'opis':'Zakres dostosowań i racjonalnych usprawnień wobec nowej podstawy programowej.',
   'druki':[('DS-1','Kacik_Nauczyciela_Dostosowania_PCTP','Zakres dostosowań — nowa podstawa 2026')]},
  {'klucz':'rewalidacja','nazwa':'Zajęcia rewalidacyjne i dziennik','ikona':'🧠',
   'opis':'Organizacja zajęć, dziennik z § 11 oraz ocena postępów.',
   'druki':[('Z-1','Kacik_Nauczyciela_Rewalidacja_Dziennik_PCTP','Karta organizacji zajęć rewalidacyjnych'),
            ('Z-2','Kacik_Nauczyciela_Rewalidacja_Dziennik_PCTP','Dziennik zajęć rewalidacyjnych i pomocy p-p'),
            ('Z-3','Kacik_Nauczyciela_Rewalidacja_Dziennik_PCTP','Ocena postępów i wnioski')]},
  {'klucz':'planowanie','nazwa':'Planowanie i realizacja zajęć','ikona':'📐',
   'opis':'Plan pracy grupy, konspekty, karta realizacji i sprawozdanie.',
   'druki':[('R-1','Kacik_Nauczyciela_Planowanie_PCTP','Plan pracy grupy'),
            ('R-2','Kacik_Nauczyciela_Planowanie_PCTP','Karta zajęć — konspekt'),
            ('R-3','Kacik_Nauczyciela_Planowanie_PCTP','Karta realizacji zajęć specjalistycznych'),
            ('R-4','Kacik_Nauczyciela_Planowanie_PCTP','Sprawozdanie z pracy grupy'),
            ('KON','Konspekt_Zajec_Szablon_PCTP','Szablon konspektu zajęć')]},
  {'klucz':'rodzice','nazwa':'Współpraca z rodzicami','ikona':'👪',
   'opis':'Rejestr kontaktów, informacja o postępach oraz zgody i upoważnienia.',
   'druki':[('W-1','Kacik_Nauczyciela_Rodzice_PCTP','Rejestr kontaktów z rodzicami'),
            ('W-2','Kacik_Nauczyciela_Rodzice_PCTP','Informacja o postępach dziecka'),
            ('W-3','Kacik_Nauczyciela_Rodzice_PCTP','Zgody i upoważnienia')]},
  {'klucz':'bezpieczenstwo','nazwa':'Bezpieczeństwo i sytuacje szczególne','ikona':'🛡',
   'opis':'Wyjścia i wycieczki, zdarzenia, adaptacja oraz zachowania trudne.',
   'druki':[('B-1','Kacik_Nauczyciela_Bezpieczenstwo_PCTP','Karta wycieczki i wyjścia poza teren'),
            ('B-2','Kacik_Nauczyciela_Bezpieczenstwo_PCTP','Karta zdarzenia — notatka służbowa'),
            ('B-3','Kacik_Nauczyciela_Bezpieczenstwo_PCTP','Karta adaptacji dziecka'),
            ('B-4','Kacik_Nauczyciela_Bezpieczenstwo_PCTP','Karta zachowań trudnych')]},
  {'klucz':'instrukcje','nazwa':'Materiały instruktażowe','ikona':'💡',
   'opis':'Jak formułować cele, żeby dało się zmierzyć postęp.',
   'druki':[('I-1','Instrukcja_Cele_SMART_PCTP','Instrukcja pisania celów SMART')]},
 ]}

def zbuduj():
    r={'schemat':1,'wygenerowano':'2026-08-31',
       'opis':'Kanoniczna kolejność i podział na kafelki dla kącika dyrektora i kącika nauczyciela. '
              'Kolejność: wykaz obowiązków → podział wg terminów → podział wg rodzajów czynności (kafelki) → druki.',
       'paleta':PALETA,'kaciki':[]}
    for k in (DYR,NAU):
        n=0; kaf=[]
        for i,f in enumerate(k['kafelki'],1):
            d=[]
            for s,plik,nazwa in f['druki']:
                n+=1
                d.append({'nr':n,'sygnatura':s,'plik':plik,'nazwa':nazwa})
            kaf.append({'nr':i,'klucz':f['klucz'],'nazwa':f['nazwa'],'ikona':f['ikona'],
                        'opis':f['opis'],'druki':d,'trasa':f"/{k['klucz']}/{f['klucz']}"})
        r['kaciki'].append({'klucz':k['klucz'],'nazwa':k['nazwa'],'etap':k['etap'],
            'trasa':f"/{k['klucz']}",'paleta':PALETA[k['klucz']],
            'kolejnosc':[
              {'krok':1,'nazwa':'Wykaz obowiązków — lista czynności','typ':'wykaz','pozycja':k['wykaz']},
              {'krok':2,'nazwa':'Podział według terminów','typ':'terminy','pozycja':k['terminy']},
              {'krok':3,'nazwa':'Podział według rodzajów czynności','typ':'kafelki','pozycja':{'kafelkow':len(kaf)}},
              {'krok':4,'nazwa':'Załączniki — druki','typ':'druki','pozycja':{'drukow':n}}],
            'kafelki':kaf,'drukow':n})
    return r

if __name__=='__main__':
    r=zbuduj()
    json.dump(r,open('/tmp/bud/rejestr-kacikow.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
    for k in r['kaciki']:
        print(f"{k['nazwa']:20s} kafelków {len(k['kafelki']):2d} · druków {k['drukow']:2d} · akcent {k['paleta']['akcent']}")
