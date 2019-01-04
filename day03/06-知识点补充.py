#!/usr/bin/env python
# -*- coding:utf-8 -*-

#a = 100
a = [100]

def test(num):
    #num+=num
    num = num+num#====>[100] + [100] ====>[100,100]
    print(num)
test(a)

print(a)