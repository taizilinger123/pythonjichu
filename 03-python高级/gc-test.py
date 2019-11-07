#!/usr/bin/env python
# -*- coding:utf-8 -*-
import  gc
class ClassA():
    def __init__(self):
        print('object born,id:%s'%str(hex(id(self))))

def f2():
    while True:
        c1 = ClassA()
        c2= ClassA()
        c1.t = c2
        c2.t = c1
        del c1
        del c2
        gc.collect()#手动清理垃圾回收
#gc.disable()
gc.disable()
f2()

# a = 100
# b = 100
# c = 100
# id(a)
# Out[5]: 1429016112
# id(b)
# Out[6]: 1429016112
# id(c)
# Out[7]: 1429016112
# A = 1000
# B = 1000
# id(A)
# Out[10]: 70088528
# id(B)
# Out[11]: 70088688
# a = "hello"
# b = "hello"
# id(a)
# Out[14]: 14450960
# id(b)
# Out[15]: 14450960
# id(a)
# Out[16]: 14450960
# a = "hello world"
# b = "hello world"
# id(a)
# Out[19]: 74076848
# id(b)
# Out[20]: 74084656
# a = 100
# id(a)
# Out[22]: 1429016112
# del a
# b = 100
# id(b)
# Out[25]: 1429016112
# import gc
# gc.get_count()
# Out[28]: (75, 5, 0)
# gc.get_count()
# Out[29]: (119, 5, 0)
# gc.get_count()
# Out[30]: (143, 5, 0)
# gc.get_threshold()
# Out[31]: (700, 10, 10)
# gc.get_threshold()
# Out[32]: (700, 10, 10)
# gc.get_threshold()
# Out[33]: (700, 10, 10)
# import sys
# a = "hello world"
# sys.getrefcount(a)
# Out[36]: 2
# b =a
# sys.getrefcount(a)
# Out[38]: 3
