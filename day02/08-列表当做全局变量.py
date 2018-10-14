#!/usr/bin/env python
# -*- coding:utf-8 -*-
#列表和字典当做全局变量，函数里面的global可以省略
nums = [11,22,33]
infor = {"name":"laowang"}

def test():
    #for num in nums:
    #    print(num)

    nums.append(44)
    infor['age'] = 18

def test2():
    print(nums)
    print(infor)

test()
test2()
