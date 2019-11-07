#!/usr/bin/env python
# -*- coding:utf-8 -*-
#python2  要加#coding=utf-8
def test(a,b,func):
    result = func(a,b)
    return result
#func_new = input("请输入一个匿名函数:")
func_new = input("请输入一个匿名函数:")
func_new = eval(func_new)  #lambda x,y:x+y
num = test(11,22,func_new)
print(num)
