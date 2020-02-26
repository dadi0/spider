import pymysql


class WeatherPipeline(object):
    def process_item(self, item, spider):
        cityDate = item['cityDate']
        week = item['week']
        temperature = item['temperature']
        weather = item['weather']
        wind = item['wind']

        connect1 = pymysql.connect(
            host='localhost',
            port=3306,
            user='crawlUSER',
            passwd='crawl123',
            db='scrapyDB',
            charset='utf8'
        )
        cur = connect1.cursor()
        mysqlCmd = "INSERT INTO weather(cityDate, week, temperature, weather, wind) VALUES" \
                   "('%s', '%s', '%s', '%s', '%s');" % (cityDate, week, temperature, weather, wind)
        cur.execute(mysqlCmd)
        cur.close()
        connect1.commit()
        connect1.close()

        return item

