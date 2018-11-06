#!/usr/bin/env python
# -*- coding:utf-8 -*-
def createNum():
    print("-----start--------")
    a,b = 0,1
    for i in range(5):
        #print(b)
        print("-----1-----")
        yield b
        print("-----2-----")
        a,b = b, a+b
        print("-----3-----")
    print("-----stop--------")

# a = createNum()
# next(a)

# from test import *
# createNum()
# a = createNum()
# next(a)
# next(a)