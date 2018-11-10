#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib
m = hashlib.md5()
m = hashlib.sha256()
print(m)
m.update('itcast')
print(m.hexdigest)

# import hashlib
# t = hashlib.md5()
# t.update(b"dongGe")
# t.hexdigest()
# Out[68]: 'be403adce5f5b5b376ecd8f9efa7ec1d'
# t.update(b"dongGegsfgdfsdggfpassword=gsidgfs")
# t.hexdigest()
# Out[70]: '7c95f3696d031bfce1d7d479cd94698f'
