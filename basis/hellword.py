#!/usr/bin/env python
# coding=utf-8  指定 不指定会报错

### 1.开始的python 复习项目
print 'Hello World'

### 2.' " ''' 三种引号之间的区别
'''
单引号 =  双引号 > 三引号（一段话）
'''

### 3.一个运算测试
length = 5
wight = 2
end = length * wight
print 'ens is', end
print 'dobule is', 2 * (length + wight)

### 4.控制
#depth = raw_input('depth cool or no cool?')
depth = 'cool'

if depth == "cool":
    print 'yes'
else:
    print 'no cool'

### 5.while有一个可选的else从句
### elif和else  elif==if else则是从句

old ='nianling'
while old:
    number='22'
    #age = raw_input('age?')
    age = '23'
    if age == number:
        print 'yes'
    elif age < number:
            print 'small'
    elif age > number:
           print 'big'
           break

count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"

for i in range(1, 5):
    print i
else:
    print 'The for loop is over'

s = 1 #变量当中用引号赋值，相当于字符型

while True: #起始一个真条件
    #s = raw_input('Enter something : ')
    s+=1
    if s < 5:
        print 's < 5'
        continue  #截至剩下的代码块 重新循环
    if s > 5:
        break
    print 's > 5'
    ##从用户处取到输入。判断

### 6函数
def sayHello():
    print 'Hello World!' # 函数内容 def定义
sayHello()

def printMax(a, b):
    if a > b:
         print a, 'is maximum'
    else:
        print b, 'is maximum'

printMax(3, 4) # 传递给函数的参数 比较大小输出较大的
x= 5
y= 7
printMax(x, y) # 定义函数的参数的值，比较大小

### 7.局部变量
def bigt(qq):
    print 'is',qq
    qq=10
    print '后来的值',qq

qq=50
bigt(qq)  #经过函数后的值会恢复之外的值
print 'is',qq

### 7.2全局变量
print "----------"
def bigt():
    global qq
    print 'is',qq
    qq=10
    print '后来的值',qq
#一个函数内的代码默认为一个模块 平级

qq=50
bigt()  #经过函数后的值不会恢复
print 'is',qq

#默认参数
def say(message, times = 1):
    print message * times
say('Hello')
say('World', 5)
#不写即为参数默认，写了之后以自己的为准

def func(a, b=5, c=10):#定义名字的参数一般叫做关键参数
    print 'a is', a, 'and b is', b, 'and c is', c

func(3, 7)
func(25, c=24)
func(c=50, a=100)
#return 从函数中返回 或者跳出 或返回一个值


def maximum(x, y):
    if x > y:#比较大小 返回值
      return x
    else:
      return y

print maximum(2, 3)
print '--------------'

def printMax(x, y):
    '''Prints the maximum of two numbers.
    The two values must be integers.'''
    x = int(x) # convert to integers, if possible y = int(y)
    if x > y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'

'''DocStrings
   Python有一个很奇妙的特性，称为 文档字符串 ，
   它通常被简称为 docstrings 。DocStrings是一个 重要的工具，由于它帮助
   你的程序文档更加简单易懂，你应该尽量使用它。你甚至可以在程序 运行的时候，
   从函数恢复文档字符串!'''

printMax(3, 5)
print printMax.__doc__

print 'maintestno'
# 与以下内容做对比 ，输出在 defclassß

if __name__ == "__main__":
    print 'maintestyes'
#文档输出