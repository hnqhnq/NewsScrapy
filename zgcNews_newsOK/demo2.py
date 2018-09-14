#name:myzhong
#author:Yangwenwu
#@Time:2018/8/11 10:49
# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MyzhongSpider(scrapy.Spider):
    name = 'myzhongg'
    allowed_domains = ['news.zol.com.cn']
    start_urls = ['http://news.zol.com.cn/695/6954724.html']
    # start_urls = ['http://news.zol.com.cn/695/6954724.html', 'http://news.zol.com.cn/list.html']

    # rules = [Rule(LinkExtractor(allow= ('[0-9]+/(.*).html$')), callback= "get_parse", follow= True)]

    def parse(self, response):
        print('response----',response.body.decode('gbk'))
        # title = response.xpath('//div[@class="article-header clearfix"]/h1/text()').extract()[0]
        # articlearc = response.xpath('//div[@id="article-content"]/div//p/text()').extract()
        imgsrc = response.xpath('//div[@id="article-content"]/div//img/@src').extract()
        #
        # print("+++++++++++++++++++", articlearc)
        # url = articlearc[-1]
        # article = ''
        # for context in articlearc:
        #      article += context.replace('\xa0', '')
        # print('+++',  article, '++')
        # print('++++++++++++++++++++++++++++')
        #
        # item = ZgcItem()
        #
        # item['title'] = title
        # item['articlearc'] = article
        # item['imgsrc'] = imgsrc
        # item['articleurl'] = url
        #
        # yield item


