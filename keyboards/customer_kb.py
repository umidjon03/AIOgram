from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


b1 = KeyboardButton('/working_time')
b2 = KeyboardButton('/address')
b3 = KeyboardButton('/menu',)
b4 = KeyboardButton('Send contact', request_contact=True)
b5 = KeyboardButton('Send location', request_location=True)

kb_customer = ReplyKeyboardMarkup(resize_keyboard=True) #argument sifatida one_time_keyboard=True deb olsa knopkalar bir marta ishlatiladi

kb_customer.add(b1).add(b2).add(b3).row(b4, b5)

#insert bu o'zidan oldingi knopkaga shu knopkani bir qatorda yozadi
# kb_customer.add(b1).add(b2).insert(b3)

#row oz ichidagi knopkalarni qo'shib yuboradi
# kb_customer.row(b1, b2, b3)