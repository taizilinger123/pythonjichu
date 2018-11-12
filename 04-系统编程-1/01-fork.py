#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
#fork windows里没有
ret = os.fork()
if ret==0:
    while True:
        print("----1----")
        time.sleep(1)
else:
    while True:
        print("-----2-----")
        time.sleep(1)