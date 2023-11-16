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


Aplikacija će biti dostupna na http://localhost:5000/.

API Endpoint
Dobijanje prosečnih vrednosti statistika za igrača
Endpoint: /player_stats/<player_id>
Metoda: GET
Primer: http://localhost:5000/player_stats/1
Odgovor će biti u JSON formatu i sadržaće prosečne vrednosti statistika za traženog igrača.

json
{
    "avg_ftm": 2.5,
    "avg_fta": 3.0,
    "avg_2pm": 5.0,
    "avg_2pa": 8.0,
    "avg_3pm": 1.0,
    "avg_3pa": 2.0,
    "avg_reb": 7.0,
    "avg_blk": 1.2,
    "avg_ast": 3.5,
    "avg_stl": 1.0,
    "avg_tov": 2.0
}
Korišćene Tehnologije

Python
Flask
SQLite
