#!/usr/bin/env python
# coding=utf-8
import demjson
data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
json = demjson.encode(data)
print json
'''存在一个灵异问题 pycharm加载不了 json模块 本地可以'''