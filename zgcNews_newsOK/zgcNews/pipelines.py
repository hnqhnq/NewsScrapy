# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql

class ZgcnewsPipeline(object):
    def __init__(self):
        # 连接数据库
        self.conn = None
        # 游标
        self.cur = None

    def open_spider(self, spider):
        self.conn = pymysql.connect(host='127.0.0.1',
                                    user='root',
                                    password="7880660",
                                    database='myitem',
                                    port=3306,
                                    charset='utf8')

        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        clos, value = zip(*item.items())

        '''
        zip()

        '''
        # sql = "INSERT INTO `%s`(%s) VALUES (%s)" % ('tb_news',
        #                                             ','.join(clos),
        #                                             ','.join(['%s']*len(value)))
        # self.cur.execute(sql, value)
        sql="INSERT INTO tb_news(news_title, news_content, news_img, news_time, hot_img,key_word) " \
              "VALUES (%r,%r,%r,%r,%r,%r)" \
              " " % (item['news_title'],item['news_content'],item['news_img'],item['news_time'],item['hot_img'],item['key_word'])

        print('sql---',sql)
        # 执行
        self.cur.execute(sql)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()