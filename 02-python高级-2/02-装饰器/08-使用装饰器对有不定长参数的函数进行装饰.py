#!/usr/bin/env python
# -*- coding:utf-8 -*-

def func(functionName):
    print("------func---1--")
    def func_in(*args, **kwargs):#如果a,b没有定义，那么会导致18行的调用失败
        print("------func_in---1--")
        functionName(*args, **kwargs)#如果没有把a,b当做实参进行传递，那么会导致调用15行的函数失败
        print("------func_in---2--")

    print("------func---2--")
    return func_in

@func
def  test(a, b, c):
    print("----code01-a=%d,b=%d,c=%d----"%(a,b,c))

@func
def  test2(a, b, c, d):
    print("----code01-a=%d,b=%d,c=%d,d=%d----"%(a,b,c,d))

test(11,22,33)
test2(11,22,33,44)