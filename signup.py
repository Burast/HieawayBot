import telebot
import sqlite3
from keyboards import mainboard

bot = telebot.TeleBot('1602726260:AAEDcaEPtwmpVUcCpSOx8MN37-zgVg054gc')

def playercheck(uid):
    con=sqlite3.connect('rating.db')
    cursor=con.cursor()
    cursor.execute("SELECT * FROM players WHERE telegramid=?", (uid, ))
    return False if cursor.fetchone()==None else True
        

def reg_step(message):
    conn=sqlite3.connect('rating.db')
    cur=conn.cursor()
    nid = message.from_user.id
    UserInfo=bot.get_chat_member(nid, nid).user
    cur.execute("INSERT INTO players(telegramid, telegramnick, gamename) VALUES(?, ?, ?)", (nid, UserInfo.first_name, message.text))
    conn.commit()
    cur.execute("SELECT rowid FROM players WHERE telegramid=?", (nid,))
    rowid = cur.fetchone()
    bot.send_message(nid, "Успешная регистрация, ваш номер: "+str(rowid[0])+'\n Он нужен для регистрации ваших партий. \n го можно будет посмотреть в профиле.' , reply_markup=mainboard)
    cur.execute("SELECT * FROM players WHERE telegramid=?", (nid, ))
    print(cur.fetchone())

