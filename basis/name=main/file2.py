#!/usr/bin/env python
# -*- coding: utf-8 -*-

from file1 import data
'''引用文件1里面的一个变量'''

data2 = 120

def com():
    if data < data2:
        print "1小于2"
    else:
        print "2大于1"

com()

'''
如果我们不希望运行 文件1当中data1的数值
由于main 已经放入了 file 的 name 中 我们引用不到 main(）
函数的使用动作，所以不会输出 data1的值
'''