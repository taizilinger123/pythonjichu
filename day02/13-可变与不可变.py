#!/usr/bin/env python
# -*- coding:utf-8 -*-

# a = 100
# a = "hello"
# a = "world"
# a[0]
# Out[41]: 'w'
# a[0]="W"
# Traceback (most recent call last):
#   File "E:\python35\lib\site-packages\IPython\core\interactiveshell.py", line 2961, in run_code
#     exec(code_obj, self.user_global_ns, self.user_ns)
#   File "<ipython-input-42-9aa676edea01>", line 1, in <module>
#     a[0]="W"
# TypeError: 'str' object does not support item assignment
# a = (11,22,33)
# a[0] = "fffff"
# Traceback (most recent call last):
#   File "E:\python35\lib\site-packages\IPython\core\interactiveshell.py", line 2961, in run_code
#     exec(code_obj, self.user_global_ns, self.user_ns)
#   File "<ipython-input-44-6be77d21f6c2>", line 1, in <module>
#     a[0] = "fffff"
# TypeError: 'tuple' object does not support item assignment
# a = [11,22,33]
# a[0] = "fffff"
# a = {"name":"laowang"}
# a['name'] = "LaoWang"
# a
# Out[49]: {'name': 'LaoWang'}
# infor = {"name":"laowang",100:"haha",3.14:"heihei"}
# infor
# Out[51]: {100: 'haha', 3.14: 'heihei', 'name': 'laowang'}
# infor = {"name":"laowang",100:"haha",3.14:"heihei",(11,22):"sdfsdfsd"}
# infor
# Out[53]: {(11, 22): 'sdfsdfsd', 100: 'haha', 3.14: 'heihei', 'name': 'laowang'}
#可变类型，列表和字典不能做key值
# infor = {"name":"laowang",100:"haha",3.14:"heihei",(11,22):"sdfsdfsd",[11,22]:"hah"}
# Traceback (most recent call last):
#   File "E:\python35\lib\site-packages\IPython\core\interactiveshell.py", line 2961, in run_code
#     exec(code_obj, self.user_global_ns, self.user_ns)
#   File "<ipython-input-54-2d9e8b6830ac>", line 1, in <module>
#     infor = {"name":"laowang",100:"haha",3.14:"heihei",(11,22):"sdfsdfsd",[11,22]:"hah"}
# TypeError: unhashable type: 'list'
