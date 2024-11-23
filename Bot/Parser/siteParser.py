import requests
import asyncio
import aiohttp
import re


from Bot.Model import film, videocard
from Bot.Controller import excel_table_creator

from bs4 import BeautifulSoup


class SiteParser:
    page_num = 1
    URLS = {
        'orki': 'https://index.minfin.com.ua/russian-invading/casualties/',
        'alarm': 'https://map.ukrainealarm.com/',
        'estore': 'https://estore.ua/iphone-15-128gb-green/',
        'films': 'https://ru.wikipedia.org/wiki/250_%D0%BB%D1%83%D1%87%D1%88%D0%B8%D1%85_%D1%84%D0%B8%D0%BB%D1%8C%D0%BC%D0%BE%D0%B2_%D0%BF%D0%BE_%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%B8_IMDb',
        'razetka': f'https://hard.rozetka.com.ua/videocards/c80087/page={page_num}/'
    }
    videocards = []

    flag = True
    url_eStore_base = f"https://estore.ua/smartfony/manufacturer:apple/page={page_num}"

    def __init__(self):
        #self.base_url = "https://estore.ua/smartfony/manufacturer:apple/page={}"
        #self.get_videocards()

        filename = "video_cards_info.xlsx"
        excel_creator = excel_table_creator.ExcelTableCreator(filename)

        # Получаем список видеокарт



    def __pages_iterator(self, page:int):
        self.page_num = page
        self.URLS['razetka'] = f'https://hard.rozetka.com.ua/videocards/c80087/page={page}/'
        return self.URLS['razetka']


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
            for element in titles:
                print(element.get_text())
            return "\n".join(element.get_text() for element in titles)
        except Exception as ex:
            return f"О{ex}"

    def get_videocards(self):
        for page in range(0, 1):
            soup = self.__get_soup(self.__pages_iterator(page+1))
            print(page+1)
            titles = soup.find(class_='catalog-grid ng-star-inserted').find_all('li')

            result_string = ""

            pattern = re.compile(
                r"(?P<id>\d+)\s+Відеокарта\s+(?P<name>.+?)\s+(?P<memory>\d+GB)\s+GDDR(?P<memory_type>\d+)\s+\(\d+bit\)\s+\((?P<core>\d+)/(?P<frequency>\d+)\)\s+.*\s+(?P<price>[\d\s\u00A0]+₴)"
            )
            print(len(titles))
            for title in titles:
                data_text = title.get_text()
                data_text = data_text.replace('\u00A0', '')

                match = pattern.search(data_text)
                if match:
                    print(title)
                    id = match.group(1)
                    name = match.group(2)
                    memory = match.group(3)
                    memory_type = f"GDDR{match.group(4)}"
                    core = match.group(5)
                    frequency = match.group(6)
                    price = match.group(7)

                    videocar = videocard.Videocard(id=id, name=name, price=price, memory=memory, core=core,
                                                   frequency=frequency,
                                                   memory_type=memory_type)
                    self.videocards.append(videocar)
                    result_string += f"\n{videocar.__str__()}\n"
        return self.videocards

    def get_top_films(self):
        try:
            headers = {'User-Agent': 'YourAppName/1.0 (idmitrashko@ukr.net)'}
            response = requests.get(self.URLS['films'], headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            titles = soup.find_all('tr')
            result_string = ""
            for element in titles[1:21]:
                parts = element.get_text().split("\n")
                if len(parts) >= 5:
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
            name_tag = item.find("div", class_="product-name")
            if name_tag and name_tag.find("a"):
                product["name"] = name_tag.find("a").text.strip()
                product["url"] = name_tag.find("a")["href"]

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

