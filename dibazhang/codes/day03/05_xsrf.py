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
    def get(self):
        self.render("index.html")

	def post(self):
            #print self.request.headers["Cookie"]
            self.write("aaaa")


          
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
        	template_path = os.path.join(os.path.dirname(__file__),"template"),
		cookie_secret = "1K6+M14RR+m+EQdZcRNxyzR7EeufSUl8vxt5pYjLTZo=",
		xsrf_cookie = True,
        	debug = True
 	)
 	app = Application([
            (r"/", IndexHandler),
 	    ], **settings)
 	http_server = tornado.httpserver.HTTPServer(app)
 	http_server.listen(options.port)
 	tornado.ioloop.IOLoop.current().start()
