# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MeijuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    story_name = scrapy.Field()
    story_state = scrapy.Field()
    tv_station = scrapy.Field()
    update_time = scrapy.Field()
