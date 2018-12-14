#coding=utf-8
from	gevent	import	monkey
import	gevent
import	urllib2
#有IO才做时需要这⼀句
monkey.patch_all()
def	myDownLoad(url):
    print('GET:	%s'	%	url)
    resp =	urllib2.urlopen(url)
    data =	resp.read()
    print('%d bytes received	from %s.'%(len(data), url))
gevent.joinall([
         gevent.spawn(myDownLoad,	'http://www.baidu.com/'),
         gevent.spawn(myDownLoad,	'http://www.itcast.cn/'),
         gevent.spawn(myDownLoad,	'http://www.itheima.com/'),
])

