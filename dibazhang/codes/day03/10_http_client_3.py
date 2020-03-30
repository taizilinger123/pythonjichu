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
    @tornado.gen.coroutine
    def get(self):
        ips = ["14.130.112.24",
            "15.130.112.24",
            "16.130.112.24",
            "17.130.112.24"]
        rep1, rep2 = yield [self.get_ip_info(ips[0]), self.get_ip_info(ips[1])]
        rep34_dict = yield dict(rep3=self.get_ip_info(ips[2]), rep4=self.get_ip_info(ips[3]))
        self.write_response(ips[0], rep1) 
        self.write_response(ips[1], rep2) 
        self.write_response(ips[2], rep34_dict['rep3']) 
        self.write_response(ips[3], rep34_dict['rep4']) 

    def write_response(self, ip, response):
        self.write(ip) 
        self.write(":<br/>") 
        if 1 == response["ret"]:
            self.write(u"国家：%s 省份: %s 城市: %s<br/>" % (response["country"], response["province"], response["city"]))
        else:
            self.write("查询IP信息错误<br/>")

    @tornado.gen.coroutine
    def get_ip_info(self, ip):
        http = tornado.httpclient.AsyncHTTPClient()
        response = yield http.fetch("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=" + ip)
        if response.error:
            rep = {"ret:1"}
        else:
            rep = json.loads(response.body)
        raise tornado.gen.Return(rep)

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
