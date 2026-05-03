import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()

# Берём токен бота из переменной окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Включаем логирование, чтобы видеть что происходит
logging.basicConfig(level=logging.INFO)

# Создаём объект бота и диспетчер
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Хендлер на команду /start
@dp.message(CommandStart())
async def cmd_start(message: Message):
    user_name = message.from_user.first_name
    await message.answer(f"Привет, {user_name}! Я твой первый бот. Напиши мне что-нибудь.")


# Хендлер на любое текстовое сообщение
@dp.message(F.text)
async def echo_message(message: Message):
    await message.answer(f"Я получил твоё сообщение: {message.text}")


# Главная функция, запускающая бота
async def main():
    print("Бот запускается...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())