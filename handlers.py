from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

gif = "https://media.tenor.com/MIpPcIjKsnwAAAAj/derpy-hooves.gif"
gif2 = "https://media1.tenor.com/m/mdIaMTCiCmcAAAAC/twilight-sparkle-twilight.gif"

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Любовный Peachy Peach?")
    
@router.message(lambda msg: msg.text.lower() == "да")

async def answer(message: Message):
    await message.answer_animation(animation="https://media.tenor.com/MIpPcIjKsnwAAAAj/derpy-hooves.gif")
    
    

@router.message()
    
async def answer(message: Message):
     
    await message.answer_animation(
        caption='''Так и думал.
        \n''',
        animation="https://media1.tenor.com/m/mdIaMTCiCmcAAAAC/twilight-sparkle-twilight.gif",
        caption2=""
        )
    
    



