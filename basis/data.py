#!/usr/bin/env python
# coding=utf-8  指定 不指定会报错
#基本分类  列表   元组    字典
#  三种 括号代表的区别

# 第一种 []
print '[] 列表 的说明 可修改 可添加------------------------------------------'
shoplist = ['apple', 'mango', 'carrot', 'banana']
print '我有', len(shoplist),"内容"

for item in shoplist:
    print item + "循环输出"

shoplist.append('rice')      # 增加内容
print '现在具有的内容  ', shoplist

shoplist.sort()              # 排序
print '排序', shoplist

print '单独取出一个内容', shoplist[0]
olditem = shoplist[0]
del shoplist[0]     #删除列表内第一个
print '删除一个内容',olditem
print '剩下的内容', shoplist

#元组 不可修改（）括号包含
print '\n() 元组 的说明 不可修改 ------------------------------------------'
zu = ('1', '2', '3')
print '几个内容', len(zu)

new_zu = ('4', '5', zu)  #内容包括
print '新加入的视为一个内容 ', len(new_zu)

print '全部的内容', new_zu
print '取一个内容', new_zu[2]
print '取内容当中的内容', new_zu[2][2]     # 元组内的元组数据
# 字典
print '\n{} 字典 的说明 不可修改 ------------------------------------------'
zd={ 'zhao' : '123',
     'qian' : '456',
     'sun'  : '789',
     'li'   : '1011' }
print "输出的值%s" %zd['zhao']
print "Tips：print语可以跟着%符号的字符。这些字符具备定制的功能。\n"     \
      "定制让输出满足某种特定的格式。定制可以是%s表示字符 或%d表示整数。\n" \
      "组必须按照相同的顺序来 对应这些定制。%s 定制后面%开头的输出"
print zd

zd['zhou'] = '1111'   # 新增加一个

del zd['li']          # 删除一个
print '\n其中的内容%s\n' %len(zd)

for name, zhi in zd.items():     #循环名字和值两个字段来自zd的值对
    print 'name %s zhi %s' %(name, zhi)
if'qian' in zd:
    print "\nqian's %s" %zd["qian"]

print ' \n序列的说明 ------------------------------------------'
list = ['one', 'two', 'three', 'for']
#Indexingor 'Subscription' operation p r i n t ' I t em 0 i s' , sh o p l i st [ 0] print'Item1 is',shoplist[1]
print 'is 0',list[0]
print 'is 1',list[1]
print 'is 2',list[2]
print 'is 3',list[3]
print 'is -1',list[-1]
print 'is -2',list[-2]
print "具体的值\n -1代表从后置未开始 0代表从头开始"

list = ['one', 'two', 'three', 'for']
print 'is 1 和 3',list[1:3]    #[]切片中的数据 是从开始位开始，结束位结束,结束位会排斥在切片之外
print 'is 2',list[2]           #输出
print 'is 1 全部',list[1:]      #从1开始的全部
print 'is 1 到 -1',list[1:-1]   # 平级的 -1 == 3 按照顺序
print '全部',list[:]            #全部


print '\n字符串的方法 ------------------------------------------'

name =  "kukudedepth"
if name.startswith('kukude'):
    print 'yes1 '  # 是否是kukude 开始
if 'kukude' in name:
    print 'yes2'   # 是否存在
if name.find('depth')!=-1:
    print 'yes3'   # 查找指定字符串再另一个字符串的位置或返回-1代表找不到w

name2 ='_*_'
mylist =['one','two','three']
print name2.join(mylist)     # join 分隔符
