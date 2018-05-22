#!/usr/bin/env python
# coding=utf-8  指定 不指定会报错

#一个类
class Ptest:
    pass
p = Ptest()

print p
#一个对象
class Ptest2:
    def sayhi (self):
        print 'hello'
p = Ptest2()

p.sayhi()

#init方法
class Ptest3:
    def __init__(self,name):
        self.name = name

    def sayHi(self):
        print 'hello'

p = Ptest3('Depth')

p.sayHi()

print '长例子说明--------------------------------------'

class Ptest4:# 类名
    popu = 0 #类的变量

    def __init__(self,name): #name对象当中的遍历
        self.name = name
        print '11名字 %s' %self.name
        Ptest4.popu += 1

    def __del__(self):
        print '%s bye' %self.name
        Ptest4.popu -= 1

        if Ptest4.popu ==0:
            print '只有一个'
        else:
            print '测试 %d' %Ptest4.popu
    def sayhello(self):
        print 'hi,hello %s' %self.name

    def howm(self):
        if Ptest4.popu ==1:
            print 'one'
        else:
            print '我们有 %d ' %Ptest4.popu

secho = Ptest4('Depth')
secho.sayhello()
secho.howm()

becho = Ptest4('kuku')
becho.sayhello()
becho.howm()

secho.sayhello()
secho.howm()

''' 太复杂了 日后研究 ，先看别的 5.22 11 章'''