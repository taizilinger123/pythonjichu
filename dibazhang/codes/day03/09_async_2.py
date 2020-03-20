# coding:utf-8

import time 
import thread

gen = None

def long_io():
	def fun():
	    global gen 
	    print '开始执行耗时操作'
	    time.sleep(5)
	    print '完成执行耗时操作'
	    result = "io result"
	    try:
	    	gen.send(result)
	    except StopIteration:
	    	pass 
	thread.start_new_thread(fun,())

def gen_coroutine(f):
	def wrapper():
		global gen 
		gen = f()
		gen.next()
	return wrapper

@gen_coroutine
def req_a():
	print '开始处理请求a'
	ret = yield  long_io()
	print ret 
	print '完成处理请求a'

def req_b():
	print '开始处理请求b'
	time.sleep(2)
	print '完成处理请求b'

def main():
    req_a()
    req_b()
    while 1:
    	pass

if __name__ == '__main__':
	main()

