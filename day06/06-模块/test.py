#!/usr/bin/env python
# -*- coding:utf-8 -*-

import  xxxx

class ClassName(object):
    """docstri ng  for  ClassName"""
    def  __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg

def  xxx():
      pass

def  main():
    pass

if  __name__  == '__main__':
    main()

# super(test, self).__init__()
# 是什么意思
# 首先找到test的父类（比如是类A），然后把类test的对象self转换为类A的对象，然后“被转换”的类A对象调用自己的__init__函数
