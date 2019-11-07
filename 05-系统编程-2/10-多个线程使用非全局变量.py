from threading import Thread
import threading
import time

def test1():
    #注意：
    #   1. 全局变量在多个线程中　共享，为了保证正确运行需要锁
    #   2. 非全局变量在每个线程中　各有一份，不会共享，当然了不需要加锁
    name = threading.current_thread().name
    #esc---->选中要粘贴的部分x---->p
    print("----thread name is %s ----"%name)
    g_num = 100
    if name == "Thread-1": 
        g_num += 1
    else:
        time.sleep(2)
    print("--thread is %s----g_num=%d"%(name,g_num))

#def test2():
#    time.sleep(1)
#    g_num = 100
#    print("---test2---g_num=%d"%g_num)


p1 = Thread(target=test1)
p1.start()

p2 = Thread(target=test1)
p2.start()

#ipython3
#In [1]: import  threading 
#In [2]: threading.curr
#threading.currentThread   threading.current_thread  
#In [2]: threading.current_thread()
#Out[2]: <_MainThread(MainThread, started 140363634886400)>
#In [3]: threading.current_thread().name 
#Out[3]: 'MainThread'


#ipython3
#In [1]: import  threading
#In [2]: mutexA = threading.Lock()
#In [3]: mutexA.ac
#mutexA.acquire       mutexA.acquire_lock  
#In [3]: help(mutexA.acquire)
