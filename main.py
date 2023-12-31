from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
import asyncio
from parser import parse_cmd
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(os.getenv('TOKEN'))

dp = Dispatcher()


@dp.message(F.text == '/start')
async def start_cmd(message: Message):
    await message.answer(text='Введите ваш запрос и вам выдаст страницу в википедии!')


@dp.message()
async def send_cmd(message: Message):
    if parse_cmd(message.text) != None:
        msg = parse_cmd(message.text)
        await bot.send_message(message.chat.id, text=msg)
    else:
        await bot.send_message(message.chat.id, text='Введен неправильный запрос')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Выход')
