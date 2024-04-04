import asyncio
import logging
from aiogram import Dispatcher, Bot
from handlers import router
from config import token

dp = Dispatcher()


async def main() -> None:
    bot = Bot(token)
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            print('Exit')