import scrapy
import html
from scrapy.crawler import CrawlerProcess


class ProductSpider(scrapy.Spider):
    name = 'product_spider'
    start_urls = ['https://allo.ua/ua/products/mobile/klass-kommunikator_smartfon/p-1/']
    all_product = []

    def parse(self, response):
        self.logger.info(f"Обрабатываем страницу: {response.url}")


        products = response.css('.products-layout__container.products-layout--grid .products-layout__item .product-card')
        if not products:
            self.logger.warning("Не найдено продуктов на странице!")

        for product in products:
            product_name = product.css('.product-card__title::text').get().strip()

            old_price = product.css('.sum::text').get()

            old_price = old_price.strip() if old_price else 'Цена не указана'


            new_price = product.css('.v-pb__cur.discount .sum::text').get()

            if new_price:
                new_price = new_price.replace('\xa0', '').strip()
            else:
                new_price = None

            self.logger.info(f"Товар: {product_name}, старая цена: {old_price}, новая цена: {new_price}")


            yield {
                'name': product_name,
                'old_price': old_price,
                'new_price': new_price
            }

        next_page = response.css('.pagination__next__link.pagination__links::attr(href)').get()
        if next_page:
            self.logger.info(f"Переход к следующей странице: {next_page}")
            yield response.follow(next_page, callback=self.parse)
        else:
            self.logger.info("Следующая страница не найдена или достигнут конец списка.")

if __name__ == "__main__":
    process = CrawlerProcess(settings={
        "FEEDS": {
            "output.json": {"format": "json"},
        },
    })
    process.crawl(ProductSpider)
    process.start()