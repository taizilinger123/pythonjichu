#coding=utf-8
from multiprocessing import Queue
q=Queue(3) #初始化⼀个Queue对象， 最多可接收三条put消息
q.put("消息1")
q.put("消息2")
print(q.full()) #False
q.put("消息3")
print(q.full()) #True
#因为消息列队已满下⾯的try都会抛出异常， 第⼀个try会等待2秒后再抛出异常， 第⼆个Try会⽴
try:
	q.put("消息4",True,2)
except:
	print("消息列队已满， 现有消息数量:%s"%q.qsize())
try:
	q.put_nowait("消息4")
except:
	print("消息列队已满， 现有消息数量:%s"%q.qsize())
#推荐的⽅式， 先判断消息列队是否已满， 再写⼊
if not q.full():
	q.put_nowait("消息4")


#读取消息时， 先判断消息列队是否为空， 再读取
if not q.empty():
	for i in range(q.qsize()):
		print(q.get_nowait())
