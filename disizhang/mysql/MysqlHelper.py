<<<<<<< HEAD
#coding=utf-8
from MySQLdb import *

class MysqlHelper:
    def __init__(self,host,port,db,user,passwd,charset='utf8'):
        self.host=host
        self.port=port
        self.db=db
        self.user=user
        self.passwd=passwd
        self.charset=charset
    def open(self):
        self.conn=connect(host=self.host,port=self.port,db=self.db,user=self.user,passwd=self.passwd,charset=self.charset)
        self.cursor=self.conn.cursor()
    def close(self):
        self.cursor.close()
        self.conn.close()
    def cud(self,sql,params):
        try:
            self.open()

            self.cursor.execute(sql,params)
            self.conn.commit()

            self.close()

            print('ok')
        except Exception,e:
            print(e.message)
    def all(self,sql,params=[]):
        try:
            self.open()

            self.cursor.execute(sql,params)
            result=self.cursor.fetchall()

            self.close()

            return result
        except Exception,e:
            print(e.message)
=======
#coding=utf-8
from MySQLdb import *

class MysqlHelper:
    def __init__(self,host,port,db,user,passwd,charset='utf8'):
        self.host=host
        self.port=port
        self.db=db
        self.user=user
        self.passwd=passwd
        self.charset=charset
    def open(self):
        self.conn=connect(host=self.host,port=self.port,db=self.db,user=self.user,passwd=self.passwd,charset=self.charset)
        self.cursor=self.conn.cursor()
    def close(self):
        self.cursor.close()
        self.conn.close()
    def cud(self,sql,params):
        try:
            self.open()

            self.cursor.execute(sql,params)
            self.conn.commit()

            self.close()

            print('ok')
        except Exception,e:
            print(e.message)
    def all(self,sql,params=[]):
        try:
            self.open()

            self.cursor.execute(sql,params)
            result=self.cursor.fetchall()

            self.close()

            return result
        except Exception,e:
            print(e.message)
>>>>>>> 4597e8de6d0b674fb3f44a7b50aa59f9c43ad005
