#!/usr/bin/env python
# coding=utf-8
#  _init__.py 用于标识当前文件夹是一个包。
# 文件下下必须存在可以为空，这样在上层的文件就可以调用文件夹内的模块

'''
test.py
package_boom
|-- __init__.py
|-- boom1.py
|-- boom2.py
结构

调用方法 test.py
from package_boom.boom1 import boom1
from package_boom.boom2 import boom2
'''

# __init__ 包文件  如何导入
# from 路径.模块 import 函数
# imp.reload 模块重载