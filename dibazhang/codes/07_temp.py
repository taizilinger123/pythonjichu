#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import json
import os

from tornado.web import RequestHandler,url,StaticFileHandler
from tornado.options import define, options

define("port", default=8001, type=int)

class  IndexHandler(RequestHandler):
	def get(self):
		self.write('<a  href="/itcast">itcast</a>')

class ItcastHandler(RequestHandler):
	def get(self):
	    self.write(dict(a=1,b=2))

if __name__ == '__main__':
 	tornado.options.parse_command_line()
 	current_path = os.path.dirname(__file__)
 	app = tornado.web.Application([
            #(r"/", IndexHandler),
            (r"/(.*)", StaticFileHandler,{"path":os.path.join(current_path, "statics/html"),"default_filename":"index.html"}),
            (r"/itcast",ItcastHandler),
 		],
 		static_path=os.path.join(current_path,"statics"),
 		debug=True)
 	http_server = tornado.httpserver.HTTPServer(app)
 	http_server.listen(options.port)
 	tornado.ioloop.IOLoop.current().start()
