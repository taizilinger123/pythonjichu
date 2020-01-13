#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import json
from  tornado.options  import  define, options
from tornado.web import RequestHandler, url 

tornado.options.define("port", type=int, default=8001, help="服务器端口")

class IndexHandler(RequestHandler):
    """主页处理类"""
    def post(self):
        """get请求方式"""
        #subject = self.get_query_argument("subject")
        # subject = self.get_query_argument("subject", "python")
        # query_args = self.get_query_arguments("q")
        # query_args = self.get_query_argument("q")
        #body_arg = self.get_body_argument("b")
        #body_args = self.get_body_arguments("b")
        #a = self.get_argument("a")
        #ags = self.get_arguments("a", strip=False)
        #self.write(str(ags))
        # print self.request.headers.get("Content-Type")
        # print self.request.body
        # json_data = self.request.body 
        # json_args = json.loads(json_data)
        print  type(self.request.files)
        print  self.request.files.keys()
        print  type(self.request.files["image1"])
        self.request.files["image1"][0]['body']
        self.write("ok")


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
       [(r"/", IndexHandler),
       ],
       debug = True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
