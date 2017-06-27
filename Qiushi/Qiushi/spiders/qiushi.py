# -*- coding: utf-8 -*-
import scrapy
from Qiushi.items import QiushiItem


class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    allowed_domains = ['qiushibaike.com']
    #baseURL = 'https://www.qiushibaike.com'
    offset = 1
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        node_list = response.xpath("//div[@class='article block untagged mb15']")
        for node in node_list:
            item = QiushiItem()

            item['username'] = node.xpath(".//h2/text()").extract()[0].encode("utf-8") if not "" else "0"

            item['content'] = node.xpath(".//div[@class='content']/span/text()").extract()[0].encode("utf-8") if not "" else "0"

            if len(node.xpath(".//span[@class='stats-vote']/i/text()")):
                item['vote'] = node.xpath(".//span[@class='stats-vote']/i/text()").extract()[0].encode("utf-8")
            else:
                item['vote'] = ""

            if len(node.xpath(".//span[@class='stats-comments']//i/text()")):
                item['comments'] = node.xpath(".//span[@class='stats-comments']//i/text()").extract()[0].encode("utf-8") if not "" else "0"
            else:
                item['comments'] = ""

            yield item

        if self.offset < 35:
            self.offset += 1
            url = 'https://www.qiushibaike.com/text/page/' +str(self.offset)+'/?s=4995260'
            yield scrapy.Request(url,callback=self.parse)