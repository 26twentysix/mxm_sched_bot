import telebot
from main import TOKEN

bot = telebot.TeleBot(TOKEN)
while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except:
        pass
