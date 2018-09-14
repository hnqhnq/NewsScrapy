# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from zgcNews.items import ZgcnewsItem

class MynewsSpider(CrawlSpider):
    name = 'mynews'
    allowed_domains = ['zol.iqiyi.com.cn','zol.com.cn']
    start_urls = ['http://news.zol.com.cn/695/6954560.html']
    # 可迭代对象,可多个
    rules = [Rule(LinkExtractor(allow=("cn/(\d+)/(\d+).html")),
                  callback='get_parse', follow=True),]

    def get_parse(self, response):
        # vido_list=response.xpath('//ul[@id="focus-list"]//li')
        # vido_title=response.xpath('')
        # vido_title=response.xpath('//div[@class="wrapper"]/div//h1/text()').extract()[0]
        vido_content=response.xpath('//div[@id="article-content"]//text()')
        # print('vido_title----',vido_title)
        # print('vido_conten----',vido_content)
        content=''
        for i in vido_content:
            content += i.extract()[0]
        print('content---',content)

        item = ZgcnewsItem()
        # for vido in vido_list:
        #     print('-----77---' * 10)
        #     vido_title = vido.xpath('./h4//text()').extract()[0]
        #     vido_data = vido.xpath('./@data-swf').extract()[0]
        #     print('vido_data----',vido_data)
        #     print('vido_title----',vido_title)

            # item[vido_title]=vido_title
            # item[vido_data]=vido_data
            #
            # yield item