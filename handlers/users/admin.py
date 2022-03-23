from aiogram import types
from asyncio import sleep

from data.config import ADMINS
from loader import dp


@dp.message_handler(chat_id= ADMINS, text= 'getdb')
async def send_data(message: types.Message):
    file = open('data/main.db', 'rb')
    await message.answer_document(file)
    file.close()


@dp.message_handler(chat_id= ADMINS)
async def send_message_users(message: types.Message):
    try:
        user_id = message.reply_to_message.forward_from.id
        await dp.bot.send_message(user_id, message.text)
        await message.answer("✅ Muvaffaqiyatli yuborildi")
    except Exception as ex:
        await message.reply(ex)
        await sleep(1)
        await message.reply('Foydalanuvchiga xabar yuborish uchun foydalanuvchidan kelgan xabarni tanlab oling💁‍♂️')
