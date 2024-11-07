import requests
import asyncio
import aiohttp

from Bot.Model import film
from bs4 import BeautifulSoup


class SiteParser:
    URLS = {
        'orki': 'https://index.minfin.com.ua/russian-invading/casualties/',
        'alarm': 'https://map.ukrainealarm.com/',
        'estore': 'https://estore.ua/iphone-15-128gb-green/',
        'films': 'https://ru.wikipedia.org/wiki/250_%D0%BB%D1%83%D1%87%D1%88%D0%B8%D1%85_%D1%84%D0%B8%D0%BB%D1%8C%D0%BC%D0%BE%D0%B2_%D0%BF%D0%BE_%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%B8_IMDb'
    }

    page_num = 1
    flag = True
    url_eStore_base = f"https://estore.ua/smartfony/manufacturer:apple/page={page_num}"

    def __init__(self):
        self.base_url = "https://estore.ua/smartfony/manufacturer:apple/page={}"
        #result = asyncio.run(self.get_all_pages())
        #print(result)

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

    def get_top_films(self):
        try:
            headers = {'User-Agent': 'YourAppName/1.0 (idmitrashko@ukr.net)'}
            response = requests.get(self.URLS['films'], headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            titles = soup.find_all('tr')
            result_string = ""
            for element in titles[1:21]:
                # Разделение данных на части
                parts = element.get_text().split("\n")  # Предполагаем, что каждый элемент разделён новой строкой
                if len(parts) >= 5:  # Если данных достаточно
                    films = film.Film(parts[1], parts[2], parts[3], parts[4], parts[5])
                    result_string += f"\n{films.__str__()}\n"
                else:
                    print("Недостаточно данных\n")

            return result_string
        except Exception as ex:
            return f"{ex}"




    def get_price_iphone15(self) -> str:
        try:
            soup = self.__get_soup(self.URLS['estore'])
            product_name = soup.find(class_='product-name').find('h1').text.strip()
            price = soup.find(class_='special-price').text.strip()
            return f"{product_name}: {price}"
        except Exception as ex:
            return f"{ex}"

    async def fetch_page(self, session, page):
        url = self.base_url.format(page)
        async with session.get(url) as response:
            return await response.text()

    async def get_all_pages(self) -> list:
        try:
            async with aiohttp.ClientSession() as session:
                tasks = []
                for page in range(1, 9):
                    if self.flag:
                        url = self.base_url.format(page)
                        print(page)
                        tasks.append(self.get_all_iphone_on_page(url))
                        # Здесь вызываем get_all_iphone_on_page
                        print(tasks[page-1])
                    else:
                        break
                page_list = await asyncio.gather(*tasks)
                return tasks
        except Exception as ex:
            return ex


    def get_all_iphone_on_page(self, url) ->[]:
        soup = self.__get_soup(url)
        items = soup.find_all("li", class_="item")
        product_list = []
        flag = True
        pattern = r'^\d+(?:\s*\d+)*\s*грн\.$'

        for item in items:
            product = {}
            # Название товара
            name_tag = item.find("div", class_="product-name")
            if name_tag and name_tag.find("a"):
                product["name"] = name_tag.find("a").text.strip()
                product["url"] = name_tag.find("a")["href"]

            # Цена товара
            price_tag = item.find("span", class_="price")
            not_nalichie = item.find("span", class_="actions clearer")

            if not price_tag and not not_nalichie:
                print("")
            else:
                product['price'] = price_tag.text.replace('\xa0', '').strip()
                product_list.append(product)
                print(product_list[0])

        return product_list

class Product:

    name = ''
    price = ''
    url = ''

