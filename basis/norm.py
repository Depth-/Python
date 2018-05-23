#!/usr/bin/env  python
# coding=utf-8
import sys
import os

def readfile(filename):
    '''打印一个标准输出'''
    f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line,
       # f.close() # 对已经关闭的文件后续调用会报ValueError: I/O operation on closed file  错误

a = sys.argv[0] #0 为空格或者默自己本身
print a

if len(sys.argv)<2: # 判断超过了参数
    print '未指定动作'
    sys.exit()


if sys.argv[1].startswith('--'): # startswith 判断 1是否匹配--
    option = sys.argv[1][2:] #等于2向后的部分表示取第一个命令行参数，但是去掉前两个字节

    if option == 'version':
        print 'Version 110'
    elif option == 'help':
        print '需要帮助'
    else:
        print '未指定参数'
    sys.exit()
else:
    for filename in sys.argv[1:]: # 遍历参数给filename
        readfile(filename)  # 读取这个函数 传递名字