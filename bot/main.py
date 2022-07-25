from aiogram import Dispatcher, Bot
import logging
from commands import register_user_commands, bot_commands
from config import token_bot
import asyncio
from aiogram.types import BotCommand

async def main():
    logging.basicConfig(level=logging.DEBUG)

    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))


    bot = Bot(token=token_bot)
    dp = Dispatcher()
    await bot.set_my_commands(commands=commands_for_bot)

    register_user_commands(dp)

    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped")
