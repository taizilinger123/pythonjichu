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
	def get(self):
		self.write("hello itcast1<br/>")
		self.write("hello itcast2<br/>")
		self.write("hello itcast3<br/>")

if __name__ == '__main__':
	tornado.options.parse_command_line()
	app = tornado.web.Application([
		     (r"/", IndexHandler),
		],
		debug=True)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.current().start()
