from aiogram.types import Message, User, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup,CallbackQuery
from aiogram import Router, Dispatcher, Bot
from aiogram.filters.command import Command
from asyncio import run
from abc import ABC, abstractmethod
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from config import BOT_TOKEN

City = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text="Tashkent",callback_data="Toshkent"),
    ],
    [
        InlineKeyboardButton(text="Fergana",callback_data="Fergana"),
        InlineKeyboardButton(text="Andijon",callback_data="Andijan"),
        InlineKeyboardButton(text="Namangan",callback_data="Namangan"),
    ],
    [
        InlineKeyboardButton(text="Sirdaryo",callback_data="Sirdaryo"),
        InlineKeyboardButton(text="Jizzah",callback_data="Jizzakh"),
    ],
    [
        InlineKeyboardButton(text="Qashqadaryo",callback_data="Qashqadaryo"),
        InlineKeyboardButton(text="Surxondaryo",callback_data="Termiz"),
    ],
    [
        InlineKeyboardButton(text="Bukhara",callback_data="Bukhara"),
        InlineKeyboardButton(text="Xorazm",callback_data="Urganch"),
    ],
    [
        InlineKeyboardButton(text="Navoi",callback_data="Navoiy"),
        InlineKeyboardButton(text="Samarkand",callback_data="Samarqand"),
    ],
    ],
)



greet = Router()

@greet.message(Command(commands=["start"]))
async def greet_message(msg: Message, bot: Bot):
    await msg.answer("Bu ob-havo ma'lumoti boti⛅️",reply_markup=City)

@greet.callback_query()
async def greet_message(call: CallbackQuery):
    city = call.data
    weatherr = abs.get_date(city)
    await call.answer(f"{weatherr}°C")



async def start():
    dp = Dispatcher()
    bot = Bot(BOT_TOKEN)
    dp.include_router(greet)
    try:
        await dp.start_polling(bot)
    except:
        await bot.session.close()

if __name__ == "__main__":
    run(start())