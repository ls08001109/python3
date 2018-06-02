# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerDemoItem(scrapy.Item):
    moviesName = scrapy.Field()
    playdate = scrapy.Field()
    years = scrapy.Field()
    director = scrapy.Field()
    pass
