import asyncio
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types

from handlers import router

async def main():
    load_dotenv()
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher()

    dp.include_router(router)
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')