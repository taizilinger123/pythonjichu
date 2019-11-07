#!/usr/bin/env python
# -*- coding:utf-8 -*-

a = 4
b = 5

#第1种
# c = 0
# c = a
# a = b
# b = c
# print("a=%d,b=%d"%(a,b))

#第2种
# a = a+b
# b = a-b
# a = a-b
# print("a=%d,b=%d"%(a,b))

#第3种
a,b = b,a
print("a=%d,b=%d"%(a,b))
