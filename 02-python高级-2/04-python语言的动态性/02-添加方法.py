#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Person(object):
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge

    def eat(self):
        print("-----%s正在吃----"%self.name)

def run(self):
    print("-----%s正在跑----"%self.name)

p1 = Person("p1", 10)
p1.eat()
p1.run = run
p1.run()#虽然p1对象中run属性已经指向了11行的函数，但是这句代码还不正确
        #因为run属性指向的函数是后来添加的，即p1.run()的时候，并没有把
        #p1当做第1个参数，导致了第11行的函数调用的时候，出现缺少参出现缺少参数的问题

# class P(object):
#     def __init__(self, newName):
#         self.name = newName
#
# p1 = P("p1")
# p1.name
# Out[136]: 'p1'
#
#
# def run(self):
#     print("----%s在跑---" % self.name)
#
#
# p1.run = run
# p1.run()
# TypeError: run()
# missing 1 required positional argument: 'self'
# import types
# help(types.MethodType)
# class method in module builtins:
#     class method(object)
#         | method(function, instance)
#         |
#         | Create
#         a
#         bound
#         instance
#         method
#         object.
#         |
#         | Methods
#         defined
#         here:
#         |
#         | __call__(self, /, *args, ** kwargs)
#         | Call
#         self as a
#         function.
#         |
#         | __delattr__(self, name, /)
#         | Implement
#         delattr(self, name).
#         |
#         | __eq__(self, value, /)
#         | Return
#         self == value.
#         |
#         | __ge__(self, value, /)
#         | Return
#         self >= value.
#         |
#         | __get__(self, instance, owner, /)
#         | Return
#         an
#         attribute
#         of
#         instance, which is of
#         type
#         owner.
#         |
#         | __getattribute__(self, name, /)
#         | Return
#         getattr(self, name).
#         |
#         | __gt__(self, value, /)
#         | Return
#         self > value.
#         |
#         | __hash__(self, /)
#         | Return
#         hash(self).
#         |
#         | __le__(self, value, /)
#         | Return
#         self <= value.
#         |
#         | __lt__(self, value, /)
#         | Return
#         self < value.
#         |
#         | __ne__(self, value, /)
#         | Return
#         self != value.
#         |
#         | __new__(*args, **kwargs)
#         from builtins.type
#         | Create and
#         return a new object.See  help(type) for accurate signature.
#             |
#             | __reduce__(...)
#             | helper

#         p1
#         Out[142]: < __main__.P  at  0x455d128 >
#         types.MethodType(run, p1)
#         Out[143]: < bound  method run  of < __main__.P  object  at 0x000000000455D128 >>
#         p1.run = types.MethodType(run, p1)
#         p1.run()
#         ----p1在跑 - --
#         p1
#         Out[146]: < __main__.P  at  0x455d128 >
#
#         def eat(self):
#             print("----%s在吃----" % self.name)
#
#         p1.eat = types.MethodType(eat, p1)
#         p1.eat()
#         ----p1在吃 - ---
# xxxxx = types.MethodType(eat, p1)
# xxxxx()
# ----p1在吃----
# @staticmethod
# def test():
#     print("-----static method-----")
#
# P.test = test
# P.test()
# -----static method ----
# P.xx = test
# P.xx()
# -----static method ----


# @classmethod
# def printNum(cls):
#     print("------class method----")
#
# P.printNum = printNum
# P.printNum()
# class ------method----

# dir(p1)
# Out[160]:
# ['__class__',
#  '__delattr__',
#  '__dict__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__gt__',
#  '__hash__',
#  '__init__',
#  '__le__',
#  '__lt__',
#  '__module__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__setattr__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  '__weakref__',
#  'eat',
#  'name',
#  'printNum',
#  'run',
#  'test',
#  'xx']
# p2 = P("p2")
# p2.age = 10
# p2.addr = "beijing"
# p2.xxx = "uweghwghgwsjgfjs"

# class Person(object):
#     __slots__ = ("name")
#
# p = Person()
# p.name = "dfdfd"
# p.age = 10  #必须是__slots__ = ("name")这里面有的，不然会报错
# AttributeError: 'Person' object has no attribute 'age'
