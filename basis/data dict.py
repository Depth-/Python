#!/usr/bin/env python
# coding=utf-8  指定 不指定会报错
#  基本分类  列表   元组    字典
#  常用的数据类型有7种  数字 字符串 列表 元组 字典 集合
#  下面讲 三种 括号代表的区别

print '[] 列表 的说明 可修改 可添加------------------------------------------'
shoplist = ['apple', 'mango', 'carrot', 'banana']
#定义一个列表
print '我有', len(shoplist),"内容"
for item in shoplist:
    print item + "循环输出"

shoplist.append('rice')      # 增加内容
print '现在具有的内容  ', shoplist

shoplist.sort()
print '排序', shoplist
print '单独取出一个内容', shoplist[0]

olditem = shoplist[0]
del shoplist[0]     #删除列表内第一个
print '删除一个内容',olditem
print '剩下的内容', shoplist


print '\n() 元组 的说明 不可修改 ------------------------------------------'
zu = ('1', '2', '3')
print '几个内容', len(zu)

new_zu = ('4', '5', zu)  #内容包括
print '新加入的视为一个内容 ', len(new_zu)

print '全部的内容', new_zu
print '取一个内容', new_zu[2]
print '取内容当中的内容', new_zu[2][2]     # 元组内的元组数据



print '\n{} 字典 的说明 不可修改 ------------------------------------------'
zd={ 'one' : '123',
     'two' : '456',
     'sun'  : '789',
     'li'   : '1011' }
print "输出的值%s" %zd['one']
print "Tips：print语可以跟着%符号的字符。这些字符具备定制的功能。\n"     \
      "定制让输出满足某种特定的格式。定制可以是%s表示字符 或%d表示整数。\n" \
      "组必须按照相同的顺序来 对应这些定制。%s 定制后面%开头的输出"

print "My name is %s and weight is %d kg!" % ('Zara', 21)
#用法是将一个值插入到一个有字符串格式符 %s 的字符串中

zd['three'] = '1111'   # 增加赋予一个值
del zd['li']           # 删除一个

print '\n其中的内容%s\n' %len(zd)
for name, zhi in zd.items():     #循环名字和值两个字段来自zd的值对
    print 'name %s zhi %s' %(name, zhi)
if 'two' in zd:
    print "\n two's %s" %zd["two"]


print ' \n序列的说明 ----------------------------------------------------'

list00 = ['one', 'two', 'three', 'for']

print 'is 0',list00[0]
print 'is 1',list00[1]
print 'is 2',list00[2]
print 'is 3',list00[3]
print 'is -1',list00[-1]
print 'is -2',list00[-2]
print 'is 1 和 3',list00[1:3]     # []切片中的数据 是从开始位开始，结束位结束,结束位会排斥在切片之外
print 'is 2',list00[2]            # 输出
print 'is 1 全部',list00[1:]       # 从1开始的全部
print 'is 1 到 -1',list00[1:-1]    # 平级的 -1 == 3 按照顺序
print '全部',list00[:]             # 全部
print "具体的值\n -1代表从后置未开始  0代表从头开始"

print '\n字符串的方法 ----------------------------------------------------'
# [1:2:3] 头：尾：间隔
# 字符串的切片对比
'''
h    e   l  l  o     w  o  r  l  d
0    1   2  3  4  5  6  7  8  9  10
-11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
'''


name =  "kukudedepth"

if name.startswith('kukude'):
    print 'yes1 '  # 是否是kukude开始
if 'kukude' in name:
    print 'yes2'   # 是否存在
if name.find('depth')!=-1:
    print 'yes3'   # 查找指定字符串在另一个字符串的位置或返回-1代表找不到

name2 ='_*_'
mylist =['one','two','three']
print name2.join(mylist)
# join分割符，循环加入字符串与列表内容


'''
更详细的对比内容说明----------------------------------------------------'
列表
'''
list01 = ['runoob', 786, 2.23, 'john', 70.2]
list02 = [123, 'john']

# 列表截取
print list01[0]   #从头
print list01[-1]  #从尾
print list01[0:3] #切片

# 列表重复
print list01 * 2

# 列表组合
print list01 + list02

# 获取列表长度
print len(list01)

# 删除列表元素
del list02[0]
print list02

# 元素是否存在于列表中
print 'john' in list02

# 迭代
for i in list01:
    print i

# 比较两个列表的元素
print cmp(list01, list02)

# 列表最大/最小值
print max([0, 1, 2, 3, 4])
print min([0, 1])

# 将元组转换为列表
aTuple = (1,2,3,4)
list03 = list(aTuple)
print list03

# 在列表末尾添加新的元素
list03.append(5)
print list03

# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list03.extend(list01)
print list03

# 统计某个元素在列表中出现的次数
print list03.count(1)

# 从列表中找出某个值第一个匹配项的索引位置
print list03.index('john')

# 将对象插入列表
list03.insert(0, 'hello')
print list03

# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print list03.pop(0)
print list03

# 移除列表中某个值的第一个匹配项
list03.remove(1)
print list03

# 反向列表中元素
list03.reverse()
print list03

# 对原列表进行排序
list03.sort()

# 列表解析 迭代到的内容用运算处理
[i * 10 for i in range(10)]



print '元组----------------------------------------------------------'
tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
tu[1][2]["k2"].append("seven")
# 在tu元祖当中第一位置的第二位置的K2字典增加一个
print tu[0]
print tu[1]
print tu[1][2]
print(tu[1][2]["k2"])
# 元组的一级元素不可被修改增加删除但可以修改二级后的。如修改元祖中列表，字典等内容


'''
字典 ----------------------------------------------------
'''
dictionary = {}
flag = 'a'
pape = 'a'
off = 'a'
# 往字典中添加数据
'''
while flag == 'a' or 'c' :
    flag = raw_input("添加或查找单词 ?(a/c)")
    if flag == "a" :                             # 开启
        word = raw_input("输入单词(key):")
        defintion = raw_input("输入定义值(value):")
        dictionary[str(word)] = str(defintion)  # 添加字典 word = defintion
        print "添加成功!"
        pape = raw_input("您是否要查找字典?(a/0)")   #read
        if pape == 'a':
            print dictionary
        else :
            continue
    elif flag == 'c':
        check_word = raw_input("要查找的单词:")  # 检索
        for key in sorted(dictionary.keys()):            # yes
            if str(check_word) == key:
                print "该单词存在! " ,key, dictionary[key]
                break
            else:                                       # no
                off = 'b'
        if off == 'b':
            print "抱歉，该值不存在！"
    else:                               # 停止
        print "error type"
        break
'''

# 计算 1到100 内的总和 和 3 5倍数的总和
num = 0
bei = 0
for i in range(0,101):
    num += i
    if i % 3 == 0 or i % 5 ==0:
        bei +=i
        print "3 5倍数",bei
    print '总倍数',num

print (sum([i for i in range(10) if i % 3 ==0 or i % 5 == 0]))

# 列表表达式
# [expr for iter_var in iterable] 核心语句是for循环  迭代iter对象的所有条目 讲 expr应用于序列的每个成员
# 生成器对象 用圆括号包含列表解析氏是一个生成器表达式，只有在使用的过程中调用才会执行
g =( i for i in range(10) if i % 3 ==0 or i % 5 == 0)
for i in g:
    print i
