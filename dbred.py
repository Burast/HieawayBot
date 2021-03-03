import sqlite3

conn = sqlite3.connect('rating.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS players(
    telegramid INT PRIMARY KEY,
    telegramnick TEXT,
    name TEXT
);""")
conn.commit()
conn.close()
