#coding:utf-8
from MysqlHelper import MysqlHelper
from hashlib import sha1

#接收用户输入
name=raw_input("请输入用户名：")
pwd=raw_input("请输入密码：")

#对密码加密
s1=sha1()
s1.update(pwd)
pwd2=s1.hexdigest()

#根据用户名查询密码
sql='select passwd from users where name=%s'
helper=MysqlHelper('sige1',3306,'python3','root','123456')
result=helper.all(sql,[name])

#验证
if len(result)==0:
    print('用户名错误')
elif result[0][0]==pwd2:
    print('登陆成功')
else:
    print('密码错误')
# print(result)
# result[0][0]
# #(('123',),)
##########################################################
# sudo pip install mysql
# https://pypi.python.org/pypi  python和mysql的包
# Connection:尽量晚打开，尽量早关闭
#    connect(host,port,user,passwd,db,charset)
#    cursor()
#      commit
#      close
# Cursor
#    execute()
#    如果执行insert update delete语句时，需要conn.commit()
#      fetchone()
#      fetchall()
#      close

