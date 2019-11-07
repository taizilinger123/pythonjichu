#!/usr/bin/env python
# -*- coding:utf-8 -*-
import  os
os.rename("xxx.txt", "yyy.txt")
os.remove("yyy.txt")
os.mkdir("code01") #创建文件夹
os.rmdir("code01") #删除文件夹
f = open("../xxx.txt","w")
f.close()
os.getcwd() #返回当前的绝对路径
os.chdir("../") #改变默认路径
os.listdir("./") #是列表，列出当前所有文件
