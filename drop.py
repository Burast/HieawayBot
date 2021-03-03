import sqlite3

conn=sqlite3.connect('rating.db')

cur=conn.cursor()

cur.execute("DROP TABLE players")