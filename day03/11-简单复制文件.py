#!/usr/bin/env python
# -*- coding:utf-8 -*-

import  os 
s = '/home/sige/test5/test5/urls.py'
filename = s[len(os.path.dirname(s))+1:]
file1 = open(filename,"r")
file2 = open("file1name","w")

s = file1.read()
w = file2.write(s)

file1.close()
file2.close()
