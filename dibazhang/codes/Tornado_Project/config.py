# coding:utf-8

import os 

# Application配置参数
settings = {
    "static_path":os.path.join(os.path.dirname(__file__),"static"),
    "template_path":os.path.join(os.path.dirname(__file__),"template"),   
    "cookie_secret":"EEk7nxO9QgeKYyqf7co3MFb2HsYQO0SZj27faPdRrtY=",
    "xsrf_cookies":False,
    "debug":True,
}

# mysql 
mysql_options =dict(
	host="127.0.0.1",
	database="ihome",
	user="root",
	password="123456"   
)

# redis
redis_options =dict(
	host="127.0.0.1",
	port=6379
)

log_file = os.path.join(os.path.dirname(__file__),"logs/log")
log_level = "debug"
