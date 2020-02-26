import pymysql


connect1 = pymysql.connect(
            host='localhost',
            port=3306,
            user='crawlUSER',
            passwd='crawl123',
            db='scrapyDB',
            charset='utf8'
        )

