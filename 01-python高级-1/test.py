#!/usr/bin/env python
# -*- coding:utf-8 -*-
def test():
    print("-------1------")
    print("-------2------")
####################################
from imp import *
reload(test) #对test模块重新加载
test.test()