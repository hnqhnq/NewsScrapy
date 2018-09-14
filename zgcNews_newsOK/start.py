#!C:\Python36\python.exe
# -*- coding:utf-8 -*-
'''
@Time    : 2018/7/10 9:51
@Author  : Fate
@File    : start.py
'''

import scrapy.cmdline

def main():
    scrapy.cmdline.execute(['scrapy', 'crawl', 'mynews','-o','news.csv'])

if __name__ == '__main__':
    main()
