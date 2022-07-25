from aiogram import types
import requests
import datetime
from bot.config import token_weather

async def q_weather(message: types.message):
    await message.reply('В каком городе посмотреть погоду?')

async def get_weather(message: types.message):
    try:
        r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={token_weather}&units=metric")
        data = r.json()
        city = data["name"]
        temp = data["main"]["temp"]

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Температура в городе {city} составляет: {temp}C°"
              )
    except Exception as ex:

        await message.reply('Я такого города не знаю. Извини')
