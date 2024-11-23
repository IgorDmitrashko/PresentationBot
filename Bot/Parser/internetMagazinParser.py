
import requests
from bs4 import BeautifulSoup
from Bot.Model import config, modelSiteParser
from Bot.Model.modelSiteParser import ModelSiteParser
from Bot.Parser import siteParser
from Bot.Model.smartphone import Smartphone

class InternetMagazinParser:

    base_url_eStore = f"https://estore.ua/smartfony/page="
    base_url_yabko = f"https://jabko.ua/kropyvnytskyi/gadzheti-i-drugoe/smartfoni?page="
    smartphones = []


    def __init__(self):
        None

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

    def __pages_iterator(self, page:int, base_url ):
        self.page_num = page
        base_url += f'{page}/'
        return base_url


    def get_all_smartphone(self, base_url_site, model_sit_parser: ModelSiteParser):
        for page in range(0,20):
            soup = self.__get_soup(self.__pages_iterator(page+1,base_url=base_url_site))
            titles_name_phone = (soup.find(class_=model_sit_parser.catalog)
                                 .find_all(class_=model_sit_parser.item))

            for title in titles_name_phone:
                product_name = title.find(class_=model_sit_parser.product_name)
                special_price = title.find(class_=model_sit_parser.special_price)
                old_price = title.find(class_=model_sit_parser.old_price)

                smart = Smartphone(
                    name=product_name.text.strip() if product_name else None,
                    new_price=special_price.text.strip() if special_price else None,
                    old_price=old_price.text.strip() if old_price else None
                )

                self.smartphones.append(smart)
        return self.smartphones



if __name__ == '__main__':
    parser = InternetMagazinParser()
    modelsite_yabko = ModelSiteParser(catalog = config.classes_yabko['catalog'],
                                      item=config.classes_yabko['item'],
                                      product_name=config.classes_yabko['product_name'],
                                      special_price=config.classes_yabko['special_price'],
                                      old_price=config.classes_yabko['old_price'])

    modelsite_eStore = ModelSiteParser(catalog=config.classes_eStore['catalog'],
                                      item=config.classes_eStore['item'],
                                      product_name=config.classes_eStore['product_name'],
                                      special_price=config.classes_eStore['special_price'],
                                      old_price=config.classes_eStore['old_price'])

    parser.get_all_smartphone(base_url_site=parser.base_url_eStore, model_sit_parser=modelsite_eStore)