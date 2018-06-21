#!/usr/bin/env python
# coding=utf-8
import re
import urllib


#  一个简单的图片爬虫
def geturl(url):
    page = urllib.urlopen(url)
    html = page.read()
    page.close()
    return html


def get_img(html):
    reg = 'src="(.*?\.jpg)" size="\d+" width="500" height="500"'  # 括号内标识一个分组 compile 返回结果为分组内的内容
    img_re = re.compile(reg)
    weather_list = img_re.findall(html)  # findall 优先返回分组内的内容
    i = 0
    for img_url in weather_list:
        print img_url
        urllib.urlretrieve(img_url, "%d.jpg" % (i,))  # 远程数据下载到本地
        i += 1


ht = geturl(r'https://tieba.baidu.com/p/5731619943')

get_img(ht)

c = open("html.txt", "w+")
c.write(ht)
c.close()
