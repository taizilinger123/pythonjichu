#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Person(object):
    def __getattribute__(self, obj):
        print("----test-----")
        if obj.startswith("a"):
            return "haha"
        else:
            return self.test

    def test(self):
        print("heihei")

t=Person()
t.a
t.b#会让程序死掉， return self.test因为会又调用__getattribute__(self, obj)方法