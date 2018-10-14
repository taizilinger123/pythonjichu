#!/usr/bin/env python
# -*- coding:utf-8 -*-
f = open("xxx.txt","r") #和这个相等f = open("xxx.txt")

content = f.read()
print(content)

f.close()