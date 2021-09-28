import telebot
import os

import req_handler

TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN)
req_handler.req_handler(bot)
bot.polling(none_stop=True, interval=0)
