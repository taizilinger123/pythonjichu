#!/usr/bin/env python
# -*- coding:utf-8 -*-
# a = (11,22,33,11,22,33)
# a
# Out[15]: (11, 22, 33, 11, 22, 33)
# b = [11,22,33,11,22,33]
# b
# Out[17]: [11, 22, 33, 11, 22, 33]
# c = {11,22,33,11,22,33}
# c
# Out[19]: {11, 22, 33}
# type(a)
# Out[20]: tuple
# type(b)
# Out[21]: list
# type(c)
# Out[22]: set

a = [11,22,33,44,11,22,33]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)

f = set(a)
print(f)
b = list(f)
print(b)

b = {11,22,33,44}
help(b.add)
b.add(55)
b.add(55) #集合去重复，第二次添加一样的不成功
b.remove(22)
b.pop(11)
b.update(33,66)
