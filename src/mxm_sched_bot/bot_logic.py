import db_logic
from db_logic import states


def start_message(user_id, username):
    if db_logic.add_user(user_id, username):
        return 'Hello, new user!'
    else:
        return 'Hello, old friend!'


def info_message():
    return 'Hi, im your schedule bot!'


def help_message():
    return 'Список доступных команд:\n' \
           '/start - Бот расскажет немного о себе\n' \
           '/setgroup - Установить группу\n' \
           '/info -  Информация о группе\n' \
           '/reset - Сбросить все в начало\n' \
           '/printday - Вывести расписание на сегодня \n' \
           '/printnextday - Вывести расписание на завтра \n' \
           '/printnextthreedays - Вывести расписание на следующие три дня \n' \
           '/printthisweek - Вывести расписание на текущую неделю \n' \
           '/printnextweek - Вывести расписание на следующую неделю \n'


def set_group():
    pass
