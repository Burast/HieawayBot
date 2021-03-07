import telebot
from telebot import types
from signup import *
from keyboards import *
from profile import *
from games import showgames

bot = telebot.TeleBot('1602726260:AAEDcaEPtwmpVUcCpSOx8MN37-zgVg054gc')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, "Привет, я бот Тайной комнаты, если ты хочешь узнать о нас больше - нажми Инфо, если ты уже играешь у нас, нажми Регистрация", reply_markup=startboard)

@bot.message_handler(content_types=['text'])
def send_text(message):
    nid = message.chat.id
    if message.text == 'Регистрация':
        if playercheck(nid):
            bot.send_message(nid, "Вы уже зарегистрированы", reply_markup=mainboard)
        else:
            msg = bot.send_message(nid, "Как тебя зовут?")
            bot.register_next_step_handler(msg, reg_step)
    elif message.text == 'Инфо':
        bot.send_message(nid, "Чё-нить потом тут будет")
    elif message.text == 'Профиль':
        if playercheck(nid):
            showprofile(nid)
        else:
            bot.send_message(nid, "Вы не зарегистрированы", reply_markup=startboard)
    elif message.text == 'Игры':
        showgames(nid)
    elif message.text == 'Партия':
        bot.send_message(nid, "Введите через пробел: id игры и номера игроков в соответствии с местами(первое место (пробел) второе...) Пример для 2х игроков, где играли в игру номер 10 и победил игрок 3:")
        bot.send_message(nid, "10 3 6")
        showgames(nid)




bot.polling()