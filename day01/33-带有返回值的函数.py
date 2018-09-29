#!/usr/bin/env python
# -*- coding:utf-8 -*-
def  get_wendu():
     wendu = 22
     print("当前的室温是:%d"%wendu)
     return wendu

def  get_wendu_huashi(wendu):
    print("--------4-------")
    wendu = wendu + 3
    print("--------5-------")
    print("当前的温度(华氏)是:%d"%wendu)
    print("--------6-------")

print("--------1-------")
result = get_wendu()
print("--------2-------")
get_wendu_huashi(result)
print("--------3-------")

# E:\python35\python35.exe E:/pythonjichu/33-带有返回值的函数.py
# Traceback (most recent call last):
#   File "E:/pythonjichu/33-带有返回值的函数.py", line 17, in <module>
#     get_wendu_huashi()
#   File "E:/pythonjichu/33-带有返回值的函数.py", line 9, in get_wendu_huashi  #报错看最后一个行数字,其他不用看
#     wendu = wendu + 3
# UnboundLocalError: local variable 'wendu' referenced before assignment
# --------1-------
# 当前的室温是:22
# --------2-------   #二分法定位错误在哪更快
# --------4-------