import asyncio

from aiogram import Bot, Dispatcher, types 
from aiogram.filters import CommandStart 
from aiogram.types import (
        Message,
        InlineQuery,
        InlineQueryResultArticle,
        InputTextMessageContent,
        ChosenInlineResult
        )

from meow import meow, stats
import json

# Получение токена из отдельного вайла
with open("config.json", "r") as f:
    config = json.load(f)
TOKEN = config["token"]


# Функционал бота
bot = Bot(token=TOKEN)
dp = Dispatcher() 

# Обработчик /start
@dp.message(CommandStart()) # /start command decorator.  
async def cmd_start(message: Message): # message - сообщение из телеги
    await message.answer('Мяуу') # Отвечает на сообщение


# Обработчик обычных сообщений боту
@dp.message()
async def echo_all(message: Message):
    await message.answer(meow())


# Инлайн-меню
@dp.inline_query() # Обработчик инлайн сообщений
async def inline_menu(inline_query: InlineQuery): # Функция, принимающая информацию о запросе пользователя
    results: list[InlineQueryResultArticle] = [
        InlineQueryResultArticle(
            id="1",
            title="Мяу",
            description="🐈",
            input_message_content=InputTextMessageContent(
                message_text=meow() 
            )
        ),
        InlineQueryResultArticle(
            id="2",
            title="Статесlkтекр",
            description="📊",
            input_message_content=InputTextMessageContent(
                message_text=stats() 
            ),
        )
    ]
    await bot.answer_inline_query(inline_query.id, results, cache_time=1)


async def main(): 
    await dp.start_polling(bot) # start_polling() - бесконечный цикл опроса серверов тг


if __name__ == '__main__': 
    asyncio.run(main()) # Старт старт асинхронного кода
