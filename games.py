import telebot
import sqlite3

bot = telebot.TeleBot('1602726260:AAEDcaEPtwmpVUcCpSOx8MN37-zgVg054gc')

def showgames(uid):
    con=sqlite3.connect('rating.db')
    cur=con.cursor()
    cur.execute("SELECT * FROM games")
    gamelist = cur.fetchall()
    show = 'Список игр: \n'
    for g in gamelist:
        show += str(g[0]) + ' ' + g[1] + '\n'
    bot.send_message(uid, show)