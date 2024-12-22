import sqlite3
import pandas as pd

conn = sqlite3.connect('fk_fenner_mrp_may_01_2024.db')
c = conn.cursor()
c.execute('''DROP TABLE IF EXISTS Fenner''')
c.execute('''
    CREATE TABLE IF NOT EXISTS SKUs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        size TEXT UNIQUE,
        pitch_length TEXT,
        Price REAL
    )
''')

fenner_skus = pd.read_csv('tabula-FENNER POLY F MRP DATED 01.05.2024.csv')
fenner_skus.to_sql('Fenner', conn, if_exists='replace', index=False)





