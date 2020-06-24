#!/usr/bin/env python
# -*- coding:utf-8 -*-
def func_arg(arg):
    def func(functionName):
        def func_in():
            print("----记录日志-arg=%s--"%arg)
            if arg=="heihei":
                functionName()
                functionName()
            else:
                functionName()
        return func_in
    return func

#1.先执行func_arg("heihei")函数，这个函数return的结果是func这个函数的引用
#2.@func
#3.使用@func对test进行装饰
@func_arg("heihei")  #test=func_arg("heihei")(test)=func
def  test():
    print("----code01----")

#带有参数的装饰器，能够起到在运行时，有不同的功能
@func_arg("haha")
def  test2():
    print("----test2----")

test()     #test()=func()
test2()