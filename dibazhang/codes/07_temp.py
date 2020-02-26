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
		#self.render("index.html",price1=100, price2=200)
		#self.render("index.html",abc="abcd")
		houses = [
		{
		    "price": 398,
		    "title": "宽窄巷子+160平大空间+文化保护区双地铁",
		    "score": 5,
		    "comments": 6,
		    "position": "北京市丰台区六里桥地铁"
		},
		{
		    "price": 398,
		    "title": "宽窄巷子+160平大空间+文化保护区双地铁",
		    "score": 5,
		    "comments": 6,
		    "position": "北京市丰台区六里桥地铁"
		},
		{
		    "price": 398,
		    "title": "宽窄巷子+160平大空间+文化保护区双地铁",
		    "score": 5,
		    "comments": 6,
		    "position": "北京市丰台区六里桥地铁"
		},
		{
		    "price": 398,
		    "title": "宽窄巷子+160平大空间+文化保护区双地铁",
		    "score": 5,
		    "comments": 6,
		    "position": "北京市丰台区六里桥地铁"
		},
		{
		    "price": 398,
		    "title": "宽窄巷子+160平大空间+文化保护区双地铁",
		    "score": 5,
		    "comments": 6,
		    "position": "北京市丰台区六里桥地铁"
		}]
		self.render("index.html", houses=houses)

class ItcastHandler(RequestHandler):
	def get(self):
	    self.write(dict(a=1,b=2))

if __name__ == '__main__':
 	tornado.options.parse_command_line()
 	current_path = os.path.dirname(__file__)
 	app = tornado.web.Application([
            (r"/", IndexHandler),
            (r"/itcast",ItcastHandler),
            (r"/(.*)", StaticFileHandler,{"path":os.path.join(current_path, "statics/html"),"default_filename":"index.html"}),
 	    ],
                
            #dict(a="abc",b="2")
 		static_path=os.path.join(current_path,"static"),
 		template_path=os.path.join(current_path,"template"),
 		debug=True)
 	http_server = tornado.httpserver.HTTPServer(app)
 	http_server.listen(options.port)
 	tornado.ioloop.IOLoop.current().start()
