from aiogram import types
from aiogram.types import CallbackQuery, Message
from loader import dp

@dp.callback_query_handler(text="uz_apps")
async def uz_show_apps(call: CallbackQuery):
    await call.message.answer("Dastur haqida")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="ru_apps")
async def uz_show_apps(call: CallbackQuery):
    await call.message.answer("Dastur haqida")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="en_apps")
async def uz_show_apps(call: CallbackQuery):
    await call.message.answer("Dastur haqida")
    await call.answer(cache_time=60)