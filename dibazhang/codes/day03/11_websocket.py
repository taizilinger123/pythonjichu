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
import tornado.gen

from tornado.web import RequestHandler,url,StaticFileHandler
from tornado.options import define, options
from tornado.httpclient import AsyncHTTPClient
from tornado.websocket import WebSocketHandler

define("port", default=8001, type=int)

class  IndexHandler(RequestHandler):
    def get(self):
        self.render("webchat.html")

class ChatHandler(WebSocketHandler):

    users = [] 

    def open(self):
        for user in self.users:
            user.write_message("%s上线了" %self.request.remote_ip)
        self.users.append(self)

    def on_message(self, msg):
        for user in self.users:
            user.write_message("%s说:%s" %(self.request.remote_ip, msg))

    def on_close(self):
        self.users.remove(self)
        for user in self.users:
            user.write_message("%s下线了" % self.request.remote_ip)
    
    def check_origin(self, origin):
        return True


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
            (r"/chat", ChatHandler)
 	    ], **settings)
 	http_server = tornado.httpserver.HTTPServer(app)
 	http_server.listen(options.port)
 	tornado.ioloop.IOLoop.current().start()
