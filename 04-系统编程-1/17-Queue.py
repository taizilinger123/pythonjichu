#!/usr/bin/env python
# encoding: utf-8

from multiprocessing import Process, Queue
import os, time, random
def write(q):
	for value in ['A', 'B', 'C']:
		print("Put %s to queue..."%value)
		q.put(value)
		time.sleep(random.random())
# 读数据进程执⾏的代码:
def read(q):
	while True:
		if not q.empty():
			value = q.get(True)
			print('Get %s from queue.'%value)
			time.sleep(random.random())
		else:
			break
if __name__=='__main__':
	# ⽗进程创建Queue， 并传给各个⼦进程：
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	# 启动⼦进程pw， 写⼊:
	pw.start()
	# 等待pw结束:
	pw.join()
	# 启动⼦进程pr， 读取:
	pr.start()
	pr.join()
	# pr进程⾥是死循环， ⽆法等待其结束， 只能强⾏终⽌:
	print('')
	print('所有数据都写⼊并且读完')
