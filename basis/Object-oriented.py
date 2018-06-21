#!/usr/bin/env python
# coding=utf-8
'''
面向对象编程
确定对象的属性和方法
     属性 -  对象的特征 - 变量
     方法 -  对象的操作 - 函数
臭相聚有共同特征的对象为一个类
设计类和类之间的关系 -- 继承
实例化对象
'''


class Employee:  # 类变量 实例间共享 首字母大写
    '''所有员工的基类'''
    empCount = 0  # 类的属性
    __money = 2000  # 私有属性

    def __init__(self, name, salary):  # init类的构造函数或初始化方法 当创建这个类的实例 就会调用 相当于 - 函数的参数
        self.name = name  # self 代表实例 必须存在 调用的时候可以不用传参
        self.salary = salary
        Employee.empCount += 1  # 运行一次加1

    def __str__(self):
        msg = '你调用了这个类'  # 魔法方法 str 类似与类的说明
        return msg

    def displayCount(self):  # 类的方法
        print "员工人数 %d" % Employee.empCount

    def displayEmployee(self):
        print "姓名 : ", self.name, ", 工资: ", self.salary, "当月奖金: ", self.__money
        # 当月奖金为私有属性，只能类里面使用


"创建 Employee 类的第一个实例对象"
emp1 = Employee("李梅", 3000)
"创建 Employee 类的第二个实例对象"
emp2 = Employee("韩磊", 5000)

print "------------"
print "这是一个实例:", emp1  # 一个实例
emp1.displayEmployee()  # 用.来链接访问的属性 这是访问一个类变量
emp2.displayEmployee()
print "全部员工: %d" % Employee.empCount
print "------------\n"

print "------------修改或者添加属性"
emp1.age = 7  # 添加一个 'age' 属性 这是一个指定一个实例属性
emp1.age = 8  # 修改 'age' 属性

print "这是一个实例：", emp1  # 一个实例
print "一个实例的属性：", emp1.name  # 实例当中的某些属性
print "一个实例的属性：", emp1.age
del emp1.age  # 删除 'age' 属性
print "------------\n"


class Parent:  # 定义父类
    '''
    继承 与多态 同一个方法在不同的类当中有可能有不同的效果 多态
    '''
    parentAttr = 100  # 公有属性
    __site = "www.test.com"  # 私有属性

    def __init__(self):
        print "初始化：调用父类构造函数"

    def parentMethod(self):
        print '方法：调用父类方法'

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父类属性 :", Parent.parentAttr

    def case(self):
        print '父类方法'


class Child(Parent):  # 定义子类 括号内是继承的父类 可以继承多个 用,区分 如果多个父类有同个方法，只继承第一个
    def __init__(self):
        print "初始化：调用子类构造方法"

    def childMethod(self):
        print '方法：调用子类方法'

    def case(self):  # 方法重写
        print '子类方法'  # 如果子类没有这个 调用的是父类的 如果有 以子类为准


c = Child()  # 实例化子类
c.childMethod()  # 调用子类的方法
print '\n'
c.parentMethod()  # 调用父类方法
c.setAttr(200)  # 再次调用父类的方法 - 设置属性值
c.getAttr()  # 再次调用父类的方法 - 获取属性值
c.case()  # 方法重写 子类为准

print   '''
__双下划线开始的方法证明私有 不能调用
不过object._className__attrName 这种方式可以调用
        '''
print '\n'
test = Parent()
print test._Parent__site


class MyList:  # 重写四则运算
    '''运算符重载'''
    __mylist = []  # 初始化定义

    def __init__(self, *args):  # 载入列表
        self.__mylist = []
        for arg in args:
            self.__mylist.append(arg)

    def __add__(self, other):  # 加
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] + other

    def __sub__(self, other):  # 减
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] - other

    def __mul__(self, other):  # 乘
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] * other

    def __div__(self, other):  # 除
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] / other

    def show(self):  # 展示
        print self.__mylist


print '\n功能区'
num = MyList(1, 2, 3, 4, 5)  # 定义一个类
num / 10  # 类运算
num.show()

print '\n自带的一些类的公有内置属性-------------------------'
print "Employee.__doc__:", Employee.__doc__  # 类的属性
print "Employee.__name__:", Employee.__name__  # 类名
print "Employee.__module__:", Employee.__module__  # 类定义所在的模块
print "Employee.__bases__:", Employee.__bases__  # 父类元素
print "Employee.__dict__:", Employee.__dict__  # 属性

'''Tips
python2
class name  经典类
class name(object)  新式类 - 子类
3
class name  新式类  新式类是水平搜索
经典类在调用多个父类的时候是从左到右的顺序
通俗来讲就是多个子类调用一个父类不会重复调用
class(B,C):
    super(name,self).__init__() 只需要指定自身的类名，不需要说明父类
'''