#!/usr/bin/env python
# -*- coding:utf-8 -*-

def test():
    a = 11
    b = 22
    c = 33

    #第1种,用一个列表来封装3个变量的值
    #d = [a,b,c]
    #return d

    #第2种
    #return [a.b,c]

    #第3种
    #return (a,b,c)
    return a,b,c

num = test()
print(num)