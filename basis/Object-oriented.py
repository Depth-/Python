#!/usr/bin/env python
# coding=utf-8  指定 不指定会报错

class Employee: # 类变量 实例间共享
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary): #init类的构造函数或初始化方法 当创建这个类的实例 就会调用
        self.name = name     #self 代表实例 必须存在 调用的时候可以不用传参
        self.salary = salary
        Employee.empCount += 1 #运行一次加1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary

"创建 Employee 类的第一个实例对象"
emp1 = Employee("Zara", 2000)  #调用类创建的一个对象
"创建 Employee 类的第二个实例对象"
emp2 = Employee("Manni", 5000)
print emp1 # 一个实例

emp1.displayEmployee()  #用.来链接访问的属性 这是访问一个类变量
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

'修改或者添加'
emp1.age = 7  # 添加一个 'age' 属性 这是一个指定一个实例属性
emp1.age = 8  # 修改 'age' 属性

print emp1   #一个实例
print emp1.name  #实例当中的某些属性
print emp1.age
del emp1.age  # 删除 'age' 属性

print '\n自带的一些类-------------------------'
print "Employee.__doc__:", Employee.__doc__          # 类的属性
print "Employee.__name__:", Employee.__name__        # 类名
print "Employee.__module__:", Employee.__module__    # 类定义所在的模块
print "Employee.__bases__:", Employee.__bases__      # 父类元素
print "Employee.__dict__:", Employee.__dict__        # 属性

print '\n继承'
class Parent:        # 定义父类
   parentAttr = 100
   __site = "www.test.com"

   def __init__(self):
      print "调用父类构造函数"

   def parentMethod(self):
      print '调用父类方法'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "父类属性 :", Parent.parentAttr

   def case(self):
       print '父类方法'


class Child(Parent): # 定义子类 括号内是继承的父类 可以继承多个 用,区分
   def __init__(self):
      print "调用子类构造方法"

   def childMethod(self):
      print '调用子类方法'

   def case(self):      # 方法重写
       print '子类方法'   #如果子类没有这个 调用的是父类的 如果有 以子类为准

c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
print '\n'
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法 - 设置属性值
c.getAttr()          # 再次调用父类的方法 - 获取属性值
c.case()             # 方法重写

'__双下划线开始的方法证明私有 不能调用 不过object._className__attrName这种方式可以调用'
test = Parent()
print test._Parent__site