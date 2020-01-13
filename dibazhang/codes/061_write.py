#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import json

from tornado.web import RequestHandler
from tornado.options import define, options

define("port", default=8001, type=int)

class IndexHandler(RequestHandler):
	def set_default_headers(self):
		self.set_header("Content-Type","application/json")

	def get(self):
		# self.write("hello itcast1<br/>")
		# self.write("hello itcast2<br/>")
		# self.write("hello itcast3<br/>")
		stu = {
		     "name":"zhangsan",
		     "age":24,
		     "gender":1,
		}
		stu_json = json.dumps(stu)
		self.write(stu_json)
		#self.write(stu)
		#self.set_header("Content-Type", "application/json; charset=UTF-8")
    def  post(self):
        stu = {
		     "name":"zhangsan",
		     "age":24,
		     "gender":1,
		}
		stu_json = json.dumps(stu)
		self.write(stu_json)

if __name__ == '__main__':
	tornado.options.parse_command_line()
	app = tornado.web.Application([
		     (r"/", IndexHandler),
		],
		debug=True)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.current().start()
