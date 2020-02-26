# -*- coding: utf-8 -*-
import scrapy
from comics.items import ComicsItem
import re


class ComicsSpider(scrapy.Spider):
    name = 'ComicsSpider'
    allowed_domains = ['http://www.mtime.com/']
    start_urls = ['http://theater.mtime.com/China_Hubei_Province_Wuhan_Wuchang/4316/']

    def parse(self, response):
        selector = response.xpath('/html/body/script[3]/text()')[0].extract()
        moviesStr = re.search('"movies":\[.*?\]', selector).group()
        moviesList = re.findall('\{.*?\}', moviesStr)
        items = []
        for movie in moviesList:
            mDic = eval(movie)
            item = ComicsItem()
            item['MovieTitleCn'] = mDic.get('movieTitleCn')
            item['MovieTitleEn'] = mDic.get('movieTitleEn')
            item['director'] = mDic.get('director')
            item['runtime'] = mDic.get('runtime')
            items.append(item)
        return items

