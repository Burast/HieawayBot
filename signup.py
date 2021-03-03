import telebot
import sqlite3
from token import bottoken

bot = telebot.TeleBot(bottoken)

def playercheck(uid):
    con=sqlite3.connect('rating.db')
    cursor=con.cursor()
    cursor.execute("SELECT * FROM players WHERE telegramid=?", (uid, ))
    return True if cursor.fetchone()==None else False
        

def reg_step(message):
    conn=sqlite3.connect('rating.db')
    cur=conn.cursor()
    nid = message.from_user.id
    UserInfo=bot.get_chat_member(nid, nid).user
    cur.execute("INSERT INTO players VALUES(?, ?, ?)", (nid, UserInfo.first_name, message.text))
    conn.commit()
    bot.send_message(nid, "ok")
    cur.execute("SELECT * FROM players WHERE telegramid=?", (nid+1, ))
    print(cur.fetchone())

