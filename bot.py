import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
    CallbackQuery,
)
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Создаём объект бота и диспетчер
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# === КЛАВИАТУРЫ ===

# Inline-клавиатура для команды /start
def get_start_inline_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="ℹ️ О боте", callback_data="about"),
                InlineKeyboardButton(text="❓ Помощь", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text="📞 Связаться", callback_data="contact"),
            ],
            [
                InlineKeyboardButton(text="❌ Закрыть", callback_data="close"),
            ],
        ]
    )
    return keyboard


# Reply-клавиатура (постоянное меню снизу)
def get_main_reply_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📋 Меню"),
                KeyboardButton(text="❓ Помощь"),
            ],
            [
                KeyboardButton(text="📞 Контакты"),
            ],
        ],
        resize_keyboard=True,  # автоматически подгоняет размер кнопок
    )
    return keyboard


# === ХЕНДЛЕРЫ КОМАНД ===

@dp.message(CommandStart())
async def cmd_start(message: Message):
    user_name = message.from_user.first_name
    greeting = (
        f"Привет, {user_name}! 👋\n\n"
        f"Я твой первый бот с меню. Выбери действие:"
    )
    await message.answer(
        text=greeting,
        reply_markup=get_start_inline_keyboard(),
    )
    # Заодно покажем reply-клавиатуру
    await message.answer(
        text="Внизу появилось главное меню — им тоже можно пользоваться 👇",
        reply_markup=get_main_reply_keyboard(),
    )


@dp.message(Command("help"))
async def cmd_help(message: Message):
    help_text = (
        "❓ <b>Помощь</b>\n\n"
        "Доступные команды:\n"
        "/start — главное меню\n"
        "/help — эта справка\n"
        "/about — о боте\n\n"
        "Ты также можешь использовать кнопки внизу экрана."
    )
    await message.answer(help_text, parse_mode="HTML")


@dp.message(Command("about"))
async def cmd_about(message: Message):
    about_text = (
        "ℹ️ <b>О боте</b>\n\n"
        "Это учебный Telegram-бот, написанный на <b>aiogram 3.x</b>.\n"
        "Демонстрирует базовые возможности: команды, inline-кнопки, reply-клавиатуры."
    )
    await message.answer(about_text, parse_mode="HTML")


# === ОБРАБОТЧИКИ INLINE-КНОПОК (callback) ===

@dp.callback_query(F.data == "about")
async def callback_about(callback: CallbackQuery):
    await callback.message.answer(
        "ℹ️ Это учебный бот на aiogram 3.x. Демонстрирует работу с кнопками и меню."
    )
    await callback.answer()  # убирает "часики" на кнопке


@dp.callback_query(F.data == "help")
async def callback_help(callback: CallbackQuery):
    await callback.message.answer(
        "❓ Используй команды /start, /help, /about или кнопки внизу экрана."
    )
    await callback.answer()


@dp.callback_query(F.data == "contact")
async def callback_contact(callback: CallbackQuery):
    await callback.message.answer(
        "📞 Связаться с разработчиком: @JupiterDuGuard"
    )
    await callback.answer()


@dp.callback_query(F.data == "close")
async def callback_close(callback: CallbackQuery):
    await callback.message.delete()  # удаляет сообщение с кнопками
    await callback.answer("Меню закрыто")


# === ОБРАБОТЧИКИ REPLY-КНОПОК (нижнее меню) ===

@dp.message(F.text == "📋 Меню")
async def reply_menu(message: Message):
    await message.answer(
        text="Выбери действие:",
        reply_markup=get_start_inline_keyboard(),
    )


@dp.message(F.text == "❓ Помощь")
async def reply_help(message: Message):
    await cmd_help(message)


@dp.message(F.text == "📞 Контакты")
async def reply_contact(message: Message):
    await message.answer("📞 Связаться с разработчиком: @JupiterDuGuard")


# === ЭХО НА ОСТАЛЬНЫЕ ТЕКСТОВЫЕ СООБЩЕНИЯ ===

@dp.message(F.text)
async def echo_message(message: Message):
    await message.answer(f"Я получил твоё сообщение: {message.text}")


# === ЗАПУСК БОТА ===

async def main():
    print("Бот запускается...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())