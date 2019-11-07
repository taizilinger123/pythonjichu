#!/usr/bin/env python
# -*- coding:utf-8 -*-

def func(functionName):
    print("------func---1--")
    def func_in():
        print("------func_in---1--")
        ret = functionName() #保存返回来的haha
        print("------func_in---2--")
        return ret #把haha返回到20行的调用

    print("------func---2--")
    return func_in

@func
def  test():
    print("----code01-----")
    return "haha"

ret = test()
print("code01 return value is %s"%ret)