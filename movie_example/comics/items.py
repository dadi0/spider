# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ComicsItem(scrapy.Item):
    MovieTitleCn = scrapy.Field()
    MovieTitleEn = scrapy.Field()
    director = scrapy.Field()
    runtime = scrapy.Field()
