#coding=utf-8

from pymongo import *

#获得客户端，建立连接
client=MongoClient('mongodb://py3:123@localhost:27017/py3')
#切换数据库
db=client.py3
#获取集合
stu=db.stu

#增加
#s1=stu.insert_one({'name':'张三丰'})

#修改
# stu.update_one({'name':'张三丰'},{'$set':{'name':'abc'}})

#删除
# stu.delete_one({'name':'abc'})

#查询
cursor=stu.find({'age':{'$gt':20}}).sort('_id',-1).skip(1).limit(1)
for s in cursor:
    print(s['name'])

