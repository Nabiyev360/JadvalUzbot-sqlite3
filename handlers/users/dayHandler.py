from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, db
from keyboards.inline.addDarsInline import add_dars_inline
from keyboards.inline.editDarsInline import days_inline
from states.newSience import NewSience
from data.config import ADMINS


days_list = ["1️⃣ Dushanba", "2️⃣ Seshanba", "3️⃣ Chorshanba", "4️⃣ Payshanba", "5️⃣ Juma", "6️⃣ Shanba"]

@dp.message_handler(state=NewSience.sience_name)
async def new_siense(message: types.Message, state: FSMContext):
    data = await state.get_data()
    day_name = data.get(f"day_name{message.chat.id}").lower()
    chat_id= message.chat.id
    db.add_lessons(chat_id, day_name, message.text)
    
    await message.answer("Darslar ro'yxati muvaffaqiyatli qo'shildi✅", reply_markup = days_inline)
    await state.finish()            #state'dan chiqamiz ( & state datasi clear bo'ladi)
    await message.forward(ADMINS[0])

@dp.message_handler(text = '📝 Jadvalni o\'zgartirish')
async def edit_lesson(message: types.Message):
    await message.answer('Kiritmoqchi / O\'zgartirmochi bo\'lgan kuningizni tanlang', reply_markup=days_inline)

@dp.message_handler(text = '✍️ Izoh qoldirish')
async def send_lesson(message: types.Message):
    await message.answer('Bot haqida fikr, mulohaza va takliflaringiz bo\'lsa shu yergda yuboring💁‍♂')

@dp.message_handler(text= days_list)
async def send_dars(message: types.Message):
    day_name= message.text[4:].lower()
    chat_id= message.chat.id
    lessons= db.get_lessons(chat_id=chat_id, day_name=day_name)
    
    keyboard = None
    if lessons== None:
        lessons= f'{day_name.title()} kunlik dars jadvali kiritilmagan'
        keyboard= add_dars_inline
        
    await message.answer(lessons, reply_markup=keyboard)
    await message.forward(ADMINS[0])



@dp.message_handler(content_types=['photo', 'audio', 'video', 'document', 'voice', 'gif', 'sticker'])
async def for_others(message: types.Message):
    await message.forward(ADMINS[0])