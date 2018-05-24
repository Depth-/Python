#!/usr/bin/env python
# coding=utf-8
import cPickle as p     # 模块重命名
import sys


text = '''这是一段大的文本，真的很大'''
f = file('open.txt','w') # 写一个文件
f.write(text) #写内容
f.close() #关闭文件

f = file('open.txt') #如果不指定r 默认为读
while True:
    line = f.readline() #读取文件的每一行
    if len(line)==0: #读到空的时候跳出，然后输出
        break
    print line
f.close() #关闭文件

'''Python提供标准的模块，称为pickle。你可以在中储存任何Python对象，之后你可以把它完整地取出来。这被称为持久地储存对象。
还有另一个模块称为cPickle，它的功能和pickle模块完全相同，只不过它是C编写的，因此要快得多( pickle快1000倍)'''

listfile = 'list'         #将存储对象的文件名称

list =['one','two','three','for']       # 内容

f =file(listfile,'w')  #以打开一个file对象
p.dump(list,f) #写存储 list 写入f
f.close()  #关闭这个

del list   #删除内容

f =file(listfile)       #打开一个对象
readlist =p.load(f)     #取存储内容
print readlist

'''异常'''
print '----------------------------------------------------'
s= raw_input('Enter something--> ')
try:
    s =raw_input('test')
except EOFError :
    print 'yichang'
    sys.exit()
except:
    print 'echo'

