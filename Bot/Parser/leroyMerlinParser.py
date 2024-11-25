import requests
from bs4 import BeautifulSoup

from Bot.Model import posudomy_mashyny
from Bot.Controller import excel_table_creator


class LeroyMerlin:

    url = f"https://www.leroymerlin.ua/ru/f/Posudomyini_mashyny.63cff165-29a2-4809-baa7-133be11faf9c"
    mashinys = []

    def __init__(self, url):
        self.url = url
        self.headers = {
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

    def __get_soup(self, url):
        response = self.__get_response(url)
        return BeautifulSoup(response.text, 'html.parser')


    def posudomyini_mashyny(self, ):
        soup = self.__get_soup(self.url)
        titles_mashyny = (soup.find(class_="css-6bmu7g")
                                 .find_all(class_="filter-card-observed css-1mrevk8"))

        for title in titles_mashyny:
            product_name = title.find(class_="css-1dve49f")
            price = title.find(class_="ListItemPriceBlock_price__RN3hw")
            in_stock = title.find(class_="css-16i62r0")

            mashyny = posudomy_mashyny.PosudomyiniMashyny(
                product_name = product_name.text.strip() if product_name else None,
                price = price.text.strip() if price else "Нет в наличии",
                in_stock = in_stock.text.strip() if in_stock else "Нет в наличии"
            )

            self.mashinys.append(mashyny)
        for item in self.mashinys:
            print(item.__repr__())

        return self.mashinys


if __name__ == '__main__':
    parser = LeroyMerlin(url=LeroyMerlin.url)
    excel_table =  excel_table_creator.ExcelTableCreator("LeroyMerlin")
    excel_table.write_to_excel_merlin(parser.posudomyini_mashyny())
    parser.posudomyini_mashyny()



