import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import user_handlers

from apscheduler.schedulers.asyncio import AsyncIOScheduler


logger = logging.getLogger(__name__)


async def main():
    
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s')
    
    logger.info('Starting bot')

    config: Config = load_config()

    bot: Bot = Bot(token=config.tg_bot.token, 
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    scheduler = AsyncIOScheduler()
    scheduler.add_job(user_handlers.send_message_temp, "interval", seconds=5,
                       kwargs={'bot': bot})

    dp.include_router(user_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    scheduler.start()
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot stopped!')
