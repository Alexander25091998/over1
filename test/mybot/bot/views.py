import telebot
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import bot_config

bot = telebot.TeleBot('6644411913:AAHSt9xiN5ZsHsIJ4fYiuxT7_QweFX51fkE', parse_mode=None)


@csrf_exempt
def index(request):
    # bot.set_webhook('https://9e93-83-242-179-137.eu.ngrok.io/')
    if request.method == "POST":
        update = telebot.types.Update.de_json(request.body.decode('utf-8'))
        bot.process_new_updates([update])

    return HttpResponse('<h1>Ты подключился!</h1>')


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    name = ''
    if message.from_user.last_name is None:
        name = f'{message.from_user.first_name}'
    else:
        name = f'{message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, f'Привет! {name}\n'
                                      f'Я бот, который будет спамить вам беседу :)\n\n'
                                      f'Чтобы узнать больше команд, напишите /help')
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()


