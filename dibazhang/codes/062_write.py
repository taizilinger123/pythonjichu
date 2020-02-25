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
            self.set_header("Itcast","Python")
   
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
		#self.set_header("Content-Type", "text/html")
                self.set_header("Itcast","CPP")
                self.set_status(444, "itcast error")

        def post(self):
                stu = {
		     "name":"zhangsan",
		     "age":24,
		     "gender":1,
		}
		stu_json = json.dumps(stu)
		self.write(stu_json)

#class MainHandler(RequestHandler):
#    def get(self):
#        err_code = self.get_argument("code", None) # 注意返回的是unicode字符串，下同
#        err_title = self.get_argument("title", "")
#        err_content = self.get_argument("content", "")
#        if err_code:
#            self.send_error(err_code, title=err_title, content=err_content)
#        else:
#            self.write("主页")
#
#    def write_error(self, status_code, **kwargs):
#        self.write(u"<h1>出错了，程序员GG正在赶过来！</h1>")
#        self.write(u"<p>错误名：%s</p>" % kwargs["title"])
#        self.write(u"<p>错误详情：%s</p>" % kwargs["content"])

if __name__ == '__main__':
	tornado.options.parse_command_line()
	app = tornado.web.Application([
		     (r"/", IndexHandler),
		],
		debug=True)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.current().start()
