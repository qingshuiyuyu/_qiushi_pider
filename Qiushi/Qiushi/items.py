# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QiushiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #用户名
    username = scrapy.Field()
    #段子内容
    content = scrapy.Field()
    #好笑数
    vote = scrapy.Field()
    #评论数
    comments = scrapy.Field()
