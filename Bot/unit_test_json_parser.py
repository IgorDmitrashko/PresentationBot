import unittest
from unittest.mock import patch

import requests
from jsonParser import JsonParser


class TestJsonParser(unittest.TestCase):

    def setUp(self):
        # Инициализация объекта JsonParser перед каждым тестом
        self.parser = JsonParser()

    @patch('your_module.requests.get')
    def test_get_rate_success(self, mock_get):
        # Имитация успешного ответа от API для курса валют
        mock_get.return_value.json.return_value = [{"ccy": "USD", "buy": "27.50"}, {"ccy": "EUR", "buy": "32.00"}]
        mock_get.return_value.status_code = 200

        result = self.parser.get_rate()

        # Проверка, что метод возвращает корректный результат
        self.assertEqual(result[0]["ccy"], "USD")
        self.assertEqual(result[0]["buy"], "27.50")

    @patch('your_module.requests.get')
    def test_get_rate_failure(self, mock_get):
        # Имитация сбоя запроса
        mock_get.side_effect = requests.RequestException("API is down")

        result = self.parser.get_rate()

        # Проверка, что метод возвращает объект исключения
        self.assertIsInstance(result, requests.RequestException)

    @patch('your_module.requests.get')
    def test_get_weather_success(self, mock_get):
        # Имитация успешного ответа от API для погоды
        mock_get.return_value.json.return_value = {"main": {"temp": 20}}
        mock_get.return_value.status_code = 200

        result = self.parser.get_weather()

        # Проверка, что метод возвращает правильную температуру
        self.assertEqual(result, 20)

    @patch('your_module.requests.get')
    def test_get_weather_failure(self, mock_get):
        # Имитация сбоя запроса
        mock_get.side_effect = requests.RequestException("API is down")

        result = self.parser.get_weather()

        # Проверка, что метод возвращает объект исключения
        self.assertIsInstance(result, requests.RequestException)

    @patch('your_module.requests.get')
    def test_get_url_images_nasa_success(self, mock_get):
        # Имитация успешного ответа от API NASA
        mock_get.return_value.json.return_value = {"url": "https://example.com/nasa_image.jpg"}
        mock_get.return_value.status_code = 200

        result = self.parser.get_url_images_nasa()

        # Проверка, что метод возвращает правильный URL изображения
        self.assertEqual(result, "https://example.com/nasa_image.jpg")

    @patch('your_module.requests.get')
    def test_get_url_images_nasa_failure(self, mock_get):
        # Имитация сбоя запроса
        mock_get.side_effect = requests.RequestException("API is down")

        result = self.parser.get_url_images_nasa()

        # Проверка, что метод возвращает объект исключения
        self.assertIsInstance(result, requests.RequestException)


if __name__ == '__main__':
    unittest.main()
