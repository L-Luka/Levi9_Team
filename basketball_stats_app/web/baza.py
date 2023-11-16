import sqlite3

# Povezivanje sa bazom
conn = sqlite3.connect('baza.db')
cursor = conn.cursor()

# Izvršavanje SQL skripte
with open('baza.db', 'r') as script:
    cursor.executescript(script.read())

df.to_sql('PlayerStats', conn, if_exists='replace', index=False)

conn.close()
