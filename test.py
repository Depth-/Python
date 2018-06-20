#!/usr/bin/env python
# coding=utf-8
import requests
me = 0
while me < 200:
    url = "http://act.dota2.com.cn/neverlosefaith/share?uid=448794769&task=zan"
    post_data = "Upgrade-Insecure-Requests: 0 酷酷的DOTA2刷赞"
    r = requests.post(url, data=post_data)
    print r.text
    me += 1