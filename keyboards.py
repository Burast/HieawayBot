import telebot
from telebot import types

startboard = telebot.types.ReplyKeyboardMarkup(True)
startboard.row('Инфо')
startboard.row('Регистрация')

mainboard = telebot.types.ReplyKeyboardMarkup(True)
mainboard.row('Профиль','Рейтинг')
mainboard.row('Игры','Партия')