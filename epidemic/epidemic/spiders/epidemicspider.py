# -*- coding: utf-8 -*-
import scrapy
from epidemic.items import EpidemicItem


class EpidemicspiderSpider(scrapy.Spider):
    name = 'epidemicspider'
    allowed_domains = ['voice.baidu.com']
    start_urls = ['https://voice.baidu.com/act/newpneumonia/newpneumonia/']

    def parse(self, response):
        items = []
        item = EpidemicItem()
        confirmed = response.xpath('//*[@id="ptab-0"]/div[2]/table/tbody/tr/td[1]/div/div[1]/text()').extract()
        suspected = response.xpath('//*[@id="ptab-0"]/div[2]/table/tbody/tr/td[2]/div/div[1]/text()').extract()
        cure = response.xpath('//*[@id="ptab-0"]/div[2]/table/tbody/tr/td[3]/div/div[1]/text()').extract()
        death = response.xpath('//*[@id="ptab-0"]/div[2]/table/tbody/tr/td[4]/div/div[1]/text()').extract()
        item['confirmed'] = confirmed[0]
        item['suspected'] = suspected[0]
        item['cure'] = cure[0]
        item['death'] = death[0]
        items.append(item)
        return items

