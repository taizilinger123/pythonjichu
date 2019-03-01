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
    def one(self,sql,params=[]):
        try:
           self.open()

           self.cursor.execute(sql,params)
           result=self.cursor.fetchone()

           self.close()

           return result
        except Exception,e:
           print(e.message)

