import sqlite3

conn = sqlite3.connect('rating.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS players(
    ROWID INTEGER PRIMARY KEY AUTOINCREMENT,
    telegramid INT,
    telegramnick TEXT,
    gamename TEXT
);""")

cur.execute("""CREATE TABLE IF NOT EXISTS playermatches(
    ROWID INTEGER PRIMARY KEY AUTOINCREMENT,
    playerid INT,
    matchid INT,
    points INT,
    place INT,
    accept INT,
    FOREIGN KEY (playerid) REFERENCES players(ROWID),
    FOREIGN KEY (matchid) REFERENCES matches(ROWID)
);""")

cur.execute("""CREATE TABLE IF NOT EXISTS matches(
    ROWID INTEGER PRIMARY KEY AUTOINCREMENT,
    gameid INT,
    playersnum INT,
    gamedate TEXT,
    accept INT,
    FOREIGN KEY (gameid) REFERENCES games(ROWID)
);""")

cur.execute("""CREATE TABLE IF NOT EXISTS games(
    ROWID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    coef REAL
);""")
conn.commit()
conn.close()
