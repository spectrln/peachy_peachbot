from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Вы зачем-то до сих пор заходите. Вы Peachy Peach?')
    
@router.message(lambda msg: msg.text.lower() == "да")
async def answer(message: Message):
    await message.answer("Удачи в новой жизни.\nhttps://www.youtube.com/watch?v=PEK3BgK5Zyo")
    
    
@router.message()
async def answer(message: Message):
    await message.answer('''
Я любил Peachy Peach.
\nЗнал, что ей было со мной очень сложно жить.
\nЯ был очень рад, что она все это время держалась.
\nПрощайте, Peachy Peach.
\nЯ помню, как вы согревали меня в самый холодный ветер зимой.
\nhttps://www.youtube.com/watch?v=oh0RQ_TgDnQ''')
    



