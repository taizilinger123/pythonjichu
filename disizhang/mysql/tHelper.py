#coding=utf-8
from MysqlHelper import MysqlHelper

#修改
# name=raw_input("请输入学生姓名")
# id1=raw_input("请输入学生编号")
#
# sql='update students set name=%s where id=%s'
# params=[name,id1]
#
# sqlhelper=MysqlHelper('sige1',3306,'python3','root','123456')
# sqlhelper.cud(sql,params)

#查询
sql='select id,name from students where id<5'
sqlhelper=MysqlHelper('sige1',3306,'python3','root','123456')
result=sqlhelper.all(sql)
print(result)
