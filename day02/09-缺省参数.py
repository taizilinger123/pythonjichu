#!/usr/bin/env python
# -*- coding:utf-8 -*-
def test(a,d,b=22,c=33): #d只能放在前面,(缺省参数,形参)
    print(a)
    print(b)
    print(c)
    print(d)

test(d=11,a=22,c=44)  #这里面的参数只能和def里面参数名一样(命名参数，实参)
