#!/usr/bin/env bash
# Blokuje commit, jesli w zmianach jest klucz API albo plik .env.
#
# Instalacja jako hook (jednorazowo, na kazdym komputerze):
#     ln -sf ../../scripts/sprawdz-sekrety.sh .git/hooks/pre-commit
#
# Uruchomienie recznie na tym, co masz w poczekalni:
#     ./scripts/sprawdz-sekrety.sh
#
# Hooki nie sa czescia repozytorium — Git ich nie klonuje. Dlatego skrypt
# lezy w scripts/ (jest wersjonowany), a dowiazanie tworzysz u siebie.

set -uo pipefail

CZERWONY=$'\033[31m'; ZOLTY=$'\033[33m'; RESET=$'\033[0m'
znaleziono=0

# Pliki w poczekalni; przy recznym uruchomieniu bez niczego — cale repozytorium.
pliki=$(git diff --cached --name-only --diff-filter=ACM 2>/dev/null)
[ -z "$pliki" ] && pliki=$(git ls-files)

# 1. Czy ktos nie probuje wrzucic samego .env
for p in $pliki; do
    case "$p" in
        .env|*/.env|.env.local|*/.env.local)
            echo "${CZERWONY}✗ $p — plik ze zmiennymi środowiskowymi nie należy do repozytorium.${RESET}"
            echo "  Usuń go z poczekalni:  git reset HEAD $p"
            znaleziono=1
            ;;
    esac
done

# 2. Wzorce kluczy. .env.example jest pomijany — trzyma same nazwy zmiennych.
#    hg_… i sk_… to HeyGen i ElevenLabs; xi-api-key to nagłówek ElevenLabs.
WZORCE='hg_[A-Za-z0-9_-]{16,}|sk_[A-Za-z0-9_-]{20,}|xi-api-key: *[A-Za-z0-9]|X-Api-Key: *[A-Za-z0-9]{16,}'

for p in $pliki; do
    [ -f "$p" ] || continue
    case "$p" in
        .env.example|*/.env.example|scripts/sprawdz-sekrety.sh) continue ;;
    esac
    trafienia=$(grep -nIE "$WZORCE" "$p" 2>/dev/null \
                | grep -vE '\$\{?[A-Z_]+\}?|TWÓJ_KLUCZ|your-api-key|WKLEJ|\.\.\.|<[a-z_]+>' || true)
    if [ -n "$trafienia" ]; then
        echo "${CZERWONY}✗ $p — wygląda na klucz API:${RESET}"
        # pokazujemy sam numer linii i poczatek, nigdy calej wartosci
        echo "$trafienia" | cut -c1-60 | sed 's/^/    /'
        znaleziono=1
    fi
done

if [ "$znaleziono" -ne 0 ]; then
    cat <<EOF

${ZOLTY}Commit zatrzymany.${RESET}

Klucze trzymaj w .env (jest w .gitignore) albo w ~/.zshrc, nigdy w plikach repozytorium.
Jeśli klucz zdążył już gdzieś wyciec — najpierw go unieważnij w panelu dostawcy,
dopiero potem sprzątaj pliki. Unieważnienie działa; czyszczenie historii nie cofa
tego, co ktoś już zdążył skopiować.

Jeśli to fałszywy alarm:  git commit --no-verify
EOF
    exit 1
fi

echo "✓ Brak kluczy w zmianach."
exit 0
