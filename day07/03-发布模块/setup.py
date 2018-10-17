#!/usr/bin/env python
# -*- coding:utf-8 -*-

from distutils.core import setup

setup(name="dongGe", version="1.0", description="dongGe's module", author="dongGe", py_modules=['TestMsg.sendmsg', 'TestMsg.recvmsg'])


#python3  setup.py  build
#python3  setup.py  sdist
#打包完成会生成dongGe-1.0.tar.gz文件

#解压用包
# tar  -zxvf   dongGe-1.0.tar.gz
# cd   dongGe-1.0
# python3  setup.py  install
# 然后在任何位置就可以用了
# ipthon3
# import TestMsg
# TestMsg.sendmsg.test1()