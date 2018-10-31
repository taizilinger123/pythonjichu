#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Test(object):
    def __init__(self):
        self.__num = 100

    def setNum(self, newNum):
        self.__num = newNum

    def getNum(self):
        return self.__num

t = Test()
# print(t.__num)
# t.__num = 200

print(t.getNum())
t.setNum(50)
print(t.getNum())

# if_ = 100   #关键字冲突