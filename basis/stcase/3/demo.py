#!/usr/bin/env python
# coding=utf-8
import random

'''
Her0 bate 0.88

'''
welcome = "欢迎来到英雄无敌"
# 初始参数
list = {'name': 'Depth', 'hp': 100, 'ack': 50, 'dun': 10}
map = ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
msg = ''' a 向 左 d 向 右'''
User_msg = '您的名字：%s  您的血量：%d 您的攻击力：%d 您的防御力：%d' % (list['name'], list['hp'], list['ack'], list['dun'])


def apple(hp): # 苹果与炸弹
    hp += 10
    return hp


def boom(hp):
    hp -= 10
    return hp


event = [apple, boom]


class Hero:
    def __init__(self, name='player', hp=100, ack=10):
        self.name = name
        self.hp = hp
        self.ack = ack
        print '英雄%s已经诞生' % self.name

    def attck(self, name):
        name.hp -= self.ack

    def blood(self):
        pass


class Boss:
    def __init__(self, name='boss', hp=100, ack=20):
        self.name = name
        self.hp = hp
        self.ack = ack
        print '坏蛋%s已经诞生' % self.name


# 正式程序
print welcome
Depth = Hero('Depth')
Boss = Boss('Boss')
print User_msg

# 核心动作
point = 0
while 1:
    map[point] = "*"
    print '你的位置', "".join(map), point
    userinput = raw_input("你的下一步操作:")

    if userinput == 'd' and point < 9:
        map[point] = '#'
        point += 1
    elif userinput == 'a' and point > 0:
        map[point] = '#'
        point -= 1
    elif userinput == 'q' or point == 9:
        print "退出"
        break
    else:
        print msg

    if point == 3:
        list['hp'] = random.choice(event)(list['hp'])
        print '您的名字：%s  您的血量：%d 您的攻击力：%d 您的防御力：%d' % (list['name'], list['hp'], list['ack'], list['dun'])
    elif point == 4:
        list['hp'] = boom(list['hp'])
        print '您的名字：%s  您的血量：%d 您的攻击力：%d 您的防御力：%d' % (list['name'], list['hp'], list['ack'], list['dun'])
    elif point == 7:
        print '你碰到了BOSS,受到了攻击'
        list['hp'] -= Boss.ack
        print '您的名字：%s  您的血量：%d 您的攻击力：%d 您的防御力：%d' % (list['name'], list['hp'], list['ack'], list['dun'])
