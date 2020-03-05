#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import json

from tornado.web import RequestHandler,url
from tornado.options import define, options

define("port", default=8001, type=int)

class IndexHandler(RequestHandler):

	def set_default_headers(self):
            self.set_header("Content-Type","application/json")
            self.set_header("Itcast", "Python")
        def write_error(self, scode, **kwargs):
            self.write("出错了<br/>")
            self.write("标题:%s<br/>" % kwargs.get("err_title", ""))
            self.write("详情:%s<br/>" % kwargs.get("err_content", ""))
        
            """
            err_title=错误标题
            err_content=错误描述
            """
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
	    #err_data = {
		#     "err_content":"abc",
		#     "err_title":"title"
		#}		
		#self.send_error(404,**err_data)
		self.send_error(404,err_content="abc",err_title="title")
		self.set_header("Itcast","CPP")
		self.set_status(404, "itcast error")
		self.redirect(self.reverse_url("itcast_url"))

        def post(self):
                stu = {
		     "name":"zhangsan",
		     "age":24,
		     "gender":1,
		}
		stu_json = json.dumps(stu)
		self.write(stu_json)

class ItcastHandler(RequestHandler):
    def get(self):
        self.write("itcast")

class MainHandler(RequestHandler):
    def prepare(self):
    #判断head Content-Type
    #json_data  body 
    #解析  反序列化
    #放到self中
        if self.request.headers.get("Content-Type","").startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        
    def get(self):
        err_code = self.get_argument("code", None)
        err_title = self.get_argument("title", "")
        err_content = self.get_argument("content", "")
        #print type(err_content)
        print  type(err_title)
        if err_code:
            self.send_error(int(err_code), title=err_title, content="中闻错误")
        else:
            self.write("主页")

    def write_error(self, status_code, **kwargs):
        for key,value in kwargs.items():
            print key, value 
        self.write(u"<h1>出错了，程序员GG正在赶过来！</h1>")
        self.write(u"<p>错误名:%s</p>" % kwargs["title"])
        self.write(u"<p>错误详情:%s</p>" % kwargs["content"].decode("utf-8"))
class InterfaceHandler(RequestHandler):

    def initialize(self):
        print "调用了initialize()"

    def prepare(self):
        print "调用了prepare()"

    def set_default_headers(self):
        print "调用了set_default_headers()"

    def write_error(self, status_code, **kwargs):
        print "调用了write_error()"

    def get(self):
        print "调用了get()"

    def post(self):
        print "调用了post()"
        self.send_error(200)  # 注意此出抛出了错误

    def on_finish(self):
        print "调用了on_finish()"
if __name__ == '__main__':
	tornado.options.parse_command_line()
	app = tornado.web.Application([
		     (r"/", InterfaceHandler),
                     url(r"/itcast", ItcastHandler,name="itcast_url")
		],
		debug=True)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.current().start()
