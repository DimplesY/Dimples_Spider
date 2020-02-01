# -*- coding: utf-8 -*-
import sys


import scrapy
from my_spider.items import MySpiderItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    # allowed_domains = ['www.itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        node_list = response.xpath("//div[@class='li_txt']")

        # 将所有数据存在列表中 输出格式默认有json csv xml jsonl
        # items = []

        for node in node_list:
            item = MySpiderItem()

            name = node.xpath("./h3/text()").extract()
            title = node.xpath("./h4/text()").extract()
            info = node.xpath("./p/text()").extract()

            item["title"] = title[0]
            item["name"] = name[0]
            item["info"] = info[0]


            yield item

            # items.append(item)

        # return items

