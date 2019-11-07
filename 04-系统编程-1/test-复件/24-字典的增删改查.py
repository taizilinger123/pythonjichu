#!/usr/bin/env python
# -*- coding:utf-8 -*-
infor = {"name":"banzhang"}
infor["age"] = 18   #增加
infor['QQ'] = 10086
infor['QQ'] = 10010 #修改
infor
del  infor['QQ']    #删除
infor
infor.get("QQ")     #查找
infor.get("name")
infor.get("age")