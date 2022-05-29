from abc import ABCMeta

from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule

from ..items import BooksCrawlerItem


class BookSpider(CrawlSpider, metaclass=ABCMeta):
    name = 'book'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(allow=r'catalogue/'), callback='parse_item', follow=True),
    )

    @staticmethod
    def parse_item(response):
        is_book_page = response.xpath('//div[@id="product_gallery"]').extract_first()
        book_loader = ItemLoader(item=BooksCrawlerItem(), response=response)
        if is_book_page:
            book_loader.add_xpath("title", "//div[contains(@class, 'product_main')]/h1/text()")
            book_loader.add_xpath("price", "//div[contains(@class, 'product_main')]/p[@class='price_color']/text()")
            book_loader.add_xpath("in_stock_qty", "//div[contains(@class, 'product_main')]/p[contains(@class, "
                                                  "'instock')]/text()")
            book_loader.add_xpath("stars", "//div[contains(@class, 'product_main')]/p[contains(@class, 'star-rating')]")
            book_loader.add_value("url", response.url)
            book_loader.add_xpath("img_url", "//*[@id='product_gallery']//img/@src")

            yield book_loader.load_item()
