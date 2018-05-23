#!/usr/bin/env  python
# coding=utf-8
import sys

a=sys.argv[1:]
b=sys.argv[1][2:]  #因为是空值 在进行第二步判断的时候会报错
c=sys.argv[2:]
d=sys.argv[1]
e=sys.argv[0]

print a
print b
print c
print d
print e

'''
a 是获取第一个参数开始的所有
b 是获取第一个参数 忽略掉参数的前2个字节
c 获取底2个参数开始的所有
d 获取第一个参数
e 程序本身
这其中的0是起始 程序本身
'''

