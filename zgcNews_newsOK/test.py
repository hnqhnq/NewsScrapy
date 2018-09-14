""" 
@file: test.py
@Time: 2018/08/11
@Author:heningqiu
"""
import re

# a='http://news.zol.com.cn/695/6954560.html'
# b="cn/(\d+)/(\d+).html"
# print(re.findall(b,a))
import jieba
a= '特斯拉也要自主研发芯片 特斯拉 处理器市场格局或剧变'
mycut=jieba.cut(a,cut_all=False)
c=[]
for i in mycut:
    c.append(i)
print("*"*10)
dic={}
for i in set(c):
    if i != ' ':
        dic[i]=c.count(i)
print(dic)
qq=sorted(dic.items(),key=lambda s:s[1],reverse=True)
print(qq)
print(qq[0][0])





