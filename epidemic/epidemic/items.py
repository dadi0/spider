# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EpidemicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    confirmed = scrapy.Field()
    suspected = scrapy.Field()
    cure = scrapy.Field()
    death = scrapy.Field()