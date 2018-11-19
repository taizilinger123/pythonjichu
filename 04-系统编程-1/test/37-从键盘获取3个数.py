#!/usr/bin/env python
# -*- coding:utf-8 -*-
def sum_3_nums(a, b, c):   #形参
    result = a+b+c
    #print("%d+%d+%d=%d"%(a,b,c,result))
    return  result

def  average_3_nums(a1, a2, a3): #形参 (接收实参的参数)
    result = sum_3_nums(a1, a2, a3) #实参
    result = result/3 #result/=3
    print("平均值是:%d"%result)

#1.获取3个数值
num1 = int(input("第1个值:"))
num2 = int(input("第2个值:"))
num3 = int(input("第3个值:"))

#sum_3_nums(num1, num2, num3)
average_3_nums(num1, num2, num3) #实参