from aiogram import types

from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.lang import lang_keys
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"HI, {message.from_user.full_name}!\nChoose your language",reply_markup=lang_keys())


