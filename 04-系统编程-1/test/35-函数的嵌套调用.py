#!/usr/bin/env python
# -*- coding:utf-8 -*-
def test1():
    pass

def test2():
    print("------2-1------")
    print("heihei")
    print("------2-1------")

def test3():
    print("------3-1------")
    test2()
    print("------3-2------")

test3()