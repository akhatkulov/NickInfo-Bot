from aiogram import types
from loader import dp 
from keyboards.inline import main_keyboards

@dp.message_handler(text="🇺🇿 Uzbek")
async def uz_menu(message : types.Message):
    await message.answer("Kerakli menyuni tanlang",reply_markup=main_keyboards.uz_menu_keyboard())

@dp.message_handler(text="🇷🇺 Russian")
async def uz_menu(message : types.Message):
    await message.answer("Kerakli menyuni tanlang",reply_markup=main_keyboards.ru_menu_keyboard())

@dp.message_handler(text="🇬🇧 English")
async def uz_menu(message : types.Message):
    await message.answer("Kerakli menyuni tanlang",reply_markup=main_keyboards.en_menu_keyboard())    
