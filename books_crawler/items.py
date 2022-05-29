# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import re

import scrapy
from itemloaders.processors import TakeFirst, MapCompose


def get_stock_qty(raw_qty):
    qty = re.findall('\d+', raw_qty)
    return qty


def get_starts(raw_stars):
    stars = raw_stars.split(' ')[-1]
    if stars == "One":
        return 1
    if stars == "Two":
        return 2
    if stars == "Three":
        return 3
    if stars == "Four":
        return 4
    if stars == "Five":
        return 5


def get_book_img_url(raw_book_img_url):
    return f"http://books.toscrape.com{raw_book_img_url.split('..')[-1]}"


class BooksCrawlerItem(scrapy.Item):
    title = scrapy.Field(
        output_processor=TakeFirst()
    )
    price = scrapy.Field(
        output_processor=TakeFirst()
    )
    in_stock_qty = scrapy.Field(
        input_processor=MapCompose(get_stock_qty),
        output_processor=TakeFirst()
    )
    stars = scrapy.Field(
        input_processor=MapCompose(get_starts),
        output_processor=TakeFirst()
    )
    url = scrapy.Field(
        output_processor=TakeFirst()
    )
    img_url = scrapy.Field(
        input_processor=MapCompose(get_book_img_url),
        output_processor=TakeFirst()
    )
