import requests
from bs4 import BeautifulSoup

class SiteParser:
    URLS = {
        'orki': 'https://index.minfin.com.ua/russian-invading/casualties/',
        'alarm': 'https://map.ukrainealarm.com/',
        'estore': 'https://estore.ua/iphone-15-128gb-green/'
    }

    def __get_response(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except requests.RequestException as ex:
            raise RuntimeError(f"Ошибка при запросе к {url}: {ex}")

    def __get_soup(self, url):
        response = self.__get_response(url)
        return BeautifulSoup(response.text, 'html.parser')

    def get_orki(self):
        try:
            soup = self.__get_soup(self.URLS['orki'])
            titles = soup.find(class_='casualties').find_all('li')
            return "\n".join(element.get_text() for element in titles)
        except Exception as ex:
            return f"О{ex}"

    def get_price_iphone15(self):
        try:
            soup = self.__get_soup(self.URLS['estore'])
            product_name = soup.find(class_='product-name').find('h1').text.strip()
            price = soup.find(class_='special-price').text.strip()
            return f"{product_name}: {price}"
        except Exception as ex:
            return f"{ex}"
