import telebot
from token import bottoken
from telebot import types
from signup import *
from keyboards import *

bot = telebot.TeleBot(bottoken)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, "Привет, я бот Тайной комнаты, если ты хочешь узнать о нас больше - нажми Инфо, если ты уже играешь у нас, нажми Регистрация", reply_markup=startboard)

@bot.message_handler(content_types=['text'])
def send_text(message):
    nid = message.chat.id
    if message.text == 'Регистрация':
        if playercheck(nid):
            msg = bot.send_message(nid, "Как тебя зовут?")
            bot.register_next_step_handler(msg, reg_step)
        else:
            bot.send_message(nid, "Вы уже зарегистрированы", reply_markup=mainboard)
    elif message.text == 'Инфо':
        bot.send_message(nid, "Чё-нить потом тут будет")


@bot.message_handler(func=lambda m :True)
def echo_all(message):
    bot.reply_to(message.from_user.id, message.text)



bot.polling()