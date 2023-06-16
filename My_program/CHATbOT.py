import telebot

bot = telebot.TeleBot("6187135757:AAEOa_qXzOduzwjo1YhWBil_2utHIMT0g68")

@bot.message_handler(commands=['start'])
def start(message):
    # back_end.sart_program()

@bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message.chat.id, "привествую хозяин")



bot.infinity_polling()