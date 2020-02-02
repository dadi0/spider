# -*- coding: utf-8 -*-
import scrapy
from meiju.items import MeijuItem


class MeijuspiderSpider(scrapy.Spider):
    name = 'meijuspider'
    allowed_domains = ['meijutt.com']
    start_urls = ['https://www.meijutt.tv/new100.html']

    def parse(self, response):
        sub_select = response.xpath('//li/div[@class="lasted-num fn-left"]')
        items = []
        for sub in sub_select:
            item = MeijuItem()
            item['story_name'] = sub.xpath('../h5/a/text()').extract()[0]
            try:
                item['story_state'] = sub.xpath('../span[@class="state1 new100state1"]/font/text()').extract()[0]
            except IndexError as e:
                item['story_state'] = sub.xpath('../span[@class="state1 new100state1"]/text()').extract()[0]
            item['tv_station'] = sub.xpath('../span[@class="mjjq"]/text()').extract()[0]
            try:
                item['update_time'] = \
                    sub.xpath('../div[@class="lasted-time new100time fn-right"]/font/text()').extract()[0]
            except IndexError as e:
                item['update_time'] = \
                    sub.xpath('../div[@class="lasted-time new100time fn-right"]/text()').extract()[0]
            items.append(item)
        return items
