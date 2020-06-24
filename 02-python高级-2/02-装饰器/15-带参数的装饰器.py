#!/usr/bin/env python
# -*- coding:utf-8 -*-

def get_parameter(*args,**kwargs):  # 工厂函数，用来接受@get_parameter('index.html/')的'index.html/'
    def log_time(func):
        def make_decorater():
            print(args,kwargs)
            print('现在开始装饰')
            func()
            print('现在结束装饰')
        return make_decorater
    return log_time
 
@get_parameter('index.html/')  ##test=get_parameter('index.html/')(test)=log_time
def test():
    print('我是被装饰的函数')
    # return num+1
 
test()  # test()=make_decorater()