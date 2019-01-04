#!/usr/bin/env python
# -*- coding:utf-8 -*-

def getAverage(a, b):
    result = a+b
    print("result=%d"%result)
    return result

a = 100
b = 200
c = a+b
ret = getAverage(a, b)
print(ret)

#python3 -m  pdb test1.py
#l---->list 显示当前的代码
#n----->next 向下执行一行代码
#c----->continue继续执行代码
#b------>break 添加断点
#clear--->删除断点
#p------->print打印一个变量的值
#s-------->step进入到一个函数
#a-------->args 打印所有的形参数据
#q-------->quit退出调试
#r--------->return 快速执行到函数的最后一行
#b 7
#c
#l
#b
#clear 1
#l
#n
#l
#c
#s
#l
# p a
# p b
#a
#b
#p result
#n
#p ret
#q

# def code01(a,b):
#     c = a+b
#     return c
# #import pdb
# pdb.run("code01(11,22)")
# s
# l
# a
# q

#import pdb
# def getAverage(a, b):
#     result = a+b
#     print("result=%d"%result)
#     return result
#
# a = 100
# b = 200
# c = a+b
# pdb.set_trace()
# ret = getAverage(a, b)
# print(ret)

# python3 test1.py
# l

#print调试

# python3空格和tab不能混用,推荐使用空格
# python2空格和tab可以混用

# a = 100; b = 200
# pep8 中文

