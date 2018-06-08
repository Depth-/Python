#!/usr/bin/env python
# coding=utf-8  指定 不指定会报错
import datetime

list0 =[2,3,4]
list1 =[2*i for i in list0 if i>2] # 循环列表1当中的每个元素 小于2 乘2
print list1

# exec eval 用来执行存在字符串或存储在文件中的 Python 语句
exec 'print "Depth is cool"'
sentence = eval('2*2'); print sentence

# 随机数
range(1,5)        # 代表从1到5(不包含5)
range(1,5,2)      # 代表从1到5，间隔2(不包含5)
range(5)          # 代表从0到5(不包含5)

i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)

# 集合
x= set('hello')
y= set("world")

print x&y
print x|y
print x-y