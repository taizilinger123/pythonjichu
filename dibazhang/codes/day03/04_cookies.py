#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import json
import os
import torndb
import time

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
	def post(self):
		# if not self.get_cookie("itcast"):
		#     print self.get_cookie("itcast")
		#     self.set_cookie("itcast","abc",expires=time.mktime(time.strptime("2020-2-11 23:59:59","%Y-%m-%d %H:%M:%S")))
		# else:
                #     self.clear_cookie("itcast")
                #self.set_header("Set-Cookie","itcast=bcd;Path=/")
            #self.set_secure_cookie("itcast","abc")
            self.write('<html><head><title>被攻击的网站</title></head>'
        '<body><h1>此网站的图片链接被修改了</h1>'
        '<img alt="这应该是图片" src="http://127.0.0.1:8000/?f=9000/">'
        '</body></html>')

class   CookieCountHandler(BaseHandler):
    def get(self):
        count = self.get_secure_cookie("page_count")
        #count = self.get_cookie("page_count")
        if not count:
            self.set_secure_cookie("page_count", "1")
            #self.set_cookie("page_count", "1",domain="127.0.0.1:"+str(options.port))
            count = 1
        else:
            count = int(count)
            count += 1
            self.set_secure_cookie("page_count", str(count))
            #self.set_cookie("page_count", str(count),domain="127.0.0.1:"+str(options.port))
        self.write(str(count))

          
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
 		cookie_secret = "1K6+M14RR+m+EQdZcRNxyzR7EeufSUl8vxt5pYjLTZo=",
                debug=True,
 	)
 	app = Application([
            (r"/", IndexHandler),
            (r"/c", CookieCountHandler),
 	    ], **settings)
 	http_server = tornado.httpserver.HTTPServer(app)
 	http_server.listen(options.port)
 	tornado.ioloop.IOLoop.current().start()
