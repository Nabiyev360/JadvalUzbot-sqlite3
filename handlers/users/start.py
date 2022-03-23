from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db
from keyboards.default.mainKeyboard import main_keyboard

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}😊. \nDars jadvalini ko'rish uchun hafta kunini tanlang!💁‍♂️", reply_markup = main_keyboard)
    db.add_user(message.chat.id, message.from_user.full_name, message.from_user.username)