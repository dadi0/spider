# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    cityDate = scrapy.Field()
    week = scrapy.Field()
    img = scrapy.Field()
    temperature = scrapy.Field()
    weather = scrapy.Field()
    wind = scrapy.Field()
