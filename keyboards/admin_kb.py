from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("/load_pizza")
b2 = KeyboardButton("/delete_pizza")

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(b1)\
    .add(b2)
    