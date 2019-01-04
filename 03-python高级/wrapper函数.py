#!/usr/bin/env python
# -*- coding:utf-8 -*-
def note(func):
    "note function"
    def wrapper():
        "wrapper function"
        print('note something')
        return func()
    return wrapper

@note
def test():
    "code01 function"
    print('I am code01')

print(help(test))