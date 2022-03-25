#from _typeshed import FileDescriptor, FileDescriptorLike
from logging import StrFormatStyle
from os import fdopen, fsdecode
from aiogram import dispatcher, types, Dispatcher
from aiogram.types.message import Message
from bot_create import dp
import string, json
from database import sqlite_db
from aiogram.dispatcher.filters import Text


# @dp.message_handler()
async def echo(message: types.message):
   # maketrans(x, y, z) x bu stringdagi almashtirmoqchi bo'lgan beli
   # y bu shu x ni o'rniga qaysi belgi qoyish
   # z esa ariginal stringdan qaysi belgini butunlay o'chirish
   # from string   ~~~string.punctuation bu belgilarni anglatadi: ex: !@#$%^&*
   if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
       .intersection(set(json.load(open('mat.json')))) != set():
       await message.reply('SENZURA!')
       await message.delete()


async def menu(message: types.Message):
    sqlite_db.sql_read()


def register_general_handler(dp: Dispatcher):
    dp.register_message_handler(echo)
    dp.register_message_handler(menu, commands='menu')
    dp.register_message_handler(menu, Text('menu', ignore_case=True))