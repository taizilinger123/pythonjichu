#!/usr/bin/env python
# -*- coding:utf-8 -*-
__all__ = ["test1","Test"]
#作用# from  msgnew  import * 限制这个只能用test1,其他导入就会报错,写谁就只能用谁，其他不能用，用就报错

def  test1():
    print("----test-1-----")

def  test2():
    print("----test-2-----")

num = 100
class Test(object):
    pass