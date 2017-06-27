# -*- coding: utf-8 -*-
import scrapy
from QiushiCrawlSpiders.items import QiushicrawlspidersItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Qiushi2Spider(CrawlSpider):
    name = 'qiushi2'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    rules = (
        Rule(LinkExtractor(allow=r's=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        node_list = response.xpath("//div[@class='article block untagged mb15']")
        for node in node_list:
            item = QiushicrawlspidersItem()

            item['username'] = node.xpath(".//h2/text()").extract()[0].encode("utf-8") if not "" else "0"

            item['content'] = node.xpath(".//div[@class='content']/span/text()").extract()[0].encode(
                "utf-8") if not "" else "0"

            if len(node.xpath(".//span[@class='stats-vote']/i/text()")):
                item['vote'] = node.xpath(".//span[@class='stats-vote']/i/text()").extract()[0].encode("utf-8")
            else:
                item['vote'] = ""

            if len(node.xpath(".//span[@class='stats-comments']//i/text()")):
                item['comments'] = node.xpath(".//span[@class='stats-comments']//i/text()").extract()[0].encode(
                    "utf-8") if not "" else "0"
            else:
                item['comments'] = ""

            yield item
