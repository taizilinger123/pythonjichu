#coding=utf-8
from  MySQLdb import *
try:
    name=raw_input("请输入用户名：")
    conn=connect(host='sige1',port=3306,user='root',passwd='123456',db='python3',charset='utf8')
    cursor1=conn.cursor()

    # sql='insert into students(name) values("郭小二")'
    # sql='update students set name="王二小" where id=8'
    # sql='delete  from students where id=9'
    sql='insert into students(name) values(%s)'
    cursor1.execute(sql,[name])

    conn.commit()

    cursor1.close()
    conn.close()
    print('ok')
except Exception,e:
    print(e.message)
