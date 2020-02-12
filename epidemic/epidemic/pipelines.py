# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import time
import codecs


class EpidemicPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y-%m-%d', time.localtime())
        fileName = 'epidemic.txt'
        with codecs.open(fileName, 'a', 'utf-8') as fp:
            fp.write(
                "%s\t\t%s\t\t%s\t\t%s\t\t%s\n" % (
                    today,
                    item['confirmed'],
                    item['suspected'],
                    item['cure'],
                    item['death']
                )
            )
        return item
