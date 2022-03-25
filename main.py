from aiogram.utils import executor
from bot_create import dp
from database import sqlite_db
from handlers import customer, general, admin



async def on_startup(_ ):
    print('Bot is in online!')
    sqlite_db.sql_start()




admin.register_admin_handler(dp)
customer.register_customer_handler(dp)
general.register_general_handler(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)