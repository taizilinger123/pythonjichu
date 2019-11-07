from  socket  import *  

def main():
    udpSocket = socket(AF_INET,SOCK_DGRAM)
    udpSocket.bind(("",6789))#""自己的主机的所有IP都可以接受
   
    #收，打印
    while True:
        recvInfo = udpSocket.recvfrom(1024)
        print("[%s]:%s"%(str(recvInfo[1]),recvInfo[0].decode("gb2312")))

if __name__ == "__main__":
    main()
