import telebot
from pygments.lexers import markup
from telebot import TeleBot
from telebot import types
import datetime
import new_file


API_TOKEN = "6132944980:AAFppxP6IfQf6HhjWs_6c7sjgnH9FYjNnfw"
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привествую хозяин")


@bot.message_handler(commands=['menu'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Ввод данных')
    markup.add(item1)
    item2 = types.KeyboardButton('Статистика')
    markup.add(item2)
    item3 = types.KeyboardButton('Выход')
    markup.add(item3)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Ввод данных":
        bot.send_message(message.chat.id, "https://github.com/Alexander25091998/over1/")
    elif message.text == "Статистика":
        pass
    elif message.text == "Выход":
        pass


bot.infinity_polling()