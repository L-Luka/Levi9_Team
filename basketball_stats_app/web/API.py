from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/player_stats/<player_id>', methods=['GET'])
def get_player_stats(player_id):
    conn = sqlite3.connect('baza.db')
    cursor = conn.cursor()

    # Upit za prosečne vrednosti statistika igrača
    query = f'''
        SELECT
            AVG(ftm) as avg_ftm,
            AVG(fta) as avg_fta,
            AVG(2pm) as avg_2pm,
            AVG(2pa) as avg_2pa,
            AVG(3pm) as avg_3pm,
            AVG(3pa) as avg_3pa,
            AVG(reb) as avg_reb,
            AVG(blk) as avg_blk,
            AVG(ast) as avg_ast,
            AVG(stl) as avg_stl,
            AVG(tov) as avg_tov
        FROM PlayerStats
        WHERE player_id = {player_id}
    '''
    
    cursor.execute(query)
    stats = cursor.fetchone()

    # Zatvaranje veze
    conn.close()

    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True)
