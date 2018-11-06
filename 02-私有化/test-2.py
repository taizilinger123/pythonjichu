#!/usr/bin/env python
# -*- coding:utf-8 -*-
def creatNum():
    print("------start----")
    a,b = 0,1
    for i in range(5):
        print("----1---")
        yield b
        print("----2---")
        a,b = b,a+b
        print("----3---")
    print("------stop----")

#创建了一个生成器对象
a = creatNum()

for num in a:
    print(num)

ret = next(a)    #让a这个生成器对象开始执行,如果是第一次执行,那么就从creatNum的开始部分执行
                #如果是之前已经执行过了,那么就从上一次停止的位置开始执行

ret = next(a)
ret = next(a)
ret = next(a)
ret = next(a)
ret = next(a)
ret = next(a)
ret = next(a)


# def test():
#     i = 0
#     while i < 5:
#         temp = yield i
#         print(temp)
#         i += 1
#
# t = test()
# t.__next__()
# Out[33]: 0
# t.__next__()
# None
# Out[34]: 1
# t.send("haha")
# haha
# Out[35]: 2

# t = test()
# t.send("haha")
# TypeError: can't send non-None value to a just-started generator
# t = test()
# t.send()
# TypeError: send() takes exactly one argument(0 given)
# t.send(None)
# Out[41]: 0
# t.send("haha")
# haha
# Out[42]: 1
# t.__next__()
# None
# Out[43]: 2
#
#
# def test():
#     i = 0
#     while i < 5:
#         if i == 0:
#             temp = yield i
#         else:
#             yield i
#         i += 1
#
# t = test()
# t.send(None)
# Out[46]: 0
# t.send("haha")
# Out[47]: 1
# t = test()
# t.__next__()
# Out[49]: 0
# t.send("haha")
# Out[50]: 1


