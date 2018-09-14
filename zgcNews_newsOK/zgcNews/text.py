""" 
@file: text.py
@Time: 2018/08/10
@Author:heningqiu
"""
import re

text='<img onerror="javascript:this.src=\'https://icon.zol-img.com.cn/public/nopic.jpg\'" alt="苹果紧急修复MacBook Pro降频问题 不是我们压不住" .src="https://article-fd.zol-img.com.cn/t_s200x150/g5/M00/01/09/ChMkJltYXiaIHO2sAADG4k9b6zoAAqAsQLGnhUAAMb6798.jpg" width="200" height="150">'
a='dhgaw8676.jpg'
b="(i?)<img.*? src=\"?(.*?\\.(jpg|gif|bmp|bnp|png))\".*? />"
print(re.findall('[0-9]',a))

print(re.findall(r'.src=\"(.*jpg)',text))

# print(re.match('com', 'www.runoob.com'))
# print(re.match('www', 'www.runoob.com').span())

# print(re.findall())