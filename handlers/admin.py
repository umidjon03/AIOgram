from os import read
import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from database import sqlite_db
from keyboards import button_case_admin
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ID= None
from bot_create import dp, bot

class Admin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


# @dp.message_handler(commands='moderator', is_chat_admin=True)
async def moderator(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(ID, 'Что хозяин надо???', reply_markup=button_case_admin)
    await message.delete()


# @dp.message_handler(commands=['load_pizza'], state=None)
async def start_load(message: types.Message):
    if ID == message.from_user.id:
        await Admin.photo.set()
        await message.reply('Send photo of the pizza')



async def cancel_fsm(message: types.Message, state: FSMContext):
    if ID == message.from_user.id:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('ok')




# @dp.message_handler(content_types=['photo'], state=Admin.photo)
async def set_photo(message: types.Message, state: FSMContext):
    if ID == message.from_user.id:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
    
        await Admin.next()
        await message.reply('Send name')


# @dp.message_handler(state= Admin.name)
async def set_name(message: types.Message, state: FSMContext):
    if ID == message.from_user.id:
        async with state.proxy() as data:
            data['name'] = message.text

        await Admin.next()
        await message.reply('send description')


# @dp.message_handler(state= Admin.description)
async def set_description(message: types.Message, state: FSMContext):
    if ID == message.from_user.id:
        async with state.proxy() as data:
            data['description'] = message.text

        await Admin.next()
        await message.reply('send price per unit')


# @dp.message_handler(state= Admin.name)
async def set_price(message: types.Message, state: FSMContext):
    if ID == message.from_user.id:
        async with state.proxy() as data:
            data['price'] = float(message.text)
        await sqlite_db.sql_add_command(state)
        await state.finish()



@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
    await bot.answer_callback_query(callback_query.id, text= f'{callback_query.data.replace("del ", "")} is deleted', show_alert=True)


@dp.message_handler(commands='delete_pizza')
async def delete_item(message: types.Message):
    if message.from_user.id == ID:
        read = await sqlite_db.sql_read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nDescription: {ret[2]}\nPrice: ${ret[3]}', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'delete {ret[1]}', callback_data= f'del {ret[1]}')))




def register_admin_handler(dp: Dispatcher):
    dp.register_message_handler(moderator, commands='moderator', is_chat_admin=True)
    dp.register_message_handler(cancel_fsm, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(cancel_fsm, state="*", commands=['cancel'])
    dp.register_message_handler(start_load, commands=['load_pizza'], state=None)
    dp.register_message_handler(set_photo, state=Admin.photo, content_types=['photo'])
    dp.register_message_handler(set_name, state=Admin.name)
    dp.register_message_handler(set_description, state=Admin.description)
    dp.register_message_handler(set_price, state=Admin.price)
    
    