#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy

#创建一个爬虫类
class ItcastSpider(scrapy.Spider):
    #爬虫名
    name = "itcast"
    #允许爬虫作用的范围
    allowd_domain = ["http://www.itcast.cn/"]
    #爬虫启始的url
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml#"]

    def parse(self, response):
        with open("teacher.html", "w") as f:
            f.write(response.body)
