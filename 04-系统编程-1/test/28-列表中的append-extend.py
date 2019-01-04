#!/usr/bin/env python
# -*- coding:utf-8 -*-
a = [11,22,33]
b = [44,55]
#a.extend(b) #一个一个加进去
a.append(b)  #b作为一个整体添加到a里
print(a)

# a = a.append(b) #没有结果None
# print(a)
