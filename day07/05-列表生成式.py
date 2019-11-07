#!/usr/bin/env python
# -*- coding:utf-8 -*-

a = [11,3,43,4,3,423,4,2,34]
# print(a)
# a = []
# i=10
# while i<=77:
#     a.append(i)
#     i+=1
# print(a)

# for i in range(10,78):
#     print(i)

# python2
# range(10) #是列表
# range(10,18)
# range(10,18,2)
# range(10,18,3)
# range(1,10000000) #内存被吃光了
a = [i for i in range(1,18)]
print(a)
b = [11 for i in range(1,18)]
print(b)
c = [i for i in range(10) if i%2==0]
print(c)
d = [i for i in range(3) for j in range(2)]
print(d)
d = [(i,j) for i in range(3) for j in range(2)]
print(d)
e = [(i,j,k) for i in range(3) for j in range(2) for k in range(3)]
print(e)


d = []
for i in range(3):
    for j in range(2):
        d.append((i,j))
print(d)