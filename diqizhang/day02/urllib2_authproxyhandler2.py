#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import os

# 获取系统环境变量的授权代理的账户和密码
proxyuser = os.environ.get("proxyuser")
proxypasswd = os.environ.get("proxypasswd")

# 授权的代理账户密码拼接
authproxy_handler = urllib2.ProxyHandler({"http" : proxyuser+":"+proxypasswd+"@114.215.104.49:16816"})
#authproxy_handler = urllib2.ProxyHandler({"http" : "114.215.104.49:16816"})

# 构建一个自定义的opener
opener = urllib2.build_opener(authproxy_handler)

# 构建请求
request = urllib2.Request("http://www.baidu.com/")

# 获取响应
response = opener.open(request)

# 打印内容
print response.read()


sige@sige1:~/pythonjichu/diqizhang/day02$ tail  -6   ~/.bashrc
alias py3="python3"
alias py2="python2"
proxyuser="mr_mao_hacker"
export proxyuser
proxypasswd="sffqry9r"
export proxypasswd
sige@sige1:~/pythonjichu/diqizhang/day02$ source   ~/.bashrc
sige@sige1:~/pythonjichu/diqizhang/day02$ cat  bash_profile.py 
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

name = os.environ.get("proxyuser")

print name
