#!/usr/bin/env python
# -*- coding:utf-8 -*-
i = 1
while i<=5:
    j = 1
    while j<=i:
        print("*",end="")
        j+=1
        #break
        continue
    print("")#换行
    i+=1
    break

a = "lao"
b = "wang"
c = a + b
print(c)
f = "====%s===="%(a+b)
print(f)