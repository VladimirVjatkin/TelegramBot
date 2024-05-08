import sys

import requests

def weather_all(location):
    # находим координаты города, широта и долгота
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid=7f4fb60ff1903e56283e7944c8b39b98'
    response = requests.get(url)
    print(response)  # печатаем ответ для контроля

    # API возвращает список результатов, поэтому нужно выбрать первый элемент списка
    # Также проверяем, что список не пустой
    if response.status_code == 200 and response.json():
        location_data = response.json()[0]
        lon = location_data['lon']
        lat = location_data['lat']
        print(lon, lat)  # печатаем координаты для контроля

        # вставляем координаты в URL запроса погоды
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid=7f4fb60ff1903e56283e7944c8b39b98'
        response = requests.get(url)
        print(response)  # печатаем ответ для контроля

        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            wind = data['wind']['speed']

            print(temp, humidity, pressure, wind)  # печатаем данные
            return temp, humidity, pressure, wind
        else:
            print("Ошибка при получении данных о погоде")
            return None
    else:
        print("Ошибка при получении данных о местоположении")
        return None


if __name__ == '__main__':
    print(weather_all('Prag'))  # Используйте кавычки вокруг названия города
 #   1 гПа = 0.7500637554192 мм рт.ст.


    #    url = 'https://randomfox.ca/floof/'
    #    response = requests.get(url)
    #    if response.status_code:
    #        data = response.json()
    #        image = data.get('image')
    #        return image
