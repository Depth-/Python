#!/usr/bin/env python
# coding=utf-8  指定 不指定会报错
#基本分类  列表   元组    字典

def web():
    chars =['a','c','e','h','k','m','n','o','_']
    pos =[1,3,2,6,3,0,7,8,1,5,4]
    return ''.join([chars[i] for i in pos])

print web()

# This is my shopping list

shoplist = ['apple', 'mango', 'carrot', 'banana']

print 'I have', len(shoplist),"查看长度"

print 'These items are:', # Notice the comma at end of the line #

for item in shoplist:
    print item + "循环输出内容"

print '\nI also have to buy rice.'
shoplist.append('rice')      # 增加内容
print 'My shopping list is now', shoplist

print 'I will sort my list now'
shoplist.sort()               # 排序
print 'Sorted shopping list is', shoplist

print 'The first item I will buy is', shoplist[0]
olditem = shoplist[0]

del shoplist[0]#删除列表内第一个  ß
print 'I bought the',olditem
print 'My shopping list is now', shoplist

#元组 不可修改（）括号包含
zu = ('1', '2', '3')
print 'Number is', len(zu)

new_zu = ('4', '5', zu)
print 'Number  new zoo is', len(new_zu)
print 'All number', new_zu
print 'Animnumberoo are', new_zu[2]
print 'Last', new_zu[2][2]     # 元组内的元组数据
# 字典
