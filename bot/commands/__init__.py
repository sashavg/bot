__all__ = ['register_user_commands', 'bot_commands']
from aiogram import Router
from bot.commands.start import start
from bot.commands.weather import q_weather, get_weather
from bot.commands.chatterbox import q_chatterbox, chatterbox
from aiogram.dispatcher.filters import Command

bot_commands = (
    ('start', 'Начало работы'),
    ('help', 'Помощь'),
    ('weather', 'Найти погоду'),
    ('poetry', 'Придумать стихи'),
    ('chatterbox', 'Просто поговорить')

)

def register_user_commands(router: Router):
    router.message.register(start, Command(commands=['start']))

    router.message.register(q_weather, Command(commands=['weather']))
    router.message.register(get_weather)

    router.message.register(q_chatterbox, Command(commands=['weather']))
    router.message.register(chatterbox)








