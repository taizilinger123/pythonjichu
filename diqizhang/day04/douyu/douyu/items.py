# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    nickname = scrapy.Field()
    imagelink = scrapy.Field()
    imagePath = scrapy.Field()

    
    
