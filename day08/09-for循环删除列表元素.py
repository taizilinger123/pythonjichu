#!/usr/bin/env python
# -*- coding:utf-8 -*-
a = [11,22,33,44,55,66,77]
b = []
 for i in a:
   if i==33 or i==44:
       b.append(i)

b
[33, 44]

for i in b:
   a.remove(i)

a
[11, 22, 55, 66, 77]

