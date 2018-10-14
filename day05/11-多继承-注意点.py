#!/usr/bin/env python
# -*- coding:utf-8 -*-
# class Base():经典类
class Base(object): #新式类
    def test(self):
        print("-----Base")

class A(Base):
    def  test(self):
        print("-----A")

class B(Base):
    def  test(self):
        print("-----B")

class C(A,B):
    pass
    # def  test(self):
    #     print("-----C")

c = C()
c.test()
print(c.__mro__)  #打印调用顺序

