# coding:utf-8

import time 

def long_io():
    print '开始执行耗时操作'
    time.sleep(5)
    print '完成执行耗时操作'
    result = "io result"
    return result 


def req_a():
	print '开始处理请求a'
	ret = long_io()
	print ret 
	print '完成处理请求a'

def req_b():
	print '开始处理请求b'
	print '完成处理请求b'

def main():
    req_a()
    req_b()

if __name__ == '__main__':
	main()

