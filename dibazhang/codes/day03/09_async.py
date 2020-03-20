# coding:utf-8

import time 
import thread

def long_io(cb):
	def fun(callback):
	    print '开始执行耗时操作'
	    time.sleep(5)
	    print '完成执行耗时操作'
	    result = "io result"
	    callback(result)
	thread.start_new_thread(fun,(cb,))

def on_finish(ret):
	print '开始执行回调函数'
	print ret 
	print '完成执行回调函数'

def req_a():
	print '开始处理请求a'
	long_io(on_finish)
	print '离开处理请求a'

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

