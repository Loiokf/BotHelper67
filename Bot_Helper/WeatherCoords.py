from config import open_weather_token
import datetime
import requests


class GetWeatherCoords:
    def __init__(self, coords):
        self.coords = coords
        self.result = []
        self.lat = self.coords[0:9]
        self.lon = self.coords[11:20]

    def __call__(self) -> list:
        code_to_smile = {
            "Clear": "Ясно \U00002600",
            "Clouds": "Облачно \U00002601",
            "Rain": "Дождь \U00002614",
            "Drizzle": "Дождь \U00002614",
            "Thunderstorm": "Гроза \U000026A1",
            "Snow": "Снег \U0001F328",
            "Mist": "Туман \U0001F32B"
        }
        try:
            r = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={open_weather_token}&units=metric")
            data = r.json()
            city = data["name"]
            cur_weather = data["main"]["temp"]
            weather_description = data["weather"][0]["main"]
            if weather_description in code_to_smile:
                wd = code_to_smile[weather_description]
            else:
                wd = "Не могу определить погоду."

            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            wind = data["wind"]["speed"]
            clouds = data["weather"][0]["description"]
            wind_deg = data["wind"]["deg"]
            visibility = data["visibility"]

            sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
            sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

            length_of_the_day = datetime.datetime.fromtimestamp(
                data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
                data["sys"]["sunrise"])
            self.result.append(f"==={datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}===\n"
                               f"Погода по координатам: {self.lat}, {self.lon}\n"
                               f"Температура: {cur_weather}C {wd}\n"
                               f"Влажность: {humidity}%\n"
                               f"Давление: {pressure} мм.рт.ст\n"
                               f"Ветер: {wind} м/с\n"
                               f"Направление ветра: {wind_deg}°\n"
                               f"Облачность: {clouds}\n"
                                f"\n"
                               f"Менее значимые параметры:\n"
                               f"\n"
                               f"Средняя видимость: {visibility}\n"
                               f"Восход солнца: {sunrise_timestamp}\n"
                               f"Закат солнца: {sunset_timestamp}\n"
                               f"Продолжительность светового дня: {length_of_the_day}")
            return self.result
        except BaseException:
            return [f'''Пожалуйста, проверьте корректность введеных координат. Вы ввели - {self.lat}, {self.lon}. Введите координаты заново, снова нажав на кнопку "Погода по координатам"''']
