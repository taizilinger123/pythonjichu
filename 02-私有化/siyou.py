#!/usr/bin/env python
# -*- coding:utf-8 -*-
num = 100
_num2 = 200
__num3 = 300

# from siyou import *
# num
# 100
# _num2 #不能用
# __num3 #不能用

# import siyou
# siyou.num
# 100
# siyou._num2
# 200
# siyou.__num3
# 300

# class Test(object):
#     def __init__(self):
#         self.__num = 100
#
# t = Test()
# dir(t)
# Out[81]:
# ['_Test__num',
#  '__class__',
#  '__delattr__',
#  '__dict__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__gt__',
#  '__hash__',
#  '__init__',
#  '__le__',
#  '__lt__',
#  '__module__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__setattr__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  '__weakref__']
# t._Test__num   #t._类名__num
# Out[82]: 100

