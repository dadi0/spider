import time
import codecs
import json


class WeatherPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d', time.localtime())
        filename = today + '.json'
        with codecs.open(filename, 'a', 'utf-8') as fp:
            jsonstr = json.dumps(dict(item))
            fp.write("%s \r\n" % jsonstr)
        return item

