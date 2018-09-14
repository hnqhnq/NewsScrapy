# -*- coding: utf-8 -*-
import re
import jieba

import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from zgcNews.items import ZgcnewsItem


class MynewsSpider(CrawlSpider):
    name = 'mynews'
    allowed_domains = ['zol.iqiyi.com.cn', 'zol.com.cn']
    start_urls = ['http://news.zol.com.cn/695/6954560.html']
    # 可迭代对象,可多个
    rules = [Rule(LinkExtractor(allow=("cn/(\d+)/(\d+).html")),
                  callback='get_parse', follow=True), ]

    def get_parse(self, response):
        #获取页面html
        html_bd=response.body.decode('gbk')
        # 标题
        news_title = response.xpath('//div[@class="wrapper"]/div//h1/text()').extract()
        if len(news_title)!=0:
            news_title=news_title[0]
        else:
            news_title='None'
        # 内容
        news_content = response.xpath('//div[@id="article-content"]//p/text()').extract()
        # 时间
        try:
            news_time = response.xpath('//*[@id="pubtime_baidu"]//text()').extract()[0]
        except KeyError:
            pass
        #正则匹配页面所有jpg
        re_img="src=(.*?\.jpg)"
        # 页面所有jpg存储格式是一个列表存放多条jpg。
        hot_img=(re.findall(re_img,html_bd))[0]
        # 内容图片
        news_img = response.xpath('//div[@id="article-content"]//img[@id="content-first-img"]/@src').extract()
        if len(news_img)!=0:
            news_img=news_img[0]
        else:
            news_img="暂无"

        print('news_title----', news_title,type(news_title))
        print('news_img----', news_img,type(news_img))
        print('news_time----', news_time,type(news_time))
        print('hot_img----', hot_img,type(hot_img))
        content = ''
        for i in news_content:
            content += i.replace('\xa0', '') + '\n'
        print('content---', content,type(content))

#————使用jieba将内容进行分词并统计出词频最高的词组设置为关键字————————
        mycut = jieba.cut(content, cut_all=False)
        c = []
        for i in mycut:
            c.append(i)
        dic = {}
        for i in set(c):
            if len(i)>1:
                dic[i] = c.count(i)
        key_word = (sorted(dic.items(), key=lambda s: s[1], reverse=True))[0][0]
        print('*key_word--',key_word,type(key_word))

        item = ZgcnewsItem()
        item["news_title"]=news_title
        item["news_content"]=content
        item["news_img"]= news_img
        item["news_time"]= news_time
        item["hot_img"]= hot_img
        item["key_word"]= key_word

        yield item
