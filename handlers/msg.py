import asyncio

from aiogram import Router, types, F

router = Router()

@router.message(F.text)
async def msg(message: types.Message):
    if 'привет' in message.text.lower():
        await message.reply('И тебе привет!')
    elif 'как дела' in message.text.lower():
        await message.reply('Нормально, а у тебя?')
    else:
        await message.reply('Не понимаю тебя друг...')
#@router.message(F.text)
#async def msg2(message: types.Message):  # Переименование функции для уникальности
#    if 'хорошо' in message.text.lower() or 'пойдет' in message.text.lower() or 'нормально' in message.text.lower():
#        await message.reply('Тогда прекрасно, надо радоваться пока еще чем-то нас мир не порадовал :))')
#    else:
#        await message.reply('все наладится, все будет хорошо, кому-то точно :))')