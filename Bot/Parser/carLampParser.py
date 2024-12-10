from Bot.Controller.excelExporter import ExcelExporter
from Bot.Model.car_lamp import CarLamp
from Bot.Parser.parser import Parser


class CarLampParser(Parser):


    base_urs_site = "https://carlamp.com.ua/products/svetodiodnye-lampy?page="

    lamps = []

    def get_all_lamp(self, base_url_site):
        try:
            for page in range(0, 10):
                soup = self.get_soup(self.pages_iterator(page + 1, base_url=base_url_site))
                titles_name_phone = (soup.find(class_="products-list main-list col-md-12")
                                     .find_all(class_="col-xs-12 col-sm-4 col-md-3 col-lg-2"))

                for title in titles_name_phone:
                    product_name = title.find(class_="product-description")
                    price = title.find(class_="price")
                    image = title.find(class_="product-photo").find("img").get("src")

                    lamp = CarLamp(
                        name=product_name.text.strip() if product_name else None,
                        price=price.text.strip() if price else 0,
                        image=image if image else None

                    )
                    print(lamp)

                    self.lamps.append(lamp)

            return self.lamps
        except Exception as ex:
            return self.lamps


if __name__ == '__main__':
    car_lamp = CarLampParser()

    excel = ExcelExporter("carLamp.xlsx")
    excel.export(car_lamp.get_all_lamp(car_lamp.base_urs_site))