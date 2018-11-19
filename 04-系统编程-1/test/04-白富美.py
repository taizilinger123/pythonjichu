#!/usr/bin/env python
# -*- coding:utf-8 -*-

color = input("你白吗?")#白 或者 黄
money = int(input("请输入你的财产总和:"))#输入1000
beautiful = input("你美吗?")#美 或者 普通

# if 白 并且 富 并且 美:
#if  白 and 富 and 美:
if color == "白" and money>10000000 and beautiful=="美":
    #ctrl+a在ubantu会自动补全
    print("白富美......")
    print("好羡慕......")
else:
    print("矮矬穷......")
#下面的代码都会执行
print("矮矬穷......")
print("矮矬穷......")
print("矮矬穷......")