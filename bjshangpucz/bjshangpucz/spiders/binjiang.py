# -*- coding: utf-8 -*-
import scrapy
from bjshangpucz.items import BjshangpuczItem


class BinjiangSpider(scrapy.Spider):
    name = 'binjiang'
    allowed_domains = ['hz.58.com']
    start_urls = ['http://hz.58.com/binjiang/shangpucz/pn1/']

    def parse(self, response):
        selector = response.xpath('//*[@id="house-list-wrap"]/li')
        items = []
        for one in selector:
            item = BjshangpuczItem()
            item['html_address'] = one.xpath('./h2/a/@href').extract()[0]
            item['general_location'] = one.xpath('./div[2]/p[1]/span[1]/text()').extract()[0].strip()
            item['location'] = one.xpath('./div[2]/p[1]/span[2]/text()').extract()[0].strip()
            item['detailed_location'] = one.xpath('./div[2]/p[2]/text()').extract()[0].strip()
            item['area'] = one.xpath('./div[4]/p[1]/span[1]/text()').extract()[0] + \
                one.xpath('./div[4]/p[1]/span[2]/text()').extract()[0]
            if one.xpath('./div[3]/@class').extract()[0] == 'price ':
                item['rent'] = one.xpath('./div[3]/span[1]/text()').extract()[0] + \
                    one.xpath('./div[3]/span[2]/text()').extract()[0]
                item['Daily_rent_square_meter'] = one.xpath('./div[3]/p[1]/text()').extract()[0]
            else:
                item['rent'] = one.xpath('./div[3]/span[1]/text()').extract()[0]
                item['Daily_rent_square_meter'] = ''

            items.append(item)
        return items
