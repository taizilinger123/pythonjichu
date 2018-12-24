#coding:utf-8

import time
from  MyWebServer  import  HTTPServer

class Application(object):
    """框架的核心部分，也就是框架的主题程序，框架是通用的"""
    def __init__(self, urls):
         # 设置路由信息
         self.urls = urls

    def __call__(self, env, start_response):
        #env.get("PATH_INFO")获取字典的值，字典的值可以不存在env["PATH_INFO"]字典的键必须存在
         path = env.get("PATH_INFO", "/")
         for url, handler in self.urls:
             if path == url:
               return  handler(env, start_response)

         # 代表未找到路由信息，404错误
         status = "404 Not Found"
         headers = []
         start_response(status, headers)
         return "not found"

def show_ctime(env, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)

    return time.ctime()

def say_hello(env, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)

    return "hello itcast"

def say_haha(env, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)

    return "haha"



if __name__ == "__main__":
    urls = [
        ("/", show_ctime),
        ("/ctime", show_ctime),
        ("/sayhello", say_hello),
        ("/sayhaha", say_haha)
    ]
    app = Application(urls)
    http_server = HTTPServer(app)
    http_server.bind(8000)
    http_server.start()

# http://127.0.0.1:8000/sayhello
# http://127.0.0.1:8000
# http://127.0.0.1:8000/sayhaha
# http://127.0.0.1:8000/ctime