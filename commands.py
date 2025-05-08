from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def command_start(message: types.Message):
    await message.answer("Web App loyihaga xush kelibsiz!")