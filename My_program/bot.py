from telebot import TeleBot
import new_file


API_TOKEN = "6132944980:AAFppxP6IfQf6HhjWs_6c7sjgnH9FYjNnfw"
bot = TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, input('Введите название месяца: '))
    bot.send_message(message.chat.id, new_file.start_table('mouth1'))
    bot.send_message(message.chat.id, "Привествую хозяин")


@bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message, "привествую хозяин")



bot.infinity_polling()