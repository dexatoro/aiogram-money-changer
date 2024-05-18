import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Dispatcher, Bot
from handlers import router


dp = Dispatcher()


async def main() -> None:
    load_dotenv()
    bot = Bot(os.getenv('TOKEN'))
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            print('Exit')