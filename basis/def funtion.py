#!/usr/bin/env python
# coding=utf-8  指定 不指定会报错
# 模块 5.17
import sys

# import 模块
# import 模块 as 别名
# form 模块 import 函数名类名

# pyc 文件是给机器看的，如果不想公开源代码 可以 python -m py_compile file.py 编译
# 装饰器 本质 传递函数 拿到一个函数进行处理在返回一个函数

print '函数类 学习----------------------------------------------------'


# 定义函数 这里写了了一个必备参数
def print_me(str):  # 括号内的内容是可控的 str只是一个标签 没有具体的对象的值
    "打印任何传入的字符串"
    print str
    return  # 执行后函数内代码终止


# 调用函数
print_me("我要调用用户自定义函数!")


def ChangeInt(a):
    a = 10
    print a


b = 2
ChangeInt(1)
ChangeInt(b)
# 函数单独执行的时候，必须要给予参数做定义这里看到参数指定为B 所以下面输出了2 函数写了参数 参数不能为空 这是一个必备参数
print b  # 结果是 2

print '\n关键字参数 案例-------------------------------------------------'


# 可写函数说明 两个关键字 关键字参数一般来确定传入的值
def print_info(name, age):
    "打印任何传入的字符串"
    print "Name: ", name
    print "Age ", age
    return


# 调用print_info函数 可以看到指定了输出
print_info(age=50, name="miki")

print '\n可选函数说明 缺省参数--------------------------------------------'


def print_info(name, age=35):
    "打印任何传入的字符串"
    print "Name: ", name
    print "Age ", age
    return


# 调用print_info函数 这里第二个函数没有定义age 但是age参数本身有缺省值 所以会正常输出
print_info(age=50, name="miki")
print_info(name="miki")

print '\n不定长参数 ----------------------------------------------------'


def print_info(arg1, *var_tuple):  # 可写函数说明
    "打印任何传入的参数"
    print "输出: ", arg1
    for var in var_tuple:
        print "循环输出的常参数", var
    return


# 加了星号（*）的变量名会存放所有未命名的变量参数
# 第二种*号的用法，如何函数内传递的是一个列表或者元组的数据 print_info(*参数) 这里会自动把数据进行拆分
# 调用print_info 函数
print_info(10)
print_info(70, 60, 50)

print '\n全局变量的区别--------------------------------------------------'
total = 0  # 这是一个全局变量


# 可写函数说明
def sum(arg1, arg2):  # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print "函数内是局部变量 : ", total
    # global total 如果函数内变量想影响全局 需要声明
    return total


# 调用sum函数
sum(10, 20)
print "函数外是全局变量 : ", total

Money = 2000


def AddMoney():
    global Money  # 全局声明
    Money = Money + 1


print '原始值', Money
AddMoney()
print '经过函数运算', Money

print '\n模块-----------------------------------------------------------'
# from 1 import 2 加载1模块当中的2函数
import sys

def_list = dir(sys)
print "打印出所有方法", def_list


def printMax(a, b):
    if a > b:
        print '第一个参数', a
    else:
        print '第二个参数', b


printMax(3, 4)  # 传递给函数的参数 比较大小输出较大的
x = 5
y = 7
printMax(x, y)  # 定义函数的参数的值，比较大小


# 局部变量
def my_qq(qq):
    print '初始值：', qq
    qq = 110
    print '后来的值：', qq


qq = 50  # 初始值
my_qq(qq)
print '经过函数后的值会恢复之前的初始的值', qq

# 全局变量
print "\n---------------------------------------------------------------"


def my_qq():
    global qq  # 需要在函数内提前声明
    print '初始值：', qq
    qq = 10
    print '后来的值：', qq


# 一个函数内的代码默认为一个模块 平级

qq = 50
my_qq()  # 经过函数后的值不会恢复
print '经过函数后的值会保存函数内声明全局的值', qq


# 默认参数
def say(message, times=1):
    print message * times


say('Hello ')
say('World ', 5)


# 不写即为参数默认，写了之后以自己的为准
# def say 里面的message 为形式参数 times 为默认参数
# say('hello') 中的hello 是实际参数

def func(a, b=5, c=10):  # 定义名字的参数一般叫做关键参数
    print '一是', a, '二是', b, '三是', c


func(3, 7)
func(25, c=24)
func(c=50, a=100)


# 不同的比较测试

def maximum(x, y):
    '''这是一个最大值计算的测试函数'''
    if x > y:  # 比较大小 返回值
        return x
    else:
        return y


print maximum(2, 3)
print maximum.__doc__
'''DocStrings
   Python有一个很奇妙的特性，称为 文档字符串 ，
   它通常被简称为 docstrings 。DocStrings是一个 重要的工具，由于它帮助
   你的程序文档更加简单易懂，你应该尽量使用它。你甚至可以在程序 运行的时候，
   从函数恢复文档字符串!'''

print '\n 内建函数 ----------------------------------------------------'

print '\n lambda   ---------------------------------------------------'
# lambda 一种快速定义单行的最小函数
MAXIMUM = lambda x, y: (x > y) * x + (x < y) * y
MINIMUM = lambda x, y: (x > y) * y + (x < y) * x
a = 10
b = 20
print 'The largar one is %d' % MAXIMUM(a, b)
print 'The lower one is %d' % MINIMUM(a, b)

print '\n 装饰器   ----------------------------------------------------'


# 函数前面增加 @函数名  意味着此函数需要用@函数进行装饰处理
def a(b):
    print b


def b():
    pass


a(b)
print '使用装饰器输出'


# 装饰器版
def a(b):
    print(b)


@a  # 定义 a 函数为 b 函数的装饰器
def b():
    pass


b  # 等于 a(b)()

print  '\n 闭包    ----------------------------------------------------'


# 函数当中嵌套一个函数 调用上层函数的参数 返回一个函数 返回的函数一直会调用上级函数的参数进行工作
def hello_config(fix):
    def hello(name):
        print fix, name

    return hello


s = hello_config('你好')
s('Depth')
print s.__name__

b = hello_config('你们好')
b('We')
print b.__name__
print '\ncase2'


def f():
    global n
    n = 0

    def add():  # 子函数，每次给父函数 +1 | 闭包
        # nonlocal n
        global n
        n = n + 1
        print(n)

    return add


'''nonlocal是Python3新增的作用域关键词。Python对闭包的支持一直不是很完美，
在 Python2 中，闭包函数可以读取到父级函数的变量，但是无法修改变量的值，为此，
我们经常要把变量声明为global全局变量，这样就打破了闭包的性质。为了解决这个问题，
Python3 引入了nonlocal，如上例代码，我们使用声明了nonlocal n之后，就可以正常操作'''

add = f()
add()
add()
add()

print '\n 生成器   ----------------------------------------------------'


# 生成器是一种惰性的序列，如果我们需要创建一个 0～1000000000 的序列，
# 这样大的序列创建出来会占用比较多的内存，生成器就是为了解决这样的问题，
# 可以让我们边使用边生成数据，在Python中，生成器的构造，依靠函数来完成。
# 生成器
def f():
    for x in range(10):
        yield x  # 返回并记录函数状态


# next
f = f()
print next(f)  # 每调用一次next，就执行一次yield | 依靠这种需要才生产的工作机制，大大的节省资源
print next(f)
print next(f)
print '间隔'

# for next
for x in range(7):  # 上面已经输出过3个了，总量为10
    print next(f)  # 超出则会出现异常
