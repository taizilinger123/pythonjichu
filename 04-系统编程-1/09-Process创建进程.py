#!/usr/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Process
import time
def test():
    for i in range(5):
        print("-----code01-----")
        time.sleep(1)

p = Process(target=test)
p.start()#让这个进程开始执行test函数里的代码
