import requests
from Bot.Model import config

class JsonParser:
    def __init__(self, city='Kyiv'):
        self.city = city
        self.url_rate = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'
        self.url_weather = f'https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={config.WEATHER_TOKEN}&lang=ru&units=metric'
        self.url_nasa = f'https://api.nasa.gov/planetary/apod?api_key={config.API_KEY_NASA}'

    def _get_json(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as ex:
            return ex

    def get_rate(self):
        return self._get_json(self.url_rate)

    def get_weather(self):
        return self._get_json(self.url_weather)["main"]["temp"]

    def get_url_images_nasa(self):
        return self._get_json(self.url_nasa)['url']

