#!/usr/bin/env python
# -*- coding: utf-8 -*-

data = 110


def main():
    print  "data", data


if __name__ == '__main__':
    main()

'''
放入if name的值只是被当前文件引用，以第三方模块加载或者执行的时候不会被调用
如果代码是被直接运行的，则代码被运行，如果模块是被导入的，则代码块不被运行。
'''
