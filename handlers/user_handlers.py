from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

from utilities.sensor import sensor_temp, triger_temp
from config_data.config import load_config


router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=sensor_temp())



async def send_message_temp(bot: Bot):
    if triger_temp():
        await bot.send_message(text=sensor_temp(), chat_id=load_config().user_id.id)