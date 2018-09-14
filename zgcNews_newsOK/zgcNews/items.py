# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ZgcnewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    news_title  = scrapy.Field()
    news_content = scrapy.Field()
    news_img    = scrapy.Field()
    news_time   = scrapy.Field()
    hot_img     = scrapy.Field()
    key_word    = scrapy.Field()



