from  socket import * 

udpSocket = socket(AF_INET, SOCK_DGRAM)

udpSock.bind(("",7788))

recvData = udpSocket.recvfrom(1024)

content,destInfo = recvData

print("content is  %s"%content)
print("content is %s"%content.decode("gb2312"))
