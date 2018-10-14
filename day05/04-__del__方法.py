#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Dog:
    def __del__(self):
        print("-----英雄over------")

dog1 = Dog()
dog2 = dog1

del dog1
del dog2
print("=============")

# 测量一个对象的引用计数的方式
# import sys
# #sys.getrefcount()
# class T:
#      pass
# t = T()
# sys.getrefcount(t)
# Out[76]: 2
# tt = t
# sys.getrefcount(t)
# Out[78]: 3
# del tt
# sys.getrefcount(t)
# Out[80]: 2
# del t
# sys.getrefcount(t)
# Traceback (most recent call last):
#   File "E:\python35\lib\site-packages\IPython\core\interactiveshell.py", line 2961, in run_code
#     exec(code_obj, self.user_global_ns, self.user_ns)
#   File "<ipython-input-82-52ae7bd4c8d6>", line 1, in <module>
#     sys.getrefcount(t)
# NameError: name 't' is not defined
