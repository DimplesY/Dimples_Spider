# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem


class WzSunSpider(scrapy.Spider):
    name = 'wz_sun'
    allowed_domains = ['wz.sun0769.com/']
    baseURL = "http://wz.sun0769.com/index.php/question/questionType?page="
    offset = 0
    start_urls = [baseURL + str(offset)]


    def parse(self, response):
        node_list = response.xpath('//body//div[@id="morelist"]//tr//tr')

        for node in node_list:
            item = TencentItem()

            item["number"] = node.xpath(".//td[1]//text()").extract()
            item["title"] = node.xpath(".//td//a[2]//text()").extract()
            item["state"] = node.xpath(".//td[3]//span//text()").extract()
            item["name"] = node.xpath(".//td[4]//text()").extract()
            item["time"] = node.xpath(".//td[5]//text()").extract()

            yield item

        if self.offset < 168810:
            self.offset += 30
            url = self.baseURL + str(self.offset)
            yield scrapy.Request(url,callback=self.parse,dont_filter=True)


