# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import time


class ComicsPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y-%m-%d', time.localtime())
        fileName = '武汉汉街万达广场店' + today + '.txt'
        print(type(item['MovieTitleCn']))
        with codecs.open(fileName, 'a+', 'utf-8') as fp:
            fp.write('%s %s %s %s \n'
                     % (item['MovieTitleCn'],
                        item['MovieTitleEn'],
                        item['director'],
                        item['runtime']))
