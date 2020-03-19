# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BjshangpuczItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    html_address = scrapy.Field()
    general_location = scrapy.Field()
    location = scrapy.Field()
    detailed_location = scrapy.Field()
    area = scrapy.Field()
    rent = scrapy.Field()
    Daily_rent_square_meter = scrapy.Field()