from aiogram import types

from loader import dp

import requests


@dp.message_handler(commands=['weather'])
async def get_weather(message: types.Message):
    await message.answer('Введите город:')
    name = message.text. split()
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={name}&appid=4321a3d417b53045aa1b6617c529c910&units=metric&lang=ru")
    weather = response.json()['weather'][0]['description']
    temp = response.json()['main']['temp']
    temp_feeling = response.json()['main']['feels_like']
    await message.answer(f'погода в городе {name}:\n {weather}, температура воздуха - {temp} ощушается как {temp_feeling}')












