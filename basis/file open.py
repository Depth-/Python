#!/usr/bin/env python
# coding=utf-8
import os
''' 两者的区别 input 可以接受表达式 另外一个只是字符串
raw_input:input
Python3 当中只剩input
Demo:
str = input("请输入：")
print "你输入的内容是: ", str
这会产生如下的对应着输入的结果：
请输入：[x*5 for x in range(2,10,2)]
你输入的内容是:  [10, 20, 30, 40]
'''

# 方法  指针是比较重要的一个概念seek
# s.read() 一个一个全读 string 字符型
# s.readline() 读取一行
# s.readline(5) 读取一行的5个字节
# s.readlines() 读取一个列表

fo = open("foo.txt", "w") # 部分模式说明 w 写 w+ 读写 a 追加 a+ 读写 r+ 打开一个文件 指针从头开始
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace

# 写
# 打开一个文件
fo = open("foo.txt", "w")
fo.write("这是一个测试文件")
# 关闭打开的文件
fo.close()

# 读
# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read(10)
print "\n读取的字符串是 : ", str

# 查找当前位置
position = fo.tell()
print "当前文件位置 : ", position

# 把指针再次重新定位到文件开头
position = fo.seek(0, 0)
str = fo.read(10)
print "重新读取字符串 : ", str
# 关闭打开的文件
fo.close()

#删除 重命名 新建
os.mkdir("newdir")
os.rename( "foo.txt","test.txt")
os.remove("test.txt")
os.rmdir("newdir")

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

try:
    '正常的操作'
except:
    '发生异常，执行这块代码'
else:
    '如果没有异常执行这块代码'
'''异常  里面可以放一些不需要的报错信息 必须加except响应'''
print '----------------------------------------------------'
s = raw_input('Enter something--> ')
try:
    s =raw_input('test')
except EOFError :
    print '异常操作'
    sys.exit()
except:
    print 'echo'