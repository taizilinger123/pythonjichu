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
    "code01 function"
    print('I am code01')

# code01()
# print(code01.__doc__)
print(help(test))