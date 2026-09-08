import React from 'react';
import {AbsoluteFill, Audio, Sequence, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {MARKA, FONT} from '../marka';
import {Napisy} from '../Napisy';
import {Logo, Pojaw, useWejscie} from '../ui';
import {OryginalnyDruk, type Krok, type Ujecie} from '../kpof/OryginalnyDruk';
import type {Napis} from '../typy';
import ocenyJson from '../../public/obserwacja-oceny.json';

/** Film „Szkoła podstawowa · Obserwacja pogłębiona” — narracja: dosłowna transkrypcja części 6 skryptu (31 akapitów) + „do czego służą” + Strażnik prawa. */
export type FilmObs = {audio: string | null; napisy: Napis[]; dlugosc: number};
export type Props = {film: FilmObs};
type Ocena = [number, string, number, number];
const OCENY = ocenyJson as unknown as Record<string, Ocena[]>;

/* ---------- plansze ---------- */
const Tlo: React.FC<{children: React.ReactNode}> = ({children}) => (
  <AbsoluteFill style={{background: `linear-gradient(160deg, ${MARKA.fioletCiemny} 0%, ${MARKA.fiolet} 55%, #3b2a86 100%)`, fontFamily: FONT}}>
    <div style={{position: 'absolute', left: 460, top: -100, width: 1000, height: 900, borderRadius: '50%', background: 'radial-gradient(circle, rgba(232,69,10,0.35) 0%, rgba(232,69,10,0) 60%)'}} />
    {children}
  </AbsoluteFill>
);
const Karta: React.FC<{od: number; children: React.ReactNode; style?: React.CSSProperties; akcent?: boolean}> = ({od, children, style, akcent}) => {
  const w = useWejscie(od, {damping: 13, stiffness: 110});
  return (
    <div style={{opacity: w, transform: `translateY(${(1 - w) * 30}px) scale(${0.94 + 0.06 * w})`, background: akcent ? MARKA.pomarancz : 'rgba(255,255,255,0.08)', border: `1.5px solid ${akcent ? MARKA.pomarancz : 'rgba(255,255,255,0.28)'}`, borderRadius: 18, padding: '20px 24px', color: '#fff', ...style}}>
      {children}
    </div>
  );
};
const Naglowek: React.FC<{kicker: string; tytul: string; od?: number}> = ({kicker, tytul, od = 0}) => (
  <Pojaw od={od} style={{position: 'absolute', left: 0, right: 0, top: 64, textAlign: 'center'}}>
    <div style={{fontSize: 19, letterSpacing: 4, color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase'}}>{kicker}</div>
    <div style={{fontSize: 54, fontWeight: 800, color: '#fff', marginTop: 10, letterSpacing: -1, lineHeight: 1.1}}>{tytul}</div>
  </Pojaw>
);
const Kolo: React.FC<{n: string | number; kolor?: string; rozmiar?: number}> = ({n, kolor = MARKA.morski, rozmiar = 54}) => (
  <div style={{width: rozmiar, height: rozmiar, borderRadius: '50%', background: kolor, display: 'grid', placeItems: 'center', fontSize: rozmiar * 0.45, fontWeight: 800, flex: '0 0 auto', color: '#fff'}}>{n}</div>
);

const Intro: React.FC<{gdzie: number; dlaczego: number; cel: number}> = ({gdzie, dlaczego, cel}) => (
  <Tlo>
    <Pojaw od={0} style={{position: 'absolute', left: 0, right: 0, top: 120, textAlign: 'center'}}>
      <div style={{fontSize: 20, letterSpacing: 4, color: 'rgba(255,255,255,0.7)', textTransform: 'uppercase'}}>EduPlaner 2026 · Szkoła podstawowa · moduł szósty</div>
      <div style={{fontSize: 86, fontWeight: 800, color: '#fff', marginTop: 12, letterSpacing: -2, lineHeight: 1.05}}>Obserwacja <span style={{color: '#F6A57E'}}>pogłębiona</span></div>
      <div style={{fontSize: 34, fontWeight: 700, color: '#fff', marginTop: 10}}>ABC i FBA · profil sensoryczny · teoria umysłu · karta mowy · profil biopsychospołeczny</div>
    </Pojaw>
    <div style={{position: 'absolute', left: 160, right: 160, top: 470, display: 'flex', gap: 24}}>
      <Karta od={gdzie} style={{flex: 1, textAlign: 'center', fontSize: 30, lineHeight: 1.35}}><div style={{fontSize: 18, letterSpacing: 3, color: '#F6A57E', fontWeight: 800}}>KWESTIONARIUSZ</div><b>gdzie</b> uczeń potrzebuje wsparcia</Karta>
      <Karta od={dlaczego} akcent style={{flex: 1, textAlign: 'center', fontSize: 30, lineHeight: 1.35}}><div style={{fontSize: 18, letterSpacing: 3, fontWeight: 800, color: 'rgba(255,255,255,0.85)'}}>OBSERWACJA POGŁĘBIONA</div><b>dlaczego</b></Karta>
    </div>
    <div style={{position: 'absolute', left: 160, right: 160, top: 720}}>
      <Karta od={cel} style={{textAlign: 'center', fontSize: 25, lineHeight: 1.45}}>Po tym module: <b>kiedy</b> uruchamiamy obserwację pogłębioną · <b>które</b> z czterech narzędzi wybrać · <b>gdzie</b> przebiega granica kompetencji nauczyciela</Karta>
    </div>
  </Tlo>
);

const Przesiew: React.FC<{p: number; o: number; kier: number; koszt: number}> = ({p, o, kier, koszt}) => (
  <Tlo>
    <Naglowek kicker="Przesiew a obserwacja pogłębiona" tytul="Wszyscy uczniowie → jeden uczeń" />
    <div style={{position: 'absolute', left: 140, right: 140, top: 230, display: 'flex', gap: 26}}>
      <Karta od={p} style={{flex: 1, textAlign: 'center', padding: '30px 24px'}}>
        <div style={{fontSize: 20, letterSpacing: 3, color: '#F6A57E', fontWeight: 800}}>PRZESIEW · KSzOF</div>
        <div style={{fontSize: 40, fontWeight: 800, marginTop: 10}}>wszyscy uczniowie</div>
        <div style={{fontSize: 22, marginTop: 8, color: 'rgba(255,255,255,0.85)'}}>wrzesień · cały oddział · 52 twierdzenia</div>
      </Karta>
      <Karta od={o} akcent style={{flex: 1, textAlign: 'center', padding: '30px 24px'}}>
        <div style={{fontSize: 20, letterSpacing: 3, fontWeight: 800, color: 'rgba(255,255,255,0.85)'}}>OBSERWACJA POGŁĘBIONA</div>
        <div style={{fontSize: 40, fontWeight: 800, marginTop: 10}}>pojedynczy uczeń</div>
        <div style={{fontSize: 22, marginTop: 8}}>gdy wynik kwestionariusza wskaże kierunek</div>
      </Karta>
    </div>
    <div style={{position: 'absolute', left: 140, right: 140, top: 560}}>
      <Karta od={kier} style={{textAlign: 'center', fontSize: 27, fontWeight: 700}}>Uruchamiamy ją wtedy, gdy wynik kwestionariusza wskaże kierunek.</Karta>
      <Karta od={koszt} style={{marginTop: 22, textAlign: 'center', fontSize: 25, lineHeight: 1.4, borderColor: '#F6A57E'}}>To <b>kilkanaście godzin pracy zespołu</b> — dlatego uruchamiamy ją z przesłanką, a nie „na wszelki wypadek”.</Karta>
    </div>
  </Tlo>
);

const REGULY: [string, string, string][] = [
  ['1', 'Wynik któregokolwiek obszaru ≤ 8 pkt w skali 0–20 (Poziom III)', 'narzędzie zależne od obszaru'],
  ['2', 'Dwa lub więcej twierdzeń ocenionych na 1 lub 2 w tym samym obszarze', 'narzędzie właściwe dla obszaru'],
  ['3', 'Rozbieżność między oceniającymi ≥ 2 steny w wyniku ogólnym', 'rozmowa z rodzicem + obserwacja w środowisku o wyższym wyniku'],
  ['4', 'Sygnał zdrowotny z metryczki (nadwrażliwość sensoryczna, choroba przewlekła)', 'profil sensoryczny'],
  ['5', 'Zachowanie powtarzalne zagrażające uczniowi lub innym — NATYCHMIAST', 'ABC + arkusz analizy funkcjonalnej'],
  ['6', 'Brak poprawy mimo udzielanej pomocy przez ok. 3 miesiące', 'karta oceny efektywności + narzędzie dla obszaru'],
  ['7', 'Nagła zmiana: oceny niżej w ≥ 3 przedmiotach albo nieobecności > 20% w miesiącu', 'wywiad z uczniem i rodzicem · konsultacja psychologa'],
];
const Reguly: React.FC<{od: number[]; rada: number; przepis: number; kto: number}> = ({od, rada, przepis, kto}) => (
  <Tlo>
    <Naglowek kicker="Wystarczy jedna, aby zespół usiadł nad kartą decyzyjną" tytul="Siedem reguł przekierowania" />
    <div style={{position: 'absolute', left: 90, right: 90, top: 205, display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 14}}>
      {REGULY.map(([n, t, nar], i) => (
        <Karta key={n} od={od[i]} style={{display: 'flex', gap: 16, alignItems: 'center', padding: '12px 18px', gridColumn: i === 6 ? '1 / span 2' : undefined}}>
          <Kolo n={n} kolor={i === 4 ? MARKA.pomarancz : MARKA.morski} rozmiar={50} />
          <div style={{flex: 1}}>
            <div style={{fontSize: 21.5, lineHeight: 1.3}}>{t}</div>
            <div style={{fontSize: 16, color: '#F6A57E', fontWeight: 700, marginTop: 3}}>→ {nar}</div>
          </div>
        </Karta>
      ))}
    </div>
    <div style={{position: 'absolute', left: 90, right: 90, bottom: 120, display: 'flex', gap: 18}}>
      <Karta od={rada} akcent style={{flex: 1.2, fontSize: 21, lineHeight: 1.35, padding: '14px 20px'}}>Reguły są decyzją <b>rady pedagogicznej</b> wpisaną do procedury szkoły.</Karta>
      <Karta od={przepis} style={{flex: 1, fontSize: 20, lineHeight: 1.35, padding: '14px 20px'}}>Przepis wymaga rozpoznawania potrzeb i oceny efektywności (t.j. Dz.U. 2023 poz. 1798).</Karta>
      <Karta od={kto} style={{flex: 1.2, fontSize: 20, lineHeight: 1.35, padding: '14px 20px'}}>Decyzja nie zależy od tego, kto danego dnia patrzy na arkusz.</Karta>
    </div>
  </Tlo>
);

const NARZEDZIA: [string, string, string, string][] = [
  ['1', 'Model ABC + arkusz analizy funkcjonalnej (FBA)', 'Dlaczego to zachowanie się powtarza?', 'wychowawca + psycholog / pedagog specjalny'],
  ['2', 'Profil sensoryczny (model Dunn)', 'Jak uczeń reaguje na bodźce i czego potrzebuje jego układ nerwowy?', 'wychowawca + terapeuta SI'],
  ['3', 'Obserwacja poznania społecznego i teorii umysłu', 'Czy uczeń rozumie intencje i przekonania innych?', 'psycholog + wychowawca'],
  ['4', 'Karta obserwacji rozwoju mowy i komunikacji', 'Czy uczeń nas rozumie i czy potrafi się porozumieć?', 'wychowawca + logopeda'],
];
const Narzedzia: React.FC<{od: number; abc: number}> = ({od, abc}) => {
  const frame = useCurrentFrame();
  return (
    <Tlo>
      <Naglowek kicker="Każde odpowiada na inne pytanie" tytul="Cztery narzędzia obserwacji pogłębionej" />
      <div style={{position: 'absolute', left: 90, right: 90, top: 225, display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 18}}>
        {NARZEDZIA.map(([n, t, q, kto], i) => {
          const wyr = i === 0 ? Math.max(0, Math.min(1, (frame - abc) / 10)) : 0;
          return (
            <Karta key={n} od={od + i * 5} style={{minHeight: 470, display: 'flex', flexDirection: 'column', gap: 14, padding: '24px 20px', background: `rgba(232,69,10,${0.85 * wyr})`, borderColor: wyr ? MARKA.pomarancz : 'rgba(255,255,255,0.28)'}}>
              <Kolo n={n} kolor={wyr ? '#fff' : MARKA.pomarancz} rozmiar={62} />
              <div style={{fontSize: 27, fontWeight: 800, lineHeight: 1.15, color: wyr ? MARKA.fioletCiemny : '#fff'}}>{t}</div>
              <div style={{fontSize: 22, lineHeight: 1.35, flex: 1, color: wyr ? '#fff' : 'rgba(255,255,255,0.9)'}}>„{q}”</div>
              <div style={{fontSize: 16, color: wyr ? '#fff' : '#F6A57E', fontWeight: 700, letterSpacing: 1}}>{kto}</div>
            </Karta>
          );
        })}
      </div>
    </Tlo>
  );
};

const Wadliwy: React.FC<{zapis: number; trzy: number}> = ({zapis, trzy}) => (
  <Tlo>
    <Naglowek kicker="Zapis wadliwy — najczęstszy w dokumentacji" tytul="Interpretacja zamiast faktu" />
    <div style={{position: 'absolute', left: 160, right: 160, top: 250}}>
      <Karta od={zapis} style={{fontSize: 34, lineHeight: 1.45, fontStyle: 'italic', borderLeft: `10px solid #c0392b`, padding: '30px 34px'}}>
        „Uczeń <span style={{background: 'rgba(192,57,43,0.55)', borderRadius: 8, padding: '0 8px'}}>zniechęcił się</span>, bo <span style={{background: 'rgba(192,57,43,0.55)', borderRadius: 8, padding: '0 8px'}}>nie chciało mu się pracować</span>, i <span style={{background: 'rgba(192,57,43,0.55)', borderRadius: 8, padding: '0 8px'}}>zamanifestował swoją niechęć</span> do przedmiotu.”
      </Karta>
      <div style={{display: 'flex', gap: 24, marginTop: 30}}>
        <Karta od={trzy} akcent style={{flex: 1, textAlign: 'center', padding: '26px 20px'}}><div style={{fontSize: 64, fontWeight: 800, lineHeight: 1}}>3</div><div style={{fontSize: 24, fontWeight: 700, marginTop: 6}}>interpretacje w jednym zdaniu</div></Karta>
        <Karta od={trzy + 6} style={{flex: 1, textAlign: 'center', padding: '26px 20px', borderColor: '#c0392b'}}><div style={{fontSize: 64, fontWeight: 800, lineHeight: 1, color: '#ff8a7a'}}>0</div><div style={{fontSize: 24, fontWeight: 700, marginTop: 6}}>faktów, które dałoby się policzyć</div></Karta>
      </div>
      <Karta od={trzy + 14} style={{marginTop: 26, textAlign: 'center', fontSize: 24, lineHeight: 1.4}}>Zapis poprawny: <b>co było przed</b> (A) · <b>co uczeń zrobił</b> — obserwowalnie, w minutach (B) · <b>co nastąpiło potem</b> (C). Każde zdanie da się sprawdzić.</Karta>
    </div>
  </Tlo>
);

const Miejsca: React.FC<{od: number; natez: number}> = ({od, natez}) => (
  <Tlo>
    <Naglowek kicker="Trzy miejsca, które w przedszkolu nie istnieją albo wyglądają inaczej" tytul="Korytarz · stołówka · sala gimnastyczna" />
    <div style={{position: 'absolute', left: 120, right: 120, top: 240, display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 22}}>
      {[['Korytarz na przerwie', 'tłok, przepychanie, dotyk z zaskoczenia, hałas kilkuset głosów'], ['Stołówka', 'zapachy, dźwięk naczyń, kolejka, ograniczony czas, bliskość innych'], ['Sala gimnastyczna', 'echo, gwizdek, pogłos, szybki ruch wielu osób, zmiana ubrania']].map(([t, o], i) => (
        <Karta key={t} od={od + i * 6} style={{minHeight: 300, padding: '26px 22px', textAlign: 'center'}}>
          <div style={{fontSize: 30, fontWeight: 800, lineHeight: 1.15}}>{t}</div>
          <div style={{fontSize: 22, lineHeight: 1.4, marginTop: 14, color: 'rgba(255,255,255,0.88)'}}>{o}</div>
        </Karta>
      ))}
    </div>
    <div style={{position: 'absolute', left: 120, right: 120, top: 640}}>
      <Karta od={natez} akcent style={{textAlign: 'center', fontSize: 26, lineHeight: 1.4, fontWeight: 700}}>Tam natężenie bodźców jest największe — i tam najczęściej dochodzi do zachowań trudnych, które potem opisujemy jako „zachowania na lekcji”.</Karta>
    </div>
  </Tlo>
);

const GDY = ['obszar kontaktów wyraźnie niższy przy zachowanych obszarach uczenia się i poruszania', 'trudność w odczytywaniu mimiki, gestu i tonu głosu', 'rozumienie dosłowne — brak rozpoznania żartu i ironii', 'nie odróżnia przypadkowego potrącenia od celowego zaczepienia', 'w pracy grupowej nie przyjmuje perspektywy kolegi', 'zespół rozważa wystąpienie do poradni (całościowe zaburzenia rozwoju)'];
const Tom: React.FC<{def: number; fund: number; kiedy: number; od: number[]; wiek: number; nietest: number}> = ({def, fund, kiedy, od, wiek, nietest}) => (
  <Tlo>
    <Naglowek kicker="Trzecie narzędzie" tytul="Obserwacja poznania społecznego i teorii umysłu" />
    <div style={{position: 'absolute', left: 90, right: 90, top: 205, display: 'grid', gridTemplateColumns: '1.05fr 1fr', gap: 22}}>
      <div style={{display: 'flex', flexDirection: 'column', gap: 16}}>
        <Karta od={def} style={{fontSize: 23, lineHeight: 1.4}}>Teoria umysłu to zdolność przypisywania sobie i innym <b style={{color: '#F6A57E'}}>stanów umysłu</b>: wiedzy, przekonań, intencji i emocji — oraz rozumienia, że mogą one różnić się od naszych.</Karta>
        <Karta od={fund} akcent style={{fontSize: 21, lineHeight: 1.4}}>Fundament: współpraca w grupie · żart · ironia · praca projektowa · rozumienie tekstu literackiego</Karta>
        <Karta od={wiek} style={{fontSize: 20, lineHeight: 1.4}}><b>Wiek:</b> fałszywe przekonanie I rzędu — od ok. 4. r.ż.; II rzędu („co Ola myśli, że Kuba myśli”) — od ok. 6.–7. r.ż. W szkole obserwujemy ironię, żart, obietnicę, kłamstwo uprzejmościowe i intencję za zachowaniem rówieśnika.</Karta>
        <Karta od={nietest} style={{fontSize: 21, lineHeight: 1.4, borderColor: '#F6A57E', textAlign: 'center', fontWeight: 700}}>Opisuje zachowania. Nie jest testem. Nie prowadzi do rozpoznania — prowadzi do rzetelnego opisu dla poradni.</Karta>
      </div>
      <div>
        <Pojaw od={kiedy}><div style={{fontSize: 18, letterSpacing: 3, color: 'rgba(255,255,255,0.75)', textTransform: 'uppercase', marginBottom: 12}}>Kiedy taka obserwacja jest potrzebna?</div></Pojaw>
        <div style={{display: 'flex', flexDirection: 'column', gap: 10}}>
          {GDY.map((g, i) => (
            <Karta key={g} od={od[i]} style={{display: 'flex', gap: 14, alignItems: 'center', padding: '10px 16px'}}>
              <Kolo n="✓" kolor={MARKA.morski} rozmiar={40} />
              <div style={{fontSize: 20.5, lineHeight: 1.3}}>Gdy {g}</div>
            </Karta>
          ))}
        </div>
      </div>
    </div>
  </Tlo>
);

const Decyzja: React.FC<{karta: number; kroki: number; nie: number; chroni: number; dalej: number}> = ({karta, kroki, nie, chroni, dalej}) => (
  <Tlo>
    <Naglowek kicker="Moduł zamyka karta decyzyjna — jedna na jednego ucznia" tytul="Karta decyzyjna obserwacji pogłębionej" />
    <div style={{position: 'absolute', left: 110, right: 110, top: 215, display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 22}}>
      <Karta od={karta} style={{padding: '22px 24px'}}>
        <div style={{fontSize: 18, letterSpacing: 3, color: '#F6A57E', fontWeight: 800, marginBottom: 12}}>KROK 1 · SPRAWDZAMY SIEDEM REGUŁ</div>
        {['1 · obszar ≤ 8 pkt (0–20)', '2 · ≥ 2 twierdzenia na 1–2 w obszarze', '3 · rozbieżność ≥ 2 steny', '4 · sygnał zdrowotny z metryczki', '5 · zachowanie zagrażające — natychmiast', '6 · brak poprawy ok. 3 miesiące', '7 · nagła zmiana funkcjonowania'].map((r, i) => (
          <div key={r} style={{display: 'flex', gap: 12, alignItems: 'center', padding: '6px 0', borderTop: i ? '1px solid rgba(255,255,255,0.12)' : 'none', fontSize: 21}}>
            <div style={{width: 26, height: 26, borderRadius: 6, border: '2px solid #F6A57E', display: 'grid', placeItems: 'center', fontSize: 16, fontWeight: 800, color: '#F6A57E'}}>{i === 0 || i === 3 ? '✓' : ''}</div>
            {r}
          </div>
        ))}
      </Karta>
      <div style={{display: 'flex', flexDirection: 'column', gap: 16}}>
        <Karta od={kroki} style={{padding: '20px 24px'}}>
          <div style={{fontSize: 18, letterSpacing: 3, color: '#F6A57E', fontWeight: 800, marginBottom: 10}}>KROK 2 · WPISUJEMY</div>
          {[['Narzędzie', 'profil sensoryczny + ABC'], ['Kto obserwuje', 'wychowawczyni + nauczyciel współorganizujący'], ['Od kiedy', '22.09.2026 (2–3 tygodnie)'], ['Spotkanie zespołu', '15.10.2026']].map(([k, v]) => (
            <div key={k} style={{display: 'grid', gridTemplateColumns: '190px 1fr', gap: 12, padding: '6px 0', fontSize: 21, borderTop: '1px solid rgba(255,255,255,0.12)'}}><div style={{color: 'rgba(255,255,255,0.7)'}}>{k}</div><div style={{fontWeight: 700}}>{v}</div></div>
          ))}
        </Karta>
        <Karta od={nie} akcent style={{fontSize: 22, lineHeight: 1.4, fontWeight: 700}}>Kartę wpinamy do teczki również wtedy, gdy decyzja brzmi: <u>nie uruchamiamy</u>.</Karta>
        <Karta od={chroni} style={{fontSize: 21, lineHeight: 1.4}}>Zapis decyzji odmownej pokazuje, że zespół sprawę rozważył — i chroni nas, gdy pół roku później ktoś zapyta, dlaczego nic nie zrobiono.</Karta>
        <Karta od={dalej} style={{fontSize: 19, lineHeight: 1.35, textAlign: 'center', color: 'rgba(255,255,255,0.85)'}}>Moduł siódmy: od zebranych danych do oceny, programu i ewaluacji.</Karta>
      </div>
    </div>
  </Tlo>
);

const Przeplyw: React.FC<{pyt: number; strzalki: number}> = ({pyt, strzalki}) => (
  <Tlo>
    <Naglowek kicker="Do czego służą te obserwacje?" tytul="Z obserwacji do oceny, programu i opinii" od={pyt} />
    <div style={{position: 'absolute', left: 80, right: 80, top: 260, display: 'grid', gridTemplateColumns: '1.3fr 60px 1fr 60px 1fr 60px 1fr', gap: 10, alignItems: 'center'}}>
      <Karta od={strzalki} style={{padding: '20px 20px'}}>
        <div style={{fontSize: 17, letterSpacing: 3, color: '#F6A57E', fontWeight: 800}}>4 NARZĘDZIA + PROFIL BIO</div>
        <div style={{fontSize: 21, lineHeight: 1.45, marginTop: 8}}>ABC / FBA · profil sensoryczny · teoria umysłu · karta mowy · profil biopsychospołeczny (ICF)</div>
      </Karta>
      <Pojaw od={strzalki + 6}><div style={{fontSize: 48, color: '#F6A57E', textAlign: 'center'}}>→</div></Pojaw>
      <Karta od={strzalki + 8} style={{padding: '20px 20px', textAlign: 'center'}}><div style={{fontSize: 17, letterSpacing: 3, color: '#F6A57E', fontWeight: 800}}>WOPF</div><div style={{fontSize: 24, fontWeight: 800, marginTop: 8, lineHeight: 1.25}}>sekcje VI–IX oceny wielospecjalistycznej</div></Karta>
      <Pojaw od={strzalki + 14}><div style={{fontSize: 48, color: '#F6A57E', textAlign: 'center'}}>→</div></Pojaw>
      <Karta od={strzalki + 16} akcent style={{padding: '20px 20px', textAlign: 'center'}}><div style={{fontSize: 17, letterSpacing: 3, fontWeight: 800, color: 'rgba(255,255,255,0.85)'}}>IPET</div><div style={{fontSize: 24, fontWeight: 800, marginTop: 8, lineHeight: 1.25}}>zalecenie ze źródłem w obserwacji</div></Karta>
      <Pojaw od={strzalki + 22}><div style={{fontSize: 48, color: '#F6A57E', textAlign: 'center'}}>→</div></Pojaw>
      <Karta od={strzalki + 24} style={{padding: '20px 20px', textAlign: 'center'}}><div style={{fontSize: 17, letterSpacing: 3, color: '#F6A57E', fontWeight: 800}}>PORADNIA</div><div style={{fontSize: 24, fontWeight: 800, marginTop: 8, lineHeight: 1.25}}>opinia o funkcjonowaniu ucznia w 10 dni</div></Karta>
    </div>
    <div style={{position: 'absolute', left: 160, right: 160, top: 620}}>
      <Karta od={strzalki + 30} style={{textAlign: 'center', fontSize: 25, lineHeight: 1.45}}>Kwestionariusz mówi <b style={{color: '#F6A57E'}}>gdzie</b> · obserwacja pogłębiona mówi <b style={{color: '#F6A57E'}}>dlaczego</b> · program mówi <b style={{color: '#F6A57E'}}>co robimy i po czym poznamy, że działa</b></Karta>
    </div>
  </Tlo>
);

const PRAWO: [string, string, string][] = [
  ['Prawo oświatowe, art. 127', 'w czterech drukach było t.j. Dz.U. 2024 poz. 737 — obowiązuje t.j. Dz.U. 2026 poz. 820', 'POPRAWIONO'],
  ['Rozp. MEN z 9.08.2017 r. — pomoc pp i kształcenie specjalne', 'pierwotne Dz.U. 2017 poz. 1591 i 1578 → t.j. Dz.U. 2023 poz. 1798 i t.j. Dz.U. 2020 poz. 1309 (ABC, Dunn, profil bio, karty mowy I–III / IV–VI / VII–VIII)', 'POPRAWIONO'],
  ['Dokumentacja przebiegu nauczania', 'arkusze obserwacji pogłębionej = dokumentacja badań i czynności uzupełniających — rozp. MEN z 25.08.2017 r., t.j. Dz.U. 2024 poz. 50', 'PODSTAWA'],
  ['Reguły przekierowania i karta decyzyjna', 'nie wynikają wprost z przepisu — decyzja rady pedagogicznej wpisana do procedury szkoły', 'PROCEDURA'],
  ['Granica kompetencji', 'nauczyciel opisuje obserwowane zachowanie; rozpoznanie i kwalifikacja do terapii — logopeda, psycholog, terapeuta SI, lekarz', 'ZASADA'],
];
const Straznik: React.FC<{od: number[]}> = ({od}) => {
  const frame = useCurrentFrame();
  const tarcza = useWejscie(0, {damping: 10, stiffness: 120});
  return (
    <Tlo>
      <div style={{position: 'absolute', left: 0, right: 0, top: 44, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 26}}>
        <div style={{width: 96, height: 96, borderRadius: '50%', background: MARKA.pomarancz, display: 'grid', placeItems: 'center', fontSize: 52, transform: `scale(${tarcza * (1 + 0.03 * Math.sin(frame / 8))})`, boxShadow: '0 16px 40px rgba(232,69,10,0.5)'}}>⚖</div>
        <Pojaw od={2}>
          <div style={{fontSize: 56, fontWeight: 800, color: '#fff', lineHeight: 1}}>Strażnik prawa · obserwacja pogłębiona</div>
          <div style={{fontSize: 20, color: 'rgba(255,255,255,0.75)', marginTop: 8, letterSpacing: 1.5}}>publikatory z druków ABC/PBS, profilu sensorycznego, profilu biopsychospołecznego i kart mowy — wg skryptu, część 6</div>
        </Pojaw>
      </div>
      <div style={{position: 'absolute', left: 90, right: 90, top: 200, background: 'rgba(255,255,255,0.07)', border: '1.5px solid rgba(255,255,255,0.25)', borderRadius: 20, overflow: 'hidden'}}>
        {PRAWO.map(([a, b, c], i) => {
          const w = Math.max(0, Math.min(1, (frame - od[i]) / 10));
          const kolor = c === 'POPRAWIONO' ? MARKA.pomarancz : '#2F8F8A';
          return (
            <div key={a} style={{display: 'grid', gridTemplateColumns: '1fr 2.2fr 190px', padding: '19px 26px', borderTop: i ? '1px solid rgba(255,255,255,0.12)' : 'none', opacity: w, transform: `translateX(${(1 - w) * -20}px)`, color: '#fff', fontSize: 23, lineHeight: 1.35, alignItems: 'center', gap: 20}}>
              <div style={{fontWeight: 800}}>{a}</div>
              <div style={{color: 'rgba(255,255,255,0.9)'}}>{b}</div>
              <div style={{textAlign: 'center'}}><span style={{display: 'inline-block', background: kolor, color: '#fff', fontWeight: 800, fontSize: 16, padding: '6px 14px', borderRadius: 999}}>{c}</span></div>
            </div>
          );
        })}
      </div>
    </Tlo>
  );
};

const Final: React.FC<{haslo: number; logo: number}> = ({haslo, logo}) => (
  <Tlo>
    <div style={{position: 'absolute', left: 0, right: 0, top: 150, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
      <Pojaw od={0}><div style={{fontSize: 56, fontWeight: 800, color: '#fff', textAlign: 'center', lineHeight: 1.2}}>Kwestionariusz mówi gdzie.<br />Obserwacja pogłębiona mówi dlaczego.</div></Pojaw>
      <Pojaw od={logo} style={{marginTop: 50, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
        <Logo rozmiar={120} />
        <div style={{fontSize: 84, fontWeight: 800, color: '#fff', letterSpacing: -2, marginTop: 18, lineHeight: 1}}>EduPlaner <span style={{color: '#F6A57E'}}>2026</span></div>
      </Pojaw>
      <Pojaw od={haslo}>
        <div style={{fontSize: 38, color: '#fff', fontWeight: 700, marginTop: 22}}>Mniej dokumentów. Więcej edukacji.</div>
        <div style={{marginTop: 30, fontSize: 19, color: 'rgba(255,255,255,0.7)', letterSpacing: 2, textAlign: 'center'}}>SZKOŁA PODSTAWOWA · OBSERWACJA POGŁĘBIONA · SKRYPT CZĘŚĆ 6 · STRAŻNIK PRAWA<br />PCTP KOSZALIN · kontakt@eduplaner2026.pl · 662 888 403</div>
      </Pojaw>
    </div>
  </Tlo>
);

/* ---------- składanie ---------- */
const Przejscie: React.FC<{trwanie: number; children: React.ReactNode}> = ({trwanie, children}) => {
  const frame = useCurrentFrame();
  const o = Math.min(interpolate(frame, [0, 10], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}), interpolate(frame, [trwanie - 9, trwanie - 1], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}));
  return <AbsoluteFill style={{opacity: o, transform: `scale(${0.985 + 0.015 * o})`}}>{children}</AbsoluteFill>;
};
const PasekPostepu: React.FC = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  return <div style={{position: 'absolute', left: 0, bottom: 0, height: 6, width: `${(100 * frame) / durationInFrames}%`, background: MARKA.pomarancz}} />;
};

const rc = (arkusz: number, obszar: string, k: number, v: number) => `@${arkusz} tr.arow[data-area="${obszar}"] .rc[data-v="${v}"] #${k}`;
/** Oceny z pliku autorki nakładane w tempie `krok` s od `start` (lub wszystkie od razu, gdy krok = 0). */
const oceny = (plik: string, start: number, krok: number): Krok[] => OCENY[plik].map(([a, o, k, v], i) => ({sek: start + i * krok, typ: 'klasa', selektor: rc(a, o, k, v), klasa: 'on'}));
const daty = (n: number, data: string): Krok[] => Array.from({length: n}, (_, i): Krok => ({sek: 0, typ: 'tekst', selektor: `@${i + 1} .student .blank #0`, tekst: data, tempo: 999}));
const CSS_WSPOLNY = [
  '.addrow,.delrow,.delcell,.printcell{display:none!important}',
  '.druk-oryginalny .sheet,.druk-oryginalny .page{box-shadow:0 10px 40px rgba(45,27,105,0.18)}',
  '.druk-oryginalny .mvl,.druk-oryginalny .blank,.druk-oryginalny .dline,.druk-oryginalny .fv{overflow-wrap:break-word;white-space:normal;height:auto;min-height:15px}',
  '.druk-oryginalny .mvl,.druk-oryginalny .blank{display:block;max-width:100%;box-sizing:border-box}',
  '.druk-oryginalny table.tbl td .dline{display:block!important;width:100%!important;min-width:0!important}',
  '.druk-oryginalny .bx.on{background:#2D1B69!important;border-color:#2D1B69!important}',
  '.druk-oryginalny .bx.on::after{content:"✓";display:block;color:#fff;font-size:8px;line-height:9px;text-align:center;font-weight:800}',
].join('\n');

export const ObserwacjaPromo: React.FC<Props> = ({film}) => {
  const {fps} = useVideoConfig();
  const n = film.napisy;
  const z = (i: number) => n[i]?.odSek ?? i * 5;
  const kz = (i: number) => n[i]?.doSek ?? i * 5 + 4;
  const granica = (i: number) => (i <= 0 ? 0 : (kz(i - 1) + z(i)) / 2);
  const fr = (sek: number) => Math.round(sek * fps);
  const lok = (od: number) => (s: number) => Math.max(0, fr(s - od));
  const koniec = film.dlugosc;

  // --- ABC 1: kolumny A/B/C i przykład poprawnego zapisu (zdania 22–31)
  const R = (k: number) => `@1 #abctbl .dline #${k}`;
  const abc1Kroki: Krok[] = [
    ...daty(9, '30.09.2026'),
    {sek: z(22) + 0.3, doSek: kz(22) + 0.2, typ: 'wyroznij', selektor: '@1 #abctbl th #2'},
    {sek: z(23) + 0.3, doSek: kz(23) + 0.2, typ: 'wyroznij', selektor: '@1 #abctbl th #3'},
    {sek: z(24) + 0.3, doSek: kz(24) + 0.2, typ: 'wyroznij', selektor: '@1 #abctbl th #4'},
    {sek: z(26) + 0.2, typ: 'tekst', selektor: R(0), tekst: '22.09 · matematyka, 3. lekcja', tempo: 40},
    {sek: z(26) + 1.4, typ: 'tekst', selektor: R(1), tekst: 'polecenie: przepisać z tablicy zadanie (6 linijek)', tempo: 40},
    {sek: z(27) + 0.2, typ: 'tekst', selektor: R(2), tekst: 'pisał ok. 2 min, odłożył ołówek, położył głowę na ławce, brak reakcji na polecenia ok. 6 min', tempo: 45},
    {sek: z(28) + 0.2, typ: 'tekst', selektor: R(3), tekst: 'N. podszedł, podzielił zadanie na 3 części i zaznaczył pierwszą; uczeń przepisał zaznaczoną część', tempo: 45},
    {sek: z(29) + 0.8, typ: 'tekst', selektor: R(4), tekst: 'ucieczka / unikanie zadania', tempo: 30},
    {sek: z(30) + 0.2, doSek: kz(31) + 0.3, typ: 'wyroznij', selektor: '@1 #abctbl tbody tr #0'},
  ];
  const abc1Kamera: Ujecie[] = [
    {sek: 0, selektor: '@1 .sec #0', skala: 1.6, przesun: -60},
    {sek: z(22), selektor: '@1 #abctbl', skala: 1.75, przesun: -170},
    {sek: z(25), selektor: '@1 #abctbl tbody tr #0', skala: 2.05, przesun: 60},
  ];
  // --- ABC 2: kwestionariusz FBA (25 pozycji), sumy funkcji, hipoteza, zachowanie zastępcze (35–43)
  const abc2Kroki: Krok[] = [...daty(9, '30.09.2026'), ...oceny('abc', z(35) + 0.3, 0.22)];
  const abc2Kamera: Ujecie[] = [
    {sek: 0, selektor: '@2 tr.arow #0', skala: 1.9, przesun: 200},
    {sek: z(35) + 3.0, selektor: '@3 tr.arow #0', skala: 1.9, przesun: 260},
    {sek: z(37), selektor: '@5 .sec #0', skala: 1.9, przesun: 200},
    {sek: z(38), selektor: '@5 .sec #1', skala: 1.9, przesun: 220},
    {sek: z(39), selektor: '@7 .eyebrow', skala: 1.8, przesun: 290},
    {sek: z(41), selektor: '@7 .fnhd #0', skala: 1.85, przesun: 330},
  ];
  // --- Profil sensoryczny 1: struktura 7 zmysłów, test modulacji, trzy wzorce (44–50)
  const dunn1Kroki: Krok[] = [
    ...daty(13, '22.09.2026'),
    {sek: 0, typ: 'tekst', selektor: '@1 .mvl #0', tekst: '22.09.2026 (obserwacja 08–22.09.2026)', tempo: 999},
    {sek: 0, typ: 'tekst', selektor: '@1 .mvl #1', tekst: 'mgr Joanna Malinowska — terapeuta SI (konsultacja) · mgr Katarzyna Wiśniewska', tempo: 999},
    ...oceny('dunn', z(45) + 0.4, 0.11),
    {sek: z(48) + 0.2, doSek: kz(48) + 0.2, typ: 'wyroznij', selektor: '@2 tr.secrow #0'},
    {sek: z(49) + 0.2, doSek: kz(49) + 0.2, typ: 'wyroznij', selektor: '@2 tr.secrow #1'},
    {sek: z(50) + 0.2, doSek: kz(50) + 0.2, typ: 'wyroznij', selektor: '@2 tr.secrow #2'},
  ];
  const dunn1Kamera: Ujecie[] = [
    {sek: 0, selektor: '@1 .sec #0', skala: 1.8, przesun: -40},
    {sek: z(45), selektor: '@1 .sec #1', skala: 1.9, przesun: 200},
    {sek: z(46) + 1.0, selektor: '@2 tr.arow #0', skala: 1.9, przesun: 200},
    {sek: z(48), selektor: '@2 tr.secrow #0', skala: 2.0, przesun: 110},
    {sek: z(49), selektor: '@2 tr.secrow #1', skala: 2.0, przesun: 110},
    {sek: z(50), selektor: '@2 tr.secrow #2', skala: 2.0, przesun: 110},
  ];
  // --- Profil sensoryczny 2: wykres 7 zmysłów, wynik i charakterystyka, granica kompetencji (53–57)
  const dunn2Kroki: Krok[] = [...daty(13, '22.09.2026'), ...oceny('dunn', 0, 0), {sek: z(57) + 0.3, doSek: kz(57) + 0.3, typ: 'wyroznij', selektor: '@6 .sec #0'}];
  const dunn2Kamera: Ujecie[] = [
    {sek: 0, selektor: '@8 svg #0', skala: 1.9, przesun: 150},
    {sek: z(54), selektor: '@6 .sec #0', skala: 1.85, przesun: 220},
    {sek: z(56), selektor: '@7 .sec #0', skala: 1.85, przesun: 220},
  ];
  // --- Karta mowy I–III (74–95)
  const mowaKroki: Krok[] = [
    ...daty(5, '24.09.2026'),
    {sek: z(74) + 0.4, typ: 'tekst', selektor: '@1 .mvl #0', tekst: '24.09.2026', tempo: 40},
    {sek: z(74) + 1.2, typ: 'tekst', selektor: '@1 .mvl #1', tekst: 'mgr Piotr Kowalczyk — neurologopeda', tempo: 40},
    {sek: z(74) + 2.4, typ: 'tekst', selektor: '@1 .dline #0', tekst: 'mgr Piotr Kowalczyk', tempo: 40},
    ...oceny('mowa13', z(79) + 0.3, 0.2),
    {sek: z(85) + 0.3, doSek: kz(86) + 0.3, typ: 'wyroznij', selektor: '@1 .arsum[data-c="II"]'},
    {sek: z(88) + 0.2, doSek: kz(90) + 0.3, typ: 'wyroznij', selektor: '@4 .sec #0'},
    {sek: z(92) + 0.3, doSek: kz(95) + 0.3, typ: 'wyroznij', selektor: '@4 .sec #2'},
  ];
  const mowaKamera: Ujecie[] = [
    {sek: 0, selektor: '@1 .sec #0', skala: 1.9, przesun: 120},
    {sek: z(76), selektor: '@1 .sec #1', skala: 1.9, przesun: 190},
    {sek: z(79) + 0.2, selektor: '@1 tr.arow #0', skala: 1.9, przesun: 200},
    {sek: z(81), selektor: '@2 tr.arow #0', skala: 1.9, przesun: 220},
    {sek: z(85), selektor: '@1 tr.cmprow #1', skala: 2.0, przesun: 30},
    {sek: z(87), selektor: '@3 svg #0', skala: 1.9, przesun: 150},
    {sek: z(91), selektor: '@4 .sec #0', skala: 1.9, przesun: 200},
    {sek: z(92), selektor: '@4 .sec #2', skala: 1.9, przesun: 200},
  ];
  // --- Profil biopsychospołeczny (105–106)
  const bioBx = [2, 6, 7, 20, 22, 25, 32, 33, 36, 38, 44];
  const bioKroki: Krok[] = [
    {sek: 0, typ: 'tekst', selektor: '.fv #0', tekst: 'Zofia Lewandowska', tempo: 999},
    {sek: 0, typ: 'tekst', selektor: '.fv #1', tekst: '14.03.2017 · 9 lat', tempo: 999},
    {sek: 0, typ: 'tekst', selektor: '.fv #2', tekst: 'III A · I etap edukacyjny', tempo: 999},
    ...bioBx.map((g, i): Krok => ({sek: z(105) + 0.4 + i * 0.35, typ: 'klasa', selektor: `.bx #${g}`, klasa: 'on'})),
    {sek: 0, typ: 'tekst', selektor: '.ed #0', tekst: 'Zasoby: pamięć wzrokowa i czytanie globalne (ok. 20 wyrazów), zainteresowanie przyrodą, sprawność ruchowa w znanych zadaniach, jedna stała koleżanka (Ola), zaangażowani rodzice i spójne rutyny domowe, akceptacja klasy.', tempo: 999},
    {sek: 0, typ: 'tekst', selektor: '.ed #1', tekst: 'Bariery: nadwrażliwość słuchowa — hałas w klasie, na stołówce i korytarzu skraca czas pracy z ok. 8 do 1 minuty; brak strefy wyciszenia w pobliżu sali; zbyt liczna klasa (26 uczniów); zadania wieloetapowe bez wsparcia wizualnego; lęk przed odpowiedzią przy tablicy; wolne tempo pisania (motoryka mała).', tempo: 999},
    {sek: 0, typ: 'tekst', selektor: '.ed #2', tekst: 'Ułatwiacze: pierwsza ławka przy nauczycielu, słuchawki wyciszające dostępne bez proszenia, zadania w 3 krokach z piktogramami, karta „proszę o przerwę”, nauczyciel współorganizujący (mgr Ewa Sikora), strefa wyciszenia w sali 12, przewidywalny plan dnia z zapowiedzią zmian, współpraca z rodzicami co 4 tygodnie.', tempo: 999},
  ];
  const bioKamera: Ujecie[] = [
    {sek: 0, selektor: '@1 .sec #0', skala: 1.8, przesun: 120},
    {sek: z(105) + 1.5, selektor: '@2 .subhead #0', skala: 1.8, przesun: 260},
    {sek: z(105) + 6.5, selektor: '@2 .sec #1', skala: 1.8, przesun: 260},
    {sek: z(106), selektor: '@3 .sec #0', skala: 1.75, przesun: 300},
  ];

  type Scena = {id: string; od: number; do: number; el: (od: number) => React.ReactNode};
  const L = (od: number) => lok(od);
  const sceny: Scena[] = [
    {id: 'intro', od: 0, do: granica(4), el: (od) => <Intro gdzie={L(od)(z(1))} dlaczego={L(od)(z(2))} cel={L(od)(z(3))} />},
    {id: 'przesiew', od: granica(4), do: granica(8), el: (od) => <Przesiew p={L(od)(z(4))} o={L(od)(z(5))} kier={L(od)(z(6))} koszt={L(od)(z(7))} />},
    {id: 'reguly', od: granica(8), do: granica(20), el: (od) => <Reguly od={[10, 11, 12, 13, 14, 15, 16].map((i) => L(od)(z(i)))} rada={L(od)(z(17))} przepis={L(od)(z(18))} kto={L(od)(z(19))} />},
    {id: 'narzedzia', od: granica(20), do: granica(22), el: (od) => <Narzedzia od={L(od)(z(20))} abc={L(od)(z(21))} />},
    {id: 'abc1', od: granica(22), do: granica(32), el: (od) => <OryginalnyDruk plik="abc.html" kroki={abc1Kroki} kamera={abc1Kamera} odSek={od} css={CSS_WSPOLNY} />},
    {id: 'wadliwy', od: granica(32), do: granica(35), el: (od) => <Wadliwy zapis={L(od)(z(33))} trzy={L(od)(z(34))} />},
    {id: 'abc2', od: granica(35), do: granica(44), el: (od) => <OryginalnyDruk plik="abc.html" kroki={abc2Kroki} kamera={abc2Kamera} wykresyOdSek={z(37) + 0.2} odSek={od} css={CSS_WSPOLNY} />},
    {id: 'dunn1', od: granica(44), do: granica(51), el: (od) => <OryginalnyDruk plik="dunn.html" kroki={dunn1Kroki} kamera={dunn1Kamera} odSek={od} css={CSS_WSPOLNY} />},
    {id: 'miejsca', od: granica(51), do: granica(53), el: (od) => <Miejsca od={L(od)(z(51))} natez={L(od)(z(52))} />},
    {id: 'dunn2', od: granica(53), do: granica(58), el: (od) => <OryginalnyDruk plik="dunn.html" kroki={dunn2Kroki} kamera={dunn2Kamera} wykresyOdSek={z(53) + 0.3} odSek={od} css={CSS_WSPOLNY} />},
    {id: 'tom', od: granica(58), do: granica(74), el: (od) => <Tom def={L(od)(z(59))} fund={L(od)(z(60))} kiedy={L(od)(z(61))} od={[62, 63, 64, 65, 66, 67].map((i) => L(od)(z(i)))} wiek={L(od)(z(68))} nietest={L(od)(z(71))} />},
    {id: 'mowa', od: granica(74), do: granica(96), el: (od) => <OryginalnyDruk plik="mowa13.html" kroki={mowaKroki} kamera={mowaKamera} wykresyOdSek={z(87) + 0.3} odSek={od} css={CSS_WSPOLNY} />},
    {id: 'decyzja', od: granica(96), do: granica(103), el: (od) => <Decyzja karta={L(od)(z(97))} kroki={L(od)(z(98))} nie={L(od)(z(99))} chroni={L(od)(z(100))} dalej={L(od)(z(102))} />},
    {id: 'przeplyw', od: granica(103), do: granica(105), el: (od) => <Przeplyw pyt={L(od)(z(103))} strzalki={L(od)(z(104))} />},
    {id: 'bio', od: granica(105), do: granica(107), el: (od) => <OryginalnyDruk plik="bio.html" kroki={bioKroki} kamera={bioKamera} odSek={od} css={CSS_WSPOLNY} />},
    {id: 'straznik', od: granica(107), do: granica(112), el: (od) => <Straznik od={[108, 109, 110, 110, 111].map((i, j) => L(od)(z(i) + (j === 3 ? 4.5 : 0)))} />},
    {id: 'final', od: granica(112), do: koniec, el: (od) => <Final logo={L(od)(z(113))} haslo={L(od)(z(114))} />},
  ];

  return (
    <AbsoluteFill style={{background: MARKA.tlo}}>
      {film.audio ? <Audio src={staticFile(film.audio)} /> : null}
      {sceny.map((s) => {
        const od = fr(s.od);
        const trwanie = Math.max(1, fr(s.do) - od);
        return (
          <Sequence key={s.id} from={od} durationInFrames={trwanie} name={s.id}>
            <Przejscie trwanie={trwanie}>{s.el(s.od)}</Przejscie>
          </Sequence>
        );
      })}
      <Napisy napisy={n} />
      <PasekPostepu />
    </AbsoluteFill>
  );
};
