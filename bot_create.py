from aiogram import Bot
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import os

storage = MemoryStorage()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot, storage= storage)