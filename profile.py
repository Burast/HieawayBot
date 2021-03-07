import telebot
from telebot import types
import sqlite3
from keyboards import *

bot = telebot.TeleBot('1602726260:AAEDcaEPtwmpVUcCpSOx8MN37-zgVg054gc')

def showprofile(nid):
    con = sqlite3.connect('rating.db')
    cur = con.cursor()
    cur.execute("""SELECT rowid FROM players WHERE telegramid=?""", (nid, ))
    row = cur.fetchone()
    bot.send_message(nid, "Ваш номер: "+str(row[0]))
