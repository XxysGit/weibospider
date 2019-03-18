from scrapy import cmdline

cmdline.execute('scrapy crawl weibo -o weibo.csv'.split())