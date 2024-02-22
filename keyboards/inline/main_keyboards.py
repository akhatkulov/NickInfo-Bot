from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

def uz_menu_keyboard():
    x = InlineKeyboardMarkup(row_width=3)
    btn1 = InlineKeyboardButton(text="Foydalanuvchi nomini tekshirish",callback_data="uz_name_search")
    btn2 = InlineKeyboardButton(text="FAQ",callback_data="uz_faq")
    btn3 = InlineKeyboardButton(text="Dasturlar",callback_data="uz_apps")
    x.add(btn1)
    x.add(btn2,btn3)
    return x

def ru_menu_keyboard():
    x = InlineKeyboardMarkup(row_width=3)
    btn1 = InlineKeyboardButton(text="Foydalanuvchi nomini tekshirish",callback_data="ru_name_search")
    btn2 = InlineKeyboardButton(text="FAQ",callback_data="ru_faq")
    btn3 = InlineKeyboardButton(text="Dasturlar",callback_data="ru_apps")
    x.add(btn1)
    x.add(btn2,btn3)
    return x

def en_menu_keyboard():
    x = InlineKeyboardMarkup(row_width=3)
    btn1 = InlineKeyboardButton(text="Foydalanuvchi nomini tekshirish",callback_data="en_name_search")
    btn2 = InlineKeyboardButton(text="FAQ",callback_data="en_faq")
    btn3 = InlineKeyboardButton(text="Dasturlar",callback_data="en_apps")
    x.add(btn1)
    x.add(btn2,btn3)
    return x