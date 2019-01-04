#!/usr/bin/env python
# -*- coding:utf-8 -*-

# nums = [1123,12,3,12,31,23,1,24123,123,11231]
# nums.sort()
# nums
# Out[57]: [1, 3, 12, 12, 23, 31, 123, 1123, 11231, 24123]
# nums.sort(reverse=True)
# nums
# Out[59]: [24123, 11231, 1123, 123, 31, 23, 12, 12, 3, 1]
# nums.reverse()
# nums
# Out[61]: [1, 3, 12, 12, 23, 31, 123, 1123, 11231, 24123]
def test1(a, b):
    return a+b
result1 = test1(11,22)

test2 = lambda a,b:a+b
result2 = test2(11,22)#调用匿名函数

print("result1=%d,result2=%d"%(result1, result2))