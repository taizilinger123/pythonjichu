#!/usr/bin/env python
# -*- coding:utf-8 -*-
def test(a,b,c=33,*args,**kwargs):#在定义的时候 *,**用来表示后面的变量有特殊功能
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


#code01(11,22,33,44,55,66,77,task=99,done=89)  #用法:task=99,done=89都是给**kwargs

A = (44,55,66)
B = {"name":"laowang","age":18}

test(11,22,33,*A,**B)#在实参中*,**表示对元祖/字典进行拆包,*A=*args, **B=**kwargs

