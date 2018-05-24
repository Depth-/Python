#!/usr/bin/env python
# coding=utf-8  指定 不指定会报错

listone =[2,3,4]
listtwo =[2*i for i in listone if i>2] # 循环李彪1当中的每个元素 小于2 乘2
print listtwo
# exec eval 用来执行存在字符串或存储在文件中的 Python 语句
exec 'print "cool"'
b = eval('2*2')
print b

list = ['item']
len(list) >=1
list.pop()



range(1,5)        # 代表从1到5(不包含5)
range(1,5,2)      # 代表从1到5，间隔2(不包含5)
range(5)          # 代表从0到5(不包含5)
