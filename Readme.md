# Basketball Player Stats API

Ova aplikacija pruža API za dobijanje prosečnih vrednosti statistika o učinku košarkaša na različitim utakmicama. Aplikacija je implementirana u Python-u koristeći Flask framework.

## Postavljanje

1. Klonirajte repozitorijum:

    ```bash
    git clone https://github.com/L-Luka/Levi9_Team.git
    ```

2. Instalirajte zavisnosti:

    ```bash
    pip install -r requirements.txt
    ```

3. Napravite `.env` fajl i postavite konfiguracije. Primer `.env` fajla možete pronaći u `.env.example`.

4. Pokrenite skriptu za inicijalizaciju baze podataka:

    ```bash
    python init_db.py
    ```

## Pokretanje

Pokrenite Flask aplikaciju:

```bash
python API.py
