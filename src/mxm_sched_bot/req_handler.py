import bot_logic


def req_handler(bot):
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.from_user.id,
                         bot_logic.start_message(message.from_user.id, message.from_user.username))

    @bot.message_handler(commands=['info'])
    def info_message(message):
        bot.send_message(message.from_user.id, bot_logic.info_message())

    @bot.message_handler(commands=['help'])
    def help_message(message):
        bot.send_message(message.from_user.id, bot_logic.help_message())

    @bot.message_handler(commands=['setgroup'])
    def setgroup_message(message):
        bot.send_message(message.from_user.id, 'Setting group')
