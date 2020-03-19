# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import csv


class BjshangpuczPipeline(object):
    def process_item(self, item, spider):
        file_name = 'bjshangpucz.txt'
        with codecs.open(file_name, 'a', 'utf-8') as fp:
            fp.write(f"\n{item['html_address']:\u3000<136s}{item['general_location']:\u3000<10s}"
                     f"{item['location']:\u3000<20s}{item['detailed_location']:\u3000<20s}{item['area']:\u3000<8s}"
                     f"{item['rent']:\u3000<8s}{item['Daily_rent_square_meter']}")
        with codecs.open('bjshangpucz.csv', 'a', 'utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([item['html_address'], item['general_location'], item['location'],
                             item['detailed_location'], item['detailed_location'], item['area'], item['rent'],
                             item['Daily_rent_square_meter']])
        return item
