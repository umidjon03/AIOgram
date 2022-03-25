from aiogram import types, Dispatcher
from bot_create import dp, bot
from database.sqlite_db import sql_read
from keyboards import kb_customer #from keyboards import kb_customer
from aiogram.types import ReplyKeyboardRemove

# @dp.message_handler(commands=['start'])
async def starting(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, f"Wellcome to our group", reply_markup=kb_customer)
        await message.delete()
    except:
        await message.reply('Welcome, for more satisfaction register our bot:\nhttp://t.me/kayfpizza_bot')


async def worktime(message: types.Message):
    await bot.send_message(message.from_user.id, 'from 9 am untill 11pm', reply_markup=kb_customer)


async def address(message: types.Message):
    await bot.send_message(message.from_user.id, 'Almazar, St. niyazova-1', reply_markup=ReplyKeyboardRemove())


async def menu(message: types.Message):
    await sql_read(message)

def register_customer_handler(dp : Dispatcher):
    dp.register_message_handler(starting, commands=['start'])
    dp.register_message_handler(address, commands=['address'])
    dp.register_message_handler(worktime, commands=['working_time'])
    dp.register_message_handler(menu, commands='menu')