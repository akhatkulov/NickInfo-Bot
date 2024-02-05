from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

def lang_keys():
    x = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    btn1 = KeyboardButton(text="Uzbek")
    btn2 = KeyboardButton(text="Russian")
    btn3 = KeyboardButton(text="English")
    x.add(btn1,btn2,btn3)
    return x