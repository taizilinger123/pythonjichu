from threading import Thread
from socket import *

#1. 收数据，然后打印
def recvData():
    while True:
        recvInfo = udpSocket.recvfrom(1024)
        print(">>%s:%s"%(str(recvInfo[1]), recvInfo[0]))

#2. 检测键盘，发数据
def sendData():
    while True:
        sendInfo = input("<<")
        udpSocket.sendto(sendInfo.encode("gb2312"), (destIp, destPort))

udpSocket = None         #下面是返回对象就用None
destIp = ""              #下面返回字符串就用""   
destPort = 0             #下面返回数字就用0

def main():
    
    global udpSocket #下面用到就申明为global
    global destIp    #下面用到就申明为global
    global destPort  #下面用到就申明为global

    destIp = input("对方的ip:")   #返回字符串   
    destPort = int(input("对方的port:"))  #返回数字

    udpSocket = socket(AF_INET, SOCK_DGRAM)  #是返回对象
    udpSocket.bind(("", 4567))

    tr = Thread(target=recvData)
    ts = Thread(target=sendData)

    tr.start()
    ts.start()

    tr.join()
    ts.join()

if __name__ == "__main__":
    main()

