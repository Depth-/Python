#!/usr/bin/env python
# coding=utf-8  指定 不指定会报错
# 模块 5.17
import sys

print '函数类 学习----------------------------------------------------'

# 定义函数 这里写了了一个必备参数
def printme(str):# 括号内的内容是可控的
    "打印任何传入的字符串"
    print str
    return
# 调用函数
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")

def ChangeInt(a):
    a = 10
    print a
b = 2

ChangeInt(1) #函数单独执行的时候，必须要给予参数做定义
ChangeInt(b) #这里看到参数指定为B 所以下面输出了2 函数写了参数 参数不能为空 这是一个必备参数
print b # 结果是 2

print '关键字参数 案例---------------------------'

# 可写函数说明 两个关键字 关键字参数一般来确定传入的值
def printinfo(name, age):
    "打印任何传入的字符串"
    print "Name: ", name
    print "Age ", age
    return


# 调用printinfo函数 可以看到指定了输出
printinfo(age=50, name="miki")


print '可写函数说明 缺省参数---------------------------'
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print "Name: ", name
    print "Age ", age
    return


# 调用printinfo函数 这里第二个函数没有定义age 但是age参数本身有缺省值 所以会正常输出
printinfo(age=50, name="miki")
printinfo(name="miki")

print '不定长参数 ---------------------------'


# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print "输出: "
    print arg1
    for var in vartuple:
        print var
    return

# 加了星号（*）的变量名会存放所有未命名的变量参数
# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)

print '全局变量的区别-----------------------'
total = 0  # 这是一个全局变量
# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2;  # total在这里是局部变量.
    print "函数内是局部变量 : ", total
    # global total 如果函数内变量想影响全局 需要声明
    return total

# 调用sum函数
sum(10, 20)
print "函数外是全局变量 : ", total

Money = 2000
def AddMoney():
    global Money
    Money = Money + 1
print Money # 原始值
AddMoney()  # 经过函数运算
print Money # 已修改

print '模块------------\n'
# from 1 import 2 加载1模块当中的2函数

import sys
deflist = dir(sys)
print deflist # 打印出所有方法

#  _init__.py 用于标识当前文件夹是一个包。
# 文件下下必须存在可以为空，这样在上层的文件就可以调用文件夹内的模块
'''
test.py
package_runoob
|-- __init__.py
|-- runoob1.py
|-- runoob2.py
结构

调用方法 test.py
from package_runoob.runoob1 import runoob1
from package_runoob.runoob2 import runoob2

'''
