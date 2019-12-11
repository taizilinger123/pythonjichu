# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguan.items import DongguanItem


class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

    rules = (
        Rule(LinkExtractor(allow=r'type=4'),process_links = "deal_links", follow=True),
        #Rule(LinkExtractor(allow=r'/html/question/\d+\d+.shtml'),callback = 'parse_item'),
    )
    
    #需要重新处理每个response里提取的链接,Type&page=xxx?type=4 修改为 Type?page=xxx&type=4
    #links 就是LinkExtractor提取出来的当前页面链接列表
    def deal_links(self, links):
        for link in links:
            link.url = link.url.replace("?","&").replace("Type&","Type?")
        #返回修改完的links链接列表
        return links

    def parse_item(self, response):
        #print response.url
        
        item = DongguanItem()
        #标题
<<<<<<< Updated upstream
        item["title"] =  response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0]
        #编号
        item["number"] = item['title'].split(' ')[-1].split(":")[-1]
         #内容
        item["content"] = response.xpath('//div[@class="c1 text14_2"]/text()').extract()[0]
        #链接
        item["url"] = response.url 
=======
>>>>>>> Stashed changes
         
        yield item
