#!/usr/bin/env python
# -*- coding:utf-8 -*-

f = open("设计4s店类-1.py", "w")
f.read() #全部读出来,包括换行\n
f.read(2) #读多少
f.write("hahah")
f.write("\nhah")
f.close()

f = open("code01.py")
f.read() #全部读出来是字符串
f.read(1)
f.readline() #只一行一行读,是字符串
f.readlines() #读出来是列表,每一行当一个元素
f.close()

#文件的定位操作
f = open("code01.py")
f.seek(2,0) #从文件的开头跳2个字节(,0)文件开头读，(,1)文件当前位置读,(,2)文件末尾读
f.readline()
f.read()
f.read()
f.seek(0,0) #再从头开始读
f.read()
f.tell() #获取所在位置
#(-1,0)py2支持,py3不支持负数, 负数表示往左边来,正数表示往右边



