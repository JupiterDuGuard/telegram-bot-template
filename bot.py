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

from texts import LANGUAGES, get_text

# Загружаем переменные из .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Логирование
logging.basicConfig(level=logging.INFO)

# Бот и диспетчер
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Хранилище языков пользователей (в памяти)
# Ключ — user_id, значение — код языка ("ru", "en", "pl", "de")
# При перезапуске бота данные стираются — это нормально для учебного проекта
user_languages: dict[int, str] = {}


# === ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ===

def get_user_lang(user_id: int) -> str | None:
    """Возвращает язык пользователя или None, если ещё не выбран."""
    return user_languages.get(user_id)


def set_user_lang(user_id: int, lang: str) -> None:
    """Сохраняет выбранный язык пользователя."""
    user_languages[user_id] = lang


# === КЛАВИАТУРЫ ===

def get_language_keyboard() -> InlineKeyboardMarkup:
    """Inline-клавиатура для выбора языка."""
    buttons = []
    # Создаём по одной кнопке на язык, по 2 кнопки в ряд
    row = []
    for code, name in LANGUAGES.items():
        row.append(InlineKeyboardButton(text=name, callback_data=f"setlang_{code}"))
        if len(row) == 2:
            buttons.append(row)
            row = []
    # Если в последнем ряду осталась одна кнопка — добавляем
    if row:
        buttons.append(row)

    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_main_inline_keyboard(lang: str) -> InlineKeyboardMarkup:
    """Главная inline-клавиатура с переводом."""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=get_text(lang, "btn_catalog"), callback_data="catalog"),
                InlineKeyboardButton(text=get_text(lang, "btn_about"), callback_data="about"),
            ],
            [
                InlineKeyboardButton(text=get_text(lang, "btn_contact"), callback_data="contact"),
            ],
            [
                InlineKeyboardButton(text=get_text(lang, "btn_change_lang"), callback_data="change_lang"),
            ],
        ]
    )
    return keyboard


def get_main_reply_keyboard(lang: str) -> ReplyKeyboardMarkup:
    """Главное reply-меню снизу с переводом."""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=get_text(lang, "menu_catalog")),
                KeyboardButton(text=get_text(lang, "menu_help")),
            ],
            [
                KeyboardButton(text=get_text(lang, "menu_contact")),
            ],
        ],
        resize_keyboard=True,
    )
    return keyboard


# === КОМАНДЫ ===

@dp.message(CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id
    lang = get_user_lang(user_id)

    if lang is None:
        # Первый запуск — предлагаем выбрать язык
        await message.answer(
            text=get_text("en", "choose_language"),  # многоязычное приветствие
            reply_markup=get_language_keyboard(),
        )
    else:
        # Язык уже выбран — показываем главное меню
        await show_main_menu(message, lang)


@dp.message(Command("lang"))
async def cmd_lang(message: Message):
    """Принудительная смена языка."""
    await message.answer(
        text=get_text("en", "choose_language"),
        reply_markup=get_language_keyboard(),
    )


@dp.message(Command("help"))
async def cmd_help(message: Message):
    lang = get_user_lang(message.from_user.id) or "en"
    await message.answer(get_text(lang, "help_text"), parse_mode="HTML")


# === ПОКАЗ ГЛАВНОГО МЕНЮ ===

async def show_main_menu(message: Message, lang: str):
    """Отправляет приветствие + inline-меню + reply-клавиатуру."""
    await message.answer(
        text=get_text(lang, "welcome"),
        reply_markup=get_main_inline_keyboard(lang),
    )
    # Reply-клавиатура отправляется отдельным служебным сообщением
    await message.answer(
        text="⬇️",
        reply_markup=get_main_reply_keyboard(lang),
    )


# === ВЫБОР ЯЗЫКА (callback) ===

@dp.callback_query(F.data.startswith("setlang_"))
async def callback_set_language(callback: CallbackQuery):
    # Извлекаем код языка из callback_data вида "setlang_ru"
    lang = callback.data.replace("setlang_", "")

    # Сохраняем язык
    set_user_lang(callback.from_user.id, lang)

    # Подтверждение
    await callback.message.answer(get_text(lang, "language_set"))

    # Показываем главное меню на новом языке
    await show_main_menu(callback.message, lang)

    # Убираем "часики" с inline-кнопки
    await callback.answer()


@dp.callback_query(F.data == "change_lang")
async def callback_change_lang(callback: CallbackQuery):
    """Смена языка через кнопку."""
    await callback.message.answer(
        text=get_text("en", "choose_language"),
        reply_markup=get_language_keyboard(),
    )
    await callback.answer()


# === КНОПКИ INLINE-МЕНЮ ===

@dp.callback_query(F.data == "catalog")
async def callback_catalog(callback: CallbackQuery):
    lang = get_user_lang(callback.from_user.id) or "en"
    await callback.message.answer(get_text(lang, "catalog_text"), parse_mode="HTML")
    await callback.answer()


@dp.callback_query(F.data == "about")
async def callback_about(callback: CallbackQuery):
    lang = get_user_lang(callback.from_user.id) or "en"
    await callback.message.answer(get_text(lang, "about_text"), parse_mode="HTML")
    await callback.answer()


@dp.callback_query(F.data == "contact")
async def callback_contact(callback: CallbackQuery):
    lang = get_user_lang(callback.from_user.id) or "en"
    await callback.message.answer(get_text(lang, "contact_text"), parse_mode="HTML")
    await callback.answer()


# === REPLY-КНОПКИ (нижнее меню) ===
# Сложность: текст кнопок зависит от языка пользователя.
# Поэтому фильтруем по списку всех возможных переводов сразу.

def get_all_menu_texts(key: str) -> list[str]:
    """Возвращает варианты текста кнопки на всех языках."""
    return [get_text(lang, key) for lang in LANGUAGES.keys()]


@dp.message(F.text.in_(get_all_menu_texts("menu_catalog")))
async def reply_menu_catalog(message: Message):
    lang = get_user_lang(message.from_user.id) or "en"
    await message.answer(
        text=get_text(lang, "welcome"),
        reply_markup=get_main_inline_keyboard(lang),
    )


@dp.message(F.text.in_(get_all_menu_texts("menu_help")))
async def reply_menu_help(message: Message):
    lang = get_user_lang(message.from_user.id) or "en"
    await message.answer(get_text(lang, "help_text"), parse_mode="HTML")


@dp.message(F.text.in_(get_all_menu_texts("menu_contact")))
async def reply_menu_contact(message: Message):
    lang = get_user_lang(message.from_user.id) or "en"
    await message.answer(get_text(lang, "contact_text"), parse_mode="HTML")


# === ЭХО НА ПРОЧИЕ СООБЩЕНИЯ ===

@dp.message(F.text)
async def echo_message(message: Message):
    lang = get_user_lang(message.from_user.id) or "en"
    await message.answer(
        get_text(lang, "echo").format(text=message.text)
    )


# === ЗАПУСК ===

async def main():
    print("Бот запускается...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())