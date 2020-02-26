# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem
import sys


class WeatherspiderSpider(scrapy.Spider):
    name = 'weatherspider'
    allowed_domains = ['www.tianqi.com']
    citys = ['wuhan', 'shanghai']
    start_urls = []
    for city in citys:
        start_urls.append('https://www.tianqi.com/' + city + '/')

    def parse(self, response):
        items = []
        city = response.xpath('//dd[@class="name"]/h2/text()').extract()
        selector = response.xpath('//div[@class="day7"]')
        date = selector.xpath('ul[@class="week"]/li/b/text()').extract()
        week = selector.xpath('ul[@class="week"]/li/span/text()').extract()
        wind = selector.xpath('ul[@class="txt"]/li/text()').extract()
        weather = selector.xpath('ul[@class="txt txt2"]/li/text()').extract()
        temperaturel = selector.xpath('div[@class="zxt_shuju"]/ul/li/span/text()').extract()
        temperature2 = selector.xpath('div[@class="zxt_shuju"]/ul/li/b/text()').extract()
        for i in range(7):
            item = WeatherItem()
            try:
                item['cityDate'] = city[0] + date[i]
                item['week'] = week[i]
                item['wind'] = wind[i]
                item['temperature'] = temperaturel[i] + ',' + temperature2[i]
                item['weather'] = weather[i]
            except IndexError as e:
                sys.exit(-1)
            items.append(item)
        return items


