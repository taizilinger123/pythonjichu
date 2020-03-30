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

define("port", default=8001, type=int)

class  IndexHandler(RequestHandler):
    # @tornado.web.asynchronous
    # def get(self):
    #     client = AsyncHTTPClient()
    #     client.fetch("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=14.130.112.24",callback=self.on_response)

    # def on_response(self, resp):
    #     json_data = resp.body 
    #     data = json.loads(json_data)
    #     self.write(data.get("city", ""))
    #     self.finish()
    # @tornado.gen.coroutine
    # def get(self):
    #     client = AsyncHTTPClient()
    #     resp = yield client.fetch("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=14.130.112.24")
    #     json_data = resp.body 
    #     data = json.loads(json_data)
    #     self.write(data.get("city", ""))

    @tornado.gen.coroutine
    def get(self):
        city = yield self.get_ip_city()
        self.write(city) 

    @tornado.gen.coroutine
    def get_ip_city(self):
        client = AsyncHTTPClient()
        resp = yield client.fetch("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=14.130.112.24")
        json_data = resp.body 
        data = json.loads(json_data)
        #return data.get("city", "") 错误
        raise tornado.gen.Return(data.get("city", ""))

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
 	    ], **settings)
 	http_server = tornado.httpserver.HTTPServer(app)
 	http_server.listen(options.port)
 	tornado.ioloop.IOLoop.current().start()
