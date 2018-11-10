#!/usr/bin/env python
# -*- coding:utf-8 -*-
import  functools
def note(func):
    "note function"
    @functools.wraps(func)
    def wrapper():
        "wrapper function"
        print('note something')
        return func()
    return wrapper

@note 
def test():
    "test function"
    print('I am test')

# test()
# print(test.__doc__)
print(help(test))