#!/usr/bin/env python
# -*- coding:utf-8 -*-
# a = [x for x in range(10)]
# a
# Out[84]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = (x for x in range(10))
# b
# Out[86]: < generator
# object < genexpr > at
# 0x0000000004644BA0 >
# for temp in b:
#     print(temp)
#
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# from collections  import Iterable
# isinstance("abc", Iterable)
# Out[89]: True
# isinstance([], Iterable)
# Out[90]: True
# isinstance({}, Iterable)
# Out[91]: True
# isinstance(100, Iterable)
# Out[92]: False
# a = [11,22,33,44]
# next(a)
# Traceback (most recent call last):
#   File "E:\python35\lib\site-packages\IPython\core\interactiveshell.py", line 2961, in run_code
#     exec(code_obj, self.user_global_ns, self.user_ns)
#   File "<ipython-input-94-15841f3f11d4>", line 1, in <module>
#     next(a)
# TypeError: 'list' object is not an iterator
# ----------------------
# from collections  import Iterator
# isinstance([], Iterator)
# Out[96]: False
# isinstance((x for x in range(10)), Iterator)
# Out[97]: True
# a = [11,22,33,44]
# a
# Out[99]: [11, 22, 33, 44]
# type(a)
# Out[100]: list
# iter(a)  #转成迭代器
# Out[101]: <list_iterator at 0x4562198>
# b = iter(a)
# b
# Out[103]: <list_iterator at 0x45621d0>
# next(b)
# Out[104]: 11
-------------------------------------
# def code01():
#     print("----1----")
# code01()
# ----1 - ---
# code01
# Out[107]: < function
# __main__.code01() >
# b = code01
# b
# Out[109]: < function
# __main__.code01() >
# code01()
# ----1 - ---
# b()
# ----1 - ---

