#!/usr/bin/env python
# coding=utf-8  指定 不指定会报错
# 模块 5.17
import sys
#import hellword
from hellword import bigt



print 'is：'
for i in sys.argv:
    print i
print '\n\nThe PYTHONPATH is', sys.path, '\n'

#加载并且输出sys.path
#pyc 字节编译的文件
#from sys import argv 取模块的某个变量
#import 两者的区别
# import 引用变量需要 模块名.变量名字
# from sys import argv 直接变量名

#使用模块的__name__

if __name__ == '__main__':
    print 'This program is being run by itself'
else:
    print 'I am being imported from another module'
#if __name__ == '__main__': 引用外部模块常量，但不执行其中代码块 详情如下

#程序hello1。py hello2.py

#hello2 文件内容————————————————————
PI = 3.14

def main():
    print "PI:", PI

#main() 定义PI 会有输出
#  运行结果
#  PI: 3.14

# 现在，我们有一个 hello1.py 文件，用于计算圆的面积，该文件里边需要用到 hello2.py
# 文件中的 PI 变量，那么我们从 hello2.py 中把 TI 变量导入到 hello1.py 中：

# from hello2 import PI

def calc_round_area(radius):
    return TI * (radius ** 2)

def main():
    print "round area: ", calc_round_area(2)

# main()
#运行 hello1.py，输出结果：

#  PI: 3.14
#  round area:  12.56
# 可以看到，const 中的 main 函数也被运行了，实际上我们是不希望它被运行，
# 提供 main 也只是为了对常量定义进行下测试。
# 这时，if __name__ == '__main__' 就派上了用场。把 hello1.py 改一下：

PI = 3.14

def main():
    print "PI:", PI

if __name__ == "__main__":
    main()
#然后再运行 hello1.py，输出如下：
#  round area:  12.56
#  再运行下 hello2.py，输出如下：
#  PI: 3.14
#结果  定时也相当于定义程序的主程序入口
# 一句话解释
# if __name__ == '__main__': 的作用就是控制这两种情况执行代码的过程，
# 在if __name__ == '__main__': 下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行，
# 而import到其他脚本中是不会被执行的。

