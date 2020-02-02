# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import time
import codecs

class MeijuPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y-%m-%d', time.localtime())
        file_name = today + 'meiju.txt'
        with codecs.open(file_name, 'a', 'utf-8') as fp:
            fp.write("%s \t" % item['story_name'])
            fp.write("%s \t" % item['story_state'])
            if len(item['tv_station']) == 0:
                fp.write("unknown \t")
            else:
                fp.write("%s \t" % item['tv_station'])
            fp.write("%s \n" % item['update_time'])
        return item
