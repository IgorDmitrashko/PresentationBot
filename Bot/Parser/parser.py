import requests
from bs4 import BeautifulSoup


class Parser:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        "Accept-Language": "uk-UA,uk;q=0.9",
        "Referer": "https://example.com"
    }

    def __get_response(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response
        except requests.RequestException as ex:
            raise RuntimeError(f"Ошибка при запросе к {url}: {ex}")

    def get_soup(self, url, response = ""):
        response = self.__get_response(url)
        return BeautifulSoup(response.text, 'html.parser')

    def pages_iterator(self, page:int, base_url):
        self.page_num = page
        base_url += f'{page}'
        return base_url