#!/usr/bin/env python
# -*- coding:utf-8 -*-
import functools
def user_login_data(f):
	@functools.wraps(f)
	def wrapper(*args, **kwargs):
		return f(*args, **kwargs)
	return wrapper

@user_login_data
def num1():
    print("aaa")

if __name__ == '__main__':
	print(num1.__name__)

