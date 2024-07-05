from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Вы Peachy Peach?')
    
@router.message(lambda msg: msg.text.lower() == "да")
async def answer(message: Message):
    await message.answer("Ураааааааааааа!")
    await message.answer_sticker("CAACAgEAAxkBAAEMb1pmh1FoyM8qJ3gJ1TAPxHqg6mOhMwAC6gIAAkzs4Ed1zNDPilb6bTUE")
    
@router.message()
async def answer(message: Message):
    await message.answer("Ну что же вы....")
    await message.answer_sticker("CAACAgEAAxkBAAEMb1Zmh0eOHvG9XDFNlNZPGtmGSh16gQACAQIAAjZZQURFqRmV5ZBj1zUE")



