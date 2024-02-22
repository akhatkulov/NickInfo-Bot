from aiogram import types
from aiogram.types import CallbackQuery,Message
from aiogram.dispatcher import FSMContext

from loader import dp
from helper.username import nick_fast_checker

@dp.callback_query_handler(text="uz_name_search")
async def uz_search(call: CallbackQuery,state: FSMContext):
    await call.message.answer("Foydalanuvchi nomini yuboring")
    await call.answer(cache_time=60)

    await state.set_state("uz_search")

@dp.callback_query_handler(text="ru_name_search")
async def uz_search(call: CallbackQuery,state: FSMContext):
    await call.message.answer("Foydalanuvchi nomini yuboring")
    await call.answer(cache_time=60)

    await state.set_state("ru_search")

@dp.callback_query_handler(text="en_name_search")
async def uz_search(call: CallbackQuery,state: FSMContext):
    await call.message.answer("Foydalanuvchi nomini yuboring")
    await call.answer(cache_time=60)

    await state.set_state("en_search")

@dp.message_handler(state="uz_search")
async def uz_search_2(msg: types.Message,state: FSMContext):
    await msg.answer("Tekshrilmoqda...")

    await msg.answer(nick_fast_checker(msg.text),parse_mode="html")
    await state.finish()

@dp.message_handler(state="ru_search")
async def uz_search_2(msg: types.Message,state: FSMContext):
    await msg.answer("Tekshrilmoqda...")

    await msg.answer(nick_fast_checker(msg.text),parse_mode="HTML")
    await state.finish()   

@dp.message_handler(state="en_search")
async def uz_search_2(msg: types.Message,state: FSMContext):
    await msg.answer("Tekshrilmoqda...")

    await msg.answer(nick_fast_checker(msg.text),parse_mode="HTML")
    await state.finish()