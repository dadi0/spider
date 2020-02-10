# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver


class EpidemicspiderSpider(scrapy.Spider):
    name = 'epidemicspider'
    allowed_domains = ['voice.baidu.com']
    start_urls = ['https://voice.baidu.com/act/newpneumonia/newpneumonia/']

    def parse(self, response):
        items = []
        sub_selector = response.xpath('//*[@id="ptab-0"]/div[2]/table/tbody/tr/td[1]/div/div[1]').extract()
