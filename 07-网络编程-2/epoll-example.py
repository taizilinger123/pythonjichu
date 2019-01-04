import	socket 
import	select
#创建套接字 
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#设置可以重复使⽤绑定的信息 
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#绑定本机信息 
s.bind(("",7788))
#变为被动 
s.listen(10)
#创建⼀个epoll对象 
epoll=select.epoll()
#测试，⽤来打印套接字对应的⽂件描述符
#	print	s.fileno()


#print	select.EPOLLIN|select.EPOLLET
#注册事件到epoll中 
#epoll.register(fd[,	eventmask])
#注意，如果fd已经注册过，则会发⽣异常 
#将创建的套接字添加到epoll的事件监听中 
epoll.register(s.fileno(),select.EPOLLIN|select.EPOLLET)
connections={} 
addresses={}
#循环等待客户端的到来或者对⽅发送数据
while	True:
  #epoll进⾏fd扫描的地⽅--未指定超时时间则为阻塞等待			
  epoll_list=epoll.poll()
  #对事件进⾏判断				
  for fd,events in epoll_list:
	#print  fd 
        #print events
        #如果是socket创建的套接字被激活								
	if fd == s.fileno():								
            conn,addr=s.accept()
            print('有新的客户端到来%s'%str(addr))
            #将conn和addr信息分别保存起来				
            connections[conn.fileno()] = conn						
            addresses[conn.fileno()] = addr
            #向epoll中注册连接socket的可读事件				
            epoll.register(conn.fileno(), select.EPOLLIN | select.EPOLLET
        elif events == select.EPOLLIN:												
	     #从激活fd上接收												
	     recvData =	connections[fd].recv(1024)
         if  len(recvData)> 0:
               print('recv:%s'%recvData)						
         else:																
               #从epoll中移除该连接fd					
               epoll.unregister(fd)
               #server侧主动关闭该连接fd		
               connections[fd].close()
               print("%s---offline---"%str(addresses[fd]))

