# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    #标题
    title  = scrapy.Field()
    #信息
    bd  = scrapy.Field()
    #评分
    star  = scrapy.Field()
    #简介
    quote  = scrapy.Field()
    
