#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import json
import os
import torndb

from tornado.web import RequestHandler,url,StaticFileHandler
from tornado.options import define, options

define("port", default=8001, type=int)

class BaseHandler(RequestHandler):
	def prepare(self):
        	pass

	def write_error(self,status_code, **kwargs):
        	pass 

	def set_default_headers(self):
        	pass 


    	def initialize(self):
        	pass 

    	def on_finish(self):
    		pass 


class  IndexHandler(BaseHandler):
	def get(self):
        	# self.write("aaa")
        	ret = self.application.db.get("select ui_name from it_user_info where ui_user_id=1")
        	self.write(ret["ui_name"])

class  InsertHandler(BaseHandler):
    def post(self):
            name = self.get_argument("name")
            passwd =self.get_argument("passwd")
            mobile = self.get_argument("mobile")
            sql = "insert into it_user_info(ui_name, ui_passwd, ui_mobile) values (%(name)s,%(passwd)s,%(mobile)s)"
            try:
            	user_id = self.application.db.execute(sql,name=name,passwd=passwd,mobile=mobile)
            except Exception as e:
                print e 
                return self.write("DB error:%s" %e)
            self.write(str(user_id))

class HouseHandler(BaseHandler):
    def get(self):
    	user_id = self.get_argument("uid")
    	sql = "select ui_name,ui_mobile,hi_name,hi_address,hi_price from it_user_info inner join it_house_info on ui_user_id=hi_user_id where ui_user_id=%s"
        try:
           ret = self.application.db.query(sql,user_id)
        except Exception as e:
           return self.write({"error":1, "errmsg":"db error","data":[]})
	houses = []
        print type(ret)
	if ret:
	   for l in ret:
	      house = {
			"uname":l["ui_name"],
			"mobile":l["ui_mobile"],
			"hname":l["hi_name"],
			"address":l["hi_address"],
			"price":l["hi_price"],
	      } 
	      houses.append(house)
        self.write({"error":0,"errmsg":"OK","data":houses})
          

class Application(tornado.web.Application):
	def __init__(self, *args, **kwargs):
	        super(Application,self).__init__(*args,**kwargs)
	        self.db = torndb.Connection(
	           host="127.0.0.1",
	           database="itcast",
	           user="root",
	           password="123456"
	 		)
          
if __name__ == '__main__':
 	tornado.options.parse_command_line()
 	current_path = os.path.dirname(__file__)
 	settings = dict(
        static_path=os.path.join(current_path,"static"),
 		template_path=os.path.join(current_path,"template"),
 		debug=True,
 	)
 	# app = tornado.web.Application([
  #           (r"/", IndexHandler),
 	#     ], **settings)
 	# app.db = torndb.Connection(
  #          host="127.0.0.1",
  #          database="itcast",
  #          user="root",
  #          password="123456"
 	# 	)
 	app = Application([
            (r"/", IndexHandler),
            (r"/insert", InsertHandler),
            (r"/house", HouseHandler),
 	    ], **settings)
 	http_server = tornado.httpserver.HTTPServer(app)
 	http_server.listen(options.port)
 	tornado.ioloop.IOLoop.current().start()
