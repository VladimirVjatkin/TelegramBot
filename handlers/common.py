from aiogram import Router, types, F
from aiogram.filters.command import Command
import logging
import random
from keyboards.keyboards import keyboard
from utils.random_fox import fox
from utils.weather import weather_all

router = Router()

@router.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup=keyboard)


@router.message(Command(commands=['стоп']))
@router.message(Command(commands=['stop']))
async def stop(message: types.Message):
    print(message.from_user.full_name)
    await message.answer(f'Пока! Стоп машина!, {message.chat.first_name}!')


@router.message(Command(commands=['инфо', 'info']))
@router.message(F.text.lower() == 'инфо')
async def info(message: types.Message):
    number = random.randint(0, 100)
    await message.answer(f'Я знаю, что твоё любимое число число: {number}!!!')


@router.message(F.text.lower() == 'покажи лису')
async def info(message: types.Message):
    img_fox = fox()
    await message.answer('Привет, лови свою красавицу лису!!')
    await message.answer_photo(img_fox)
    # img_fox = fox()
    # await bot.send_photo(message.from_user.id, img_fox)


@router.message(F.text.lower() == 'погода в праге')
async def info(message: types.Message):
    weath = weather_all('Prague')
    await message.answer(f'С помощью API запрашиваем погоду на сервере openweathermap.org')
    await message.answer(f'И Вот вам погода в Праге в настоящий момен:')
    await message.answer(f"Температура: {weath[0]}С, Влажность: {weath[1]}%, Давление: {weath[2]}ГПа., Скорость ветра: {weath[3]}м/с")

#@router.message(F.text.lower() == 'погода')
#async def ask_for_city(message: types.Message):
#        await message.answer("Пожалуйста, введите название города:")

#@router.message()
#async def get_weather(message: types.Message):
#    city = message.text  # Получаем название города из сообщения пользователя
#    weath = weather_all(city)
#    await message.answer(f'С помощью API запрашиваем погоду на сервере openweathermap.org')
#    await message.answer(f'И Вот вам погода в {city} в настоящий момент:')
#    await message.answer(f"Температура: {weath[0]}С, Влажность: {weath[1]}%, Давление: {weath[2]}ГПа., Скорость ветра: {weath[3]}м/с")

