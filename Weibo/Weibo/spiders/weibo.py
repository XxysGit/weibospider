# -*- coding: utf-8 -*-
import scrapy
from Weibo.items import WeiboItem

class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.com']
    #基准URL，方便后续做URL拼接
    url= 'https://weibo.com/p/1004065781311106/home?is_all=1&page='
    start_urls=[url+str(1)]

    def parse(self,response):
        for i in range(1,8):
            url=self.url+str(i)
            # scrapy.Request()
            yield scrapy.Request(url, callback=self.parseHtml,dont_filter=True)

    def parseHtml(self, response):
        # 创建item对象
        item = WeiboItem()
        # 每条微博节点对象列表
        baseList = response.xpath('//div[ @ tbinfo] | //div[ @ minfo]')
        for base in baseList:
            item['Time'] = base.xpath('//div[@class="WB_from S_txt2"]/a[@title]').extract()[0]
            item['Blog'] = base.xpath('//div[@class="WB_text W_f14"]/text()').extract()[0]
            yield  item
